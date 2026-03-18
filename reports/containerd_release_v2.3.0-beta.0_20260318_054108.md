# Containerd 版本发布分析报告
## containerd 2.3.0-beta.0 (v2.3.0-beta.0)

### 📋 版本信息
- **版本标签：** v2.3.0-beta.0
- **版本名称：** containerd 2.3.0-beta.0
- **发布时间：** 2026-03-18T05:34:34Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.0-beta.0

### 🔍 分析统计
- **分析时间：** 2026-03-18 05:41:08
- **分析的 PR 数量：** 10
- **分析的 Issue 数量：** 1
- **重要项目数量：** 2

## 📊 版本概述
containerd 2.3.0-beta.0 是首个年度LTS（长期支持）版本，标志着项目进入与Kubernetes对齐的4个月发布周期，核心价值在于提供至少两年的稳定支持，并引入了EROFS原生镜像支持、NRI插件功能增强及多项运行时稳定性改进。

## 🔒 安全问题修复
1. ⚠️ 本次发布说明未提及具体CVE。但依赖项有大量升级，通常包含安全修复，建议关注 - **风险级别：** 需评估依赖库升级带来的潜在风险
2. ⚠️ 升级了多个核心安全相关库，如 `golang.org/x/crypto`, `golang.org/x/sys`, `github.com/opencontainers/selinux` 等 - **风险级别：** 中。建议审查依赖变更日志以识别具体修复。

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复CRI插件中创建沙箱请求时忽略Annotations参数的问题，确保调用者设置的注解能正确传递给底层运行时 - [PR #12566](https://github.com/containerd/containerd/pull/12566) - **影响：** 此前通过 `WithAnnotations` 设置的沙箱注解会丢失，影响依赖沙箱注解进行网络策略、监控标签传递的组件
2. 优化OOMKilled事件处理顺序，确保在容器退出事件前发送OOM事件 - [PR #12714](https://github.com/containerd/containerd/pull/12714) - **影响：** 使监控系统和编排器（如Kubernetes）能更准确、及时地判断容器退出是否由OOM引起，对于自动扩缩容和故障诊断至关重要

## 💥 破坏性变更
1. 🚨 项目依赖的API模块版本从 `v1.10.0` 升级至 `v1.11.0-beta.0` - [依赖变更](https://github.com/containerd/containerd/blob/main/CHANGELOG/CHANGELOG-2.3.md) - **影响：** 直接依赖containerd API（非CRI）的客户端工具或库需要验证兼容性，可能存在接口变更
2. 🚨 作为首个年度LTS版本，项目明确了从1.7 LTS到2.3 LTS的直接升级路径将得到测试和支持，但非LTS版本间的升级需谨慎评估 - **影响：** 为长期支持的用户提供了清晰的升级规划

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 插件配置迁移逻辑优化，在加载时执行以防止配置版本不一致 - [PR #12608](https://github.com/containerd/containerd/pull/12608)
2. CDI规范中检测供应商信息，为 `--gpus` 参数生成正确的设备ID，优化GPU支持 - [PR #12839](https://github.com/containerd/containerd/pull/12839)
3. 沙箱API增加spec字段，为沙箱运行时提供更完整的配置信息 - [PR #12840](https://github.com/containerd/containerd/pull/12840)
4. 支持EROFS（Enhanced Read-Only File System）作为原生容器镜像层媒体类型 - [PR #12567](https://github.com/containerd/containerd/pull/12567)
5. 使用fsmount API挂载EROFS，避免PAGE_SIZE限制，支持更大镜像 - [PR #12783](https://github.com/containerd/containerd/pull/12783)

## 🚀 性能优化
1. EROFS原生层支持，提供更高的压缩率和读取性能，尤其适合大型容器镜像 - [PR #12567](https://github.com/containerd/containerd/pull/12567) - **提升：** 减少镜像拉取和存储空间占用，提升容器启动速度
2. 运行时使用新的过滤式cgroups统计信息API，可能减少查询开销 - [PR #12901](https://github.com/containerd/containerd/pull/12901) - **提升：** 优化资源监控性能，降低对主机的影响
3. 优化OOM事件监控处理，减少事件丢失或顺序错乱的风险 - [PR #12714](https://github.com/containerd/containerd/pull/12714) - **提升：** 提高在高内存压力场景下事件处理的可靠性

## 🎯 风险评估
整体风险评估：中等。作为beta版本，存在功能不稳定或未完成的风险，不适用于生产环境。然而，作为未来两年的LTS基础版本，其架构和API变更需要提前关注和测试。
建议的升级时机：在 `v2.3.0` 正式版发布后，经过充分的测试环境验证，再规划生产环境升级。
需要特别关注的方面：1) 与Kubernetes版本的兼容性（依赖已升级至v0.35.2）；2) NRI插件对新增容器参数的兼容性；3) 直接调用containerd API的内部工具或脚本的适配情况；4) 使用EROFS等新特性对现有运维流程的影响。

## 📋 升级建议
1. **立即行动：** 由于这是首个年度LTS的beta版，建议立即在非生产测试环境中部署，验证与现有Kubernetes版本、CNI插件、监控Agent及自定义运行时（如有）的兼容性。
2. **重点测试：** 如果使用GPU或特定硬件加速设备，请验证 `--gpus` 参数在新版本下的功能。如果考虑使用EROFS镜像，需评估其对现有CI/CD流水线和镜像仓库的影响。
3. **关注NRI插件：** 如果使用了Node Resource Interface (NRI) 插件，本次更新传递了大量新的容器上下文（如rlimits、sysctl、seccomp、用户信息等），需确保插件能正确处理这些新增信息。
4. **等待正式版：** 生产环境升级应等待 `v2.3.0` 正式版本发布。鉴于其LTS属性，升级后可获得长期稳定的支持。
5. **审查配置：** 升级前备份containerd配置。由于插件配置迁移逻辑变更（PR #12608），需确认配置加载和迁移行为符合预期。

## 📋 Release 包含的变更

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

### PR #12769: Pass container user (uid, gids) to plugins
- **链接：** https://github.com/containerd/containerd/pull/12769
- **状态：** closed
- **已合并：** 是
- **作者：** klihub
- **标签：** impact/changelog, size/S, area/nri
- **变更说明：**
  **PR #12769:** Pass container user (uid, gids) to plugins
**标签:** impact/changelog, size/S, area/nri

**PR内容:** Implement missing support for passing any container user (uid, gids) as input to NRI plugins....

### PR #12770: Pass extended container status to NRI.
- **链接：** https://github.com/containerd/containerd/pull/12770
- **状态：** closed
- **已合并：** 是
- **作者：** klihub
- **标签：** impact/changelog, size/L, area/nri
- **变更说明：**
  **PR #12770:** Pass extended container status to NRI.
**标签:** impact/changelog, size/L, area/nri

**PR内容:** Pass more complete container status information to NRI, including exit code, and timestamps for container creation, start, and exit events....

---
*本报告由 Containerd Release Tracker 自动生成*