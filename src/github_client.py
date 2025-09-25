"""GitHub API client for fetching containerd release information."""

import re
import requests
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from urllib.parse import urlparse, parse_qs

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
    
    def __init__(self, config: GitHubConfig):
        self.config = config
        self.session = requests.Session()
        if config.token:
            self.session.headers.update({
                'Authorization': f'token {config.token}',
                'Accept': 'application/vnd.github.v3+json'
            })
    
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
        # Pattern to match GitHub PR links like #12345 or full URLs
        patterns = [
            r'#(\d+)',  # #12345
            r'https://github\.com/[^/]+/[^/]+/pull/(\d+)',  # Full PR URLs
        ]
        
        pr_numbers = set()
        for pattern in patterns:
            matches = re.findall(pattern, text)
            pr_numbers.update(int(match) for match in matches)
        
        return sorted(list(pr_numbers))
    
    def get_pr_info(self, pr_number: int) -> Optional[PRInfo]:
        """Get detailed information about a pull request."""
        url = f"{self.config.api_url}/repos/{self.config.repo_owner}/{self.config.repo_name}/pulls/{pr_number}"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            
            return PRInfo(
                number=data['number'],
                title=data['title'],
                url=data['html_url'],
                body=data['body'] or '',
                state=data['state'],
                merged=data['merged'],
                created_at=data['created_at'],
                merged_at=data.get('merged_at'),
                author=data['user']['login'],
                labels=[label['name'] for label in data['labels']]
            )
        except requests.RequestException as e:
            print(f"Error fetching PR {pr_number}: {e}")
            return None
    
    def extract_issue_numbers_from_text(self, text: str) -> List[int]:
        """Extract issue numbers from text."""
        # Pattern to match GitHub issue links
        patterns = [
            r'https://github\.com/[^/]+/[^/]+/issues/(\d+)',  # Full issue URLs
            r'(?:fixes?|closes?|resolves?)\s+#(\d+)',  # "fixes #123"
        ]
        
        issue_numbers = set()
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            issue_numbers.update(int(match) for match in matches)
        
        return sorted(list(issue_numbers))
    
    def get_issue_info(self, issue_number: int) -> Optional[IssueInfo]:
        """Get detailed information about an issue."""
        url = f"{self.config.api_url}/repos/{self.config.repo_owner}/{self.config.repo_name}/issues/{issue_number}"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Skip if this is actually a PR (GitHub treats PRs as issues)
            if 'pull_request' in data:
                return None
            
            return IssueInfo(
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
        except requests.RequestException as e:
            print(f"Error fetching issue {issue_number}: {e}")
            return None
