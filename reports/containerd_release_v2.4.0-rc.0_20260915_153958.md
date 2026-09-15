# Containerd 版本发布分析报告
## containerd 2.4.0-rc.0 (v2.4.0-rc.0)

### 📋 版本信息
- **版本标签：** v2.4.0-rc.0
- **版本名称：** containerd 2.4.0-rc.0
- **发布时间：** 2026-09-15T14:27:33Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.4.0-rc.0

### 🔍 分析统计
- **分析时间：** 2026-09-15 15:39:58
- **分析的 PR 数量：** 15
- **分析的 Issue 数量：** 0
- **重要项目数量：** 6

## 📊 版本概述
Error calling LLM API: 401 Client Error: Unauthorized for url: https://qianfan.baidubce.com/v2/chat/completions

## 📋 Release 包含的变更

### PR #12698: remotes/docker: Propagate registry warnings to the resolver
- **链接：** https://github.com/containerd/containerd/pull/12698
- **状态：** closed
- **已合并：** 是
- **作者：** vvoland
- **标签：** impact/changelog, size/XL, area/distribution
- **变更说明：**
  **PR #12698:** remotes/docker: Propagate registry warnings to the resolver
**标签:** impact/changelog, size/XL, area/distribution

**PR内容:** According to the OCI distribution spec registries may include informational warnings in HTTP Warning headers:

- https://github.com/opencontainers/distribution-spec/blob/e612a6e1e1bc717f9fa7e1feb4f05c8b6568754a/spec.md#warnings
- https://www.rfc-editor.or...

### PR #12889: docker fetcher: strip sensitive headers on descriptor URLs
- **链接：** https://github.com/containerd/containerd/pull/12889
- **状态：** closed
- **已合并：** 是
- **作者：** 1seal
- **标签：** impact/changelog, kind/enhancement, cherry-picked/1.7.x, size/L, area/distribution, cherry-picked/2.0.x, cherry-picked/2.2.x, cherry-picked/2.3.x
- **变更说明：**
  **PR #12889:** docker fetcher: strip sensitive headers on descriptor URLs
**标签:** impact/changelog, kind/enhancement, cherry-picked/1.7.x, size/L, area/distribution, cherry-picked/2.0.x, cherry-picked/2.2.x, cherry-picked/2.3.x

**PR内容:** # docker fetcher: strip sensitive headers for desc.urls fetches

context:
- containerd supports fetching content from `descriptor.urls` (oci descriptor URLs)....

### PR #13162: Set the default of runtimeFeatures.UserNamespacesHostNetwork to true
- **链接：** https://github.com/containerd/containerd/pull/13162
- **状态：** closed
- **已合并：** 是
- **作者：** HirazawaUi
- **标签：** impact/changelog, area/cri, dependencies, size/XS, cherry-pick/2.3.x
- **变更说明：**
  **PR #13162:** Set the default of runtimeFeatures.UserNamespacesHostNetwork to true
**标签:** impact/changelog, area/cri, dependencies, size/XS, cherry-pick/2.3.x

**PR内容:** This is a follow-up to #12518, after it is merged.

