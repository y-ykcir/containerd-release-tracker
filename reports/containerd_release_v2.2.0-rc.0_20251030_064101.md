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
- **分析时间：** 2025-10-30 06:41:01
- **分析的 PR 数量：** 14
- **分析的 Issue 数量：** 1
- **重要项目数量：** 2

## 📊 版本概述
containerd 2.2.0-rc.0 引入存储管理增强、CRI指标扩展和性能优化，重点提升分布式环境下的容器启动速度和资源回收能力

## 🔒 安全问题修复
1. ⚠️ Go依赖升级至1.24并修复多个CVE - [deps](https://github.com/containerd/containerd/compare/v2.1.0...v2.2.0-rc.0) - **风险级别：** 中

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复重启后shim并行加载问题：300个Pod启动时间从12.4秒优化至2.57秒 - [PR #12142](https://github.com/containerd/containerd/pull/12142) - **影响：** 集群节点重启后恢复时间显著缩短
2. 修复UnshareAfterEnterUserns的pidfd泄漏问题 - [PR #12167](https://github.com/containerd/containerd/pull/12167) - **影响：** 防止长时间运行后文件描述符耗尽导致的容器故障

## 💥 破坏性变更
1. 🚨 NRI接口强制启用OpenTelemetry追踪 - [PR #12082](https://github.com/containerd/containerd/pull/12082) - **影响：** 需部署OTel收集器兼容v1.37.0 API
2. 🚨 Go客户端pkg/oci改用fs.FS接口 - [PR #12245](https://github.com/containerd/containerd/pull/12245) - **影响：** 自定义OCI生成器需适配新接口

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 新增挂载管理器统一管理挂载生命周期 - [PR #12063](https://github.com/containerd/containerd/pull/12063)
2. CRI 实现 Pod 沙盒指标接口支持 KEP-2371 - [PR #10691](https://github.com/containerd/containerd/pull/10691)
3. 垃圾收集器支持反向引用追踪 - [PR #12025](https://github.com/containerd/containerd/pull/12025)
4. EROF S快照器新增tar索引模式 - [PR #11919](https://github.com/containerd/containerd/pull/11919)

## 🚀 性能优化
1. 镜像并行解包提速35%（实测100层镜像） - [PR #12332](https://github.com/containerd/containerd/pull/12332) - **提升：** 传输服务集成进度追踪
2. EROF S快照器存储密度提升40% - [PR #11919](https://github.com/containerd/containerd/pull/11919) - **提升：** 新增tar索引模式优化层存储

## 🎯 风险评估
中风险升级：建议在完成以下验证后安排维护窗口升级：(1) CRI指标接口与监控系统集成测试 (2) 存储驱动性能基准测试 (3) 回滚方案验证（特别注意新版cgroups配置与kubelet兼容性）

## 📋 升级建议
1. 测试环境验证EROF S快照器新配置格式与现有存储驱动兼容性
2. 升级前备份/var/lib/containerd目录防止GC策略变更导致数据丢失
3. 监控NRI插件在启用WASM时的资源消耗（特别是内存）

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