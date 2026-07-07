# EdgeFleet Pitch

更新时间：2026-07-06。本页按 YC / Airbnb 风格重写：问题、现有替代方案为什么失败、解决方案、为什么现在、产品、API/证据、市场、竞争壁垒、为什么 Qualcomm、演示和请求。

## One-Line Pitch

EdgeFleet 是 Qualcomm-first 机器人队列的 progressive delivery 与 evidence backbone：把模型、地图、配置、QNN artifact、Dragonwing device profile、灰度发布、远程协助、事故包、回滚和失败数据回流做成 RaaS/OEM/SI 可以用来保证 uptime、降低 truck roll、处理质保和训练下一版技能的运营系统。

## Thesis

机器人商业化的核心风险正在从 “能不能 demo” 变成 “能不能长期运营”。

RaaS 让客户不用买机器人，但风险没有消失；风险被转移给 OEM、RaaS operator、系统集成商和售后团队。他们真正需要的不是又一个 dashboard，而是：

> LaunchDarkly + SRE rollout discipline + incident replay + warranty ledger for production robot fleets.

EdgeFleet 的承诺：每个模型、每次发布、每次失败、每次远程协助、每次回滚，都能追到具体机器人、站点、技能、QNN artifact、传感器状态和训练数据。

## 01 · Problem

客户不买 demo 视频，客户买可运营、可回滚、可审计的机器人劳动。

上线之后，企业会问：

- 哪台机器人在运行哪个模型、哪个技能、哪个 QNN artifact、哪个 OS image、哪个地图和哪个配置？
- 这次失败来自传感器、模型、网络、现场、任务配置、热降频还是操作员？
- 新版本如何 shadow、canary、暂停、回滚？
- 远程协助是谁批准的，权限多大，持续多久，命令有没有越界？
- 事故前后有没有可校验证据，而不是几张截图？
- 失败片段能否进入下一轮 TeleopStudio、TrainRouter 和 CloudTwin，而不是留在客服工单里？

如果回答不了这些问题，机器人就会停在 pilot，无法进入可续费的生产部署。

## 02 · Current Alternatives Fail

### Robot Fleet Dashboards

Formant、Viam、InOrbit、Foxglove、OEM 云平台都证明 RobOps 有预算。但多数产品强在 observability、teleop、data 或 orchestration；EdgeFleet 的切入点是 release governance：谁获得新模型，什么时候上线，在什么安全条件下验证，如何回滚，保留什么证据。

### Generic IoT OTA

AWS IoT Jobs、Greengrass、Azure IoT Edge、Kubernetes rollout 和 LaunchDarkly 都提供好类比，但机器人不是普通 IoT 设备。机器人更新需要地图、传感器、任务队列、安全状态、人工覆盖、客户 SLA 和物理空间上下文。

### OEM Fleet Clouds

PUDU、Geek+、HAI、SEER、Keenon、Gausium、Boston Dynamics Orbit 等都可能有强 fleet software。EdgeFleet 不能声称 OEM 没软件；更准确的说法是：EdgeFleet sits above OEM tools，做跨品牌、跨模型、跨 Qualcomm profile 的 evidence and release layer。

### Data Viewers

Foxglove、MCAP、Rerun 等能帮助看数据，但看数据不等于发布治理、SLA 复盘、质保证据和训练回流。

### Cloud Robotics

云很重要，但 “no cloud in the safety loop”。EdgeFleet 可以请求、授权、审计、暂停和回滚；本体 safety controller、E-stop、STO、scanner、speed/zone limits 和现场风险评估不能被云端替代。

## 03 · Solution

EdgeFleet = `Robot Progressive Delivery + Fleet Evidence Backbone + Remote Assist Boundary + Incident-to-Training Loop`。

它站在 DragonWorks、SkillCertKit、SkillDock 之后：

```text
TeleopStudio -> CloudTwin -> TrainRouter -> SkillCertKit -> SkillDock -> EdgeFleet
```

核心对象是 `release-correlated incident timeline`：

- release object：model、map、config、container、ROS package、QNN artifact、feature flag、rollback plan。
- rollout ring：simulator/lab -> internal robot -> friendly site -> one robot -> one hardware cohort -> one site -> fleet。
- readiness gate：self-test、localization confidence、perception health、watchdog、E-stop、battery、network、mission queue、operator coverage。
- health gate：mission success、intervention、stuck events、near miss、latency、thermal、battery drain、DDS/QoS miss、operator tickets。
- rollback mode：disable flag、pin previous artifact、revert config/map/model、drain mission queue、return to dock、pause autonomy。

EdgeFleet 不自动判定法律责任；它保全事实、支持 root-cause review、SLA、质保、客户复盘和训练改进。

## 04 · Why Now

