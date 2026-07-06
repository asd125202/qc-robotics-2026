# RobotLeaseOps Pitch

更新时间：2026-07-06。RaaS、融资租赁、补贴、税务、保险、服务合同、机器人价格和监管要求高度依赖地区、客户资质和会计处理；真实销售前必须由客户财务、税务、法律、银行、保险和安全团队确认。

## One-Line Pitch

RobotLeaseOps 是 Dragonwing lease-ready 机器人资产运营层：

> robot hardware + deployment + cloud training + AI Hub / QNN evidence + EdgeFleet monitoring + SafetyOps + UptimeOS + RiskLedger + warranty + maintenance + financing + SLA invoice。

一句话：别让客户买机器人，先让客户雇一支有 SLA 的机器人班组。

## Core Problem

商业机器人今天不是“买一台机器”的问题，而是“谁对现场结果负责”的问题。

客户要自动化，但每次采购都会被拆成十几个问题：

- CapEx 谁批。
- 机器人是否适合现场。
- 集成和安全评估谁做。
- 模型和边缘部署是否被验证。
- 维护、保修、备件、换机和停机责任谁承担。
- 融资方如何判断资产健康和残值。
- 月度发票和 SLA credit 如何计算。
- 现场失败是否能复盘和训练下一版。

RobotLeaseOps 的目标不是做又一个 RaaS 厂商，而是让 OEM、SI、融资方、保险方、维护商和客户共享一条机器人租赁事实链。

## Why Now

RaaS 已经被市场教育：

- IFR 2025：2024 年专业服务机器人销售接近 20 万台，RaaS fleet 增长 31%。
- Locus、Formic、Brightpick、AutoStore、Universal Robots leasing、RobotLAB、Knightscope MaaS 等都证明机器人可以按月、按小时、按任务或按产能采购。
- 中国活动/服务机器人短租平台证明买家接受“租机器人”，但更多停留在活动、展陈、餐饮和营销场景。
- 人形机器人、AMR、清洁、巡检和制造 cobot 正在从试点进入付费部署，最缺运营责任层。

缺口不是“还有没有 RaaS”，而是有没有跨品牌、跨融资方、跨维护商的资产运营系统。

## Product Thesis

RobotLeaseOps 把机器人从硬件项目变成 SLA-backed robot labor contract：

1. 客户输入任务、班次、面积、吞吐、SLA 和预算约束。
2. 系统生成 robot SKU、Dragonwing target、部署计划、AI Hub/QNN evidence、SafetyOps、EdgeFleet、维护和融资方案。
3. 试点通过 acceptance gate 后进入正式订阅或租赁期。
4. EdgeFleet 和 UptimeOS 持续记录 uptime、任务小时、故障、维护、备件和远程诊断。
5. RiskLedger 保留安全事件、事故回放、责任边界和保险/融资证据。
6. 月底自动生成 SLA invoice、service credit、QBR、续约风险和扩容建议。

## Product Modules

### 1. Lease Bundle Builder

报价不是“这台机器人多少钱”，而是：

- 场景：仓储 AMR、商业清洁、安保巡逻、餐饮配送、制造 cobot、受控人形试点。
- 任务量：小时、面积、pick、cycle、inspection、weld seam、shift。
- KPI：uptime、coverage、throughput、first-pass yield、intervention rate。
- 合同：购买、租赁、RaaS、按小时、按件、保底加超额、季节性扩容。
- 服务：Core / Pro / Critical SLA。
- 数据边界：中国本地、海外云、私有化、离线缓存。

### 2. Acceptance Gate

不应在“机器人到货”时开始正式收费，而应在可验证验收后开始：

- 3-10 个连续生产班次。
- 30 天稳定运行。
- target throughput / coverage。
- uptime。
- first-pass yield。
- intervention rate。
- MTTR。
- safety incidents。
- operator/customer signoff。

### 3. Asset And Lease Registry

每台机器人都有资产出生证：

- serial、BOM、Dragonwing target、MAC/IMEI、证书链、固件基线。
- lease contract、客户、站点、SLA、保修、排除项、服务等级。
- deployment photo、handover checklist、customer signoff。
- residual value、再部署状态、回收/转租记录。

