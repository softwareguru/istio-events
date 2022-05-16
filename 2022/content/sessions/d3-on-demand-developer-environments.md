---
id: d3
title: "On-demand Developer Environments in Mesh based Infrastructure"
url: /sessions/on-demand-developer-environments
speakers:
 - Rajath Ramesh
 - Edward Samuel Pasaribu
time_start: 2022-04-27T16:40:00.000Z
time_end: 2022-04-27T17:15:00.000Z
session_type: Presentation
track: Tools, features & functionality
track_slug: tools-features-functionality
language: English
block: d
slot: 3
slides: d3-OndemandDeveloperEnvironment
video: https://youtu.be/p9ayBEQSnq0
---

In a micro-service architecture - development and testing changes, in a service or set of services involved in a feature, without affecting stability of shared environments like staging, pre-prod, etc. is challenging. 
 
We are excited to share an approach to tackle it by spinning up a developer/feature environment on demand, which only contains a subset of services that have code changes. Traffic to other services and datastores, which are not in the developer environment, is routed to a shared environment. This whole setup is orchestrated by Istio service mesh. With this, we can have multiple developer environments running in-parallel sharing the same shared environment - enabling the developer and/or feature development team to have an isolated environment to test out the code changes and rollout with confidence.  
 
This has been adopted across our organisation, improving the developer productivity & experience along with stability of shared environments while keeping costs in check.