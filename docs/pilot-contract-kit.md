# PilotContractKit Pitch

更新时间：2026-07-06。

## One-Line Thesis

PilotContractKit 是机器人试点的商业操作系统：把 robot demo 变成采购、运营、安全、IT、法务和工程都能审查的 paid pilot，再把 paid pilot 变成 rollout contract。

> We turn robot demos into paid pilots, and paid pilots into rollout contracts.

中文主张：

> 企业不是不想试机器人，是不知道怎样低风险购买一次可验收试点。

## 01 · Problem

机器人公司能做 demo，但企业不能采购“一个看起来不错的 demo”。

企业内部的真实问题是：

- Procurement：价格、取消权、扩张价、CapEx/OpEx、供应商风险、付款条件。
- Operations：baseline、throughput、intervention、uptime、punch list、班次影响。
- IT/OT：视频、遥测、远程访问、网络分段、云区域、保留期限、日志。
- Safety/EHS：急停、防护、人工监督、stop-work authority、rollback、现场边界。
- Legal/Insurance：数据权利、责任限制、工伤/财损、保险、出口/制裁、隐私。
- Engineering：dataset、训练版本、edge profile、latency、温度、功耗、可复现。

所以机器人商业化的瓶颈正在从“机器人能不能动”变成“这个试点能不能被批准、验收和扩张”。

## 02 · Current Alternatives Fail

现有工具让机器人更容易卖，但没有形成中立的 pilot acceptance layer。

- RaaS vendors：Formic、Locus、Brightpick、inVia、Vecna 能把自家或合作 stack 做成月费服务，但通常绑定特定机器人、场景或商业模式。
- Robot sourcing marketplaces：HowToRobot、RBTX、Alibaba-style listings 帮买方找供应商和报价，但 discovery 不是 bankable pilot。
- OEM ecosystems：UR+、FANUC CRX、ABB、KUKA 降低某个 OEM orbit 内的技术集成风险，但不统一跨厂商 KPI、付款、数据权利和扩张条款。
- RobOps / fleet tools：Formant、Viam、Foxglove、InOrbit 强在运营、遥测、调试和 fleet orchestration，不是采购、融资、合同或 success arbitration layer。
- System integrators：能现场交付，但每个项目都重新写 SOW、验收、风险边界、数据条款和扩张报价，复用度低。

PilotContractKit 不替代这些角色。它把它们的证据翻译成买方能签字的试点语言。

## 03 · Solution

PilotContractKit 是机器人付费试点的 neutral commercial operating system。

它把一次 4-8 周轻量试点，或 60-90 天复杂现场试点，组织成可采购工作包：

1. `Pilot SOW`：范围、site/zone、robot count、task、排除项、RACI、deliverables、timeline、price。
2. `Baseline Pack`：人工流程、周期、劳时、错误率、停机、当前成本、订单/SKU mix、site constraints。
3. `KPI Scorecard`：throughput、quality、autonomy、uptime、integration、safety、edge evidence、ROI。
4. `FAT/SAT Protocol`：requirements traceability、test scripts、evidence pack、punch list、retest/signoff。
5. `Risk Boundary`：safety、operating envelope、supervision、change control、data/privacy、cyber/OT、insurance。
6. `Qualcomm Evidence`：BoardBringupKit packet、EdgeRuntimeBench report、AI Hub/QNN/ONNX artifact、rollback。
7. `Scale Decision Memo`：go/no-go、rollout price、RaaS/monthly option、support SLA、fleet/industry pack path。

它不是法律合同生成器，不是安全认证，不是合规结论。它是试点证据和风险分配的组织层。

## 04 · Why Now

机器人 adoption 已经不是科幻，但采购更理性。

- IFR：2024 年全球新增工业机器人约 542,000 台，全球运行存量约 4.664M 台；中国新增约 295,000 台。
- IFR：2024 年专业服务机器人销量接近 200,000 台，RaaS fleet 增长约 31% 到 24,500+ 台。
- A3：2025 年北美机器人订单增长 6.6% 到 36,766 台，价值约 $2.25B；cobots 占 19.6%。
- A3：2026 Q1 北美 life sciences/pharma/biomed、semiconductors/electronics、food/consumer goods 和 cobots 增长明显。
- MHI/Deloitte：供应链买方有技术预算，但需要 proof、ROI、risk allocation 和 rollout plan。
- 中国机器人供给、政策和硬件速度强，但海外买方更重视 KPI、liability、SLA、数据边界和 reference evidence。

