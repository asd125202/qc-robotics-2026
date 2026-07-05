# IntegratorForge Pitch

更新时间：2026-07-05。机器人系统集成、工业安全标准、渠道伙伴和区域合规变化较快，真实交付前需要按客户现场、目标国家和机器人类型重新验证。

## Core Thesis

RobotMac / Qualcomm edge robots 如果要商业化，不能只靠开发板、SDK、云训练和单个 demo。企业购买的是可上线结果：现场调研、系统集成、安全评估、验收测试、培训、质保、备件、SLA 和持续维护。

> IntegratorForge = certified partner marketplace + reusable project library + deployment evidence system。

它把系统集成商的经验变成可复制产品：

- deployment playbook。
- reference BOM。
- sensor / EOAT / robot / edge compute compatibility。
- ROS 2 graph and QNN model assets。
- safety and risk assessment evidence。
- FAT / SAT / SIT acceptance packet。
- handover binder。
- field service and SLA workflow。

## Research Synthesis

### 1. Integration Is The Value Pool

机器人系统集成不是附属服务，而是巨大价值池。公开市场研究把 robotics system integration 估算在数百亿美元规模，并且持续增长；MIT Sloan 也指出，对于中小企业，集成到流程里往往是最大障碍，甚至可能达到机器人本体成本的数倍。

企业买家的真实痛点：

- 机器人硬件只是生产单元或队列的一部分。
- WMS / MES / ERP / PLC / 安全系统 / 人员流程必须一起工作。
- 成本超支、上线延期和 KPI 失败会破坏管理层信心。
- 非汽车行业、SME、实验室和物流客户更缺少内部自动化专家。

### 2. Ecosystem Pattern

成熟机器人与工业自动化公司都在做同一件事：

- Universal Robots：UR+ 认证组件、开发者套件、Academy、Certified System Integrator。
- MiR：Certified System Integrators、MiRGo top modules、partner locator、Academy 和 support portal。
- ABB / FANUC / Yaskawa / Omron：value provider、authorized integrator、training、仿真工具、应用库和 partner locator。
- Rockwell / Siemens：系统集成商渠道、PartnerNetwork、code library、industrial marketplace、training / certification。
- NVIDIA：Jetson ecosystem、Isaac / Isaac ROS、NPN、Inception 和 reference workflows。

结论：IntegratorForge 不能只是“黄页”。它必须是 credentialed marketplace + reusable project library。

### 3. Safety And Acceptance Evidence

部署机器人必须有证据链：

- ISO 10218-1:2025 / ISO 10218-2:2025。
- ISO/TS 15066 collaborative robot guidance。
- ANSI/A3 R15.06:2025。
- ANSI/A3 R15.08 for AMR / IMR。
- ISO 3691-4 for driverless industrial trucks。
- OSHA robotics guidance, LOTO, machine guarding, electrical, PPE。
- ISA-105 / ANSI/ISA-62381 for FAT / SAT / SIT methodology。
- EU Machinery Regulation 2023/1230 for EU-facing deployments from 2027。
- UL / NRTL evidence where relevant。

IntegratorForge 不应该声称自己“认证客户现场”。更稳妥的表达是：生成 audit-ready deployment evidence 和 standards-aware handover binder。

### 4. Business Model

最强商业包装不是“买工具”，而是 managed deployment program：

- Readiness audit：workflow survey、ROI model、safety scan、integration map、SI quote package。
- Paid pilot：6-12 周，1 个现场，1-5 台机器人 / 单元，明确 success metrics。
- Deployment package：starter AMR / cobot / lab cell，包含集成、调试、培训和 hypercare。
- Platform subscription：按 site 和 robot 计费，包含 telemetry、support、templates、evidence。
- Training / certification：online seat、hands-on lab、train-the-trainer、exam、annual renewal。
- Managed support：8x5 / 24x5 / 24/7 SLA，现场 FSE 和备件池。
- Marketplace take rate：对服务、模板、软件模块和私有报价收取合理比例。

### 5. China And Overseas Versions

China Forge：

- 本地硬件供应和模块生态：Thundercomm、Quectel、Fibocom、Radxa、Firefly 等。
- 本地文档、Gitee / CSDN / 高校实验室、中文 AI Hub / QNN materials。
- 本地云和 OTA，数据最小化，避免不必要跨境数据流。
- 面向 Jetson / RK3588 / Raspberry Pi / ROS 教育项目提供 Dragonwing migration kit。

Overseas Forge：

- 对接 Qualcomm AI Hub、FoundriesFactory、Edge Impulse、Arduino Project Hub、GitHub。
- 与 Advantech、VVDN、Lantronix、ModalAI、e-con、SECO、Silex、NEXCOM、MassRobotics 类伙伴合作。
- 针对 EU / US / healthcare / factory / public-sector 提供 region pack。
- 不和 NVIDIA 打纯 TOPS 战，而是卖低功耗、连接、生命周期和 production deployment path。

