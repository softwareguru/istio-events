---
id: e7p
title: Accelerate istio-cni with ebpf
url: /sessions/accelerate-istio-cni-with-ebpf
speakers:
 - Yizhou Xu
 - Ruijing Guo
time_start: 2021-02-25T04:40:00.000Z
time_end:   2021-02-25T05:20:00.000Z
block: e
slot: 7
format: presentation
language: chinese
tags:
slides: e7p-AccelerateIstioCNIwithebpf-XuYizhou-GuoRuijing.pdf
video:
---

Datapath between envoy(sidecar) and service is an nonnegligible part in Istio, Isito-cni inserts iptables to intercept and redirect traffic between envoy and service, which brings costs like real TCP/IP traffic over loopback and has to insert IPTables rules.

eBPF is a revolutionary technology that can run sandboxed programs in the Linux kernel without changing kernel source code or loading kernel modules.Replacing iptables with ebpf  allows data traverse from Envoy‘s inbound socket to its outbound socket directly,reducing datapath over loopback interface and sparing iptable rules. 

In this session, we will briefly introduce what the ebpf is and how it accelerates the  Istio with real case studies. Then we will show the performance improvement and comparison data of these cases with/witout ebpf.
