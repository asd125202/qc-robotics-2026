# UptimeOS Pitch

更新时间：2026-07-06。该版本按 YC / Airbnb 风格 pitch spine 重写：先讲问题，再讲现状为什么失败、方案、为什么现在、产品、商业模式、壁垒、为什么需要 Qualcomm、比赛演示和需要的支持。

## One-Liner

RaaS 卖的不是机器人，是可审计的 uptime。UptimeOS 给每台 Dragonwing 机器人一份 Health Passport，把遥测、AI Hub/QNN 证据、远程诊断、FRU/RMA、技师工单、质保和 SLA 发票接成一条售后经济账本。

## 1. Problem

机器人能交付，不代表它能被持续运营、融资、保险和续约。

商业机器人进入客户现场后，真正决定 ROI 的不是首日 demo，而是 uptime、MTTR、一次修复率、备件命中、质保责任、SLA 证据和下次续约。现在这些事实散落在 OEM 云、ROS 日志、微信群、CRM、Excel、备件 PDF、工单系统和财务发票里。

核心痛点：

- 客户只看到业务中断，却难以判断是硬件、软件、网络、模型、操作还是环境问题。
- 工程师往往先拉群、翻日志、要视频，再决定是否派人；MTTR 被信息收集拖长。
- FRU、库存、替代件、技师资质、工单 checklist 和客户签收没有形成同一条闭环。
- 融资方和保险方需要健康、维修、事故、模型版本和残值证据，而不是静态设备清单。
- 如果 Qualcomm 只出现在 BOM 里，就无法进入售后、续费、服务网络和生态标准。

## 2. Current Alternatives Fail

今天的售后工具各管一段，没有一层为机器人 uptime 负责。

- OEM service cloud 强在单品牌，弱在跨队列。客户现场常是多品牌、多系统、多集成商。
- RobOps dashboard 能看状态、日志和远程介入，但不天然覆盖 FRU/RMA、保修和发票。
- CMMS/EAM/FSM 能派单，但不了解 ROS、QNN、模型、OTA 和事故回放语义。
- Excel 和群聊可以撑住试点，但撑不住 RaaS 毛利、融资尽调、保险理赔和大客户采购审计。

UptimeOS 不替代 OEM，也不替代 ServiceNow / Maximo / Dynamics。它补的是机器人级系统记录：谁在何时更换了哪个部件、哪个模型版本在什么硬件上运行、哪次事故影响了 SLA，以及这台机器人是否还值得融资或转售。

## 3. Solution

UptimeOS 是机器人售后经济的系统记录。

核心流程：

1. Enroll：扫码建档，写入 robot_id、客户站点、Dragonwing target、BOM、证书、保修和数据边界。
2. Sense：边缘 agent 采集 ROS、CAN、BMS、热、相机、网络、QNN latency 和任务状态。
3. Diagnose：生成 incident packet、log bundle、疑似原因、风险等级、远程只读诊断和升级路径。
4. Fix：匹配 FRU、库存、RMA、技师资质、移动 checklist、照片和客户签收。
5. Bill & Learn：更新 uptime ledger、质保证据、SLA credit、RobotLeaseOps 发票和 LeRobot 失败片段。

一句话：把每次运行、异常、诊断、维修、OTA、换件、签收和 SLA 结算变成同一份可信资产记录。

## 4. Why Now

机器人正在从项目交付转向运营资产，售后数据第一次变成战略入口。

- IFR 2025 显示，2024 年专业服务机器人销售接近 20 万台，RaaS fleet 增长 31%。
- Autodesk 2026 年宣布以约 36 亿美元收购 MaintainX，说明维护、资产历史和现场运营数据正在进入平台级生命周期管理。
- EU Cyber Resilience Act、数字产品护照、数据出境、AI 模型治理和客户 IT/OT 安全审计，会让机器人生命周期记录变成采购门槛。
- 机器人比传统设备更需要这层记录，因为它同时包含硬件、软件、AI 模型、传感器、远程操作和安全责任。

