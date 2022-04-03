---
id: d2
title: "Understanding the new Istio Telemetry API"
url: /sessions/understanding-the-new-istio-telemetry-api
speakers:
 - Neeraj Poddar
 - Douglas Reid
time_start: 2022-04-27T16:00:00.000Z
time_end: 2022-04-27T16:35:00.000Z
session_type: Presentation
track: Tools, features & functionality
track_slug: tools-features-functionality
language: English
block: d
slot: 2
---

We have introduced the new Telemetry API in v1.11 which provides a flexible and uniform way for configuring how telemetry is generated in the mesh. Since the initial release, we have made continuous improvements in functionality by adding support for various telemetry types and expanding to more providers. In this session, we will go over the motivations and use cases that drove the design of the new API and deep dive into the following aspects:
 
 * Inheritance and override semantics.
 * Provider selection and enabling multiple providers for any telemetry type. 
 * How to easily add dimensions in Prometheus metrics, provide tracing configuration and filtering access logging at various scopes from mesh wide to a specific workload.