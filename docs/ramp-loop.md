# RampLoop 机坪异常闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

RampLoop 帮航空公司、机场和地服团队把机坪周转里的小异常在变成离港延误前闭环：

> FOD、GSE 迟到、行李/配餐/清洁阻塞、安全区占用和 SLA 争议，都变成有人负责、有倒计时、有升级、有证据的关闭记录。

它不是另一个机场大屏，也不是自动拖车公司。它做的是从 observation 到 case，到 assignment，到 verified closure，到 evidence，再到 LeRobot HIL 的机坪异常闭环层。

## Problem

航班延误通常不是突然发生的，而是从一个个没人真正关掉的异常开始。

- 加油窗口错过。
- 行李装卸没到位。
- 清洁队还在上一架飞机。
- 客梯车或廊桥没准备好。
- 配餐晚到。
- FOD 没清。
- 舱单信息卡住。
- GSE 停错位置或找不到。

机坪主管的痛点不是没有更多数据，而是高峰波次里每个人都知道一点情况，但没人拥有完整闭环。最后延误发生时，团队开始补截图、追电话、争 delay code。航司损失准点率，地服损失 SLA 信任，机场损失机位效率。

## Why Now

航班量继续增长，但机位、人手和周转时间没有同步变宽。

- ACI 预测 2026 年全球机场旅客量约 102 亿人次，2045 年约 188 亿，并指出机场基础设施、飞机交付、供应链、地缘政治和可持续性都是约束。
- IATA 2026 年航空运输 outlook 显示航司利润率承压，买方必须卖硬节省，而不是创新概念。
- A4A 估算 2024 年美国客运航司直接 aircraft block time 成本约 100.76 美元/分钟。
- SITA 2025 报告显示机场 IT 预算开放，机场在 AI、跨系统数据流和共享上继续投资。
- SITA baggage benchmark 显示错运行李仍是数十亿美元级成本池。
- 中国 2025 年运输机场旅客吞吐量约 15.29 亿人次，货邮吞吐量约 2186 万吨，运输机场 270 个。
- 中国运输机场运行安全管理新规 2026-07-01 生效，强化 SMS、FOD、机坪全链条检查、车辆设备管理、运行指挥和记录。

## Insight

机坪的关键产品单位不是“检测到一个事件”，而是：

> 把一个会拖延离港的异常关掉。

机场已经有 AODB、A-CDM、OCC、地服排班、CCTV、无线电、微信群和人工经验。缺的是一个跨航司、机场、地服、GSE、货站和 AOCC/APOC 的异常闭环层：

- 谁现在必须做什么？
- 最晚什么时候完成？
- 没完成谁接手？
- 完成证据是什么？
- 这次异常是否真的影响 TOBT / TSAT / off-block？

## Solution

RampLoop 是离港倒计时下的机坪异常闭环层。

核心结果：

- 对航司：减少可控延误分钟，提升 D0/D15 和站点准点表现。
- 对地服：减少 SLA 争议、罚款、复盘时间和跨班组扯皮。
- 对机场/AOCC：提升机位利用率、租户问责、SMS 证据和机坪安全闭环。
- 对 GSE / cargo：把设备、人员、货站和服务节点绑定到具体航班风险。

## Product Workflow

1. Build Turn：导入航班、机位、机型、SOBT/EOBT、TOBT、航司 SOP、地服 SLA、关键节点和责任团队。
2. Watch：站位摄像头、GSE 位置、BHS/RFID、扫码、人工 App 和现有系统共同更新机坪状态。
3. Create Observation：固定摄像头、机器人/仿真巡检、GSE telematics、人工 App 产生 observations。
4. Compile Case：规则引擎把 observations 变成 FOD、GSE out-of-zone、baggage blocker、service blocker、safety exception、milestone risk。
5. Assign Owner：每个 case 有 owner、倒计时、下一步动作、升级路径和关闭条件。
6. Escalate：未按时关闭就升级给班组长、地服主管、航司站长、OCC 或 AOCC/APOC。
7. Verify Closure：before/after clip、连续帧、GSE 状态、照片、人工审批和 hash 证据满足条件后进入 verified_closed。
8. Review：航班推出后输出异常账本：哪些提前关掉，哪些拖成延误，哪个流程反复卡住。
9. Learn：低置信度、误报、人工纠错、机器人接管和最终延误结果进入 LeRobot HIL。

## Market Wedge

先切：

> 一个航司站点 + 一个核心地服供应商 + 5-15 个高频窄体机位。

