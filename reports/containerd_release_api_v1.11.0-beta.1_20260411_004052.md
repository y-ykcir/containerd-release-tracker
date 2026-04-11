# Containerd 版本发布分析报告
## containerd API 1.11.0-beta.1 (api/v1.11.0-beta.1)

### 📋 版本信息
- **版本标签：** api/v1.11.0-beta.1
- **版本名称：** containerd API 1.11.0-beta.1
- **发布时间：** 2026-04-11T00:06:52Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/api/v1.11.0-beta.1

### 🔍 分析统计
- **分析时间：** 2026-04-11 00:40:52
- **分析的 PR 数量：** 13
- **分析的 Issue 数量：** 0
- **重要项目数量：** 7

## 📊 版本概述
containerd API 1.11.0-beta.1 是一个预发布版本，为即将到来的 containerd 2.3 版本奠定 API 基础，核心价值在于引入了新的 shim 引导协议、沙箱 API 改进以及容器文件系统复制支持，同时包含重要的 gRPC 安全更新。

## 🔒 安全问题修复
1. ⚠️ gRPC 库安全更新，修复了路径头授权绕过漏洞 - [PR #13099](https://github.com/containerd/containerd/pull/13099) - **风险级别：** 中。影响依赖于 gRPC 拦截器进行路径级权限校验的场景。

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 更新 gRPC 依赖至 1.79.3，修复了路径授权绕过漏洞，该漏洞允许恶意构造的 :path 请求头绕过基于路径的拦截器（如 grpc/authz）的“拒绝”规则 - [PR #13099](https://github.com/containerd/containerd/pull/13099) - **影响：** 如果使用了 gRPC 拦截器进行细粒度授权控制，此漏洞可能导致未授权访问，建议关注并评估风险。

## 💥 破坏性变更
1. 🚨 沙箱 API 元数据中移除了 `Container` 字段，依赖此字段获取 pause 容器信息的插件（如 NRI）需要重构，改为从元数据存储中获取所需数据 - [PR #12840](https://github.com/containerd/containerd/pull/12840) - **影响：** 自定义插件或工具如果直接访问沙箱的 Container 字段，将无法编译或运行，需要适配新的 API。
2. 🚨 新的 shim 引导协议将逐步弃用原有的 CLI 参数、环境变量等启动参数传递方式。虽然当前是新增而非立即替换，但为未来版本废弃旧方式做准备，shim 实现者需要关注 - [PR #12786](https://github.com/containerd/containerd/pull/12786) - **影响：** 自定义或第三方 shim 需要评估并计划支持新的 BootstrapParams 协议。

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 引入 shim 引导协议，统一并标准化 containerd 向 shim 传递配置参数的方式，取代原有的混合传递机制（CLI参数、环境变量、stdin） - [PR #12786](https://github.com/containerd/containerd/pull/12786)
2. 更新沙箱 API，移除元数据中的 Container 字段，改为包含 spec 字段，以抽象化对 pause 容器的依赖 - [PR #12840](https://github.com/containerd/containerd/pull/12840)
3. 为容器文件系统复制（类似 `docker cp`）添加传输类型定义，为未来实现容器与宿主机间安全文件传输提供 API 支持 - [PR #13165](https://github.com/containerd/containerd/pull/13165)
4. 在平台定义中添加 `os.features` 字段，以原生支持 EROFS 容器镜像，优化解压和运行体验 - [PR #13091](https://github.com/containerd/containerd/pull/13091)

## 🚀 性能优化
1. 将 Protobuf 构建工具从 protobuild 迁移至 buf，简化 CI/本地构建依赖，提高代码生成的可复现性，并为未来引入 API 破坏性变更检测、代码规范检查等能力铺平道路 - [PR #12762](https://github.com/containerd/containerd/pull/12762) - **提升：** 主要提升开发效率和工具链现代化水平。
2. 新的 shim 引导协议使用 Protobuf 替代 JSON 和混合传递方式，有望简化 shim 启动逻辑，提高参数传递的效率和可维护性 - [PR #12786](https://github.com/containerd/containerd/pull/12786) - **提升：** 改善启动流程的健壮性和未来可扩展性。

## 🎯 风险评估
整体风险评估：中等。作为 API 的 Beta 预发布版，其本身不直接用于生产环境，因此直接升级风险低。然而，版本中预示的 API 变化（特别是破坏性变更）为未来 containerd 2.3 的升级带来了必须提前准备的中等风险。建议的升级时机是在 containerd 2.3 正式发布并经过充分测试后。需要特别关注的方面是：1) 所有自定义或第三方 shim 对新引导协议的兼容性；2) 依赖沙箱内部结构的插件或监控工具的适配情况；3) gRPC 安全修复在现有分支的落地情况。

## 📋 升级建议
1. **当前版本为 Beta 预发布版，不建议在生产环境直接升级。** 主要目的是供开发者和生态插件作者进行兼容性测试。
2. 建议安全团队评估 gRPC 授权绕过漏洞（CVE-2024-7240）对现有环境的影响，并考虑在当前的稳定版本（如 1.6.x 或 1.7.x）中向后移植此安全修复。
3. 插件和工具开发者应重点关注两项破坏性变更（沙箱 API 和 shim 引导协议），并开始适配工作，为 containerd 2.3 的正式发布做准备。
4. 关注 EROFS 镜像支持特性，如果计划使用 EROFS 作为容器镜像格式，可以开始测试相关工作流。

## 📋 Release 包含的变更

### PR #12762: Migrate from protobuild to buf
- **链接：** https://github.com/containerd/containerd/pull/12762
- **状态：** closed
- **已合并：** 是
- **作者：** mxpv
- **标签：** size/XXL, area/toolchain
- **变更说明：**
  **PR #12762:** Migrate from protobuild to buf
**标签:** size/XXL, area/toolchain

**PR内容:** This PR migrates from `Protobuild` (which we all love and use for quite some time) to [`buf`](https://github.com/bufbuild/buf) to manage our proto files.

Immediate benefits:
- No need to install `protoc` dependency. Mush simpler [CI setup](https://github.com/containerd/containerd/pull/12762/changes/edb...

### PR #12786: Introduce shim bootstrap protocol
- **链接：** https://github.com/containerd/containerd/pull/12786
- **状态：** closed
- **已合并：** 是
- **作者：** mxpv
- **标签：** impact/changelog, size/XXL
- **变更说明：**
  **PR #12786:** Introduce shim bootstrap protocol
**标签:** impact/changelog, size/XXL

**PR内容:**  Containerd needs to pass a bunch of parameters from the daemon down to the shim. Historically, we introduced several mechanisms to do it:
- CLI arguments (-namespace, -id, -address, -publish-binary, -debug)
- Env variables (TTRPC_ADDRESS, GRPC_ADDRESS, NAMESPACE, MAX_SHIM_VERSION, GOMAXPROCS, SCHED...

### PR #12815: Generate api/next.txtpb and name module
- **链接：** https://github.com/containerd/containerd/pull/12815
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** size/XXL, area/toolchain
- **变更说明：**
  **PR #12815:** Generate api/next.txtpb and name module
**标签:** size/XXL, area/toolchain

**PR内容:** `buf` will generate the protobuf text file which can be used for viewing all protobuf changes in one file and quickly diffing changes.

Add a module name to the buf.yaml to allow pushing. With the switch the buf and relative paths, without publishing the containerd protos are not importable with...

### PR #12840: Remove Container field from sandbox metadata
- **链接：** https://github.com/containerd/containerd/pull/12840
- **状态：** closed
- **已合并：** 是
- **作者：** mxpv
- **标签：** impact/changelog, size/XXL
- **变更说明：**
  **PR #12840:** Remove Container field from sandbox metadata
**标签:** impact/changelog, size/XXL

**PR内容:** There are multiple places in CRI which assume the use of pause containers and the podsandbox package. Since the goal of the Sandbox API is to abstract away the use of pause containers, we should not make such assumptions.                                                                      ...

### PR #12841: Use buf to format proto files
- **链接：** https://github.com/containerd/containerd/pull/12841
- **状态：** closed
- **已合并：** 是
- **作者：** mxpv
- **标签：** size/XXL, area/toolchain
- **变更说明：**
  **PR #12841:** Use buf to format proto files
**标签:** size/XXL, area/toolchain

**PR内容:** We've integrated `buf` in https://github.com/containerd/containerd/pull/12762                                                                                                                
`buf` comes with an integrated linter and formatter.                                                                 ...

### PR #12913: api: regenerate and re-vendor protos
- **链接：** https://github.com/containerd/containerd/pull/12913
- **状态：** closed
- **已合并：** 是
- **作者：** thaJeztah
- **标签：** size/XXL, go, area/toolchain
- **变更说明：**
  **PR #12913:** api: regenerate and re-vendor protos
**标签:** size/XXL, go, area/toolchain

**PR内容:** Probably related to https://github.com/containerd/containerd/commit/ca1c5b2d3db8c620c26ab9674b7ccb9a4b023a63 (https://github.com/containerd/containerd/pull/12841).

I got this diff when running `make protos`; let's see if CI agrees it's OK 😅 ...

### PR #13045: Prepare release notes for api/v1.11.0-beta.0
- **链接：** https://github.com/containerd/containerd/pull/13045
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** size/S
- **变更说明：**
  **PR #13045:** Prepare release notes for api/v1.11.0-beta.0
**标签:** size/S

**PR内容:** First step in v2.3 beta process

----
containerd api/v1.11.0-beta.0

Welcome to the api/v1.11.0-beta.0 release of containerd!  
*This is a pre-release of containerd*

The 12th release for the containerd 1.x API aligns with the containerd 2.3 release.

### Highlights

* Update sandbox API to include...

### PR #13091: Add `os.features` support for EROFS native container images
- **链接：** https://github.com/containerd/containerd/pull/13091
- **状态：** closed
- **已合并：** 是
- **作者：** hsiangkao
- **标签：** kind/feature, size/XL, area/distribution
- **变更说明：**
  **PR #13091:** Add `os.features` support for EROFS native container images
**标签:** kind/feature, size/XL, area/distribution

**PR内容:** ~depends on #13080~ 
supercedes #12784 

**Note that users still need to explicitly specify the EROFS snapshotter in order to run the EROFS native images by design; it only improves the user experence of the unpacking process**

First, it enhances the trans...

### PR #13099: build(deps): bump google.golang.org/grpc from 1.59.0 to 1.79.3 in /api
- **链接：** https://github.com/containerd/containerd/pull/13099
- **状态：** closed
- **已合并：** 是
- **作者：** dependabot[bot]
- **标签：** dependencies, size/M, go
- **变更说明：**
  **PR #13099:** build(deps): bump google.golang.org/grpc from 1.59.0 to 1.79.3 in /api
**标签:** dependencies, size/M, go

**PR内容:** Bumps [google.golang.org/grpc](https://github.com/grpc/grpc-go) from 1.59.0 to 1.79.3.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/grpc/grpc-go/releases">google.golang.org/grpc's releases</a>.</em></p>
<blockquote>
<h2>R...

### PR #13165: Add transfer types for container filesystem copy
- **链接：** https://github.com/containerd/containerd/pull/13165
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** impact/changelog, kind/feature, size/XXL
- **变更说明：**
  **PR #13165:** Add transfer types for container filesystem copy
**标签:** impact/changelog, kind/feature, size/XXL

**PR内容:** Add support for transfering data to and from a container filesystem. This is needed to implement an equivalent of `docker cp` when the runtime cannot/should not directly access to mounted container filesystem.

Upstreaming the types from Nerdbox (https://github.com/conta...

---
*本报告由 Containerd Release Tracker 自动生成*