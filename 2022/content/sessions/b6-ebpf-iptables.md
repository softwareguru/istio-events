---
id: b6
title: "Use eBPF instead of iptables to accelerate the Istio dataplane（使用 eBPF 代替 iptables 加速 Istio 数据平面）"
url: /sessions/ebpf-iptables
speakers:
 - Kebe Liu
time_start: 2022-04-26T04:40:00.000Z
time_end: 2022-04-26T05:15:00.000Z
session_type: Presentation
track: Infrastructure & networking
track_slug: infrastructure-networking
language: Chinese
block: b
slot: 6
---

Replacing iptables rules with eBPF to allow data being transported directly from inbound sockets to outbound sockets to shorten the datapath between sidecars and services.