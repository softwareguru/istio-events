---
id: a3
title: "External CA integration with Istio explained"
url: /sessions/external-ca-integration-with-istio-explained
speakers:
 - Lin Sun
 - Josh van Leeuwen
time_start: 2022-04-25T16:40:00.000Z
time_end: 2022-04-25T17:15:00.000Z
session_type: Presentation
track: Tools, features & functionality
track_slug: tools-features-functionality
language: English
block: a
slot: 3
---

Most organizations already have their PKI system in place before they adopt Istio or any service mesh. There are a few approaches in the Istio community, either plugging in your intermediate CA as secrets manually, or use the istio-csr open source project, or leverage Kubernetes CA or Kubernetes Certificate Signing Request (CSR) API. This talk dives into the few approaches out there in the service mesh community to tackle this challenge and the tradeoffs among them.