四个趋势让 EdgeFleet 现在值得做：

1. **RaaS 改变了风险承担者**：客户买 uptime，RaaS/OEM/SI 承担故障、SLA、truck roll、质保和续费风险。
2. **机器人队列规模已足够大**：IFR 2025 显示工业机器人年新增约 542,000 台，专业服务机器人接近 200,000 台，物流机器人是最大服务机器人类别，RaaS fleet 增长 31%。
3. **Robot SRE 模式开始可迁移**：Kubernetes rollout、AWS/Azure IoT staged deployment、LaunchDarkly guarded rollout、SRE canary/postmortem 都能转译成 robot-native release discipline。
4. **Qualcomm edge evidence 已经可采集**：AI Hub/QNN、Dragonwing/RB3/QCS/IQ devices、camera/sensor health、thermal/power telemetry、QNN backend/fallback 让 field evidence 不再只是日志。

机会不是“再做一个机器人看板”，而是帮机器人运营商把 uptime 变成可管理、可证明、可计费的能力。

## 05 · Product

### 5.1 EdgeFleet Agent

运行在机器人或站点边缘节点上，作为旁路 evidence agent：

- 不替代 autonomy stack。
- 不绕过本体 safety controller。
- 不把云放进 safety loop。
- 采集 ROS 2/MCAP、OpenTelemetry、CloudEvents、QNN/runtime logs、thermal/power、camera health、operator session。
- 对 remote assist 执行 identity、TTL、zone、mode、speed、command allowlist 和 audit log。

### 5.2 Progressive Release

发布对象包含：

- model / checkpoint / QNN context hash。
- map / config / calibration。
- ROS/package/container versions。
- SkillDock digest。
- SkillCertKit policy decision。
- Dragonwing device profile。
- rollout rings。
- halt thresholds。
- rollback target。

### 5.3 Incident Capsule

触发条件：

- teleop takeover。
- E-stop / safe stop。
- planner no-path。
- DDS liveliness loss。
- perception confidence drop。
- p95 latency spike。
- camera stall/disconnect。
- thermal throttling。
- node restart。
- battery anomaly。
- customer abort。

输出 `incident_capsule`：MCAP、timeline、OTel traces/logs、CloudEvents、redaction report、hashes、retention policy 和 review annotations。

### 5.4 Replay Lab

把 incident capsule 变成训练和发布门禁：

1. 重放事故前后片段。
2. 对比 previous-known-good 与 candidate。
3. 生成 regression test。
4. 红线片段进入 TeleopStudio review。
5. 合规且已脱敏片段进入 TrainRouter。
6. 新版本通过 SkillCertKit 后再次 canary。

## 06 · Product API/Evidence

### Core APIs

```text
POST /v1/releases
POST /v1/rollouts
POST /v1/robots/{id}/preflight
POST /v1/capture-campaigns
POST /v1/incidents
GET  /v1/incidents/{id}/timeline
POST /v1/incidents/{id}/capsule
POST /v1/redaction/jobs
POST /v1/remote-assist/sessions
POST /v1/rollbacks
POST /v1/failure-mining/queries
POST /v1/teleopstudio/reviews
POST /v1/trainrouter/candidates
```

### Evidence Lanes

- **ROS 2 / MCAP**：robot sensor、topic、command、TF、diagnostics、selected perception output、redacted media。
- **OpenTelemetry / OTLP**：agent、upload service、teleop bridge、TrainRouter、CloudTwin replay workers 的 traces/logs/metrics。
- **CloudEvents**：incident lifecycle metadata and routing；不要把视频或敏感数据塞进 event context。

### Incident Capsule

```json
{
  "incident_id": "inc_20260706_0021",
  "robot_id": "rb3-amr-017",
  "site_id": "warehouse_sjc_03",
  "skill_id": "dock-assist-v2",
  "release_digest": "sha256:...",
  "ai_hub_job": "job_ref",
  "qnn_context_hash": "sha256:...",
  "trigger": "camera_stall_and_latency_spike",
  "window": "T-300s:T+120s",
  "artifacts": {
    "mcap": "evidence.mcap",
    "otel": "otel_trace.otlp",
    "timeline": "timeline.jsonl",
    "redaction": "redaction_report.json"
  },
  "rollback": {
    "target": "previous-known-good",
    "completed": true
  }
}
```

### Qualcomm Field Evidence

每次 rollout 绑定：

- AI Hub job ID。
- QNN context hash。
- model hash。
- runtime / SDK / QNN version。
- device profile。
- compute backend。
- CPU fallback flag。
- FPS / dropped frames。
- p50/p95/p99 latency。
- thermal zones。
- fan state。
- power mode。
- camera topology。
- rollout cohort。
- rollback proof。

## 07 · Market & Business Model

