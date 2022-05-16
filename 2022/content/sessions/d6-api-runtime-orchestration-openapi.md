---
id: d6
title: "API runtime Orchestration with Istio and OpenAPI 3"
url: /sessions/api-runtime-orchestration-openapi
speakers:
 - Anil Attuluri
 - Siva Thiru
time_start: 2022-04-27T19:10:00.000Z
time_end: 2022-04-27T19:45:00.000Z
session_type: Presentation
track: Tech evolution & what's next
track_slug: tech-evolution-whats-next
language: English
block: d
slot: 6
slides: d6-APIRuntimeOrchestration.pdf
video: https://youtu.be/ZSobk611_IY
---

API-as-a-Product is an emerging concept in software development. Open API 3 enables faster and collaborative API development and its custom extensions can be leveraged to augment API contracts with additional functionality. Here at Intuit we built a system that uses Open API spec, Istio Service Mesh and other extensions to generate capability/orchestration APIs and dynamically generate the runtime for them. It includes K8s resource manifests and Istio VirtualServices for routing rules to enable faster API delivery. This runtime supports API patterns like aggregation, transformation and proxy and can be used uniformly across both north-south (via API Gateway on Mesh) and east-west traffic. Such an API orchestration runtime will allow you to create and present new and elegant APIs on top of existing APIs while adhering to industry best practices. Come and learn how Intuit’s API Management Platform team built a low code / no code runtime solution for API orchestration using Istio.