# Containerd 版本发布分析报告
## containerd 2.2.3 (v2.2.3)

### 📋 版本信息
- **版本标签：** v2.2.3
- **版本名称：** containerd 2.2.3
- **发布时间：** 2026-04-14T17:38:30Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.2.3

### 🔍 分析统计
- **分析时间：** 2026-04-14 18:40:53
- **分析的 PR 数量：** 19
- **分析的 Issue 数量：** 2
- **重要项目数量：** 17

## 📊 版本概述
containerd 2.2.3 是一个重要的补丁版本，主要修复了安全漏洞、容器创建回归问题以及并行解包导致的文件系统错误，并升级了底层依赖以提升稳定性和安全性。

## 🔒 安全问题修复
1. ⚠️ 修复spdystream依赖中的安全漏洞 CVE-2026-35469。 - [更新提交](https://github.com/containerd/containerd/commit/31bd34a064dc7136413efde09b99a2bdd14dabe9) - **风险级别：** 中（依赖项漏洞，具体影响需参考上游公告）
2. ⚠️ 修复镜像层tar提取过程中的TOCTOU（检查时间与使用时间）竞争条件漏洞。 - [PR #12971](https://github.com/containerd/containerd/pull/12971) - **风险级别：** 中（可能被用于破坏容器镜像完整性或进行符号链接攻击）
3. ⚠️ 升级Go工具链至1.25.8/1.26.2，包含多个Go标准库安全修复。 - [PR #13011](https://github.com/containerd/containerd/pull/13011) - **风险级别：** 中（修复了`crypto/x509`, `html/template`, `net/url`, `os`等包的安全问题）

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复：特权容器会错误地覆盖主机的cgroup挂载选项（如`nsdelegate`）。 - [PR #13120](https://github.com/containerd/containerd/pull/13120) - **影响：** 运行特权容器可能意外改变主机cgroup子系统的行为，影响资源管理和安全隔离。
2. 修复：当镜像中`/etc/passwd`或`/etc/group`是绝对路径符号链接时，容器创建失败。 - [PR #13015](https://github.com/containerd/containerd/pull/13015) - **影响：** 使用NixOS、Guix等发行版基础镜像的容器无法启动，是Go 1.24引入的严重回归。
3. 修复：启用并行解包时，上层镜像层中删除的文件（白洞）可能在下层仍然可见。 - [PR #13125](https://github.com/containerd/containerd/pull/13125) - **影响：** 导致容器内文件系统状态与镜像定义不符，可能引发安全或功能问题。
4. 修复：CRI接口中`UpdatePodSandbox`方法返回通用错误而非`Unimplemented`。 - [PR #13023](https://github.com/containerd/containerd/pull/13023) - **影响：** 调用该API的客户端（如某些版本的Kubelet）可能收到令人困惑的错误信息。

## 💥 破坏性变更
1. 🚨 此版本为补丁版本，未引入故意的破坏性变更。所有变更旨在修复bug、提升安全性和兼容性。

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 修复特权容器cgroup挂载选项丢失的问题，避免影响主机cgroup配置 - [PR #13120](https://github.com/containerd/containerd/pull/13120)
2. 修复使用Go 1.24时，因绝对符号链接导致无法从NixOS等风格镜像创建容器的回归问题 - [PR #13015](https://github.com/containerd/containerd/pull/13015) / [Issue #12683](https://github.com/containerd/containerd/issues/12683)
3. 修复并行解包 (`max_concurrent_unpacks > 1`) 时白洞（whiteout）文件被忽略的bug，确保文件删除操作正确生效 - [PR #13125](https://github.com/containerd/containerd/pull/13125) / [Issue #13030](https://github.com/containerd/containerd/issues/13030)
4. 修复tar提取过程中的TOCTOU竞争条件漏洞，增强安全性 - [PR #12971](https://github.com/containerd/containerd/pull/12971)
5. 更新底层runc运行时至v1.3.5版本 - [PR #13061](https://github.com/containerd/containerd/pull/13061)

## 🚀 性能优化
1. 在差异计算（diff walking）中启用挂载管理器，修复某些快照器（如EROFS）的层提取错误。 - [PR #13198](https://github.com/containerd/containerd/pull/13198) - **提升：** 提高与特定文件系统和快照器的兼容性，减少镜像拉取失败。
2. 升级压缩库`github.com/klauspost/compress`至v1.18.5。 - [PR #13197](https://github.com/containerd/containerd/pull/13197) - **提升：** 通常包含bug修复和潜在的性能优化。

## 🎯 风险评估
整体风险评估：**低风险**。这是一个修复导向的补丁版本，主要解决已知的bug和安全问题，未引入新功能或架构变更。
建议的升级时机：下一个维护窗口。对于受特定bug（如NixOS镜像启动失败、白洞文件问题）影响的环境，建议优先升级。
需要特别关注的方面：1) 验证绝对符号链接相关修复是否解决了您环境中容器启动的问题。2) 如果使用了`max_concurrent_unpacks`配置，升级后检查之前被错误保留的文件是否已被正确删除。3) 观察特权容器运行后，主机cgroup的挂载选项是否保持稳定。

## 📋 升级建议
1. **建议升级**：对于使用2.2.x版本的用户，特别是那些使用NixOS风格镜像、启用了并行解包功能或运行特权容器的环境，建议尽快安排升级到2.2.3。
2. **测试重点**：升级前，请在测试环境中重点验证容器创建（尤其是基于特定发行版的镜像）、镜像拉取和解压、以及特权容器的cgroup行为。
3. **关联组件**：由于runc已升级至v1.3.5，请确保同时更新runc二进制文件以获取完整的修复集。
4. **回滚准备**：虽然风险较低，但任何升级都应制定回滚计划。备份当前containerd配置和状态。

## 📋 Release 包含的变更

### PR #12971: [release/2.2] Fix TOCTOU race bug in tar extraction
- **链接：** https://github.com/containerd/containerd/pull/12971
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/XS, area/distribution
- **变更说明：**
  **PR #12971:** [release/2.2] Fix TOCTOU race bug in tar extraction
**标签:** impact/changelog, size/XS, area/distribution

**原始PR #12961:** Fix TOCTOU race bug in tar extraction
**原始PR标签:** kind/bug, size/XS
**原始PR内容:** See https://github.com/containerd/containerd/security/advisories/GHSA-ww5g-h6rh-8wm3 for a conversation around this particular bug.

**Cherry-pick PR内容:** This is an automated che...

### PR #13011: [release/2.2 backport] update to go1.25.8, test go1.26.1
- **链接：** https://github.com/containerd/containerd/pull/13011
- **状态：** closed
- **已合并：** 是
- **作者：** thaJeztah
- **标签：** size/S, go, area/toolchain
- **变更说明：**
  **PR #13011:** [release/2.2 backport] update to go1.25.8, test go1.26.1
**标签:** size/S, go, area/toolchain

**原始PR #12985:** update to go1.25.8, test go1.26.1
**原始PR标签:** cherry-pick/1.7.x, size/S, area/toolchain, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** go1.25.8 (released 2026-03-05) includes security fixes to the html/template, net/url, and os packages, as well as bug fixes to the...

### PR #13015: [release/2.2] fix(oci): handle absolute symlinks in rootfs user lookup
- **链接：** https://github.com/containerd/containerd/pull/13015
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/L, go, area/client
- **变更说明：**
  **PR #13015:** [release/2.2] fix(oci): handle absolute symlinks in rootfs user lookup
**标签:** impact/changelog, area/runtime, size/L, go, area/client

**原始PR #12732:** fix(oci): handle absolute symlinks in rootfs user lookup
**原始PR标签:** size/L, go, area/client, cherry-picked/2.2.x
**原始PR内容:** ### Analysis
This PR addresses a regression/behavior change introduced with Go 1.24 builds regarding s...

### PR #13019: [release/2.2] fix(oci): apply absolute symlink resolution to /etc/group
- **链接：** https://github.com/containerd/containerd/pull/13019
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/M, go
- **变更说明：**
  **PR #13019:** [release/2.2] fix(oci): apply absolute symlink resolution to /etc/group
**标签:** impact/changelog, area/runtime, size/M, go

**原始PR #12925:** fix(oci): apply absolute symlink resolution to /etc/group
**原始PR标签:** cherry-pick/1.7.x, size/M, go, area/client, cherry-pick/2.1.x, cherry-picked/2.2.x
**原始PR内容:** This is a follow-up to PR #12732. 

As noted by @TheColorman, while the pr...

### PR #13023: [release/2.2] cri: UpdatePodSandbox should return Unimplemented
- **链接：** https://github.com/containerd/containerd/pull/13023
- **状态：** closed
- **已合并：** 是
- **作者：** samuelkarp
- **标签：** impact/changelog, area/cri, size/XS
- **变更说明：**
  **PR #13023:** [release/2.2] cri: UpdatePodSandbox should return Unimplemented
**标签:** impact/changelog, area/cri, size/XS

**PR内容:** errgrpc will correctly translate ErrNotImplemented to GRPC's Unimplemented, but a plain error will be returned directly.

```release-note
Ensure UpdatePodSandbox returns Unimplemented instead of a generic error
```...

### PR #13061: [release/2.2] update runc binary to v1.3.5
- **链接：** https://github.com/containerd/containerd/pull/13061
- **状态：** closed
- **已合并：** 是
- **作者：** thaJeztah
- **标签：** impact/changelog, area/runtime, size/XS
- **变更说明：**
  **PR #13061:** [release/2.2] update runc binary to v1.3.5
**标签:** impact/changelog, area/runtime, size/XS

**PR内容:** release notes: https://github.com/opencontainers/runc/releases/tag/v1.3.5
full diff: https://github.com/opencontainers/runc/compare/v1.3.4...v1.3.5

```release-note
Update runc to v1.3.5
```...

### PR #13066: [release/2.2] Fix vagrant on CI
- **链接：** https://github.com/containerd/containerd/pull/13066
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS
- **变更说明：**
  **PR #13066:** [release/2.2] Fix vagrant on CI
**标签:** size/XS

**原始PR #13055:** Fix vagrant on CI
**原始PR标签:** size/XS
**原始PR内容:** Recent jobs started to fail:

```bash
    default: NOCHANGE: partition 4 is size 123318239. it cannot be grown
The SSH command responded with a non-zero exit status. Vagrant
assumes that this means the command failed. The output for this command
should be in t...

### PR #13120: [release/2.2] Preserve cgroup mount options for privileged containers
- **链接：** https://github.com/containerd/containerd/pull/13120
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/L
- **变更说明：**
  **PR #13120:** [release/2.2] Preserve cgroup mount options for privileged containers
**标签:** impact/changelog, area/cri, size/L

**原始PR #12952:** Preserve cgroup mount options for privileged containers
**原始PR标签:** kind/bug, area/cri, size/L, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** Privileged containers don't have a cgroup namespace, so by default they run in the host's cgroup names...

### PR #13125: [release/2.2] Tweak mount info for overlayfs in case of parallel unpack
- **链接：** https://github.com/containerd/containerd/pull/13125
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/snapshotters, size/L
- **变更说明：**
  **PR #13125:** [release/2.2] Tweak mount info for overlayfs in case of parallel unpack
**标签:** impact/changelog, area/snapshotters, size/L

**原始PR #13115:** Tweak mount info for overlayfs in case of parallel unpack
**原始PR标签:** kind/bug, size/L, cherry-pick/2.2.x
**原始PR内容:** Fixes: https://github.com/containerd/containerd/issues/13030

Alternative to: https://github.com/containerd/containerd/p...

### PR #13154: [release/2.2] Skip TestExportAndImportMultiLayer on s390x
- **链接：** https://github.com/containerd/containerd/pull/13154
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** kind/test, size/XS
- **变更说明：**
  **PR #13154:** [release/2.2] Skip TestExportAndImportMultiLayer on s390x
**标签:** kind/test, size/XS

**原始PR #13149:** Skip TestExportAndImportMultiLayer on s390x
**原始PR标签:** kind/test, cherry-picked/1.7.x, size/XS, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** Skip TestExportAndImportMultiLayer on s390x

The test image `ghcr.io/containerd/volume-copy-up:2.`1 does not include a manifest...

---
*本报告由 Containerd Release Tracker 自动生成*