不要先卖全机场操作系统。先在一个延误敏感站点、一个高峰波次、6-10 类高频异常里证明：

- open exceptions 更少。
- 异常关闭更快。
- SLA 复盘更可信。
- 可控延误分钟下降。

第一批 use cases：

- Chocks / cones。
- Belt loader / GPU / PCA。
- Fuel / catering / cabin clean。
- Baggage/cargo load complete。
- Boarding start。
- FOD / safety-zone violation。
- GSE proximity / unattended equipment。

中国版本：

- 面向千万级枢纽机场、机场集团、主基地航司和地服保障公司。
- 关键词：安全底线、全链条责任、数智化、绿色化、高质量运行。
- 覆盖 FOD 发现-处置-溯源-整改-报表闭环。
- 支持机坪保障一张图、车辆/设备/人员/任务节点自动取证。
- 接入 A-CDM / AOC / BHS / 货运 / 视频 / IoT 系统。
- eGSE、共享调度、设备利用率、电量/充电排班、异常占位预警可作为扩展模块。

## Business Model

收入模型：

> paid pilot + station SaaS + hub/AOCC tier + vision/GSE modules + optional success fee

建议包装：

| Product | Pricing Model | ACV |
|---|---:|---:|
| 10-12 周试点 | 5-15 gates/stands, 6-10 exception types | $50k-$150k |
| Core Exception Closure SaaS | Per station, by departures / gates | $75k-$250k / station / year |
| Hub / AOCC tier | Multi-tenant airport operating layer | $300k-$1.2M / airport / year |
| Airline enterprise | Multi-station rollout | $1M-$5M / year |
| Computer vision stand pack | Existing cameras | $1k-$3k / stand / month |
| New camera / edge kit | One-time hardware / install | $5k-$20k / stand |
| GSE module | Powered asset or integration fee | $10-$35 / asset / month |
| Cargo module | Cargo station / ramp zone | $75k-$300k / year |

ROI formula：

```text
Annual savings =
turns per year
* minutes saved per turn
* delay cost per minute
* attribution factor
```

Example：

100 daily departures = 36,500 turns/year。

Saving 1.0 minute per turn at $100.76/min direct airline operating cost equals $3.68M gross annual value。

At only 15% attribution to RampLoop, value is about $552k/year, enough to support $150k-$300k ACV。

Additional ROI pools：

- Ground damage: IATA says GSE operations account for up to 40% of aircraft ground damage; annual ground-damage cost could approach $10B by 2035 without action.
- Baggage: SITA pegs mishandled baggage at $260 per bag and $6.3B industry cost.
- GSE: better utilization and fewer missing-asset delays can defer equipment capex.
- SMS / audit: closure logs become evidence for airport SMS, airline SLA reviews and tenant meetings.

## Go-To-Market

YC-style land motion：

1. Founder team visits station and shadows a peak bank.
2. Run a 30-day delay autopsy：split each delay into unresolved exceptions.
3. Show station manager and ground-handler GM where time, trust and evidence are lost.
4. Sell a 10-12 week paid pilot.
5. Convert to station SaaS when RampLoop proves exception closure and hard-dollar benefit.

Pilot scope：

- 5-15 gates/stands or one cargo ramp zone.
- Flight schedule / AODB or airline ops feed.
- Camera or manual-mobile evidence.
- Handler roster/task feed if available.
- GSE telematics if available.
- 6-10 exception types.
- Weekly ops review with airline station, handler, airport observer.

Success criteria：

- Alert latency < 60-90 seconds.
- 85%+ precision on selected exceptions.
- 70%+ of exceptions assigned and closed in RampLoop.
- 1-2 avoidable minutes saved per turn, or 10-20% reduction in late critical tasks.
- At least one hard-dollar proof point：delay minutes, SLA penalty avoided, fewer baggage/cargo misses, or safety-risk reduction.

Expansion：

1. One airline station, 5-15 gates.
2. Handler SLA module and more exception types.
3. Multi-station airline rollout.
4. Airport AOCC/APOC shared operating picture.
5. GSE and cargo modules.
6. Airport-wide ramp exception network.

## Competition

RampLoop 不替代已有系统：

