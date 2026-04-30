# Containerd 版本发布分析报告
## containerd API 1.11.0 (api/v1.11.0)

### 📋 版本信息
- **版本标签：** api/v1.11.0
- **版本名称：** containerd API 1.11.0
- **发布时间：** 2026-04-30T03:58:14Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/api/v1.11.0

### 🔍 分析统计
- **分析时间：** 2026-04-30 05:40:30
- **分析的 PR 数量：** 12
- **分析的 Issue 数量：** 0
- **重要项目数量：** 7

## 📊 版本概述
containerd API 1.11.0 版本主要引入了新的 shim 引导协议以统一运行时参数传递，增强了沙箱 API 的抽象能力，并正式支持 EROFS 原生容器镜像，为 containerd 2.3 的发布奠定基础。

## 🔒 安全问题修复
1. ⚠️ 升级 gRPC 依赖至 1.79.3，修复了路径头畸形时可能绕过 `grpc/authz` 等拦截器中基于路径的“拒绝”规则的授权绕过漏洞 - [PR #13099](https://github.com/containerd/containerd/pull/13099) - **风险级别：** 中

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复 rootless 模式下 shim socket 目录硬编码问题，使其遵循 containerd 的配置目录 - [PR #12785](https://github.com/containerd/containerd/pull/12785) - **影响：** 解决了 rootless 容器因默认 `/run/containerd/s` 目录权限问题导致 shim 启动失败的问题，提升了 rootless 部署的可靠性。

## 💥 破坏性变更
1. 🚨 沙箱 API 的元数据中移除了 `Container` 字段，相关数据需通过元数据存储获取 - [PR #12840](https://github.com/containerd/containerd/pull/12840) - **影响：** 直接依赖此字段（例如某些 NRI 插件）的客户端代码需要更新，改为从沙箱存储中获取沙箱 spec。
2. 🚨 shim 引导协议引入新的参数传递方式（通过 stdin 传递 `BootstrapParams`），废弃了部分原有的 CLI 参数和环境变量传递方式 - [PR #12786](https://github.com/containerd/containerd/pull/12786) - **影响：** 自定义或深度定制 shim 的用户需要适配新的引导协议。

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 引入 shim 引导协议，统一并标准化 containerd 向 shim 传递参数的方式 - [PR #12786](https://github.com/containerd/containerd/pull/12786)
2. 更新沙箱 API，移除对 pause 容器的直接依赖，增加 spec 字段以提升抽象能力 - [PR #12840](https://github.com/containerd/containerd/pull/12840)
3. 为容器文件系统拷贝操作添加传输类型定义 - [PR #13165](https://github.com/containerd/containerd/pull/13165)
4. 在平台定义中增加 `os.features` 字段以支持 EROFS 原生容器镜像的识别与处理 - [PR #13091](https://github.com/containerd/containerd/pull/13091)

## 🚀 性能优化
1. 将 Protobuf 工具链从 protobuild 迁移至 buf，提升了构建的一致性和开发效率 - [PR #12762](https://github.com/containerd/containerd/pull/12762) - **提升：** 简化 CI 设置，确保本地与 CI 环境生成结果完全一致，并为未来引入 API 破坏性变更检测、代码规范检查等功能铺平道路。

## 🎯 风险评估
整体风险评估：中等。此版本包含重要的 API 演进和底层通信协议变更，可能影响依赖特定内部 API 的插件或自定义组件。然而，核心功能保持稳定，且包含重要的安全修复。建议的升级时机是在 containerd 2.3 正式发布后，结合完整的集成测试周期进行。需要特别关注的方面是：1) 所有与沙箱管理相关的自定义工具或插件；2) 任何非标准的 shim 实现或定制。

## 📋 升级建议
1. **升级前务必测试**：由于存在 API 变更（特别是沙箱 API 和 shim 引导协议），建议在非生产环境充分验证现有工作负载和自定义插件的兼容性。
2. **关注插件兼容性**：检查并更新任何依赖沙箱 `Container` 字段的插件（如 NRI 插件）。
3. **利用安全更新**：建议升级以获取 gRPC 安全修复带来的益处。
4. **评估 EROFS 价值**：如果关注容器镜像密度和启动速度，可以开始评估并测试 EROFS 原生镜像，但需注意需显式配置 EROFS snapshotter。
5. **遵循工具链变更**：开发者在本地生成 Protobuf 代码时，需安装 `buf` 工具而非 `protoc`。

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
- **标签：** impact/changelog, area/runtime, size/XXL
- **变更说明：**
  **PR #12786:** Introduce shim bootstrap protocol
**标签:** impact/changelog, area/runtime, size/XXL

**PR内容:**  Containerd needs to pass a bunch of parameters from the daemon down to the shim. Historically, we introduced several mechanisms to do it:
- CLI arguments (-namespace, -id, -address, -publish-binary, -debug)
- Env variables (TTRPC_ADDRESS, GRPC_ADDRESS, NAMESPACE, MAX_SHIM_VERSION, GOM...

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
- **标签：** impact/changelog, kind/feature, size/XL, area/distribution
- **变更说明：**
  **PR #13091:** Add `os.features` support for EROFS native container images
**标签:** impact/changelog, kind/feature, size/XL, area/distribution

**PR内容:** ~depends on #13080~ 
supercedes #12784 

**Note that users still need to explicitly specify the EROFS snapshotter in order to run the EROFS native images by design; it only improves the user experence of the unpacking process**

First, it ...

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