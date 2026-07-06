# CircularLoop 城市矿山价值路由 Pitch

更新时间：2026-07-06。

## One-Line Company

CircularLoop 是旧电子设备的价值路由层：

> 帮品牌、运营商、ITAD、翻新商和回收商把每一台退回来的手机、笔记本、服务器模块、SSD 和电池，送到最赚钱、最可信、风险最低的下一站，并留下可验证的数据擦除、流向和合规证据。

它不做二手交易平台，不替代持证回收商，不处理真实损坏锂电池。它做的是进仓第一小时的 asset-level evidence routing。

## Problem

电子产品回收今天不是“没人回收”的问题，而是“回收后被送错地方”的问题。

同一台设备，在不同去向里价值完全不同：

- 对消费者，它可能只是一个回收补贴。
- 对翻新商，它可能是一台可售库存。
- 对维修网络，它可能是一组紧缺零件。
- 对 OEM，它可能是保修成本下降。
- 对材料商，它只是最后一层残值。

但今天这个判断很分散：

- 品牌看到的是退货。
- 维修商看到的是故障。
- 二手平台看到的是 SKU。
- 回收商看到的是重量。
- 企业 IT 看到的是数据风险。

结果是：还能卖的被拆了，能修的被压价，能做备件的被当废料，数据承载设备的擦除证据不完整，电池风险混入普通料箱。

## Why Now

设备下半生正在从环保成本，变成利润、合规和客户信任问题。

- Global E-waste Monitor：2022 年全球电子废弃物 6200 万吨，2030 年预计 8200 万吨，2022 年正式记录的收集和回收比例只有 22.3%。
- 中国“十四五”期间闲置手机存量约 60 亿部，进入二手平台比例约 10%，主要障碍是数据泄露担忧。
- GB 46864-2025 信息清除标准将于 2027-01-01 生效，要求二手手机/平板等流转前清除、验证和留痕。
- Basel e-waste amendments 于 2025-01-01 生效，危险和非危险电子废弃物跨境移动更需要事先知情同意和证据。
- EU Battery Regulation 推动 2027-02-18 起 EV、LMT 和大型工业电池 battery passport。
- EU Right to Repair 从 2026-07-31 起经成员国转化后适用，维修和再流通证据更重要。
- 中国“以旧换新”继续覆盖手机、平板、智能手表/手环、智能眼镜等数字产品，补贴风控需要实名、序列号、订单和去向证据。

## Insight

CircularLoop 的核心洞察：

> 电子循环的最大商业机会，不在“回收更多垃圾”，而在“把每台设备路由到最高价值用途”。

今天行业按品类、批次和重量处理设备；CircularLoop 按下一美元价值处理设备。

我们不是卖环保软件，而是卖：

- 利润发现。
- 数据擦除信任。
- 电池风险前端隔离。
- 可审计流向。
- 设备生命周期价格层。

## Solution

CircularLoop 是旧电子设备进仓第一小时的 AI 证据路由器。

它在进仓工位把每台设备识别、拍照、估值、风险分级、数据擦除验证、人工复核、分流标签和下游去向绑定成资产级证据包。

核心结果：

- 对 ITAD：证明每台数据承载设备被安全接收、擦除、销毁或交接。
- 对翻新/回收商：把可卖、可修、可拆、该回收、该隔离的设备更早分开。
- 对运营商/OEM：以旧换新、保修返件和保险换机有一致分级、流向和结算依据。
- 对监管/企业客户：输出 chain of custody、数据擦除证书、电池隔离和 ESG 证据。

## Product Workflow

1. Intake：设备入盘，系统生成防篡改 QR/GS1 资产标签，读取 IMEI、serial、service tag、客户批次和合同规则。
2. Inspect：RGB、depth、thermal、scale、barcode 和 OCR 在 edge 侧识别型号、成色、损伤、锁定状态和电池风险。
3. Route：比较翻新收入、维修成本、零件需求、物流成本、材料残值、合规风险和合作方报价。
4. Approve：数据承载、高价值、低置信度、电池风险、ID 不一致、擦除失败和 legal hold 进入人工审批。
5. Prove：数据擦除、NVMe/ATA sanitize、MDM/OEM erase、物理销毁或下游交接都形成签名证据。
6. Writeback：回写 ITAD、ERP、WMS、数据擦除、补贴、危废交接、二手平台和客户门户。
7. Learn：人工改判、抓取失败、错分、实际售价、拆件收益和隔离结果进入 LeRobot HIL 数据闭环。

