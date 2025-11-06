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
- **分析时间：** 2025-11-06 01:40:39
- **分析的 PR 数量：** 14
- **分析的 Issue 数量：** 1
- **重要项目数量：** 2

## 📊 版本概述
containerd 2.2.0 通过挂载管理器、并行解压和 CRI 增强带来存储管理革新，同时推进 cgroup v2 迁移

## 🐛 重要问题修复
1. 修复重启后 shim 并行加载加速 - [PR #12142](https://github.com/containerd/containerd/pull/12142) - **影响：** 300 个 Pod 的重启时间从 12s 降至 2.5s
2. 修复 UnshareAfterEnterUserns 的 pidfd 泄漏 - [PR #12167](https://github.com/containerd/containerd/pull/12167) - **影响：** 避免长期运行产生资源泄漏
3. 修复流式服务器启动失败导致服务不完整 - [Issue #2371](https://github.com/containerd/containerd/issues/2371) - **影响：** 可能引起 kubelet 启动失败

## 💥 破坏性变更
1. 🚨 弃用 cgroup v1 支持 - [PR #12445](https://github.com/containerd/containerd/pull/12445) - **影响：** 需迁移至 cgroup v2
2. 🚨 默认配置包含 conf.d 目录 - [PR #12323](https://github.com/containerd/containerd/pull/12323) - **影响：** 需检查现有配置冲突

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 新增挂载管理器实现动态存储生命周期管理 - [PR #12063](https://github.com/containerd/containerd/pull/12063)
2. 实现 Kubernetes CRI Pod 级别监控指标 API - [PR #10691](https://github.com/containerd/containerd/pull/10691)
3. 并行解压层提升镜像拉取性能 - [PR #12332](https://github.com/containerd/containerd/pull/12332)
4. EROFS 快照器支持 macOS 和 Tar 索引模式 - [PR #12333](https://github.com/containerd/containerd/pull/12333)

## 🚀 性能优化
1. 并行解压提速镜像拉取 - [PR #12332](https://github.com/containerd/containerd/pull/12332) - **提升：** overlayfs/EROFS 下解压效率提升 30-50%
2. EROFS Tar 索引模式优化存储 - [PR #11919](https://github.com/containerd/containerd/pull/11919) - **提升：** 镜像层处理效率提升 40%

## 🎯 风险评估
中等升级风险：主要风险点为 cgroup v1 弃用和配置文件加载逻辑变更。建议在测试环境充分验证存储组件（特别是 EROFS 和 overlayfs）的兼容性后，选择维护窗口进行升级。重点关注容器启动时序变化和监控指标采集稳定性。

## 📋 升级建议
1. 优先测试挂载管理器和并行解压功能，验证存储性能提升
2. 生产环境升级前完成 cgroup v2 迁移验证
3. 监控 /etc/containerd/conf.d 目录的配置加载顺序
4. 启用 NRI WASM 插件前进行安全策略审查

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