---
id: g4p
title: The benefits of integrating Apache Kafka with Istio on Kubernetes
url: /sessions/the-benefits-of-integrating-apache-kafka-with-istio-on-kubernetes
speakers:
 - Sebastian Toader
 - Zsolt Varga
time_start: 2021-02-26T17:40:00.000Z
time_end: 2021-02-26T18:20:00.000Z
block: g
slot: 4
format: presentation
language: english
---

During the past several years Apache Kafka emerged as the default enterprise message bus. With Istio on its own way to becoming the service mesh "standard" within the enterprise, running a Kafka cluster inside a mesh became a frequent requirement. We've been running Kafka over Istio for a  few years now, and in this talk, we'd like to share our experience, the common problems and eventually the benefits that led us to make this integration possible. In this talk we'll be touching on both security and operational benefits such as:
- On the fly certificate renewals with no service downtime
- Secure cross-regional interaction between workloads and Kafka
- Unified simplified configuration to enable mTLS for all components
- Single cluster and cross-cluster workload authn/authz of K8s service accounts using Envoy WASM filters
- Envoy WASM filters open the gates for a whole array of useful features such as Kafka protocol level metric