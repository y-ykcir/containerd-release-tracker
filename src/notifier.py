"""Notification module for sending alerts to Ruliu (如流)."""

import json
import requests
from datetime import datetime
from typing import List, Optional

from .config import NotificationConfig
from .llm_analyzer import LLMAnalysisResult
from .link_analyzer import AnalysisResult


class RuliuNotifier:
    """Ruliu notification client."""
    
    def __init__(self, config: NotificationConfig):
        self.config = config
    
    def send_release_notification(self, analysis_result: AnalysisResult, 
                                llm_result: LLMAnalysisResult) -> bool:
        """Send release analysis notification to Ruliu."""
        # Generate markdown content
        md_content = self._generate_markdown_content(analysis_result, llm_result)
        
        # Send notification
        return self._send_markdown_message(md_content)
    
    def _generate_markdown_content(self, analysis_result: AnalysisResult,
                                 llm_result: LLMAnalysisResult) -> str:
        """Generate concise markdown content for notification."""
        release = analysis_result.release_info

        md_parts = []

        # Header with key info
        md_parts.append(f"# 🚀 Containerd {release.tag_name} 发布")

        # Release type indicator
        if release.prerelease:
            md_parts.append("**🧪 预发布版本 (Beta/RC)**")
        else:
            md_parts.append("**✅ 正式版本**")

        md_parts.append(f"**发布时间:** {release.published_at[:10]}")
        md_parts.append("")

        # Executive Summary (most important)
        if llm_result.summary:
            md_parts.append("## 📋 版本概要")
            md_parts.append(llm_result.summary)
            md_parts.append("")

        # Key Changes with links
        if llm_result.key_changes:
            md_parts.append("## 🔄 主要变更")
            for change in llm_result.key_changes[:4]:  # Top 4 changes
                md_parts.append(f"- {change}")
            md_parts.append("")

        # Critical Security Issues
        if llm_result.security_issues:
            md_parts.append("## 🔒 安全更新")
            for issue in llm_result.security_issues[:2]:  # Top 2 security issues
                md_parts.append(f"- {issue}")
            md_parts.append("")

        # Important Bugfixes
        if llm_result.important_bugfixes:
            md_parts.append("## 🐛 重要修复")
            for bugfix in llm_result.important_bugfixes[:3]:  # Top 3 bugfixes
                md_parts.append(f"- {bugfix}")
            md_parts.append("")

        # Performance Improvements
        if llm_result.performance_improvements:
            md_parts.append("## ⚡ 性能优化")
            for improvement in llm_result.performance_improvements[:2]:  # Top 2 improvements
                md_parts.append(f"- {improvement}")
            md_parts.append("")

        # Breaking Changes
        if llm_result.breaking_changes:
            md_parts.append("## ⚠️ 破坏性变更")
            for change in llm_result.breaking_changes:
                md_parts.append(f"- {change}")
            md_parts.append("")

        # Risk assessment
        if llm_result.risk_assessment:
            md_parts.append("## 📊 风险评估")
            md_parts.append(f"> {llm_result.risk_assessment}")
            md_parts.append("")

        # Upgrade recommendations
        if llm_result.recommendations:
            md_parts.append("## 💡 升级建议")
            for i, rec in enumerate(llm_result.recommendations[:3], 1):  # Top 3 recommendations
                md_parts.append(f"{i}. {rec}")
            md_parts.append("")
        
        # Quick stats
        md_parts.append("## 📈 分析统计")
        md_parts.append(f"- 分析了 **{len(analysis_result.analyzed_prs)}** 个 PR")
        md_parts.append(f"- 分析了 **{len(analysis_result.analyzed_issues)}** 个 Issue")
        md_parts.append(f"- 识别出 **{len(analysis_result.important_items)}** 个重要项目")
        md_parts.append("")

        # Links
        md_parts.append("## 🔗 相关链接")
        md_parts.append(f"- [Release 页面]({release.html_url})")
        md_parts.append("")

        # Footer
        md_parts.append("---")
        md_parts.append(f"*🤖 由 Containerd Release Tracker 自动生成 | {datetime.now().strftime('%Y-%m-%d %H:%M')}*")

        return "\n".join(md_parts)


    
    def _send_markdown_message(self, content: str) -> bool:
        """Send markdown message to Ruliu."""
        if not self.config.access_token or not self.config.target_ids:
            print("Warning: Ruliu configuration incomplete, skipping notification")
            return False
        
        # Construct webhook URL with access token
        webhook_url = f"{self.config.webhook_url}?access_token={self.config.access_token}"
        
        # Prepare message body
        body_content = {
            "message": {
                "header": {
                    "toid": self.config.target_ids
                },
                "body": [
                    {
                        "type": "MD",
                        "content": content
                    }
                ]
            }
        }
        
        try:
            response = requests.post(
                webhook_url,
                headers={"Content-Type": "application/json"},
                json=body_content,
                timeout=60
            )
            response.raise_for_status()
            
            print(f"[{datetime.now()}] Ruliu notification sent successfully")
            return True
            
        except requests.RequestException as e:
            print(f"[{datetime.now()}] Failed to send Ruliu notification: {e}")
            return False
    
    def send_simple_message(self, message: str) -> bool:
        """Send a simple text message to Ruliu."""
        return self._send_markdown_message(message)
    
    def test_connection(self) -> bool:
        """Test Ruliu connection with a simple message."""
        test_message = f"🧪 Containerd Release Tracker Test - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        return self.send_simple_message(test_message)
