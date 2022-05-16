---
id: a6
title: "Proxyless gRPC"
url: /sessions/proxyless-grpc
speakers:
 - Sanjay Pujare
time_start: 2022-04-25T19:10:00.000Z
time_end: 2022-04-25T19:45:00.000Z
session_type: Presentation
track: Infrastructure & networking
track_slug: infrastructure-networking
language: English
block: a
slot: 6
slides: a6-ProxylessgRPC.pdf
video: https://youtu.be/zOEtoHTEZWQ
---

gRPC has been a popular choice for building microservices based service mesh architectures especially after the recent introduction of service mesh features such as service discovery, load balancing, mTLS for transport security, and observability which eliminated the need for sidecar proxies - like Envoy - in the service mesh. The introduction of these features in gRPC enabled a "proxyless service mesh". Besides supporting Google's Traffic Director proxyless service mesh product, proxyless gRPC also works with Istio because of the use of "xDS" - the industry standard and open protocol created by Envoy. 
 
The talk will include the use-case of how you can manage gRPC workloads without having to deploy an Envoy sidecar. It will also include the current efforts to standardize Istio support across all gRPC languages and multiple environments. One of those environments is ASM - which is managed Istio in Google Cloud and the talk will include a description of that implementation.