- Assaia / Deep Turnaround：AI turnaround visibility 强；RampLoop 强调 case ownership、verified closure、SLA evidence 和 HIL。
- SITA / Amadeus / INFORM：AODB、A-CDM、资源管理强；RampLoop 把现场 blocker feed 回这些系统。
- Veovo / AeroCloud：机场运营系统强；RampLoop 是站位级 exception accountability layer。
- Targa / Undagrid / TCR：GSE telematics 强；RampLoop 把设备状态绑定到具体航班、SLA 和离港风险。
- QinetiQ / Xsight / iFerret / ADB SAFEGATE AiPRON FOD：偏检测；RampLoop 负责处置和证据。
- Aurrigo / autonomous GSE：自动 GSE 是执行层；RampLoop 先做 assistive automation，再逐步接入自动设备。

## Moat

壁垒不是模型，而是站点级运营记忆和跨组织信任。

会积累的资产：

- Exception graph：航班、机位、GSE、人员、服务节点、SLA、TOBT、延误原因和责任方。
- Closure dataset：谁接、怎么关、几分钟关、是否复发、是否恢复离港表现。
- Airport connectors：AODB/AIDX、A-CDM、BHS/RFID、GSE telematics、地服 App、SLA 和 AOCC/APOC 接口。
- Evidence vault：before/after clip、模型版本、人工审批、SHA-256 hash chain、WORM 存证和审计包。
- Station playbook：航司、机型、地服合同、机位和高峰波次的异常分类、升级规则和关闭证据。

## Architecture

Production principle：RampLoop 不接管飞机或 GSE 控制。它接收感知和状态，生成 case，由人或既有系统执行，RampLoop 负责监督、验证、存证和学习。

```text
Edge cameras + sim robot/drone
  -> Qualcomm edge perception nodes
  -> event broker + stand digital twin
  -> case compiler + rules engine
  -> human approval / assignment workflow
  -> verification engine
  -> AODB / A-CDM / turnaround APIs
  -> WORM evidence vault + LeRobot learning loop
```

Case object：

```json
{
  "case_type": "FOD | GSE_OUT_OF_ZONE | BAGGAGE_BLOCKER | SERVICE_BLOCKER | SAFETY_EXCEPTION | MILESTONE_RISK",
  "flight_leg_id": "AIDX/AODB flight key",
  "stand_id": "B12",
  "zone": "pushback-envelope | cargo-side | taxi-lane | service-road",
  "severity": "critical | major | minor",
  "confidence": 0.94,
  "assignee_role": "ramp_lead | baggage_lead | fod_sweeper | airline_ops",
  "status": "needs_approval | assigned | in_progress | pending_verification | verified_closed | rejected",
  "evidence": ["clip_uri", "frame_hash", "model_version", "camera_calibration_id"]
}
```

### Edge Perception

- RB3/RB5 stand nodes.
- 2-3 camera views：gate-line, aircraft service side, baggage belt / cargo-door side。
- Detect/track FOD, belt loader, tug, GPU, fuel truck, catering, stairs, cones/chocks, baggage blockers, safety-zone violations.

### Airport Integration

- AODB/AIDX inbound data：flight, stand, aircraft type, SOBT/EOBT, linked inbound, handler, TOBT owner, task schedule。
- A-CDM milestone logic：TOBT risk, Aircraft Ready check, TSAT/TTOT context。
- Update turnaround system or A-CDM adapter with case status, not raw detections.

### Evidence

For every case:

- 10-20 sec before/after clips.
- Annotated frames.
- Model version / threshold / camera pose / stand polygon version.
- Human approval trail.
- SHA-256 hash chain.
- WORM/Object Lock evidence bundle.

### LeRobot HIL

- Competition version uses tabletop or Gazebo/PX4/Three.js sim.
- Robot/drone sim streams frames into same perception and case APIs.
- Human operator uses gamepad/keyboard interventions.
- Save intervention episodes as LeRobotDataset: synchronized video plus state/action data.
- Train HIL policy to inspect a stand, approach FOD, frame evidence and return.

## Competition Demo

3 分钟 demo：

1. AODB mock loads flight on stand B12 with TOBT, TSAT, service tasks and live edge camera tiles.
2. Camera detects FOD near nose gear and baggage cart blocking cargo-side belt-loader access.
3. RampLoop creates two cases with severity, assignee, evidence clip and map zone.
4. Ramp lead approves. FOD case assigned to sweeper/robot; baggage blocker assigned to baggage lead.
5. A TOBT-risk banner appears, but no A-CDM update is sent yet.
6. Simulated robot/drone launches in supervised LeRobot HIL mode, navigates to FOD zone, captures close-up evidence and waits for human confirmation.
7. FOD removed and baggage cart moved. Edge cameras verify clean zone and unblocked cargo path.
8. Cases move to `pending_verification`, then `verified_closed`.
9. WORM evidence bundle shows hash, model version, approver, assignee, before/after frames.
10. A-CDM / turnaround adapter marks blockers cleared and aircraft-ready checks passing.