第一批买家不是“所有企业”，而是承担 SLA 风险的人：

- RaaS operator。
- Robot OEM。
- System integrator。
- Distributor / overseas service partner。
- Enterprise robotics ops。
- Hospital/logistics/cleaning/security fleet owner。

### Beachhead

最强 wedge：海外 RaaS operators / SIs 部署混合中国服务机器人到 hospitals、cleaning、security、warehouses。他们需要本地信任、SLA 报告、跨 OEM 可见性、远程诊断和质保证据。

### SKUs

- **Core**：per-robot monitoring、alerts、logs、OTA/version inventory、uptime reports。
- **Ops**：incident triage、remote diagnostics、runbooks、service tickets、SLA dashboards、customer reports。
- **Enterprise/Private**：SSO、audit、data residency、private cloud/on-prem、WMS/MES/HIS/CMMS/ServiceNow integrations。
- **Risk Ledger**：warranty、financing、insurance data、maintenance、utilization、residual-value evidence。

### Pricing

- Core：`$30-$100/robot/month` as telemetry wedge。
- Ops：`$200-$800/robot/month` depending on SLA and remote support。
- Enterprise/private：`$1k-$5k/site/month` plus integration。
- Critical infrastructure / hospital / manufacturing：`$500-$2k/robot/month` plus site fee。
- China version：`¥500-¥5,000/robot/month` depending on robot class and SLA；large sites `¥200k-¥3M/year`。
- OEM white-label：platform fee plus `¥50-¥300/robot/month` or revenue share。

Metric to sell: downtime minutes avoided、MTTR、truck rolls avoided、SLA credits prevented、field visits reduced、warranty claims resolved、fleet gross margin lift。

## 08 · Competition & Moat

EdgeFleet 不替代已有工具；它把 release evidence 和 field incident memory 做成系统记录。

Competition map：

- **Viam**：fleet management、registry、modules、ML rollout、OTA；EdgeFleet 强调 robot-native canary/rollback evidence and Qualcomm lineage。
- **Formant**：telemetry、timeline、teleop、incident；EdgeFleet 强调 release governance and training feedback。
- **Foxglove**：MCAP、data、search、visualization；EdgeFleet 将数据变成 release-correlated incident capsules。
- **InOrbit**：multi-vendor RobOps、missions、orchestration；EdgeFleet 强调 model/QNN artifact lineage。
- **Open-RMF / MassRobotics / VDA 5050**：interop protocols，不是发布治理系统；EdgeFleet 应兼容。
- **OEM clouds**：品牌内体验强；EdgeFleet 坐在多 OEM、多站点、多技能证据层。

### Moat

短期壁垒：

- release evidence schema。
- EdgeFleet Agent。
- incident capsule format。
- Dragonwing profile telemetry。
- SkillDock / SkillCertKit integration。

中期壁垒：

- connector compound：WMS/MES/CMMS/ERP、ROS 2、Open-RMF、VDA 5050、MassRobotics、OEM API、charger/door/elevator。
- support workflows：ServiceNow/Jira、customer portals、runbooks、field technician records。
- redaction and retention policies by region/customer。

长期壁垒：

```text
release x robot profile x site x mission x incident x rollback x training candidate x next release
```

每次失败、接管、热降频、QoS miss、相机故障、rollback 和客户复盘都会变成下一版门禁规则。

## 09 · Why Qualcomm

EdgeFleet 让 Qualcomm 不只是边缘推理芯片，而是机器人队列运营的默认证据底座。

Qualcomm 价值：

- 把 `AI Hub job ID -> QNN context hash -> runtime -> device profile -> rollout cohort` 绑定成现场证据。
- 证明 field device 实际用了预期 QNN/NPU backend，而不是悄悄 CPU fallback。
- 把 RB3/QCS/IQ 的 camera、thermal、power、fan、QNN runtime 和 sensor health 纳入上线门禁。
- 让 Robotics Hub sample 可以升级为 installable, monitored, rollbackable reference workflow。
- 帮 Qualcomm 从 “model benchmark” 进入 “production robot lifecycle”。

### Validation Sprint Ask

请求 Qualcomm 支持 6-8 周：

- 2-3 个 target：RB3 Gen 2/QCS6490，加 IQ-8275 或 IQ-9075 级设备。
- 1 条 AI Hub model path：compile/profile/inference job ID、downloadable artifact、sample data。
- telemetry hooks：QNN/runtime logs、thermal/power state、V4L2/GStreamer stats、device inventory。
- acceptance gates：max p95 latency、min FPS、max dropped frames、thermal threshold、allowed backend/runtime。
- 三个场景：clean rollout、bad model/perf regression、camera or thermal fault。
- 交付：signed evidence bundle with artifact manifest、rollout timeline、device profiles、inference samples、telemetry、rollback proof。

