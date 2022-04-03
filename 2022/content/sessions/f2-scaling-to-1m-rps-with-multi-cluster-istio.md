---
id: f2
title: "Scaling to 1M RPS with multi cluster Istio"
url: /sessions/scaling-to-1m-rps-with-multi-cluster-istio
speakers:
 - Devarajan Ramaswamy
 - Nizam Uddin
time_start: 2022-04-28T16:00:00.000Z
time_end: 2022-04-28T16:35:00.000Z
session_type: Presentation
track: Infrastructure & networking
track_slug: infrastructure-networking
language: English
block: f
slot: 2
---

Scaling systems to handle high throughput is an art and a journey fraught with several hurdles and blockers. We shall demonstrate how every little configuration can cause a huge impact at very high RPS, how we managed to beat 500K RPS with minimum latency and how we geared the system to be capable of handling upto 1M RPS. We shall show using the example deployment topology of Istio Service Mesh, how we addressed the issues of connection handling, load balancing shortcomings, cross cluster pitfalls, side effects of HPA, uneven resource utilization, etc.and achieved a smooth response graph at very high throughputs.