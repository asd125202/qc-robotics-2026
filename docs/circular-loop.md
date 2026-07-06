# CircularLoop 城市矿山分流闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

CircularLoop 是给 ITAD、电子回收商、运营商和 OEM 以旧换新的利润分流系统：

> 把混杂进仓的旧手机、笔记本、服务器模块和电池先分到转售、维修、拆件、危险电池处理、材料回收五条路径，并留下可审计记录。

它不做废品交易平台，也不声称全自动处理危险电池。它做的是旧电子设备进仓第一小时的 value routing、risk routing 和 proof routing。

## Problem

电子废弃物不是没有价值，是价值在进仓时被看不见、分不准、证明不了。

- 仍可转售、翻新或拆件的设备被过早当作材料粉碎。
- 鼓包、损伤或来源不明的锂电池被混入普通料箱，制造仓储、运输和保险风险。
- 企业设备、运营商回收机和服务器模块需要数据擦除证据、资产交接和客户审计。
- WEEE、动力电池追溯、以旧换新补贴、危险品交接和 ESG 报告需要完整链路记录。

## Why Now

四个变化同时发生：

- 全球电子废弃物继续增长。Global E-waste Monitor 2024 估算 2022 年全球电子废弃物 62M 吨，2030 年预计 82M 吨，2022 年正式记录的收集和回收比例仅 22.3%。
- 逆向物流规模扩大。NRF / Happy Returns 报告 2024 年美国零售退货总额 890B 美元，电子品、翻新和退役设备会继续增加。
- 电池风险进入运营和保险层。EPA 统计 2013-2020 年 64 个设施发生 245 起锂电池相关火灾，且可能被低估；CalRecycle 也把电池列为加州废弃物设施火灾主要原因。
- 中国政策在强化可追溯循环。2026 年动力电池回收措施强调全生命周期、数字身份和国家追溯；电子产品可用性分级、数据擦除标准、以旧换新和 WEEE 处理都在把“证据”变成基础设施。

## Insight

真正的价值不在最后粉碎，而在粉碎之前决定去向。

CircularLoop 的非显而易见判断：

> 回收商不会先为“机器人拆一切”付钱，但会为每批设备更高净回收价值、更低电池事故风险、更完整数据擦除证据和更可审计补贴链路付钱。

## Solution

CircularLoop 是旧电子设备的第一小时利润路由器。

1. 批次入库，扫码、称重、拍照，绑定来源、客户、合同、数据擦除要求和合规规则。
2. 边缘模型识别设备类型、型号、外观损伤、螺丝/连接器位置和电池风险线索。
3. 系统估算转售、维修、拆件、隔离和材料回收的净价值，并标出低置信度项。
4. 监督式低力机械臂做 mock 拆盖、螺丝定位、连接器断开和证据采集，人类批准高风险动作。
5. 系统生成数据擦除证书、链路记录和分流标签。
6. 状态回写 ITAD、ERP、WMS、回收、危险品交接和补贴系统。
7. 人工纠错、实际售价、拆件收益和电池隔离结果进入 LeRobot HIL。
8. 中国版在国内云或私有云训练，海外版在海外云训练，经 AI Hub / QNN / QAIRT / ONNX Runtime QNN EP 回到 Qualcomm edge。

## Product Workflow

状态机：

`identified -> inspect -> locate_fasteners -> unscrew -> disconnect -> grade -> sort -> audit`

第一版 demo：

- 旧手机、笔记本、平板、电源宝、服务器模块和假电池进入混合料箱。
- 本地模型识别设备、成色、疑似损伤、螺丝位置和电池风险。
- 低力机械臂做 mock 拆盖、定位、扫码、扭矩受限拧螺丝和连接器证据采集。
- 操作员批准高价值设备、低置信度和风险电池的去向。
- 系统导出数据擦除证书、链路记录、分流标签、价值估算和 QNN/QAIRT 模型版本。

## Market Wedge

第一批买方：

