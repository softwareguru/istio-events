---
id: c3
title: "Gatekeeper + Istio, FTW"
url: /sessions/gatekeeper-istio
speakers:
 - Mathieu Benoit
 - Ernest Wong
time_start: 2022-04-28T19:50:00.000Z
time_end: 2022-04-28T20:25:00.000Z
session_type: Presentation
track: Tools, features & functionality
track_slug: tools-features-functionality
language: English
block: c
slot: 3
---

This session will demonstrate how Gatekeeper policies could help you make sure your Kubernetes cluster and your Istio mesh are secure and compliant with common and your own best practices. We'll see in action how to guarantee that the deployed resources like Namespace, Service, AuthorizationPolicy, Sidecar, etc. are properly written. And because shifting left security guardrails is important, we'll also illustrate how you could catch such policy violations in your Continuous Integration (CI) system, before actually applying these resources in your Kubernetes clusters.