## 5. Product

UptimeOS 的交付物不是一句“我们有运维平台”，而是一组客户、服务商、金融方和 Qualcomm 都能读取的 artifact。

核心 artifact：

- `robot-health-passport.json`：序列号、站点、Dragonwing SoC、运行小时、电池循环、固件、模型、维修、质保和 SLA。
- `uptime-agent.manifest.yaml`：采集 topic、诊断权限、脱敏策略、离线缓存、远程访问和上报频率。
- `incident-log-bundle.mcap`：任务上下文、地图位置、错误码、QNN profile、MCAP slice、照片/视频引用和 custody hash。
- `fru-rma-record.json`：BOM、可更换件、兼容性、库存、替代件、质保状态、RMA 和技师签收。
- `warranty-ledger.json`：质保期、排除项、换件记录、事故关联和责任判断依据。
- `monthly-uptime-ledger.pdf`：uptime、MTTR、一次修复率、SLA credit、排除项、服务成本和续约风险。

技术层：

- Robot-side Uptime Agent：设备身份、遥测采集、健康评分、远程诊断、日志包、OTA 客户端。
- Cloud control plane：Robot Registry、Digital Twin、telemetry ingest、incident engine、predictive maintenance、OTA Orchestrator、AI Hub/QNN Evidence Store。
- Service business layer：CMMS / Field Service adapter、Spare Parts Inventory、FRU/RMA、Warranty Ledger、Technician Mobile App、Root-Cause Reports。
- Evidence layer：RiskLedger、CertForge、RobotLeaseOps、LeRobot failure mining。

## 6. Market And Business Model

卖给谁？卖给机器人停机时真正亏钱的人。

第一批客户：

- RaaS 运营商：需要控制服务成本、SLA credit、备件、换机和续约。
- OEM 售后部门：需要把硬件销售变成可续费服务能力。
- 系统集成商：需要在多品牌现场提供统一服务门户和维护记录。
- 工厂/仓库/园区运营团队：需要对 uptime、维修、事故和审计有统一事实。
- 维护服务商：需要标准化 checklist、备件、RMA、技师资质和客户签收。

商业模式：

- 中国版：OEM/SI 白标服务中台，支持企微/钉钉入口、本地备件库、授权服务商、私有化和客户工单门户。
- 海外版：按 robot/month、site/year、service tier、数据保留和系统集成收 SaaS 费用。
- RaaS 版：可按机器人月费，或按 RaaS MRR 的一小部分作为服务运营层费用。
- Enterprise/regulated 版：私有化部署、SSO/RBAC、审计、OT 分区、合规包和定制 adapter。

安全表述：不承诺固定 uptime 提升或质保准备金释放。UptimeOS 先建立基线，再用 MTTR、一次修复率、现场派工、备件命中和 SLA dispute 的变化做验证。

## 7. Competition And Moat

市场已有三层碎片化工具：

- OEM service clouds：ABB Connected Services、KUKA iiQoT、FANUC ZDT、Universal Robots UR Care 等。
- RobOps / fleet ops：Formant、Viam、InOrbit、Foxglove 等。
- CMMS / EAM / FSM：ServiceNow、IBM Maximo、Microsoft Dynamics、MaintainX、UpKeep、Limble 等。

UptimeOS 的 wedge：

- Cross-brand robot/cell health graph：从单机状态上升到现场资产健康图。
- Alert-to-fix closed loop：异常、诊断、备件、派工、签收、RMA、发票和训练回流在同一条链上。
- Multi-tenant service network：OEM、SI、维护商、备件仓和客户共享一份事实。
- Robot knowledge layer：故障语义、FRU、QNN/模型版本、OTA 和维修结果持续复利。
- Coexistence：上接 ServiceNow / Maximo / Dynamics，下接 OEM cloud / ROS / PLC / OPC UA / MTConnect / QNN runtime。

