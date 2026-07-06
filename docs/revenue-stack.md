# RevenueStack Pitch

更新时间：2026-07-06。机器人商业化、RaaS 价格、融资租赁、会计处理和平台生态变化很快；正式提交和客户交付前必须重新核对目标市场、税务/发票、收入确认、租赁会计、质保责任和渠道合同。

## One-Line Pitch

> 机器人不是一次性卖货，而是持续产生现金流的劳动力。

RevenueStack 是机器人公司的收入操作系统：把硬件、租赁、技能、云训练、SLA、渠道和用量计费变成可定价、可授权、可计量、可开票、可分账、可确认收入的系统。

## Required Deck Spine

### 01 · Problem

机器人越来越便宜，但机器人公司还在用卖硬件的方式赚钱。

- 硬件收入一次性，容易被价格战和售后成本吃掉。
- 客户想买 outcome：更高产能、更少人工、更稳定 uptime，而不是一堆零散设备。
- 试点没有升级路径：starter kit、pilot、fleet、industry pack 之间缺报价和续费逻辑。
- 软件技能、云训练、数据回流、远程支持、SLA、租赁、保修、渠道分账没有统一账本。
- 财务看不到真实 ARR、deferred revenue、usage revenue、warranty liability、partner payout 和 expansion。

### 02 · Current Alternatives Fail

ERP、Stripe 和普通 SaaS 计费工具不理解机器人。

- ERP 管物料和订单，但不理解技能订阅、用量计费、训练积分、机器人任务证明和 App Store 分成。
- Stripe / SaaS billing 适合 seat 和 API；机器人还需要序列号、BOM 修订、替换机、保修、SLA 和部署里程碑。
- Fleet dashboard 能看设备在线和任务状态，但不会生成 quote、invoice、revenue recognition、dealer payout 和续费预测。
- Marketplace 证明生态价值，但 robot OEM 仍需要自己的授权、结算、兼容性账本和支持责任。
- Leasing tools 能处理设备租赁，却不理解每台机器人今天跑了多少任务、用了哪个技能、触发了哪种 SLA。
- Spreadsheet 只适合 1-5 台试点；进入 10-500 台部署后，报价、续费、渠道、保修和用量都会失控。

### 03 · Solution

RevenueStack 是机器人公司的收入操作系统。

四个核心 ledger：

1. Product Ledger：SKU、BOM、robot serial、payload、firmware、app-store package、cloud credit pack、service plan、warranty plan、price book。
2. Entitlement Ledger：customer、site、fleet、robot_serial、skill_package、meter、quota、effective_dates，回答“现在能安装/使用什么”。
3. Usage Ledger：autonomy hours、tasks、picks、deliveries、inspection points、teleop minutes、inference minutes、training GPU-minutes、simulation steps、data GB、SLA incidents。
4. Revenue Ledger：合同、发票、用量、质保、预付积分、partner payout 和 delivery events 转成 revenue schedule。

### 04 · Why Now

硬件价格下探、RaaS 扩张和技能生态正在创造机器人 App Store 时刻。

- IFR 报告中国 2024 年新增工业机器人安装约 29.5 万台，占全球 54%。
- IFR 报告 2024 年专业服务机器人销量接近 20 万台，RaaS fleet 增长 31% 至超过 24,500 台。
- 低价人形机器人和开发套件把硬件入口拉低，收入重心转向软件、技能、SLA、数据和服务。
- RaaS、leasing、usage-based work、skill marketplace 和 cloud training credits 正在成为机器人商业化关键词。
- UR+、MiR Go、Viam、Intrinsic 等证明：机器人生态价值来自可验证组件、技能、registry 和 deployment workflow。

### 05 · Product

第一批 ICP：正在从 pilot 走向 10-500 台部署的机器人公司，尤其是通过经销商、SI、RaaS、租赁和海外渠道销售的 OEM。

产品模块：

- Robotics CPQ：硬件、BOM、payload、安装、训练、技能、SLA、租赁、买断和渠道折扣。
- RaaS Billing：按月、按小时、按任务、按配送、按巡检点、按亩、按 tote、按节省金额计费。
- Asset & Lease Ledger：序列号、部署状态、租期、折旧、押金、替换机、退货、买断和保险。
- Skill Store：技能包、QNN profile、兼容 BOM、license、trial、canary、usage meter、开发者分成。
- SLA / Warranty：保修、延保、预防性维护、备件、远程支持、现场派单、service credit 和收入确认。
- Finance Dashboard：ARR、usage revenue、deferred revenue、gross margin、warranty liability、partner payout、renewal expansion。

### 06 · Product API

关键对象：

