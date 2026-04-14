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
- **分析时间：** 2026-04-14 18:40:52
- **分析的 PR 数量：** 19
- **分析的 Issue 数量：** 2
- **重要项目数量：** 17

## 📊 版本概述
containerd 2.2.3 是一个重要的补丁版本，主要修复了多个影响容器创建、镜像解压和安全性的关键Bug，并包含一个安全更新。

## 🔒 安全问题修复
1. ⚠️ 更新spdystream依赖以修复CVE-2026-35469 - [PR #13217](https://github.com/containerd/containerd/pull/13217) - **风险级别：** 中（具体细节需参考上游公告）
2. ⚠️ 修复tar提取中的TOCTOU竞争条件漏洞 - [PR #12971](https://github.com/containerd/containerd/pull/12971) - **风险级别：** 低（属于防御性加固）
3. ⚠️ 更新Go至1.25.8/1.26.2，包含多个Go运行时安全修复（如crypto/x509, html/template等） - [PR #13011](https://github.com/containerd/containerd/pull/13011) - **风险级别：** 中（修复了Go标准库中的安全漏洞）

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复绝对符号链接处理：解决使用Go 1.24时，因/etc/passwd或/etc/group为绝对符号链接导致容器创建失败的问题 - [PR #13015](https://github.com/containerd/containerd/pull/13015) - **影响：** 使用NixOS风格镜像或类似配置的系统将无法创建容器
2. 修复tar提取中的TOCTOU竞争条件：增强安全性，防止潜在的竞争条件攻击 - [PR #12971](https://github.com/containerd/containerd/pull/12971) - **影响：** 降低在镜像提取过程中因竞争条件导致的安全风险
3. 修复并行解压时忽略whiteout文件的问题：确保在启用`max_concurrent_unpacks`时，被删除的文件正确隐藏 - [PR #13125](https://github.com/containerd/containerd/pull/13125) - **影响：** 已删除的文件可能错误地出现在容器文件系统中，导致应用行为异常
4. 为/etc/group应用绝对符号链接解析：扩展修复范围，确保组信息查找也支持绝对符号链接 - [PR #13019](https://github.com/containerd/containerd/pull/13019) - **影响：** 与上述/etc/passwd问题类似，影响用户组解析和容器启动

## 💥 破坏性变更
1. 🚨 无明显的破坏性变更。此版本主要为向后兼容的Bug修复和安全更新。

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 修复特权容器cgroup挂载选项，防止意外修改主机cgroup设置 - [PR #13120](https://github.com/containerd/containerd/pull/13120)
2. 确保UpdatePodSandbox返回正确的Unimplemented错误码，改善Kubernetes兼容性 - [PR #13023](https://github.com/containerd/containerd/pull/13023)
3. 修复并行解压时忽略whiteout文件的问题，确保文件系统层正确性 - [PR #13125](https://github.com/containerd/containerd/pull/13125)
4. 更新runc至v1.3.5，包含上游修复和改进 - [PR #13061](https://github.com/containerd/containerd/pull/13061)

## 🚀 性能优化
1. 在差异计算中启用挂载管理器，修复使用某些快照程序（如EROFS）时的层提取错误 - [PR #13198](https://github.com/containerd/containerd/pull/13198) - **提升：** 提高与特定文件系统和快照程序的兼容性，减少提取失败
2. 更新Go版本至1.25.9和1.26.2，通常包含性能改进和垃圾回收优化 - [PR #13190](https://github.com/containerd/containerd/pull/13190) - **提升：** 整体运行时性能和稳定性提升

## 🎯 风险评估
整体风险评估：**低风险**。这是一个补丁版本，主要包含关键Bug修复和安全更新，未引入新功能或架构变更。建议在下一个维护窗口安排升级。需要特别关注的方面是：1) 特权容器的cgroup行为变化；2) 绝对符号链接处理的修复是否会影响现有基于NixOS或类似定制镜像的容器。升级后应监控容器创建成功率和运行时稳定性。

## 📋 升级建议
1. **建议尽快安排升级**，特别是如果您使用NixOS风格镜像、启用了并行解压(`max_concurrent_unpacks > 1`)，或运行特权容器。
2. 升级前，请在测试环境中验证与您的工作负载的兼容性，重点关注容器创建和镜像拉取流程。
3. 如果您的环境对安全性要求高，应优先考虑此版本，因为它包含了Go语言的安全修复和一个CVE修复。
4. 升级时，建议同时将`runc`更新至v1.3.5，以获取完整的运行时修复。
5. 对于使用Windows容器并采用进程隔离的场景，此版本修复了客户端挂载根目录的支持，相关用户应进行验证。

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