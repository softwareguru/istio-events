---
id: c2
title: "How I upgraded 3000 proxies in my sleep - and you can too!"
url: /sessions/upgrade-proxies
speakers:
 - Mitch Connors
time_start: 2022-04-26T16:00:00.000Z
time_end: 2022-04-26T16:35:00.000Z
session_type: Presentation
track: Tech evolution & what's next
track_slug: tech-evolution-whats-next
language: English
block: c
slot: 2
---

Keeping Istio up to date can be quite a chore. With monthly patch releases and quarterly minor releases, many users fall behind on upgrades, exposing their traffic to known CVEs and bugs. Upgrades can feel risky and unpredictable, with gateways acting as a single point of failure, and proxies upgrading unexpectedly. 
 
This talk will cover lessons learned at Google, where we have performed 1700 control plane upgrades and 3000 data plane upgrades on behalf of our users in the last year. We will explore the patterns and practices employed to keep users up to date, and show how open source users can take advantage of these principles as well. We will demonstrate using OSS tooling and gitops to handle upgrading an entire service mesh across a minor release with only two (automatically generated) pull requests.