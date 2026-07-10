# Containerd 版本发布分析报告
## containerd 2.3.3 (v2.3.3)

### 📋 版本信息
- **版本标签：** v2.3.3
- **版本名称：** containerd 2.3.3
- **发布时间：** 2026-07-10T00:04:40Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.3

### 🔍 分析统计
- **分析时间：** 2026-07-10 00:39:51
- **分析的 PR 数量：** 20
- **分析的 Issue 数量：** 3
- **重要项目数量：** 13

## 📊 版本概述
Error calling LLM API: 401 Client Error: Unauthorized for url: https://qianfan.baidubce.com/v2/chat/completions

## 📋 Release 包含的变更

### PR #13632: [release/2.3] erofs: align default mkfs block size across platforms
- **链接：** https://github.com/containerd/containerd/pull/13632
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/snapshotters, size/XS
- **变更说明：**
  **PR #13632:** [release/2.3] erofs: align default mkfs block size across platforms
**标签:** impact/changelog, area/snapshotters, size/XS

**原始PR #13624:** erofs: align default mkfs block size across platforms
**原始PR标签:** size/XS, cherry-picked/2.3.x
**原始PR内容:** Force a 4K block size on all platforms rather than only on darwin. An explicit caller-supplied `-b` is still respected.

**Cherry-pick P...

### PR #13643: [release/2.3] test: fix flaky image timestamp check on coarse clocks
- **链接：** https://github.com/containerd/containerd/pull/13643
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/S
- **变更说明：**
  **PR #13643:** [release/2.3] test: fix flaky image timestamp check on coarse clocks
**标签:** size/S

**原始PR #13588:** test: fix flaky image timestamp check on coarse clocks
**原始PR标签:** size/S, cherry-picked/2.3.x
**原始PR内容:** TestImagesCreateUpdateDelete asserts that an image's updatedat is strictly after its createdat. Both timestamps are stamped via time.Now().UTC(), which strips the monotonic ...

### PR #13645: [release/2.3] Add defer in event of mid-function failures in RunPodSandbox to avoid mount leaks
- **链接：** https://github.com/containerd/containerd/pull/13645
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/S
- **变更说明：**
  **PR #13645:** [release/2.3] Add defer in event of mid-function failures in RunPodSandbox to avoid mount leaks
**标签:** impact/changelog, area/cri, size/S

**原始PR #13399:** Add defer in event of mid-function failures in RunPodSandbox to avoid mount leaks
**原始PR标签:** ok-to-test, size/S, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** - Fixes https://github.com/containerd/containerd/issues/13...

### PR #13666: [release/2.3] update runhcs to v0.15.0-rc.2
- **链接：** https://github.com/containerd/containerd/pull/13666
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS
- **变更说明：**
  **PR #13666:** [release/2.3] update runhcs to v0.15.0-rc.2
**标签:** size/XS

**原始PR #13659:** update runhcs to v0.15.0-rc.2
**原始PR标签:** size/XS, cherry-picked/2.3.x
**原始PR内容:** full diff: https://github.com/microsoft/hcsshim/compare/v0.15.0-rc.1...v0.15.0-rc.2

**Cherry-pick PR内容:** This is an automated cherry-pick of #13659

/assign thaJeztah...

### PR #13668: [release/2.3] cri: reject CreateContainer when sandbox is not running
- **链接：** https://github.com/containerd/containerd/pull/13668
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/XS
- **变更说明：**
  **PR #13668:** [release/2.3] cri: reject CreateContainer when sandbox is not running
**标签:** impact/changelog, area/cri, size/XS

**原始PR #13654:** cri: reject CreateContainer when sandbox is not running
**原始PR标签:** size/XS, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** ## What does this PR do?

`CreateContainer` currently proceeds without checking whether the sandbox is in a running (`St...

### PR #13686: [release/2.3] Update to current setup-go version
- **链接：** https://github.com/containerd/containerd/pull/13686
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS
- **变更说明：**
  **PR #13686:** [release/2.3] Update to current setup-go version
**标签:** size/XS

**原始PR #13516:** Update to current setup-go version
**原始PR标签:** cherry-pick/1.7.x, size/XS, cherry-pick/2.0.x, cherry-pick/2.1.x, cherry-pick/2.2.x, cherry-pick/2.3.x
**原始PR内容:** Update the setup-go version in our private action yml to:

1) be pinned by hash (with comment to version string)
2) remove cache disab...

### PR #13693: [release/2.3] update runhcs to v0.15.0-rc.3
- **链接：** https://github.com/containerd/containerd/pull/13693
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS
- **变更说明：**
  **PR #13693:** [release/2.3] update runhcs to v0.15.0-rc.3
**标签:** size/XS

**原始PR #13691:** update runhcs to v0.15.0-rc.3
**原始PR标签:** size/XS, cherry-pick/2.3.x
**原始PR内容:** - relates to https://github.com/containerd/containerd/pull/13684
- relates to https://github.com/containerd/containerd/pull/13690

full diff: https://github.com/microsoft/hcsshim/compare/v0.15.0-rc.2...v0.15.0-rc.3

**Ch...

### PR #13694: [release/2.3] Set SystemTemp env var to config temp on Windows
- **链接：** https://github.com/containerd/containerd/pull/13694
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, platform/windows, size/M
- **变更说明：**
  **PR #13694:** [release/2.3] Set SystemTemp env var to config temp on Windows
**标签:** impact/changelog, platform/windows, size/M

**原始PR #13667:** Set SystemTemp env var to config temp on Windows
**原始PR标签:** cherry-pick/1.7.x, size/M, cherry-pick/2.0.x, cherry-pick/2.1.x, cherry-pick/2.2.x, cherry-pick/2.3.x
**原始PR内容:** Since Go 1.21, os.MkdirTemp/os.TempDir resolve the temp directory via Windo...

### PR #13697: [release/2.3] Fix nil pointer dereference in NRI GetIPs
- **链接：** https://github.com/containerd/containerd/pull/13697
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/cri, size/M
- **变更说明：**
  **PR #13697:** [release/2.3] Fix nil pointer dereference in NRI GetIPs
**标签:** impact/changelog, area/cri, size/M

**原始PR #13683:** Fix nil pointer dereference in NRI GetIPs
**原始PR标签:** size/M, cherry-picked/2.1.x, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** Adds a `nil` guard to `GetIPs` on `criPodSandbox` before accessing promoted struct fields on the embedded `Sandbox` pointer.

D...

### PR #13711: [release/2.3] ci: pin fog-json to resolve gem conflict
- **链接：** https://github.com/containerd/containerd/pull/13711
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS
- **变更说明：**
  **PR #13711:** [release/2.3] ci: pin fog-json to resolve gem conflict
**标签:** size/XS

**原始PR #13707:** ci: pin fog-json to resolve gem conflict
**原始PR标签:** cherry-picked/1.7.x, size/XS, cherry-picked/2.0.x, cherry-picked/2.1.x, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** Vagrant 2.4.x bundles an embedded Ruby 3.3.0 runtime that loads the default specification json-2.7.2 during initial...

---
*本报告由 Containerd Release Tracker 自动生成*