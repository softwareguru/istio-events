---
id: c1s
title: Going dynamic with Envoy at Atlassian
url: /sessions/going-dynamic-with-envoy-at-atlassian
speakers:
 - Nicolas Meessen
time_start: 2021-02-23T16:00:00.000Z
time_end:   2021-02-23T16:25:00.000Z
block: c
slot: 1
format: spotlight 
language: english
tags:
---

Atlassian has been deploying Envoy to the compute nodes of its internal PaaS over the past 2 years to simplify service-to-service communication for internal developers. Today we deploy Envoy with static configuration and we want to take advantage of dynamic features like client-side routing, direct communication, and fault injection. We decided Istio was the best choice to deliver this over the next year. We’ll talk through Atlassian’s journey with service-to-service communication, Envoy and the evolution of our home-grown control planes, then walk through the analysis that led to Istio being the best decision for Atlassian’s business moving forward.
