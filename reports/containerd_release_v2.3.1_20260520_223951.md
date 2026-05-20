# Containerd 版本发布分析报告
## containerd 2.3.1 (v2.3.1)

### 📋 版本信息
- **版本标签：** v2.3.1
- **版本名称：** containerd 2.3.1
- **发布时间：** 2026-05-20T20:46:56Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.1

### 🔍 分析统计
- **分析时间：** 2026-05-20 22:39:51
- **分析的 PR 数量：** 17
- **分析的 Issue 数量：** 2
- **重要项目数量：** 16

## 📊 版本概述
Error calling LLM API: 401 Client Error: Unauthorized for url: https://qianfan.baidubce.com/v2/chat/completions

## 📋 Release 包含的变更

### PR #13364: [release/2.3] Fix optional EROFS differ setup in transfer plugin
- **链接：** https://github.com/containerd/containerd/pull/13364
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/snapshotters, size/L
- **变更说明：**
  **PR #13364:** [release/2.3] Fix optional EROFS differ setup in transfer plugin
**标签:** impact/changelog, area/snapshotters, size/L

**原始PR #13328:** Fix optional EROFS differ setup in transfer plugin
**原始PR标签:** kind/bug, priority/P0, size/L, cherry-picked/2.3.x
**原始PR内容:** - closes https://github.com/containerd/containerd/issues/13346

Found this during some smoke tests for containerd 2.3....

### PR #13374: [release/2.3] Update Go to 1.26.3
- **链接：** https://github.com/containerd/containerd/pull/13374
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** size/S
- **变更说明：**
  **PR #13374:** [release/2.3] Update Go to 1.26.3
**标签:** size/S

**原始PR #13361:** Update Go to 1.26.3
**原始PR标签:** size/S
**原始PR内容:** - https://github.com/golang/go/issues?q=milestone%3AGo1.26.3+label%3ACherryPickApproved
- full diff: https://github.com/golang/go/compare/go1.26.2...go1.26.3

**- Description for the changelog**

```markdown changelog
Update Go runtime to [1.26.3](https://go...

### PR #13379: [release/2.3] fix: close boltdb on metadata and mount plugin close
- **链接：** https://github.com/containerd/containerd/pull/13379
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/L, area/storage
- **变更说明：**
  **PR #13379:** [release/2.3] fix: close boltdb on metadata and mount plugin close
**标签:** impact/changelog, size/L, area/storage

**原始PR #13348:** fix: close boltdb on metadata and mount plugin close
**原始PR标签:** kind/bug, size/L, cherry-picked/2.3.x
**原始PR内容:** ### Issue

When containerd shuts down its metadata or mount plugin never explicitly close the underlying bboltdb file deferring clean...

### PR #13390: [release/2.3] server: tolerate failed gRPC plugins when starting listeners
- **链接：** https://github.com/containerd/containerd/pull/13390
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/M, area/rootless
- **变更说明：**
  **PR #13390:** [release/2.3] server: tolerate failed gRPC plugins when starting listeners
**标签:** impact/changelog, size/M, area/rootless

**原始PR #13363:** server: tolerate failed gRPC plugins when starting listeners
**原始PR标签:** priority/P0, size/M, cherry-picked/2.3.x, area/rootless
**原始PR内容:** The grpc, grpc-tcp, and ttrpc server plugins enumerated their services through ic.GetByType, which s...

### PR #13394: [release/2.3] overlay: disable "rebase" capability when running in UserNS
- **链接：** https://github.com/containerd/containerd/pull/13394
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/snapshotters, size/XS, area/rootless
- **变更说明：**
  **PR #13394:** [release/2.3] overlay: disable "rebase" capability when running in UserNS
**标签:** impact/changelog, area/snapshotters, size/XS, area/rootless

**原始PR #13389:** overlay: disable "rebase" capability when running in UserNS
**原始PR标签:** area/cri, size/XS, cherry-picked/2.2.x, cherry-picked/2.3.x, area/rootless
**原始PR内容:** Fix #13388

```
[...]
May 12 16:57:23 kind-control-plane ku...

### PR #13405: [release/2.3] Prepare release notes for v2.3.1
- **链接：** https://github.com/containerd/containerd/pull/13405
- **状态：** closed
- **已合并：** 是
- **作者：** AkihiroSuda
- **标签：** size/L
- **变更说明：**
  **PR #13405:** [release/2.3] Prepare release notes for v2.3.1
**标签:** size/L

**PR内容:** containerd 2.3.1

Welcome to the v2.3.1 release of containerd!

The first patch release for containerd 2.3 contains various fixes and improvements.

### Security Updates

* [**CVE-2026-46680**](https://github.com/containerd/containerd/security/advisories/GHSA-fqw6-gf59-qr4w)

### Highlights

* Fi...

### PR #13409: [release/2.3] seccomp: Block AF_ALG in default socket policy
- **链接：** https://github.com/containerd/containerd/pull/13409
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/M
- **变更说明：**
  **PR #13409:** [release/2.3] seccomp: Block AF_ALG in default socket policy
**标签:** impact/changelog, area/runtime, size/M

**原始PR #13327:** seccomp: Block AF_ALG in default socket policy
**原始PR标签:** kind/enhancement, cherry-picked/1.7.x, size/M, cherry-picked/2.0.x, cherry-pick/2.1.x, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** - port: https://github.com/moby/profiles/pull/20

Addre...

### PR #13422: [release/2.3] Fix sandbox task API endpoints for non-runc runtimes
- **链接：** https://github.com/containerd/containerd/pull/13422
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, area/runtime, size/XXL
- **变更说明：**
  **PR #13422:** [release/2.3] Fix sandbox task API endpoints for non-runc runtimes
**标签:** impact/changelog, area/runtime, size/XXL

**原始PR #13360:** Fix sandbox task API endpoints for non-runc runtimes
**原始PR标签:** impact/deprecation, kind/bug, size/XXL, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** I believe we overlooked this in https://github.com/containerd/containerd/pull/9736 and int...

### PR #13444: Prepare release notes for api/v1.11.1
- **链接：** https://github.com/containerd/containerd/pull/13444
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** size/S
- **变更说明：**
  **PR #13444:** Prepare release notes for api/v1.11.1
**标签:** size/S

**PR内容:** Generated notes

----

Welcome to the api/v1.11.1 release of containerd!

The first patch release for the containerd 1.11 API includes a fix
in the task endpoints for non-runc shims.

### Highlights

* Fix sandbox task API endpoints for non-runc runtimes ([#13422](https://github.com/containerd/containerd/p...

### PR #13447: [release/2.3] oci: return explicit error for out-of-range USER values
- **链接：** https://github.com/containerd/containerd/pull/13447
- **状态：** closed
- **已合并：** 是
- **作者：** samuelkarp
- **标签：** impact/changelog, area/runtime, size/M
- **变更说明：**
  **PR #13447:** [release/2.3] oci: return explicit error for out-of-range USER values
**标签:** impact/changelog, area/runtime, size/M

**PR内容:** ```release-note
Fix handling of out-of-range USER values in OCI spec to avoid unexpected username/group lookups
```...

---
*本报告由 Containerd Release Tracker 自动生成*