- ITAD：企业电脑、服务器、网络设备和手机退役，需要数据擦除证据、资产交接和再销售价值最大化。
- 运营商 / OEM：以旧换新、保险换机、维修返件和备件拆解需要稳定分级、去向记录和渠道回写。
- 零售退货中心：退货设备如果不能快速判定翻新、维修、拆件或报废，会占用仓储和折价窗口。
- 授权拆解厂：中国 WEEE 和电池追溯要求更强，合规链路和补贴证据本身就是产品价值。
- 数据中心：服务器刷新制造大量可拆件、可再制造和可审计销毁的高价值物料。
- 电池回收前端：第一版不做电池化学处理，而是做识别、隔离、交接、追溯和安全运输前证据层。

## Business Model

收入模型：

> paid pilot + site SaaS + device usage + optional value share

建议价格：

- Paid pilot：25k-75k 美元或 20-60 万元，4-8 周，一个品类、一个站点、1000 台设备基线。
- Site SaaS：3k-15k 美元/月/站点，包含设备路由、证据包、数据擦除接口、合规报表和训练队列。
- Usage：每台设备 2-8 美元；电池包或高价值模块 50-300 美元。
- Value share：对增量净回收价值收 5-15% 分成。

KPI：

- 净回收价值提升 5-15 个百分点。
- 人工触碰降低 20-40%。
- 电池隔离召回率超过 95%。
- 审计证据完整率超过 98%。
- 数据擦除证书覆盖率和异常闭环时间。

## Go-To-Market

90 天试点：

1. 找一个 ITAD、翻新商、运营商回收中心、OEM 以旧换新团队或 WEEE 授权拆解企业。
2. 选择一个品类：手机、笔记本、平板或服务器模块。
3. 跑 30 天人工 baseline。
4. 部署一个 CircularLoop workcell。
5. 对比净回收价值、人工触碰、电池隔离、证据完整率和异常返工。
6. 从单品类扩到多品类，从一个工位扩到全站点。

## Competition

竞争信号：

- AMP、Greyparrot、Recycleye、Glacier 等证明 AI 回收和材料分选正在资本化。
- Molg、R3 Robotics 等证明机器人拆解和 microfactory 有商业窗口。
- ATRenew 等证明二手电子品回收、分级、翻新和流通有大市场。
- ITAD、ERP、WMS、数据擦除和电池回收企业各自覆盖一段流程。

CircularLoop 的定位：

> 设备级第一小时价值路由 + 合规证据 + 机器人工作站 + LeRobot HIL 数据闭环。

## Moat

壁垒不是一个视觉模型，而是：

> device value graph + evidence dataset + compliance connectors + Qualcomm edge profiles

会积累的资产：

- 型号、成色、部件、渠道、维修成本、拆件收益、金属价值和处置成本的动态估值图谱。
- 照片、拆解动作、螺丝/连接器、人工纠错、数据擦除和实际售价组成的数据资产。
- ITAD、WMS、ERP、数据擦除、危险品交接、电池追溯和补贴申报接口。
- 多相机、弱网、本地隐私、QNN/QAIRT 部署和人工接管日志。

## Architecture

### Edge Capture

- Overhead RGB。
- Wrist RGB。
- RGB-D / depth / stereo。
- Barcode / OCR scanner。
- Scale。
- Torque-limited screwdriver。
- Force / motor current proxy。
- Optional thermal for visualization only。

### Edge Runtime

- RB3 Gen 2 / QCS6490 或 Dragonwing。
- Device detection, damage grading, screw/connector detection, battery-risk flagging, route recommendation。
- Low-confidence queue and operator approval。

### Cloud Training

- LeRobot HIL corrections and recovery trajectories。
- China cloud/private cloud for China sites。
- Overseas cloud for overseas sites。
- PyTorch / ONNX -> AI Hub compile/profile -> QNN/QAIRT package -> signed registry -> edge redeploy。

### Enterprise Writeback

