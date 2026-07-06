# FleetConductor Pitch

更新时间：2026-07-06。该版本按 YC / Airbnb 风格 pitch spine 重写：先讲现场问题，再讲现有方案为什么失败、方案、为什么现在、产品、商业模式、壁垒、为什么 Qualcomm 必须参与、比赛演示和申请支持。

## One-Liner

FleetConductor 是给仓库、工厂、医院和园区的本地机器人塔台：

> 在现场边缘节点统一协调多品牌机器人、门梯充电、交通资源、企业工单和异常处置，让第二个机器人厂商上线不再变成一次新的系统集成项目。

## 1. Problem

商业现场真正崩掉的不是单台机器人导航，而是多机器人共用同一个空间。

仓库、工厂、医院和园区开始同时部署 AMR、AGV、清洁、配送、巡检和机械臂。每个厂商都有自己的地图、调度器、充电逻辑、dashboard 和异常流程，客户最后用群聊、电话和临时脚本协调共享空间。

痛点：

- 第二个机器人品牌进入后，地图、交通规则、充电队列、异常语义和 WMS/WES 任务都要重新集成。
- 电梯、门禁、窄走廊、装卸点、充电桩、禁区和人机混行区，才是真实部署中的瓶颈。
- 云端 dashboard 能看状态，但不能替代现场低延迟、本地连续运行和断网可用。
- 堵塞、抢梯、低电、人工接管和绕行轨迹没有进入训练/复盘数据闭环。

一句话：客户不是想再买一个 dashboard，而是想让机器人增加后，订单能派、走廊不堵、电梯不抢、云断了不瘫、事故能复盘。

## 2. Current Alternatives Fail

现在的标准和工具都是必要组件，但没有一个完整商业产品承担现场塔台责任。

- OEM fleet manager：MiR、OTTO、Locus、Geek+、Hikrobot、HAI 等系统管自家队列很强，但跨品牌和共享设施通常不是第一责任。
- VDA 5050 v3：提供 central control 与 AGV/AMR 的 MQTT/JSON 通信语言，但明确不定义安全、交通算法、外设接口、实施流程、运营责任或网络安全。
- MassRobotics AMR Interoperability：适合共享位置、状态、速度、健康和可用性，不是 fleet management、导航或安全控制系统。
- Open-RMF：证明多车队和门梯等共享资源调度可行，但真实企业项目仍需要 hardened product、commissioning、权限、安全审计、支持和商业 adapter。
- WMS / WES：Manhattan、Blue Yonder、GreyOrange、SVT 等管业务流程和集成，但不天然负责低延迟机器人交通和楼宇资源。

## 3. Solution

FleetConductor 是 WMS/WES 之下、OEM fleet manager 之上的本地塔台。

它不替代机器人厂商 autonomy stack，也不替代安全控制器。它把不同机器人 API、VDA 5050 / Open-RMF-compatible 工作流和设施接口，翻译成现场级任务、交通、门梯、充电和事件 orchestration。

核心流程：

1. Receive：从 WMS、MES、CMMS、LIMS、HIS、BMS 或人工调度台接收任务和设施事件。
2. Model：把楼层、车道、门、电梯、充电桩、队列点、禁区和地图版本变成 SiteGraph。
3. Adapt：通过 VDA 5050 v3、Open-RMF、MassRobotics、ROS 2、REST/MQTT/OPC UA/BACnet 接入。
4. Reserve：按时间窗预约走廊、电梯、门、充电桩和装卸位，避免共享资源冲突。
5. Replay：把低电、堵塞、门梯失败、人工接管和断网事件变成可审计复盘包。

## 4. Why Now

机器人密度、互操作标准和边缘 AI 硬件第一次同时成熟。

- IFR 显示，2024 年全球工业机器人新增安装约 542,000 台，连续第四年超过 500,000 台。
- IFR 也显示，2024 年专业服务机器人销量接近 20 万台，运输/物流是最大专业服务机器人类别之一。
- VDA 5050 3.0.0 于 2026-03 发布，异构移动机器人通信继续标准化。
- ROS 2 LTS、Open-RMF、MassRobotics、CloudEvents、OpenAPI、AsyncAPI 让现场塔台可以从集成项目变成可产品化平台。
- Qualcomm Dragonwing / IQ edge hardware 把本地多摄像头、NPU、连接、离线运行和边缘 AI profile 放到同一个现场 appliance 里。

## 5. Product

先做 second-vendor rollout kit，再扩展为多站点机器人塔台。

第一阶段：

- 接入 WMS/WES + Vendor A fleet manager + Vendor B fleet manager + 一个共享设施资源。
- 提供统一状态、incident response、adapter normalization、共享区 traffic control 和 audit trail。
- 证明更快部署、更少人工干预、更高利用率和更清晰责任边界。

核心模块：

