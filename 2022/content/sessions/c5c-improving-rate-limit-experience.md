---
id: c5c
title: "Improving Rate Limit Experience for Developers in Istio"
url: /sessions/improving-rate-limit-experience
speakers:
 - Zufar Dhiyaulhaq
time_start: 2022-04-26T18:50:00.000Z
time_end: 2022-04-26T19:00:00.000Z
session_type: Lightning talk
track: Tools, features & functionality
track_slug: tools-features-functionality
language: English
block: c
slot: 5c
---

Managing Rate limit configuration in Istio is a tedious task since currently, we are setting up the EnvoyFilter object to configure the rate limit function.
 
There are some drawbacks with this approach, developers need to understand very complex configurations within EnvoyFilter. Maintenance also becomes a problem because every time the infrastructure team wants to upgrade the mesh, Developers need to check if the rate limit configuration is working on the newer version of the mesh.  

In GoPay, we are trying to improve the experience for developers to apply rate-limiting functions to their services. This is archived via Kubernetes operator that helps us abstract the details from developers.