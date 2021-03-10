---
id: g7p
title: Leveraging Istio to Reduce Engineering Effort for API testing
url: /sessions/leveraging-istio-to-reduce-engineering-effort-for-api-testing
speakers:
 - Venky Ganti
 - Rahul Lahiri
time_start: 2021-02-26T19:40:00.000Z
time_end: 2021-02-26T20:20:00.000Z
block: g
slot: 7
format: presentation
language: english
slides: g7p-LeveragingIstioAPITesting-Venky-Rahul.pptx.pdf
video: https://www.youtube.com/embed/fl_tYzYXwn0
---

Microservices applications rely on complex interactions among services. Engineering teams must create API tests with API mocks to shift testing left. Current approaches to mock creation are manual, which is expensive and inefficient. 

We illustrate how Istio can be leveraged to significantly reduce engineering effort necessary for API testing.  

API tests can be built using the following Istio capabilities: 
- Dynamic deployment of Envoy filters to capture relevant examples of API requests and responses.  
- Observability to trace request execution flows across all microservices.  
- Virtual services can switch traffic between live services and mocks with no code changes. 

Developer benefits: 
- Ad hoc service testing locally leveraging API data to mock producer services
- Create service tests with auto-created API mocks, eliminating costly manual API mock creation
- Get visibility into failed API requests from end-to-end tests with no additional effort
