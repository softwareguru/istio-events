---
id: e2
title: "Our Way Improving Service Mesh Scalability"
url: /sessions/our-way-improving-service-mesh-scalability
speakers:
 - Zhonghu Xu
 - Xue Leng
time_start: 2022-04-28T02:00:00.000Z
time_end: 2022-04-28T02:35:00.000Z
session_type: Presentation
track: Infrastructure & networking
track_slug: infrastructure-networking
language: Chinese
block: e
slot: 2
---

In this session Zhonghu and Leng Xue will share how their they improved istio scalability to 10 Million sidecars. They introduced an intelligent way to make istio aware of service connectivity, so istio and envoy can achieve lazy xds pushing, which saves more than 99% memory cost of sidecars. This solution is quite different from others and is more efficient and light-weighted, they have made it production-ready in Huawei Application Service Mesh.  
 
In the meantime, they will share recent performance optimizing works on istio control plane, including xds cache, delta xds, on-demand xds, etc.   
 
At last, they will shed light on the future service mesh evolution in terms of scalability and performance. Ideally, the mesh control plane will be more light-weighted. With ebpf, the datapath will be shorter, but they thinks it is not enough, shared proxy or proxyless can be a good direction.