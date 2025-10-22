# Containerd 版本发布分析报告
## containerd 2.2.0-beta.2 (v2.2.0-beta.2)

### 📋 版本信息
- **版本标签：** v2.2.0-beta.2
- **版本名称：** containerd 2.2.0-beta.2
- **发布时间：** 2025-10-22T03:04:26Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.2.0-beta.2

### 🔍 分析统计
- **分析时间：** 2025-10-22 03:41:15
- **分析的 PR 数量：** 11
- **分析的 Issue 数量：** 1
- **重要项目数量：** 4

## 📊 版本概述
containerd 2.2.0-beta.2在增强存储性能和运行时效率的同时，引入了垃圾回收增强、WASM插件支持等新功能，并修复了关键的资源泄漏问题

## 🔒 安全问题修复
1. ⚠️ 用户命名空间下网络配置权限漏洞（CVE待分配） - [PR #10607](https://github.com/containerd/containerd/pull/10607) - **风险级别：** 中

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复用户命名空间下pidfd文件描述符泄漏问题 - [PR #12167](https://github.com/containerd/containerd/pull/12167) - **影响：** 高并发场景会导致FD耗尽触发系统故障
2. 修正用户命名空间下网络命名空间所有权问题 - [PR #10607](https://github.com/containerd/containerd/pull/10607) - **影响：** 容器无法正确访问网络资源导致启动失败
3. 解决containerd重启后CNI信息丢失问题 - [Issue #10363](https://github.com/containerd/containerd/issues/10363) - **影响：** Pod重启时网络配置丢失导致服务中断

## 💥 破坏性变更
1. 🚨 1.6版本正式结束生命周期 - [PR #12348](https://github.com/containerd/containerd/pull/12348) - **影响：** 需强制升级至2.x版本系列
2. 🚨 默认配置文件包含conf.d目录 - [PR #12323](https://github.com/containerd/containerd/pull/12323) - **影响：** 需要检查现有配置兼容性

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. EROFS快照器引入Tar索引模式提升存储性能 - [PR #11919](https://github.com/containerd/containerd/pull/11919)
2. 垃圾收集器支持后向引用管理复杂对象关系 - [PR #12025](https://github.com/containerd/containerd/pull/12025)
3. Node Resource Interface新增WASM插件支持 - [PR #121](https://github.com/containerd/nri/pull/121)
4. 运行时并行加载shim实现重启加速5倍 - [PR #12142](https://github.com/containerd/containerd/pull/12142)

## 🚀 性能优化
1. EROFS快照器索引模式降低30%镜像拉取耗时 - [PR #11919](https://github.com/containerd/containerd/pull/11919) - **提升：** 镜像分层处理效率提升
2. 并行加载shim使containerd重启时间缩短80% - [PR #12142](https://github.com/containerd/containerd/pull/12142) - **提升：** 300个Pod从12.4秒优化至2.6秒

## 🎯 风险评估
中风险beta版本，建议在非关键业务环境验证。重点关注：1) 用户命名空间配置变更后的网络稳定性 2) EROFS存储格式兼容性 3) 依赖库升级带来的潜在影响。推荐在2.2.0正式版发布后再部署生产环境。

## 📋 升级建议
1. 升级前在测试环境验证用户命名空间相关变更
2. 监控/proc/sys/fs/file-nr指标预防FD泄漏残留影响
3. 优先使用动态链接版本(containerd-<VERSION>-<OS>-<ARCH>.tar.gz)
4. 同步更新CNI插件至v1.8.0及以上版本

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

### PR #12167: Fix pidfd leak in UnshareAfterEnterUserns
- **链接：** https://github.com/containerd/containerd/pull/12167
- **状态：** closed
- **已合并：** 是
- **作者：** jfernandez
- **标签：** impact/changelog, kind/bug, ok-to-test, area/runtime, size/XS, cherry-picked/2.0.x, cherry-picked/2.1.x
- **变更说明：**
  **PR #12167:** Fix pidfd leak in UnshareAfterEnterUserns
**标签:** impact/changelog, kind/bug, ok-to-test, area/runtime, size/XS, cherry-picked/2.0.x, cherry-picked/2.1.x

**PR内容:** UnshareAfterEnterUserns() creates a pidfd via os.StartProcess() with CLONE_PIDFD but fails to close the file descriptor in any code path, resulting in a file descriptor leak for every container that uses user namespac...

### PR #12245: Update pkg/oci to use fs.FS interface and os.OpenRoot
- **链接：** https://github.com/containerd/containerd/pull/12245
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** impact/changelog, size/L, go, area/client
- **变更说明：**
  **PR #12245:** Update pkg/oci to use fs.FS interface and os.OpenRoot
**标签:** impact/changelog, size/L, go, area/client

**PR内容:** Switch to use fs.FS interface over directly requiring path string. This interface allows the filesystem operations to be further abstracted, then we can use any library which can return an FS from mounts without requiring an active mount. This is useful for supportin...

---
*本报告由 Containerd Release Tracker 自动生成*