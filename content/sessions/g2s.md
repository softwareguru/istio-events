---
id: g2s
title: "Istio at scale: How eBay is building a massive multitenant service mesh using Istio"
url: /sessions/istio-at-scale-ebay
speakers:
 - Sudheendra Murthy
time_start: 2021-02-26T16:25:00.000Z
time_end: 2021-02-26T16:50:00.000Z
block: g
slot: 2
format: spotlight
language: english
---

Managing a service mesh that spans hundreds of thousands of containers across the globe is no easy feat. At high scale, achieving fast configuration convergence time to thousands of proxies, while limiting the CPU & memory utilization of control-plane & proxies is a challenging problem. This talk describes eBay's initial journey into building a scalable service mesh that provides the traffic management, load-balancing, security and observability features at scale leveraging Istio. The talk presents the federated design to manage configuration across multiple meshes in different availability zones, multiple trust domains to support workloads in different environment. The talk shares results from the extensive control-plane scale and performance tests to establish the efficacy of the design to support the massive scale, provides insights into the breaking limits of Istio control-plane and sidecar proxy and finally provides best practices & recommendations to operate Istio at scale.