# InfraLoop 设施巡检闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

InfraLoop 是关键设施的 AI 巡检闭环系统：

> 机器人发现问题，InfraLoop 让维修闭环。

它面向数据中心、变电站、工业园区、城市生命线和能源 O&M 团队，把机器人、无人机、固定摄像头和人工巡检看到的现场事实，变成可分级、可派单、可复检、可审计、可训练的维修闭环。

它不替代 Maximo / SAP / ServiceNow / 国产 CMMS，也不卖“另一台机器人”。它卖的是现场事实到 verified repair 的操作层。

## Problem

关键设施不是缺巡检，而是缺“异常被关闭”的闭环。

数据中心、工厂、医院、园区、泵站、管廊和变电站每天都有表单、照片、微信群、机器人后台和 CMMS 工单，但缺陷经常没有被准确识别、分级、派责、复检，最后变成停机、事故、合规风险和老技师脑子里的隐性知识。

具体痛点：

- 无人机、机器人和固定相机能拍到现场，但图片常常停在报告里，没有变成责任人和 SLA。
- Maximo、SAP、ServiceNow 和国产 CMMS 知道资产和工单，却不知道这次异常是否真的修好。
- 热漂移、异响、仪表异常、腐蚀和坏视角依赖老技师判断，新人和外包商很难继承。
- 保险、合规、客户 SLA 和事故复盘需要时间戳、位置、证据、处理动作和复检结果。
- “机器人检测到异常”不如“这个隐患已经带证据闭环”有商业价值。

## Why Now

AI 数据中心、电网投资、城市生命线和工业 edge AI 正在同一时间推高巡检价值。

关键变化：

- IEA 认为全球到 2040 年需要新增或替换约 8000 万公里电网，2030 年电网投资需超过每年 6000 亿美元。
- ABB 调研称典型工业企业非计划停机成本接近每小时 12.5 万美元。
- Energy Robotics 披露其机器人巡检已完成 100 万次以上，覆盖 5 大洲，并节省 32,000+ 小时危险人工劳动。
- Gecko Robotics 2025 年达到 12.5 亿美元估值，并在 2026 年获得美国海军 5 年 7100 万美元 IDIQ。
- ANYbotics 总融资已超过 1.5 亿美元，Qualcomm Ventures 投资 ANYbotics，说明工业巡检机器人是 Qualcomm 生态关注的真实市场。
- Skydio、Percepto、Voliro、Zeitview 等在无人机和基础设施巡检中继续融资、获批或扩张。
- 中国政策把巡检从 routine maintenance 推向 regulated safety governance：城市基础设施生命线、新城建/韧性城市、安全生产三年行动、工业互联网+危化安全、矿山机器人替人都强调实时监测、闭环处置和监管证据。

过去巡检是“拍照打勾”。现在买方要的是少停机、少派人进危险区域、少漏检、可追责、可审计、可复制的维修运营层。

## Core Insight

巡检真正的价值不在生成报告，而在把一个异常关闭。

AI 的切入点不是替代 CMMS，也不是造一台更贵的机器人，而是在现场把图像、传感器、SOP、资产历史和责任人连接起来：

> evidence -> risk score -> work order -> repair -> verification -> asset memory -> HIL improvement

买方付费买的是更快的异常确认、更明确的责任、更少的二次出车、更完整的修复证据和可复用的资产历史。

## Solution

InfraLoop 是硬件无关的关键设施异常闭环层。

产品模块：

1. **Asset Graph**：导入资产台账、SOP、巡检模板、平面图、历史工单、标准视角和风险等级。
2. **Edge Inspection**：接入 UGV、无人机、固定摄像头、手持设备和人工巡检；Qualcomm edge 现场识别热、视觉、仪表、声音、气体和路线异常。
3. **Anomaly Card**：输出资产 ID、位置、时间戳、模型版本、置信度、严重度、证据、人工复核按钮和建议动作。
4. **Work Order Bridge**：一键生成 Maximo / SAP / ServiceNow / 国产 CMMS 工单，并同步状态。
5. **Verified Repair**：维修后自动复检，形成 before/after、模型版本、责任人和审计包。
6. **Learning Loop**：误判、坏视角、堵路、teleop recovery 和人工纠正进入 LeRobotDataset，用于离线训练、shadow validation 和 canary OTA。

