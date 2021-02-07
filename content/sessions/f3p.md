---
id: f3p
title: "How to manage any layer-7 traffic in an Istio service mesh?"
url: /sessions/how-to-manage-any-layer-7-traffic-in-an-istio-service-mesh
speakers:
 - Huabing Zhao
 - 阳 唐
time_start: 2021-02-25T17:00:00.000Z
time_end: 2021-02-25T17:40:00.000Z
block: f
slot: 3
format: presentation
language: english
---

Traffic management is probably the most used feature of Istio. However, handling layer-7 traffic other than HTTP and gRPC can become challenging in an Istio service mesh.  In this session, I'll discuss a few possible approaches to extend Istio's traffic management capability to other layer-7 protocols such as Dubbo, Thrift, TARS, Redis, MySql, MongoDB, etc. I'll introduce Aeraki, an open-source project that provides a framework to allow Istio to support more layer 7 protocols than just HTTP and gRPC. A demo of Thrift and Dubbo traffic version-based routing and percentage-based routing will also be shown in this session.  In the end, l'll discuss some other interesting things we are planning at Aeraki, such as on-demand xDS to the sidecars.

Github: https://github.com/aeraki-framework/aeraki
Live Demo: http://aeraki.zhaohuabing.com:3000/d/pgz7wp-Gz/aeraki-demo?orgId=1&kiosk
Recorded Demo: Dubbo and Thrift Traffic Management https://youtu.be/vrjp-Yg3Leg