# RevenueStack Pitch

更新时间：2026-07-07。机器人商业化、RaaS 价格、融资租赁、发票/税务、收入确认、数据合规和平台生态变化很快；正式提交、路演或客户交付前必须重新核对目标市场、合同、会计、质保、渠道和合规边界。

## One-Line Pitch

> RevenueStack 把机器人从一次性硬件销售，变成可定价、可授权、可计量、可续费、可融资的劳动力账户。

机器人公司今天缺的不是又一个 billing tool，而是从 `robot event -> customer value -> invoice -> partner payout -> revenue evidence` 的商业记录系统。RevenueStack 是面向机器人 OEM / RaaS / SI / 渠道的收入操作系统，补上 Qualcomm `prototype-to-production` 之后的 `production-to-revenue` 层。

## Required Deck Spine

### 01 · Problem

机器人 demo 越来越容易，机器人公司赚钱越来越难。

- 硬件价格快速下探，买方不想为“机器”付高价，只愿为产能、节省人工、稳定 uptime 和责任边界付费。
- 从 1 台 demo 到 10-500 台部署时，报价、租赁、RaaS、技能包、云训练积分、质保、SLA、渠道佣金和收入确认同时爆炸。
- 一台机器人真实做了多少工作，通常没有进入计费系统；自主小时、任务数、配送、巡检点、抓取次数、远程接管、训练 GPU minutes 和 SLA 事件都散在运维日志里。
- CEO 看不到哪类机器人真的赚钱，CFO 看不到 ARR、deferred revenue、usage revenue、warranty liability、partner payout 和 renewal expansion。
- 中国市场还要处理项目采购、经销商/SI 交付、e-fapiao、押金/租赁/活动短租、现场运维和本地数据边界；海外市场还要处理 RaaS、ERP/e-invoice、Data Act/GDPR 和保险/融资材料。

### 02 · Current Alternatives Fail

现有工具各管一段，但没有谁理解“机器人收入对象”。

- ERP / NetSuite / Oracle 管 BOM、订单和会计，但不理解 robot serial、技能授权、QNN profile、现场 SLA、替换机和任务证明。
- Stripe / Metronome 能做 usage billing、credit wallet 和 entitlement，但默认对象是 SaaS feature，不是机器人、传感器、BOM revision、保修责任和渠道安装里程碑。
- Fleet dashboard 能看在线率、任务状态和故障，但通常不会自动生成 quote、invoice、dealer payout、SLA credit、rev-rec handoff 和续费预测。
- Hardfin 等 HaaS/RaaS finance ops 证明融资运营是真痛点，但机器人公司还需要技能商店、云训练积分、Qualcomm edge evidence 和多方分账。
- UR+、MiR Go、Viam Registry、Unitree/OpenMind robot app stores 证明生态价值，但 OEM 仍需要自己的授权、兼容性、结算和支持责任账本。
- 表格在 1-5 台试点能撑住；进入多站点、多 SKU、多技能、多渠道后，漏收费、错分账、错开票、错承诺 SLA 都会变成毛利黑洞。

### 03 · Solution

RevenueStack = 机器人公司的收入操作系统。

它把“机器人干了什么”变成“客户该付什么、伙伴该分什么、公司该确认什么收入、哪条证据支持这笔收入”。

四个核心 ledger：

1. Product Ledger：hardware SKU、BOM revision、robot serial、payload、firmware、skill package、cloud credit、fleet plan、SLA、warranty、price book。
2. Entitlement Ledger：customer、site、fleet、robot、skill、quota、effective dates、install policy，回答“这台机器人现在能用什么”。
3. Usage Ledger：autonomy hours、tasks、picks、deliveries、inspection points、teleop minutes、inference minutes、training GPU-minutes、data GB、SLA incidents。
4. Revenue Ledger：contract、fapiao/invoice、usage、prepaid credits、warranty obligations、partner payout、delivery event、rev-rec schedule。

一句话：RevenueStack 是 `quote-to-cash + usage-to-bill + profile-to-marketplace + evidence-to-finance` 的机器人商业控制面。

### 04 · Why Now

RaaS、机器人技能商店和 edge AI 量产路径在 2025-2026 同时成熟。