## Product Workflow

1. 导入 asset list、SOP、inspection template、地图、禁行区、慢行区、标准视角和历史工单。
2. 调度 UGV、无人机、固定相机或手机采集 RGB、热图、深度、声学、气体和仪表读数。
3. 端侧模型对比历史基线，生成 anomaly type、confidence、severity、evidence 和 review status。
4. 人工 reviewer 对低置信度或高风险事件进行确认。
5. 系统生成工单并写入 CMMS/EAM，附资产、位置、证据、建议动作和 SLA。
6. 技术员或承包商处理并记录维修动作。
7. 机器人或固定相机复检，结果回写 verified / reopened。
8. 误判、接管和失败片段导出为 LeRobot episode。
9. 区域云训练后导出 QNN/QAIRT artifact，经 shadow/canary 后回到 edge fleet。

## Market Wedge

先切 AI 数据中心和高可靠性园区的关键 MEP 设施：

- UPS。
- 电池柜。
- 发电机。
- 冷却系统。
- 配电柜。
- 消防。
- 泵房。
- 管廊节点。

原因：

- 停机代价高。
- 巡检频繁。
- 合规和客户 SLA 强。
- 技工短缺明显。
- 客户愿意为“少一次事故或停机”付费。
- 场景可控，适合安全 demo 和付费试点。

中国版：

- 目标：城市生命线、一网统管、工业互联网+危化安全、数据中心、园区变电站、管廊、桥隧、水务、矿山和能源设施。
- 竞合：不与宇树、云深处、优艾智合、大疆、亿嘉和、申昊、七腾等设备正面竞争，做统一异常闭环层。
- 强调：边缘推理、视频最小化、私有部署、国产云适配、敏感设施数据不默认出境、监管证据。

海外版：

- 目标：AI data centers、colocation、utilities、IPP、industrial facilities、BESS、utility contractors、facility O&M。
- 生态：Spot、ANYmal、Skydio、Percepto、Flyability、Voliro、Energy Robotics、IBM Maximo、SAP EAM、Bentley iTwin。
- 切入：一个站点、1-2 条高价值路线、100-300 个资产、可证明的 work-order loop。

## Business Model

InfraLoop 卖 inspection closed loop，不靠一次性硬件差价赚钱。

建议模型：

- **Paid Pilot**：海外 25k-75k 美元，6-10 周；中国 20万-80万元，选择 1-2 条路线和 100-300 个资产。
- **Software ARR**：60k-180k 美元 / site / year，按资产数量、路线数量、机器人/摄像头和报告层级分档。
- **Managed Inspection**：12k-35k 美元 / site / month，用于客户需要机器人运营、数据 QA 和月度可靠性报告时。
- **Enterprise Fleet**：5-20 个站点可到 500k-2M 美元 / year。
- **Implementation**：数据 onboarding、EAM/CMMS 集成、SOP 模板、私有部署和 change management 单独收费。
- **Hardware**：机器人、无人机、dock、传感器以 pass-through、融资、租赁或 OEM 合作处理，不做第一收入核心。

ROI 逻辑：

- 不只算 labor saving。
- 主价值是 avoided downtime、危险人工减少、access/scaffolding 减少、缺陷响应加速、turnaround 时间缩短和 audit evidence。
- 一个高可靠性站点只要减少 0.5-2 小时非计划停机，就足以支撑高价合同。
- 付费门槛：客户在 6-14 个月内看到回本路径。

试点 KPI：

- data completeness >95%。
- route completion >90%。
- anomaly-to-work-order time。
- time-to-verified-fix。
- actionable anomaly precision。
- hazardous man-hours removed。
- overdue inspection count。
- inspection backlog reduction。
- audit evidence retrieval time。
- edge FPS / latency / NPU load。
- pilot-to-production conversion。

## Go-To-Market

第一阶段：