结论：市场不缺机器人 demo，缺的是把 demo 变成 paid pilot 的采购格式。

## 05 · Product

PilotContractKit 的产品不是模板文档，而是 pilot generator + evidence binder + scale router。

核心模块：

- `Pilot SOW Builder`：scope、assumptions、exclusions、site readiness、interfaces、deliverables、RACI。
- `Baseline Data Pack`：2-4 周代表性数据、measurement calendar、variance controls、manual process map。
- `KPI Scorecard`：operational KPIs 与 robot KPIs 分开，定义 target bands、pass/fail、exceptions。
- `ROI / Payback Model`：CapEx vs RaaS、labor、throughput、quality、maintenance、ramp-up、sensitivity。
- `FAT/SAT Protocol Generator`：requirements -> test scripts -> evidence -> punch list -> retest -> signoff。
- `Support SLA Addendum`：uptime definition、response time、maintenance、spares、remote access、downtime attribution。
- `Safety/Data/Cyber Addendum`：site risk prompts、training/signoff、data map、retention、MFA/RBAC、OT segmentation。
- `Qualcomm Evidence Binder`：board bring-up、model artifact、compile/profile、latency/power/thermal、rollback。
- `Scale Decision Memo`：go/no-go、production readiness、rollout pricing、RevenueStack handoff。

## 06 · Evidence Objects

PilotContractKit 把技术证据转成付款、验收和扩张证据。

- `pilot-sow.md`：customer、site、task、timeline、deliverables、assumptions、exclusions、price。
- `baseline-data-request.xlsx`：process map、task frequency、cycle time、labor hours、quality errors、downtime。
- `acceptance-scorecard.json`：metric、baseline、target、measurement method、test window、owner、pass/fail。
- `fat-sat-protocol.md`：requirements, test script, evidence artifact, punch-list owner, retest status。
- `risk-boundary.md`：operating envelope、safety assumptions、supervision、change control、stop conditions。
- `data-rights-addendum.md`：video、telemetry、production data、retention、training rights、cross-border review。
- `support-raci.md`：customer、OEM、SI、cloud、robot operator、spares、remote diagnostics、escalation。
- `qualcomm-edge-evidence.zip`：board manifest、AI Hub/QNN profile、runtime report、SafetyOps gate、rollback record。
- `scale-decision-memo.md`：ROI、payback、risk residuals、rollout quote、RaaS option、next-stage contract path。

## 07 · Market & Business Model

买方不是“想看机器人”的人，而是要把试点批下来的人。

中国版：

- ICP：AMR、cobot、仓储机器人、实验室自动化、工业巡检、清洁、服务机器人创业公司和 SI。
- 痛点：硬件快、价格卷、demo 多，但试点材料、SLA、数据边界、保险语言和海外采购材料弱。
- 入口：¥3万-15万 scoping + ¥30万-100万 paid pilot package + SI/OEM 成交分成。

海外版：

- ICP：warehouse、factory、lab、food/CPG、life sciences、semiconductor/electronics 的自动化负责人和 integrator。
- 痛点：劳动力短缺、预算存在，但要求 baseline、ROI、safety、cyber、insurance、liability、support、rollout option。
- 入口：$10k-50k pilot readiness sprint + $50k-250k pilot package + transaction/success fee + annual evidence subscription。

后续收入：

- SI/OEM 模板 licensing。
- Telemetry-backed milestone payment rails。
- Pilot benchmark database。
- Financing / warranty / insurance underwriting evidence。
- RevenueStack handoff：RaaS、subscription、support、usage metering、expansion quote。

## 08 · Competition & Moat

PilotContractKit 不是 RaaS vendor、lead marketplace、fleet dashboard 或法律事务所。

