# Containerd 版本发布分析报告
## containerd 2.4.1 (v2.4.1)

### 📋 版本信息
- **版本标签：** v2.4.1
- **版本名称：** containerd 2.4.1
- **发布时间：** 2026-09-24T23:40:25Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.4.1

### 🔍 分析统计
- **分析时间：** 2026-09-25 00:39:53
- **分析的 PR 数量：** 18
- **分析的 Issue 数量：** 2
- **重要项目数量：** 13

## 📊 版本概述
Error calling LLM API: 401 Client Error: Unauthorized for url: https://qianfan.baidubce.com/v2/chat/completions

## 📋 Release 包含的变更

### PR #14179: [release/2.4] vendor: github.com/fxamacker/cbor/v2 v2.9.4
- **链接：** https://github.com/containerd/containerd/pull/14179
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/L
- **变更说明：**
  **PR #14179:** [release/2.4] vendor: github.com/fxamacker/cbor/v2 v2.9.4
**标签:** size/L

**原始PR #14174:** vendor: github.com/fxamacker/cbor/v2 v2.9.4
**原始PR标签:** size/L, cherry-pick/2.4.x
**原始PR内容:** update to the latest version, which fixes various potential panics.

full diff: https://github.com/fxamacker/cbor/compare/v2.9.1...v2.9.4

**Cherry-pick PR内容:** This is an automated cherry-pick o...

### PR #14188: [release/2.4] ctr: disable slice flag separator on commands
- **链接：** https://github.com/containerd/containerd/pull/14188
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/L, area/ctr
- **变更说明：**
  **PR #14188:** [release/2.4] ctr: disable slice flag separator on commands
**标签:** impact/changelog, size/L, area/ctr

**原始PR #14185:** ctr: disable slice flag separator on commands
**原始PR标签:** size/L, cherry-picked/2.4.x
**原始PR内容:** In urfave/cli/v3, child commands do not inherit
DisableSliceFlagSeparator from the root command, unlike in urfave/cli/v2. When containerd migrated to v3 in commit...

### PR #14197: [release/2.4] remotes: revert closing fetch readers at EOF
- **链接：** https://github.com/containerd/containerd/pull/14197
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/L, area/distribution
- **变更说明：**
  **PR #14197:** [release/2.4] remotes: revert closing fetch readers at EOF
**标签:** impact/changelog, size/L, area/distribution

**原始PR #14194:** remotes: revert closing fetch readers at EOF
**原始PR标签:** size/L, cherry-pick/2.4.x
**原始PR内容:** Revert #13438 to restore registry-cache upload retries, addressing the regression blocking BuildKit containerd v2.4.0 upgrade in https://github.com/moby/build...

### PR #14200: [release/2.4] core/unpack: don't honor id-mapping labels from image annotations
- **链接：** https://github.com/containerd/containerd/pull/14200
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/snapshotters, size/M
- **变更说明：**
  **PR #14200:** [release/2.4] core/unpack: don't honor id-mapping labels from image annotations
**标签:** impact/changelog, area/snapshotters, size/M

**原始PR #13855:** core/unpack: don't honor id-mapping labels from image annotations
**原始PR标签:** cherry-pick/1.7.x, size/M, cherry-pick/2.0.x, cherry-pick/2.2.x, cherry-pick/2.3.x, cherry-picked/2.4.x
**原始PR内容:** The unpacker turns each image layer de...

### PR #14212: [release/2.4] cri: tolerate wrapped ENOTSUP during relabel
- **链接：** https://github.com/containerd/containerd/pull/14212
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/XS
- **变更说明：**
  **PR #14212:** [release/2.4] cri: tolerate wrapped ENOTSUP during relabel
**标签:** impact/changelog, area/cri, size/XS

**原始PR #14207:** cri: tolerate wrapped ENOTSUP during relabel
**原始PR标签:** size/XS, cherry-picked/2.2.x, cherry-picked/2.3.x, cherry-picked/2.4.x
**原始PR内容:** `label.Relabel` can return an `*os.PathError` wrapping `syscall.ENOTSUP` when the source filesystem does not support SELi...

### PR #14215: [release/2.4] ctr: fix flag parsing issues in run, containers create, tasks exec, and oci-hook
- **链接：** https://github.com/containerd/containerd/pull/14215
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/L, area/ctr
- **变更说明：**
  **PR #14215:** [release/2.4] ctr: fix flag parsing issues in run, containers create, tasks exec, and oci-hook
**标签:** impact/changelog, size/L, area/ctr

**原始PR #14209:** ctr: fix flag parsing issues in run, containers create, tasks exec, and oci-hook
**原始PR标签:** size/L
**原始PR内容:** Fixes https://github.com/containerd/containerd/issues/14208

**Cherry-pick PR内容:** This is an automated cherry-pic...

### PR #14219: [release/2.4] ctr: preserve args after "-" in images export
- **链接：** https://github.com/containerd/containerd/pull/14219
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/L, area/ctr
- **变更说明：**
  **PR #14219:** [release/2.4] ctr: preserve args after "-" in images export
**标签:** impact/changelog, size/L, area/ctr

**原始PR #14217:** ctr: preserve args after "-" in images export
**原始PR标签:** size/L, cherry-picked/2.4.x
**原始PR内容:** urfave/cli/v3 breaks out of its flag parsing loop when it encounters a "-" positional argument without appending the remaining arguments, causing "ctr images expor...

### PR #14223: [release/2.4] cri: don't leak task when StartContainer cleanup fails to delete task
- **链接：** https://github.com/containerd/containerd/pull/14223
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/L, kind/resource-leak
- **变更说明：**
  **PR #14223:** [release/2.4] cri: don't leak task when StartContainer cleanup fails to delete task
**标签:** impact/changelog, area/cri, size/L, kind/resource-leak

**原始PR #14218:** cri: don't leak task when StartContainer cleanup fails to delete task
**原始PR标签:** size/L, kind/resource-leak, cherry-pick/2.4.x
**原始PR内容:** When `StartContainer` fails after the task is created and the cleanup task de...

---
*本报告由 Containerd Release Tracker 自动生成*