### Demo Metrics

- 100% artifact traceability。
- 1 -> 10% -> 50% -> 100% canary ladder。
- 30-minute sustained inference: FPS、dropped frames、p95 latency、backend、temperature、fan、power mode。
- camera fault detected within 5 seconds。
- mismatched artifact/runtime flagged not promotable。
- rollback proof with before/after evidence packet。

## 10 · Demo & Ask

### 3-Minute Demo

1. **0:00-0:25**：注册三台机器人：stable、canary、offline-cache。
2. **0:25-0:55**：上传 `dock-assist-v2`，展示 LeRobot dataset、SkillDock digest、QNN context hash、SBOM、Dragonwing profile。
3. **0:55-1:25**：preflight gate 检查 battery、task idle、camera health、safety boundary、QNN backend。
4. **1:25-1:55**：canary 激活，制造 latency spike 或 camera stall，EdgeFleet 自动 halt rollout。
5. **1:55-2:25**：生成 incident capsule：MCAP、OTel、CloudEvents、redacted video、operator audit、model/artifact digest。
6. **2:25-2:45**：rollback 到 previous-known-good，显示 rollout timeline 和 evidence packet。
7. **2:45-3:00**：失败片段进入 TeleopStudio review 和 TrainRouter candidate queue。

### Ask

主办方和 Qualcomm 给我们 RB3/QCS/IQ target、AI Hub/QNN artifact review、telemetry hook 指导和 reference workflow；我们交付一个可复用样例：从 SkillDock 发布到 EdgeFleet canary、incident capsule、rollback proof 和 LeRobot/TrainRouter failure feedback。

## Claim Boundaries

可以声称：

- Robot progressive delivery and evidence control plane。
- Incident-ready、audit-ready、rollback-ready fleet evidence。
- Supports release governance, RCA, SLA review, warranty review, and training feedback。
- Integrates with ROS 2、MCAP、OpenTelemetry、CloudEvents、AI Hub/QNN、SkillDock、SkillCertKit。
- Supports China-local and global deployment architectures。

不能声称：

- EdgeFleet makes robots safe/compliant/certified。
- zero downtime。
- rollback removes physical-world risk。
- cloud is in the safety loop。
- replaces OEM fleet manager, AI Hub, QNN, FoundriesFactory, OTA, or MDM。
- universal fleet management for all robots out of box。
- OpenTelemetry gives physical root cause。
- MCAP makes data private/compliant。
- redaction equals anonymization。
- guaranteed latency, power savings, safety certification, regulatory compliance, or insurance savings。

## Sources

- IFR industrial robot demand：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Viam fleet management：https://www.viam.com/platform/fleet-management
- Viam versions：https://docs.viam.com/fleet/manage-versions/
- Formant fleet observability：https://docs.formant.io/docs/fleet-observability
- Formant incident management：https://docs.formant.io/docs/incident-management
- InOrbit operations：https://www.inorbit.ai/operations
- Foxglove data：https://docs.foxglove.dev/docs/data
- Open-RMF：https://www.open-rmf.org/
- AWS IoT Jobs：https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations-details.html
- AWS Greengrass deployments：https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html
- Azure IoT Device Update：https://learn.microsoft.com/en-us/azure/iot-hub-device-update/device-update-deployments
- Kubernetes deployments：https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- LaunchDarkly progressive rollouts：https://launchdarkly.com/docs/home/releases/progressive-rollouts
- SRE canarying releases：https://sre.google/workbook/canarying-releases/
- MCAP spec：https://mcap.dev/spec
- MCAP ROS 2 guide：https://mcap.dev/guides/getting-started/ros-2
- ROS 2 tracing：https://github.com/ros2/ros2_tracing
- OpenTelemetry traces：https://opentelemetry.io/docs/concepts/signals/traces/
- OpenTelemetry Collector：https://opentelemetry.io/docs/collector/
- CloudEvents spec：https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md
- NIST Privacy Framework：https://www.nist.gov/privacy-framework
- NIST Zero Trust SP 800-207：https://csrc.nist.gov/pubs/sp/800/207/final
- NIST SP 800-82 Rev. 3：https://csrc.nist.gov/pubs/sp/800/82/r3/final
- EU Machinery Regulation：https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng
- EU AI Act：https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- EU Cyber Resilience Act：https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EU Product Liability Directive：https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L2853
- Qualcomm AI Hub：https://aihub.qualcomm.com/get-started
- Qualcomm AI Hub compile docs：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- Qualcomm AI Hub profile docs：https://workbench.aihub.qualcomm.com/docs/hub/profile_examples.html
- RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm Foundries workflow：https://www.qualcomm.com/developer/blog/2025/01/unifying-workflow-of-embedded-devices-foundries-factory
