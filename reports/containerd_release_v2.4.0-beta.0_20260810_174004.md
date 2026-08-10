# Containerd 版本发布分析报告
## containerd 2.4.0-beta.0 (v2.4.0-beta.0)

### 📋 版本信息
- **版本标签：** v2.4.0-beta.0
- **版本名称：** containerd 2.4.0-beta.0
- **发布时间：** 2026-08-10T16:56:46Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.4.0-beta.0

### 🔍 分析统计
- **分析时间：** 2026-08-10 17:40:04
- **分析的 PR 数量：** 16
- **分析的 Issue 数量：** 2
- **重要项目数量：** 6

## 📊 版本概述
Error calling LLM API: 401 Client Error: Unauthorized for url: https://qianfan.baidubce.com/v2/chat/completions

## 📋 Release 包含的变更

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

**PR内容:** Defines a global label for setting size and initially uses it for the erofs snapshotter...

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

Swap the stdlib gzip decompression code for [Klaus Post's inflate code](https://github.com/klauspost/compress/blob/v1.18.6/flate/inflate.go) in [`gzipDecompress`](https://github.com/containerd/containerd/blob/v2.3.1/pkg/archive/compression/compression.go#L...

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

	Refere...

### PR #13699: Add parent path to runc checkpoint options
- **链接：** https://github.com/containerd/containerd/pull/13699
- **状态：** closed
- **已合并：** 是
- **作者：** ktock
- **标签：** impact/changelog, size/L
- **变更说明：**
  **PR #13699:** Add parent path to runc checkpoint options
**标签:** impact/changelog, size/L

**PR内容:** This commit allows the client to specify runc's `--parent-path` flag during checkpointing. This is useful for trying CRIU features relying on this flag (e.g. incremental checkpointing) from the client's side.
...

### PR #13813: Support warm image cache for erofs snapshotter
- **链接：** https://github.com/containerd/containerd/pull/13813
- **状态：** closed
- **已合并：** 是
- **作者：** mxpv
- **标签：** impact/changelog, size/XXL
- **变更说明：**
  **PR #13813:** Support warm image cache for erofs snapshotter
**标签:** impact/changelog, size/XXL

**PR内容:** A common technique to speed up cold container launches is to prefetch image
content onto the node:

- https://aws.amazon.com/blogs/containers/start-pods-faster-by-prefetching-images/
- https://docs.cloud.google.com/artifact-registry/docs/prewarm-images
- https://aws.amazon.com/blogs/...

### PR #13833: Include media type in content create event
- **链接：** https://github.com/containerd/containerd/pull/13833
- **状态：** closed
- **已合并：** 是
- **作者：** phillebaba
- **标签：** impact/changelog, size/XXL
- **变更说明：**
  **PR #13833:** Include media type in content create event
**标签:** impact/changelog, size/XXL

**PR内容:** This adds a new media type field to the content create event. This is needed as content create events occur before the image create event does. Meaning it is impossible to determine the media type of the content without first reading the content and fingerprinting it.

Fixes #12884

**关联的Is...

### PR #13871: cri: remove restore in CreateContainer
- **链接：** https://github.com/containerd/containerd/pull/13871
- **状态：** closed
- **已合并：** 是
- **作者：** samuelkarp
- **标签：** impact/breaking, area/criu, size/XXL
- **变更说明：**
  **PR #13871:** cri: remove restore in CreateContainer
**标签:** impact/breaking, area/criu, size/XXL

**PR内容:** Remove support for restoring checkpoint data during CreateContainer, which was previously deprecated in v2.3.

This will conflict with https://github.com/containerd/containerd/pull/13822. If this PR lands first, #13822 will need to add back relevant code (and would be a good time to r...

---
*本报告由 Containerd Release Tracker 自动生成*