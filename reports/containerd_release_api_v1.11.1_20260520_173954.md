# Containerd 版本发布分析报告
## containerd API 1.11.1 (api/v1.11.1)

### 📋 版本信息
- **版本标签：** api/v1.11.1
- **版本名称：** containerd API 1.11.1
- **发布时间：** 2026-05-20T17:37:13Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/api/v1.11.1

### 🔍 分析统计
- **分析时间：** 2026-05-20 17:39:54
- **分析的 PR 数量：** 6
- **分析的 Issue 数量：** 0
- **重要项目数量：** 3

## 📊 版本概述
Error calling LLM API: 401 Client Error: Unauthorized for url: https://qianfan.baidubce.com/v2/chat/completions

## 📋 Release 包含的变更

### PR #13422: [release/2.3] Fix sandbox task API endpoints for non-runc runtimes
- **链接：** https://github.com/containerd/containerd/pull/13422
- **状态：** closed
- **已合并：** 是
- **作者：** k8s-infra-cherrypick-robot
- **标签：** impact/changelog, size/XXL
- **变更说明：**
  **PR #13422:** [release/2.3] Fix sandbox task API endpoints for non-runc runtimes
**标签:** impact/changelog, size/XXL

**原始PR #13360:** Fix sandbox task API endpoints for non-runc runtimes
**原始PR标签:** impact/deprecation, kind/bug, size/XXL, cherry-picked/2.2.x, cherry-picked/2.3.x
**原始PR内容:** I believe we overlooked this in https://github.com/containerd/containerd/pull/9736 and introduced task A...

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

---
*本报告由 Containerd Release Tracker 自动生成*