# Containerd 版本发布分析报告
## containerd API 1.11.0-rc.0 (api/v1.11.0-rc.0)

### 📋 版本信息
- **版本标签：** api/v1.11.0-rc.0
- **版本名称：** containerd API 1.11.0-rc.0
- **发布时间：** 2026-04-29T00:22:18Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/api/v1.11.0-rc.0

### 🔍 分析统计
- **分析时间：** 2026-04-29 00:40:33
- **分析的 PR 数量：** 12
- **分析的 Issue 数量：** 0
- **重要项目数量：** 7

## 📊 版本概述
containerd API 1.11.0-rc.0 是为 containerd 2.3 版本准备的 API 预发布版，核心是为沙箱化（Sandbox）和 shim 管理奠定基础，引入了新的引导协议并移除了对 pause 容器的硬编码依赖。

## 🔒 安全问题修复
1. ⚠️ 升级 gRPC 依赖至 1.79.3，修复了路径授权绕过漏洞 - [PR #13099](https://github.com/containerd/containerd/pull/13099) - **风险级别：** 高 - 恶意构造的 :path 头（缺少前导斜杠）可能绕过基于路径的拦截器（如 grpc/authz）中的“拒绝”规则。
2. ⚠️ 多项 gRPC 安全更新，包括解决特定条件下可能的内存耗尽问题 - [PR #13099](https://github.com/containerd/containerd/pull/13099) - **风险级别：** 中

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. Shim 引导协议更新日志级别定义，确保日志配置正确传递 - [PR #13208](https://github.com/containerd/containerd/pull/13208) - **影响：** 修复了通过新协议传递日志级别可能不正确的问题
2. 修复从 stdin 读取数据的问题，确保引导协议参数可靠传递 - [PR #12786](https://github.com/containerd/containerd/pull/12786) - **影响：** 保障了 shim 启动过程的稳定性

## 💥 破坏性变更
1. 🚨 沙箱 API 移除元数据中的 Container 字段，依赖此字段获取 pause 容器信息的客户端需要调整 - [PR #12840](https://github.com/containerd/containerd/pull/12840) - **影响：** 需要更新直接使用 Sandbox 元数据中 Container 字段的代码，改为通过其他 API 或存储查询所需信息。
2. 🚨 引入新的 shim 引导协议，逐步弃用原有的 CLI 参数、环境变量传参方式 - [PR #12786](https://github.com/containerd/containerd/pull/12786) - **影响：** 自定义或第三方 shim 实现需要适配新的 BootstrapParams 协议以接收配置，旧方式目前仍兼容但未来会废弃。

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 引入 shim 引导协议，统一并简化 containerd 向 shim 传递配置参数的方式 - [PR #12786](https://github.com/containerd/containerd/pull/12786)
2. 更新沙箱 API，移除元数据中的 Container 字段，抽象化对 pause 容器的依赖 - [PR #12840](https://github.com/containerd/containerd/pull/12840)
3. 添加容器文件系统拷贝的传输类型，为容器数据迁移和备份提供标准化 API - [PR #13165](https://github.com/containerd/containerd/pull/13165)
4. Shim 套接字目录现在使用 containerd 配置的目录，解决了 rootless 环境下的权限问题 - [PR #12785](https://github.com/containerd/containerd/pull/12785)
5. 为 EROFS 原生容器镜像添加 `os.features` 支持，优化镜像拉取和运行体验 - [PR #13091](https://github.com/containerd/containerd/pull/13091)

## 🚀 性能优化
1. 迁移构建工具链，从 protobuild 切换到 buf，提升 Protobuf 文件管理和生成的效率与一致性 - [PR #12762](https://github.com/containerd/containerd/pull/12762) - **提升：** 简化 CI 设置，提升本地/CI 环境生成代码的可复现性。
2. 支持 EROFS 原生容器镜像，可显著提升容器启动速度和减少存储占用 - [PR #13091](https://github.com/containerd/containerd/pull/13091) - **提升：** 对于使用 EROFS 格式的镜像，启动性能有显著优化。

## 🎯 风险评估
整体风险评估：中等。此版本是 API 预发布版，包含重要的架构变更（如 shim 引导协议、沙箱 API 更新）和关键安全更新。虽然引入了破坏性变更，但主要影响的是直接使用底层 API 的客户端或自定义运行时。对于大多数通过 Kubernetes CRI 使用的用户，影响是间接的。建议等待对应的 containerd 2.3 稳定版发布后，再在非关键业务环境中进行小范围升级验证。需要特别关注自定义 shim 的兼容性和沙箱相关功能的测试。

## 📋 升级建议
1. **当前为预发布版（rc.0），不建议在生产环境直接升级。** 应在测试环境中充分验证与现有工作负载的兼容性。
2. 关注 gRPC 的安全更新（PR #13099），评估当前生产环境版本是否受相关漏洞影响，并规划升级至稳定版。
3. 如果使用自定义或第三方 shim，需要开始评估适配新的 shim 引导协议（PR #12786）的工作量。
4. 对于使用沙箱 API 的高级用户或开发者，检查代码是否依赖被移除的 `Container` 字段（PR #12840），并准备迁移。
5. 计划使用 EROFS 镜像的用户，可以开始测试此版本对 `os.features` 的支持（PR #13091）。

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