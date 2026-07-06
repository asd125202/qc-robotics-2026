# ShipyardLoop 船厂生产证据闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

ShipyardLoop 是船厂生产现场的 AI 证据闭环：

> 把照片、视频、扫码、机器人遥测和质检记录自动绑定到分段、焊缝、涂层、工单和验收项，让每个工包从“口头完成”变成可验收、可审计、可回写、可结算的数据资产。

它不替代 PLM、CAD、ERP、MES 或 QMS，也不声称“全自动船厂”。它做的是现场信任层：让人、机器人、传感器、工长、质检、船东验收和结算系统之间形成闭环。

## Problem

造一条船最贵的不是不知道计划，而是不知道哪些工包真的可以关闭。

船厂已经有 CAD、PLM、ERP、MES、P6 和各种报表，但生产总监每天真正追问的是：

- 哪条焊缝能交检？
- 哪块涂层要返工？
- 哪份证据能让船东、船级社、质量部和承包商同时认可？
- 今天能不能释放下一道工序？
- 哪个 NCR 正在拖延交付？

具体痛点：

- 工包状态写着完成，现场可能仍在等材料、等检验、等返工、等照片、等签字或等前序释放。
- 焊接参数、seam 图像、NDT/VT 记录、涂装环境、DFT、NCR、inspector disposition 不在同一个证据包。
- 焊接、打磨、喷涂和扫描机器人能做单点自动化，但产出很少自然回到 work package、QA、返工和排程。
- 证据缺失会拖慢船东验收、船级社检查、QA dossier、承包商付款和下一道工序释放。

## Why Now

四个变化同时出现：

- 全球造船订单处在高位。BIMCO 报告 2026 Q1 全球手持订单达到 191m CGT，约等于全球船队 17%，为 17 年高点。
- 中国仍是核心市场。中国船舶工业行业协会披露，2025 年中国造船完工量 53.69m DWT、新接订单 107.82m DWT、手持订单 274.42m DWT，分别占全球 56.1%、69.0%、66.8%。
- QA/QC 证据仍大量人工化。NSRP 焊接记录项目估算，数字化每份检查报告可节省 10-15 分钟。
- 机器人投入正在增加，但资格认证、QA 证据、系统集成和 ROI 仍是采用瓶颈。NDIA/ETI 报告显示，受访海军造船单位中 40% 机器人焊接使用很少，22% 完全没有。
- 中国绿色船舶和智能船厂政策强调数字化工艺、智能装备、QHSE、绿色涂装、VOCs 管控和工业互联网。
- Qualcomm Dragonwing、RB3/RB5、AI Hub、QNN/QAIRT、私有 5G、Open-RMF、ROS 2 和 LeRobot HIL 让 edge-first evidence loop 可用更轻方式启动。

## Insight

ShipyardLoop 的核心洞察：

> 船厂不是缺另一个系统，而是缺一层“信任机制”。

Airbnb 的价值不是房源数据库，而是让陌生人交易可信。ShipyardLoop 的价值也类似：让工包、质量、返工、验收和结算从争议状态变成可信交易。

非显而易见判断：

- 船厂不会先为“全自动船厂”买单，但会为更快释放工序、更少缺证返工、更完整 QA 证据和更可信的每日进度付钱。
- 机器人会越来越多，但机器人本身不是最终产品。买方需要的是证明机器人、人和承包商到底完成了什么。
- 第一版不应该从全厂替换开始，而应该从 weld/NDT/OQE closure 这个强痛点进入。

## Solution

ShipyardLoop 在现有 ERP/MES/PLM/QMS 之上加一层轻量证据操作系统。

核心结果：

- 对生产：每天看到哪些工包真的 ready for inspection，哪些被材料、返工、检验或前序释放阻塞。
- 对质量：每条焊缝、涂层和返工都有可检索的客观质量证据和人工处置记录。
- 对财务和项目：承包商付款、船东验收和进度确认不再只依赖电话、截图和手工汇总。
- 对机器人团队：机器人输出不再是孤岛数据，而是进入工包关闭、NCR 和学习数据闭环。

