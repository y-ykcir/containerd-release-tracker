"""LLM-based analysis module using Baidu Qianfan API."""

import json
import requests
from typing import Dict, List, Optional
from dataclasses import dataclass

from .config import LLMConfig
from .link_analyzer import AnalysisResult


@dataclass
class LLMAnalysisResult:
    """Result of LLM analysis."""
    summary: str
    key_changes: List[str]
    important_bugfixes: List[str]
    security_issues: List[str]
    performance_improvements: List[str]
    breaking_changes: List[str]
    recommendations: List[str]
    risk_assessment: str


class LLMAnalyzer:
    """LLM analyzer using Baidu Qianfan API."""
    
    def __init__(self, config: LLMConfig):
        self.config = config
    
    def analyze_release(self, analysis_result: AnalysisResult) -> LLMAnalysisResult:
        """Analyze release using LLM."""
        # Prepare context for LLM
        context = self._prepare_context(analysis_result)
        
        # Get LLM analysis
        llm_response = self._call_llm(context)
        
        # Parse LLM response
        return self._parse_llm_response(llm_response)
    
    def _prepare_context(self, analysis_result: AnalysisResult) -> str:
        """Prepare context for LLM analysis."""
        context_parts = []
        
        # Release information
        release = analysis_result.release_info
        context_parts.append(f"# Containerd Release Analysis: {release.name}")
        context_parts.append(f"Tag: {release.tag_name}")
        context_parts.append(f"Published: {release.published_at}")
        context_parts.append(f"Release Notes:\n{release.body}")
        
        # Important items identified by link analyzer
        if analysis_result.important_items:
            context_parts.append("\n## Important Items Identified:")
            for item_type, title, reason in analysis_result.important_items:
                context_parts.append(f"- {item_type}: {title} (Reason: {reason})")
        
        # Detailed PR information
        if analysis_result.analyzed_prs:
            context_parts.append("\n## Analyzed Pull Requests:")
            for pr_number, pr_info in analysis_result.analyzed_prs.items():
                context_parts.append(f"\n### PR #{pr_number}: {pr_info.title}")
                context_parts.append(f"State: {pr_info.state}, Merged: {pr_info.merged}")
                context_parts.append(f"Author: {pr_info.author}")
                if pr_info.labels:
                    context_parts.append(f"Labels: {', '.join(pr_info.labels)}")
                if pr_info.body:
                    # Truncate long PR bodies
                    body = pr_info.body[:1000] + "..." if len(pr_info.body) > 1000 else pr_info.body
                    context_parts.append(f"Description: {body}")
        
        # Detailed issue information
        if analysis_result.analyzed_issues:
            context_parts.append("\n## Analyzed Issues:")
            for issue_number, issue_info in analysis_result.analyzed_issues.items():
                context_parts.append(f"\n### Issue #{issue_number}: {issue_info.title}")
                context_parts.append(f"State: {issue_info.state}")
                context_parts.append(f"Author: {issue_info.author}")
                if issue_info.labels:
                    context_parts.append(f"Labels: {', '.join(issue_info.labels)}")
                if issue_info.body:
                    # Truncate long issue bodies
                    body = issue_info.body[:1000] + "..." if len(issue_info.body) > 1000 else issue_info.body
                    context_parts.append(f"Description: {body}")
        
        return "\n".join(context_parts)
    
    def _call_llm(self, context: str) -> str:
        """Call Baidu Qianfan LLM API."""
        system_prompt = """你是一个专业的云原生和容器技术专家，特别擅长分析containerd等容器运行时的技术变更。

请分析提供的containerd release信息，生成适合发送到企业群聊的总结性报告。

**分析要求：**
1. 每个重要变更必须包含对应的PR/Issue链接
2. 用简洁明了的语言描述技术影响
3. 突出对生产环境的实际影响
4. 提供明确的行动建议

**输出格式要求：**
请以JSON格式返回，每个字段都必须是字符串或字符串数组，格式如下：

```json
{
  "summary": "一句话总结这个版本的核心价值和主要变更",
  "key_changes": [
    "变更描述 - [PR #12345](https://github.com/containerd/containerd/pull/12345)",
    "另一个变更 - [Issue #12346](https://github.com/containerd/containerd/issues/12346)"
  ],
  "important_bugfixes": [
    "修复描述：具体问题和影响 - [PR #12347](链接) - **影响：** 生产环境影响说明",
    "另一个修复..."
  ],
  "security_issues": [
    "安全问题描述 - [PR #12348](链接) - **风险级别：** 高/中/低",
    "另一个安全问题..."
  ],
  "performance_improvements": [
    "性能改进描述 - [PR #12349](链接) - **提升：** 具体性能提升数据",
    "另一个性能改进..."
  ],
  "breaking_changes": [
    "破坏性变更描述 - [PR #12350](链接) - **影响：** 需要的迁移动作",
    "另一个破坏性变更..."
  ],
  "recommendations": [
    "针对生产环境的具体升级建议",
    "注意事项和最佳实践"
  ],
  "risk_assessment": "整体风险评估：升级风险级别、建议的升级时机、需要特别关注的方面"
}
```

**重要：**
- 所有PR/Issue引用必须使用完整的GitHub链接格式
- 每个技术变更都要说明对生产环境的具体影响
- 使用中文，但保持技术术语的准确性
- 重点突出需要立即关注的安全和稳定性问题"""

        payload = {
            "model": self.config.model,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": context
                }
            ],
            "max_tokens": self.config.max_tokens,
            "temperature": self.config.temperature
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.config.token}"
        }
        
        try:
            response = requests.post(
                self.config.api_url,
                headers=headers,
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content']
            else:
                return "Error: No response from LLM"
                
        except requests.RequestException as e:
            print(f"Error calling LLM API: {e}")
            return f"Error calling LLM API: {e}"
    
    def _parse_llm_response(self, response: str) -> LLMAnalysisResult:
        """Parse LLM response into structured result."""
        def ensure_string(value, default=""):
            """Ensure value is a string."""
            if isinstance(value, str):
                return value
            elif isinstance(value, (dict, list)):
                return str(value)
            else:
                return default

        def ensure_list(value, default=None):
            """Ensure value is a list of strings."""
            if default is None:
                default = []
            if isinstance(value, list):
                return [ensure_string(item) for item in value]
            elif isinstance(value, str):
                return [value]
            else:
                return default

        try:
            # Try to extract JSON from response
            json_start = response.find('{')
            json_end = response.rfind('}') + 1

            if json_start >= 0 and json_end > json_start:
                json_str = response[json_start:json_end]
                data = json.loads(json_str)

                return LLMAnalysisResult(
                    summary=ensure_string(data.get('summary', '')),
                    key_changes=ensure_list(data.get('key_changes', [])),
                    important_bugfixes=ensure_list(data.get('important_bugfixes', [])),
                    security_issues=ensure_list(data.get('security_issues', [])),
                    performance_improvements=ensure_list(data.get('performance_improvements', [])),
                    breaking_changes=ensure_list(data.get('breaking_changes', [])),
                    recommendations=ensure_list(data.get('recommendations', [])),
                    risk_assessment=ensure_string(data.get('risk_assessment', ''))
                )
            else:
                # Fallback: treat entire response as summary
                return LLMAnalysisResult(
                    summary=response,
                    key_changes=[],
                    important_bugfixes=[],
                    security_issues=[],
                    performance_improvements=[],
                    breaking_changes=[],
                    recommendations=[],
                    risk_assessment=""
                )

        except json.JSONDecodeError:
            # Fallback: treat entire response as summary
            return LLMAnalysisResult(
                summary=response,
                key_changes=[],
                important_bugfixes=[],
                security_issues=[],
                performance_improvements=[],
                breaking_changes=[],
                recommendations=[],
                risk_assessment=""
            )
