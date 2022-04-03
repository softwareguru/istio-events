---
id: d4
title: "Sidecarless with eBPF or sidecar with Envoy proxy?"
url: /sessions/sidecarless-ebpf-envoy
speakers:
 - Idit Levine
time_start: 2022-04-27T17:20:00.000Z
time_end: 2022-04-27T17:55:00.000Z
session_type: Presentation
track: Tech evolution & what's next
track_slug: tech-evolution-whats-next
language: English
block: d
slot: 4
---

eBPF and service mesh both optimize the functionality around networking, observability, and security. Are they competing? Or complementary to each other? To what extent can eBPF play a role in a service mesh? How does the role of the service proxy change? In this talk, we will dig into the role of eBPF for a service mesh data plane and what are some of the tradeoffs in terms of features, resource overhead, feature isolation, security granularity and upgrade impact for various data-plane architectures: shared proxy vs shared proxy per node vs sidecar proxy vs shared proxy per service account etc.