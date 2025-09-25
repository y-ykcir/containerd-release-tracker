# Containerd 版本发布分析报告
## containerd 2.2.0-beta.0 (v2.2.0-beta.0)

### 📋 版本信息
- **版本标签：** v2.2.0-beta.0
- **版本名称：** containerd 2.2.0-beta.0
- **发布时间：** 2025-09-18T17:05:00Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.2.0-beta.0

### 🔍 分析统计
- **分析时间：** 2025-09-25 04:09:58
- **分析的 PR 数量：** 10
- **分析的 Issue 数量：** 1
- **重要项目数量：** 5

## 📊 版本概述
containerd 2.2.0-beta.0 引入了GC反向引用支持、EROFS性能优化和关键资源泄漏修复，同时升级关键依赖版本

## 🔒 安全问题修复
1. ⚠️ 用户命名空间网络配置加固 - [PR #10607](https://github.com/containerd/containerd/pull/10607) - **风险级别：** 中 - 修复用户命名空间挂载/sys失败问题

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复用户命名空间场景下的pidfd泄漏 - [PR #12167](https://github.com/containerd/containerd/pull/12167) - **影响：** 每个容器启动泄漏1个文件描述符，高密度环境可能导致FD耗尽
2. 修复CNI网络信息丢失问题 - [Issue #10363](https://github.com/containerd/containerd/issues/10363) - **影响：** containerd重启后导致Kubernetes Pod强制重建

### 💡 修复建议
- ✅ **常规升级**：此版本包含常规问题修复，可按正常升级流程进行
- 🧪 **测试建议**：升级前建议在测试环境中验证核心功能

## 💥 破坏性变更
1. 🚨 Go客户端接口变更 - [PR #12245](https://github.com/containerd/containerd/pull/12245) - **影响：** 需要适配新的fs.FS接口和os.OpenRoot方法
2. 🚨 Kubernetes依赖升级到v0.34.1 - [Dependency](https://github.com/containerd/containerd/commit/...) - **影响：** 需验证与现有K8s集群版本的兼容性

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 垃圾回收器支持反向引用 - [PR #12025](https://github.com/containerd/containerd/pull/12025) - 允许对象被尚未存在的对象引用，提升临时对象管理能力
2. EROFS快照器新增tar索引模式 - [PR #11919](https://github.com/containerd/containerd/pull/11919) - 优化OCI镜像层处理流程

## 🚀 性能优化
1. EROFS快照器tar索引模式 - [PR #11919](https://github.com/containerd/containerd/pull/11919) - **提升：** 减少镜像层存储开销和加载时间
2. tar解包进度跟踪优化 - [PR #11921](https://github.com/containerd/containerd/pull/11921) - **提升：** 增强大规模镜像分发过程的可观测性

## 🎯 风险评估
中风险升级：
1. Beta版本包含未稳定功能（如WASM插件支持）
2. 关键运行时依赖项（如runc/CNI）需同步验证
3. 建议生产环境等待正式版发布，紧急修复场景可选择性cherry-pick关键修复（如#12167）

## 📋 升级建议
1. 优先在测试环境验证用户命名空间相关功能（特别是CNI网络配置）
2. 监控升级后的文件描述符使用情况，确认pidfd泄漏修复效果
3. 使用EROFS快照器的团队应评估tar索引模式的性能收益

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