Due to the integration with NodeDeclaredFeatures, the kubelet needs to know exactly which version of containerd provides this feature. Therefore, I added the `UserNamespac...

### PR #13360: Fix sandbox task API endpoints for non-runc runtimes
- **链接：** https://github.com/containerd/containerd/pull/13360
- **状态：** closed
- **已合并：** 是
- **作者：** mxpv
- **标签：** impact/deprecation, kind/bug, area/runtime, size/XXL, cherry-picked/2.2.x, cherry-picked/2.3.x
- **变更说明：**
  **PR #13360:** Fix sandbox task API endpoints for non-runc runtimes
**标签:** impact/deprecation, kind/bug, area/runtime, size/XXL, cherry-picked/2.2.x, cherry-picked/2.3.x

**PR内容:** I believe we overlooked this in https://github.com/containerd/containerd/pull/9736 and introduced task API address and version fields in Runc options.

Those are used in Sandbox API flow and have nothing to do wit...

### PR #13504: Introspect OCI runtime features for non-runc runtimes
- **链接：** https://github.com/containerd/containerd/pull/13504
- **状态：** closed
- **已合并：** 是
- **作者：** a7i
- **标签：** impact/changelog, area/cri, size/L, cherry-pick/2.2.x, cherry-pick/2.3.x
- **变更说明：**
  **PR #13504:** Introspect OCI runtime features for non-runc runtimes
**标签:** impact/changelog, area/cri, size/L, cherry-pick/2.2.x, cherry-pick/2.3.x

**PR内容:** ## What this does

Remove the runc-only guard in `introspectRuntimeFeatures` so CRI introspects OCI runtime features for all shim types, not only `io.containerd.runc.v2`.

## Why

Kubelet rejects pods with `runtimeClassName: gvisor` and...

### PR #13520: Add max size label for snapshots
- **链接：** https://github.com/containerd/containerd/pull/13520
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** impact/changelog, area/snapshotters, size/M
- **变更说明：**
  **PR #13520:** Add max size label for snapshots
**标签:** impact/changelog, area/snapshotters, size/M

**PR内容:** Defines a global label for setting size and initially uses it for the erofs snapshotter

```release-note
Add max size label for snapshots
```
...

### PR #13542: cri: enable mount manager for image mounts
- **链接：** https://github.com/containerd/containerd/pull/13542
- **状态：** closed
- **已合并：** 是
- **作者：** hsiangkao
- **标签：** impact/changelog, area/cri, size/S, cherry-picked/2.2.x, cherry-picked/2.3.x
- **变更说明：**
  **PR #13542:** cri: enable mount manager for image mounts
**标签:** impact/changelog, area/cri, size/S, cherry-picked/2.2.x, cherry-picked/2.3.x

**PR内容:** Fix #13534
~Depends on #13656~

```release-note
Enable mount manager for image mounts in CRI
```
...

### PR #13560: Use klauspost/compress/gzip for decode
- **链接：** https://github.com/containerd/containerd/pull/13560
- **状态：** closed
- **已合并：** 是
- **作者：** jgehrcke
- **标签：** impact/changelog, size/XXL, area/distribution
- **变更说明：**
  **PR #13560:** Use klauspost/compress/gzip for decode
**标签:** impact/changelog, size/XXL, area/distribution

**PR内容:** Related to #13559.

Swap the stdlib gzip decompression code for [Klaus Post's inflate code](https://github.com/klauspost/compress/blob/v1.18.6/flate/inflate.go) in [`gzipDecompress`](https://github.com/containerd/containerd/blob/v2.3.1/pkg/archive/compression/compression.go#L27...

### PR #13634: Add forward References to the GC collection context
- **链接：** https://github.com/containerd/containerd/pull/13634
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** impact/changelog, size/L, area/storage
- **变更说明：**
  **PR #13634:** Add forward References to the GC collection context
**标签:** impact/changelog, size/L, area/storage

**PR内容:** Extend the garbage-collection framework so a collectible resource can emit forward references during graph traversal, in addition to the existing back-reference mechanism.

A CollectionContext may now implement the optional collectionWithReferences interface:

	References...

### PR #13699: Add parent path to runc checkpoint options
- **链接：** https://github.com/containerd/containerd/pull/13699
- **状态：** closed
- **已合并：** 是
- **作者：** ktock
- **标签：** impact/changelog, area/runtime, size/L
- **变更说明：**
  **PR #13699:** Add parent path to runc checkpoint options
**标签:** impact/changelog, area/runtime, size/L

**PR内容:** This commit allows the client to specify runc's `--parent-path` flag during checkpointing. This is useful for trying CRIU features relying on this flag (e.g. incremental checkpointing) from the client's side.

```release-note
Allow specifying parent checkpoint directory when chec...

---
*本报告由 Containerd Release Tracker 自动生成*