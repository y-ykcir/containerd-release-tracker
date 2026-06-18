# Containerd 版本发布分析报告
## containerd 2.3.2 (v2.3.2)

### 📋 版本信息
- **版本标签：** v2.3.2
- **版本名称：** containerd 2.3.2
- **发布时间：** 2026-06-18T23:16:02Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.2

### 🔍 分析统计
- **分析时间：** 2026-06-18 23:39:50
- **分析的 PR 数量：** 18
- **分析的 Issue 数量：** 1
- **重要项目数量：** 15

## 📊 版本概述
Error calling LLM API: 401 Client Error: Unauthorized for url: https://qianfan.baidubce.com/v2/chat/completions

## 📋 Release 包含的变更

### PR #13459: [release/2.3] contrib/checkpoint: increase timeouts to 30s
- **链接：** https://github.com/containerd/containerd/pull/13459
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS
- **变更说明：**
  **PR #13459:** [release/2.3] contrib/checkpoint: increase timeouts to 30s
**标签:** size/XS

**原始PR #13436:** contrib/checkpoint: increase timeouts to 30s
**原始PR标签:** size/XS, cherry-pick/2.2.x, cherry-picked/2.3.x
**原始PR内容:** Under slow network conditions (e.g., simulated 2 Mbps ingress bandwidth limits in CI), restoring a container from a checkpoint can fail if it requires pulling the base imag...

### PR #13512: [release/2.3] runc-shim: don't hold the service lock across runc create
- **链接：** https://github.com/containerd/containerd/pull/13512
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/XS
- **变更说明：**
  **PR #13512:** [release/2.3] runc-shim: don't hold the service lock across runc create
**标签:** impact/changelog, area/runtime, size/XS

**原始PR #13483:** runc-shim: don't hold the service lock across runc create
**原始PR标签:** easy-to-review, size/XS, cherry-pick/2.3.x
**原始PR内容:** The task service guards its containers map with s.mu, and getContainer() takes it on behalf of effectively every task R...

### PR #13522: [release/2.3] core/runtime/v2: fix race on Windows deferredPipeConnection.c in Read
- **链接：** https://github.com/containerd/containerd/pull/13522
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, platform/windows, size/XS
- **变更说明：**
  **PR #13522:** [release/2.3] core/runtime/v2: fix race on Windows deferredPipeConnection.c in Read
**标签:** impact/changelog, platform/windows, size/XS

**原始PR #13462:** core/runtime/v2: fix race on Windows deferredPipeConnection.c in Read
**原始PR标签:** kind/bug, platform/windows, size/XS, cherry-pick/2.2.x, cherry-pick/2.3.x
**原始PR内容:** Read short-circuited on `if dpc.c == nil` before calling `dp...

### PR #13568: [release/2.3] Configure udevd children-max for root-test
- **链接：** https://github.com/containerd/containerd/pull/13568
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS
- **变更说明：**
  **PR #13568:** [release/2.3] Configure udevd children-max for root-test
**标签:** size/XS

**原始PR #13562:** Configure udevd children-max for root-test
**原始PR标签:** cherry-picked/1.7.x, size/XS, cherry-picked/2.0.x, cherry-picked/2.1.x, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** GHA runners occasionally experience I/O constraints during root-test test execution. While concurrent tests rap...

### PR #13580: [release/2.3] update go to 1.26.4
- **链接：** https://github.com/containerd/containerd/pull/13580
- **状态：** closed
- **已合并：** 是
- **作者：** akhilerm
- **标签：** size/S
- **变更说明：**
  **PR #13580:** [release/2.3] update go to 1.26.4
**标签:** size/S

**PR内容:** - go1.26.4 includes security fixes to the crypto/x509, mime, and net/textproto packages, as well as bug fixes to the compiler, the runtime, the go fix command, and the crypto/fips140 package.
- remove 1.26.2 from CI builds as it is not supported any longer due to dependency...

### PR #13591: [release/2.3] resolver: retry on transient network errors
- **链接：** https://github.com/containerd/containerd/pull/13591
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/L, area/distribution
- **变更说明：**
  **PR #13591:** [release/2.3] resolver: retry on transient network errors
**标签:** impact/changelog, size/L, area/distribution

**原始PR #13323:** resolver: retry on transient network errors
**原始PR标签:** kind/enhancement, size/L, area/distribution, cherry-pick/2.3.x
**原始PR内容:** Allow the last host to retry on transient network errors to incrase the likelihood of the operation succeeding and help red...

### PR #13601: [release/2.3] update runc binary to v1.4.3
- **链接：** https://github.com/containerd/containerd/pull/13601
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/XS
- **变更说明：**
  **PR #13601:** [release/2.3] update runc binary to v1.4.3
**标签:** size/XS

**原始PR #13590:** update runc binary to v1.4.3
**原始PR标签:** cherry-pick/1.7.x, size/XS, cherry-pick/2.0.x, cherry-pick/2.1.x, cherry-pick/2.2.x, cherry-pick/2.3.x
**原始PR内容:** release notes: https://github.com/opencontainers/runc/releases/tag/v1.4.3
full diff: https://github.com/opencontainers/runc/compare/v1.4.2...v1.4.3
...

### PR #13608: [release/2.3] vendor: golang.org/x/crypto v0.53.0
- **链接：** https://github.com/containerd/containerd/pull/13608
- **状态：** closed
- **已合并：** 是
- **作者：** thaJeztah
- **标签：** size/XXL
- **变更说明：**
  **PR #13608:** [release/2.3] vendor: golang.org/x/crypto v0.53.0
**标签:** size/XXL

**原始PR #13600:** vendor: golang.org/x/crypto v0.53.0
**原始PR标签:** cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** golang.org/x/crypto v0.52.0 contains various security updates; those do NOT impact containerd, but may show up as vulnerability in scanners;

    === Symbol Results ===

    No vulnerabilities...

### PR #13627: [release/2.3] Prepare release notes for v2.3.2 
- **链接：** https://github.com/containerd/containerd/pull/13627
- **状态：** closed
- **已合并：** 是
- **作者：** samuelkarp
- **标签：** size/XL
- **变更说明：**
  **PR #13627:** [release/2.3] Prepare release notes for v2.3.2 
**标签:** size/XL

**PR内容:** containerd 2.3.2

Welcome to the v2.3.2 release of containerd!

The second patch release for containerd 2.3 contains various fixes
and updates including security patches.

### Security Updates

* **containerd**
  * [**CVE-2026-50195**](https://github.com/containerd/containerd/security/advisories/...

---
*本报告由 Containerd Release Tracker 自动生成*