## Product Workflow

一个工包从计划变成可验收证据：

1. 导入 WBS、工单、分段、舱室、焊缝、WPS、检验表、材料状态和验收要求。
2. AI 为每个作业生成证据清单：必须拍什么、扫什么、记录什么、谁复核。
3. 工人、班组长、固定相机、机器人、无人机或边缘网关采集照片、视频、参数和位置。
4. 模型识别缺陷、缺证、错位、低置信度和安全风险。
5. 主管或质检确认：接受、打回、分派返工、补拍证据或释放下一道工序。
6. 状态回写 MES/QMS/ERP/Ship OS：planned、in_progress、blocked、rework、ready_for_inspection、released、payable。
7. 人工改判、低置信度、遮挡和返工结果进入 LeRobot HIL episode。
8. 中国数据留在中国云或私有云；海外数据留在海外云或客户私有环境。
9. 模型经 AI Hub / Neural Processing SDK / QNN / QAIRT profile 后签名回到 Qualcomm edge。

## Market Wedge

Beachhead：weld/NDT/OQE 工包关闭。

为什么先切这里：

- 证据要求强。
- 报告量大。
- 返工代价高。
- 审计检索痛。
- 机器人正在进入现场。
- QA/QC 和制造工程有明确预算。

第一买方：

- QA/QC 总监。
- 焊接/NDT 经理。
- 制造工程负责人。
- 生产控制负责人。

中国版本：

- 面向商船、修船、海工、民营船厂和供应链。
- 强调本地部署、数据分级、绿色制造、QHSE、VOCs 过程证据和政策预算。

海外版本：

- 面向工作船、船修、海军供应链和二级供应商。
- 强调 OQE、审计检索、机器人 QA traceability、CUI/ITAR-aware 部署和 GovCloud/on-prem 选项。

扩展路径：

- 涂装 / VOCs / DFT。
- 表面处理 / 打磨 / 喷砂。
- 管系 / 舾装 / 材料追溯。
- HSE / 承包商结算 / 船东验收。
- 机器人连接器和多项目看板。

## Business Model

收入模型：

> paid pilot + QA evidence core + work package closure module + robot evidence connector + integration / services

建议包装：

| Package | Pricing Assumption | Buyer Logic |
|---|---:|---|
| 12-24 周付费试点 | $40k-$75k 或 30-60 万元 | 一个 hull、一个工序或一个机器人单元，低摩擦证明 ROI。 |
| QA Evidence Core | $120k-$250k / site / year | 离线移动端、OQE 包、报告、签字、审计搜索、FPY 看板。 |
| Work Package Closure | +$75k-$200k / program / year | 按关闭工包、项目或 active vessel 设置用量阶梯。 |
| Robot Evidence Connector | +$12k-$30k / robot cell / year | 捕获机器人参数、图像、WPS、NDT/VT、模型版本和异常。 |
| Enterprise / multi-yard | $500k-$1.5m ARR | 多项目、多厂区、SSO、CUI/ITAR 控制、ERP/PLM/MES 深集成。 |

投资人 underwriting 规则：

- 每个生产客户应能证明 3x+ gross annual benefit vs ARR。
- 试点到扩张目标 payback < 12 months。
- 长期软件毛利目标 70-85%；早期 pilot 因实施重，blended GM 45-60%。

## Go-To-Market

第一阶段：

1. 选择一个船修/改装/海工/工作船 yard 或二级供应商。
2. 跑 2-4 周 baseline：报告时间、缺证率、审计检索时间、NCR aging、工包关闭延迟。
3. 4-6 周配置表单、二维码、移动端、edge camera 和 ERP/MES/QMS 轻量接口。
4. Side-by-side 运行到 QA 接受数字记录作为 source of truth。
5. 达到 80-90% 数字采集、报告时间下降、审计包可导出、指定扩张 owner。

第二阶段：

- 接机器人供应商：Path、Inrotech、Novarc、HD Hyundai Robotics、Pemamek、国内焊接/涂装机器人。
- 接企业系统：MES、QMS、ERP、PLM、P6、document control、NCR、Ship OS。
- 从 weld/NDT 扩到涂装、管系、舾装、承包商结算和全厂 KPI。

