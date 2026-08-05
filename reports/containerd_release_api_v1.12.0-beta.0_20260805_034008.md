# Containerd 版本发布分析报告
## containerd API 1.12.0-beta.0 (api/v1.12.0-beta.0)

### 📋 版本信息
- **版本标签：** api/v1.12.0-beta.0
- **版本名称：** containerd API 1.12.0-beta.0
- **发布时间：** 2026-08-05T02:33:29Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/api/v1.12.0-beta.0

### 🔍 分析统计
- **分析时间：** 2026-08-05 03:40:08
- **分析的 PR 数量：** 12
- **分析的 Issue 数量：** 1
- **重要项目数量：** 3

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

### PR #13423: do not hide linitng errors
- **链接：** https://github.com/containerd/containerd/pull/13423
- **状态：** closed
- **已合并：** 是
- **作者：** SergeyKanzhelev
- **标签：** size/L
- **变更说明：**
  **PR #13423:** do not hide linitng errors
**标签:** size/L

**PR内容:** This was counterproductive to format files before checking. Now lining errors will actually be checked...

### PR #13490: Update typeurl/v2 to v2.3.0 to drop gogo dependency
- **链接：** https://github.com/containerd/containerd/pull/13490
- **状态：** closed
- **已合并：** 是
- **作者：** liggitt
- **标签：** size/XXL
- **变更说明：**
  **PR #13490:** Update typeurl/v2 to v2.3.0 to drop gogo dependency
**标签:** size/XXL

**PR内容:** Pull in https://github.com/containerd/typeurl/pull/51#issuecomment-4558801701

cc @samuelkarp ...

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

### PR #13740: build(deps): bump github.com/containerd/ttrpc to v1.2.9
- **链接：** https://github.com/containerd/containerd/pull/13740
- **状态：** closed
- **已合并：** 是
- **作者：** liggitt
- **标签：** size/L
- **变更说明：**
  **PR #13740:** build(deps): bump github.com/containerd/ttrpc to v1.2.9
**标签:** size/L

**PR内容:** Update ttrpc to pick up https://github.com/containerd/ttrpc/pull/239

cc @fuweid @samuelkarp ...

### PR #13819: build(deps): bump golang.org/x/net from 0.51.0 to 0.55.0 in /api
- **链接：** https://github.com/containerd/containerd/pull/13819
- **状态：** closed
- **已合并：** 是
- **作者：** dependabot[bot]
- **标签：** dependencies, size/S, go
- **变更说明：**
  **PR #13819:** build(deps): bump golang.org/x/net from 0.51.0 to 0.55.0 in /api
**标签:** dependencies, size/S, go

**PR内容:** Bumps [golang.org/x/net](https://github.com/golang/net) from 0.51.0 to 0.55.0.
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/golang/net/commit/7770ec48d03fec35e378665337b4faca93c38423"><code>7770ec4</code></a> go.mod: update golang.org/x depende...

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

### PR #13899: Prepare release notes for api/v1.12.0-beta.0
- **链接：** https://github.com/containerd/containerd/pull/13899
- **状态：** closed
- **已合并：** 是
- **作者：** dmcgowan
- **标签：** size/S
- **变更说明：**
  **PR #13899:** Prepare release notes for api/v1.12.0-beta.0
**标签:** size/S

**PR内容:** Part of the v2.4 beta process

----

containerd api/v1.12.0-beta.0

Welcome to the api/v1.12.0-beta.0 release of containerd!  
*This is a pre-release of containerd*

The 13th release for the containerd 1.x API aligns with the containerd 2.4 release.

### Highlights

* **Include media type in conte...

---
*本报告由 Containerd Release Tracker 自动生成*