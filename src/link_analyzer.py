"""Intelligent link analysis module for chain-style analysis of PRs and issues."""

import re
from typing import Dict, List, Set, Optional, Tuple
from dataclasses import dataclass, field

from .github_client import GitHubClient, PRInfo, IssueInfo, ReleaseInfo
from .config import AnalysisConfig


@dataclass
class AnalysisResult:
    """Result of link analysis."""
    release_info: ReleaseInfo
    analyzed_prs: Dict[int, PRInfo] = field(default_factory=dict)
    analyzed_issues: Dict[int, IssueInfo] = field(default_factory=dict)
    important_items: List[Tuple[str, str, str]] = field(default_factory=list)  # (type, title, reason)
    analysis_summary: str = ""


class LinkAnalyzer:
    """Intelligent link analyzer for GitHub releases."""
    
    def __init__(self, github_client: GitHubClient, config: AnalysisConfig):
        self.github_client = github_client
        self.config = config
    
    def analyze_release(self, release_info: ReleaseInfo) -> AnalysisResult:
        """Perform comprehensive analysis of a release."""
        result = AnalysisResult(release_info=release_info)
        
        # Extract initial PR numbers from release body
        pr_numbers = self.github_client.extract_pr_numbers_from_text(release_info.body)
        
        # Analyze PRs and follow links
        analyzed_prs = set()
        analyzed_issues = set()
        
        for pr_number in pr_numbers[:self.config.max_links_to_analyze]:
            self._analyze_pr_chain(pr_number, result, analyzed_prs, analyzed_issues)
        
        # Identify important items
        self._identify_important_items(result)
        
        return result
    
    def _analyze_pr_chain(self, pr_number: int, result: AnalysisResult, 
                         analyzed_prs: Set[int], analyzed_issues: Set[int]) -> None:
        """Analyze a PR and follow its chain of related PRs and issues."""
        if pr_number in analyzed_prs:
            return
        
        pr_info = self.github_client.get_pr_info(pr_number)
        if not pr_info:
            return
        
        analyzed_prs.add(pr_number)
        result.analyzed_prs[pr_number] = pr_info
        
        # 如果是 cherry-pick，同时获取原始 PR（用于更完整的分析）
        if pr_info.cherry_pick_from and pr_info.cherry_pick_from not in analyzed_prs:
            print(f"🍒 PR #{pr_number} is cherry-picked from #{pr_info.cherry_pick_from}, fetching original PR...")
            self._analyze_pr_chain(pr_info.cherry_pick_from, result, analyzed_prs, analyzed_issues)
        
        # Extract related PR numbers from PR body and title
        related_prs = self.github_client.extract_pr_numbers_from_text(
            f"{pr_info.title} {pr_info.body}"
        )
        
        # Extract related issue numbers
        related_issues = self.github_client.extract_issue_numbers_from_text(
            f"{pr_info.title} {pr_info.body}"
        )
        
        # Analyze related issues
        for issue_number in related_issues:
            if issue_number not in analyzed_issues:
                self._analyze_issue(issue_number, result, analyzed_issues)
        
        # Follow related PRs (limit depth to avoid infinite loops)
        if len(analyzed_prs) < self.config.max_links_to_analyze:
            for related_pr in related_prs:
                if related_pr != pr_number:  # Avoid self-reference
                    self._analyze_pr_chain(related_pr, result, analyzed_prs, analyzed_issues)
    
    def _analyze_issue(self, issue_number: int, result: AnalysisResult, 
                      analyzed_issues: Set[int]) -> None:
        """Analyze an issue."""
        if issue_number in analyzed_issues:
            return
        
        issue_info = self.github_client.get_issue_info(issue_number)
        if not issue_info:
            return
        
        analyzed_issues.add(issue_number)
        result.analyzed_issues[issue_number] = issue_info
    
    def _identify_important_items(self, result: AnalysisResult) -> None:
        """Identify important PRs and issues based on keywords and patterns."""
        important_items = []
        
        # Check PRs for important keywords
        for pr_number, pr_info in result.analyzed_prs.items():
            importance_reasons = self._check_importance(
                f"{pr_info.title} {pr_info.body}", pr_info.labels
            )
            if importance_reasons:
                important_items.append((
                    "PR", 
                    f"#{pr_number}: {pr_info.title}",
                    "; ".join(importance_reasons)
                ))
        
        # Check issues for important keywords
        for issue_number, issue_info in result.analyzed_issues.items():
            importance_reasons = self._check_importance(
                f"{issue_info.title} {issue_info.body}", issue_info.labels
            )
            if importance_reasons:
                important_items.append((
                    "Issue", 
                    f"#{issue_number}: {issue_info.title}",
                    "; ".join(importance_reasons)
                ))
        
        result.important_items = important_items
    
    def _check_importance(self, text: str, labels: List[str]) -> List[str]:
        """Check if text or labels contain important keywords."""
        reasons = []
        text_lower = text.lower()
        
        # Check for important keywords in text
        for keyword in self.config.important_keywords:
            if keyword.lower() in text_lower:
                reasons.append(f"Contains '{keyword}'")
        
        # Check for important labels
        important_labels = ['security', 'critical', 'urgent', 'bug', 'regression']
        for label in labels:
            if any(important_label in label.lower() for important_label in important_labels):
                reasons.append(f"Has label '{label}'")
        
        # Check for version patterns that might indicate backports or cherry-picks
        if re.search(r'cherry.?pick|backport', text_lower):
            reasons.append("Cherry-pick or backport")
        
        # Check for panic or crash patterns
        if re.search(r'panic|crash|segfault|sigsegv', text_lower):
            reasons.append("Potential crash issue")
        
        # Check for performance issues
        if re.search(r'performance|slow|timeout|hang', text_lower):
            reasons.append("Performance related")
        
        return reasons
    
    def generate_summary(self, result: AnalysisResult) -> str:
        """Generate a summary of the analysis."""
        summary_parts = []
        
        summary_parts.append(f"Release: {result.release_info.name} ({result.release_info.tag_name})")
        summary_parts.append(f"Published: {result.release_info.published_at}")
        summary_parts.append(f"Analyzed PRs: {len(result.analyzed_prs)}")
        summary_parts.append(f"Analyzed Issues: {len(result.analyzed_issues)}")
        summary_parts.append(f"Important Items: {len(result.important_items)}")
        
        if result.important_items:
            summary_parts.append("\nImportant Items:")
            for item_type, title, reason in result.important_items:
                summary_parts.append(f"- {item_type}: {title} ({reason})")
        
        result.analysis_summary = "\n".join(summary_parts)
        return result.analysis_summary