## Competition

ShipyardLoop 不替代设计主干、排程系统、机器人或 inspector。

- Path Robotics / Inrotech / Novarc：robot execution 强；ShipyardLoop 捕获机器人证据并接入 QA、返工和排程。
- HD Hyundai Robotics / Fincantieri humanoid programs：未来机器人路线强；ShipyardLoop 做跨品牌、跨工序、跨承包商证据层。
- Palantir / BigBear.ai：数据整合和计划优化强；ShipyardLoop 从现场 edge 采集可信 production evidence。
- Siemens / Dassault / AVEVA / Cadmatic / SSI：设计、PLM、工程数据强；ShipyardLoop 补 as-built、OQE 和现场闭环。
- Floorganise：船厂 MES 强；ShipyardLoop 提供关闭工包所需的证据和异常处理。
- TRU / TruQC / 检查表工具：检查和文档强；ShipyardLoop 进一步连接 edge AI、机器人遥测、工包状态和训练数据。

## Moat

壁垒不是一个视觉模型，而是：

> work-package trust graph + OQE dataset + shipyard integration playbook + Qualcomm edge profile

会积累的资产：

- 分段、焊缝、舱室、涂层、管系、材料、班组、检验点和排程依赖的 work graph。
- 焊缝图像、NDT/VT 结果、涂层证据、工具遥测、位置、模型置信度和人工复核数据集。
- ERP、MES、PLM、QMS、P6、文档控制、NCR、WPS、材料和 inspector disposition connectors。
- 船厂弱网、强反光、钢结构遮挡、承包商协作、QA 习惯和安全边界的实施经验。
- 从缺陷发现、返工分派、复检证据、签字放行到付款依据的流程锁定。
- Qualcomm AI Hub / QNN / QAIRT profile、离线缓存、签名模型、回滚和低置信度队列。

## Architecture

边缘先保证现场可用，云端只负责训练和跨项目学习。

```text
ERP / PLM / MES / QMS
  |  work orders, drawings, inspection plans, NCRs, approvals
  v
ShipyardLoop Integration Plane
  - ISA-95 object model: block / seam / zone / operation / inspection / result
  - REST / MQTT adapters for MES / QMS / ERP
  - OPC UA adapter for welder, paint-booth, tool telemetry
  v
Evidence Orchestration
  - Open-RMF for fleet/task coordination
  - VDA 5050 adapter for AGV/AMR fleets
  - ROS 2 / Nav2 on robots for local navigation
  v
Qualcomm Edge Nodes
  - Dragonwing / RB3 / RB5 vision compute
  - RGB, depth, thermal, laser-line, DFT/env probes
  - On-device weld, paint, corrosion, missing-part inference
  v
Evidence Ledger
  - WORM/object storage for raw media
  - Hash chain for work order, pose, model hash, operator, signoff
  v
Human + Learning Loop
  - Inspector validates / overrides AI findings
  - Low-confidence cases become LeRobot HIL episodes
  - Signed model update returns to edge after validation
```

## Competition Demo

3 分钟 demo：

1. Judge 扫描 QR：Block B17 / Weld S-023 / Paint Zone P-14。
2. Mock MES 释放检查任务，QMS 给出证据要求。
3. Open-RMF 派发小 AMR 或桌面机器人；Qualcomm edge 捕获 RGB/depth/热图。
4. 模型标出 weld undercut / spatter、paint holiday / run、corrosion 或 missing bracket。
5. 检查员接受一个发现、驳回一个误报；被接受的发现打开 mock NCR/rework hold。
6. 替换样板或覆盖缺陷后复扫。
7. Evidence ledger 显示 before/after chain：原始缺陷、人工处置、返工证明、最终放行。
8. 低置信度场景通过操作员接管记录为 LeRobot HIL episode。
9. 断开 WAN 测试：本地推理和证据采集继续运行，恢复连接后同步。
10. 输出 one-page evidence passport，包含工单、图像、hash、缺陷、复核签字和 MES/QMS 状态。

