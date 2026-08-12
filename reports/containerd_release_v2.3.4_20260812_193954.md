# Containerd 版本发布分析报告
## containerd 2.3.4 (v2.3.4)

### 📋 版本信息
- **版本标签：** v2.3.4
- **版本名称：** containerd 2.3.4
- **发布时间：** 2026-08-12T17:59:47Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.4

### 🔍 分析统计
- **分析时间：** 2026-08-12 19:39:54
- **分析的 PR 数量：** 22
- **分析的 Issue 数量：** 2
- **重要项目数量：** 16

## 📊 版本概述
Error calling LLM API: 401 Client Error: Unauthorized for url: https://qianfan.baidubce.com/v2/chat/completions

## 📋 Release 包含的变更

### PR #13454: [release/2.3] Handle []byte envvar value for CRI
- **链接：** https://github.com/containerd/containerd/pull/13454
- **状态：** closed
- **已合并：** 是
- **作者：** liggitt
- **标签：** impact/changelog, area/cri, ok-to-test, size/L
- **变更说明：**
  **PR #13454:** [release/2.3] Handle []byte envvar value for CRI
**标签:** impact/changelog, area/cri, ok-to-test, size/L

**PR内容:** Part of recovering from a regression in the ability of v0.34.0+ cri-api being able to transmit binary non-utf8 envvar values

xref
* https://github.com/kubernetes/kubernetes/issues/139132
* https://github.com/kubernetes/kubernetes/pull/139168#issuecomment-4501163...

### PR #13734: [release/2.3] Disable checkpoint restore codepath when CRIU is not installed
- **链接：** https://github.com/containerd/containerd/pull/13734
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/XL
- **变更说明：**
  **PR #13734:** [release/2.3] Disable checkpoint restore codepath when CRIU is not installed
**标签:** impact/changelog, area/cri, size/XL

**原始PR #13664:** Disable checkpoint restore codepath when CRIU is not installed
**原始PR标签:** area/cri, area/criu, size/XL, cherry-picked/2.1.x, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** Checkpoint restore was implicated in [several](https://github.co...

### PR #13759: [release/2.3] cri: auto-add prefix for pause image
- **链接：** https://github.com/containerd/containerd/pull/13759
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/S
- **变更说明：**
  **PR #13759:** [release/2.3] cri: auto-add prefix for pause image
**标签:** impact/changelog, area/cri, size/S

**原始PR #13513:** cri: auto-add prefix for pause image
**原始PR标签:** size/S, cherry-pick/2.3.x
**原始PR内容:** fix if  sandbox_image doesn't have docker.io prefix cause run pod failed.

reproduce :


use config 
```
sandbox_image = "rancher/mirrored-pause:3.6"
```
image is exist 
```...

### PR #13778: [release/2.3] fix(cri): introspect OCI runtime features for non-runc runtimes
- **链接：** https://github.com/containerd/containerd/pull/13778
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/L
- **变更说明：**
  **PR #13778:** [release/2.3] fix(cri): introspect OCI runtime features for non-runc runtimes
**标签:** impact/changelog, area/cri, size/L

**原始PR #13504:** Introspect OCI runtime features for non-runc runtimes
**原始PR标签:** impact/changelog, area/cri, size/L, cherry-pick/2.2.x, cherry-pick/2.3.x
**原始PR内容:** ## What this does

Remove the runc-only guard in `introspectRuntimeFeatures` so CRI introspe...

### PR #13785: [release/2.3] ci: bound Go fuzzing by execution count
- **链接：** https://github.com/containerd/containerd/pull/13785
- **状态：** closed
- **已合并：** 是
- **作者：** chrishenzie
- **标签：** size/S
- **变更说明：**
  **PR #13785:** [release/2.3] ci: bound Go fuzzing by execution count
**标签:** size/S

**PR内容:** Go can report context deadline exceeded when a duration-based fuzz limit expires (https://go.dev/issue/75804).

Use a 50,000-execution limit based on the roughly 47,000 executions FuzzImageStore completed in 30 seconds in CI. This keeps work stable across runners and avoids the duration issue.

As...

### PR #13803: [release/2.3] core/runtime/v2: Preserve protobuf shim response bytes
- **链接：** https://github.com/containerd/containerd/pull/13803
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/M
- **变更说明：**
  **PR #13803:** [release/2.3] core/runtime/v2: Preserve protobuf shim response bytes
**标签:** impact/changelog, area/runtime, size/M

**原始PR #13801:** core/runtime/v2: Preserve protobuf shim response bytes
**原始PR标签:** size/M, cherry-picked/2.3.x
**原始PR内容:** Shim start output was trimmed before protobuf decoding. Because arbitrary protobuf fields may legitimately end with whitespace bytes, includi...

### PR #13840: [release/2.3] core/runtime/v2: Drop checkpointctl module dependency
- **链接：** https://github.com/containerd/containerd/pull/13840
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** area/runtime, size/XS
- **变更说明：**
  **PR #13840:** [release/2.3] core/runtime/v2: Drop checkpointctl module dependency
**标签:** area/runtime, size/XS

**原始PR #13839:** core/runtime/v2: Drop checkpointctl module dependency
**原始PR标签:** size/XS, cherry-pick/2.3.x
**原始PR内容:** The shim imported github.com/checkpoint-restore/checkpointctl/lib for a single string constant.
Consumers that embed only the runtime v2 plugin (and never touch...

### PR #13857: [release/2.3] shim_load: Consider shim leaked only if we can't find pids
- **链接：** https://github.com/containerd/containerd/pull/13857
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/L
- **变更说明：**
  **PR #13857:** [release/2.3] shim_load: Consider shim leaked only if we can't find pids
**标签:** impact/changelog, area/runtime, size/L

**原始PR #13790:** shim_load: Consider shim leaked only if we can't find pids
**原始PR标签:** size/L, cherry-pick/2.3.x
**原始PR内容:** Right now the statement is treating any error from the shim as leaking
(len(pInfo == 0 is true for any error). It seems the intent was...

### PR #13868: [release/2.3] cri: deprecate restore in CreateContainer
- **链接：** https://github.com/containerd/containerd/pull/13868
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, impact/deprecation, area/cri, size/L
- **变更说明：**
  **PR #13868:** [release/2.3] cri: deprecate restore in CreateContainer
**标签:** impact/changelog, impact/deprecation, area/cri, size/L

**原始PR #13838:** cri: deprecate restore in CreateContainer
**原始PR标签:** size/L, cherry-picked/2.2.x, cherry-picked/2.3.x

**Cherry-pick PR内容:** This is an automated cherry-pick of #13838

/assign samuelkarp

```release-note
Deprecate checkpoint restore in CreateC...

### PR #13870: [release/2.3] internal/oom: Fix memory leak by removing watcher from map on Stop
- **链接：** https://github.com/containerd/containerd/pull/13870
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, kind/bug, area/runtime, size/M
- **变更说明：**
  **PR #13870:** [release/2.3] internal/oom: Fix memory leak by removing watcher from map on Stop
**标签:** impact/changelog, kind/bug, area/runtime, size/M

**原始PR #13856:** internal/oom: Fix memory leak by removing watcher from map on Stop
**原始PR标签:** kind/bug, size/M, cherry-picked/2.3.x
**原始PR内容:** - Fixes #13853

The `oomWatchers.Stop` method stopped the watcher but never removed it from the...

---
*本报告由 Containerd Release Tracker 自动生成*