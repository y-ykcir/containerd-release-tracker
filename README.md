# Containerd Release Tracker

一个自动化的 containerd 版本发布跟踪和分析工具，能够：

- 🔍 自动获取 containerd 最新版本发布信息
- 🤖 使用 AI 大模型分析发布内容和重要 bugfix
- 🔗 智能链式分析相关 PR 和 Issue
- 📢 自动发送如流群通知
- 📄 生成详细的分析报告

## 功能特性

### 核心功能
- **自动版本检测**: 通过 GitHub API 获取 containerd 最新版本
- **智能链接分析**: Agent 方式自动跟踪 PR 和 Issue 链接
- **AI 内容分析**: 使用百度千帆大模型分析发布内容
- **重要性识别**: 自动识别安全问题、性能改进、破坏性变更等
- **多渠道通知**: 支持如流群消息通知
- **详细报告**: 生成 Markdown 和 JSON 格式的分析报告

### 分析维度
- 关键技术变更和新功能
- 重要 bugfix（安全、性能、稳定性）
- 安全问题和漏洞修复
- 性能改进
- 破坏性变更（breaking changes）
- 风险评估和升级建议

## 安装和配置

### 1. 环境准备

```bash
# 克隆项目
git clone <repository-url>
cd containerd-release-tracker

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置设置

```bash
# 初始化配置
python main.py setup

# 编辑环境变量文件
cp .env.example .env
# 编辑 .env 文件，填入必要的 API token
```

### 3. 环境变量配置

在 `.env` 文件中配置以下变量：

```bash
# GitHub API Token (可选，用于提高 API 限制)
GITHUB_TOKEN=your_github_token_here

# 百度千帆 API Token (必需)
QIANFAN_TOKEN=your_qianfan_token_here

# 如流通知配置 (必需)
RULIU_ACCESS_TOKEN=your_ruliu_access_token_here
RULIU_TARGET_IDS=[11901701]
```

### 4. 测试配置

```bash
# 测试所有连接
python main.py test

# 查看当前配置
python main.py config-info
```

## 使用方法

### 命令行接口

```bash
# 运行完整分析（推荐）
python main.py analyze

# 只分析不发送通知
python main.py analyze --no-notification

# 只分析不生成报告
python main.py analyze --no-report

# 获取最新版本摘要
python main.py summary

# 发送测试通知
python main.py notify -m "测试消息"

# 测试所有连接
python main.py test

# 查看配置信息
python main.py config-info
```

### 典型工作流

1. **日常监控**:
   ```bash
   python main.py analyze
   ```

2. **快速检查**:
   ```bash
   python main.py summary
   ```

3. **测试配置**:
   ```bash
   python main.py test
   ```

## 配置文件

### config/config.yaml

主配置文件包含以下部分：

- `github`: GitHub API 配置
- `llm`: 大模型 API 配置
- `notification`: 通知配置
- `analysis`: 分析参数配置
- `reports`: 报告生成配置

### 重要配置项

```yaml
analysis:
  max_links_to_analyze: 10  # 最大分析链接数
  important_keywords:       # 重要关键词
    - "panic"
    - "deadlock"
    - "security"
    # ...

reports:
  output_dir: "reports"     # 报告输出目录
  include_full_analysis: true
```

## 输出文件

### 报告文件
- `reports/containerd_release_v2.1.4_20240101_120000.md` - Markdown 格式报告
- `reports/containerd_release_v2.1.4_20240101_120000.json` - JSON 格式数据

### 报告内容
- 执行摘要
- 关键变更
- 重要 bugfix
- 安全问题
- 性能改进
- 破坏性变更
- 风险评估
- 升级建议
- 详细的 PR/Issue 分析

## API 集成

### 百度千帆 API
使用 deepseek-r1 模型进行智能分析，需要有效的 API token。

### 如流通知 API
支持 Markdown 格式的群消息发送。

### GitHub API
获取 release、PR、Issue 信息，建议配置 token 以提高 API 限制。

## 开发和测试

### 运行测试

```bash
# 运行所有测试
pytest tests/

# 运行特定测试
pytest tests/test_github_client.py

# 运行测试并显示覆盖率
pytest tests/ --cov=src
```

### 项目结构

```
containerd-release-tracker/
├── src/                    # 源代码
│   ├── config.py          # 配置管理
│   ├── github_client.py   # GitHub API 客户端
│   ├── link_analyzer.py   # 链接分析器
│   ├── llm_analyzer.py    # LLM 分析器
│   ├── notifier.py        # 通知模块
│   ├── report_generator.py # 报告生成器
│   └── tracker.py         # 主跟踪器
├── tests/                  # 测试文件
├── config/                 # 配置文件
├── reports/               # 生成的报告
├── main.py               # CLI 入口
├── requirements.txt      # 依赖列表
└── README.md            # 说明文档
```

## 故障排除

### 常见问题

1. **GitHub API 限制**
   - 配置 GITHUB_TOKEN 以提高 API 限制
   - 检查网络连接

2. **LLM API 调用失败**
   - 验证 QIANFAN_TOKEN 是否正确
   - 检查 API 余额和权限

3. **如流通知失败**
   - 验证 RULIU_ACCESS_TOKEN 和 RULIU_TARGET_IDS
   - 检查网络连接和权限

### 调试模式

```bash
# 使用详细输出
python main.py -v analyze

# 测试单个组件
python main.py test
```

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个工具。

## 许可证

MIT License
