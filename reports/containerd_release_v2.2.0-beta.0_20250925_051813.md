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
- **分析时间：** 2025-09-25 05:18:13
- **分析的 PR 数量：** 10
- **分析的 Issue 数量：** 1
- **重要项目数量：** 5

## 📊 版本概述
Error calling LLM API: HTTPSConnectionPool(host='qianfan.baidubce.com', port=443): Read timed out. (read timeout=60)

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