# Containerd 版本发布分析报告
## containerd 2.1.8 (v2.1.8)

### 📋 版本信息
- **版本标签：** v2.1.8
- **版本名称：** containerd 2.1.8
- **发布时间：** 2026-06-02T18:58:41Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.1.8

### 🔍 分析统计
- **分析时间：** 2026-06-02 19:39:49
- **分析的 PR 数量：** 11
- **分析的 Issue 数量：** 1
- **重要项目数量：** 10

## 📊 版本概述
Error calling LLM API: 401 Client Error: Unauthorized for url: https://qianfan.baidubce.com/v2/chat/completions

## 📋 Release 包含的变更

### PR #13249: [release/2.1] Add GitHub Action for k8s node e2e tests
- **链接：** https://github.com/containerd/containerd/pull/13249
- **状态：** closed
- **已合并：** 是
- **作者：** chrishenzie
- **标签：** size/L, github_actions
- **变更说明：**
  **PR #13249:** [release/2.1] Add GitHub Action for k8s node e2e tests
**标签:** size/L, github_actions

**原始PR #13247:** [release/2.2] Parameterize K8s version in node-e2e workflow
**原始PR标签:** size/XS, github_actions
**原始PR内容:** Manual backport of https://github.com/containerd/containerd/pull/13234

**Cherry-pick PR内容:** Backport the k8s node e2e workflow from release/2.2: https://github.com/cont...

### PR #13272: [release/2.1] backport: sandbox: forward Create fields, fix event topics
- **链接：** https://github.com/containerd/containerd/pull/13272
- **状态：** closed
- **已合并：** 是
- **作者：** estesp
- **标签：** impact/changelog, kind/bug, area/runtime, size/L
- **变更说明：**
  **PR #13272:** [release/2.1] backport: sandbox: forward Create fields, fix event topics
**标签:** impact/changelog, kind/bug, area/runtime, size/L

**PR内容:** The gRPC sandbox controller service only forwarded the `options` field when calling the local controller. The `netns_path`, `rootfs`, and `annotations` fields were silently dropped, causing clients using the gRPC proxy path to receive incomp...

### PR #13274: [release/2.1] apparmor: Set abi conditionally
- **链接：** https://github.com/containerd/containerd/pull/13274
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/S, go
- **变更说明：**
  **PR #13274:** [release/2.1] apparmor: Set abi conditionally
**标签:** impact/changelog, area/runtime, size/S, go

**原始PR #13268:** apparmor: Set abi conditionally
**原始PR标签:** kind/bug, cherry-pick/1.7.x, size/S, cherry-pick/2.0.x, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** The "abi" keyword was added for apparmor 3.0
The original change to add this ended up breaking versions < 3.0. Th...

### PR #13297: [release/2.1] Support both styles of volatile mount option
- **链接：** https://github.com/containerd/containerd/pull/13297
- **状态：** closed
- **已合并：** 是
- **作者：** chrishenzie
- **标签：** impact/changelog, area/snapshotters, size/M
- **变更说明：**
  **PR #13297:** [release/2.1] Support both styles of volatile mount option
**标签:** impact/changelog, area/snapshotters, size/M

**原始PR #13256:** Support both styles of volatile mount option
**原始PR标签:** kind/bug, cherry-pick/1.7.x, size/M, cherry-picked/2.1.x, cherry-picked/2.2.x
**原始PR内容:** Kernel 6.12.80+ returns `fsync=volatile` instead of just `volatile` in mount options, which breaks contain...

### PR #13489: [release/2.1] Prepare release notes for v2.1.8
- **链接：** https://github.com/containerd/containerd/pull/13489
- **状态：** closed
- **已合并：** 是
- **作者：** cpuguy83
- **标签：** size/M
- **变更说明：**
  **PR #13489:** [release/2.1] Prepare release notes for v2.1.8
**标签:** size/M

**原始PR #13272:** [release/2.1] backport: sandbox: forward Create fields, fix event topics
**原始PR标签:** impact/changelog, kind/bug, area/runtime, size/L
**原始PR内容:** The gRPC sandbox controller service only forwarded the `options` field when calling the local controller. The `netns_path`, `rootfs`, and `annotations` fiel...

### PR #13497: [release/2.1] oci: return explicit error for out-of-range USER values
- **链接：** https://github.com/containerd/containerd/pull/13497
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/M
- **变更说明：**
  **PR #13497:** [release/2.1] oci: return explicit error for out-of-range USER values
**标签:** impact/changelog, area/runtime, size/M

**原始PR #13448:** [release/2.2] oci: return explicit error for out-of-range USER values
**原始PR标签:** impact/changelog, area/runtime, size/M
**原始PR内容:** ```release-note
Fix handling of out-of-range USER values in OCI spec to avoid unexpected username/group lookups
``...

---
*本报告由 Containerd Release Tracker 自动生成*