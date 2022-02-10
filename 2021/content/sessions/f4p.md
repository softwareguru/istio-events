---
id: f4p
title: "Istio Debugging: Finding and Fixing Issues in a Multi-cluster Service Graph"
url: /sessions/istio-debugging-finding-and-fixing-issues-in-a-multi-cluster-service-graph
speakers:
 - Scott Weiss
 - Eitan Yarmush
time_start: 2021-02-25T17:40:00.000Z
time_end: 2021-02-25T18:20:00.000Z
block: f
slot: 4
format: presentation
language: english
video: https://www.youtube.com/embed/0oaiJbfIKwI
---

Istio has some basic tooling to facilitate request troubleshooting, but it has something much more powerful at its core: Envoy proxy. When requests in the mesh start failing, Envoy is the definitive source for debugging information as it has a wealth of telemetry and logging that can be enabled to pinpoint problems along the request path. Trouble with certificates? Incorrect headers? Connection pooling or upstream errors? Un-routable request?

In this talk, we’ll look at how to build a repeatable and automatable set of tools to quickly debug a request path across multiple hops and potentially across multiple clusters and Istio control planes. Leveraging Envoy capabilities like access logging, module debug logging, the tap filter, configuration dumps, and detailed telemetry across multiple hops in the data path combined with some best practices, you will no longer have to worry when things appear to “not be working”.