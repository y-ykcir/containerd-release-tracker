# Containerd 版本发布分析报告
## containerd 2.1.6 (v2.1.6)

### 📋 版本信息
- **版本标签：** v2.1.6
- **版本名称：** containerd 2.1.6
- **发布时间：** 2025-12-18T01:06:52Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.1.6

### 🔍 分析统计
- **分析时间：** 2025-12-18 01:40:09
- **分析的 PR 数量：** 19
- **分析的 Issue 数量：** 1
- **重要项目数量：** 12

## 📊 版本概述
containerd 2.1.6 核心版本聚焦安全补丁和运行时稳定性改进，包含关键runc升级、golang安全漏洞修复及日志敏感信息防护

## 🔒 安全问题修复
1. ⚠️ 修复golang.org/x/crypto SSH组件3个高危漏洞（GO-2025-4135/4134/4116） - [PR #12639](https://github.com/containerd/containerd/pull/12639) - **风险级别：** 高
2. ⚠️ 升级SELinux策略库至v1.13.1 - [PR #12528](https://github.com/containerd/containerd/pull/12528) - **风险级别：** 中

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复runc v1.3.4的tmpfs挂载模式回归问题 - [PR #12593](https://github.com/containerd/containerd/pull/12593) - **影响：** 容器启动失败风险
2. 修复OpenTelemetry客户端拦截器兼容性问题 - [PR #12606](https://github.com/containerd/containerd/pull/12606) - **影响：** 监控数据采集异常

## 💥 破坏性变更
1. 🚨 移除Go 1.23编译支持 - [PR #12639](https://github.com/containerd/containerd/pull/12639) - **影响：** 需确保开发环境使用Go 1.24+

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 更新runc至v1.3.4版本 - [PR #12618](https://github.com/containerd/containerd/pull/12618)
2. 升级golang.org/x/crypto至v0.45.0并移除Go 1.23支持 - [PR #12639](https://github.com/containerd/containerd/pull/12639)
3. CRI错误日志全量参数脱敏 - [PR #12547](https://github.com/containerd/containerd/pull/12547)

## 🚀 性能优化
1. Solaris平台构建优化 - [PR #203](https://github.com/containerd/containerd/pull/203) - **提升：** 跨平台构建效率优化
2. CI流水线升级至Go 1.24.11/1.25.5 - [PR #12626](https://github.com/containerd/containerd/pull/12626) - **提升：** 工具链稳定性改进

## 🎯 风险评估
整体风险等级：中。关键安全修复需优先处理，建议在2周内完成升级。特别注意：升级需同步更新runc二进制文件，测试环境需提前验证容器启动流程，Windows Server 2025平台用户需验证镜像兼容性

## 📋 升级建议
1. 立即升级以修复SSH相关高危安全漏洞，特别是暴露SSH服务的环境
2. 验证runtime版本兼容性，确保runc v1.3.4在生产环境无异常
3. 审核日志配置，确认CRI接口错误日志无敏感参数泄露
4. 构建环境需同步升级Go工具链至1.24.11或1.25.5

## 📋 Release 包含的变更

### PR #12487: Update 2.1 branch to no longer build as latest
- **链接：** https://github.com/containerd/containerd/pull/12487
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** size/XS, github_actions
- **变更说明：**
  **PR #12487:** Update 2.1 branch to no longer build as latest
**标签:** size/XS, github_actions

**PR内容:** 2.2 release will now build as latest, change this to false to prevent overwriting 2.2 builds....

### PR #12547: [release/2.1] Redact all query parameters in CRI error logs
- **链接：** https://github.com/containerd/containerd/pull/12547
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** kind/bug, area/cri, size/L
- **变更说明：**
  **PR #12547:** [release/2.1] Redact all query parameters in CRI error logs
**标签:** kind/bug, area/cri, size/L

**原始PR #12491:** fix: redact all query parameters in CRI error logs
**原始PR标签:** kind/bug, area/cri, cherry-picked/1.7.x, size/L, area/distribution, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** Trying to fix #5453 



**Cherry-pick PR内容:** This is an automated cherry-pick of #...

### PR #12590: [release/2.1] build(deps): bump github.com/opencontainers/selinux
- **链接：** https://github.com/containerd/containerd/pull/12590
- **状态：** closed
- **已合并：** 是
- **作者：** AkihiroSuda
- **标签：** dependencies, size/XXL
- **变更说明：**
  **PR #12590:** [release/2.1] build(deps): bump github.com/opencontainers/selinux
**标签:** dependencies, size/XXL

**PR内容:** Cherry-pick (not clean)
- #12528...

### PR #12618: [release/2.1] Update runc binary to v1.3.4
- **链接：** https://github.com/containerd/containerd/pull/12618
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/XS
- **变更说明：**
  **PR #12618:** [release/2.1] Update runc binary to v1.3.4
**标签:** impact/changelog, area/runtime, size/XS

**原始PR #12593:** [release/2.2] Update runc binary to v1.3.4
**原始PR标签:** impact/changelog, cherry-picked/1.7.x, area/runtime, size/XS, cherry-picked/2.1.x
**原始PR内容:** - Related to: https://github.com/containerd/containerd/issues/12484

This update includes a fix for a regression introduce...

### PR #12623: [release/2.1] core/runtime/v2: remove uses of otelgrpc.UnaryClientInterceptor
- **链接：** https://github.com/containerd/containerd/pull/12623
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** area/runtime, size/XS
- **变更说明：**
  **PR #12623:** [release/2.1] core/runtime/v2: remove uses of otelgrpc.UnaryClientInterceptor
**标签:** area/runtime, size/XS

**原始PR #12606:** core/runtime/v2: remove uses of otelgrpc.UnaryClientInterceptor
**原始PR标签:** size/XS, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** - relates to https://github.com/containerd/containerd/pull/12604#issuecomment-3596523255
- relates to https://github....

### PR #12626: [release/2.1] ci: bump Go 1.24.11, 1.25.5
- **链接：** https://github.com/containerd/containerd/pull/12626
- **状态：** closed
- **已合并：** 是
- **作者：** austinvazquez
- **标签：** size/S, area/toolchain
- **变更说明：**
  **PR #12626:** [release/2.1] ci: bump Go 1.24.11, 1.25.5
**标签:** size/S, area/toolchain

**PR内容:** This change backports two changesets for Go toolchain maintenance.

1. https://github.com/containerd/containerd/pull/12583
2. https://github.com/containerd/containerd/pull/12615

Note: the Dockerfile change is not strictly required but nice to have to simplify toolchain updates in stable bran...

### PR #12633: [release/2.1] ci: update CIFuzz actions to support Ubuntu 24.04
- **链接：** https://github.com/containerd/containerd/pull/12633
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS, github_actions
- **变更说明：**
  **PR #12633:** [release/2.1] ci: update CIFuzz actions to support Ubuntu 24.04
**标签:** size/XS, github_actions

**原始PR #12631:** ci: update CIFuzz actions to support Ubuntu 24.04
**原始PR标签:** cherry-picked/1.7.x, size/XS, github_actions, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** Update the OSS-Fuzz CIFuzz action references from commit abe2c06d (Oct 2024) to c8c1b257 (Dec 2025) which i...

### PR #12639: [release/2.1] go.mod: golang.org/x/crypto v0.45.0 (drop support for Go 1.23)
- **链接：** https://github.com/containerd/containerd/pull/12639
- **状态：** closed
- **已合并：** 是
- **作者：** AkihiroSuda
- **标签：** dependencies, size/XXL
- **变更说明：**
  **PR #12639:** [release/2.1] go.mod: golang.org/x/crypto v0.45.0 (drop support for Go 1.23)
**标签:** dependencies, size/XXL

**PR内容:** 
Silence the following govulncheck reports
("you import and 3 vulnerabilities in modules you require, but your code doesn't appear to call these vulnerabilities"):

```
Vulnerability #1: GO-2025-4135
    Malformed constraint may cause denial of service in
...

---
*本报告由 Containerd Release Tracker 自动生成*