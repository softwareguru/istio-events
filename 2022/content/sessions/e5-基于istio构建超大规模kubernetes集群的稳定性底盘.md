---
id: e5
title: "基于istio构建超大规模kubernetes集群的稳定性底盘"
url: /sessions/基于istio构建超大规模kubernetes集群的稳定性底盘
speakers:
 - 远科 韦
time_start: 2022-04-28T04:00:00.000Z
time_end: 2022-04-28T04:35:00.000Z
session_type: Presentation
track: Tools, features & functionality
track_slug: tools-features-functionality
language: Chinese
block: e
slot: 5
---

背景
 
 蚂蚁集团运行着全球最大的 kubernetes集群之一。kubernetes 社区官方以 5K node 作为 kubernetes 规模化的事实标准，而蚂蚁集团在 2019 年的时候，就已经维护着单集群规模超过 10K node 的 kubernetes 集群，现如今规模更是远超10K，集群数量也持续增长；
 
 蚂蚁集群采用KOK（Kubernetes On Kubernetes）的方式来管理内部的众多集群。
 
 
 面临的问题
 
 集群数量多，单集群规模大，这给日常运维和稳定性保障带来了很大的挑战：
 
 1. apiserver流量均衡的问题，http2的连接复用导致实例间流量差别巨大，
 2. webhook/controller无法做到精细化的灰度发布；
 3. 原生k8s无体系化的精细限流能力，导致apiserver很容易被流量打死； 
 4. apiserver/webhook等组件的发布无损问题；
 5. 缺乏全链路追踪能力；
 
 
 我们的方案
 
 为体系化解决以上问题，我们引入了Istio。
 
 在KOK架构中，增加了ServiceMesh层来管理管控组件（apiserver/webhook/controller）之间的流量；
 
 调整之后，架构就变成了kubernetes on Istio on Kubernetes，简称KOI架构（kubernetes On Istio）；

 
 本次分享的内容
 
  1. 蚂蚁当前情况介绍，包括k8s集群的规模、当前的KOK架构及面临的问题；
  2. 蚂蚁KOI架构详细介绍； 如何利用istio来有效提升k8s管控面的稳定性、优化系统架构、提升流量调度能力及增强链路的安全性； istio落地中碰到的问题：主要包括envoy参数的调优、http2 flood check问题、k8s认证的适配等； 
  3. 通过落地istio拿到的收益；主要包括： kubernetes webhook/apiserver/controller的精细化灰度能力，支持namespace粒度；apiserver/webhook的流量均衡及无损发布能力；kubernetes大版本的无损升级能力；基于真实流量镜像实现了etcd新版本的测试仿真； 关键链路（ingress/apiserver/webhook/etcd）的全链路追踪能力；
  4. 后续计划和展望；