## Product Modules

### 1. Partner Graph

- Partner profile。
- 地区、行业、应用、机器人类型。
- 认证等级。
- 培训记录。
- 过往项目证据。
- 可服务 SLA。
- 可支持硬件 / 软件 / connector。

### 2. Recipe Library

- Warehouse AMR。
- Machine tending。
- Palletizing / depalletizing。
- Factory inspection。
- Lab sample handling。
- Education / developer kit。
- Jetson / RK / RPi to Dragonwing migration。

每个 recipe 都包含 BOM、传感器、EOAT、RobotCoreOS image、QNN model asset、ROS 2 graph、OpsConnector template、SafetyOps gate 和 acceptance test。

### 3. FAT / SAT Runner

- 测试步骤。
- 照片 / 视频证据。
- 见证签名。
- 安全测试。
- cycle-time / throughput test。
- punch list。
- retest history。
- final acceptance packet export。

### 4. Handover Binder

自动生成交付包：

- site survey。
- risk assessment。
- standards crosswalk。
- commissioning report。
- safety validation。
- operator training。
- maintenance plan。
- open punch list。
- change history。
- AI Hub / edge runtime evidence。

### 5. Field Service Pack

- installed-base registry。
- service case。
- spare part recommendation。
- remote triage。
- SLA timer。
- customer portal。
- CMMS / ITSM export。
- model / robot / map / firmware change management。

## Competition Demo

初赛和复赛可以展示一个“从比赛 demo 到可交付项目”的流程：

1. 客户选择 LabForgePilot 或 warehouse AMR recipe。
2. IntegratorForge 生成 readiness audit 和 project scope。
3. 系统匹配 certified integrator。
4. recipe 自动带出 BOM、RobotCoreOS image、OpsConnector template、SafetyOps gate、EdgeRuntimeBench。
5. FAT / SAT Runner 展示验收步骤、照片证据、签名和 punch list。
6. Handover Binder 导出项目交付包。
7. Field Service Pack 创建 SLA、备件和远程支持流程。

这个 demo 很适合评委，因为它把技术创新、商业落地和 Qualcomm 生态价值连在一起。

## Why Qualcomm Should Care

Qualcomm 已经有 reference design、AI Hub、FoundriesFactory、Edge Impulse、Arduino、Dragonwing Robotics Hub 和 Partner Network。缺口不是“再做一个板子”，而是让更多开发者、集成商和企业客户能把 Dragonwing edge 真正装进机器人项目。

IntegratorForge 的高通价值：

- 让 SI 在 recipe 里默认选用 Dragonwing / RB / QCS target。
- 把 AI Hub / QNN / EdgeRuntimeBench 变成交付证据。
- 降低 Qualcomm 支持成本，因为认证伙伴和模板承担大量现场问题。
- 把高校 / maker / Jetson / RK / RPi 项目转化为 Dragonwing migration candidates。
- 通过 partner channel 形成更强 design-in pull-through。

一句话：

> IntegratorForge turns Qualcomm robotics from reference designs into repeatable deployments.

## Sources

- Precedence Research robotics system integration：https://www.precedenceresearch.com/robotics-system-integration-market
- IFR World Robotics 2025：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- MIT Sloan collaborative robots integration：https://mitsloan.mit.edu/ideas-made-to-matter/how-smaller-firms-can-harness-potential-collaborative-robots
- Universal Robots UR+ marketplace：https://www.universal-robots.com/marketplace/
- MiR partner program：https://mobile-industrial-robots.com/contacts/become-a-partner
- FANUC integrators：https://www.fanucamerica.com/integrators
- Yaskawa Motoman partners：https://www.motoman.com/en-us/integration/partners
- Rockwell system integrator partners：https://www.rockwellautomation.com/en-us/company/partnernetwork/system-integrator-partners.html
- ANSI/A3 R15.06-2025 update：https://www.ishn.com/articles/115129-part-3-of-ansi-a3-r1506-2025-robot-safety-standard-now-available-for-purchase
- OSHA robotics standards：https://www.osha.gov/robotics/standards
- ISA-105 standards：https://www.isa.org/standards-and-publications/isa-standards/isa-105-standards
- Locus RaaS：https://locusrobotics.com/why-locus/robots-as-a-service
- Brightpick RaaS：https://brightpick.ai/resources/how-brightpicks-raas-works/
- Mujin integrator partner program：https://mujin-corp.com/resources/news/mujin-partners-with-leading-integrators-to-expand-adoption-of-its-robotics-operating-system
- Qualcomm Partner Network：https://www.qualcomm.com/support/partner
- Qualcomm Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Qualcomm FoundriesFactory：https://www.qualcomm.com/developer/software/foundriesfactory
- Dragonwing IQ10 robotics reference design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
