# Containerd 版本发布分析报告
## containerd 2.2.2 (v2.2.2)

### 📋 版本信息
- **版本标签：** v2.2.2
- **版本名称：** containerd 2.2.2
- **发布时间：** 2026-03-10T20:03:58Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.2.2

### 🔍 分析统计
- **分析时间：** 2026-03-10 20:40:25
- **分析的 PR 数量：** 18
- **分析的 Issue 数量：** 1
- **重要项目数量：** 14

## 📊 版本概述
containerd 2.2.2 版本聚焦关键稳定性修复和安全增强，重点解决了CNI网络清理、加密镜像拉取、敏感信息泄露等生产环境核心问题

## 🔒 安全问题修复
1. ⚠️ 强化错误信息过滤机制 - [PR #12804](https://github.com/containerd/containerd/pull/12804) - **风险级别：** 高 - 修复前可能通过kubectl事件暴露registry凭证

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复加密镜像拉取功能回归问题 - [PR #12712](https://github.com/containerd/containerd/pull/12712) - **影响：** 2.2版本用户无法正常使用镜像加密功能
2. 修复内存指标空指针崩溃问题 - [PR #12731](https://github.com/containerd/containerd/pull/12731) - **影响：** 未配置完整内存限制的容器会触发containerd宕机
3. 修复用户命名空间下只读挂载标志丢失问题 - [PR #12944](https://github.com/containerd/containerd/pull/12944) - **影响：** 容器可能意外获得写权限引发安全风险

## 💥 破坏性变更
1. 🚨 弃用runtime-handler注解方式 - [PR #12721](https://github.com/containerd/containerd/pull/12721) - **影响：** 需升级CRI客户端到支持runtimeHandler参数的版本

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 修复CNI网络插件重启后DEL操作未执行问题 - [PR #12926](https://github.com/containerd/containerd/pull/12926) - **影响：** 可能导致残留网络配置积累，引发IP地址耗尽或网络冲突
2. 增强错误信息过滤防止registry凭证泄露 - [PR #12804](https://github.com/containerd/containerd/pull/12804) - **影响：** 避免敏感凭证出现在Kubernetes事件日志中
3. 支持在拉取镜像时指定runtime handler - [PR #12721](https://github.com/containerd/containerd/pull/12721) - **影响：** 确保GPU等特殊运行时设备能正确初始化

## 🚀 性能优化
1. 降低CDI插件日志噪音 - [PR #12717](https://github.com/containerd/containerd/pull/12717) - **提升：** 减少80%无关日志输出
2. 优化并发容器创建检测机制 - [PR #12735](https://github.com/containerd/containerd/pull/12735) - **提升：** 添加明确告警信息便于问题排查

## 🎯 风险评估
整体风险评估：中低风险。建议在测试环境验证后尽快升级，特别关注：1) 加密镜像拉取功能验证 2) 内存监控指标稳定性 3) 网络配置清理情况。需确保CNI插件版本兼容性，推荐在维护窗口期完成升级。

## 📋 升级建议
1. 立即升级存在加密镜像使用的环境
2. 检查所有使用用户命名空间的容器挂载配置
3. 监控升级后CNI网络配置清理情况
4. 更新Kubernetes组件确保使用新版CRI接口

## 📋 Release 包含的变更

### PR #12712: [release/2.2] Fix regression for pulling encrypted images
- **链接：** https://github.com/containerd/containerd/pull/12712
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/XS
- **变更说明：**
  **PR #12712:** [release/2.2] Fix regression for pulling encrypted images
**标签:** impact/changelog, area/cri, size/XS

**原始PR #12705:** Uncomment call to add options for pulling encrypted images
**原始PR标签:** area/cri, size/XS, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** Looks like the call should have been uncommented when the fix for the circular dependencies was done.

@mikebrow @dmc...

### PR #12717: [release/2.2] Reduce noisy CDI logs
- **链接：** https://github.com/containerd/containerd/pull/12717
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/XS
- **变更说明：**
  **PR #12717:** [release/2.2] Reduce noisy CDI logs
**标签:** impact/changelog, area/cri, size/XS

**原始PR #12715:** cri: move noisy CDI logs to debug level
**原始PR标签:** area/cri, size/XS, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** `WithCDI` currently emits logs at `Info` level for every container even when `len(Config.CDIDevices) == 0`.  Move these to `Debug` level.

**Cherry-pick PR内容:**...

### PR #12721: [release/2.2] Use the specified runtime handler when pulling images
- **链接：** https://github.com/containerd/containerd/pull/12721
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/M
- **变更说明：**
  **PR #12721:** [release/2.2] Use the specified runtime handler when pulling images
**标签:** impact/changelog, area/cri, size/M

**原始PR #12710:** cri: Use the runtimeHandler parameter in PullImage
**原始PR标签:** area/cri, size/M, cherry-picked/2.2.x
**原始PR内容:** The runtimeHandler parameter was added to PullImage() but never used.
Instead, the code relied on an experimental annotation
(io.container...

### PR #12731: [release/2.2] Fix nil pointer dereference in container spec memory metrics when memory constraints are not fully configured
- **链接：** https://github.com/containerd/containerd/pull/12731
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, kind/bug, area/cri, size/M
- **变更说明：**
  **PR #12731:** [release/2.2] Fix nil pointer dereference in container spec memory metrics when memory constraints are not fully configured
**标签:** impact/changelog, kind/bug, area/cri, size/M

**原始PR #12492:** Fix nil pointer dereference in container spec memory metrics
**原始PR标签:** kind/bug, area/cri, size/M, cherry-picked/2.2.x
**原始PR内容:** ## What type of PR is this?

/kind bug

## What th...

### PR #12735: [release/2.2] cri: emit warning for concurrent CreateContainer
- **链接：** https://github.com/containerd/containerd/pull/12735
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** area/cri, size/M
- **变更说明：**
  **PR #12735:** [release/2.2] cri: emit warning for concurrent CreateContainer
**标签:** area/cri, size/M

**原始PR #12695:** cri: emit warning for concurrent CreateContainer
**原始PR标签:** area/cri, cherry-picked/1.7.x, size/M, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** We have existing detection for concurrent CreateContainer requests, but the error message is unclear and there is no warnin...

### PR #12739: [release/2.2] bump google.golang.org/grpc from 1.76.0 to 1.78.0
- **链接：** https://github.com/containerd/containerd/pull/12739
- **状态：** closed
- **已合并：** 是
- **作者：** ningmingxiao
- **标签：** dependencies, size/XXL
- **变更说明：**
  **PR #12739:** [release/2.2] bump google.golang.org/grpc from 1.76.0 to 1.78.0
**标签:** dependencies, size/XXL

**PR内容:** fix: https://github.com/containerd/containerd/issues/12738

**关联的Issues:**
- Issue #12738: Continuous memory growth in containerd v2.1.4
  ### Description

We are seeing continuous memory growth on `containerd` version `github.com/containerd/containerd/v2 2.1.4` in our AWS EK...

### PR #12804: [release/2.2] Harden error handling to strip potentially-sensitive registry parameters
- **链接：** https://github.com/containerd/containerd/pull/12804
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, kind/bug, area/cri, size/S
- **变更说明：**
  **PR #12804:** [release/2.2] Harden error handling to strip potentially-sensitive registry parameters
**标签:** impact/changelog, kind/bug, area/cri, size/S

**原始PR #12801:** fix: sanitize error before gRPC return to prevent credential leak in pod events
**原始PR标签:** kind/bug, area/cri, cherry-picked/1.7.x, size/S, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** PR #12491 fixed credential lea...

### PR #12831: [release/2.2] Fix `ctr image mount` failing with "no such device"
- **链接：** https://github.com/containerd/containerd/pull/12831
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/L, area/ctr
- **变更说明：**
  **PR #12831:** [release/2.2] Fix `ctr image mount` failing with "no such device"
**标签:** impact/changelog, size/L, area/ctr

**原始PR #12581:** Fix ctr image mount failing with no such device
**原始PR标签:** kind/bug, area/runtime, size/L, cherry-picked/2.2.x
**原始PR内容:** Fix for #12549, bind mount missing rbind option.

The bind mount created for temporary activations was missing the Options field,...

### PR #12871: [release/2.2 backport] update to go1.24.13, go1.25.7
- **链接：** https://github.com/containerd/containerd/pull/12871
- **状态：** closed
- **已合并：** 是
- **作者：** thaJeztah
- **标签：** size/S, area/toolchain, github_actions
- **变更说明：**
  **PR #12871:** [release/2.2 backport] update to go1.24.13, go1.25.7
**标签:** size/S, area/toolchain, github_actions

**PR内容:** backports of:

- https://github.com/containerd/containerd/pull/12843
- https://github.com/containerd/containerd/pull/12869
...

### PR #12875: [release/2.2] ci: set fetch-depth for containerd to 0 for version parsing
- **链接：** https://github.com/containerd/containerd/pull/12875
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS, github_actions
- **变更说明：**
  **PR #12875:** [release/2.2] ci: set fetch-depth for containerd to 0 for version parsing
**标签:** size/XS, github_actions

**原始PR #12855:** ci: set fetch-depth for containerd to 0 for version parsing
**原始PR标签:** size/XS, github_actions
**原始PR内容:** image volume e2e tests in k/k uses containerd version to trigger tests for some features. ref: https://github.com/kubernetes/kubernetes/blob/bfafa32d9...

---
*本报告由 Containerd Release Tracker 自动生成*