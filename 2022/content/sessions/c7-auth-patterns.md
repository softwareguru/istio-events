---
id: c7
title: "Auth Patterns: What to Use and When"
url: /sessions/auth-patterns
speakers:
 - Aaron Teague
time_start: 2022-04-26T19:50:00.000Z
time_end: 2022-04-26T20:25:00.000Z
session_type: Presentation
track: Tools, features & functionality
track_slug: tools-features-functionality
language: English
block: c
slot: 7
slides: c7-AuthPatterns.pdf
video: https://youtu.be/aVsvL9EClHU
---

One of the great things about Istio is that it provides a solid mechanism for service to service auth within a mesh using mTLS and AuthorizationPolicy

But what if the thing accessing your services is not in the mesh. What if it’s a person and not a process? What if it’s a customer instead of an employee in your organization?

Suddenly, the options and tools to fulfill them become overwhelming. Let’s break down our patterns and tools to determine which to use and when.