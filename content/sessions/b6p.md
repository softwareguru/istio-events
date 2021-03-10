---
id: b6p
title: Preserve Original Source Address within Istio
url: /sessions/preserve-original-source-address-within-istio
speakers:
 - Zhonghu Xu
time_start: 2021-02-23T04:00:00.000Z
time_end:   2021-02-23T04:40:00.000Z
block: b
slot: 6
format: presentation 
language: chinese
tags:
slides: b6p-PreserveOriginalAddress-ZhonghuXu.pdf
video: 
---

Original source address is heavily relied on by many scenarios, however in service mesh, with sidecar injected and traffic proxied by a sidecar, it is naturally unable to get the original client ip address.

In this presentation, Zhonghu will introduce what istio and envoy have done to help preserve original source ip both for TCP and HTTP protocols. And then he will present a live demo about how to achieve original src IP preserve with proxy protocol, original source filter, and TProxy.
