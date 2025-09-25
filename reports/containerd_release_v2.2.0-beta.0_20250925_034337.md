# Containerd Release Analysis Report
## containerd 2.2.0-beta.0 (v2.2.0-beta.0)

### Release Information
- **Tag:** v2.2.0-beta.0
- **Name:** containerd 2.2.0-beta.0
- **Published:** 2025-09-18T17:05:00Z
- **Author:** github-actions[bot]
- **Prerelease:** True
- **Draft:** False
- **URL:** https://github.com/containerd/containerd/releases/tag/v2.2.0-beta.0

### Analysis Metadata
- **Generated:** 2025-09-25 03:43:37
- **Analyzed PRs:** 10
- **Analyzed Issues:** 1
- **Important Items:** 5

## Executive Summary
containerd 2.2.0-beta.0 版本聚焦稳定性增强与存储/运行时优化，引入垃圾收集器反向引用和块存储支持，修复关键资源泄漏问题

## Key Changes
1. 垃圾收集器支持反向引用 - [PR #12025](https://github.com/containerd/containerd/pull/12025) - 优化资源生命周期管理
2. Go客户端OCI包接口升级为fs.FS - [PR #12245](https://github.com/containerd/containerd/pull/12245) - 改进文件系统抽象能力
3. 新增块CIM格式的snapshotter/differ支持 - [PR #12050](https://github.com/containerd/containerd/pull/12050) - Windows容器镜像优化
4. EROFSSnapshotter添加tar索引模式 - [PR #11919](https://github.com/containerd/containerd/pull/11919) - 提升OCI层处理效率

## Important Bugfixes
1. 修复用户命名空间下的pidfd泄漏 - [PR #12167](https://github.com/containerd/containerd/pull/12167) - **影响：** 容器高密度场景可能导致文件描述符耗尽
2. 解决用户命名空间下CNI信息丢失问题 - [Issue #10363](https://github.com/containerd/containerd/issues/10363) - **影响：** 容器重启后网络配置丢失

## Security Issues
1. ⚠️ 简化固定用户命名空间的网络配置 - [PR #10607](https://github.com/containerd/containerd/pull/10607) - **风险级别：** 中 - 涉及用户命名空间权限模型变更
2. ⚠️ 替换go:linkname为ptrace实现 - [PR #10611](https://github.com/containerd/containerd/pull/10611) - **风险级别：** 低 - 安全加固但兼容性变化

## Performance Improvements
1. EROFSSnapshotter的tar索引模式 - [PR #11919](https://github.com/containerd/containerd/pull/11919) - **提升：** OCI层处理效率优化（具体数值待实测）
2. 传输服务整合tar解压进度跟踪 - [PR #11921](https://github.com/containerd/containerd/pull/11921) - **提升：** 镜像拉取过程可视化

## Breaking Changes
1. 🚨 Go客户端OCI接口变更 - [PR #12245](https://github.com/containerd/containerd/pull/12245) - **影响：** 需要更新相关依赖代码
2. 🚨 依赖组件升级（如Kubernetes客户端至v0.34.1） - **影响：** 需验证与现有K8s集群的兼容性

## Risk Assessment
中等升级风险，建议：1. 生产环境等待正式版发布 2. 必须升级时优先修复环境 3. 重点关注用户命名空间、CNI插件、文件描述符泄漏问题 4. 验证K8s CRI接口兼容性

## Recommendations
1. 在测试环境充分验证用户命名空间相关功能
2. 升级前检查所有自定义插件对Go客户端接口的兼容性
3. 监控容器重启后的网络配置状态
4. 优先评估EROFSSnapshotter新特性在存储敏感场景的收益

## Important Items Identified
### PR: #11919: Add tar index mode to erofs snapshotter
**Reason:** Performance related

### PR: #12167: Fix pidfd leak in UnshareAfterEnterUserns
**Reason:** Has label 'kind/bug'

### PR: #10607: internal/cri: simplify netns setup with pinned userns
**Reason:** Contains 'security'

### PR: #10611: core/mount: use ptrace instead of go:linkname
**Reason:** Performance related

### Issue: #10363: [v2.0.0] No CNI info for pod sandbox after containerd restart when using user namespaces
**Reason:** Contains 'security'; Has label 'kind/bug'; Performance related

## Detailed Pull Request Analysis
### PR #121: Send "live" event only if past events requested
- **URL:** https://github.com/containerd/containerd/pull/121
- **State:** closed
- **Merged:** True
- **Author:** mlaventure
- **Created:** 2016-02-29T19:19:02Z
- **Merged:** 2016-02-29T19:25:51Z
- **Description:**
  This fixes a bug where the live events are recorded in the events log.

Signed-off-by: Kenfe-Mickael Laventure mickael.laventure@gmail.com


### PR #11919: Add tar index mode to erofs snapshotter
- **URL:** https://github.com/containerd/containerd/pull/11919
- **State:** closed
- **Merged:** True
- **Author:** aadhar-agarwal
- **Created:** 2025-05-30T18:17:02Z
- **Merged:** 2025-07-09T07:26:36Z
- **Labels:** impact/changelog, ok-to-test, size/L, area/storage
- **Description:**
  ## Summary

This PR introduces support for a new "tar index" mode in the EROFS snapshotter and differ. The tar index mode enables more efficient handling of OCI image layers by generating a tar index and appending the original tar content

## Key Changes

- **docs/snapshotters/erofs.md**: Added documentation for the new tar index mode, including configuration and usage details.
- **internal/erofsutils/mount_linux.go**: 
  - Added `GenerateTarIndexAndAppendTar` to create a combined EROFS ...

### PR #11921: Tar unpack progress through transfer service
- **URL:** https://github.com/containerd/containerd/pull/11921
- **State:** closed
- **Merged:** True
- **Author:** dmcgowan
- **Created:** 2025-05-30T21:24:16Z
- **Merged:** 2025-09-17T05:01:14Z
- **Labels:** impact/changelog, size/L, area/distribution
- **Description:**
  Adds unpack to transfer service.

See https://asciinema.org/a/6bJRKKKuqkAVV51GjN8SBSeYu

A few notes...
- we could order the progress lines better to make it easier to follow
- remote differ will not have the progress but the proxy will at least send start and end progress

### PR #12025: Add support for back references in the garbage collector
- **URL:** https://github.com/containerd/containerd/pull/12025
- **State:** closed
- **Merged:** True
- **Author:** dmcgowan
- **Created:** 2025-06-24T23:32:23Z
- **Merged:** 2025-08-22T05:20:56Z
- **Labels:** impact/changelog, kind/feature, size/L
- **Description:**
  Add backreference labels for an object. This allows objects to be referred to by objects which already exist without updating the labels on the original object or referred to by objects which do not yet exist. This is useful for ephemeral objects as well as objects with a 1 to many relationship.

Use cases:
- Dependent images ("dangling" images)
- Ephemeral container objects (such as streams, networks, or mounts)
- OCI referrers (1 to many relationship)


### PR #12050: Add snapshotter and differ for block CIMs
- **URL:** https://github.com/containerd/containerd/pull/12050
- **State:** closed
- **Merged:** True
- **Author:** ambarve
- **Created:** 2025-07-01T22:17:28Z
- **Merged:** 2025-07-31T20:50:31Z
- **Labels:** impact/changelog, platform/windows, needs-ok-to-test, size/XXL, go, area/storage
- **Description:**
  This commit adds the snapshotter and differ plugins that can be used to pull/import container images in the block CIM format. (More about block CIMs [here](https://github.com/microsoft/hcsshim/blob/main/pkg/cimfs/doc.go).)

### PR #12082: Enable otel traces in NRI
- **URL:** https://github.com/containerd/containerd/pull/12082
- **State:** closed
- **Merged:** True
- **Author:** klihub
- **Created:** 2025-07-10T18:42:30Z
- **Merged:** 2025-07-21T15:01:18Z
- **Labels:** impact/changelog, size/S, area/nri
- **Description:**
  Set up NRI for producing otel trace spans.

### PR #12167: Fix pidfd leak in UnshareAfterEnterUserns
- **URL:** https://github.com/containerd/containerd/pull/12167
- **State:** closed
- **Merged:** True
- **Author:** jfernandez
- **Created:** 2025-08-05T04:06:03Z
- **Merged:** 2025-08-07T04:54:21Z
- **Labels:** impact/changelog, kind/bug, ok-to-test, area/runtime, size/XS, cherry-picked/2.0.x, cherry-picked/2.1.x
- **Description:**
  UnshareAfterEnterUserns() creates a pidfd via os.StartProcess() with CLONE_PIDFD but fails to close the file descriptor in any code path, resulting in a file descriptor leak for every container that uses user namespace isolation.

The leak occurs because:
- The pidfd is created when PidFD field is set in SysProcAttr
- The defer block only calls PidfdSendSignal() and pidfdWaitid()
- No code path calls unix.Close(pidfd) to release the file descriptor

This causes one pidfd leak per containe...

### PR #10607: internal/cri: simplify netns setup with pinned userns
- **URL:** https://github.com/containerd/containerd/pull/10607
- **State:** closed
- **Merged:** True
- **Author:** fuweid
- **Created:** 2024-08-17T14:14:59Z
- **Merged:** 2024-09-19T01:46:30Z
- **Labels:** area/cri, ok-to-test, size/XL
- **Description:**
  ## Motivation:

For pod-level user namespaces, it's impossible to force the container runtime
to join an existing network namespace after creating a new user namespace.

According to the capabilities section in [user_namespaces(7)][1], a network
namespace created by containerd is owned by the root user namespace. When the
container runtime (like runc or crun) creates a new user namespace, it becomes
a child of the root user namespace. Processes within this child user namespace
are not p...

### PR #10611: core/mount: use ptrace instead of go:linkname
- **URL:** https://github.com/containerd/containerd/pull/10611
- **State:** closed
- **Merged:** True
- **Author:** fuweid
- **Created:** 2024-08-19T14:02:35Z
- **Merged:** 2024-08-30T17:46:23Z
- **Labels:** area/runtime, size/XL, go
- **Description:**
  The Go runtime has started to [lock down future uses of linkname][1] since
go1.23. In the go source code, containerd project has been marked in the
comment, [hall of shame][2]. Well, the go:linkname is used to fork no-op
subprocess efficiently. However, since that comment, I would like to use
ptrace and remove go:linkname in the whole repository.

With go1.22 `go:linkname`:

```bash
$ go test -bench=.  -benchmem ./ -exec sudo
goos: linux
goarch: amd64
pkg: github.com/containerd/conta...

### PR #12245: Update pkg/oci to use fs.FS interface and os.OpenRoot
- **URL:** https://github.com/containerd/containerd/pull/12245
- **State:** closed
- **Merged:** True
- **Author:** dmcgowan
- **Created:** 2025-08-28T06:16:14Z
- **Merged:** 2025-08-30T02:18:18Z
- **Labels:** impact/changelog, size/L, go, area/client
- **Description:**
  Switch to use fs.FS interface over directly requiring path string. This interface allows the filesystem operations to be further abstracted, then we can use any library which can return an FS from mounts without requiring an active mount. This is useful for supporting erofs on hosts which cannot directly mount it.

Using os.OpenRoot over continuity's RootPath is the preferred solution going forward as it is part of the standard library and able to leverage the openat syscall. Switching with th...

## Detailed Issue Analysis
### Issue #10363: [v2.0.0] No CNI info for pod sandbox after containerd restart when using user namespaces
- **URL:** https://github.com/containerd/containerd/issues/10363
- **State:** closed
- **Author:** mathias-ioki
- **Created:** 2024-06-19T13:47:35Z
- **Closed:** 2024-10-17T10:32:33Z
- **Labels:** kind/bug, Stale
- **Description:**
  ### Description

We are using containerd (2.0) in combination with standalone kubelet and user namespaces.

When we do a restart of containerd and after that a restart of kubelet, all pods are getting restarted as well. The reason for that is pretty much the same as described here: https://github.com/containerd/containerd/issues/7843

After restarting containerd, all network informations for the pod sandbox are gone. As kubelet is checking these infos at start and can't find them, it will ...

## Original Release Notes
```
Welcome to the v2.2.0-beta.0 release of containerd!
*This is a pre-release of containerd*

The second minor release of containerd 2.x focuses on continued stability alongside
new features and improvements. This is the second time-based released for containerd.

This is a beta release and some functionality is still under development.

### Highlights

* Add support for back references in the garbage collector ([#12025](https://github.com/containerd/containerd/pull/12025))

#### Go client

* Update pkg/oci to use fs.FS interface and os.OpenRoot ([#12245](https://github.com/containerd/containerd/pull/12245))

#### Image Distribution

* Tar unpack progress through transfer service ([#11921](https://github.com/containerd/containerd/pull/11921))

#### Image Storage

* Add snapshotter and differ for block CIMs ([#12050](https://github.com/containerd/containerd/pull/12050))
* Add tar index mode to erofs snapshotter ([#11919](https://github.com/containerd/containerd/pull/11919))

#### Node Resource Interface (NRI)

* Enable otel traces in NRI ([#12082](https://github.com/containerd/containerd/pull/12082))
* Add WASM plugin support ([containerd/nri#121](https://github.com/containerd/nri/pull/121))

#### Runtime

* Fix pidfd leak in UnshareAfterEnterUserns ([#12167](https://github.com/containerd/containerd/pull/12167))

Please try out the release binaries and report any issues at
https://github.com/containerd/containerd/issues.

### Contributors

* Phil Estes
* Derek McGowan
* Krisztian Litkey
* Akihiro Suda
* Maksym Pavlenko
* Mike Brown
* Wei Fu
* Markus Lehtonen
* Samuel Karp
* Sebastiaan van Stijn
* Austin Vazquez
* ningmingxiao
* yashsingh74
* Jin Dong
* Kirtana Ashok
* Etienne Champetier
* Rodrigo Campos
* Akhil Mohan
* Chris Henzie
* Gao Xiang
* Sascha Grunert
* Aleksa Sarai
* Eric Mountain
* Keith Mattix II
* Paweł Gronowski
* Adrien Delorme
* Enji Cooper
* Kohei Tokunaga
* Yang Yang
* jokemanfire
* Aadhar Agarwal
* Amit Barve
* Andrew Halaney
* Antonio Ojea
* Brian Goff
* Chenyang Yan
* Dawei Wei
* Divya Rani
* Fabiano Fidêncio
* Henry Wang
* Iceber Gu
* Jared Ledvina
* Jonathan Perkin
* Jose Fernandez
* Karl Baumgartner
* Radostin Stoyanov
* Rehan Khan
* Ruidong Cao
* Sameer
* Swagat Bora
* Sylvain MOUQUET
* Tom Wieczorek
* Tycho Andersen
* Ubuntu
* Wuyue (Tony) Sun
* jinda.ljd
* tanhuaan
* zounengren

### Dependency Changes

* **dario.cat/mergo**                                                    v1.0.1 -> v1.0.2
* **github.com/Microsoft/hcsshim**                                       v0.13.0-rc.3 -> v0.14.0-rc.1
* **github.com/checkpoint-restore/checkpointctl**                        v1.3.0 -> v1.4.0
* **github.com/containerd/console**                                      v1.0.4 -> v1.0.5
* **github.com/containerd/go-cni**                                       v1.1.12 -> v1.1.13
* **github.com/containerd/nri**                                          v0.8.0 -> v0.10.0
* **github.com/containernetworking/plugins**                             v1.7.1 -> v1.8.0
* **github.com/coreos/go-systemd/v22**                                   v22.5.0 -> v22.6.0
* **github.com/cpuguy83/go-md2man/v2**                                   v2.0.5 -> v2.0.7
* **github.com/emicklei/go-restful/v3**                                  v3.11.0 -> v3.13.0
* **github.com/fxamacker/cbor/v2**                                       v2.7.0 -> v2.9.0
* **github.com/go-jose/go-jose/v4**                                      v4.0.5 -> v4.1.1
* **github.com/go-logr/logr**                                            v1.4.2 -> v1.4.3
* **github.com/golang/groupcache**                                       41bb18bfe9da -> 2c02b8208cf8
* **github.com/gorilla/websocket**                                       v1.5.0 -> e064f32e3674
* **github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus**  v1.0.1 -> v1.1.0
* **github.com/intel/goresctrl**                                         v0.8.0 -> v0.9.0
* **github.com/knqyf263/go-plugin**                                      v0.9.0 **_new_**
* **github.com/modern-go/reflect2**                                      v1.0.2 -> 35a7c28c31ee
* **github.com/prometheus/client_golang**                                v1.22.0 -> v1.23.2
* **github.com/prometheus/client_model**                                 v0.6.1 -> v0.6.2
* **github.com/prometheus/common**                                       v0.62.0 -> v0.66.1
* **github.com/prometheus/procfs**                                       v0.15.1 -> v0.16.1
* **github.com/stretchr/testify**                                        v1.10.0 -> v1.11.1
* **github.com/tchap/go-patricia/v2**                                    v2.3.2 -> v2.3.3
* **github.com/tetratelabs/wazero**                                      v1.9.0 **_new_**
* **github.com/urfave/cli/v2**                                           v2.27.6 -> v2.27.7
* **github.com/vishvananda/netlink**                                     0e7078ed04c8 -> v1.3.1
* **go.etcd.io/bbolt**                                                   v1.4.0 -> v1.4.3
* **go.opentelemetry.io/otel**                                           v1.35.0 -> v1.37.0
* **go.opentelemetry.io/otel/metric**                                    v1.35.0 -> v1.37.0
* **go.opentelemetry.io/otel/sdk**                                       v1.35.0 -> v1.37.0
* **go.opentelemetry.io/otel/trace**                                     v1.35.0 -> v1.37.0
* **go.uber.org/goleak**                                                 v1.3.0 **_new_**
* **go.yaml.in/yaml/v2**                                                 v2.4.2 **_new_**
* **golang.org/x/crypto**                                                v0.36.0 -> v0.41.0
* **golang.org/x/mod**                                                   v0.24.0 -> v0.28.0
* **golang.org/x/net**                                                   v0.38.0 -> v0.43.0
* **golang.org/x/oauth2**                                                v0.27.0 -> v0.30.0
* **golang.org/x/sync**                                                  v0.14.0 -> v0.17.0
* **golang.org/x/sys**                                                   v0.33.0 -> v0.36.0
* **golang.org/x/term**                                                  v0.30.0 -> v0.34.0
* **golang.org/x/text**                                                  v0.23.0 -> v0.28.0
* **golang.org/x/time**                                                  v0.7.0 -> v0.9.0
* **google.golang.org/genproto/googleapis/api**                          56aae31c358a -> 8d1bb00bc6a7
* **google.golang.org/genproto/googleapis/rpc**                          56aae31c358a -> 8d1bb00bc6a7
* **google.golang.org/grpc**                                             v1.72.0 -> v1.75.1
* **google.golang.org/protobuf**                                         v1.36.6 -> v1.36.9
* **k8s.io/api**                                                         v0.32.3 -> v0.34.1
* **k8s.io/apimachinery**                                                v0.32.3 -> v0.34.1
* **k8s.io/client-go**                                                   v0.32.3 -> v0.34.1
* **k8s.io/cri-api**                                                     v0.32.3 -> v0.34.1
* **k8s.io/utils**                                                       3ea5e8cea738 -> 4c0f3b243397
* **sigs.k8s.io/json**                                                   9aa6b5e7a4b3 -> cfa47c3a1cc8
* **sigs.k8s.io/randfill**                                               v1.0.0 **_new_**
* **sigs.k8s.io/structured-merge-diff/v6**                               v6.3.0 **_new_**
* **sigs.k8s.io/yaml**                                                   v1.4.0 -> v1.6.0

Previous release can be found at [v2.1.0](https://github.com/containerd/containerd/releases/tag/v2.1.0)
### Which file should I download?
* `containerd-<VERSION>-<OS>-<ARCH>.tar.gz`:         ✅Recommended. Dynamically linked with glibc 2.35 (Ubuntu 22.04).
* `containerd-static-<VERSION>-<OS>-<ARCH>.tar.gz`:  Statically linked. Expected to be used on Linux distributions that do not use glibc >= 2.35. Not position-independent.

In addition to containerd, typically you will have to install [runc](https://github.com/opencontainers/runc/releases)
and [CNI plugins](https://github.com/containernetworking/plugins/releases) from their official sites too.

See also the [Getting Started](https://github.com/containerd/containerd/blob/main/docs/getting-started.md) documentation.

```

---
*This report was generated automatically by the Containerd Release Tracker.*