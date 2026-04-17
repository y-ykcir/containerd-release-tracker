# Containerd 版本发布分析报告
## containerd 2.3.0-beta.2 (v2.3.0-beta.2)

### 📋 版本信息
- **版本标签：** v2.3.0-beta.2
- **版本名称：** containerd 2.3.0-beta.2
- **发布时间：** 2026-04-17T18:15:35Z
- **发布者：** github-actions[bot]
- **预发布版本：** 是
- **草稿状态：** 否
- **GitHub 链接：** https://github.com/containerd/containerd/releases/tag/v2.3.0-beta.2

### 🔍 分析统计
- **分析时间：** 2026-04-17 19:41:03
- **分析的 PR 数量：** 3
- **分析的 Issue 数量：** 0
- **重要项目数量：** 0

## 📊 版本概述
containerd 2.3.0-beta.2 是首个年度LTS（长期支持）版本的预览，引入了新的shim启动协议、增强的EROFS支持、OpenTelemetry追踪集成以及多项CRI和NRI改进，旨在提升稳定性、可观测性和性能。

## 🔒 安全问题修复
1. ⚠️ 修复tar提取过程中的TOCTOU竞争条件漏洞 - [PR #12961](https://github.com/containerd/containerd/pull/12961) - **风险级别：** 中
2. ⚠️ 在返回gRPC错误前清理错误信息，防止凭证在Pod事件中泄露 - [PR #12801](https://github.com/containerd/containerd/pull/12801) - **风险级别：** 低

**🚨 安全建议：** 如果您的环境中使用了受影响的功能，建议优先升级到此版本。

## 🐛 重要问题修复
1. 修复二进制日志驱动在失败时未阻塞容器启动的问题，避免日志丢失 - [PR #12595](https://github.com/containerd/containerd/pull/12595) - **影响：** 生产环境中日志驱动故障可能导致容器异常启动且无日志，影响问题排查
2. 修复CNI DEL操作在某些情况下从未执行的问题，可能导致网络资源泄漏 - [PR #12923](https://github.com/containerd/containerd/pull/12923) - **影响：** 长期运行后可能累积未清理的网络命名空间或接口，影响节点稳定性
3. 修复tar提取过程中的TOCTOU竞争条件漏洞 - [PR #12961](https://github.com/containerd/containerd/pull/12961) - **影响：** 在并行解压镜像时可能引发竞态条件，导致文件系统错误
4. 修复Windows上shim管道就绪检查，提升Windows容器启动可靠性 - [PR #13202](https://github.com/containerd/containerd/pull/13202) - **影响：** Windows节点上容器启动可能因管道未就绪而失败
5. 修复特权容器cgroup挂载选项未保留的问题 - [PR #12952](https://github.com/containerd/containerd/pull/12952) - **影响：** 特权容器可能无法正确访问主机cgroup文件系统

## 💥 破坏性变更
1. 🚨 引入新的shim bootstrap协议，旧有的shim启动接口被标记为废弃（Deprecated） - [PR #12786](https://github.com/containerd/containerd/pull/12786) - **影响：** 自定义shim或直接调用旧接口的工具需要评估兼容性，未来版本中旧接口将被移除
2. 🚨 插件配置迁移现在在加载时运行，而非启动时 - [PR #12608](https://github.com/containerd/containerd/pull/12608) - **影响：** 配置加载逻辑有变，需确保所有节点的配置文件格式一致
3. 🚨 从沙盒元数据中移除Container字段，更新沙盒API以包含spec字段 - [PR #12840](https://github.com/containerd/containerd/pull/12840) - **影响：** 直接依赖沙盒元数据中Container字段的内部组件或插件需要更新

**⚠️ 升级警告：** 此版本包含破坏性变更，升级前请仔细评估对现有系统的影响。

## ✨ 主要变更
1. 引入新的shim启动协议，为未来shim架构演进奠定基础 - [PR #12786](https://github.com/containerd/containerd/pull/12786)
2. 新增容器文件系统复制传输类型，支持更灵活的容器文件操作 - [PR #13165](https://github.com/containerd/containerd/pull/13165)
3. 支持在日志中注入OpenTelemetry追踪ID，增强可观测性 - [PR #13117](https://github.com/containerd/containerd/pull/13117)
4. 在插件客户端的外发RPC中传播OpenTelemetry追踪，实现端到端追踪 - [PR #13113](https://github.com/containerd/containerd/pull/13113)
5. 支持zstd压缩的EROFS层，优化镜像分发和存储 - [PR #13185](https://github.com/containerd/containerd/pull/13185)
6. 新增EROFS层媒体类型，完善EROFS生态支持 - [PR #12567](https://github.com/containerd/containerd/pull/12567)
7. 允许容器在使用主机网络的同时使用用户命名空间，提升安全性 - [PR #12518](https://github.com/containerd/containerd/pull/12518)
8. 为NRI插件传递更多容器运行时信息（如用户、seccomp策略、rlimits等），增强插件能力 - [PR #12769](https://github.com/containerd/containerd/pull/12769), [PR #12768](https://github.com/containerd/containerd/pull/12768), [PR #12765](https://github.com/containerd/containerd/pull/12765)

## 🚀 性能优化
1. EROFS快照器使用fsmount API绕过PAGE_SIZE限制，提升大文件挂载性能 - [PR #12783](https://github.com/containerd/containerd/pull/12783) - **提升：** 改善大块设备文件的挂载效率
2. 使用新的过滤式cgroups统计API，减少不必要的数据收集开销 - [PR #12901](https://github.com/containerd/containerd/pull/12901) - **提升：** 降低容器指标收集时的CPU和内存开销
3. 支持只读overlay的无挂载读取，优化某些场景下的文件访问 - [PR #12865](https://github.com/containerd/containerd/pull/12865) - **提升：** 减少不必要的挂载操作

## 🎯 风险评估
整体风险评估：中等偏高。作为beta版本，其稳定性和兼容性尚未经过大规模生产验证。然而，作为首个年度LTS（2.3）的预览版，其引入的架构变更（如shim协议）和重要功能（如EROFS、OpenTelemetry）对未来的技术选型至关重要。建议在非关键测试环境中进行充分的功能、性能和兼容性测试，特别关注破坏性变更对现有工作流的影响。正式的LTS版本发布后，再进行生产环境的滚动升级。

## 📋 升级建议
1. **生产环境暂勿升级**：此为beta预发布版本，包含实验性功能，不建议用于生产环境。
2. **开始测试评估**：建议在测试环境中部署此版本，重点验证EROFS集成、新的shim启动协议以及与Kubernetes 1.36（CRI API v0.36.0-rc.0）的兼容性。
3. **关注NRI插件兼容性**：如果使用NRI插件，请验证插件是否能正确处理新传递的容器信息（用户、seccomp、设备等）。
4. **检查自定义配置**：由于插件配置迁移逻辑变化，请检查并测试所有自定义或通过drop-in文件添加的配置。
5. **准备shim升级**：如果使用自定义shim或工具直接与shim交互，应开始规划向新的bootstrap协议迁移。

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

### PR #158: Add runtimeArgs to pass to shim
- **链接：** https://github.com/containerd/containerd/pull/158
- **状态：** closed
- **已合并：** 是
- **作者：** crosbymichael
- **变更说明：**
  **PR #158:** Add runtimeArgs to pass to shim

**PR内容:** This allows you to pass options like:

``` bash
containerd --debug --runtime-args "--debug" --runtime-args
"--systemd-cgroup"
```

Signed-off-by: Michael Crosby crosbymichael@gmail.com
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

---
*本报告由 Containerd Release Tracker 自动生成*