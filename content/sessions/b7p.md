---
id: b7p
title: Performance tuning and best practices in a Knative based, large-scale serverless platform with Istio
url: /sessions/performance-tuning-and-best-practices-in-a-knative-based,-large-scale-serverless-platform-with-istio
speakers:
 - Gong Zhang
 - Yu Zhuang
time_start: 2021-02-23T04:40:00.000Z
time_end:   2021-02-23T05:20:00.000Z
block: b
slot: 7
format: presentation 
language: chinese
tags:
---

Istio is the default networking layer solution of Knative and it is leveraged for routing, traffic splitting, security and so on. We're now building a large-scale, multi-tenant serverless platform on top of Knative and Istio. While building it, one of the main questions was how to tune Istio together with Knative so it can unleash the maximum scalability and performance. 

In this session, we will share how we detected performance bottlenecks using difficult but fruitful analysis processes, tuned and optimized Istio and our platform, and eventually reduced over 90% latency in Knative service provision scenario. Also we'll share our best-practices about how to fully leverage rich functionalities provided by Istio itself to improve performance in Knative platform, such as namespace isolation, CNI replacement, mTLS without sidecar, tunings and so on.
