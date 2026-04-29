# Containerd 版本发布分析报告
## containerd 2.3.0-rc.1 (v2.3.0-rc.1)

### 📋 版本信息
- **版本标签：** v2.3.0-rc.1
- **版本名称：** containerd 2.3.0-rc.1
- **发布时间：** 2026-04-29T07:23:43Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.0-rc.1

### 🔍 分析统计
- **分析时间：** 2026-04-29 07:41:19
- **分析的 PR 数量：** 10
- **分析的 Issue 数量：** 2
- **重要项目数量：** 5

## 📊 版本概述
containerd 2.3.0-rc.1 是首个年度长期支持（LTS）版本，提供至少两年支持，核心变更为引入新的 shim 引导协议、增强 OpenTelemetry 可观测性、原生支持 EROFS 镜像层以及大量 CRI 和 NRI 插件功能的完善。

## 🔒 安全问题修复
1. ⚠️ 依赖项全面升级，包含多个安全补丁（如 golang.org/x/* 套件、containerd/nri、go-jose等） - **风险级别：** 中 - 建议审查依赖变更列表以评估特定环境风险。

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复二进制日志驱动（binary logging driver）失败时不会阻塞容器启动的问题，确保日志收集可靠性 - [PR #12595](https://github.com/containerd/containerd/pull/12595) - **影响：** 此前若日志驱动初始化失败，容器仍会启动，导致关键日志丢失。修复后，启动流程将正确阻塞，保证日志系统就绪。
2. 修复插件配置迁移逻辑，确保在配置加载时正确执行，避免版本不一致导致的配置问题 - [PR #12608](https://github.com/containerd/containerd/pull/12608) - **影响：** 防止因全局配置和插件配置迁移步骤不同步而导致的潜在配置错误或插件加载失败。
3. 改进 OOMKilled 事件处理顺序，确保在容器退出事件前发送 OOM 事件 - [PR #12714](https://github.com/containerd/containerd/pull/12714) - **影响：** 使监控系统能更准确地判断容器退出原因（尤其是因 OOM 被杀）。

## 💥 破坏性变更
1. 🚨 修复 NRI 插件中 OCI 钩子的所有权跟踪问题，可能影响依赖特定行为的 NRI 插件 - [PR #264](https://github.com/containerd/nri/pull/264) - **影响：** 使用 NRI 插件的环境需要测试插件兼容性，确保修复后的行为符合预期。

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 引入 shim 引导协议，改进 shim 生命周期管理 - [PR #12786](https://github.com/containerd/containerd/pull/12786)
2. 增强 OpenTelemetry 追踪集成，支持在 RPC 调用和日志中传播 Trace ID - [PR #13113](https://github.com/containerd/containerd/pull/13113) / [PR #13117](https://github.com/containerd/containerd/pull/13117)
3. 原生支持 EROFS 镜像层，提升容器镜像分发与存储效率 - [PR #12567](https://github.com/containerd/containerd/pull/12567) / [PR #13185](https://github.com/containerd/containerd/pull/13185)
4. CRI：允许容器同时使用主机网络和用户命名空间 - [PR #12518](https://github.com/containerd/containerd/pull/12518)
5. CRI：修复 Sandbox 创建请求中注解（Annotations）未传递的问题 - [PR #12566](https://github.com/containerd/containerd/pull/12566) - [Issue #12565](https://github.com/containerd/containerd/issues/12565)
6. NRI：向插件传递更多容器运行时信息（如用户、seccomp策略、rlimits、sysctl、CDI设备等） - [PR #12765](https://github.com/containerd/containerd/pull/12765) / [PR #12766](https://github.com/containerd/containerd/pull/12766) / [PR #12767](https://github.com/containerd/containerd/pull/12767) / [PR #12768](https://github.com/containerd/containerd/pull/12768) / [PR #12769](https://github.com/containerd/containerd/pull/12769)

## 🚀 性能优化
1. 使用新的过滤式 cgroups 统计信息 API，可能提升资源监控效率 - [PR #12901](https://github.com/containerd/containerd/pull/12901) - **提升：** 减少不必要的数据收集开销。
2. EROFS 层使用 fsmount API，避免 PAGE_SIZE 限制，提升挂载性能 - [PR #12783](https://github.com/containerd/containerd/pull/12783) - **提升：** 优化大镜像或特殊场景下的存储性能。

## 🎯 风险评估
整体风险评估：中等。作为首个年度 LTS 的预发布版，其引入的新特性和架构变更（如 shim 引导协议）需要充分测试。然而，大量的 bug 修复和稳定性改进为生产环境带来了积极影响。建议的升级时机是在 2.3.0 稳定版发布后，并经过充分的测试验证。需要特别关注的方面包括：NRI 插件兼容性、二进制日志驱动行为变化、以及任何自定义运行时或沙箱集成点。

## 📋 升级建议
1. **当前版本为候选发布版（rc.1），不建议直接用于生产环境。** 应尽快在测试环境中部署，验证新功能（如 EROFS、shim 引导协议）和关键修复（如日志驱动）的稳定性。
2. 计划升级至 2.3 LTS 版本的用户，应利用此预发布版开始兼容性测试，特别是针对 NRI 插件和自定义沙箱（Sandbox）实现。
3. 关注 OpenTelemetry 集成增强，评估并调整现有监控和日志链路，以充分利用分布式追踪能力。
4. 检查并更新容器镜像构建流程，评估采用 EROFS 格式镜像以提升分发和存储效率的可能性。

## 📋 Release 包含的变更

### PR #264: Fix panic within ctr if the daemon dies while attached to a container
- **链接：** https://github.com/containerd/containerd/pull/264
- **状态：** closed
- **已合并：** 是
- **作者：** mlaventure
- **变更说明：**
  **PR #264:** Fix panic within ctr if the daemon dies while attached to a container

**PR内容:** Signed-off-by: Kenfe-Mickael Laventure mickael.laventure@gmail.com
...

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

relate: #12489

```release-note
Allow contain...

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

---
*本报告由 Containerd Release Tracker 自动生成*