1. 找一个有明确资产台账和停机成本的站点。
2. 选择 20-50 个巡检点和 1-2 条高价值路线。
3. 部署小型巡检机器人 / 固定相机 / 手持设备 + mock CMMS。
4. 用 6-10 周证明异常发现、工单创建、维修复检和证据报告。
5. 向设施负责人、运维主管、HSE、OT/IT、风险/保险和财务同时展示价值。

第二阶段：

- 从单路线扩到全站关键路线。
- 加入更多传感器和机器人/无人机品牌。
- 与 Maximo / SAP / ServiceNow / 国产 CMMS / DCIM / BMS 对接。
- 通过 O&M 服务商、红外巡检承包商、CMMS/EAM 集成商和机器人 OEM 渠道复制。

不建议一开始直接硬闯大型受监管公共电网采购，除非通过既有 O&M 或集成商通道进入。

## Competition

InfraLoop 不替代机器人、无人机、CMMS 或数字孪生，而是拥有异常生命周期。

- Spot / ANYbotics / Unitree / Deep Robotics：移动机器人强；InfraLoop 做跨设备异常、工单、复检和训练闭环。
- Skydio / Percepto / DJI / Flyability：无人机和监管场景强；InfraLoop 连接空中证据与地面维修。
- Gecko / Voliro / MISTRAS：专用检测、NDT 和传统服务强；InfraLoop 从日常 O&M 与非侵入式路线切入。
- Energy Robotics / DroneDeploy / Optelos / Zeitview：巡检平台强；InfraLoop 强调资产级工单闭环、复检审计和区域训练部署。
- IBM Maximo / SAP EAM / ServiceNow / Bentley：企业系统主账本强；InfraLoop 提供 robotics-native 现场事实和 verified repair。
- 中国电力和工业巡检生态：亿嘉和、申昊、国网/南网相关体系、云深处、优艾智合、大疆、宇树、七腾等已有设备；InfraLoop 可做统一事实层和训练闭环。

## Moat

壁垒是：

> asset-level memory + defect lifecycle dataset + CMMS connectors + risk taxonomy + edge profiles

会积累的资产：

- 每个柜、泵、阀、UPS、电池柜、管廊节点的基线、趋势和维修历史。
- 标准视角、异常图像、维修动作、复检结果、误判和停机后果的闭环数据集。
- Maximo / SAP / ServiceNow / 国产 CMMS connector、字段映射、状态同步和报告模板。
- 数据中心、BESS、变电站、管廊、泵站、电厂、冷链、轨交等行业 severity taxonomy。
- 视频最小化、本地留存、私有部署、区域云训练、审计和数据出境边界 playbook。
- LeRobot HIL 片段、AI Hub / QNN / QAIRT profile、shadow validation、canary 和 rollback。

时间越久，InfraLoop 越懂每类设施“什么异常会变成事故”，并通过 SOP 模板、CMMS 集成、审计记录和多站点 benchmark 形成迁移成本。

## Architecture

### Facility Twin

- 资产台账、地图、SOP、restricted zone、slow zone、标准视角、历史 baseline。
- 可接 Bentley iTwin / Cesium 风格 asset view，但比赛 demo 可以用轻量 mock twin。

### Robots + Sensors

- UGV：ROS 2、Nav2、LiDAR/depth/RGB/thermal、E-stop、edge inference。
- Drone：PX4 / ArduPilot + MAVSDK / uXRCE-DDS bridge，RGB/thermal payload。
- Fixed sensors：camera、thermal、acoustic、vibration、gas、SCADA tags。
- Human upload：手机、QR/NFC、定位、人工备注和复检照片。

### Qualcomm Edge Layer

- RB3 Gen 2 做比赛原型。
- RB5 / RB6 / IQ-9075 / Dragonwing IQ10 做多流、多传感器、生产级路线。
- AI Hub / QNN / QAIRT / ONNX Runtime QNN EP 做模型转换、profile、量化、部署和回滚。

### Inspection Intelligence

- asset recognition -> anomaly detection -> evidence package。
- rules：confidence threshold、sensor fusion、safety stop、human review gate。
- 低置信度事件默认 review required，不自动变成维护事实。

