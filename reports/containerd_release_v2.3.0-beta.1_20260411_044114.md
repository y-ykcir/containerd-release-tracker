# Containerd 版本发布分析报告
## containerd 2.3.0-beta.1 (v2.3.0-beta.1)

### 📋 版本信息
- **版本标签：** v2.3.0-beta.1
- **版本名称：** containerd 2.3.0-beta.1
- **发布时间：** 2026-04-11T03:32:20Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.0-beta.1

### 🔍 分析统计
- **分析时间：** 2026-04-11 04:41:14
- **分析的 PR 数量：** 10
- **分析的 Issue 数量：** 2
- **重要项目数量：** 4

## 📊 版本概述
containerd 2.3.0-beta.1 是首个年度长期支持（LTS）版本，标志着项目进入与Kubernetes对齐的稳定发布节奏，核心价值在于提供为期两年的稳定支持，并引入了新的shim引导协议、EROFS镜像支持以及多项NRI和可观测性增强。

## 🔒 安全问题修复
1. ⚠️ 更新大量依赖项至新版本，包括golang.org/x/crypto, golang.org/x/net等，通常包含安全修复 - [Dependency Changes](https://github.com/containerd/containerd/releases/tag/v2.3.0-beta.1) - **风险级别：** 中（建议关注最终正式版的CVE详情）
2. ⚠️ 引入新的安全相关库，如`cyphar.com/go-pathrs`和`github.com/cyphar/filepath-securejoin`，可能用于增强路径处理安全性 - [Dependency Changes](https://github.com/containerd/containerd/releases/tag/v2.3.0-beta.1) - **风险级别：** 低

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复二进制日志驱动在初始化失败时仍会启动容器的问题，确保日志驱动就绪前容器不会启动 - [PR #12595](https://github.com/containerd/containerd/pull/12595) - **影响：** 修复前，当日志驱动（如Fluentd）启动失败时，容器仍会运行但日志丢失，可能导致关键日志数据缺失和排障困难。
2. 修复Sandbox创建请求中Annotations参数被忽略的问题，确保传递给shim - [PR #12566](https://github.com/containerd/containerd/pull/12566) - **影响：** 修复前，通过`WithAnnotations`设置的沙箱注解无法传递给底层运行时，影响依赖注解进行特定配置的插件或shim功能。
3. 更新OOMKilled事件处理逻辑，确保在容器退出事件前发送OOM事件 - [PR #12714](https://github.com/containerd/containerd/pull/12714) - **影响：** 提升OOM事件监控的准确性，确保监控系统能正确关联容器退出原因。

## 💥 破坏性变更
1. 🚨 二进制日志驱动协议变更：引入了`binary-v2://`协议以避免破坏性变更，但旧版`binary://`驱动可能存在兼容性问题 - [PR #12595](https://github.com/containerd/containerd/pull/12595) - **影响：** 使用自定义或旧版二进制日志驱动的用户需要验证兼容性或迁移到新协议。
2. 🚨 插件配置迁移逻辑调整：现在在配置加载时执行迁移，可能影响包含复杂插件配置和版本升级的场景 - [PR #12608](https://github.com/containerd/containerd/pull/12608) - **影响：** 需要仔细测试从旧版本升级时的插件配置迁移过程。

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 引入首个年度LTS（长期支持）版本，支持周期至少两年，并与Kubernetes发布周期对齐 - [Release Notes](https://github.com/containerd/containerd/releases/tag/v2.3.0-beta.1)
2. 引入新的shim引导协议，旨在提升shim启动的可靠性和性能 - [PR #12786](https://github.com/containerd/containerd/pull/12786)
3. 增加对EROFS（只读文件系统）原生容器镜像层的支持，提升镜像分发和存储效率 - [PR #12567](https://github.com/containerd/containerd/pull/12567)
4. CRI：允许容器同时使用主机网络和用户命名空间，支持Kubernetes KEP-5607 - [PR #12518](https://github.com/containerd/containerd/pull/12518)
5. NRI增强：向插件传递容器用户、seccomp策略、rlimits、sysctl和CDI设备等更多运行时配置信息 - [PR #12765](https://github.com/containerd/containerd/pull/12765), [PR #12766](https://github.com/containerd/containerd/pull/12766), [PR #12767](https://github.com/containerd/containerd/pull/12767), [PR #12768](https://github.com/containerd/containerd/pull/12768)

## 🚀 性能优化
1. 使用新的过滤式cgroups统计API，可能提升资源监控效率并减少开销 - [PR #12901](https://github.com/containerd/containerd/pull/12901) - **提升：** 更高效地获取容器cgroup指标。
2. 支持EROFS镜像层，利用其高压缩率和原地解压特性，可显著提升镜像拉取速度和容器启动速度 - [PR #12567](https://github.com/containerd/containerd/pull/12567) - **提升：** 镜像拉取和容器启动性能，尤其在资源受限环境中。
3. 使用fsmount API绕过PAGE_SIZE限制挂载EROFS，提升大镜像处理能力 - [PR #12783](https://github.com/containerd/containerd/pull/12783) - **提升：** 对大尺寸EROFS镜像的支持和挂载性能。

## 🎯 风险评估
整体风险评估：中等偏高。作为首个年度LTS的Beta版，引入了新的发布模式、架构协议（shim bootstrap）和存储格式（EROFS），变化较大。虽然LTS承诺长期稳定，但Beta阶段可能存在未知问题。建议的升级时机是在2.3.0正式版发布后，并在非关键业务集群中经过至少一个完整的发布周期（如一个月）的验证。需要特别关注shim新协议的稳定性、与现有CNI/CSI插件的兼容性，以及从旧版本（尤其是1.7 LTS）升级的平滑性。

## 📋 升级建议
1. **此版本为Beta预发布版本，不建议直接用于生产环境。** 建议在测试环境中充分验证新功能（如EROFS、shim新协议）和与现有工作负载的兼容性。
2. 计划从containerd 1.7 LTS直接升级到2.3 LTS的用户，应密切关注社区发布的升级路径指南和测试报告。
3. 如果使用二进制日志驱动（如通过CRI配置的Fluentd），务必测试其在新版本下的行为，确认日志收集功能正常。
4. 升级前，检查所有自定义插件或与NRI集成的工具，确保它们能正确处理新增的容器配置信息（如rlimits, sysctl等）。
5. 利用增强的OpenTelemetry追踪功能（Trace ID注入日志、RPC传播）来提升生产环境下的可观测性和排障能力。

## 📋 Release 包含的变更

### PR #12518: feat: Allow containers to use both host network and user namespace
- **链接：** https://github.com/containerd/containerd/pull/12518
- **状态：** closed
- **已合并：** 是
- **作者：** HirazawaUi
- **标签：** impact/changelog, area/cri, size/L
- **变更说明：**
  **PR #12518:** feat: Allow containers to use both host network and user namespace
**标签:** impact/changelog, area/cri, size/L

**PR内容:** This PR implements the feature proposed in KEP: kubernetes/enhancements#5607 for containerd.

This PR modifies the behavior to use bind mounts for /sys when a pod employs both hostNetwork and user namespace.

relate: #12489...

### PR #12566: Set annotations parameter in CreateSandbox request
- **链接：** https://github.com/containerd/containerd/pull/12566
- **状态：** closed
- **已合并：** 是
- **作者：** rawahars
- **标签：** impact/changelog, kind/feature, area/cri, size/S
- **变更说明：**
  **PR #12566:** Set annotations parameter in CreateSandbox request
**标签:** impact/changelog, kind/feature, area/cri, size/S

**PR内容:** In the CreateSandbox request, which is part of the Sandbox Controller, we ignored the `Annotations` parameter which could have been set by the caller via `WithAnnotations` option.

This PR rectifies the same and adds the Annotations parameter to the request.
...

### PR #12567: Add EROFS layer media type
- **链接：** https://github.com/containerd/containerd/pull/12567
- **状态：** closed
- **已合并：** 是
- **作者：** ChengyuZhu6
- **标签：** impact/changelog, size/S, area/distribution
- **变更说明：**
  **PR #12567:** Add EROFS layer media type
**标签:** impact/changelog, size/S, area/distribution

**PR内容:** It introduces "application/vnd.erofs.layer.v1" to add support for EROFS native layers, so that containerd can fetch EROFS native container images directly.
E.g. `ctr run --snapshotter erofs -t quay.io/chengyuzhu6/ubuntu:20.04-erofs test /bin/bash`...

### PR #12595: Fix binary logging driver not blocking container start on failure
- **链接：** https://github.com/containerd/containerd/pull/12595
- **状态：** closed
- **已合并：** 是
- **作者：** tao12345666333
- **标签：** impact/changelog, kind/bug, kind/feature, area/runtime, size/L
- **变更说明：**
  **PR #12595:** Fix binary logging driver not blocking container start on failure
**标签:** impact/changelog, kind/bug, kind/feature, area/runtime, size/L

**PR内容:** fix https://github.com/containerd/containerd/issues/12490

~~Note: I think this is a breaking change; perhaps we should also consider compatibility issues.~~

`binary-v2://` was introduced to avoid breaking changes.

**关联的Issues:**
...

### PR #12608: Update plugin config migration to run on load
- **链接：** https://github.com/containerd/containerd/pull/12608
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** impact/changelog, size/L
- **变更说明：**
  **PR #12608:** Update plugin config migration to run on load
**标签:** impact/changelog, size/L

**PR内容:** Perform the plugin migrations on load to allow stepping through plugin migration versions to happen alongside migration of the global configuration object. When the configuration migrations happen separately, the version in the config can get increasd on load and cause plugin migration not t...

### PR #12714: Update OOMKilled event handling
- **链接：** https://github.com/containerd/containerd/pull/12714
- **状态：** closed
- **已合并：** 是
- **作者：** fuweid
- **标签：** impact/changelog, area/runtime, size/XL
- **变更说明：**
  **PR #12714:** Update OOMKilled event handling
**标签:** impact/changelog, area/runtime, size/XL

**PR内容:** ### cmd/containerd-shim-runc-v2: add experimental OOM package


The OOM handling code is intended to live under pkg/oom/v2. However, the
cgroupv2 package still needs further refinement, such as exporting the
cgroup path and allowing callers to query specific stats instead of
returning...

### PR #12765: cri,nri: pass any POSIX rlimits to plugins.
- **链接：** https://github.com/containerd/containerd/pull/12765
- **状态：** closed
- **已合并：** 是
- **作者：** klihub
- **标签：** impact/changelog, size/S, area/nri
- **变更说明：**
  **PR #12765:** cri,nri: pass any POSIX rlimits to plugins.
**标签:** impact/changelog, size/S, area/nri

**PR内容:** Implement missing support for passing any container POSIX rlimits as input to NRI plugins. 

```release-note
Pass any POSIX rlimits to plugins
```...

### PR #12766: cri,nri: pass linux sysctl to plugins.
- **链接：** https://github.com/containerd/containerd/pull/12766
- **状态：** closed
- **已合并：** 是
- **作者：** klihub
- **标签：** impact/changelog, size/S, area/nri
- **变更说明：**
  **PR #12766:** cri,nri: pass linux sysctl to plugins.
**标签:** impact/changelog, size/S, area/nri

**PR内容:** Implement missing support for passing any container linux sysctl parameters as input to NRI plugins.

```release-note
Pass linux sysctl to plugins
```...

### PR #12767: Pass injected CDI devices to plugins
- **链接：** https://github.com/containerd/containerd/pull/12767
- **状态：** closed
- **已合并：** 是
- **作者：** klihub
- **标签：** impact/changelog, size/S, area/nri
- **变更说明：**
  **PR #12767:** Pass injected CDI devices to plugins
**标签:** impact/changelog, size/S, area/nri

**PR内容:** Implement passing injected CDI devices as input to NRI plugins....

### PR #12768: Pass seccomp policy to plugins
- **链接：** https://github.com/containerd/containerd/pull/12768
- **状态：** closed
- **已合并：** 是
- **作者：** klihub
- **标签：** impact/changelog, size/S, area/nri
- **变更说明：**
  **PR #12768:** Pass seccomp policy to plugins
**标签:** impact/changelog, size/S, area/nri

**PR内容:** Implement missing support for passing any container seccomp policy as input to NRI plugins....

---
*本报告由 Containerd Release Tracker 自动生成*