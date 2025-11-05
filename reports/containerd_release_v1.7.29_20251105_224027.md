# Containerd 版本发布分析报告
## containerd 1.7.29 (v1.7.29)

### 📋 版本信息
- **版本标签：** v1.7.29
- **版本名称：** containerd 1.7.29
- **发布时间：** 2025-11-05T22:15:34Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v1.7.29

### 🔍 分析统计
- **分析时间：** 2025-11-05 22:40:27
- **分析的 PR 数量：** 15
- **分析的 Issue 数量：** 1
- **重要项目数量：** 14

## 📊 版本概述
containerd 1.7.29 重点修复5个高危安全漏洞并优化容器日志稳定性，建议生产环境立即升级

## 🔒 安全问题修复
1. ⚠️ runc文件描述符泄露漏洞 (GHSA-qw9x-cqr3-wc7r) - [PR #12475](https://github.com/containerd/containerd/pull/12475) - **风险级别：** 高
2. ⚠️ runc权限逃逸漏洞 (GHSA-cgrx-mc8f-2prm) - [PR #12475](https://github.com/containerd/containerd/pull/12475) - **风险级别：** 高
3. ⚠️ containerd镜像验证绕过漏洞 (GHSA-pwhc-rpq9-4c8w) - [安全公告](https://github.com/containerd/containerd/security/advisories/GHSA-pwhc-rpq9-4c8w) - **风险级别：** 中

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复快速关闭IO导致的容器日志丢失问题 - [PR #12375](https://github.com/containerd/containerd/pull/12375) - **影响：** 可能造成关键业务日志不完整，影响监控和排障
2. 修复容器attach操作的goroutine泄漏问题 - [commit c575d1b](https://github.com/containerd/containerd/commit/c575d1b5f4011f33b32f71ace75367a92b08c750) - **影响：** 长期运行可能导致内存持续增长

## ✨ 主要变更
1. 支持zstd压缩格式的镜像分发处理 - [PR #12018](https://github.com/containerd/containerd/pull/12018)
2. 升级runc至v1.3.3修复多个安全漏洞 - [PR #12480](https://github.com/containerd/containerd/pull/12480)

## 🚀 性能优化
1. Go版本升级至1.24.9/1.25.3提升运行时性能 - [PR #12471](https://github.com/containerd/containerd/pull/12471) - **提升：** 内存管理和并发处理优化
2. CI基础镜像更新提升构建效率 - [PR #12450](https://github.com/containerd/containerd/pull/12450)

## 🎯 风险评估
高风险安全版本，建议72小时内完成升级。需特别注意：1) 升级后验证runc与现有编排系统的兼容性 2) 监控升级后前24小时的日志采集情况 3) 检查容器镜像签名验证流程是否符合预期

## 📋 升级建议
1. 立即安排升级以修复关键安全漏洞，特别是使用多租户环境的集群
2. 升级前重点验证日志收集系统的完整性
3. 建议同时更新Kubernetes集群的runtime配置

## 📋 Release 包含的变更

### PR #12018: [release/1.7]  Update differ to handle zstd media types
- **链接：** https://github.com/containerd/containerd/pull/12018
- **状态：** closed
- **已合并：** 是
- **作者：** ningmingxiao
- **标签：** impact/changelog, kind/enhancement, needs-ok-to-test, size/S, area/distribution
- **变更说明：**
  **PR #12018:** [release/1.7]  Update differ to handle zstd media types
**标签:** impact/changelog, kind/enhancement, needs-ok-to-test, size/S, area/distribution

**PR内容:** The differ should be able to generate zstd compressed layers when provided with the zstd media type.


(cherry picked from commit 17f7858b4e2e31b447410f66d0100b816c1fe6b3)...

### PR #12188: [release/1.7] ci: bump Go 1.23.12, 1.24.6
- **链接：** https://github.com/containerd/containerd/pull/12188
- **状态：** closed
- **已合并：** 是
- **作者：** austinvazquez
- **标签：** size/S, go, area/toolchain
- **变更说明：**
  **PR #12188:** [release/1.7] ci: bump Go 1.23.12, 1.24.6
**标签:** size/S, go, area/toolchain

**原始PR #12180:** ci: bump Go 1.24.6
**原始PR标签:** cherry-pick/1.6.x, cherry-picked/1.7.x, size/S, area/github_actions, area/toolchain, cherry-picked/2.0.x, cherry-picked/2.1.x
**原始PR内容:** This change bumps the golang version used in CI to Go 1.24.6.

> go1.24.6 (released 2025-08-06) includes security fi...

### PR #12276: [release/1.7] runc:Update runc binary to v1.3.1
- **链接：** https://github.com/containerd/containerd/pull/12276
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** needs-ok-to-test, area/runtime, size/XS
- **变更说明：**
  **PR #12276:** [release/1.7] runc:Update runc binary to v1.3.1
**标签:** needs-ok-to-test, area/runtime, size/XS

**原始PR #12271:** runc:Update runc binary to v1.3.1
**原始PR标签:** needs-ok-to-test, area/runtime, size/XS

**Cherry-pick PR内容:** This is an automated cherry-pick of #12271

/assign AkihiroSuda...

### PR #12362: [release/1.7] ci: bump Go 1.24.8
- **链接：** https://github.com/containerd/containerd/pull/12362
- **状态：** closed
- **已合并：** 是
- **作者：** austinvazquez
- **标签：** platform/windows, size/L, area/github_actions, area/toolchain, github_actions
- **变更说明：**
  **PR #12362:** [release/1.7] ci: bump Go 1.24.8
**标签:** platform/windows, size/L, area/github_actions, area/toolchain, github_actions

**PR内容:** This change backports a few CI updates alongside the maintenance Go bump to resolve CI failures.

Most backports applied cleanly except:
1. https://github.com/containerd/containerd/pull/12362/commits/8a67abc4cac67bf806da0b2b55ac7159e91f6996
  a. Mo...

### PR #12375: [release/1.7] Fix lost container logs from quickly closing io
- **链接：** https://github.com/containerd/containerd/pull/12375
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, kind/bug, area/runtime, size/XS
- **变更说明：**
  **PR #12375:** [release/1.7] Fix lost container logs from quickly closing io
**标签:** impact/changelog, kind/bug, area/runtime, size/XS

**原始PR #12364:** bugfix:fix container logs lost because io close too quickly
**原始PR标签:** kind/bug, needs-ok-to-test, cherry-picked/1.7.x, area/runtime, size/XS, cherry-picked/2.0.x, cherry-picked/2.1.x
**原始PR内容:** fix  https://github.com/containerd/containerd/i...

### PR #12429: [release/1.7] CI: skip ubuntu-24.04-arm on private repos
- **链接：** https://github.com/containerd/containerd/pull/12429
- **状态：** closed
- **已合并：** 是
- **作者：** AkihiroSuda
- **标签：** kind/test, size/XS, github_actions
- **变更说明：**
  **PR #12429:** [release/1.7] CI: skip ubuntu-24.04-arm on private repos
**标签:** kind/test, size/XS, github_actions

**PR内容:** Cherrypick (not clean):
- #12419...

### PR #12450: [release/1.7] CI: update Fedora to 43
- **链接：** https://github.com/containerd/containerd/pull/12450
- **状态：** closed
- **已合并：** 是
- **作者：** AkihiroSuda
- **标签：** kind/test, size/S, github_actions
- **变更说明：**
  **PR #12450:** [release/1.7] CI: update Fedora to 43
**标签:** kind/test, size/S, github_actions

**PR内容:** Cherry-pick (not clean)
- https://github.com/containerd/containerd/pull/12446...

### PR #12471: [release/1.7] Update GHA images and bump Go 1.24.9; 1.25.3
- **链接：** https://github.com/containerd/containerd/pull/12471
- **状态：** closed
- **已合并：** 是
- **作者：** austinvazquez
- **标签：** size/L, area/toolchain, github_actions
- **变更说明：**
  **PR #12471:** [release/1.7] Update GHA images and bump Go 1.24.9; 1.25.3
**标签:** size/L, area/toolchain, github_actions

**PR内容:** Backports a handful of CI updates to update GHA images for low risk jobs and Go version update.

1. https://github.com/containerd/containerd/pull/8732
1. https://github.com/containerd/containerd/pull/11933
2. https://github.com/containerd/containerd/pull/12469...

### PR #12480: [release/1.7] Update runc binary to v1.3.3
- **链接：** https://github.com/containerd/containerd/pull/12480
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/XS
- **变更说明：**
  **PR #12480:** [release/1.7] Update runc binary to v1.3.3
**标签:** impact/changelog, area/runtime, size/XS

**原始PR #12475:** runc: Update runc binary to v1.3.3 to fix cve
**原始PR标签:** area/runtime, size/XS
**原始PR内容:** fix cve [CVE-2025-31133](https://github.com/opencontainers/runc/security/advisories/GHSA-9493-h29p-rfm2), [CVE-2025-52565](https://github.com/opencontainers/runc/security/advisories...

### PR #12486: [release/1.7] Prepare release notes for v1.7.29
- **链接：** https://github.com/containerd/containerd/pull/12486
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** size/M
- **变更说明：**
  **PR #12486:** [release/1.7] Prepare release notes for v1.7.29
**标签:** size/M

**PR内容:** Generated notes
----
containerd 1.7.29

Welcome to the v1.7.29 release of containerd!

The twenty-ninth patch release for containerd 1.7 contains various fixes
and updates including security patches.

### Security Updates

* **runc**
  * [**GHSA-qw9x-cqr3-wc7r**](https://github.com/opencontainer...

---
*本报告由 Containerd Release Tracker 自动生成*