## 8. Why Qualcomm

Dragonwing 的下一层生态 attach，不是更多 demo，而是 uptime。

Qualcomm 已经在 Dragonwing IQ10 Robotics Reference Design 中强调从 prototype 到 production 的一体化机器人平台：计算、传感、网络、软件、部署、验证和生命周期管理。UptimeOS 把这条主线商业化：让 Dragonwing 不只负责机器人跑起来，还负责机器人被客户长期运营、维护、升级和续约。

Qualcomm 价值：

- Dragonwing Uptime Agent：在本体侧完成健康摘要、异常优先上报和低带宽诊断。
- AI Hub / QNN Evidence：latency、runtime、模型 hash、profile、rollback 记录进入健康护照。
- Product Longevity：长期供货、PCN/PDN、安全更新和备件计划变成客户采购信心。
- Ecosystem Attach：OEM、SI、云训练、SkillDock、RobotLeaseOps 和服务商围绕 Dragonwing 标准协同。

需要 Qualcomm 支持：

- Dragonwing 诊断 profile：温度、功耗、QNN latency、相机、网络、BMS 和系统版本的标准上报模板。
- AI Hub / QNN 证据接口：让模型部署证据直接进入售后记录。
- 开发板与生态背书：复赛用真实开发板跑诊断 agent，展示 Qualcomm-first aftermarket OS 的可行性。

## 9. Competition Demo

8 分钟 demo 要证明：我们能把一次故障变成可审计、可收费、可学习的服务闭环。

演示脚本：

1. 扫码建档：生成健康护照，包含 robot_id、BOM、Dragonwing target、模型版本、服务合同和数据边界。
2. 异常触发：模拟电机温升、相机丢帧或 QNN latency 漂移。
3. 远程诊断：边缘 agent 生成 incident packet、log bundle、疑似原因和只读诊断报告。
4. 备件与技师：系统推荐 FRU，检查库存，创建移动工单，记录照片、换件、客户签收和 RMA。
5. SLA 与训练回流：更新 uptime ledger、RobotLeaseOps 发票、RiskLedger 证据、CertForge 变更和 LeRobot failure episode。

## Claims To Avoid

- 不承诺所有客户都能达到固定 uptime。
- 不承诺自动替代 OEM、实验室质保判断或法律责任判断。
- 不说 AI 自动判断责任；只能做故障建议、证据整理和人工审批。
- 不直接控制安全关键链路；远程动作必须有 RBAC、审批、审计和 SafetyOps gate。
- 不声称跨所有品牌无缝兼容；先说 Qualcomm-powered / RobotCoreOS-first，再开放 adapter。

## Sources

- IFR service robots 2025：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Autodesk to acquire MaintainX：https://adsknews.autodesk.com/en/news/autodesk-to-acquire-maintainx-advancing-unified-platform-in-operations/
- Qualcomm Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm Product Longevity Program：https://www.qualcomm.com/internet-of-things/products/product-longevity-program
- FANUC ZDT：https://www.fanucamerica.com/products/software/zero-down-time-zdt
- ABB Connected Services：https://new.abb.com/products/robotics/nl/service/data-driven-services/connected-services
- KUKA iiQoT Robot Condition Monitoring：https://www.kuka.com/en-us/products/robotics-systems/software/cloud-software/iiqot-robot-condition-monitoring
- Formant incident management：https://docs.formant.io/docs/incident-management
- InOrbit Unified Command：https://www.inorbit.ai/unified-command
- ServiceNow Field Service Management：https://www.servicenow.com/docs/r/release-notes/field-service-management-rn.html
- IBM Maximo：https://www.ibm.com/products/maximo
- Microsoft Dynamics Connected Field Service：https://learn.microsoft.com/en-us/dynamics365/field-service/connected-field-service
- ROS diagnostics：https://github.com/ros/diagnostics
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN execution provider：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- EU Cyber Resilience Act：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
