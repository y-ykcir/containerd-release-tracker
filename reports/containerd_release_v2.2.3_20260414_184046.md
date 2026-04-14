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
- **分析时间：** 2026-04-14 18:40:46
- **分析的 PR 数量：** 19
- **分析的 Issue 数量：** 2
- **重要项目数量：** 17

## 📊 版本概述
containerd 2.2.3 是一个重要的稳定性和安全性补丁版本，主要修复了特权容器cgroup挂载、Go 1.24兼容性、并行解压以及一个TOCTOU安全漏洞。

## 🔒 安全问题修复
1. ⚠️ 更新spdystream依赖以修复CVE-2026-35469 - [PR #13217](https://github.com/containerd/containerd/pull/13217) - **风险级别：** 中（具体细节需参考上游公告）
2. ⚠️ 修复tar解压中的TOCTOU竞争条件漏洞 - [PR #12971](https://github.com/containerd/containerd/pull/12971) - **风险级别：** 中
3. ⚠️ 更新Go版本至1.25.8，包含多个安全修复（crypto/x509, html/template, net/url, os等） - [PR #13011](https://github.com/containerd/containerd/pull/13011) - **风险级别：** 中

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复TOCTOU竞争条件漏洞，防止tar解压过程中的竞态条件 - [PR #12971](https://github.com/containerd/containerd/pull/12971) - **影响：** 在镜像拉取和容器创建过程中存在潜在的安全和稳定性风险
2. 修复Go 1.24中因绝对符号链接导致的容器创建失败问题 - [PR #13015](https://github.com/containerd/containerd/pull/13015) - **影响：** 使用NixOS风格镜像（如`docker.io/nixos/nix`）时无法创建容器 - [Issue #12683](https://github.com/containerd/containerd/issues/12683)
3. 修复并行解压时whiteout文件被忽略的问题 - [PR #13125](https://github.com/containerd/containerd/pull/13125) - **影响：** 当`max_concurrent_unpacks > 1`时，已删除的文件可能错误地出现在最终文件系统中 - [Issue #13030](https://github.com/containerd/containerd/issues/13030)
4. 启用diff walking中的挂载管理器，修复某些快照器（如EROFS）的层提取错误 - [PR #13198](https://github.com/containerd/containerd/pull/13198) - **影响：** 在使用特定快照器时可能无法成功拉取或创建镜像

## ✨ 主要变更
1. 修复特权容器cgroup挂载选项，防止意外更改主机cgroup设置 - [PR #13120](https://github.com/containerd/containerd/pull/13120)
2. 确保CRI的UpdatePodSandbox接口返回正确的Unimplemented错误码 - [PR #13023](https://github.com/containerd/containerd/pull/13023)
3. 修复并行解压时忽略whiteout文件的问题 - [PR #13125](https://github.com/containerd/containerd/pull/13125)
4. 更新runc至v1.3.5版本 - [PR #13061](https://github.com/containerd/containerd/pull/13061)

## 🚀 性能优化
1. 启用diff walking中的挂载管理器，改善特定快照器的层提取可靠性 - [PR #13198](https://github.com/containerd/containerd/pull/13198) - **提升：** 修复了EROFS等快照器的提取失败问题，提升了兼容性

## 🎯 风险评估
整体风险评估：**中等偏低**。这是一个补丁版本，主要包含向后兼容的bug修复和安全更新。升级风险主要来自依赖项更新（如runc v1.3.5）和特权容器cgroup行为的细微调整。建议在测试环境中充分验证后，于维护窗口安排生产环境升级。需要特别关注升级后特权容器的行为以及使用NixOS镜像的服务的启动情况。

## 📋 升级建议
1. **强烈建议升级**：此版本包含重要的安全修复（CVE-2026-35469和TOCTOU漏洞）和稳定性修复，特别是对于使用NixOS镜像或并行解压功能的用户。
2. 升级前，请在测试环境中验证特权容器的cgroup行为，确保与您的安全策略兼容。
3. 如果您的环境使用NixOS风格的容器镜像，此版本解决了Go 1.24引入的兼容性问题，升级后应能恢复正常。
4. 建议同时将runc升级至v1.3.5，以获取其包含的修复。
5. 升级后，监控容器创建和镜像拉取日志，确保whiteout文件处理和并行解压功能正常。

## 📋 Release 包含的变更

### PR #12971: [release/2.2] Fix TOCTOU race bug in tar extraction
- **链接：** https://github.com/containerd/containerd/pull/12971
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/XS, area/distribution
- **变更说明：**
  修复tar解压过程中的TOCTOU（检查时间与使用时间）竞争条件漏洞，应用了安全加固措施。

### PR #13011: [release/2.2 backport] update to go1.25.8, test go1.26.1
- **链接：** https://github.com/containerd/containerd/pull/13011
- **状态：** closed
- **已合并：** 是
- **作者：** thaJeztah
- **标签：** size/S, go, area/toolchain
- **变更说明：**
  将Go版本更新至1.25.8（包含安全修复），并测试Go 1.26.1。

### PR #13015: [release/2.2] fix(oci): handle absolute symlinks in rootfs user lookup
- **链接：** https://github.com/containerd/containerd/pull/13015
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/L, go, area/client
- **变更说明：**
  修复Go 1.24引入的严格路径验证导致容器无法解析根文件系统中绝对符号链接（如NixOS中的`/etc/passwd`）的问题。通过`openUserFile`助手函数重新锚定绝对符号链接路径。

### PR #13019: [release/2.2] fix(oci): apply absolute symlink resolution to /etc/group
- **链接：** https://github.com/containerd/containerd/pull/13019
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/M, go
- **变更说明：**
  作为PR #12732的后续修复，将绝对符号链接解析逻辑同样应用于`/etc/group`文件的查找，确保在OCI用户/组解析的所有路径中都能正确处理NixOS风格的绝对符号链接。

### PR #13023: [release/2.2] cri: UpdatePodSandbox should return Unimplemented
- **链接：** https://github.com/containerd/containerd/pull/13023
- **状态：** closed
- **已合并：** 是
- **作者：** samuelkarp
- **标签：** impact/changelog, area/cri, size/XS
- **变更说明：**
  确保CRI的`UpdatePodSandbox` API返回正确的gRPC `Unimplemented`状态码，而非通用错误。

### PR #13061: [release/2.2] update runc binary to v1.3.5
- **链接：** https://github.com/containerd/containerd/pull/13061
- **状态：** closed
- **已合并：** 是
- **作者：** thaJeztah
- **标签：** impact/changelog, area/runtime, size/XS
- **变更说明：**
  将runc二进制文件更新至v1.3.5版本。

### PR #13066: [release/2.2] Fix vagrant on CI
- **链接：** https://github.com/containerd/containerd/pull/13066
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS
- **变更说明：**
  修复CI环境中Vagrant因磁盘分区无法扩容而失败的问题。

### PR #13120: [release/2.2] Preserve cgroup mount options for privileged containers
- **链接：** https://github.com/containerd/containerd/pull/13120
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/L
- **变更说明：**
  修复特权容器因硬编码cgroup挂载选项而意外剥离主机cgroup2 VFS超级块选项（如`nsdelegate`）的问题。解决方案是在容器创建时读取主机的`/sys/fs/cgroup`挂载选项并显式包含。包含集成测试验证。

### PR #13125: [release/2.2] Tweak mount info for overlayfs in case of parallel unpack
- **链接：** https://github.com/containerd/containerd/pull/13125
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/snapshotters, size/L
- **变更说明：**
  修复当`max_concurrent_unpacks > 1`时，overlayfs并行解包会忽略白文件（whiteout）的bug。通过调整unpacker逻辑而非直接修改overlay snapshotter来解决问题。

### PR #13154: [release/2.2] Skip TestExportAndImportMultiLayer on s390x
- **链接：** https://github.com/containerd/containerd/pull/13154
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** kind/test, size/XS
- **变更说明：**
  在s390x架构上跳过`TestExportAndImportMultiLayer`测试，因为测试镜像`ghcr.io/containerd/volume-copy-up:2.1`不包含该架构的manifest，导致测试失败。

---
*本报告由 Containerd Release Tracker 自动生成*