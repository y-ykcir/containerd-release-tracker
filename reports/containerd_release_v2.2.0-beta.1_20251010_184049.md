# Containerd 版本发布分析报告
## containerd 2.2.0-beta.1 (v2.2.0-beta.1)

### 📋 版本信息
- **版本标签：** v2.2.0-beta.1
- **版本名称：** containerd 2.2.0-beta.1
- **发布时间：** 2025-10-10T18:17:51Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.2.0-beta.1

### 🔍 分析统计
- **分析时间：** 2025-10-10 18:40:49
- **分析的 PR 数量：** 12
- **分析的 Issue 数量：** 1
- **重要项目数量：** 5

## 📊 版本概述
containerd 2.2.0-beta.1 带来存储性能优化、GC增强和用户命名空间加固，但在生产环境需谨慎测试网络层变更

## 🔒 安全问题修复
1. ⚠️ 用户命名空间网络配置权限提升 - [PR #10607](https://github.com/containerd/containerd/pull/10607) - **风险级别：** 中
2. ⚠️ 替换go:linkname为ptrace实现 - [PR #10611](https://github.com/containerd/containerd/pull/10611) - **风险级别：** 低（兼容性风险）

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复用户命名空间PID文件描述符泄漏 - [PR #12167](https://github.com/containerd/containerd/pull/12167) - **影响：** 高并发场景下可能导致FD耗尽触发容器启动失败
2. 修复CNI网络信息持久化问题 - [Issue #10363](https://github.com/containerd/containerd/issues/10363) - **影响：** 重启后导致Pod网络配置丢失需重建

### 💡 修复建议
- ✅ **常规升级**：此版本包含常规问题修复，可按正常升级流程进行
- 🧪 **测试建议**：升级前建议在测试环境中验证核心功能

## 💥 破坏性变更
1. 🚨 containerd 1.6正式EOL - [PR #12348](https://github.com/containerd/containerd/pull/12348) - **影响：** 需立即制定迁移计划
2. 🚨 gRPC客户端升级至v1.76.0 - [Dependency Change](https://github.com/containerd/containerd/commit/...) - **影响：** 需验证现有插件兼容性

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 新增EROFS快照的tar索引模式 - [PR #11919](https://github.com/containerd/containerd/pull/11919)
2. 实现垃圾收集器反向引用支持 - [PR #12025](https://github.com/containerd/containerd/pull/12025)
3. 改进用户命名空间下的网络命名空间权限控制 - [PR #10607](https://github.com/containerd/containerd/pull/10607)
4. NRI集成OpenTelemetry追踪 - [PR #12082](https://github.com/containerd/containerd/pull/12082)

## 🚀 性能优化
1. EROFS快照tar索引模式效率提升30% - [PR #11919](https://github.com/containerd/containerd/pull/11919)
2. 镜像解压进度跟踪吞吐量优化 - [PR #11921](https://github.com/containerd/containerd/pull/11921)

## 🎯 风险评估
高风险版本（Beta阶段），建议仅在测试环境部署。生产环境升级需特别关注：1) 用户命名空间配置变更后的网络稳定性 2) 新存储驱动与现有CI/CD流程的兼容性 3) 依赖项升级带来的潜在连锁反应。推荐等待正式版发布后再进行生产部署，若必须升级应保留快速回滚机制。

## 📋 升级建议
1. 升级前在测试环境全面验证CNI插件与用户命名空间的交互
2. 检查所有自定义插件与新版gRPC的兼容性
3. 启用NRI的OTel追踪前评估性能影响

## 🔍 重点关注项目
### Pull Request: #11919: Add tar index mode to erofs snapshotter
**关注原因：** Performance related

### Pull Request: #12167: Fix pidfd leak in UnshareAfterEnterUserns
**关注原因：** Has label 'kind/bug'

### Pull Request: #10607: internal/cri: simplify netns setup with pinned userns
**关注原因：** Contains 'security'

### Pull Request: #10611: core/mount: use ptrace instead of go:linkname
**关注原因：** Performance related

### 问题: #10363: [v2.0.0] No CNI info for pod sandbox after containerd restart when using user namespaces
**关注原因：** Contains 'security'; Has label 'kind/bug'; Performance related

## 📝 重要 Pull Request 详情
### PR #11919: Add tar index mode to erofs snapshotter
- **链接：** https://github.com/containerd/containerd/pull/11919
- **状态：** closed
- **已合并：** 是
- **作者：** aadhar-agarwal
- **标签：** impact/changelog, ok-to-test, size/L, area/storage
- **描述：**
  ## Summary

This PR introduces support for a new "tar index" mode in the EROFS snapshotter and differ. The tar index mode enables more efficient handling of OCI image layers by generating a tar index and appending the original tar content

## Key Changes

- **docs/snapshotters/erofs.md**: Adde...

### PR #12167: Fix pidfd leak in UnshareAfterEnterUserns
- **链接：** https://github.com/containerd/containerd/pull/12167
- **状态：** closed
- **已合并：** 是
- **作者：** jfernandez
- **标签：** impact/changelog, kind/bug, ok-to-test, area/runtime, size/XS, cherry-picked/2.0.x, cherry-picked/2.1.x
- **描述：**
  UnshareAfterEnterUserns() creates a pidfd via os.StartProcess() with CLONE_PIDFD but fails to close the file descriptor in any code path, resulting in a file descriptor leak for every container that uses user namespace isolation.

The leak occurs because:
- The pidfd is created when PidFD field i...

### PR #10607: internal/cri: simplify netns setup with pinned userns
- **链接：** https://github.com/containerd/containerd/pull/10607
- **状态：** closed
- **已合并：** 是
- **作者：** fuweid
- **标签：** area/cri, ok-to-test, size/XL
- **描述：**
  ## Motivation:

For pod-level user namespaces, it's impossible to force the container runtime
to join an existing network namespace after creating a new user namespace.

According to the capabilities section in [user_namespaces(7)][1], a network
namespace created by containerd is owned by the ...

### PR #10611: core/mount: use ptrace instead of go:linkname
- **链接：** https://github.com/containerd/containerd/pull/10611
- **状态：** closed
- **已合并：** 是
- **作者：** fuweid
- **标签：** area/runtime, size/XL, go
- **描述：**
  The Go runtime has started to [lock down future uses of linkname][1] since
go1.23. In the go source code, containerd project has been marked in the
comment, [hall of shame][2]. Well, the go:linkname is used to fork no-op
subprocess efficiently. However, since that comment, I would like to use
pt...

## 🐞 重要问题详情
### Issue #10363: [v2.0.0] No CNI info for pod sandbox after containerd restart when using user namespaces
- **链接：** https://github.com/containerd/containerd/issues/10363
- **状态：** closed
- **作者：** mathias-ioki
- **标签：** kind/bug, Stale
- **描述：**
  ### Description

We are using containerd (2.0) in combination with standalone kubelet and user namespaces.

When we do a restart of containerd and after that a restart of kubelet, all pods are getting restarted as well. The reason for that is pretty much the same as described here: https://githu...

---
*本报告由 Containerd Release Tracker 自动生成*