- `SKU`: hardware、component、skill、cloud_credit、fleet_plan、warranty、sla、service、marketplace_app。
- `BOM`: parent_sku、revision、component_sku、quantity、serial_required、firmware_min、warranty_policy。
- `SkillPackage`: version、publisher、runtime、required_capabilities、compatible_bom_revisions、pricing_dimensions、install_policy。
- `UsageMeter`: event_name、unit、aggregation、dimensions、included_quota_source、overage_price。
- `FleetOpsSubscription`: customer、site、fleet、included robots、autonomy hours、data GB、support tier、addons。
- `SLAWarrantyLedger`: robot_serial、coverage_type、covered_components、response_time、uptime_commitment、service_credit_policy。
- `AppStoreListing`: package、publisher、certification_state、pricing_model、rev_share、install_targets。
- `DealerSIChannel`: partner、territory、certifications、deal_registration、margin_policy、payout account。

核心 API：

```text
POST /v1/skus
POST /v1/boms
POST /v1/robots/{serial}/activate
POST /v1/entitlements/grant
GET  /v1/entitlements/check
POST /v1/skills/{package_id}/deployments
POST /v1/meter-events
GET  /v1/usage/summary
POST /v1/training-jobs
POST /v1/subscriptions
POST /v1/bill-runs
POST /v1/revenue/fulfillment-events
POST /v1/app-store/listings
POST /v1/channel/deal-registrations
```

### 07 · Market & Business Model

买方：

- Robot OEM：硬件价格压力、售后负担、软件/技能/数据无法持续收费。
- End customer：ROI 不确定、CapEx 审批、运维风险、uptime guarantee。
- Distributor / SI：一次性 resale margin、部署责任不清、缺续费和服务账本。
- Education buyer：课程、教师 seat、备件、比赛包、年度支持和多校区 license。
- Finance / leasing partner：需要资产、利用率、服务历史、保险和回收价值数据。

RevenueStack 自身收费：

- 中国 Starter：人民币 3k-20k / month，用于 10-100 台机器人和基础 CPQ/订阅/用量。
- 中国 Growth：人民币 100k-500k / year，加入渠道、RaaS、质保、私有化和国产云/模型计费。
- 海外 Startup：$999-$5k / month + active robot fee。
- 海外 Scale：$25k-$150k / year + usage metering volume。
- Enterprise：$150k-$500k / year for audit, ASC 606/842 handoff, dealer/channel, private marketplace and warranty automation。
- GMV take rate：0.5%-2%；skill marketplace / channel rev share：10%-25%。

### 08 · Competition & Moat

竞争 / 替代：

- Hardfin：hardware/RaaS finance ops。
- Stripe / Metronome：usage billing、credit wallets、revenue recognition。
- ERP / NetSuite / Oracle：BOM、订单、会计。
- AWS Marketplace / SaaS marketplace：contracts、metering、private offers。
- Viam / Formant / Boston Dynamics Orbit：fleet platform。
- UR+ / MiR Go / Viam Registry / Intrinsic Flowstate：robot ecosystem / registry。

壁垒：

- Telemetry + billing：真实机器人任务直接生成 invoice、overage、SLA credit、renewal expansion。
- Contract templates：仓储、餐饮、医疗、安防、农业、人形、教育的 RaaS / lease / task pack 模板。
- Marketplace network：skill developer、SI、dealer、leasing partner、insurer 围绕 entitlement 和 payout 增长。
- Finance graph：硬件交付、订阅履约、用量消耗、预付积分、质保义务和渠道分成形成融资需要的数据。
- Qualcomm profile：技能是否可售取决于目标硬件、AI Hub/QNN profile、runtime constraints 和支持责任。
- System of record：一旦成为 quote-to-cash、usage-to-bill、renewal 的记录源，迁移成本很高。

### 09 · Why Qualcomm

Qualcomm 的机会不是只卖开发板，而是拥有开发板周围的收银机。

收入 attach chain：

`Dragonwing/RB3 starter kit -> cloud training credits -> AI Hub/QNN profile -> validated edge package -> certified skill listing -> fleet runtime subscription -> IQ10/Dragonwing production SKU`

Qualcomm 价值：

- Every starter kit creates a Qualcomm-first developer。
- Every trained model must produce a Qualcomm edge evidence record。
- No QNN profile, no marketplace-ready skill。
- Cloud trains; Qualcomm edge ships。
- Fleet ops keeps Qualcomm in the revenue stream after hardware sale。
- Prototype on RB3, productize on Dragonwing/IQ10。

竞争 framing：

- NVIDIA sells the robot brain; RevenueStack helps Qualcomm sell the robot business system around efficient edge deployment。
- UR+ / MiR Go 证明 approved ecosystem 能降低部署风险，但 scope 多数是 OEM-specific。
- Viam / Intrinsic 证明 registry、skills、digital twins 和 fleet deployment 正在成为机器人软件层；RevenueStack 把 Qualcomm AI Hub/QNN evidence 变成 marketplace gate。

### 10 · Demo & Ask