- IFR 2025 service robots 报告显示，2024 年专业服务机器人销量接近 20 万台，RaaS fleet 增长 31%，transport/logistics RaaS 增长 42%。
- IFR 2025 industrial robots 报告显示，中国 2024 年新增工业机器人安装约 29.5 万台，占全球 54%；中国既是最大机器人需求市场，也是最需要可复制商业模型的市场。
- Formic、Locus、Knightscope、Serve Robotics、Sproutmation、RobotLAB 等案例说明：机器人正从 CapEx 设备变成包含部署、软件、维护、支持、SLA 和升级的月度服务。
- Unitree、OpenMind、UR Marketplace、MiR Go、Viam Registry 说明：机器人生态正在向 App Store / package registry / certified component 模式移动。
- Viam、Transitive、Double Robotics 等已公开 per-robot/month、usage-based、cloud credits、capability-by-capability pricing，说明机器人软件计费正在被市场教育。
- Qualcomm 正在强调 Dragonwing 从 prototype 到 production；RevenueStack 把生产级 profile、QNN/QAIRT 证据、Partner Network 和渠道 SKU 接到 revenue attach。

### 05 · Product

第一批 ICP：正在从 paid pilot 走向 10-500 台部署，并通过经销商、SI、RaaS、租赁或海外渠道销售机器人的 OEM。

产品模块：

- Robotics CPQ：硬件、BOM、payload、安装、训练积分、技能包、SLA、租赁、买断、押金、渠道折扣和行业模板。
- Robot Account：customer、site、fleet、robot serial、owner、operator、lease status、subscription、warranty、data lane。
- RaaS / Lease Billing：按月、按小时、按任务、按配送、按巡检点、按亩、按 tote、按节省金额、按事件短租计费。
- Skill Store & Entitlement：技能包、兼容 BOM、Qualcomm AI Hub/QNN profile、license、trial、canary、usage meter、开发者分成。
- Cloud Training Credits：LeRobot 数据集、训练任务、GPU minutes、simulation steps、model eval、edge export、credit burn-down。
- SLA / Warranty Ops：保修、延保、备件、远程支持、现场派单、替换机、RMA、service credit 和收入确认数据。
- Partner & Fapiao / Invoice：经销商/SI deal registration、佣金、结算、e-fapiao、EU e-invoice、US ERP/PDF/ACH adapters。
- Finance Dashboard：ARR、usage revenue、gross margin、deferred revenue、warranty liability、partner payout、renewal expansion、fleet payback。

中国版必须 fapiao-native、partner-native、project-procurement-native、本地数据优先；海外版必须 RaaS-native、ERP/e-invoice-native、data-rights-aware、insurance/finance-ready。

### 06 · Product API/Evidence

投资人和评委需要看到它不是“财务概念”，而是一组能演示的机器人商业 API。

关键对象：

- `SKU`: hardware、component、skill、cloud_credit、fleet_plan、warranty、SLA、service、marketplace_app。
- `BOM`: parent_sku、revision、component_sku、quantity、serial_required、firmware_min、warranty_policy。
- `RobotAccount`: serial、customer、site、fleet、owner、operator、lease_status、warranty、data_region。
- `SkillPackage`: version、publisher、runtime、required_capabilities、compatible_bom_revisions、pricing_dimensions、install_policy。
- `EdgeProfile`: device、model、QAIRT/QNN version、latency、memory、power、accuracy、profile_date、support_boundary。
- `UsageMeter`: event_name、unit、aggregation、dimensions、included_quota_source、overage_price。
- `SLAWarrantyLedger`: robot_serial、covered_components、response_time、uptime_commitment、RMA、service_credit_policy。
- `DealerSIChannel`: partner、territory、certifications、deal_registration、margin_policy、settlement_account。

核心 API：

```text
POST /v1/skus
POST /v1/boms
POST /v1/robots/{serial}/activate
POST /v1/entitlements/grant
GET  /v1/entitlements/check
POST /v1/skills/{package_id}/deployments
POST /v1/edge-profiles
POST /v1/meter-events
GET  /v1/usage/summary
POST /v1/training-jobs
POST /v1/subscriptions
POST /v1/bill-runs
POST /v1/revenue/fulfillment-events
POST /v1/app-store/listings
POST /v1/channel/deal-registrations
POST /v1/invoices/fapiao
```

Evidence pack：

- `Inspection Pro v3` 只有在 robot capabilities、BOM revision、ODD、安全门禁、Qualcomm AI Hub/QNN profile、latency/memory/power 指标、support boundary 都满足时才能上架。
- 每次任务产生 `meter_event`，每次故障产生 `service_event`，每次训练产生 `credit_event`，月底形成 bill run、partner payout、warranty reserve 和 renewal forecast。
- 这让 Qualcomm edge profile 从工程 artifact 变成商业 gating field：没有可复现 profile，就不能被采购、上架、分账或承诺 SLA。

