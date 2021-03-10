---
id: c8p
title: Extending Envoy with WASM from start to finish
url: /sessions/extending-envoy-with-wasm-from-start-to-finish
speakers:
 - Ed Snible
time_start: 2021-02-23T21:00:00.000Z
time_end:   2021-02-23T21:40:00.000Z
block: c
slot: 8
format: presentation
language: english
tags:
slides: c8p-ExtendingEnvoyWasm-EdSnible.pdf
video:
---

This talk is for every engineer interested in creating traffic management and telemetry capabilities for the mesh itself.

Istio has offered extensibility through WebAssembly since 1.5. User code, running in the sidecar, can implement custom traffic management and telemetry. No Istio control plane access or special builds of the sidecar are needed. C++ and JavaScript developers can write, compile, deploy and test extensions quickly, with just a bit of Istio EnvoyFilter YAML on their clusters.

Yet developers I’ve talked to are not having success getting started.  Others start but get stuck factoring their idea into a framework of HTTP protocol callbacks. Even a good design is not enough—troubleshooting extensions is difficult and some developers give up in frustration.

We’ll demystify the difference between Istio’s EnvoyFilter resource and Envoy’s HTTP filter chain.  Attends will learn the framework, code delivery, and troubleshooting using as few new concepts as possible.