- ITAD。
- ERP / WMS。
- Data erasure provider。
- Hazardous battery handoff。
- WEEE / trade-in / subsidy reporting。
- Customer audit packet。

## Competition Demo

3 分钟 demo：

1. Mixed intake bin has phones, laptops, tablets, power-bank shells, server modules and dummy battery props。
2. Edge model identifies device type, visible damage, screw/connector candidates and risk flags。
3. Cobot performs safe mock scan, unscrew and connector-disconnect evidence collection。
4. System recommends resale / repair / parts / battery quarantine / material recovery。
5. Operator corrects one low-confidence decision; correction enters LeRobot HIL queue。
6. Dashboard exports audit packet: data wipe certificate, route label, chain-of-custody, model version and edge profile。

Safety boundary：

- 不使用真实鼓包电池。
- 不做穿刺、切割、破碎、加热、化学处理或危险运输。
- 使用假电池、空壳或已移除电芯的设备。

## Why Qualcomm

CircularLoop 是 Qualcomm edge AI 的强样板：

- 现场多相机、多传感器、低延迟判断。
- 企业资产、序列号和数据擦除记录需要本地隐私处理。
- 回收仓库弱网，不能依赖云端实时推理。
- RB3 Gen 2 / QCS6490 / Dragonwing 可以承担本地视觉、队列和人机交互。
- AI Hub、QNN、QAIRT 和 ONNX Runtime QNN EP 让比赛 demo 能展示 compile/profile/deploy 证据链。
- 商业上把 Qualcomm 机器人能力延伸到 ITAD、回收、翻新、电池和循环经济基础设施。

## Ask

比赛阶段需要：

- RB3 Gen 2 / RB6 / Dragonwing dev kit。
- 多相机、扫码、称重、低力机械臂和扭矩受限电批。
- 1000 台匿名设备样例，含型号、成色、维修/转售/拆件结果、数据擦除状态和最终去向。
- 一个 ITAD、翻新商、运营商回收中心、OEM 以旧换新团队或 WEEE 授权拆解企业。
- mock data-wipe API、mock ITAD/WMS/ERP API。
- AI Hub / QNN profile 支持。

## Claims To Avoid

- 不说全自动电池回收。
- 不处理真实损坏锂电池。
- 不用视觉判断电池健康度。
- 不承诺 100% 检测或 100% 合规。
- 不说消灭人工。
- 不暗示已获得 Qualcomm 官方合作。
- 不承诺适用于所有电子废弃物。

## Sources

- Global E-waste Monitor 2024：https://ewastemonitor.info/the-global-e-waste-monitor-2024/
- EPA lithium-ion battery fires：https://www.epa.gov/system/files/documents/2021-08/lithium-ion-battery-report-update-7.01_508.pdf
- CalRecycle battery fire risk：https://calrecycle.ca.gov/epr/batteries/
- NRF / Happy Returns retail returns：https://www.nrf.com/media-center/press-releases/nrf-and-happy-returns-report-2024-retail-returns-total-890-billion
- Molg：https://www.molg.ai/
- ABB / Molg server disassembly：https://new.abb.com/news/detail/120071/prsrl-abb-robotics-and-us-start-up-molg-tackle-data-center-e-waste-with-robotic-microfactories
- R3 Robotics：https://eicscalingclub.eu/news/r3-robotics-raises-20-million-to-scale-automated-disassembly-for-end-of-life-electric-vehicle-systems
- AMP Series D：https://ampsortation.com/articles/amp-raises-91m-seriesd
- Greyparrot：https://www.greyparrot.ai/
- Recycleye / CP Group：https://recycleye.com/cp-group-acquires-recycleye/
- ATRenew：https://www.atrenew.com/
- China battery traceability measures：https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=105536
- GB/T 45656-2025：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=78CE40189798B4568879A068B1B773DC
- GB 46864-2025：https://std.samr.gov.cn/gb/search/gbDetailed?id=44F3E6F8202EB68DE06397BE0A0A3836
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/general_introduction.html
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