### 07 · Market & Business Model

RevenueStack 不从“所有机器人公司”开始，从最痛的商业化阶段切入：paid pilot 后、规模部署前。

买方：

- Robot OEM：硬件毛利下滑，需要软件、技能、SLA、数据和服务续费。
- RaaS / leasing operator：需要资产、利用率、维护历史、保险、残值、回收和融资材料。
- Distributor / SI：需要渠道报价、deal registration、deployment milestone、验收材料、续费和分账。
- Enterprise customer：需要 ROI、uptime proof、服务责任、数据边界和采购可解释性。
- Qualcomm / module partners：需要把 dev kit、AI profile、reference design、SI 和 OEM SKU 变成持续 attach。

商业模式：

- 中国 Starter：RMB 3k-20k / month，10-100 台机器人，基础 CPQ、订阅、用量、e-fapiao、partner portal。
- 中国 Growth：RMB 100k-500k / year，渠道、RaaS、质保、私有化、本地云/模型计费、招投标/验收材料。
- 海外 Startup：$999-$5k / month + active robot fee。
- 海外 Scale：$25k-$150k / year + usage metering volume。
- Enterprise：$150k-$500k / year，audit、ASC 606/842 handoff、dealer/channel、private marketplace、warranty automation。
- GMV take rate：0.5%-2%；skill marketplace / channel rev share：10%-25%；training credit / cloud lane margin：按项目或消耗分成。

### 08 · Competition & Moat

竞争不是“有没有计费工具”，而是谁能成为机器人收入事实表。

替代方案：

- Stripe / Metronome：usage billing、credit wallets、entitlements、revenue recognition。
- ERP / NetSuite / Oracle：BOM、订单、库存、会计。
- Hardfin：hardware / RaaS finance ops。
- AWS Marketplace / SaaS marketplace：contracts、metering、private offers。
- Viam / Formant / Boston Dynamics Orbit：robotics / fleet platform。
- UR+ / MiR Go / Viam Registry / Intrinsic / Unitree / OpenMind：ecosystem、registry、robot app store。

壁垒：

- Robot revenue schema：BOM、serial、skill、training credit、warranty、lease、usage、partner payout 在同一数据模型。
- Telemetry-to-invoice：真实 robot task 直接生成 overage、SLA credit、renewal expansion 和 gross-margin evidence。
- Profile-to-marketplace：Qualcomm AI Hub/QNN/QAIRT profile 变成 skill listing、采购和支持责任的商业门槛。
- Vertical contract templates：仓储、餐饮、医疗、安防、农业、教育、人形的 RaaS / lease / task pack / SLA 模板沉淀。
- Partner network effects：技能开发者、SI、dealer、leasing partner、insurer 围绕同一套 entitlement 和 payout 增长。
- System of record：一旦成为 quote-to-cash、usage-to-bill、renewal 和 finance diligence 的记录源，迁移成本高。

### 09 · Why Qualcomm

Qualcomm 的机会不是只卖开发板，而是占据开发板周围的收入层。

Revenue attach chain：

`Dragonwing/RB3 starter kit -> LeRobot dataset -> cloud training credits -> AI Hub/QNN/QAIRT profile -> validated edge package -> certified skill listing -> fleet runtime subscription -> IQ/Dragonwing production SKU`

对 Qualcomm 的价值：

- Qualcomm 正在把非手机业务、IoT、industrial/networking/robotics 作为增长重点；RevenueStack 直接服务“机器人商业化”这一收入目标。
- Dragonwing 已经覆盖从开发板、AI Hub、Edge Impulse、Foundries.io 到 lifecycle management 的 prototype-to-production 路径；RevenueStack 补上 production-to-revenue。
- RB3 / QCS6490 可以作为 demo 起点，IQ / Dragonwing production hardware 作为规模化目标；同一份 revenue account 记录 profile、SKU、skill、SLA 和续费。
- AI Hub/QNN/QAIRT profile 变成销售资产：每个模型都有 device、runtime、latency、memory、power、accuracy 和 support boundary。
- Partner Network 可以通过 RevenueStack 获得共同的 catalog、deal registration、profile evidence、SI payout 和 marketplace rev share。
- 竞争 framing：NVIDIA sells the robot brain; RevenueStack helps Qualcomm sell the efficient edge robot business system.

### 10 · Demo & Ask

7 分钟演示：机器人跑一次任务，收入系统自动闭环。

