---
id: f5b
title: "Egress Woes: Debugging external service traffic in Istio"
url: /sessions/egress-woes
speakers:
 - Gregory Hanson
time_start: 2022-04-28T18:40:00.000Z
time_end: 2022-04-28T18:50:00.000Z
session_type: Lightning talk
track: Getting started
track_slug: getting-started
language: English
block: f
slot: 5b
slides: f5b-EgressWoes.pdf
video: https://youtu.be/opLiXzkseCI
---

You have successfully deployed Istio, there are sidecars injected in all your services and pods can talk to each other. Now it's time to start looking outside your service mesh and getting your pods talking to services outside of your cluster. It's time to introduce ServiceEntries. Defining traffic routing behavior in Istio for external services does not happen automatically. Users need to often create four separate CRD's to define external traffic routing behavior and that introduces four potential avenues for bugs to get introduced. This talk will cover common pitfalls in egress configurations and debugging techniques for when those calls to external databases start failing.