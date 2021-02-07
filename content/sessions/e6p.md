---
id: e6p
title: Extending service mesh capabilities using a streamlined way based on WASM and ORAS
url: /sessions/extending-service-mesh-capabilities-using-a-streamlined-way-based-on-wasm-and-oras
speakers:
 - Xi Ning Wang
time_start: 2021-02-25T04:00:00.000Z
time_end:   2021-02-25T04:40:00.000Z
block: e
slot: 6
format: presentation
language: chinese
tags:
---

With the introduction of WebAssembly (for short,WASM) support, you can extend the data plane's functionality by writing custom Filters for out-of-process Envoy proxy in service mesh. But it's not easy to build, deploy and run WASM filters within service mesh. ORAS  is a proposed implementation for the OCI Artifacts project, which aims to extend the OCI registry specification and simplify storing arbitrary content in OCI registries.  

In this topic, we will present how to use ORAS client to push the WASM modules with the allowed media types into ACR registry, and then deploy the WASM filter into all the pods corresponding to the specified workload selection criteria. All the steps in the WASM filter deployment are using a declarative way, meaning that you can create one CRD to describe the WASM filter deployment. Then the WASM module can be loaded into the corresponding Envoy proxy in the data plane layer. Meanwhile, the Istio EnvoyFilter CR is created in the control plane layer.

