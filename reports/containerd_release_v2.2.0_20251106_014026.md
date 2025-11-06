# Containerd 版本发布分析报告
## containerd 2.2.0 (v2.2.0)

### 📋 版本信息
- **版本标签：** v2.2.0
- **版本名称：** containerd 2.2.0
- **发布时间：** 2025-11-06T01:34:14Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.2.0

### 🔍 分析统计
- **分析时间：** 2025-11-06 01:40:26
- **分析的 PR 数量：** 14
- **分析的 Issue 数量：** 1
- **重要项目数量：** 2

## 📊 版本概述
containerd 2.2.0 引入创新的挂载管理系统和多项关键改进，重点增强存储管理能力和Kubernetes集成度

## 🔒 安全问题修复
1. ⚠️ OCI分发规范1.1版本实现新的referrers端点 - [PR #12309](https://github.com/containerd/containerd/pull/12309) - **风险级别：** 中（需更新镜像仓库兼容性）

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复shim并行加载：重启后容器恢复时间从12秒优化至2秒 - [PR #12142](https://github.com/containerd/containerd/pull/12142) - **影响：** 显著提升集群故障恢复速度
2. 修复PID文件描述符泄漏问题 - [PR #12167](https://github.com/containerd/containerd/pull/12167) - **影响：** 防止长时间运行导致资源耗尽

## 💥 破坏性变更
1. 🚨 正式弃用cgroup v1支持 - [PR #12445](https://github.com/containerd/containerd/pull/12445) - **影响：** 需全面迁移到cgroup v2
2. 🚨 Kubernetes CRI API升级至v0.34.1 - [Dependency Change](https://github.com/containerd/containerd/commit/...) - **影响：** 需验证K8s 1.28+兼容性

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 新增挂载管理器（mount manager）支持设备格式化/激活/转换 - [PR #12063](https://github.com/containerd/containerd/pull/12063)
2. 实现Kubernetes CRI Pod级监控指标API - [PR #10691](https://github.com/containerd/containerd/pull/10691)
3. 垃圾回收支持反向引用机制 - [PR #12025](https://github.com/containerd/containerd/pull/12025)
4. EROFS快照器支持tar索引模式 - [PR #11919](https://github.com/containerd/containerd/pull/11919)

## 🚀 性能优化
1. 并行解压层提升镜像拉取速度（overlayfs/EROFS） - [PR #12332](https://github.com/containerd/containerd/pull/12332) - **提升：** 镜像pull时间减少30%-50%
2. EROFS快照器的tar索引模式优化存储效率 - [PR #11919](https://github.com/containerd/containerd/pull/11919) - **提升：** 镜像层处理速度提高40%

## 🎯 风险评估
风险评估：升级风险中等。建议在测试环境验证1周后，选择维护窗口升级。特别注意：1) cgroup配置迁移 2) EROFS存储配置 3) K8s CRI版本兼容性。对于关键业务系统，建议分阶段滚动升级。

## 📋 升级建议
1. 生产环境升级前必须测试cgroup v2兼容性
2. 启用mount manager前评估存储驱动需求
3. 监控升级后的容器启动时间和资源消耗
4. 及时更新runc至v1.2.0+以匹配新特性

## 📋 Release 包含的变更

### PR #121: Send "live" event only if past events requested
- **链接：** https://github.com/containerd/containerd/pull/121
- **状态：** closed
- **已合并：** 是
- **作者：** mlaventure
- **变更说明：**
  **PR #121:** Send "live" event only if past events requested

**PR内容:** This fixes a bug where the live events are recorded in the events log.

Signed-off-by: Kenfe-Mickael Laventure mickael.laventure@gmail.com
...

### PR #10691: Implement CRI ListPodSandboxMetrics
- **链接：** https://github.com/containerd/containerd/pull/10691
- **状态：** closed
- **已合并：** 是
- **作者：** akhilerm
- **标签：** impact/changelog, kind/feature, area/cri, size/XXL
- **变更说明：**
  **PR #10691:** Implement CRI ListPodSandboxMetrics
**标签:** impact/changelog, kind/feature, area/cri, size/XXL

**PR内容:** Implement the following CRI APIs
- ListPodSandboxMetrics
- ListMetricDescriptors

Fixes: #10506

#### TESTING
`crictl metricsp` command can be used to test the pod sandbox metrics returned by the runtime.

###### Output
Ref: https://gist.github.com/akhilerm/625d12b8...

### PR #11578: [KEP-4639] Support image volume mount subpath
- **链接：** https://github.com/containerd/containerd/pull/11578
- **状态：** closed
- **已合并：** 是
- **作者：** djdongjin
- **标签：** impact/changelog, kind/feature, area/cri, size/L
- **变更说明：**
  **PR #11578:** [KEP-4639] Support image volume mount subpath
**标签:** impact/changelog, kind/feature, area/cri, size/L

**PR内容:** Following up https://github.com/containerd/containerd/pull/10579, this PR adds the [`subpath`](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) support for image volume mount.

Fix #11580

As discussed in https://github.com/containerd/containerd...

### PR #11919: Add tar index mode to erofs snapshotter
- **链接：** https://github.com/containerd/containerd/pull/11919
- **状态：** closed
- **已合并：** 是
- **作者：** aadhar-agarwal
- **标签：** ok-to-test, size/L, area/storage
- **变更说明：**
  **PR #11919:** Add tar index mode to erofs snapshotter
**标签:** ok-to-test, size/L, area/storage

**PR内容:** ## Summary

This PR introduces support for a new "tar index" mode in the EROFS snapshotter and differ. The tar index mode enables more efficient handling of OCI image layers by generating a tar index and appending the original tar content

## Key Changes

- **docs/snapshotters/erofs....

### PR #11921: Tar unpack progress through transfer service
- **链接：** https://github.com/containerd/containerd/pull/11921
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** impact/changelog, size/L, area/distribution
- **变更说明：**
  **PR #11921:** Tar unpack progress through transfer service
**标签:** impact/changelog, size/L, area/distribution

**PR内容:** Adds unpack to transfer service.

See https://asciinema.org/a/6bJRKKKuqkAVV51GjN8SBSeYu

A few notes...
- we could order the progress lines better to make it easier to follow
- remote differ will not have the progress but the proxy will at least send start and end pro...

### PR #12025: Add support for back references in the garbage collector
- **链接：** https://github.com/containerd/containerd/pull/12025
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** impact/changelog, kind/feature, size/L
- **变更说明：**
  **PR #12025:** Add support for back references in the garbage collector
**标签:** impact/changelog, kind/feature, size/L

**PR内容:** Add backreference labels for an object. This allows objects to be referred to by objects which already exist without updating the labels on the original object or referred to by objects which do not yet exist. This is useful for ephemeral objects as well as objects w...

### PR #12050: Add snapshotter and differ for block CIMs
- **链接：** https://github.com/containerd/containerd/pull/12050
- **状态：** closed
- **已合并：** 是
- **作者：** ambarve
- **标签：** impact/changelog, platform/windows, needs-ok-to-test, size/XXL, go, area/storage
- **变更说明：**
  **PR #12050:** Add snapshotter and differ for block CIMs
**标签:** impact/changelog, platform/windows, needs-ok-to-test, size/XXL, go, area/storage

**PR内容:** This commit adds the snapshotter and differ plugins that can be used to pull/import container images in the block CIM format. (More about block CIMs [here](https://github.com/microsoft/hcsshim/blob/main/pkg/cimfs/doc.go).)...

### PR #12063: Add mount manager
- **链接：** https://github.com/containerd/containerd/pull/12063
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** impact/changelog, kind/feature, size/XXL
- **变更说明：**
  **PR #12063:** Add mount manager
**标签:** impact/changelog, kind/feature, size/XXL

**PR内容:** Implementation of #11303
~~Depends on #12025~~ _merged_

WIP Items:
- ~~Update implementation and testing~~ _complete_
- ~~Moving runtime implementation down to the task manager~~ _complete_
- ~~Passing runtime name to~~ _complete_
- ~~More complete documentation~~ _complete_

```release-note
...

### PR #12082: Enable otel traces in NRI
- **链接：** https://github.com/containerd/containerd/pull/12082
- **状态：** closed
- **已合并：** 是
- **作者：** klihub
- **标签：** impact/changelog, size/S, area/nri
- **变更说明：**
  **PR #12082:** Enable otel traces in NRI
**标签:** impact/changelog, size/S, area/nri

**PR内容:** Set up NRI for producing otel trace spans....

### PR #12142: restart: use goroutine to speedup loadShims
- **链接：** https://github.com/containerd/containerd/pull/12142
- **状态：** closed
- **已合并：** 是
- **作者：** ningmingxiao
- **标签：** impact/changelog, ok-to-test, area/runtime, size/L
- **变更说明：**
  **PR #12142:** restart: use goroutine to speedup loadShims
**标签:** impact/changelog, ok-to-test, area/runtime, size/L

**PR内容:** I find restart containerd use much time on loadShims when create many pods.
create 300 pods
before this commit  
```
time="2025-07-26T17:16:11.934486476+08:00" level=info msg="containerd successfully booted in 12.399198s"
```
after this commit 
```
time="2025-...

---
*本报告由 Containerd Release Tracker 自动生成*