## Safety / Risk Controls

- Human approval required before assignment, dispatch or milestone update.
- Robots operate in shadow/supervised mode unless an airport-approved safety case exists.
- Geofenced no-go zones around aircraft, engines, taxi lanes, fueling and pushback path.
- Speed limits, e-stop, loss-of-comms stop, heartbeat and manual takeover.
- No live drone airside demo without airport and ATC/airspace authorization.
- Use ISO 3691-4 and ANSI/RIA R15.08 as mobile robot safety reference.
- Align operational categories with IATA IGOM/AHM: baggage, servicing, ramp safety, loading/unloading and GSE usage.

## Why Qualcomm

RampLoop 是 Qualcomm 机场 edge AI 样板：

- 机场不能把每路机坪视频、人员位置、航班节点和安全事件都送到公网云再等推理。
- 异常提醒需要低延迟和弱网可用。
- 多相机、GSE 信号和机器人状态适合 edge fusion。
- AI Hub、Neural Processing SDK、QNN/QAIRT 可以展示模型到设备 profile、签名、部署和回滚链路。
- 商业上连接机场、航司、地服、自动 GSE、智能摄像头、航空物流和交通基础设施 design partner。

## Ask

比赛阶段：

- RB3 Gen 2 / RB5 / Dragonwing dev kit。
- 广角摄像头、可选深度摄像头、小型 AMR 或桌面机械臂。
- 打印机位图、玩具飞机、GSE token、FOD token、轮挡/锥桶、MQTT mock。
- 匿名过站节点、延误原因、GSE/BHS/SLA 异常、站位 SOP 和 30 天 delay autopsy 样例。
- AI Hub / QNN profile 支持。

赛后 18 个月目标：

- Pre-seed $1.5M。
- 3 个付费试点。
- 10 个站点部署。
- 可复用 station playbook。

对 Qualcomm 的具体 ask：

- 参与 $500k-$750k。
- 提供 edge AI reference support。
- 引荐 1-2 个航空/交通基础设施 design partner。

## Claims To Avoid

- 不说消除航班延误。
- 不说 FAA/EASA/CAAC 认证。
- 不说可安全用于真实机坪无人值守。
- 不控制真实飞机或 GSE。
- 不承诺杜绝所有 FOD、延误或事故。
- 不说无需集成。
- 不说 AI 自动管理机坪。
- 不说替代 AODB/OCC/地服系统。
- 不引用未实测的 NPU FPS。
- 不说 LeRobot tabletop policy 可以直接泛化到机场。

## Sources

- ACI traffic forecast：https://aci.aero/2026/01/28/aci-world-releases-global-airport-traffic-forecasts-as-long-term-demand-growth-continues-to-reshape-aviation/
- IATA 2026 outlook：https://www.iata.org/en/iata-repository/publications/economic-reports/global-outlook-for-air-transport-june-2026/
- SITA Airport IT Insights：https://www.sita.aero/resources/surveys-reports/air-transport-it-insights-2025/airports/
- A4A delay costs：https://www.airlines.org/dataset/u-s-passenger-carrier-delay-costs/
- SITA Baggage IT Insights：https://www.sita.aero/resources/surveys-reports/sita-baggage-it-insights-2025/
- IATA Enhanced GSE：https://www.iata.org/en/programs/ops-infra/ground-operations/ground-support-equipment/enhanced-gse-recognition-program/
- CAAC 2025 bulletin：https://www.caac.gov.cn/XWZX/MHYW/202604/t20260417_230603.html
- China airport safety rule：https://xxgk.mot.gov.cn/gz/202511/t20251127_4180546.html
- Assaia turnaround report：https://www.assaia.com/turnaround-report-2025
- Assaia Alaska case：https://www.assaia.com/customer-stories/assaia-helps-alaska-airlines-increase-on-time-performance-by-17-at-sea
- IATA AIDX：https://www.iata.org/en/publications/info-data-exchange/
- EUROCONTROL A-CDM：https://www.eurocontrol.int/concept/airport-collaborative-decision-making
- S3 Object Lock：https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB5：https://www.qualcomm.com/developer/hardware/robotics-rb5-development-kit
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- LeRobot HIL-SERL：https://huggingface.co/docs/lerobot/en/hilserl