### 4. Service Ledger

RaaS 毛利来自服务运营：

- 工单、技师、远程诊断、日志包、客户批准。
- 备件、库存、RMA、RTV、换件记录。
- warranty reserve、MTBF 假设、预计维修成本和释放流水。
- EdgeFleet 告警、断网补传、服务历史和 root-cause report。

### 5. AI / QNN Evidence Registry

租赁资产里的 AI 必须可证明：

- model card、dataset version、model digest。
- AI Hub compile / profile / inference job。
- QNN / ONNX Runtime QNN backend、runtime version、target device。
- latency、memory、accuracy/eval、thermal/power summary。
- OTA release、canary、rollback 和 deployment digest。

## China / Global Versions

### China

中国市场的两个入口不同：

- 短租/活动/文旅/商场/餐饮：买的是曝光、互动、确定性交付和现场服务。
- 功能型工业/仓储/巡检/清洁：买的是任务完成率、可用率、维护响应、低首付和本地服务。

建议套餐：

- 活动引流包：日租，机器人+运输+现场工程师+脚本/动作模板+保险。
- 门店运营包：月租，迎宾、配送、互动、巡逻。
- 清洁巡检包：按面积、班次、耗材和响应 SLA 定价。
- 工厂/仓储试点包：按任务吞吐、OEE、节省人工小时和 success fee 建模。

合规边界：

- 长期租赁不一定自动表外，CAS21 等规则可能要求确认使用权资产和租赁负债。
- 数据默认本地化，跨境按数据类型、客户角色、行业和阈值评估。
- AI 内容标识、生成式 AI、网络数据安全和等保要求需按实际功能评估。

### Global

海外优先场景：

- 仓储/3PL。
- 商业清洁。
- 安保巡逻。
- 酒店/餐饮配送。
- 制造 cobot。
- 受控人形试点。

常见商业语言：

- lower upfront cash。
- uptime SLA。
- remote diagnostics。
- maintenance included。
- productive-hour pricing。
- customer success review。
- SBOM / cyber evidence。
- GDPR / AI Act / Machinery / CRA readiness where relevant。

边界：

- IFRS 16 / ASC 842 下，超过 12 个月的租赁可能仍上表。
- 不承诺税务优惠、补贴、保险降价、融资审批或表外处理。

## Competition

RobotLeaseOps 的定位不是单一机器人供应商：

- Formic：制造业全托管 RaaS，证明中小制造客户愿意为 outcome + maintenance 付费。
- Locus / inVia / Vecna / ForwardX：AMR RaaS，证明仓储订阅和峰值扩容成立。
- Brightpick / AutoStore：仓储 automation subscription / pay-per-pick 证明 outcome pricing。
- Universal Robots / Hirebotics / RobCo：cobot 生态证明应用包和租赁需求。
- GXO / Agility / Figure / Apptronik：大客户和人形试点说明早期商业部署需要运营责任层。
- 中国 AMR / 服务机器人 / 人形机器人厂商：硬件供应强，但中立租赁资产运营层仍弱。
- 金融租赁方和设备租赁公司：懂信用和残值，但不懂机器人 uptime、任务完成率和模型/软件状态。

RobotLeaseOps 可占的空白：

- 中立租赁操作系统。
- 任务级资产台账。
- 合同与计费引擎。
- 机器人残值与二级流转。
- 人形机器人试点运营责任层。
- 面向 SME 的 RaaS 后台即服务。

## Moat

护城河来自可审计运营事实：

- Lease-ready artifacts：资产出生证、合同、服务历史、SLA 公式、AI/QNN 证据、月度发票。
- Service data compounding：故障率、备件消耗、远程修复率、停机原因、排除项、维护成本。
- Residual value curve：跨品牌资产健康、再部署成功率、二级租赁、残值曲线。
- Channel network：OEM、SI、金融租赁方、保险方、维护商共享同一套运营语言。
- Qualcomm profile library：Dragonwing / RB / QCS / IQ target、runtime、thermal、power、QNN evidence 和 longevity 数据。

## Demo Storyboard

三分钟网页演示：

