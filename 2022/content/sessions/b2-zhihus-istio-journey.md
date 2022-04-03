---
id: b2
title: "Zhihu‘s istio Journey"
url: /sessions/zhihus-istio-journey
speakers:
 - 阳 唐
 - 楚瑜 谢
time_start: 2022-04-26T02:00:00.000Z
time_end: 2022-04-26T02:35:00.000Z
session_type: Presentation
track: Use case
track_slug: use-case
language: Chinese
block: b
slot: 2
---

In this presentation, we will talk about how we upgraded our microservices architecture by using istio in large scale clusters. Including:  
 1. How to make istio managed services and our existing services communicate with each other. 
 2. Use istio's dynamic routing capabilities to implement sandbox functionality. 
 3. Simplified the configuration management of istio by introducing a new CR (istiofilter) and implementing a new management console.
 4. Simplify the rate limit configurations by implementing a new CR.
 5. Performance tuning in large scale clusters. 
 
 
 在本次演讲中，我们要谈谈我们如何在大规模集群下使用istio升级我们的微服务架构。
 这包括：
 1. 如何使 istio 管理的服务和现存服务之间可以互相通信。
 2. 使用 istio 动态路由的能力实现沙箱功能。
 3. 通过引入一个新的自定义资源 istiofilter 来简化 istio 的各项配置管理，并通过此实现一个 istio 的管理平台。
 4. 通过一个新的自定义资源实现限流配置的简化管理。
 5. 大规模集群性能优化
 
 等等