竞争/邻近类别：

- RaaS：让单一 stack 更可买，但不中立。
- Marketplaces：帮找供应商，但不承担 pilot success language。
- OEM ecosystems：降低某一生态技术风险，但不统一跨厂商商业验收。
- RobOps tools：提供 telemetry，但不直接决定付款、责任和扩张。
- Integrators：能交付，但模板化和数据化 pilot knowledge 弱。

护城河：

- `Pilot Knowledge Base`：场景、任务、KPI、失败类型、site readiness、punch list、rollout patterns。
- `Telemetry-Backed Acceptance`：把 Formant/Viam/Foxglove/InOrbit/vendor APIs 的数据变成 milestone evidence。
- `Cross-Vendor Benchmark`：不同机器人/任务/场地的 cycle time、intervention、deployment duration、ROI、support burden。
- `Risk Clause Library`：safety, data, cyber, insurance, support, change control, stop conditions。
- `Buyer Trust`：不卖某台机器人，先站在试点能不能被验收的中立位置。
- `Qualcomm Evidence Default`：每个试点都留下可复用 edge profile 和 board/runtime evidence。

## 09 · Why Qualcomm

PilotContractKit 把 Qualcomm 从 competition hardware 变成 paid pilot 的 evidence standard。

Portfolio connection：

- `LabForgePilot`：给客户试点场景和真实任务。
- `BoardBringupKit`：证明 Qualcomm target board、camera、sensor、I/O、runtime image ready。
- `EdgeRuntimeBench`：生成 latency、p95/p99、memory、thermal、power、runtime path、rollback 证据。
- `DualCloudOps`：证明本地优先，只有成本、隐私、模型体积或 latency 需要时才走云。
- `SafetyOps`：把 hazard、mitigation、rollback、OTA、privacy、security 变成 gate。
- `RevenueStack`：把 BOM、margin、pilot price、subscription、SLA 和 rollout quote 连起来。

Qualcomm 的战略收益：

- 让 Dragonwing/AI Hub/QNN/QAIRT 出现在采购验收表里，而不只在 demo 终端里。
- 给 FAE、开发者生态和合作伙伴一套“prototype to paid pilot”的证据格式。
- 帮 QCS6490/QCS8550/RB3/未来 IQ10 RRD 进入 robot OEM/SI/customer procurement flow。
- 把 Qualcomm edge evidence 和 LeRobot/CloudTwin 训练链路绑定成商业标准。

## 10 · Demo & Ask

三分钟 demo 要证明：一个 robot task 可以从 demo 进入可采购 paid pilot。

Demo flow：

1. 0:00-0:20：选择 LabForgePilot 或 FactoryPilot，展示客户痛点、Qualcomm target、timeline、price anchor。
2. 0:20-0:50：生成 Pilot SOW：scope、baseline、KPI、site boundary、RACI、deliverables、exclusions。
3. 0:50-1:20：BoardBringupKit 证据：OS/kernel/runtime、camera/sensor check、NPU/runtime availability、network/OTA。
4. 1:20-1:55：EdgeRuntimeBench 证据：policy artifact、AI Hub/QNN/ONNX status、p95 latency、memory、thermal、rollback。
5. 1:55-2:25：SafetyOps + DualCloudOps：safety gate、data boundary、local-first routing、fallback reason。
6. 2:25-2:50：RevenueStack：pilot price、support SLA、success gate、rollout / RaaS / subscription path。
7. 2:50-3:00：导出 `pilot-contract-audit-pack.zip`。

Ask Qualcomm：

- QCS8550/QCS6490/RB3/VENTUNO Q target hardware or partner validation path。
- AI Hub Workbench / device cloud credits。
- QNN/QAIRT profiling guidance and FAE review。
- Qualcomm Linux/robotics office hours for camera, runtime, OTA, watchdog。
- Permission to publish as a Dragonwing Robotics Hub reference pilot workflow。
- Introductions to APLUX, Radxa, Thundercomm, Advantech, robotics integrators, education partners, and one design-partner pilot。

## Risk Boundary

