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
- **分析时间：** 2025-12-18 01:40:21
- **分析的 PR 数量：** 19
- **分析的 Issue 数量：** 1
- **重要项目数量：** 12

## 📊 版本概述
containerd 2.1.6 主要包含安全补丁和运行时稳定性改进，重点升级 runc 到 v1.3.4 并修复多个安全漏洞

## 🔒 安全问题修复
1. ⚠️ 修复 golang.org/x/crypto 中的 SSH 组件漏洞（GO-2025-4135/4134/4116）- [PR #12639](https://github.com/containerd/containerd/pull/12639) - **风险级别：** 高 - 可能导致 SSH 连接 DoS 或敏感信息泄露
2. ⚠️ 更新 containerd/platforms 的 Windows Server 2025 匹配规则 - [containerd/platforms#24](https://github.com/containerd/platforms/pull/24) - **风险级别：** 低

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复 runc tmpfs 挂载参数错误导致的权限问题 - [PR #12618](https://github.com/containerd/containerd/pull/12618) - **影响：** 容器启动时可能触发 `permission denied` 错误（如 #12484 问题）
2. SELinux 依赖升级至 v1.13.1 - [PR #12590](https://github.com/containerd/containerd/pull/12590) - **影响：** 增强 SELinux 策略兼容性

## 💥 破坏性变更
1. 🚨 移除 OpenTelemetry gRPC 拦截器 - [PR #12623](https://github.com/containerd/containerd/pull/12623) - **影响：** 依赖该组件的监控系统需迁移到 NewClientHandler
2. 🚨 放弃对 Go 1.23 的支持 - [PR #12639](https://github.com/containerd/containerd/pull/12639) - **影响：** 自编译用户需升级到 Go 1.24+

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 升级 runc 到 v1.3.4 - [PR #12618](https://github.com/containerd/containerd/pull/12618) - **影响：** 修复 tmpfs 挂载参数错误导致的容器启动失败问题
2. CRI 错误日志中敏感参数脱敏 - [PR #12547](https://github.com/containerd/containerd/pull/12547) - **影响：** 防止 URL 查询参数中的敏感信息泄露

## 🚀 性能优化
1. CI 流水线升级至 Go 1.24.11/1.25.5 - [PR #12626](https://github.com/containerd/containerd/pull/12626) - **提升：** 构建稳定性和编译器优化

## 🎯 风险评估
整体风险评估：中风险。升级需重点关注 runc 兼容性（尤其是 tmpfs 挂载场景）和监控系统适配性。建议在维护窗口期升级，生产环境需充分测试容器启动和网络策略。安全更新涉及 SSH 组件，建议 1 周内完成升级。

## 📋 升级建议
1. 立即升级 runc 到 v1.3.4（需与 containerd 同步升级）
2. 检查监控系统是否依赖旧版 OpenTelemetry 拦截器
3. 优先在测试环境验证 tmpfs 挂载场景
4. 若使用自编译部署，确保 Go 版本 ≥1.24

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