## Market Wedge

先切数据承载、高残值、强审计的设备流，不从所有电子垃圾开始。

Beachhead：

- ITAD / 企业退役：电脑、手机、服务器、SSD、网络设备。
- 运营商 / OEM 以旧换新：手机、平板、可穿戴、智能设备。
- 翻新 / 二手平台：成色、故障、锁定、假件、电池健康和价格争议。
- 数据中心退役：AI 服务器、GPU、SSD、内存和网络设备刷新。
- 电池前端隔离：识别、隔离、DDR/危废交接、追溯和合规下游路由。

中国版本：

- “安全清除，放心换新”。
- 面向 GB 46864-2025 的信息清除、验证、证书和审计日志。
- 支持以旧换新活动的实名、序列号、订单和补贴风控。
- 接入“回收点 - 中转站 - 分拣中心”三级回收体系。
- 不宣传进口 foreign e-waste；强调国内闭环回收、再流通和合规材料。

海外版本：

- 面向 ITAD、R2/NAID、NIST 800-88、数据中心退役、right-to-repair、Basel e-waste、battery EPR。
- 强调 asset-level chain of custody、wipe evidence、reuse/refurb before shred、battery quarantine。

## Business Model

收入模型：

> paid pilot + facility SaaS + serialized asset/event usage + evidence add-on + optional recovery take-rate

建议包装：

| Package | Pricing Assumption | Buyer Logic |
|---|---:|---|
| 8-12 周试点 | $15k-$35k 或 10-30 万元 | 一个站点、1-2 个品类、5000-25000 件资产，事先定义成功指标。 |
| Facility SaaS | $2k-$8k / month / facility | 工作流、证据包、客户门户、合规报表、训练队列。 |
| Usage | $0.25-$1.50 / serialized asset or event | 设备级拍照、OCR、标签、路由、事件记录。 |
| Evidence Add-on | $1-$4 / data-bearing device | 擦除证书编排、审计门户、WORM 存证和客户报告。 |
| Hardware Kit | $2.5k-$7.5k basic; $10k-$30k advanced | 相机、扫码、称重、擦除工位、电池隔离和机器人辅助。 |
| Recovery Take-rate | 1-3% incremental recovery | 平台参与渠道路由或结算时，对增量回收价值分成。 |

示例 ROI：

- 中型站点每月 10000 件资产，$5k base + $0.75/event = $12.5k MRR。
- 如果每台节省 2 分钟人工，按 $25/hour 计算，每月约节省 $8.3k。
- 如果更快分级和更好路由每台提升 $3 回收价值，每月增加约 $30k。
- 目标 payback：3-6 个月。

## Go-To-Market

Land motion：“30 天审计包”。

1. 选一个设备流：laptops、phones、mixed enterprise endpoints、SSD/server modules。
2. 接入 spreadsheet、NetSuite/WMS、Blancco/BitRaser-style erasure logs、label printer、marketplace 或客户门户。
3. 记录 baseline：人工分钟/台、receipt-to-disposition、证书完整率、转售回收、错分、隔离、返工。
4. 试点目标：95%+ 序列化采集、样本数据设备 100% 可出证、人工分钟/台下降 20%、处置周期下降 30%、转售回收或避免成本提升 3-8%。
5. 扩展到多站点、多品类、电池工作流、企业客户门户、下游认证伙伴和 resale/recycle 结算。

渠道：

- R2 / NAID 顾问。
- ITAD broker。
- 数据擦除工具供应商。
- NetSuite / WMS implementer。
- MSP / enterprise ITAM。
- 3PL reverse logistics。
- 电池 stewardship / EPR 计划。

## Competition

现有玩家各管一段：

- ITAD incumbents：Sims、Iron Mountain、SK tes、ERI、Reconext 等有物流和客户信任。
- Trade-in / refurb：Assurant、Likewize、Back Market、ATRenew 等强在交易和渠道。
- AI sorting：AMP、Greyparrot、Glacier、Recycleye 多面向 MRF / 包装流。
- Robotic disassembly：Molg 证明服务器/电子拆解机器人趋势。
- Battery recyclers：Redwood、Cirba、CATL/Brunp、Glencore/Li-Cycle 等需要更干净、更安全、更可追溯的前端料流。
- China incumbents：万物新生、转转、华为、小米、联想、荣耀、vivo、OPPO 等靠近标准。

