# Containerd 版本发布分析报告
## containerd 2.3.5 (v2.3.5)

### 📋 版本信息
- **版本标签：** v2.3.5
- **版本名称：** containerd 2.3.5
- **发布时间：** 2026-09-04T20:49:28Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.5

### 🔍 分析统计
- **分析时间：** 2026-09-04 21:39:47
- **分析的 PR 数量：** 19
- **分析的 Issue 数量：** 2
- **重要项目数量：** 16

## 📊 版本概述
Error calling LLM API: 401 Client Error: Unauthorized for url: https://qianfan.baidubce.com/v2/chat/completions

## 📋 Release 包含的变更

### PR #34: Add graphite metrics support
- **链接：** https://github.com/containerd/containerd/pull/34
- **状态：** closed
- **已合并：** 是
- **作者：** LK4D4
- **变更说明：**
  **PR #34:** Add graphite metrics support

**PR内容:** I tried with https://github.com/hopsoft/docker-graphite-statsd and it
looks pretty nice. We can see how different metrics depends on a number of
containers and find bottlenecks under heavy load.
...

### PR #13921: [release/2.3] Add more context to the shim delete error
- **链接：** https://github.com/containerd/containerd/pull/13921
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/M
- **变更说明：**
  **PR #13921:** [release/2.3] Add more context to the shim delete error
**标签:** impact/changelog, area/runtime, size/M

**原始PR #13912:** Add more context to the shim delete error
**原始PR标签:** size/M, cherry-picked/2.3.x
**原始PR内容:** When a shim delete hits a timeout, currently the error message does not indicate that the delete was killed rather than failed to complete.

Adds more context to the...

### PR #13983: [release/2.3] fix(runtime): apply load timeout to load shim
- **链接：** https://github.com/containerd/containerd/pull/13983
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/M
- **变更说明：**
  **PR #13983:** [release/2.3] fix(runtime): apply load timeout to load shim
**标签:** impact/changelog, area/runtime, size/M

**原始PR #13954:** fix(runtime): apply load timeout to load shim
**原始PR标签:** size/M, cherry-pick/2.3.x
**原始PR内容:** Carries #13852

This change applies the `io.containerd.timeout.shim.load` budget to all of shim manager load shim and `io.containerd.timeout.shim.cleanup` to c...

### PR #13990: [release/2.3] update runhcs to v0.15.0-rc.4
- **链接：** https://github.com/containerd/containerd/pull/13990
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS
- **变更说明：**
  **PR #13990:** [release/2.3] update runhcs to v0.15.0-rc.4
**标签:** size/XS

**原始PR #13984:** update runhcs to v0.15.0-rc.4
**原始PR标签:** cherry-picked/2.3.x
**原始PR内容:** full diff: https://github.com/microsoft/hcsshim/compare/v0.15.0-rc.3...v0.15.0-rc.4

**Cherry-pick PR内容:** This is an automated cherry-pick of #13984

/assign thaJeztah...

### PR #13995: [release/2.3] Revert "add check on version of drop in configs"
- **链接：** https://github.com/containerd/containerd/pull/13995
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/S
- **变更说明：**
  **PR #13995:** [release/2.3] Revert "add check on version of drop in configs"
**标签:** impact/changelog, area/runtime, size/S

**原始PR #13939:** Revert "add check on version of drop in configs"
**原始PR标签:** size/S, cherry-pick/2.3.x
**原始PR内容:** This reverts commit 21248d00762ec572772c41e3bbb69a518e0a0eaf.

Since the config merge now happens after migration, the version check need not be performe...

### PR #13999: [release/2.3] pkg/oci: resolve rootfs symlinks for user lookup
- **链接：** https://github.com/containerd/containerd/pull/13999
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/XL
- **变更说明：**
  **PR #13999:** [release/2.3] pkg/oci: resolve rootfs symlinks for user lookup
**标签:** impact/changelog, area/runtime, size/XL

**原始PR #13818:** pkg/oci: resolve rootfs symlinks for user lookup
**原始PR标签:** size/XL, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** Some rootfs may use symlinks for /etc/passwd and /etc/group. For example,
NixOS uses absolute symlinks to files in /nix/store. os...

### PR #14030: [release/2.3] docker fetcher: strip sensitive headers on descriptor URLs
- **链接：** https://github.com/containerd/containerd/pull/14030
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, kind/enhancement, size/L, area/distribution
- **变更说明：**
  **PR #14030:** [release/2.3] docker fetcher: strip sensitive headers on descriptor URLs
**标签:** impact/changelog, kind/enhancement, size/L, area/distribution

**原始PR #12889:** docker fetcher: strip sensitive headers on descriptor URLs
**原始PR标签:** kind/enhancement, cherry-picked/1.7.x, size/L, area/distribution, cherry-picked/2.0.x, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** # docker f...

### PR #14048: [release/2.3] vendor: github.com/containerd/platforms v1.0.0-rc.5
- **链接：** https://github.com/containerd/containerd/pull/14048
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/M
- **变更说明：**
  **PR #14048:** [release/2.3] vendor: github.com/containerd/platforms v1.0.0-rc.5
**标签:** size/M

**原始PR #14001:** vendor: github.com/containerd/platforms v1.0.0-rc.5
**原始PR标签:** cherry-picked/2.3.x
**原始PR内容:** - relates to https://github.com/moby/moby/issues/53397

### vendor: github.com/containerd/platforms v1.0.0-rc.5

- Fix WS2022 compat on hosts past the latest LTSC

full diff: https:...

### PR #14049: [release/2.3] pkg/tracing: handle error and typed-nil Stringer attributes
- **链接：** https://github.com/containerd/containerd/pull/14049
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/M
- **变更说明：**
  **PR #14049:** [release/2.3] pkg/tracing: handle error and typed-nil Stringer attributes
**标签:** impact/changelog, area/runtime, size/M

**原始PR #14013:** pkg/tracing: handle error and typed-nil Stringer attributes
**原始PR标签:** size/M, cherry-picked/2.3.x
**原始PR内容:** noticed this code, and recently had a similar issue in logrus;

- https://github.com/sirupsen/logrus/issues/1580
- https://githu...

### PR #14059: [release/2.3] update runc to v1.5.1
- **链接：** https://github.com/containerd/containerd/pull/14059
- **状态：** closed
- **已合并：** 是
- **作者：** thaJeztah
- **标签：** size/XS
- **变更说明：**
  **PR #14059:** [release/2.3] update runc to v1.5.1
**标签:** size/XS

**PR内容:** backports;

- https://github.com/containerd/containerd/pull/13673
- https://github.com/containerd/containerd/pull/13791...

---
*本报告由 Containerd Release Tracker 自动生成*