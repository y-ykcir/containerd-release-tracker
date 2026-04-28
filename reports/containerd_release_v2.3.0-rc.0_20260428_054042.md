# Containerd 版本发布分析报告
## containerd 2.3.0-rc.0 (v2.3.0-rc.0)

### 📋 版本信息
- **版本标签：** v2.3.0-rc.0
- **版本名称：** containerd 2.3.0-rc.0
- **发布时间：** 2026-04-28T05:09:02Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.0-rc.0

### 🔍 分析统计
- **分析时间：** 2026-04-28 05:40:42
- **分析的 PR 数量：** 10
- **分析的 Issue 数量：** 2
- **重要项目数量：** 4

## 📊 版本概述
containerd 2.3.0-rc.0 是首个年度长期支持（LTS）版本，提供至少两年的支持，核心变更为引入新的 shim 引导协议、增强 NRI 插件支持、原生支持 EROFS 镜像格式以及改进的可观测性。

## 🔒 安全问题修复
1. ⚠️ 此版本发布说明中未列出新的CVE或安全公告。但依赖项（如golang.org/x/crypto, golang.org/x/sys）的更新通常包含安全修复。 - **风险级别：** 低

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复二进制日志驱动在初始化失败时仍会启动容器的问题，确保日志完整性 - [PR #12595](https://github.com/containerd/containerd/pull/12595) - **影响：** 生产环境中若日志驱动（如Fluentd）启动失败，容器将无法启动，避免产生无日志的容器，符合预期行为。
2. 修复插件配置迁移逻辑，确保在配置加载时正确执行迁移，避免版本不一致问题 - [PR #12608](https://github.com/containerd/containerd/pull/12608) - **影响：** 确保升级时插件配置能平滑迁移，防止因配置版本错配导致插件功能异常。
3. 修复创建沙箱（Sandbox）时注解（Annotations）参数未传递给底层运行时的问题 - [PR #12566](https://github.com/containerd/containerd/pull/12566) - **影响：** 依赖沙箱注解进行特定配置或策略执行的运行时或插件（如安全沙箱）现在能正常工作。

## 💥 破坏性变更
1. 🚨 二进制日志驱动接口行为变更（修复），现在会在驱动未就绪时阻止容器启动 - [PR #12595](https://github.com/containerd/containerd/pull/12595) - **影响：** 使用 `binary://` 或 `binary-v2://` 日志驱动的环境需要确保驱动可靠，否则容器启动会失败。建议测试日志驱动配置。
2. 🚨 插件配置迁移逻辑变更，现在在加载时执行 - [PR #12608](https://github.com/containerd/containerd/pull/12608) - **影响：** 自定义插件或复杂配置链在升级时需要验证配置迁移是否按预期工作。

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 引入 shim 引导协议，改进容器运行时生命周期管理 - [PR #12786](https://github.com/containerd/containerd/pull/12786)
2. 增强 Node Resource Interface (NRI) 插件支持，传递容器用户、seccomp策略、rlimits等完整配置 - [PR #12765](https://github.com/containerd/containerd/pull/12765), [PR #12766](https://github.com/containerd/containerd/pull/12766), [PR #12768](https://github.com/containerd/containerd/pull/12768)
3. 原生支持 EROFS 只读文件系统镜像层，提升容器镜像性能与安全性 - [PR #12567](https://github.com/containerd/containerd/pull/12567), [PR #13185](https://github.com/containerd/containerd/pull/13185)
4. 新增容器文件系统复制传输类型，增强容器运维能力 - [PR #13165](https://github.com/containerd/containerd/pull/13165)
5. 集成 OpenTelemetry 追踪，在插件客户端 RPC 调用中传播 Trace ID，提升可观测性 - [PR #13113](https://github.com/containerd/containerd/pull/13113), [PR #13117](https://github.com/containerd/containerd/pull/13117)

## 🚀 性能优化
1. 支持 EROFS 镜像层，可提供更快的容器启动速度和更低的存储开销 - [PR #12567](https://github.com/containerd/containerd/pull/12567) - **提升：** EROFS 作为只读文件系统，在镜像拉取和容器启动时相比传统叠加文件系统有显著性能优势。
2. 使用新的过滤式 cgroups 统计信息 API，可能减少资源查询开销 - [PR #12901](https://github.com/containerd/containerd/pull/12901) - **提升：** 优化容器资源使用统计的收集效率。

## 🎯 风险评估
整体风险评估：中等。作为首个年度LTS版本和预发布版本，其长期稳定性有待大规模验证。然而，LTS承诺意味着后续会有更严格的修复和支持。关键风险点在于日志驱动行为变更和插件配置迁移逻辑变化，可能影响现有工作流。建议的升级时机是在正式版（GA）发布后，经过充分的测试环境验证。需要特别关注与Kubernetes版本的兼容性（依赖已升级至k8s v1.36.0）、NRI插件集成测试以及任何自定义运行时或沙箱的适配情况。

## 📋 升级建议
1. **当前为候选发布版（rc.0），不建议直接用于生产环境。** 建议在测试环境中部署验证，特别是针对 LTS 版本的长期稳定性。
2. 如果计划使用 NRI 插件进行资源管理或安全策略注入，需测试新版中传递的完整容器配置（用户、seccomp、rlimits等）是否与插件兼容。
3. 评估 EROFS 镜像格式的适用性，对于追求极致启动速度和镜像安全（不可变）的场景，可以开始进行技术验证。
4. 检查并测试现有的二进制日志驱动（如与Fluentd、Logstash的集成）配置，确保其可靠性，避免因 PR #12595 的修复导致容器启动失败。
5. 关注从旧版本（尤其是1.7 LTS）直接升级到2.3 LTS的官方测试报告和指南，此版本是首个支持跨LTS版本升级的版本。

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