1. Configure：输入 10 万平方英尺仓库、两班制、98.5% uptime、清洁+巡检任务。
2. Contract：生成两台机器人、Dragonwing edge module、AI Hub/QNN badge、月费、SLA、验收 KPI。
3. Enroll：扫描机器人二维码，创建 `robot_id`，绑定序列号、X.509 证书、客户站点和合同。
4. Operate：EdgeFleet 显示心跳、任务小时、battery、thermal、model version、coverage。
5. Fail：模拟电机温度异常或导航进程崩溃，自动开 incident。
6. Service：拉取日志包，远程诊断，派备件或替换机，更新 service history。
7. AI Evidence：展示模型 hash、AI Hub job、QNN backend、latency、target device。
8. Invoice：月底生成 uptime、downtime 排除项、SLA credit、使用量、发票和 QBR。

## Why Qualcomm

RobotLeaseOps makes Dragonwing lease-ready。

Qualcomm 的收益：

- Dragonwing attach：每台租赁机器人绑定 Qualcomm target profile。
- AI Hub/QNN usage：AI evidence 从开发工具变成合同、验收、续约材料。
- Telemetry feedback：合规聚合数据反馈真实热、功耗、故障、模型漂移和维护成本。
- OEM/SI channel：伙伴可以围绕 Dragonwing 发布 lease-ready kit。
- Enterprise confidence：产品寿命、OTA、fleet lifecycle、QNN evidence 和服务记录进入采购语言。
- Developer ecosystem：Dragonwing Robotics Hub / Arduino / Edge Impulse demo 可以升级成可租赁应用模板。

建议对 Qualcomm 的 ask：

- Dragonwing Lease-Ready Program。
- AI Hub / QNN / Device Cloud quota。
- 2-3 个 reference SKU：轻量服务机器人、仓储/巡检 AMR、受控人形/多传感器机器人。
- 共同定义 lease evidence schema：model passport、runtime profile、uptime telemetry、service history、SLA invoice。

## Claim Boundaries

可以讲：

- RobotLeaseOps 能降低 upfront cash、把服务风险显性化、让机器人运营可计量。
- RobotLeaseOps 可以帮助 OEM/SI/租赁方把机器人打包成可验收、可服务、可续约的产能。
- RobotLeaseOps 与 Qualcomm Dragonwing、AI Hub/QNN、EdgeFleet、SafetyOps、UptimeOS 和 RiskLedger 高度互补。

避免讲：

- 已获 Qualcomm 官方认证、合作或投资。
- 保证融资、保险、补贴、税务优惠、表外处理或固定 ROI。
- 自动满足中国、美国、欧盟或行业监管。
- 所有模型都能在 QNN 上最优运行。
- RaaS 一定比购买更便宜。
- 机器人能力等同于人工替代。

## Sources

- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Locus RaaS：https://locusrobotics.com/why-locus/robots-as-a-service
- Formic full-service automation：https://formic.co/full-service-automation
- Brightpick RaaS：https://brightpick.ai/resources/how-brightpicks-raas-works/
- AutoStore Pay-per-Pick：https://www.autostoresystem.com/news/autostore-launches-pay-per-pick-service-option-to-address-fast-growing-demand-for-fulfillment-automation
- Universal Robots leasing：https://www.universal-robots.com/services/collaborative-robot-leasing/
- RobotLAB financing：https://www.robotlab.com/financing/
- Knightscope MaaS：https://knightscope.com/use-cases/who-we-serve
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm AI Engine Direct SDK：https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk
- Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm Product Longevity Program：https://www.qualcomm.com/internet-of-things/products/product-longevity-program
- NIST IoT device baseline：https://nvlpubs.nist.gov/nistpubs/ir/2020/NIST.IR.8259A.pdf
- AWS IoT Jobs：https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html
- AWS IoT Secure Tunneling：https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html
- Microsoft Dynamics Field Service service history：https://learn.microsoft.com/en-us/dynamics365/field-service/service-history
- IFRS 16 leases：https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/
- CAC data export rules：https://www.cac.gov.cn/2024-03/22/c_1712776612187994.htm
- EU AI Act：https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU Cyber Resilience Act：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