### Ops Integration

- CMMS/EAM：Maximo / SAP / ServiceNow / 国产 CMMS / mock API。
- 字段：asset ID、location、evidence、severity、suggested action、review status、verification rule。
- 工单状态：open、assigned、in_progress、fixed_pending_verify、verified、reopened。

### Learning Loop

- HIL review + teleop corrections -> LeRobotDataset。
- offline training -> simulation / shadow validation -> canary OTA -> fleet rollout。
- 学习策略不能越过独立的碰撞、安全、禁区、速度和远程审核约束。

## Competition Demo

3 分钟 demo：

1. 设施 twin 显示 pump、pipe rack、valve cabinet、禁行区和 20-50 个巡检点。
2. Operator 选择 weekly critical inspection loop。
3. Open-RMF 分配 UGV 到地面资产；无人机或云台相机捕获高位视角。
4. Qualcomm edge 本地识别 pump hotspot、腐蚀区域、仪表异常或气体风险。
5. 若 gas/VOC/no-go zone 被触发，UGV 停止并退回 safe waypoint，请求人工审核。
6. Evidence pin 出现在 twin：asset ID、pose、timestamp、hash、model version、confidence、raw image、thermal map。
7. Reviewer 批准后自动创建 CMMS work order。
8. 技术员标记处理，机器人或固定相机复检并回写 verified。
9. 坏视角、误判和人工接管保存为 LeRobot episode，进入 shadow/canary 队列。

演示重点：

> 不是机器人巡了一圈，而是设施当天完成了一次可审计的自动交班。

## Why Qualcomm

InfraLoop 是 Qualcomm 工业 edge AI、机器人和专网能力的应用层样板：

- 关键设施视频、资产图和告警证据不适合默认全量上云。
- 现场需要低延迟热异常、仪表读数、低照度视觉、声音、气体和低置信度事件判断。
- 弱网时仍要本地安全执行、缓存证据、恢复后同步 twin/CMMS。
- RB3 Gen 2 适合比赛原型；RB5/RB6/IQ-9075/Dragonwing IQ10 适合多摄像头、多传感器、5G/private-network 的生产路线。
- AI Hub / QNN / QAIRT 把云训练模型变成可部署、可 profile、可回滚的 edge artifact。
- Qualcomm + Aramco Digital 工业 IoT 合作、Qualcomm Ventures 投资 ANYbotics，都说明工业 edge AI 和巡检机器人是战略方向。

Qualcomm 的价值不是“提供一块板”，而是把 edge AI、连接、模型部署和机器人生态变成可复制的 O&M 解决方案。

## Ask

比赛阶段需要：

- RB3 Gen 2 / RB5 / RB6 / Vision Kit 或 Dragonwing dev kit。
- 一个 mock Maximo / SAP / ServiceNow / CMMS API。
- 设施地图、20-50 个巡检点、两周匿名读数、SOP 样例和合成异常数据。
- 3-5 个数据中心、能源、制造园区、城市生命线或设施 O&M 设计伙伴引荐。
- AI Hub / QNN profile 支持。
- 一个安全、非防爆、非高压实操环境的 demo 场景。

90 天目标：

> 跑出一个 Qualcomm-powered anomaly-to-repair 标杆 demo：本地视觉/热异常识别 -> 自动派单 -> 复检审计 -> HIL 训练回流。

## Claims To Avoid

- 不说完全替代人工巡检。
- 不说零停机。
- 不说预测所有故障。
- 不说任何机器人都即插即用。
- 不说已经通过防爆、ATEX、Ex 或电力行业认证。
- 不说 EPA、NFPA、国网/南网或 Qualcomm 官方认证，除非真实取得。
- 不在第一版演示危险高压、易燃易爆或需要特种资质的现场。

## Sources

