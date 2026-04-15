# Containerd 版本发布分析报告
## containerd API 1.11.0-beta.2 (api/v1.11.0-beta.2)

### 📋 版本信息
- **版本标签：** api/v1.11.0-beta.2
- **版本名称：** containerd API 1.11.0-beta.2
- **发布时间：** 2026-04-15T14:30:08Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/api/v1.11.0-beta.2

### 🔍 分析统计
- **分析时间：** 2026-04-15 15:41:22
- **分析的 PR 数量：** 12
- **分析的 Issue 数量：** 0
- **重要项目数量：** 7

## 📊 版本概述
这是 containerd API v1.11.0 的第二个 Beta 版本，主要为即将到来的 containerd 2.3 版本提供 API 支持，核心变更包括引入新的 shim 引导协议、更新沙箱 API 以及添加容器文件系统复制功能。

## 🔒 安全问题修复
1. ⚠️ 升级 gRPC 依赖至 1.79.3，修复了路径头畸形时可能绕过 `grpc/authz` 等拦截器中基于路径的“拒绝”规则的授权绕过漏洞 - [PR #13099](https://github.com/containerd/containerd/pull/13099) - **风险级别：** 中高。该漏洞允许攻击者通过构造特定的非规范路径绕过授权检查，建议关注并计划升级。

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. Shim 套接字目录配置修复：解决了 rootless 模式下因硬编码路径导致 shim 无法创建套接字的问题 - [PR #12785](https://github.com/containerd/containerd/pull/12785) - **影响：** 此修复直接影响 rootless containerd 部署的稳定性和可用性，之前可能导致容器启动失败。
2. 更新引导 API 日志级别定义，确保日志配置能正确传递到 shim - [PR #13208](https://github.com/containerd/containerd/pull/13208) - **影响：** 影响 shim 进程的日志输出级别，有助于生产环境调试。

## 💥 破坏性变更
1. 🚨 沙箱 API 变更：从沙箱元数据中移除了 `Container` 字段，依赖此字段直接访问 pause 容器信息的客户端（如某些 NRI 插件）需要调整代码，改为从沙箱存储中获取信息 - [PR #12840](https://github.com/containerd/containerd/pull/12840) - **影响：** 直接使用沙箱 API 的客户端需要适配。
2. 🚨 Shim 启动协议变更：引入了新的 `BootstrapParams` 协议（通过 stdin 传递），并计划逐步弃用旧的参数传递方式（CLI 参数、部分环境变量）。虽然当前是增量式引入，但 shim 实现者需要关注此变化以确保未来兼容性 - [PR #12786](https://github.com/containerd/containerd/pull/12786) - **影响：** 自定义或第三方 shim 需要评估对新协议的支持。

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 引入 shim 引导协议，统一并标准化 containerd 向 shim 传递参数的方式，取代原有的混合传递机制（CLI参数、环境变量、stdin） - [PR #12786](https://github.com/containerd/containerd/pull/12786)
2. 更新沙箱 API，移除对 pause 容器的直接依赖，为未来支持更多沙箱实现（如基于 VM 的沙箱）铺平道路 - [PR #12840](https://github.com/containerd/containerd/pull/12840)
3. 为容器文件系统复制操作添加传输类型定义，为容器迁移、备份等高级功能提供底层 API 支持 - [PR #13165](https://github.com/containerd/containerd/pull/13165)
4. Shim 套接字目录现在使用 containerd 配置的目录，解决了 rootless 模式下默认目录不可写的问题 - [PR #12785](https://github.com/containerd/containerd/pull/12785)
5. 为 EROFS 原生容器镜像添加 `os.features` 支持，改善使用 EROFS 快照器时的用户体验 - [PR #13091](https://github.com/containerd/containerd/pull/13091)

## 🚀 性能优化
1. 将 Protobuf 工具链从 protobuild 迁移至 buf，提升了构建的可重复性和开发效率，并集成了格式化和 lint 功能 - [PR #12762](https://github.com/containerd/containerd/pull/12762) - **提升：** 主要提升开发体验和 CI 一致性，对运行时性能无直接影响。
2. 使用 buf 格式化所有 proto 文件，确保 API 定义文件的风格统一 - [PR #12841](https://github.com/containerd/containerd/pull/12841) - **提升：** 提升代码可维护性，减少因格式不一致导致的合并冲突。

## 🎯 风险评估
整体风险评估：中等。这是一个预发布（Beta）的 API 版本，主要风险在于与现有客户端和 shim 实现的兼容性。虽然包含重要的安全修复（gRPC），但破坏性变更（沙箱 API）要求下游进行适配。建议的升级时机是在 containerd 2.3 正式发布并经过充分测试后。需要特别关注的方面包括：1) 自定义 shim 对新引导协议的兼容性；2) 任何直接使用沙箱 API 的代码；3) rootless 部署模式下 shim 套接字路径的配置和行为。

## 📋 升级建议
1. **当前为 Beta 版本，不建议直接用于生产环境。** 建议在测试环境中部署此版本，重点验证与现有 shim（如 runc、gVisor）的兼容性，以及 rootless 模式下的功能。
2. 如果开发了直接调用 containerd 沙箱 API 或管理 shim 的插件/工具，请立即基于此 Beta 版本开始兼容性测试和代码适配。
3. 关注 gRPC 安全更新（PR #13099），虽然本次是 API 模块更新，但预示着 containerd 主项目也将升级。建议将此漏洞纳入安全风险评估。
4. 计划升级至 containerd 2.3 的用户，应利用此 API 版本提前验证客户端（如 Kubernetes CRI 实现、自定义控制器）的兼容性。

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

### PR #12785: Make shim socket directory use configured directory
- **链接：** https://github.com/containerd/containerd/pull/12785
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** impact/changelog, area/runtime, size/XL
- **变更说明：**
  **PR #12785:** Make shim socket directory use configured directory
**标签:** impact/changelog, area/runtime, size/XL

**PR内容:** Pass the socket directory from containerd to the shim via bootstrapparameters. The shim still decides the socket filename but now places it in the directory configured by containerd, ensuring proper ownership and permissions.

**Why:** In rootless setups the default st...

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

---
*本报告由 Containerd Release Tracker 自动生成*