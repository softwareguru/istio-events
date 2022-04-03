---
id: d5d
title: "Testing Istio’s Virtual Machine integration locally with Calico"
url: /sessions/testing-vm-integration-calico
speakers:
 - Nina Polshakova
time_start: 2022-04-27T19:00:00.000Z
time_end: 2022-04-27T19:10:00.000Z
session_type: Lightning talk
track: Tools, features & functionality
track_slug: tools-features-functionality
language: English
block: d
slot: 5d
---

Istio provides native Virtual Machine integration for legacy applications which requires IP connectivity to the East/West gateway deployed in the mesh, and optionally connectivity to the pod networking for enhanced performance.
 
 In production deployments, the communication between Kubernetes nodes and non-Kubernetes nodes are often handled with sophisticated techniques like VPC or VPN, but on a developer machine your Kubernetes nodes may be running in a simulated environment such as minikube, k3s or kind. It can be tricky to test this locally on a developer setup. How can you test calls from a Kubernetes service locally to and from a service on a VM without using LoadBalancer type Kubernetes services - using only Cluster-IP or Pod-IP? 
 
 In this session, I will talk about challenges you may face in a developer setup and how using the Calico Networking Plugin enables you to develop VM integrated meshes without LoadBalancer services in both single network and multi network environments.