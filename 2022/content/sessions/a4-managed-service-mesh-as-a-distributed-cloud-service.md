---
id: a4
title: "Managed service mesh as a distributed cloud service"
url: /sessions/managed-service-mesh-as-a-distributed-cloud-service
speakers:
 - Gergő Huszty
time_start: 2022-04-25T17:20:00.000Z
time_end: 2022-04-25T17:55:00.000Z
session_type: Presentation
track: Infrastructure & networking
track_slug: infrastructure-networking
language: English
block: a
slot: 4
---

The external control plane deployment model in Istio enabled some new use cases for mesh management. The ownership and the management of the control plane may belong to a completely different entity, other than the end-user.
 
Leveraging this new model, a cloud vendor can create a cost effective, managed, multi-tenant mesh control plane, safely isolated from the mesh clusters. Behind the scene, the vendor can manage/scale/update the service with or without the user's intervention.
 
In this talk I will describe such a managed solution, focusing on the extra challenges that the basic Istio external control plane setup does not solve. 

Agenda: 
 * the generic problem of running kubernetes operators and webhook services remotely to the managed cluster
 * exposing control plane endpoints
 * the problem domain of metrics collection
 * how to hide/embed/manage and automate the control-plane parts from the user
 * how and why multi-tenant control plane can be safely operated