7 分钟演示：

1. Dealer 配置 20 台机器人报价：硬件、Inspection Pro 技能、10k 训练积分、3 年 SLA、渠道折扣。
2. 扫描 robot serial 激活 fleet：BOM revision、firmware、payload、warranty、customer、site、subscription。
3. 安装付费技能：校验 robot capabilities、BOM compatibility、QNN profile、entitlement，canary 到两台机器人。
4. 机器人跑任务：3 hours uptime、182 tasks、12 skill calls、40 training-credit minutes、SLA status green。
5. 触发售后：一台 lidar fault，ledger 检查保修和 SLA，生成 RMA、dealer dispatch 和 service credit risk。
6. Bill run：subscription line、usage overage、training-credit burn-down、app-store revenue share、dealer commission、revenue-recognition schedule。
7. Finance dashboard：ARR、usage revenue、deferred revenue、warranty liability、partner payout、renewal expansion。

对 Qualcomm 的请求：

- 6-8 周 Dragonwing Revenue Attach Sprint。
- RB3 / IQ10 demo target。
- AI Hub + QNN quota for 2-3 reference skills。
- Joint `Dragonwing Skill Profile v0.1`。
- Intro path to module partners, SI partners, education channels, and IQ10 RRD early-access ecosystem。
- 允许谨慎使用 `Dragonwing-profiled` 或 `Qualcomm-edge-ready candidate`，不声称官方认证。

## China / Overseas Packaging

中国版：

- 租售一体：purchase、lease、trial、deposit、service、renewal、buyout。
- 渠道友好：reseller/SI commission、regional price book、partner portal、deployment milestone。
- 发票/补贴材料：contract、BOM、utilization、service、invoice data for equipment-upgrade or local subsidy submissions。
- 国产云/模型适配：Alibaba, Baidu, Tencent, Huawei cloud and model-service billing connectors。
- 技能商店/数据服务：robot skills、teleop datasets、fine-tuning、remote monitoring、SLA tiers after robot ships。

海外版：

- RaaS billing：monthly、hourly、per pick、per delivery、per patrol、per acre、per tote、per task。
- Finance stack：lender reporting、collateral tracking、subsidy docs、ASC 606/842 handoff。
- Partner marketplace：dealers、integrators、leasing partners、installers、territory commissions。
- Usage proof：labor saved、throughput、uptime、robot utilization。
- Add-on marketplace：crop algorithms、robot skills、remote operators、AI monitoring、analytics。

## Claim Guardrails

- 不承诺替代客户 ERP/财务系统；RevenueStack 是机器人商业对象层，可与 ERP/Stripe/NetSuite 集成。
- 不给正式会计/税务/收入确认法律意见；只说提供数据和流程支持。
- 不把 `Dragonwing-profiled` 说成官方安全认证。
- 不说所有技能都能自动上架；需要兼容性、profile、支持责任和风险审查。
- 不把 RaaS 描述成一定降低成本；要基于 utilization、support cost 和客户场景计算。

## Sources

- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Formic RaaS：https://formic.co/resources/articles/robots-as-a-service-raas
- Locus RaaS ROI：https://locusrobotics.com/blog/raas-warehouse-roi
- Brightpick RaaS：https://brightpick.ai/resources/how-brightpicks-raas-works/
- Richtech 10-K：https://www.sec.gov/Archives/edgar/data/1963685/000121390025003458/ea0226831-10k_richtech.htm
- Intuitive 10-Q：https://www.sec.gov/Archives/edgar/data/1035267/000103526725000109/isrg-20250331.htm
- Starship deliveries：https://www.starship.xyz/press/autonomous-delivery-moves-into-the-mainstream-as-starship-technologies-passes-10-million-deliveries/
- UR Marketplace：https://www.universal-robots.com/marketplace/
- UR leasing：https://www.universal-robots.com/services/collaborative-robot-leasing/
- UR warranty：https://www.universal-robots.com/download/service-documentation/standard-warranty/
- PUDU Care：https://www.pudurobotics.com/en/pudu-care
- Unitree shop：https://shop.unitree.com/collections/humanoid-robot
- 1X order：https://www.1x.tech/order
- Agility RaaS：https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics
- Figure BMW：https://www.figure.ai/news/production-at-bmw
- Hardfin robotics：https://www.hardfin.com/industries/robotics
- Stripe Billing：https://docs.stripe.com/billing
- Stripe Entitlements：https://docs.stripe.com/billing/entitlements
- AWS Marketplace SaaS contracts：https://docs.aws.amazon.com/marketplace/latest/userguide/saas-contracts.html
- Viam registry：https://docs.viam.com/what-is-viam/
- Intrinsic Flowstate：https://www.intrinsic.ai/flowstate
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- AI Hub profile docs：https://workbench.aihub.qualcomm.com/docs/hub/profile_examples.html
