# RampLoop 机坪异常闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

RampLoop 是给航空公司、机场和地面代理的机坪异常闭环系统：

> 用 Qualcomm 边缘视觉、GSE 信号、机器人/人工任务和 LeRobot HIL，把皮带车晚到、行李转运风险、FOD、安全区占用、加油/配餐阻塞和 SLA 争议变成有责任人、有倒计时、有证据的关闭记录。

它不是另一个机场大屏，也不是自动拖车公司。它做的是从 detect 到 assign 到 close 到 evidence 的 live exception closure。

## Problem

航班不是被一个大故障延误，而是被几十个小异常拖到起飞后才算账。

- 过站节点多：廊桥、轮挡、锥桶、卸行李、加油、清洁、配餐、登机、装载、推出、安全检查。
- 多方协作：航司、机场、地服、油料、配餐、清洁、货站和监管各有局部视角。
- 异常处理依赖对讲机、群聊、人工巡场和事后时间戳。
- 看见了不等于有人接，接了不等于关掉，关掉了不等于能举证。

## Why Now

四个信号同时出现：

- 客流回升和机位紧张。ACI 预计 2026 年全球机场旅客量约 102 亿人次。
- 每分钟延误很贵。A4A 估算 2024 年美国客运航司直接飞机运营成本约 100.76 美元/区块分钟。
- 行李错运仍然昂贵。SITA 报告 2025 年全球约 2400 万件行李错运，平均成本约 260 美元/件。
- 机场正在采购 AI 和自动化。Changi、dnata、Narita/JAL、DXB/Emirates、YVR、Ezeiza、Swissport/Aurrigo 等信号说明机坪视觉、自动 GSE、智能转场正在从试点走向部署。
- 中国政策直接支持。CAAC “AI + 民航”方向强调保障节点状态感知、站坪车辆协同调度、无人巡检、行李关键节点识别、全流程监控和异常自动提醒。

## Insight

机坪的最小经营单元不是“一个航班”，而是一个有倒计时的异常。

RampLoop 的判断：

> 机场和航司不会先为“全自动机坪”买单，但会为可控延误分钟减少、行李错运下降、GSE/FOD 风险关闭、SLA 争议变少和 TOBT 更准付费。

## Solution

RampLoop 是过站异常的关闭操作系统。

1. 导入航班、机位、STD/ETD、TOBT、服务清单、SLA、站位规则和责任方。
2. 用站位摄像头、FOD 摄像头、GSE GPS/UWB/BLE、扫码、BHS/RFID、AODB/A-CDM 和人工 App 形成实时状态。
3. 边缘模型识别轮挡、锥桶、皮带车、行李车、FOD、安全区、人员和关键服务节点。
4. 异常按航班倒计时、SLA、责任方、严重度和站位规则自动派给地服主管、TOC、机场运控或机器人队列。
5. 人工/机器人完成动作后，用连续帧、GSE 信号、扫码、照片和主管审批生成关闭证据。
6. 低置信度、人工纠错、机器人接管和实际延误结果进入 LeRobot HIL。
7. 中国站点在国内云/私有云训练，海外站点在海外云训练；模型经 AI Hub / QNN / QAIRT 回到 edge。

## Product Workflow

状态对象：

- `turnaround_id`
- `stand_id`
- `phase`
- `observation`
- `gse_signal`
- `exception`
- `closure_action`
- `evidence_packet`

工作流：

1. Import schedule and service checklist。
2. Sense ramp state。
3. Detect exception。
4. Assign owner。
5. Propose action。
6. Human approves。
7. Robot/human closes。
8. Verify acceptance criteria。
9. Export evidence packet。
10. Feed HIL dataset。

## Market Wedge

第一批场景：

- Turn-critical tasks：廊桥、轮挡、锥桶、皮带车、清洁、加油、配餐、登机、推出。
- Baggage/load：中转行李风险、晚到行李、ULD/装载差错、装卸节点缺证、BHS/RFID 异常。
- GSE/FOD：设备未到、错误停放、等待时间、FOD、安全区未清空、近距离风险事件。
- Cargo hubs：跨境电商、货站、冷链 ULD、查验滞留、单证不一致、车辆协同。
- China airports：浦东、广州、深圳、首都/大兴、鄂州花湖、郑州、成都、杭州、重庆。
- Ground handlers：SLA、人员调度、车辆利用率和事故证据可以变成可续费服务。

## Business Model

收入模型：

> 90-day paid pilot + stand/station subscription + edge node + success fee

建议价格：

- 90 天试点：4.5 万美元/站点起，覆盖一个航司或地服团队、最多约 3000 个 turn、三类异常工作流。
- 附加参与方：每增加一个航司/地服/独立航站区，加 1.5 万美元。
- 正式订阅：按 active stand、航班量、参与方和异常模块收费。
- 成功分成：可选收取经验证硬节省的 12%，试点封顶。

硬节省公式：

`Savings = avoided controllable delay minutes * $100.76 + avoided mishandled bags * $260 + avoided SLA penalties + documented ground damage/FOD cost avoided + avoided exception labor hours * loaded labor rate`

90 天试点 KPI：

- 可控延误分钟 / 100 turns 下降 8-12%，或至少 0.5 min/turn。
- D0 提升 2-4 点，D15 提升 1-2 点。
- TOBT +/-5 分钟准确率提升 10 点。
- 90%+ 关键异常 2 分钟内分配责任人。
- 异常关闭时间下降 20%。
- 95%+ SLA 影响异常有证据包。

## Competition