安全边界：

- 不做真实电弧焊。
- 不做真实喷涂。
- 不做高风险打磨。
- AI 只做 triage / evidence capture，最终验收由 qualified inspector 或 QMS 规则决定。

## Why Qualcomm

这是 Qualcomm 最适合讲的重工业 physical AI 样板：

- 多摄像头和多传感器：RGB/HDR、thermal、depth/LiDAR、tool telemetry、DFT、pose 和 timestamp 需要同步成证据。
- 低延迟：weld/paint/defect inference、low-confidence routing 和安全边界需要现场判断。
- 弱网和私有数据：船厂 CAD、工艺、质量视频和防务/海工信息不能默认上公网云。
- 私有连接：船坞、车间、分段和移动机器人需要 private 5G / Wi-Fi / store-and-forward。
- 硬件路径：RB3 Gen 2 / RB5 做 demo；Dragonwing 工业 edge AI 设备做多传感器生产路线。
- 软件路径：AI Hub、Neural Processing SDK、QNN/QAIRT 让模型可 profile、可签名、可回滚。
- 商业路径：把 Qualcomm edge AI 从普通工厂延伸到船厂、海工、重型制造和工业私有网络。

## Ask

请 Qualcomm 帮我们把一个可演示闭环变成 90 天可试点产品：

- Dragonwing / RB3 / RB5 dev kit。
- AI Hub / Neural Processing SDK / QNN profile 工程支持。
- 多摄像头、本地推理、弱网 store-and-forward 的参考设计建议。
- 引荐 1-2 个船修厂、海工制造商、船厂 SI、焊接/涂装机器人厂商或质量顾问。
- 共同完成 10-30 个样例工包：证据采集、异常分流、人工复核、返工关闭、QMS/MES 回写和 ROI 报告。

## Claims To Avoid

- 不说解决造船危机。
- 不说替代工人、工长、焊工、质检或 NDT。
- 不说全自动船厂。
- 不承诺 100% 自动识别进度或 100% weld acceptance。
- 不声称已通过 Navy、船级社、军工或安全认证。
- 不把 QNN/QAIRT 描述成 safety-certified control system。
- 不承诺中国/海外数据无障碍流动。

## Sources

- BIMCO global orderbook 2026 Q1：https://www.bimco.org/news-insights/market-analysis/shipping-number-of-the-week/2026/0409-snow/
- OECD shipbuilding overview：https://www.oecd.org/en/topics/sub-issues/shipbuilding.html
- CANSI 2025 中国造船数据：https://www.cansi.org.cn/cms/document/19815.html
- NSRP Optimized Weld Records：https://www.nsrp.org/wp-content/uploads/2023/01/2021-481-001-MS08-RAPOptimized-Weld-Records-Final-Report-020323.pdf
- NSRP Automated Detail Planning / MES：https://www.nsrp.org/wp-content/uploads/2026/01/2019-483-011-ADP-MS11-Final-Report-Rev2.pdf
- NDIA / ETI robotic welding：https://www.emergingtechnologiesinstitute.org/-/media/ndia-eti/reports/robotics/accelerating-robotic-welding-solutions-report.pdf
- HII / Path Robotics：https://hii.com/news/hii-teams-with-path-robotics-to-integrate-physical-ai-into-manned-and-unmanned-shipbuilding
- HD Hyundai Robotics / Chouest：https://www.workboat.com/chouest-orders-welding-robots-for-its-shipyards
- Fincantieri humanoid welding program：https://www.marinelink.com/news/partners-aim-develop-humanoid-welding-535594
- TRU Marine：https://trusolutions.com/solutions/marine/
- Floorganise MES：https://www.floorganise.com/mes-manufacturing-execution-system/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm Neural Processing SDK：https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai
- Open-RMF：https://www.open-rmf.org/
- VDA 5050：https://www.vda.de/en/topics/automotive-industry/vda-5050
- OPC UA：https://opcfoundation.org/about/opc-technologies/opc-ua/
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
