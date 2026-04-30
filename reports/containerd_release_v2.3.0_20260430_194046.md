# Containerd 版本发布分析报告
## containerd 2.3.0 (v2.3.0)

### 📋 版本信息
- **版本标签：** v2.3.0
- **版本名称：** containerd 2.3.0
- **发布时间：** 2026-04-30T19:35:05Z
- **发布者：** github-actions[bot]
- **预发布版本：** 否
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.0

### 🔍 分析统计
- **分析时间：** 2026-04-30 19:40:46
- **分析的 PR 数量：** 10
- **分析的 Issue 数量：** 1
- **重要项目数量：** 4

## 📊 版本概述
containerd 2.3.0 是首个年度LTS（长期稳定）版本，提供至少两年的支持，核心价值在于引入EROFS镜像格式支持、大幅增强NRI（节点资源接口）功能、改进可观测性（OpenTelemetry追踪）以及提升CRI（容器运行时接口）的稳定性和功能性。

## 🔒 安全问题修复
1. ⚠️ 依赖项全面升级，包含多个安全补丁（如golang.org/x/*系列、runc、CNI插件等） - [Dependency Changes](https://github.com/containerd/containerd/releases/tag/v2.3.0) - **风险级别：** 中（建议升级以获取安全修复）

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复gRPC连接超时问题，防止`ctr`命令在无法连接时无限期挂起 - [PR #166](https://github.com/containerd/containerd/pull/166) - **影响：** 提升客户端工具的可靠性和用户体验
2. 修复当containerd守护进程在`ctr attach`期间死亡时导致的panic崩溃问题 - [PR #264](https://github.com/containerd/containerd/pull/264) - **影响：** 提升`ctr`工具的健壮性，避免意外崩溃
3. 修复`ctr container list`命令无法正确显示容器状态（如暂停状态）的问题 - [PR #215](https://github.com/containerd/containerd/pull/215) - **影响：** 确保运维工具能准确反映容器真实状态
4. 修复二进制日志驱动在失败时未阻塞容器启动的问题 - [PR #12595](https://github.com/containerd/containerd/pull/12595) - **影响：** 确保日志收集配置错误时，容器不会在无日志状态下启动，避免排障困难
5. 更新OOMKilled事件处理逻辑 - [PR #12714](https://github.com/containerd/containerd/pull/12714) - **影响：** 更可靠地捕获和处理容器因OOM被杀的事件

## 💥 破坏性变更
1. 🚨 NRI：OCI钩子调整会累积所有者信息，且插件名称中不允许使用逗号（`,`） - [containerd/nri#264](https://github.com/containerd/nri/pull/264) - **影响：** 如果自定义NRI插件名称包含逗号，需要重命名以避免注册失败
2. 🚨 弃用`shim.Command` API - [PR #13319](https://github.com/containerd/containerd/pull/13319) - **影响：** 依赖此API的自定义shim或工具需要迁移到新的shim引导协议

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 首个年度LTS版本，支持周期至少两年，并与Kubernetes发布周期对齐 - [Release Notes](https://github.com/containerd/containerd/releases/tag/v2.3.0)
2. 支持EROFS（Enhanced Read-Only File System）原生容器镜像及zstd压缩层，提升镜像拉取和容器启动性能 - [PR #13185](https://github.com/containerd/containerd/pull/13185), [PR #13091](https://github.com/containerd/containerd/pull/13091), [PR #12567](https://github.com/containerd/containerd/pull/12567)
3. NRI框架重大增强，向插件传递容器用户、seccomp策略、rlimits、sysctl、CDI设备等完整配置信息，支持更精细的资源调整 - [PR #12769](https://github.com/containerd/containerd/pull/12769), [PR #12768](https://github.com/containerd/containerd/pull/12768), [PR #12765](https://github.com/containerd/containerd/pull/12765)
4. 集成OpenTelemetry追踪，支持在RPC调用和日志中注入Trace ID，提升分布式系统排障能力 - [PR #13113](https://github.com/containerd/containerd/pull/13113), [PR #13117](https://github.com/containerd/containerd/pull/13117)
5. 引入新的shim引导协议，改进shim生命周期管理 - [PR #12786](https://github.com/containerd/containerd/pull/12786), [PR #12785](https://github.com/containerd/containerd/pull/12785)
6. CRI：允许容器在使用主机网络的同时使用用户命名空间，增强安全隔离 - [PR #12518](https://github.com/containerd/containerd/pull/12518)
7. CRI：添加后台统计收集器，为容器和Pod沙箱计算更准确的CPU使用率（UsageNanoCores） - [PR #12629](https://github.com/containerd/containerd/pull/12629)

## 🚀 性能优化
1. EROFS快照器支持dm-verity和数据去重，并使用fsmount API避免PAGE_SIZE限制，提升镜像安全性和挂载性能 - [PR #12502](https://github.com/containerd/containerd/pull/12502), [PR #12783](https://github.com/containerd/containerd/pull/12783) - **提升：** 更安全、更高效的只读层管理
2. 使用新的过滤式cgroups统计API，减少不必要的数据收集开销 - [PR #12901](https://github.com/containerd/containerd/pull/12901) - **提升：** 降低资源统计时的系统开销
3. 为特定运行时解压镜像时使用每层标签，优化存储效率 - [PR #12835](https://github.com/containerd/containerd/pull/12835) - **提升：** 针对不同运行时的镜像存储优化

## 🎯 风险评估
整体风险评估：**中低风险**。作为首个年度LTS版本，其核心目标是稳定性，且经过了较长时间的测试。主要风险点在于NRI的破坏性变更和EROFS等新特性的引入。建议的升级时机是在下一个维护窗口，并在升级前完成充分的测试。需要特别关注的方面包括：自定义NRI插件、使用特定shim实现的场景、以及对镜像性能有严格要求的场景。对于关键业务，建议先在小规模节点集群上灰度升级。

## 📋 升级建议
1. **对于生产环境：** 鉴于2.3.0是LTS版本，建议规划从1.7 LTS或2.x非LTS版本升级，以获得长期稳定支持和安全更新。
2. **评估NRI插件兼容性：** 如果使用了NRI插件，请检查插件名称是否符合新规范（无逗号），并验证插件是否能处理新增的容器配置信息（如用户、seccomp等）。
3. **测试EROFS支持：** 如果考虑使用EROFS镜像格式以提升性能，需在测试环境中验证与现有镜像构建、分发和运行流程的兼容性。
4. **利用增强的可观测性：** 配置OpenTelemetry导出器，以利用新的分布式追踪功能，便于排查跨服务的容器生命周期问题。
5. **更新监控配置：** CRI新增的后台统计收集器提供了更准确的`UsageNanoCores`，可考虑更新监控仪表板或告警规则以利用此改进。
6. **在测试环境充分验证：** 升级前，务必在测试环境中模拟生产负载，重点验证CRI稳定性、shim生命周期以及任何自定义插件或配置的兼容性。

## 📋 Release 包含的变更

### PR #157: let user to specify the shim name or path
- **链接：** https://github.com/containerd/containerd/pull/157
- **状态：** closed
- **已合并：** 是
- **作者：** mYmNeo
- **变更说明：**
  **PR #157:** let user to specify the shim name or path

**PR内容:** Signed-off-by: mYmNeo mymneo@163.com
...

### PR #160: Integration test
- **链接：** https://github.com/containerd/containerd/pull/160
- **状态：** closed
- **已合并：** 是
- **作者：** mlaventure
- **变更说明：**
  **PR #160:** Integration test

**PR内容:** This is what I came up with for the integration testing.

@crosbymichael, @icecrime, @tonistiigi, @anusha-ragunathan PTAL

I dropped a few extra fixes in the mix since I needed them for the tests to work or for debugging.
...

### PR #166: Add grpc timeout
- **链接：** https://github.com/containerd/containerd/pull/166
- **状态：** closed
- **已合并：** 是
- **作者：** mlaventure
- **变更说明：**
  **PR #166:** Add grpc timeout

**PR内容:** Fixes #165 


**关联的Issues:**
- Issue #165: ctr: inability to connect to grpc causes hang
  If you run `ctr` commands without sufficient privileges to connect to the `grpc` socket, the command will _not_ fail. It will just hang indefinitely. It should error out instead.
......

### PR #215: Bugfix: ctr container list can not get the proper status of container
- **链接：** https://github.com/containerd/containerd/pull/215
- **状态：** closed
- **已合并：** 是
- **作者：** HuKeping
- **变更说明：**
  **PR #215:** Bugfix: ctr container list can not get the proper status of container

**PR内容:**  Prior to this patch, when list containers by "ctr containers" or
"ctr containers xxx", it will not get the proper status of conatinser(s).

for example:

```
h00283522@ubuntu:~$ sudo ctr containers
ID                  PATH                                  STATUS              PROCESSES
hukeping_xxx    ...

### PR #230: uprev dependencies required for build clean on Solaris
- **链接：** https://github.com/containerd/containerd/pull/230
- **状态：** closed
- **已合并：** 是
- **作者：** amitkris
- **变更说明：**
  **PR #230:** uprev dependencies required for build clean on Solaris

**PR内容:** This PR uprevs pkg/term and runc/libcontainer in containerd such that they build on Solaris.
This is a dependency for #203.

Signed-off-by: Amit Krishnan krish.amit@gmail.com
...

### PR #248: fix typo in error-message
- **链接：** https://github.com/containerd/containerd/pull/248
- **状态：** closed
- **已合并：** 是
- **作者：** thaJeztah
- **变更说明：**
  **PR #248:** fix typo in error-message

### PR #253: Store the checkpoint and restore logs in the same directory as the checkpoint image
- **链接：** https://github.com/containerd/containerd/pull/253
- **状态：** closed
- **已合并：** 是
- **作者：** boucher
- **变更说明：**
  **PR #253:** Store the checkpoint and restore logs in the same directory as the checkpoint image

**PR内容:** Currently the storage defaults to a /runc managed directory that is usually destroyed, making the logs difficult to get. This just stores them in the same path as the rest of the checkpoint files (which also makes things easier at the Docker level, which destroys the containerd managed fo...

### PR #264: Fix panic within ctr if the daemon dies while attached to a container
- **链接：** https://github.com/containerd/containerd/pull/264
- **状态：** closed
- **已合并：** 是
- **作者：** mlaventure
- **变更说明：**
  **PR #264:** Fix panic within ctr if the daemon dies while attached to a container

**PR内容:** Signed-off-by: Kenfe-Mickael Laventure mickael.laventure@gmail.com
...

### PR #274: Call start in containerd
- **链接：** https://github.com/containerd/containerd/pull/274
- **状态：** closed
- **已合并：** 是
- **作者：** crosbymichael
- **变更说明：**
  **PR #274:** Call start in containerd

**PR内容:** This fixes a sync issue when the containerd api returns after a
container has started.  It fixes it by calling the runtime start inside
containerd after the oom handler has been setup.

Signed-off-by: Michael Crosby crosbymichael@gmail.com
...

---
*本报告由 Containerd Release Tracker 自动生成*