RampLoop 不替代已有系统：

- Assaia / Deep Turnaround / Synaptic Aviation：视觉转场和事件识别强；RampLoop 负责责任分配、动作、关闭证据和训练数据。
- INFORM / AODB / A-CDM：计划和协同强；RampLoop 处理现场异常到 TOBT/TSAT/TTOT 的实时风险。
- Aurrigo / TractEasy / EasyMile / AeroVect / autonomous GSE：执行硬件强；RampLoop 做跨品牌异常派发、闭环审计和人机协同。
- Samsara / fleet telematics：车辆与安全数据强；RampLoop 绑定到航班过站和离港结果。

## Moat

壁垒不是一张机坪照片，而是：

> exception graph + closure dataset + airport connectors + regional edge deployment profile

会积累的资产：

- 航班、机位、GSE、人员、服务节点、SLA、TOBT 和延误原因的 exception graph。
- 谁接、怎么关、几分钟关、是否复发、是否恢复离港表现的 closure dataset。
- AODB、A-CDM、BHS/RFID、GSE telematics、地服 App、SLA 和运控系统接口。
- 中国本地化/私有云、海外云、数据最小化、弱网缓存和 Qualcomm edge profile。

## Architecture

### Edge Sensors

- Stand camera。
- Optional FOD camera。
- Optional depth camera for tabletop。
- GSE telematics: GPS / UWB / BLE / MQTT / CAN where available。
- BHS/RFID baggage node status。
- QR scan and supervisor app。
- AODB / A-CDM / flight schedule。

### Edge Runtime

- RB3 Gen 2 / QCS6490 / Dragonwing。
- QNN/QAIRT perception inference。
- Object tracking and apron world model。
- Turnaround finite-state machine。
- Safety supervisor。
- Closure orchestrator。
- Evidence store。

### LeRobot HIL

- Policy-driven robot/AMR action only in supervised demo。
- Human takeover and recovery segments recorded。
- Corrections and low-confidence frames become episodes。
- Dataset trains next detector/action policy。

### Deployment

- China: local cloud or on-prem, no default cross-border transfer。
- Overseas: overseas cloud lane。
- Export only compliant model artifacts, metrics and anonymized examples。

## Competition Demo

3 分钟 demo：

1. Tabletop ramp: printed stand map, toy aircraft, tagged GSE, cone/chock tokens, FOD token, small mobile robot or desktop arm。
2. Dashboard loads expected sequence: chocks placed, cones placed, belt loader approaches, FOD clear。
3. Camera sees normal tasks and simulated MQTT confirms GSE status; RampLoop auto-closes normal steps。
4. Place FOD in engine exclusion zone or move belt loader before chocks; Qualcomm edge flags exception。
5. Supervisor approves robot/human task。
6. Robot begins response; operator performs HIL correction if it drifts。
7. Camera verifies area clear for three consecutive frames and GSE state valid。
8. System exports evidence packet with exception owner, closure time, snapshots, model version and HIL episode ID。

## Why Qualcomm

RampLoop 是 Qualcomm 机场 edge AI 样板：

- 机坪视频、人员位置、航班节点和安全事件不能默认上公网云。
- 异常提醒需要低延迟和弱网可用。
- 多相机、GSE 信号和机器人状态适合 edge fusion。
- AI Hub / QNN / QAIRT 可以展示从模型到设备 profile 到部署回滚的链路。
- 商业上连接机场、航司、地服、自动 GSE、智能摄像头和民航物流生态。

## Ask

比赛阶段需要：

- RB3 Gen 2 / RB6 / Dragonwing dev kit。
- 广角摄像头、可选深度摄像头、小型 AMR 或桌面机械臂。
- 打印机位图、玩具飞机、GSE token、FOD token、轮挡/锥桶、MQTT 模拟状态。
- 一组匿名过站节点、延误原因、行李/GSE/SLA 异常样例和站位 SOP。
- AI Hub / QNN profile 支持。

## Claims To Avoid

- 不声称 FAA/EASA/CAAC 认证。
- 不声称可安全用于真实机坪无人值守。
- 不控制真实飞机或 GSE。
- 不承诺杜绝所有延误、FOD 或事故。
- 不引用未实测的 NPU FPS。
- 不说 LeRobot tabletop policy 可以直接泛化到机场。

## Sources

- ACI traffic forecast：https://aci.aero/2026/01/28/aci-world-releases-global-airport-traffic-forecasts-as-long-term-demand-growth-continues-to-reshape-aviation/
- A4A delay costs：https://www.airlines.org/dataset/u-s-passenger-carrier-delay-costs/
- SITA Baggage IT Insights：https://www.sita.aero/about-us/pressroom/news-releases/tech-drove-down-mishandled-bag-rates-by-23-in-2025-but-mishandling-still-costs-the-industry-%246.3-billion-a-year
- IATA ground operations：https://www.iata.org/en/pressroom/2025-speeches/2025-05-13-01/
- Assaia Series B：https://www.assaia.com/resources/assaia-raises-26-6-million-in-series-b-funding-to-enhance-global-ai-leadership-in-airport-operations
- dnata autonomous GSE：https://www.dnata.com/media-centre/dnata-rolls-out-autonomous-vehicles-in-airport-operations/
- YVR Deep Turnaround：https://news.yvr.ca/yvr-launches-ai-powered-innovation-to-optimize-the-aircraft-turnaround-process/
- CAAC statistics：https://www.caac.gov.cn/XXGK/XXGK/TJSJ/
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/general_introduction.html
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