CircularLoop 的位置：

> 资产级第一小时：识别、价值路由、数据擦除证据、电池隔离、人工复核、下游结算。

## Moat

护城河不是会识别手机，而是设备下半生的事件图、价格层和信任层。

会积累的资产：

- Device event graph：资产历史、来源、序列号、成色、故障、擦除、证书、下游和最终售价。
- Receiver network：翻新商、维修商、零件商、材料商、合规回收商和电池处理商实时需求。
- Compliance connectors：NIST 800-88、IEEE 2883、R2v3、NAID AAA、GB 46864、WEEE、电池追溯和客户审计。
- Edge evidence：多相机、扫码、称重、热像、机器人动作、人工改判、WORM 存证和 QNN/QAIRT profile。
- Price history：型号、故障、地区、渠道、时间窗口对应真实成交和处置结果。

## Architecture

现场本地判定，证据不可篡改，训练按区域隔离。

```text
Intake tray
  -> vision / OCR / barcode tunnel
  -> Qualcomm edge decision
  -> human approval gate
  -> robot sort / wipe / test
  -> WORM evidence ledger
  -> LeRobot HIL training loop
```

### Edge Cell

- Top / side / wrist RGB cameras。
- ToF / depth。
- Thermal for risk cues and demo visualization。
- Scale。
- Barcode / OCR。
- Torque-limited tool。
- Small 6-axis arm / SCARA / gantry with soft gripper or vacuum tool。
- Four gated bins：refurb、parts、recycle、quarantine。
- Wipe/test docks。
- Fire-rated quarantine box in production, inert prop in demo。

### Routing Rules

- `refurb`：ID verified, battery safe, wipe proof pass, functional grade A/B。
- `parts`：not refurb-grade but components usable; storage wiped/removed first。
- `recycle`：no reuse value; storage sanitized or destroyed first。
- `quarantine`：damaged/defective/recalled battery, thermal anomaly, swelling/leak, ID mismatch, wipe failure, low confidence, legal hold, human escalation。

### Evidence

每个事件包含：

- asset ID / serial / IMEI / service tag。
- images / video hashes。
- method / tool version / operator / timestamp。
- model hash / confidence / route reason。
- wipe or destruction method。
- human approval / override reason。
- downstream receiver。
- final disposition。

全球可用 S3 Object Lock / WORM pattern；中国证据可用 Alibaba OSS WORM 或客户私有对象存储。QR 打开 redacted verification page。

### Qualcomm Path

- Competition demo：RB3 Gen 2 Vision Kit 或 RB5。
- Production reference：Dragonwing IQ10 RRD，按 Qualcomm 2026-06 信息，其全球可用性从 2026-09 开始，因此在比赛中描述为生产路线，不承诺当前可用。
- Model chain：PyTorch / ONNX -> Qualcomm AI Hub -> Neural Processing SDK / QNN / QAIRT -> signed registry -> edge redeploy。

### LeRobot Loop

- Teleop demos and human interventions become LeRobotDataset v3 episodes。
- Episode fields：multi-camera video, robot state, action, decision reason, success/failure。
- Use HIL data for grasp recovery, cable/connector handling, edge-case sorting。
- China raw imagery/evidence stays in China region or private cloud unless legal review approves export。

## Competition Demo

3 分钟 demo：

1. Mixed tray：phone、laptop SSD tray、server drive caddy、dummy battery pack。
2. Vision tunnel 扫描，显示 object class、OCR serial、barcode ID、thermal reading、model confidence、asset QR。
3. Simulated battery swelling / thermal marker 被标记为 `quarantine`，机器人放入隔离箱。
4. Laptop / drive 路由到 wipe dock，展示 mock NVMe log、NIST/IEEE method、signed wipe certificate、WORM object version、QR verification。
5. Cracked phone 置信度 78%，触发人工审批；操作员选择 `parts` 并填写原因。
6. 触发一次抓取失败，操作员接管；LeRobot 记录 HIL episode。
7. Dashboard 输出 batch result：refurb value、parts value、recycle weight、quarantined hazards、wipe certificates、WORM audit bundle、Global / China training queues。

## Risk Controls