1. Dealer 配置 20 台巡检机器人报价：硬件、Inspection Pro 技能、10k 训练积分、3 年 SLA、渠道折扣。
2. 扫描 robot serial 激活 fleet：BOM revision、firmware、payload、warranty、customer、site、subscription、data region。
3. 安装付费技能：校验 robot capability、BOM compatibility、AI Hub/QNN profile、entitlement，canary 到 2 台。
4. 机器人跑任务：3 hours uptime、182 tasks、12 skill calls、40 training-credit minutes、SLA green。
5. 售后事件：一台 lidar fault，ledger 生成 warranty check、RMA、dealer dispatch、service credit risk。
6. Bill run：subscription、usage overage、training-credit burn-down、app-store rev share、dealer commission、fapiao/invoice、rev-rec schedule。
7. Finance dashboard：ARR、usage revenue、deferred revenue、warranty liability、partner payout、renewal expansion。

对 Qualcomm 的请求：

- 6-8 周 `Dragonwing Revenue Attach Sprint`。
- RB3 / QCS6490 demo target；IQ / Dragonwing reference design 作为 production-forward profile。
- AI Hub + QNN quota for 2-3 reference skills。
- Joint `Dragonwing Skill Profile v0.1`：profile fields、support boundary、listing requirements。
- Intro path to module partners、SI partners、education channels、RaaS/leasing partners。
- 允许谨慎使用 `Dragonwing-profiled` 或 `Qualcomm-edge-ready candidate`，不声称官方认证或正式合作。

## Claim Guardrails

- 不承诺替代客户 ERP/财务系统；RevenueStack 是机器人商业对象层，可与 ERP/Stripe/NetSuite 集成。
- 不给正式会计、税务、收入确认、数据出境或招投标法律意见；只说提供数据和流程支持。
- 不把 `Dragonwing-profiled` 说成官方安全认证或官方合作。
- 不说所有技能都能自动上架；需要兼容性、profile、支持责任、安全边界和风险审查。
- 不把 RaaS 描述成一定降低成本；必须基于 utilization、support cost、融资成本和客户场景计算。

## Sources

- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Formic RaaS：https://formic.co/resources/articles/robots-as-a-service-raas
- Formic fact sheet 2025：https://www.datocms-assets.com/43704/1744224995-formic-fact-sheet-2025-3.pdf
- Locus RaaS：https://locusrobotics.com/why-locus/robots-as-a-service
- Locus 7B picks：https://locusrobotics.com/blog/seven-billion-picks-warehouse
- RobotLAB store：https://www.robotlab.com/store/
- Sproutmation RaaS：https://sproutmation.com/solutions/raas
- PUDU / Deloitte service robot white paper：https://www.deloitte.com/cn/en/Industries/energy/perspectives/open-full-stack-intelligent-service-robot-ecosystem.html
- PUDU 2025 shipments：https://www.pudurobotics.com/en/news/pudu-robotics-scaled-120000-units-100-percent-growth-2025
- People Daily China rental robots：https://en.people.cn/n3/2026/0303/c98649-20430652.html
- UR Marketplace：https://www.universal-robots.com/marketplace/
- MiR Go：https://mobile-industrial-robots.com/products/mir-go
- Viam pricing：https://www.viam.com/pricing
- Viam registry：https://www.viam.com/post/announcing-the-viam-modular-registry
- Transitive Robotics capabilities：https://transitiverobotics.com/caps/
- Unitree Explore App：https://apps.apple.com/us/app/unitree-explore-robot/id6778743889
- OpenMind robot app store：https://roboticsandautomationnews.com/2026/02/02/openmind-launches-app-store-for-robots/98554/
- Hardfin robotics：https://www.hardfin.com/industries/robotics
- Stripe Entitlements：https://docs.stripe.com/billing/entitlements
- AWS Marketplace SaaS contracts：https://docs.aws.amazon.com/marketplace/latest/userguide/saas-contracts.html
- Qualcomm diversification strategy：https://www.qualcomm.com/news/releases/2026/06/qualcomm-accelerates-diversification-with-comprehensive-strategy
- Qualcomm Dragonwing portfolio：https://www.qualcomm.com/news/onq/2025/02/unveiling-the-qualcomm-dragonwing-brand-portfolio
- Qualcomm edge AI prototype to deployment：https://www.qualcomm.com/developer/blog/2026/05/edge-ai-prototype-deployment-qualcomm-dragonwing-developer-ecosystem
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm QNN SDK：https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk
- Qualcomm Partner Network：https://www.qualcomm.com/support/partner/iot
