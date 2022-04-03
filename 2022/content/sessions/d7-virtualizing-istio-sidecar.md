---
id: d7
title: "Virtualizing the Istio Sidecar"
url: /sessions/virtualizing-istio-sidecar
speakers:
 - Christian Posta
time_start: 2022-04-27T19:50:00.000Z
time_end: 2022-04-27T20:25:00.000Z
session_type: Presentation
track: Tech evolution & what's next
track_slug: tech-evolution-whats-next
language: English
block: d
slot: 7
---

Istio derives a bulk of its power from Envoy proxy which gets deployed as a sidecar to a running application. However, sidecar deployments are not the only way to achieve service-mesh capabilities. In this talk we discuss the work we've been doing to "virtualize" the Istio sidecar for our users by giving options for sidecar, service-account, shared-node, and even remote proxies and micro proxies.