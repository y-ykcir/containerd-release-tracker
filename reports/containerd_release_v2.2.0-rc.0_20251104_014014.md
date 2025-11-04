# Containerd 版本发布分析报告
## containerd 2.2.0-rc.0 (v2.2.0-rc.0)

### 📋 版本信息
- **版本标签：** v2.2.0-rc.0
- **版本名称：** containerd 2.2.0-rc.0
- **发布时间：** 2025-10-30T05:03:54Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.2.0-rc.0

### 🔍 分析统计
- **分析时间：** 2025-11-04 01:40:14
- **分析的 PR 数量：** 14
- **分析的 Issue 数量：** 1
- **重要项目数量：** 2

## 📊 版本概述
containerd 2.2.0-rc.0 带来存储优化、并行处理增强和CRI监控能力升级，同时改进垃圾回收机制和生产环境稳定性

## 🔒 安全问题修复
1. ⚠️ 更新Go安全依赖至1.24版本 - [PR #11533](https://github.com/containerd/containerd/pull/11533) - **风险级别：** 中（包含多个安全补丁）
2. ⚠️ 升级crypto模块至v0.41.0 - [Dependency Change](https://github.com/golang/crypto) - **风险级别：** 高（涉及加密算法改进）

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复重启后shim并行加载问题 - [PR #12142](https://github.com/containerd/containerd/pull/12142) - **影响：** 容器重启时间从12秒缩短至2.5秒
2. 修复UnshareAfterEnterUserns的pidfd泄漏 - [PR #12167](https://github.com/containerd/containerd/pull/12167) - **影响：** 避免长期运行时的资源泄漏

## 💥 破坏性变更
1. 🚨 Go客户端接口更新至fs.FS - [PR #12245](https://github.com/containerd/containerd/pull/12245) - **影响：** 需要更新依赖pkg/oci的客户端代码
2. 🚨 CRI插件升级至Kubernetes 1.34 API - [Dependency Change](https://github.com/kubernetes/api) - **影响：** 需验证Kubernetes集群兼容性

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 新增并行镜像解包支持 - [PR #12332](https://github.com/containerd/containerd/pull/12332) - 提升大规模镜像分发效率
2. 实现CRI ListPodSandboxMetrics接口 - [PR #10691](https://github.com/containerd/containerd/pull/10691) - 增强Kubernetes Pod监控能力
3. EROF Snapshotter新增tar索引模式 - [PR #11919](https://github.com/containerd/containerd/pull/11919) - 优化镜像层存储效率

## 🚀 性能优化
1. 镜像解包进度追踪集成到传输服务 - [PR #11921](https://github.com/containerd/containerd/pull/11921) - **提升：** 镜像操作可视化和调试能力
2. 块存储CIM支持 - [PR #12050](https://github.com/containerd/containerd/pull/12050) - **提升：** Windows容器存储性能优化

## 🎯 风险评估
整体风险评估：中风险。关键改进集中在存储和运行时组件，建议在准生产环境验证以下方面：1）新Snapshotter模式与现有存储驱动兼容性 2）并行解包对节点IO的影响 3）Kubernetes 1.34 API兼容性。推荐在业务低峰期分阶段升级，优先升级边缘节点验证稳定性。

## 📋 升级建议
1. 生产环境升级前务必测试EROF Snapshotter新配置模式
2. 检查所有自定义插件与新版Go 1.24的兼容性
3. 利用新的CRI监控接口优化K8s集群监控方案
4. 隔离测试新的垃圾回收反向引用机制

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
- **标签：** impact/changelog, ok-to-test, size/L, area/storage
- **变更说明：**
  **PR #11919:** Add tar index mode to erofs snapshotter
**标签:** impact/changelog, ok-to-test, size/L, area/storage

**PR内容:** ## Summary

This PR introduces support for a new "tar index" mode in the EROFS snapshotter and differ. The tar index mode enables more efficient handling of OCI image layers by generating a tar index and appending the original tar content

## Key Changes

- **docs/s...

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
- More complete documentation - _could be follow up_...

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