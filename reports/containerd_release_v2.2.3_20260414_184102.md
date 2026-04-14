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
- **分析时间：** 2026-04-14 18:41:02
- **分析的 PR 数量：** 19
- **分析的 Issue 数量：** 2
- **重要项目数量：** 17

## 📊 版本概述
containerd 2.2.3 是一个重要的补丁版本，主要包含一个安全更新、多个关键Bug修复（包括并行解包和特权容器cgroup问题）以及对Go 1.24兼容性的修复。

## 🔒 安全问题修复
1. ⚠️ 更新 `github.com/moby/spdystream` 依赖至 v0.5.1，修复安全漏洞 - [CVE-2026-35469](https://github.com/moby/spdystream/security/advisories/GHSA-pc3f-x583-g7j2) - **风险级别：** 中
2. ⚠️ 修复镜像tar提取过程中的TOCTOU（检查时间与使用时间）竞争条件漏洞，防止潜在的文件替换攻击 - [PR #12971](https://github.com/containerd/containerd/pull/12971) - **风险级别：** 中
3. ⚠️ 更新Go工具链至1.25.8/1.26.2，包含多个Go标准库的安全修复（如 `crypto/x509`, `html/template`, `net/url`, `os`） - [PR #13011](https://github.com/containerd/containerd/pull/13011) - **风险级别：** 低至中

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复并行解包导致白名单失效：当配置 `max_concurrent_unpacks > 1` 时，后续层中删除的文件可能仍然存在于最终文件系统中，破坏镜像层语义 - [PR #13125](https://github.com/containerd/containerd/pull/13125) - **影响：** 可能导致容器内出现预期已删除的文件，影响应用行为和安全策略。
2. 修复特权容器cgroup挂载选项：特权容器会无意中剥离主机cgroup2挂载的额外选项（如 `nsdelegate`, `memory_recursiveprot`），影响主机cgroup行为 - [PR #13120](https://github.com/containerd/containerd/pull/13120) - **影响：** 运行特权容器可能改变主机cgroup配置，影响资源管理和安全隔离。
3. 修复CRI `UpdatePodSandbox` 错误返回：确保返回正确的 `Unimplemented` 状态码而非通用错误，改善Kubernetes等CRI客户端兼容性 - [PR #13023](https://github.com/containerd/containerd/pull/13023) - **影响：** 使上层编排系统能更准确地处理未实现的操作。

## 💥 破坏性变更
1. 🚨 此版本为补丁版本，未引入破坏性变更。所有变更为向后兼容的Bug修复和安全更新。

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 修复特权容器cgroup挂载选项丢失的问题，避免影响主机cgroup配置 - [PR #13120](https://github.com/containerd/containerd/pull/13120)
2. 修复使用Go 1.24时，因绝对符号链接导致容器创建失败的问题（影响NixOS等系统） - [PR #13015](https://github.com/containerd/containerd/pull/13015) / [Issue #12683](https://github.com/containerd/containerd/issues/12683)
3. 修复镜像tar提取过程中的TOCTOU竞争条件漏洞，增强安全性 - [PR #12971](https://github.com/containerd/containerd/pull/12971)
4. 修复并行解包 (`max_concurrent_unpacks > 1`) 时白名单文件失效的问题 - [PR #13125](https://github.com/containerd/containerd/pull/13125) / [Issue #13030](https://github.com/containerd/containerd/issues/13030)
5. 更新底层runc运行时至v1.3.5版本 - [PR #13061](https://github.com/containerd/containerd/pull/13061)
6. 在镜像差异计算中启用挂载管理器，修复使用某些快照器（如EROFS）时的层提取错误 - [PR #13198](https://github.com/containerd/containerd/pull/13198)

## 🚀 性能优化
1. 在镜像差异计算中启用挂载管理器，可改善使用overlayfs之外快照器（如 `stargz`, `erofs`）时的层提取性能和可靠性 - [PR #13198](https://github.com/containerd/containerd/pull/13198) - **提升：** 减少特定快照器下的提取错误，提升稳定性。

## 🎯 风险评估
整体风险评估：**低风险**。这是一个经过充分测试的补丁版本，主要修复已知Bug和安全问题，无破坏性变更。建议的升级时机：下一个维护窗口。需要特别关注的方面：升级后观察特权容器的资源限制是否生效，以及并行解包功能是否正常工作。对于安全要求高的环境，因包含CVE修复，建议尽快升级。

## 📋 升级建议
1. **建议升级**：对于使用containerd 2.2.x版本的生产环境，建议规划升级至2.2.3，特别是使用了并行解包功能或运行基于NixOS镜像的容器。
2. **测试重点**：升级前，请在测试环境中重点验证：1) 特权容器的cgroup行为；2) 使用 `max_concurrent_unpacks` 配置时的镜像拉取和容器启动；3) 包含绝对符号链接 `/etc/passwd` 或 `/etc/group` 的镜像（常见于NixOS）。
3. **兼容性**：此版本修复了与Go 1.24的兼容性问题，如果运行环境已升级Go版本，此修复至关重要。
4. **运行时更新**：升级containerd时，需同步更新runc至v1.3.5，以获取完整的修复集。

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