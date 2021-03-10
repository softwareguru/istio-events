---
id: e4p
title: Is Your Virtual Machine Really Ready-to-go with Istio?
url: /sessions/is-your-virtual-machine-really-ready-to-go-with-istio
speakers:
 - Kailun Qin
 - Haoyuan Ge
time_start: 2021-02-25T02:40:00.000Z
time_end:   2021-02-25T03:20:00.000Z
block: e
slot: 4
format: presentation
language: chinese
tags:
slides: e4p-VMReady-KailunQin-HaoyuanGe.pdf
video:
---

Using Kubernetes and containers is the easiest and most practical way to run Istio. However, both academic and industry surveys show that massive organizations and users are still deploying their workloads in VMs to fulfill their needs like security, multi-tenancy, fitting into the existing processes and hybrid multi-clouds. To include those workloads outside of K8s, Istio has introduced VM support since 1.6.

In this talk, we will:
- Go through the real use cases and tumultuous odyssey of Istio’s VM integration;
- Summarize the key VM mesh features, designs and tradeoffs introduced, e.g. WorkloadGroup, Smart DNS proxy and VM security incl. (auto) identity bootstrapping and cert provisioning etc.;
- Analyze the limitations of the current VM workflow, with a focus on usability and security;
- Benchmark against the performance of VM/hybrid usage and explore the bottlenecks;
- Look into the intersections with HW acceleration technologies, such as SR-IOV, SmartNIC etc. for VM mesh.
