---
id: d8p
title: Deep Dive into Istio Auth Policies
url: /sessions/deep-dive-into-istio-auth-policies
speakers:
 - Lawrence Gadban
time_start: 2021-02-24T21:00:00.000Z
time_end:   2021-02-24T21:40:00.000Z
block: d
slot: 8
format: presentation
language: english
tags:
slides: d8p-DeepDiveAuthPolicies-LawrenceGadban.pdf
video:
---

One of the primary benefits of using Istio is its comprehensive security model, which enables users to express complex authentication and authorization policies for the services running within their mesh. While these security features are commonly used, they can cause confusion and are frequently misunderstood.

This talk will explore the security mechanisms available in Istio and will dive into how these policies are translated from high-level user-facing configuration to runtime policies in the various Envoy proxies that comprise the Istio data plane.

Specifically, we will look at the following:
* Mutual TLS and how to configure peer authentication through PeerAuthentication and DestinationRule resources
* Enforcing end-user authentication via JWTs with RequestAuthentication resources
* Enforcing authorization rules through AuthorizationPolicy resources

Attendees will leave with a clear picture of how Istio’s various auth policies are implemented in the data plane.