- Edge Tower Runtime：本地任务队列、交通调度、资源预约、事件日志和 store-and-forward。
- Adapter Hub：VDA 5050 v3、Open-RMF、MassRobotics、ROS 2、vendor API、OPC UA、BACnet。
- SiteGraph + Map Federation：多楼层、车道、门梯、充电桩、坐标变换、地图版本和运行时封控。
- Traffic Manager：time-windowed reservation over graph edges, intersections, doors, elevators, charger docks, narrow areas。
- RBAC + Audit：角色、权限、指令风险、审批、设备 ack、replay pointer 和 append-only audit。
- Incident Replay + LeRobot Export：事件时间线、视频片段、人工接管和训练/回放/eval 数据包。

### Reference Architecture

```text
Dragonwing / IQ edge tower appliance
  ├─ api-gateway
  ├─ operator-ui
  ├─ site-graph
  ├─ map-federation
  ├─ traffic-manager
  ├─ task-manager
  ├─ robot-adapter-runtime
  ├─ resource-manager
  ├─ incident-replay
  ├─ rbac-audit
  ├─ event-bus
  └─ sync-agent
```

Data plane:

- Postgres for durable state.
- Append-only event log.
- Object storage for replay media and map releases.
- NATS JetStream or MQTT internally.
- MQTT specifically for VDA 5050 robots.
- Cloud optional for licensing, analytics, remote support and model/package updates; never required for live dispatch.

### Core Schemas

```json
{
  "SiteGraph": {
    "site_graph_id": "acme-medical-tower",
    "version": "2026.07.06",
    "nodes": ["L1_lobby", "L2_pharmacy", "B1_loading"],
    "resources": ["door-01", "lift-service-a", "charger-03"],
    "checksum": "sha256:..."
  },
  "RobotAdapter": {
    "fleet_id": "delivery_vda5050",
    "mode": "vda5050|rmf_ros2|vendor_rest_grpc|traffic_light|observe_only",
    "capabilities": ["pose", "pause", "resume", "dock", "charge"],
    "health": "ok|degraded|offline"
  },
  "ReservationLease": {
    "resource_id": "lift-service-a",
    "holder": "robot-delivery-02",
    "valid_from": "2026-07-06T12:00:00Z",
    "valid_to": "2026-07-06T12:02:00Z",
    "reason": "pharmacy_delivery"
  },
  "Incident": {
    "incident_id": "inc_elevator_timeout_001",
    "kind": "elevator_timeout",
    "site_graph_version": "2026.07.06",
    "replay_pointer": "s3://replay/inc_elevator_timeout_001"
  }
}
```

## 6. Market And Business Model

卖的不是 generic fleet management，而是更快上线第二个机器人厂商。

第一批客户：

- 3PL / contract logistics：多客户、多站点、多机器人品牌、峰值波动和 SLA 压力。
- e-commerce / retail fulfillment：频繁扩容、季节波峰、WMS/WES 深度集成。
- 制造业：汽车、电子、半导体、工业制造，VDA 5050 相关性强。
- 医院 / 机场 / 园区：门梯、禁区、巡检、清洁、配送和服务机器人共存。
- 系统集成商、WMS/WES vendor、robot OEM、RaaS provider：把一次性集成变成可复用 IP 和持续服务收入。

海外定价：

- Pilot / site setup：$25k-$150k per site。
- Platform fee：$3k-$15k / site / month。
- Observe / monitor：$75-$200 / robot / month。
- Active dispatch / traffic / charger optimization：$250-$700 / robot / month。
- Enterprise network：10+ sites negotiated annual license。
- RaaS attach：5%-12% of robot RaaS MRR 或 $100-$400 / robot / month。

中国定价：

- 更适合本地部署、私有化、项目制和 SI-led delivery。
- 人民币 10k-40k / site / month。
- 人民币 100-500 / robot / month。
- 或人民币 100k-500k project license + 15%-20% annual maintenance。

## 7. Competition And Moat

竞争不是“没人做”，而是现有方案各自解决一层。

- Cloud RobOps / observability：InOrbit、Formant、WAKU、Freedom Robotics / Rocos。
- Vendor-agnostic FMS：Meili、SYNAOS、KINEXON、BlueBotics ANT server、Mushiny Synall、SEER RDS。
- Open / developer middleware：Open-RMF、NVIDIA Isaac Mission Dispatch / Mission Control、MOV.AI、Rapyuta。
- OEM fleet managers：MiR Fleet、OTTO Fleet Manager、LocusONE、KUKA.AMR Fleet、Geek+、Hikrobot、HAI、Quicktron、ForwardX。
- WMS/WES / orchestration：Manhattan、Blue Yonder、GreyOrange、SVT Robotics、Tecsys。
- Building integration：Otis、KONE、Aethon ReadyElevator、Relay Robotics、Pudu。

FleetConductor 的壁垒：

- Facility graph：每个商业站点的楼层、门梯、走廊、充电、禁区、WMS/WES 和运营规则会形成黏性资产。
- Adapter compound：机器人、门梯、充电、WMS/MES/CMMS/BMS 的 adapter 越多，交付速度越快。
- Incident memory：堵塞、抢梯、低电、人工接管和绕行会变成下一站点配置、仿真场景和训练数据。
- Qualcomm edge profile library：不同 Dragonwing/RB/QCS/IQ target 的相机、NPU、网络、热、电源和离线行为形成 profile library。
- SI/OEM/RaaS channel compounding：越多伙伴使用，越多 connector 和 deployment pattern 可复用。