- IEA electricity grids：https://www.iea.org/reports/electricity-grids-and-secure-energy-transitions/executive-summary
- IEA Energy and AI：https://www.iea.org/reports/energy-and-ai/executive-summary
- ABB downtime survey：https://manufacturingdigital.com/procurement-and-supply-chain/unscheduled-downtime-costs-us-125-000-per-hour-abb-survey
- Inspection robots market：https://www.thebusinessresearchcompany.com/report/inspection-robots-global-market-report
- Asset integrity management market：https://www.fortunebusinessinsights.com/industry-reports/asset-integrity-management-market-100988
- ASCE bridges：https://infrastructurereportcard.org/cat-item/bridges-infrastructure/
- Gecko unicorn status：https://www.geckorobotics.com/news/gecko-reaches-unicorn-status
- Gecko Navy IDIQ：https://www.geckorobotics.com/news/navy-idiq
- ANYbotics funding：https://www.anybotics.com/news/anybotics-raises-additional-60-million-to-drive-u-s-expansion/
- Energy Robotics：https://www.climateinvestment.com/news/energy-robotics-secures-13-5-million-series-a-to-scale-critical-infrastructure-inspections-with-ai-robotics
- Skydio utilities：https://www.skydio.com/solutions/utilities/distribution-network-inspection
- Percepto EPA alternative method：https://percepto.co/autonomous-ogi-drones-now-alternative-test-method-for-epa-subpart-ooooa-oooob/
- Voliro funding：https://voliro.com/blog/voliro-secures-23m-via-series-a-extension-to-modernize-infrastructure-with-aerial-robotics/
- Zeitview funding：https://www.climateinvestment.com/news/zeitview-secures-60m-to-advance-ai-powered-inspections-of-global-critical-infrastructure
- FAA BVLOS NPRM：https://www.federalregister.gov/documents/2025/08/07/2025-14992/normalizing-unmanned-aircraft-systems-beyond-visual-line-of-sight-operations
- 2026 政府工作报告：https://www.news.cn/politics/20260305/33c6919ec7a44dc5abff9420c5b424f1/c.html
- 新城建 / 韧性城市：https://www.mee.gov.cn/zcwj/zyygwj/202412/t20241206_1098168.shtml
- 安全生产治本攻坚三年行动：https://www.mem.gov.cn/gk/zfxxgkpt/fdzdgknr/202402/t20240222_478449.shtml
- 交通运输统计：https://xxgk.mot.gov.cn/jigou/zhghs/202506/t20250610_4170228.html
- 城市管线数据：https://www.cstid.org.cn/hxyw/003010/003010004/003010004003/20241209/cbabdb5a-50c5-48d3-96df-40dacd485b0d.html
- 5G 与数据中心规模：http://finance.people.com.cn/n1/2026/0130/c1004-40656081.html
- Deep Robotics X30：https://www.deeprobotics.cn/robot/wap/product3.html
- Unitree B2：https://www.unitree.com/cn/b2/
- Boston Dynamics inspection：https://bostondynamics.com/solutions/inspection/
- Cenosco AIM：https://cenosco.com/products
- MaxGrip AIM：https://www.maxgrip.com/software/asset-integrity-management-that-controls-risk-and-extends-asset-life/
- Nav2：https://docs.nav2.org/
- Open-RMF：https://www.open-rmf.org/
- PX4 ROS 2：https://docs.px4.io/main/en/ros2/user_guide
- MAVSDK：https://mavsdk.mavlink.io/main/en/
- Bentley iTwin：https://developer.bentley.com/itwin-platform-concepts/
- IBM Maximo：https://www.ibm.com/products/maximo
- SAP EAM：https://www.sap.com/products/scm/asset-management-eam.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB5：https://www.qualcomm.com/developer/hardware/robotics-rb5-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Qualcomm IQ-9075：https://www.qualcomm.com/internet-of-things/products/iq9-series/iq-9075
- Qualcomm IQ10 robotics reference design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/QNN_general_overview.html
- Qualcomm Aramco Digital：https://www.qualcomm.com/news/releases/2025/05/qualcomm-and-aramco-digital-to-drive-industry-transformation-thr
- Qualcomm Ventures ANYbotics：https://www.qualcommventures.com/insights/blog/portfolio-watch-investing-in-anybotics-a-leader-in-ai-powered-industrial-inspections/
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobotDataset：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
