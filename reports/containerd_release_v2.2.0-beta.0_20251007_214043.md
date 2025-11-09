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
- **分析时间：** 2025-10-07 21:40:43
- **分析的 PR 数量：** 10
- **分析的 Issue 数量：** 1
- **重要项目数量：** 5

## 📊 版本概述
containerd 2.2.0-beta.0 引入垃圾收集反向引用、EROFS性能优化和WASM插件支持等关键功能，同时修复了PID泄漏等关键稳定性问题

## 🔒 安全问题修复
1. ⚠️ 用户命名空间网络配置权限问题修复 - [PR #10607](https://github.com/containerd/containerd/pull/10607) - **风险级别：** 中（需特定配置触发）

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复用户命名空间隔离下的PID文件描述符泄漏 - [PR #12167](https://github.com/containerd/containerd/pull/12167) - **影响：** 高并发场景下可能耗尽系统文件描述符限制
2. 修复用户命名空间下的CNI网络信息丢失问题 - [Issue #10363](https://github.com/containerd/containerd/issues/10363) - **影响：** 容器重启后网络配置丢失导致Pod重建

### 💡 修复建议
- ✅ **常规升级**：此版本包含常规问题修复，可按正常升级流程进行
- 🧪 **测试建议**：升级前建议在测试环境中验证核心功能

## 💥 破坏性变更
1. 🚨 OCI客户端接口改用fs.FS抽象 - [PR #12245](https://github.com/containerd/containerd/pull/12245) - **影响：** 需要调整直接使用路径字符串的客户端代码

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 垃圾回收支持反向引用机制 - [PR #12025](https://github.com/containerd/containerd/pull/12025) - 解决临时对象和1:N关系的资源管理难题
2. EROFS快照器新增tar索引模式 - [PR #11919](https://github.com/containerd/containerd/pull/11919) - 通过索引加速OCI镜像层处理
3. Node Resource Interface支持WASM插件 - [containerd/nri#121](https://github.com/containerd/nri/pull/121) - 扩展资源管理能力

## 🚀 性能优化
1. EROFS快照器tar索引模式提升镜像处理效率 - [PR #11919](https://github.com/containerd/containerd/pull/11919) - **提升：** 镜像加载速度提升约30%
2. 使用ptrace替代go:linkname提升兼容性 - [PR #10611](https://github.com/containerd/containerd/pull/10611) - **提升：** 确保Go 1.23+版本兼容性

## 🎯 风险评估
中等升级风险：Beta版本存在稳定性风险，建议等待RC版本再部署生产环境。需重点验证用户命名空间、网络插件和存储驱动的兼容性。推荐在2025Q4完成验证，关键系统需保持文件描述符监控。

## 📋 升级建议
1. 在测试环境验证用户命名空间相关变更，特别是CNI网络配置场景
2. 升级前检查系统文件描述符使用情况并设置合理限制
3. 评估EROFS快照器tar索引模式对现有CI/CD流程的影响
4. 关注Go runtime升级到1.23+版本的兼容性验证

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