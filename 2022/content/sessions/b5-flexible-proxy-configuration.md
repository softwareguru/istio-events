---
id: b5
title: "Flexible proxy configuration of service mesh under diverse workloads"
url: /sessions/flexible-proxy-configuration
speakers:
 - 阳 刘
 - Lan Zhang
time_start: 2022-04-26T04:00:00.000Z
time_end: 2022-04-26T04:35:00.000Z
session_type: Presentation
track: Infrastructure & networking
track_slug: infrastructure-networking
language: Chinese
block: b
slot: 5
---

As the scale of the cluster managed by the service mesh grows and the needs of diverse business scenarios, the proxy configuration corresponding to each different workload will also be different. Although global configuration and Pod Annotation configuration can complete diversified settings, when the number of Pods increases, it becomes more difficult for user to manage the proxy configuration.
 
In this topic, we propose a global, namespace-level, and workload-level approach to managing proxy configuration, compatible with Pod Annotation. In Alibaba Cloud Service Mesh ASM, starting from v1.10, you can manage namespace-level proxy configuration in a declarative way, such as setting sidecar proxy life cycle, resource limit, and so on. istio introduced ProxyConfig from v1.13, which is similar to the above solution, and we will integrate the two in the future.