"""GitHub API client for fetching containerd release information."""

import re
import requests
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from urllib.parse import urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor, as_completed

from .config import GitHubConfig


@dataclass
class PRInfo:
    """Pull request information."""
    number: int
    title: str
    url: str
    body: str
    state: str
    merged: bool
    created_at: str
    merged_at: Optional[str]
    author: str
    labels: List[str]
    cherry_pick_from: Optional[int] = None  # 原始 PR 编号（如果是 cherry-pick）


@dataclass
class IssueInfo:
    """Issue information."""
    number: int
    title: str
    url: str
    body: str
    state: str
    created_at: str
    closed_at: Optional[str]
    author: str
    labels: List[str]


@dataclass
class ReleaseInfo:
    """Release information."""
    tag_name: str
    name: str
    body: str
    published_at: str
    prerelease: bool
    draft: bool
    html_url: str
    author: str


class GitHubClient:
    """GitHub API client."""
    
    # Compile regex patterns once at class level for better performance
    _PR_PATTERNS = [
        re.compile(r'#(\d+)'),  # #12345
        re.compile(r'https://github\.com/[^/]+/[^/]+/pull/(\d+)'),  # Full PR URLs
    ]
    _ISSUE_PATTERNS = [
        re.compile(r'https://github\.com/[^/]+/[^/]+/issues/(\d+)'),  # Full issue URLs
        re.compile(r'(?:fixes?|closes?|resolves?)\s+#(\d+)', re.IGNORECASE),  # "fixes #123"
    ]
    _CHERRY_PICK_PATTERNS = [
        re.compile(r'automated cherry-pick of #(\d+)', re.IGNORECASE),
        re.compile(r'cherry-pick of #(\d+)', re.IGNORECASE),
        re.compile(r'backport.*#(\d+)', re.IGNORECASE),
        re.compile(r'backport.*https://github\.com/[^/]+/[^/]+/pull/(\d+)', re.IGNORECASE),
    ]
    
    def __init__(self, config: GitHubConfig):
        self.config = config
        self.session = requests.Session()
        if config.token:
            self.session.headers.update({
                'Authorization': f'token {config.token}',
                'Accept': 'application/vnd.github.v3+json'
            })
        # Configure connection pooling for better performance
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=config.pool_connections,
            pool_maxsize=config.pool_maxsize,
            max_retries=config.max_retries
        )
        self.session.mount('https://', adapter)
        self.session.mount('http://', adapter)
        # Simple in-memory cache to avoid duplicate API calls
        self._pr_cache: Dict[int, Optional[PRInfo]] = {}
        self._issue_cache: Dict[int, Optional[IssueInfo]] = {}
    
    def get_latest_release(self, include_prerelease: bool = False) -> Optional[ReleaseInfo]:
        """Get the latest release information."""
        if include_prerelease:
            # Get all releases and find the latest one (including prereleases)
            url = f"{self.config.api_url}/repos/{self.config.repo_owner}/{self.config.repo_name}/releases"
            try:
                response = self.session.get(url)
                response.raise_for_status()
                releases = response.json()

                if not releases:
                    return None

                # Return the first release (most recent)
                data = releases[0]
            except requests.RequestException as e:
                print(f"Error fetching releases: {e}")
                return None
        else:
            # Get only the latest stable release
            url = f"{self.config.api_url}/repos/{self.config.repo_owner}/{self.config.repo_name}/releases/latest"
            try:
                response = self.session.get(url)
                response.raise_for_status()
                data = response.json()
            except requests.RequestException as e:
                print(f"Error fetching latest release: {e}")
                return None

        return ReleaseInfo(
            tag_name=data['tag_name'],
            name=data['name'],
            body=data['body'],
            published_at=data['published_at'],
            prerelease=data['prerelease'],
            draft=data['draft'],
            html_url=data['html_url'],
            author=data['author']['login']
        )
    
    def extract_pr_numbers_from_text(self, text: str) -> List[int]:
        """Extract PR numbers from release text."""
        pr_numbers = set()
        for pattern in self._PR_PATTERNS:
            matches = pattern.findall(text)
            pr_numbers.update(int(match) for match in matches)
        
        return sorted(list(pr_numbers))
    
    def _detect_cherry_pick(self, body: str) -> Optional[int]:
        """检测 PR 是否是 cherry-pick，返回原始 PR 编号。"""
        if not body:
            return None
        
        for pattern in self._CHERRY_PICK_PATTERNS:
            match = pattern.search(body)
            if match:
                return int(match.group(1))
        
        return None
    
    def get_pr_info(self, pr_number: int) -> Optional[PRInfo]:
        """Get detailed information about a pull request."""
        # Check cache first
        if pr_number in self._pr_cache:
            return self._pr_cache[pr_number]
        
        url = f"{self.config.api_url}/repos/{self.config.repo_owner}/{self.config.repo_name}/pulls/{pr_number}"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            
            body = data['body'] or ''
            # 检测是否是 cherry-pick
            cherry_pick_from = self._detect_cherry_pick(body)
            
            pr_info = PRInfo(
                number=data['number'],
                title=data['title'],
                url=data['html_url'],
                body=body,
                state=data['state'],
                merged=data['merged'],
                created_at=data['created_at'],
                merged_at=data.get('merged_at'),
                author=data['user']['login'],
                labels=[label['name'] for label in data['labels']],
                cherry_pick_from=cherry_pick_from
            )
            # Cache the result
            self._pr_cache[pr_number] = pr_info
            return pr_info
        except requests.RequestException as e:
            # 404 错误可能是正常的（PR 不存在或已删除），使用 debug 级别
            if '404' in str(e):
                print(f"⚠️  PR #{pr_number} not found (may have been deleted or is invalid)")
            else:
                print(f"❌ Error fetching PR {pr_number}: {e}")
            # Cache None to avoid retrying failed requests
            self._pr_cache[pr_number] = None
            return None
    
    def extract_issue_numbers_from_text(self, text: str) -> List[int]:
        """Extract issue numbers from text."""
        issue_numbers = set()
        for pattern in self._ISSUE_PATTERNS:
            matches = pattern.findall(text)
            issue_numbers.update(int(match) for match in matches)
        
        return sorted(list(issue_numbers))
    
    def get_issue_info(self, issue_number: int) -> Optional[IssueInfo]:
        """Get detailed information about an issue."""
        # Check cache first
        if issue_number in self._issue_cache:
            return self._issue_cache[issue_number]
        
        url = f"{self.config.api_url}/repos/{self.config.repo_owner}/{self.config.repo_name}/issues/{issue_number}"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Skip if this is actually a PR (GitHub treats PRs as issues)
            if 'pull_request' in data:
                self._issue_cache[issue_number] = None
                return None
            
            issue_info = IssueInfo(
                number=data['number'],
                title=data['title'],
                url=data['html_url'],
                body=data['body'] or '',
                state=data['state'],
                created_at=data['created_at'],
                closed_at=data.get('closed_at'),
                author=data['user']['login'],
                labels=[label['name'] for label in data['labels']]
            )
            # Cache the result
            self._issue_cache[issue_number] = issue_info
            return issue_info
        except requests.RequestException as e:
            # 404 错误可能是正常的（Issue 不存在或已删除），使用 debug 级别
            if '404' in str(e):
                print(f"⚠️  Issue #{issue_number} not found (may have been deleted or is invalid)")
            else:
                print(f"❌ Error fetching issue {issue_number}: {e}")
            # Cache None to avoid retrying failed requests
            self._issue_cache[issue_number] = None
            return None
    
    def get_prs_batch(self, pr_numbers: List[int], max_workers: int = 5) -> Dict[int, Optional[PRInfo]]:
        """Fetch multiple PRs concurrently for better performance.
        
        Args:
            pr_numbers: List of PR numbers to fetch
            max_workers: Maximum number of concurrent requests
            
        Returns:
            Dictionary mapping PR numbers to PRInfo objects (or None if fetch failed)
        """
        results = {}
        
        # Separate cached and uncached PRs
        uncached_prs = [pr_num for pr_num in pr_numbers if pr_num not in self._pr_cache]
        for pr_num in pr_numbers:
            if pr_num in self._pr_cache:
                results[pr_num] = self._pr_cache[pr_num]
        
        if not uncached_prs:
            return results
        
        # Fetch uncached PRs concurrently
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_pr = {executor.submit(self.get_pr_info, pr_num): pr_num for pr_num in uncached_prs}
            
            for future in as_completed(future_to_pr):
                pr_num = future_to_pr[future]
                try:
                    pr_info = future.result()
                    results[pr_num] = pr_info
                except Exception as e:
                    print(f"❌ Error fetching PR #{pr_num} in batch: {e}")
                    results[pr_num] = None
        
        return results
    
    def get_issues_batch(self, issue_numbers: List[int], max_workers: int = 5) -> Dict[int, Optional[IssueInfo]]:
        """Fetch multiple issues concurrently for better performance.
        
        Args:
            issue_numbers: List of issue numbers to fetch
            max_workers: Maximum number of concurrent requests
            
        Returns:
            Dictionary mapping issue numbers to IssueInfo objects (or None if fetch failed)
        """
        results = {}
        
        # Separate cached and uncached issues
        uncached_issues = [issue_num for issue_num in issue_numbers if issue_num not in self._issue_cache]
        for issue_num in issue_numbers:
            if issue_num in self._issue_cache:
                results[issue_num] = self._issue_cache[issue_num]
        
        if not uncached_issues:
            return results
        
        # Fetch uncached issues concurrently
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_issue = {executor.submit(self.get_issue_info, issue_num): issue_num for issue_num in uncached_issues}
            
            for future in as_completed(future_to_issue):
                issue_num = future_to_issue[future]
                try:
                    issue_info = future.result()
                    results[issue_num] = issue_info
                except Exception as e:
                    print(f"❌ Error fetching Issue #{issue_num} in batch: {e}")
                    results[issue_num] = None
        
        return results
