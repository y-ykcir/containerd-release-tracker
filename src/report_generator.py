"""Report generation module for creating detailed analysis reports."""

import os
import json
from datetime import datetime
from typing import Dict, Any
from pathlib import Path

from .config import ReportsConfig
from .llm_analyzer import LLMAnalysisResult
from .link_analyzer import AnalysisResult


class ReportGenerator:
    """Generate detailed analysis reports."""
    
    def __init__(self, config: ReportsConfig):
        self.config = config
        self._ensure_output_dir()
    
    def _ensure_output_dir(self):
        """Ensure output directory exists."""
        Path(self.config.output_dir).mkdir(parents=True, exist_ok=True)
    
    def generate_report(self, analysis_result: AnalysisResult, 
                       llm_result: LLMAnalysisResult) -> str:
        """Generate comprehensive analysis report."""
        release = analysis_result.release_info
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"containerd_release_{release.tag_name}_{timestamp}.md"
        filepath = os.path.join(self.config.output_dir, filename)
        
        # Generate report content
        content = self._generate_markdown_report(analysis_result, llm_result)
        
        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Also generate JSON report for programmatic access
        json_filename = f"containerd_release_{release.tag_name}_{timestamp}.json"
        json_filepath = os.path.join(self.config.output_dir, json_filename)
        self._generate_json_report(analysis_result, llm_result, json_filepath)
        
        print(f"Report generated: {filepath}")
        print(f"JSON data generated: {json_filepath}")
        
        return filepath
    
    def _generate_markdown_report(self, analysis_result: AnalysisResult, 
                                llm_result: LLMAnalysisResult) -> str:
        """Generate markdown report content."""
        release = analysis_result.release_info
        
        md_parts = []
        
        # Title and metadata
        md_parts.append(f"# Containerd Release Analysis Report")
        md_parts.append(f"## {release.name} ({release.tag_name})")
        md_parts.append("")
        md_parts.append("### Release Information")
        md_parts.append(f"- **Tag:** {release.tag_name}")
        md_parts.append(f"- **Name:** {release.name}")
        md_parts.append(f"- **Published:** {release.published_at}")
        md_parts.append(f"- **Author:** {release.author}")
        md_parts.append(f"- **Prerelease:** {release.prerelease}")
        md_parts.append(f"- **Draft:** {release.draft}")
        md_parts.append(f"- **URL:** {release.html_url}")
        md_parts.append("")
        
        # Analysis metadata
        md_parts.append("### Analysis Metadata")
        md_parts.append(f"- **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        md_parts.append(f"- **Analyzed PRs:** {len(analysis_result.analyzed_prs)}")
        md_parts.append(f"- **Analyzed Issues:** {len(analysis_result.analyzed_issues)}")
        md_parts.append(f"- **Important Items:** {len(analysis_result.important_items)}")
        md_parts.append("")
        
        # Executive Summary
        md_parts.append("## Executive Summary")
        if llm_result.summary:
            md_parts.append(llm_result.summary)
        else:
            md_parts.append("No AI-generated summary available.")
        md_parts.append("")
        
        # Key Changes
        if llm_result.key_changes:
            md_parts.append("## Key Changes")
            for i, change in enumerate(llm_result.key_changes, 1):
                md_parts.append(f"{i}. {change}")
            md_parts.append("")
        
        # Important Bugfixes
        if llm_result.important_bugfixes:
            md_parts.append("## Important Bugfixes")
            for i, bugfix in enumerate(llm_result.important_bugfixes, 1):
                md_parts.append(f"{i}. {bugfix}")
            md_parts.append("")
        
        # Security Issues
        if llm_result.security_issues:
            md_parts.append("## Security Issues")
            for i, security_issue in enumerate(llm_result.security_issues, 1):
                md_parts.append(f"{i}. ⚠️ {security_issue}")
            md_parts.append("")
        
        # Performance Improvements
        if llm_result.performance_improvements:
            md_parts.append("## Performance Improvements")
            for i, improvement in enumerate(llm_result.performance_improvements, 1):
                md_parts.append(f"{i}. {improvement}")
            md_parts.append("")
        
        # Breaking Changes
        if llm_result.breaking_changes:
            md_parts.append("## Breaking Changes")
            for i, breaking_change in enumerate(llm_result.breaking_changes, 1):
                md_parts.append(f"{i}. 🚨 {breaking_change}")
            md_parts.append("")
        
        # Risk Assessment
        if llm_result.risk_assessment:
            md_parts.append("## Risk Assessment")
            md_parts.append(llm_result.risk_assessment)
            md_parts.append("")
        
        # Recommendations
        if llm_result.recommendations:
            md_parts.append("## Recommendations")
            for i, recommendation in enumerate(llm_result.recommendations, 1):
                md_parts.append(f"{i}. {recommendation}")
            md_parts.append("")
        
        # Important Items from Link Analysis
        if analysis_result.important_items:
            md_parts.append("## Important Items Identified")
            for item_type, title, reason in analysis_result.important_items:
                md_parts.append(f"### {item_type}: {title}")
                md_parts.append(f"**Reason:** {reason}")
                md_parts.append("")
        
        # Detailed PR Analysis
        if self.config.include_pr_details and analysis_result.analyzed_prs:
            md_parts.append("## Detailed Pull Request Analysis")
            for pr_number, pr_info in analysis_result.analyzed_prs.items():
                md_parts.append(f"### PR #{pr_number}: {pr_info.title}")
                md_parts.append(f"- **URL:** {pr_info.url}")
                md_parts.append(f"- **State:** {pr_info.state}")
                md_parts.append(f"- **Merged:** {pr_info.merged}")
                md_parts.append(f"- **Author:** {pr_info.author}")
                md_parts.append(f"- **Created:** {pr_info.created_at}")
                if pr_info.merged_at:
                    md_parts.append(f"- **Merged:** {pr_info.merged_at}")
                if pr_info.labels:
                    md_parts.append(f"- **Labels:** {', '.join(pr_info.labels)}")
                if pr_info.body:
                    md_parts.append(f"- **Description:**")
                    md_parts.append(f"  {pr_info.body[:500]}{'...' if len(pr_info.body) > 500 else ''}")
                md_parts.append("")
        
        # Detailed Issue Analysis
        if self.config.include_issue_details and analysis_result.analyzed_issues:
            md_parts.append("## Detailed Issue Analysis")
            for issue_number, issue_info in analysis_result.analyzed_issues.items():
                md_parts.append(f"### Issue #{issue_number}: {issue_info.title}")
                md_parts.append(f"- **URL:** {issue_info.url}")
                md_parts.append(f"- **State:** {issue_info.state}")
                md_parts.append(f"- **Author:** {issue_info.author}")
                md_parts.append(f"- **Created:** {issue_info.created_at}")
                if issue_info.closed_at:
                    md_parts.append(f"- **Closed:** {issue_info.closed_at}")
                if issue_info.labels:
                    md_parts.append(f"- **Labels:** {', '.join(issue_info.labels)}")
                if issue_info.body:
                    md_parts.append(f"- **Description:**")
                    md_parts.append(f"  {issue_info.body[:500]}{'...' if len(issue_info.body) > 500 else ''}")
                md_parts.append("")
        
        # Original Release Notes
        md_parts.append("## Original Release Notes")
        md_parts.append("```")
        md_parts.append(release.body)
        md_parts.append("```")
        md_parts.append("")
        
        # Footer
        md_parts.append("---")
        md_parts.append("*This report was generated automatically by the Containerd Release Tracker.*")
        
        return "\n".join(md_parts)
    
    def _generate_json_report(self, analysis_result: AnalysisResult, 
                            llm_result: LLMAnalysisResult, filepath: str):
        """Generate JSON report for programmatic access."""
        data = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "tool": "containerd-release-tracker",
                "version": "1.0.0"
            },
            "release": {
                "tag_name": analysis_result.release_info.tag_name,
                "name": analysis_result.release_info.name,
                "body": analysis_result.release_info.body,
                "published_at": analysis_result.release_info.published_at,
                "prerelease": analysis_result.release_info.prerelease,
                "draft": analysis_result.release_info.draft,
                "html_url": analysis_result.release_info.html_url,
                "author": analysis_result.release_info.author
            },
            "analysis": {
                "summary": llm_result.summary,
                "key_changes": llm_result.key_changes,
                "important_bugfixes": llm_result.important_bugfixes,
                "security_issues": llm_result.security_issues,
                "performance_improvements": llm_result.performance_improvements,
                "breaking_changes": llm_result.breaking_changes,
                "recommendations": llm_result.recommendations,
                "risk_assessment": llm_result.risk_assessment
            },
            "statistics": {
                "analyzed_prs": len(analysis_result.analyzed_prs),
                "analyzed_issues": len(analysis_result.analyzed_issues),
                "important_items": len(analysis_result.important_items)
            },
            "important_items": [
                {
                    "type": item_type,
                    "title": title,
                    "reason": reason
                }
                for item_type, title, reason in analysis_result.important_items
            ]
        }
        
        if self.config.include_pr_details:
            data["prs"] = {
                str(pr_number): {
                    "title": pr_info.title,
                    "url": pr_info.url,
                    "body": pr_info.body,
                    "state": pr_info.state,
                    "merged": pr_info.merged,
                    "created_at": pr_info.created_at,
                    "merged_at": pr_info.merged_at,
                    "author": pr_info.author,
                    "labels": pr_info.labels
                }
                for pr_number, pr_info in analysis_result.analyzed_prs.items()
            }
        
        if self.config.include_issue_details:
            data["issues"] = {
                str(issue_number): {
                    "title": issue_info.title,
                    "url": issue_info.url,
                    "body": issue_info.body,
                    "state": issue_info.state,
                    "created_at": issue_info.created_at,
                    "closed_at": issue_info.closed_at,
                    "author": issue_info.author,
                    "labels": issue_info.labels
                }
                for issue_number, issue_info in analysis_result.analyzed_issues.items()
            }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