PilotContractKit helps define pilot scope, operating envelope, role allocation, data terms, cyber controls, insurance requirements, and stop conditions. It does not certify compliance with OSHA, ISO, ANSI/RIA, CE, China GB standards, EU AI Act, export controls, or any other regulatory regime.

Each pilot still needs site-specific safety assessment, local legal review, insurance review, and customer approval before operation.

Avoid claims:

- certified safe。
- OSHA/ISO/CE/AI Act compliant。
- export-control cleared。
- China-ready data transfer。
- cloud dashboard as safety-rated control system。
- replacement for counsel, safety integrators, insurers, regulators, or customer approval。

## Sources

- IFR industrial robots 2025：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots growth：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- IFR service robots executive summary：https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Service_Robots.pdf
- A3 2025 robot orders：https://www.automate.org/robotics/news/robot-orders-grow-6-6-in-2025-as-general-industries-drive-broader-automation-adoption
- A3 Q1 2026 robot orders：https://www.automate.org/robotics/news/robot-orders-hold-steady-in-q1-2026-as-demand-broadens-across-non-automotive-industries
- MHI/Deloitte supply chain report：https://www.mhi.org/content/2/2285545/new-mhi-and-deloitte-report-focuses-on-orchestrating-end-to-end-digital-supply-chain-solutions
- Manufacturing workforce shortage：https://themanufacturinginstitute.org/manufacturers-need-as-many-as-3-8-million-new-employees-by-2033/
- China AI-powered robots strategy：https://ifr.org/ifr-press-releases/news/china-makes-ai-powered-robots-core-of-national-strategy
- SAP SOW guide：https://www.sap.com/resources/what-is-statement-of-work-sow
- Locus AMR ROI：https://locusrobotics.com/blog/true-roi-autonomous-mobile-robots
- Locus warehouse automation PoC：https://locusrobotics.com/blog/warehouse-automation-poc
- WAKU PoC KPI guide：https://www.waku-robotics.com/en/robot-journey/robot-operations/initial-proof-of-concept-on-site-test/poc-define-kpis
- FAT/SAT commissioning overview：https://appliedintegration.co.uk/capabilities/project-lifecycle-services/test-fat-sat-commissioning/
- Formic full-service automation：https://formic.co/full-service-automation
- Locus RaaS：https://locusrobotics.com/why-locus/robots-as-a-service
- Brightpick：https://brightpick.ai/
- inVia RaaS：https://inviarobotics.com/robotics-as-a-service/
- Vecna RaaS：https://www.vecnarobotics.com/the-vecna-system/move-faster-with-raas/
- HowToRobot procurement risk：https://howtorobot.com/expert-insight/customers-pay-price-when-robot-projects-go-wrong
- UR+ marketplace：https://www.universal-robots.com/marketplace/
- FANUC CRX devices：https://crx.fanucamerica.com/cobot-devices
- ABB Robotics ecosystem：https://www.abb.com/global/en/areas/robotics/products/equipment/ecosystem
- Foxglove：https://foxglove.dev/
- Formant fleet observability：https://docs.formant.io/docs/fleet-observability
- Viam：https://www.viam.com/
- InOrbit unified command：https://www.inorbit.ai/unified-command
- OSHA robotics：https://www.osha.gov/robotics
- OSHA robotics technical manual：https://www.osha.gov/otm/section-4-safety-hazards/chapter-4
- A3/ANSI R15.06-2025 update：https://www.automate.org/industry-insights/ansi-a3-publish-revised-r15-06-industrial-robot-safety-standard
- NIST CSF 2.0：https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- NIST SP 800-82 Rev. 3：https://csrc.nist.gov/pubs/sp/800/82/r3/final
- EU AI Act：https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- China PIPL English text：https://en.spp.gov.cn/2021-12/29/c_948419.htm
- China cross-border data rules：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm edge AI prototype to deployment：https://www.qualcomm.com/developer/blog/2026/05/edge-ai-prototype-deployment-qualcomm-dragonwing-developer-ecosystem
- Qualcomm Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm Linux 2：https://www.qualcomm.com/developer/blog/2026/06/qualcomm-linux-2-now-available