- Battery：不演示真实损坏锂电池；使用 inert props。生产需要热监控、隔离箱、hazmat handling、DDR 包装和运输流程。
- Robot：安全 PLC 独立于 AI；e-stop、interlock、light curtain / area scanner、reduced speed teach、torque limits、LOTO。
- AI：数据承载资产和电池风险不能自动执行不可逆决定；需要 confidence threshold、OOD、manifest cross-check、human approval、version logging、rollback。
- Data：训练前脱敏屏幕和 PII；证据加密；中国证据地域锁定；RBAC；signed logs；下游回收商认证检查。

## Why Qualcomm

CircularLoop 不是回收软件，而是 Qualcomm 设备生态的下半生价值基础设施。

- Edge privacy：序列号、资产标签、擦除状态和客户信息先在站点内处理。
- Multimodal AI：多相机、深度、扫码、称重、工具遥测和人工复核适合 Qualcomm edge AI。
- Hardware roadmap：RB3/RB5 可做比赛 demo；Dragonwing IQ10 RRD 可以讲生产参考路线。
- Model pipeline：AI Hub、Neural Processing SDK、QNN/QAIRT 让模型可 profile、可签名、可回滚。
- Ecosystem story：帮助 OEM、运营商、ITAD 和翻新生态建立设备生命周期价值报告。

## Ask

请 Qualcomm 帮我们把第一小时价值路由做成可试点工位：

- RB3 Gen 2 / RB5 / Dragonwing dev kit。
- 多相机、扫码、称重、低力机械臂和安全隔离箱建议。
- 1000-5000 台匿名设备样例：型号、成色、故障、擦除状态、去向、售价和人工判断。
- 一个 ITAD、翻新商、运营商回收中心、OEM 换新团队或 WEEE 授权拆解企业。
- AI Hub / QNN profile 工程支持。
- 90 天对比报告：同批设备的收入、周期、证据完整率、风险隔离和人工触碰变化。

## Claims To Avoid

- 不说解决全球电子垃圾。
- 不说保证零废弃。
- 不说已经和 Qualcomm 合作。
- 不说 AI/区块链彻底改变回收行业。
- 不说每台设备都能被翻新。
- 不说自动满足所有合规要求。
- 不说处理真实损坏锂电池。
- 不说视觉能判断电池健康度。
- 不宣传进口 foreign e-waste。

## Sources

- Global E-waste Monitor / ITU：https://www.itu.int/en/ITU-D/Environment/Pages/Publications/The-Global-E-waste-Monitor-2024.aspx
- UNITAR E-waste Monitor：https://unitar.org/about/news-stories/press/global-e-waste-monitor-2024-electronic-waste-rising-five-times-faster-documented-e-waste-recycling
- China data erasure / idle phones：https://www.cac.gov.cn/2025-12/14/c_1767349770073163.htm
- GB 46864-2025：https://std.samr.gov.cn/gb/search/gbDetailed?id=44F3E6F8202EB68DE06397BE0A0A3836
- CAICT phone shipments Jan-May 2026：https://www.caict.ac.cn/kxyj/qwfb/qwsj/202606/P020260624562906177013.pdf
- Grand View ITAD market：https://www.grandviewresearch.com/industry-analysis/it-asset-disposition-market
- Assurant trade-in Q1 2026：https://www.assurant.com/news-insights/news_releases/mobile-trade-in-programs-trends-Q1-2026
- NIST SP 800-88：https://csrc.nist.gov/pubs/sp/800/88/r1/final
- IEEE 2883：https://standards.ieee.org/ieee/2883/10277/
- R2v3 / SERI：https://sustainableelectronics.org/r2/
- NAID AAA：https://isigmaonline.org/certifications/naid-aaa-certification/
- EPA used lithium-ion batteries：https://www.epa.gov/recycle/used-lithium-ion-batteries
- PHMSA DDR battery guide：https://www.phmsa.dot.gov/sites/phmsa.dot.gov/files/2023-03/DDR-brochure.pdf
- Basel e-waste amendments：https://www.basel.int/Implementation/Ewaste/EwasteAmendments/Overview/tabid/9266/Default.aspx
- Molg：https://www.molg.ai/
- ABB / Molg server disassembly：https://new.abb.com/news/detail/120071/prsrl-abb-robotics-and-us-start-up-molg-tackle-data-center-e-waste-with-robotic-microfactories
- AMP Robotics Series D：https://ampsortation.com/articles/amp-raises-91m-seriesd
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
