---
id: g5a
title: Moving large scale consumer e-commerce Infrastructure to Mesh
url: /sessions/moving-large-scale-ecommerce-infrastructure-to-mesh
speakers:
 - Rajath Ramesh
 - Harshad Rotithor
time_start: 2021-02-26T18:20:00.000Z
time_end: 2021-02-26T18:45:00.000Z
block: g
slot: 5
format: adoption
language: english
slides: g5a-MovingLargeScaleInfra-RajathHarshad.pdf
video:
---

In this session we will cover 
* Previous Setup: High level overview of setup focussing on external and inter-service/component communication where we mainly used Nginx, HAProxy and Envoyproxy. 
* Challenges and Improvements: Briefly cover the challenges and improvements which essentially was translated into set of requirements
* Istio Onboarding and Integration: How Istio covered our requirements and steps we took and tools we built/used to on-board micro-services and manage the mesh setup. We will also cover the challenges involved in migrating, solutions derived and learnings gained. If we need to do it again, what could be done differently. 
* Next Steps: Currently we integrated completely stateless use-cases, future plan on how we plan to on-board the stateful entities as well.