# Containerd 版本发布分析报告
## containerd API 1.11.0-beta.0 (api/v1.11.0-beta.0)

### 📋 版本信息
- **版本标签：** api/v1.11.0-beta.0
- **版本名称：** containerd API 1.11.0-beta.0
- **发布时间：** 2026-03-17T17:48:06Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/api/v1.11.0-beta.0

### 🔍 分析统计
- **分析时间：** 2026-03-17 18:40:22
- **分析的 PR 数量：** 6
- **分析的 Issue 数量：** 0
- **重要项目数量：** 3

## 📊 版本概述
containerd 1.11.0-beta.0 带来沙箱API重构和Proto工具链升级，主要面向容器运行时集成商和插件开发者

## 💥 破坏性变更
1. 🚨 沙箱元数据删除Container字段 - [PR #12840](https://github.com/containerd/containerd/pull/12840) - **影响：** 需要修改依赖pause容器元数据的插件实现
2. 🚨 Proto生成路径标准化 - [PR #12762](https://github.com/containerd/containerd/pull/12762) - **影响：** 自定义插件需验证proto兼容性

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 沙箱API重构：移除Container字段改用独立spec字段 - [PR #12840](https://github.com/containerd/containerd/pull/12840) - **影响：** 需要更新依赖沙箱元数据的组件（如NRI插件）
2. Proto工具链迁移至buf并改进API管理 - [PR #12762](https://github.com/containerd/containerd/pull/12762) - **影响：** 改进proto文件生成一致性和CI可靠性

## 🚀 性能优化
1. Proto生成工具链优化 - [PR #12841](https://github.com/containerd/containerd/pull/12841) - **提升：** 统一proto文件格式化标准，降低协作冲突
2. API模块化改进 - [PR #12815](https://github.com/containerd/containerd/pull/12815) - **提升：** 支持通过buf registry管理proto依赖

## 🎯 风险评估
中风险升级：沙箱API变更可能影响插件兼容性，建议在非关键环境先行验证。生产环境建议等待正式版发布，重点验证：1) 沙箱生命周期管理 2) NRI插件兼容性 3) 自定义proto插件的构建流程

## 📋 升级建议
1. 立即测试沙箱API变更对CRI插件、NRI插件的影响
2. 检查自定义插件对沙箱元数据字段的依赖情况
3. 在预发布环境验证proto文件生成的一致性
4. 关注后续beta版本对API稳定性的改进

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

---
*本报告由 Containerd Release Tracker 自动生成*