## 8. Why Qualcomm

Qualcomm 不应只展示“单台机器人跑 AI”，而应展示“一个商业站点如何用 Qualcomm 边缘节点协调一群机器人”。

FleetConductor 对 Qualcomm 的价值：

- 把 RB3 / IQ / Dragonwing 从开发板叙事升级成现场 edge tower appliance。
- 把 AI Hub / QNN compile-profile-run 结果变成机器人上线门禁和现场证据。
- 用多摄像头、NPU/GPU/DSP、Wi-Fi/private 5G、低功耗边缘计算支持商业站点的本地协同。
- 让 Qualcomm 进入 WMS/WES、SI、RaaS、设施系统和混合机器人站点，而不只停留在单机 BOM。

需要 Qualcomm 支持：

- RB3 Gen 2 / Dragonwing IQ10 / IQ-9075 硬件访问或技术 profile。
- AI Hub / QNN 技术指导，把 edge profile 写入上线门禁。
- 机器人 OEM、系统集成商或 WMS/WES pilot introduction。
- 允许作为 Qualcomm edge robotics reference workflow 继续打磨。

## 9. Competition Demo

8 分钟 demo：一个医院/仓库现场，三种机器人抢同一部电梯。

Demo site：`Acme Medical Tower`

- Levels：`B1_loading`、`L1_lobby`、`L2_pharmacy`。
- Fleets：`delivery_vda5050`、`cleaning_ros2`、`security_vendor_rest`。
- Robots：2 台配送 AMR、1 台清洁机器人、1 台巡检机器人、1 个 simulator。
- Infrastructure：6 扇自动门、2 部服务电梯、4 个 charger、3 个 queue zone、2 个 restricted zone。
- Tasks：pharmacy delivery、linen pickup、lobby cleaning、patrol loop、forced charge。
- Incidents：elevator timeout、narrow-corridor deadlock、charger occupied、manual door override。

演示流程：

1. Second Vendor：接入 delivery_vda5050、cleaning_ros2、security_vendor_rest 三个 fleet adapter 和同一张 SiteGraph。
2. Conflict：同时出现药房配送、清洁任务和巡检任务，三台机器人争抢电梯、窄走廊和充电桩。
3. Edge Tower：FleetConductor 本地预约电梯、门、走廊和充电窗口；断开云端后继续运行并记录事件。
4. Replay：导出 incident capsule、audit trail、CloudEvents log 和 LeRobot-compatible recovery episode。
5. Qualcomm profile：展示 Dragonwing / IQ edge target 上的本地推理、视频摘要、事件 replay 和 AI Hub/QNN profile。

## Claims To Avoid

- 不说开箱支持所有机器人、所有电梯、所有门禁和所有 WMS。
- 不说 FleetConductor 替代机器人本体安全控制器、site risk assessment 或 certified building systems。
- 不说 VDA 5050 是安全标准、自动处理 traffic，或解决所有 interoperability。
- 不说 MassRobotics、VDA 5050 和 Open-RMF 可以互换。
- 不说 guaranteed collision-free、零事故、零停机、无人监管。
- 不说 Wi-Fi/5G 是安全关键控制链路，除非有站点设计、QoS 和认证证据。
- 不说 LeRobot 数据回流会自动产生可上线策略；必须经过仿真、shadow mode、受限 rollout 和 OEM approval。
- 不说一个边缘盒子可以直接控制消防、电梯或门禁；正确说法是通过授权设施接口发起请求并记录结果。
- 不声称 Qualcomm 官方认证、投资、合作或背书，除非签署。

## Sources

- VDA 5050：https://www.vda.de/en/topics/automotive-industry/vda-5050
- VDA 5050 GitHub：https://github.com/VDA5050/VDA5050
- Open-RMF：https://www.open-rmf.org/
- Open-RMF interfaces：https://openrmf.readthedocs.io/en/latest/interfacing/index.html
- Open-RMF fleet adapter tutorial：https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html
- MassRobotics AMR standard：https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/
- IFR industrial robot demand：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- AMR/AGV fleet management software market：https://www.marketsandmarkets.com/PressReleases/amr-agv-fleet-management-software.asp
- SVT Robotics：https://www.svtrobotics.com/
- NIST SP 800-82 Rev. 3：https://csrc.nist.gov/News/2023/nist-publishes-sp-800-82-revision-3
- ISO 3691-4：https://www.iso.org/standard/83545.html
- ANSI/RIA R15.08 overview：https://www.automate.org/robotics/industry-insights/mobile-robot-standard-r15-08-1-2020-what-you-need-to-know
- Qualcomm IQ-9075：https://www.qualcomm.com/internet-of-things/products/iq9-series/iq-9075
- Qualcomm Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- CloudEvents：https://cloudevents.io/
- OpenAPI：https://swagger.io/specification/
- AsyncAPI：https://www.asyncapi.com/docs/reference/specification/latest
- InOrbit API docs：https://developer.inorbit.ai/docs
- Formant fleet management：https://docs.formant.io/docs/getting-started-fleet-management
