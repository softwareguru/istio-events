---
id: f4
title: "API Gateway on Service Mesh - Complete Zero Trust"
url: /sessions/api-gateway-on-service-mesh
speakers:
 - Anil Attuluri
 - Shriram Sharma
time_start: 2022-04-28T17:20:00.000Z
time_end: 2022-04-28T17:55:00.000Z
session_type: Presentation
track: Infrastructure & networking
track_slug: infrastructure-networking
language: English
block: f
slot: 4
---

Securing services behind a Gateway (also called API Gateway) is a common pattern in the industry. With proliferation of microservices architecture and increased communication between them it's natural for these services to be on Service Mesh. By moving the API Gateway to Service Mesh, microservices that have external clients can continue to take traffic from API Gateway while converging their ingress onto a single path over Istio Service Mesh. At Intuit, this approach resulted in a complete zero trust model architecture and greatly simplified the networking and traffic management for the applications. It also helped accelerate their journey to Service Mesh. This was made possible with Istio’s Sidecar tls termination implementation which provides a way for regular TLS termination on Service mesh sidecar. In this talk Shriram and Anil will elucidate the pattern used, the Istio feature implementation and their journey to make API Gateway part of the Service Mesh.