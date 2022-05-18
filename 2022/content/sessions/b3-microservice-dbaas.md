---
id: b3
title: "The road to microservice for Database as a Service (DBaaS) via Istio"
url: /sessions/microservice-dbaas
speakers:
 - Peng Hui Jiang
 - Huailong Zhang
time_start: 2022-04-26T02:40:00.000Z
time_end: 2022-04-26T03:15:00.000Z
session_type: Presentation
track: Tools, features & functionality
track_slug: tools-features-functionality
language: Chinese
block: b
slot: 3
slides: b3-microservice-dbaas.pdf
video: https://youtu.be/NyIleb63pCk
---

Database as a Service (DBaaS) saw a significant growth YoY. One reason for the growth of DBaaS is explosive growth of data. The pandemic created strong data growth.
 
However, well designed DBaaS systems tend to adopt a stateless, loosely coupled architecture, with efficient message passing to produce a scalable, stable and reliable service. In addition, serving for multi-tenants to reduce cost and provide highly availability and scalability is a important offering of DBaaS.

Successful multi-tenant platforms require massive scalability, online patching/upgrading, the ability to process high volumes of data ingestion.
 
To make the DBaaS become more cloud native, there is a journey to migrate the legacy monolithic systems into microservice architecture. And as an excellent project of service mesh, Istio become the first choice to help to complete this process. 
 
In this talk, the audience can know the whole process to build a DBaaS in cloud native mode via Istio.