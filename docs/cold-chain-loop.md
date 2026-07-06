# ColdChainLoop 冷链闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

ColdChainLoop 是面向生鲜连锁、中央厨房、餐饮供应链、区域冷链 3PL 和温敏品仓配的冷链异常闭环系统：

> 把每一次脱温、滞留、错温区、封签/交接缺证，从告警变成责任、纠偏、证据、放行/隔离/拒收和下一轮机器人训练数据。

它不是又一个温度 logger，也不是车队 GPS 大屏。它是冷链事故从 `alert -> action -> proof -> release/CAPA` 的操作层。

## Problem

冷链企业已经有温度计、记录仪、GPS、WMS、TMS、司机 APP 和客户门户。缺的是异常闭环。

昂贵问题通常发生在交接点：

- dock dwell 时间太长。
- 冷藏车预冷不到位。
- 门开太久。
- 托盘进错温区。
- 记录仪没激活。
- 封签不一致。
- 干冰/冰袋耗尽。
- 收货方争议。

大多数系统只会产生一个告警或 PDF，但不回答：

> 谁处理了？什么时候处理？用什么证据证明？这批货还能不能放行？

## Why Now

- 全球冷链物流 2026 年估算在数千亿美元量级，食品、医药、跨境供应链和生鲜即时零售持续增长。
- FAO/UNEP 数据显示，全球食品在供应链前段损失 13.2%，零售、餐饮和家庭端再浪费 19%。
- FDA FSMA 204 虽然延后执法到 2028-07-20 前不会强制，但 CTE/KDE 和 24 小时记录访问要求已经给食品企业明确方向。
- 中国 2025 年冷链需求约 3.814 亿吨，冷链物流总收入约 5567.1 亿元；2026 年市场规模预计超过 5850 亿元。
- 中国已经布局 105 个国家骨干冷链物流基地，覆盖 31 个省份，冷链从建容量转向智能化运营。
- 医药追溯码从 2025-07-01 接入医保结算流程，到 2026-01-01 医疗/药店机构全面采集上传，药品冷链和追溯运营压力上升。
- 食品安全法、GB 31605、集中配送服务规范和采购商审计都在把“有没有温度记录”推向“异常是否及时处置、追溯、复盘”。

## Non-Obvious Insight

冷链不是缺 dashboard，而是缺 closed exception。

真正防御性的冷链数据不是温度曲线，而是：

> 温度曲线 + 产品/批次/序列号 + 交接节点 + 纠正动作 + 证据 + QA 放行/拒收结果。

ColdChainLoop 的价值不在于“看见脱温”，而在于把脱温变成可执行、可追责、可审计、可学习的闭环。

## Solution

ColdChainLoop 用四层把冷链异常闭环：

1. Detect：接入温湿度、光照、震动、门磁、GPS、reefer telematics、扫码、dock camera、人工 QA。
2. Decide：判断脱温、滞留、预冷失败、错温区、包装风险、封签不符、记录仪缺失和交接缺证。
3. Dispatch：把 SOP 派给司机、仓库、QA、3PL control tower 或冷库 AMR/机器人。
4. Prove：只有温度恢复、扫码、照片/视频、探针读数、封签、签名和系统回写齐全，异常才算关闭。

## Product Workflow

1. 货主定义产品 profile：冷藏、冷冻、2-8C 医药、干冰、CRT 或自定义路线规则。
2. ColdChainLoop 校验发运：批次、托盘、记录仪、包装、预冷、车辆/容器、收货方。
3. 运输或入库时监控温度、滞留、路线、门开、扫描和交接状态。
4. 异常触发 case、SLA 和 playbook。
5. 操作员纠偏：回冷、加冰、移区、复核封签、转入合格冷库、隔离、升级 QA。
6. 系统要求 proof：扫码、照片、温度恢复、签名、机器人/AMR 任务结果。
7. 写回 TMS/WMS/QMS，并生成审计、理赔、客户和监管材料。
8. 根因分析反向优化路线、承运商、包装、站点和 SOP。

## Market Wedge

先打“已经买了监控，但仍用群聊和截图关闭异常”的客户。

中国首批场景：

- 国家骨干冷链基地 / 区域 3PL：温度 SLA、异常处置、dock-to-dock trace、WMS/TMS 连接。
- 生鲜连锁 / 即时零售：前置仓、门店到家、拒收争议、损耗和 freshness proof。
- 中央厨房 / 团餐：食材验收、供应商证照、冷链交接、学校/企业供餐审计。
- 医药配送 / 疫苗：追溯码、温度记录、异常处置、过期/召回/隔离。

海外首批场景：

- 海鲜、肉类、果蔬、meal-kit 和 fresh-food 分销。
- Specialty pharma、2-8C 医药、临床样本和中型医药 3PL。
- 冷库和温控 cross-dock 运营商。

## Business Model

一句话收入模型：按冷链站点、货量和异常闭环收费，而不是只卖传感器。

- 90 天付费试点：中国 8万-30万元；海外 $10k-$60k，聚焦一个冷库、cold dock、路线或温区。
- 站点 SaaS：中国 3k-2万元/站点/月；海外 $500-$5k/站点/月，按事件、case、客户门户或合规模板扩展。
- 企业版：中国 30万-150万元/年；海外 $50k-$300k/年，含 TMS/WMS/QMS 集成、客户门户、SLA 报表和 QMS deviation/CAPA workflow。
- Edge kit：Qualcomm dock / truck / cold-room inspection node，按租赁、伙伴销售或成果分成组合。
- 渠道：WMS/TMS 厂商、冷库集成商、reefer 设备商、sensor/logging 厂商、冷链咨询公司。

## Go-To-Market

Beachhead promise：

> 45 天验证证据链，90 天验证经济性。

试点应先跑 2 周 baseline，再跑 10 周改进。核心指标包括异常关闭时间、温度偏离分钟/托盘、开门 dwell、错温区移区 SLA、缺标签/漏扫、QA hold 决策周期、模拟召回定位时间、审计包导出时间、人工日志/群聊追单时间和证据完整率。

中国版：

- 从冷链园区、区域 3PL、餐饮供应链、医药配送和本地系统集成商切入。
- 集成企业微信/钉钉/飞书、中国 WMS/TMS、本地私有云和药品/食品追溯要求。
- 主张：不是看温度，是把脱温异常闭环到责任、证据和赔付。

海外版：

- 从货主 QA、物流负责人和 3PL control tower 切入。
- 先做高价值路线，再扩展到 cold dock、区域网络、客户 proof portal 和 claims automation。

## Competition

- Controlant / Sensitech / Tive / Roambee / Wiliot：温度、位置和实时可视化强，但通常止于 alert。
- ELPRO / Berlinger / LogTag / Logmore / DeltaTrak：记录仪便宜可靠，但更多是事后证明。
- Thermo King / Carrier / ORBCOMM / Geotab / Samsara：reefer telematics 强，但资产中心重于产品/批次风险。
- GS1 EPCIS / IBM Food Trust / FoodLogiQ / TraceLink / SAP ATTP：追溯、序列化和合规强，但纠偏执行弱。
- AutoStore / Locus / Geek+ / Hai / Quicktron / Hikrobot：冷库机器人和仓内自动化强，但不天然理解产品温控风险。
- SafetyCulture / SAP / Oracle / Manhattan / Blue Yonder / 富勒 / 唯智：检查、WMS/TMS/QMS 强，但冷链质量闭环通常需要昂贵定制。

ColdChainLoop 的位置：

> Vendor-neutral cold-chain quality operating layer：把 sensor/logger、reefer、WMS/TMS、serialization、EPCIS、vision 和 robot tasks 连接成异常闭环。

## Moat

- Exception-action-outcome dataset：脱温、滞留、错区、封签、包装、承运商、站点、纠偏和 QA 结果持续积累。
- 产品/批次风险模型：从资产温度变成产品、批次、序列号和 shelf-life 风险。
- 深度集成：WMS/TMS/QMS、EPCIS、传感器、记录仪、AMR/fleet manager、客户门户。
- 合规模板：FSMA、GDP/GSP、GB/T 28843、GB 31605、药品追溯码和企业 SOP。
- 客户 proof portal：一旦客户和承运商都用同一套证据链，切换成本上升。
- Edge deployment profile：摄像头、传感器、离线运行和机器人巡检在 Qualcomm edge 上形成标准包。

## Architecture

### Edge Cell

- 每个 dock door、cold room、trailer 或 staging lane 部署一个 Qualcomm edge node。
- 接入温湿度、BLE tag、LoRa sensor、cellular tracker、门磁、相机和扫码。
- 本地执行阈值/规则、视觉识别、door-state、label/seal/pallet 检查、隐私遮罩和短期证据缓存。

### ColdOps Core

- `ColdChainProfile`、`ShipmentLeg`、`HandlingUnit`、`Excursion`、`CorrectiveAction`、`EvidenceBundle`。
- 生成 SLA、playbook、责任人、隔离/移区/加冰/转运/QA hold。
- 写回 WMS/TMS/QMS，输出 EPCIS-style event chain 和审计包。

### Robot Task Layer

- AMR/机器人只执行受限任务：扫描托盘、检查封签、移动到隔离区、送冷包、拍摄 after image。
- 通过 vendor fleet manager 或 MassRobotics AMR Interop 风格状态层接入。
- 安全由 AMR/机器人控制器、安全扫描器、E-stop 和现场流程负责。

### Learning Loop

- 人工接管、机器人纠错、漏扫、错区、低置信度视觉识别进入 LeRobot HIL。
- LeRobotDataset 记录图像、状态、动作、时间戳、控制模式和 intervention flag。
- 云端训练后通过 AI Hub / QNN / ONNX Runtime QNN EP profile，再灰度回 edge cell。

## Data Objects

- `EnvironmentalObservation`: sensor id、温度、湿度、时间戳、位置、电量、RSSI、校准状态。
- `VisionObservation`: camera id、label/seal/pallet/door 检测、OCR/QR、图像证据、模型版本。
- `ColdChainProfile`: 产品、批次、温区、最大脱温时间、包装、SOP。
- `Excursion`: shipment/lot、开始/结束、min/max、累计时长、严重度、证据。
- `CorrectiveAction`: quarantine、re-ice、move-to-cold-room、notify-carrier、hold-for-QA。
- `RobotTask`: 目标托盘、位置、批准动作、安全边界、状态、intervention count。
- `EvidenceBundle`: 温度曲线、照片、视频、扫码、签名、WMS/TMS/QMS 回写。
- `TrainingEpisode`: LeRobot dataset id、camera、robot state、action、intervention、success/failure。

## Demo

比赛 demo 应该让“异常关闭”可见，并保持低风险：

1. 创建模拟 shipment：2-8C 食品/温敏样品、托盘 QR/AprilTag、低压温度传感器、温度 profile。
2. Qualcomm edge node 监控一个泡沫箱、亚克力盒或 mini cold dock；不使用真实食品、药品、干冰、液氮、压缩机制冷或高功率加热。
3. 打开箱门、错区、漏扫或软件阈值触发温度/门开异常。
4. Edge 在本地生成 excursion case，显示温度曲线、相机证据和受影响 lot。
5. 人工批准纠偏：低速 rover 复扫、拍照、提示移区或由操作员完成隔离动作。
6. 系统要求 proof：扫码、照片、温度恢复、签名和任务完成。
7. WMS 更新到 `QUARANTINE`，TMS 标记 exception，QMS 生成 deviation/evidence bundle。
8. 操作者人工修正一次机器人动作，记录为 LeRobot HIL episode。

## Why Qualcomm

ColdChainLoop 是 Qualcomm supply-chain edge AI 的自然延伸：

- 冷链决策发生在 truck、dock、cold room、warehouse 和 last mile，网络不稳定且需要现场 proof。
- Qualcomm edge 能做传感器融合、相机视觉、低功耗连接、离线推理和本地缓存。
- Qualcomm Aware 的 supply-chain awareness 可以通过 ColdChainLoop 延伸到 action closure。
- AI Hub、QNN、ONNX Runtime QNN EP 可以让 label/seal/door/pallet/dwell 模型形成部署证据。
- Robotics Hub / LeRobot HIL 可以把 cold warehouse 的异常处理动作变成可训练数据。

## Claims To Avoid

- 不说自动 QA 放行或自动判定食品/药品安全。
- 不说满足 FDA/GxP/FSMA/GSP/药品追溯合规，除非逐项验证。
- 不说从环境温度精确推断产品核心温度。
- 不说零损耗、零召回、不可篡改追溯。
- 不说 BLE/LoRa 能承载视频或低延迟机器人控制。
- 不说 AI 本身提供机器人安全认证。
- 不说 LeRobot 能通过短 demo 达到生产级仓库自主操作。

## Ask

比赛阶段最需要 Qualcomm 支持三件事：

1. Edge hardware + AI Hub profile：用于 cold dock camera、传感器融合、离线 excursion detection 和 proof。
2. Qualcomm Aware / supply-chain sandbox：用于把资产可视化延伸到异常闭环。
3. 冷链试点伙伴：一个冷库/区域 3PL/生鲜配送/医药物流场景，验证 45 天 exception closure。

## Sources

- 中国冷链物流发展报告 2026：https://www.mot.gov.cn/xinwen/jiaotongyaowen/202606/t20260612_4207392.html
- Mordor cold-chain logistics market：https://www.mordorintelligence.com/industry-reports/cold-chain-logistics-market
- FAO food loss data：https://www.fao.org/policy-support/policy-themes/food-loss-and-food-waste/-Food-Loss-and-Food-Waste-Database/en
- UNEP Food Waste Index 2024：https://www.unep.org/resources/publication/food-waste-index-report-2024
- FDA FSMA traceability：https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods
- FDA sanitary transportation：https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-sanitary-transportation-human-and-animal-food
- 21 CFR Part 1 Subpart O：https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-1/subpart-O
- 中国 2025 冷链数据：https://gxt.fujian.gov.cn/zwgk/xw/hydt/xydt/202601/t20260128_7086292.htm
- 105 national cold-chain bases：https://www.ndrc.gov.cn/fzggw/jgsj/jms/sjdt/202506/t20250609_1398336.html
- China 14th five-year cold-chain plan：https://www.ndrc.gov.cn/fggz/fzzlgh/gjjzxgh/202203/t20220325_1320204.html
- 食品安全法 2025：https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=104105
- GB 31605 冷链物流卫生规范：https://zwfw.nhc.gov.cn/kzx/tzgg/sptjjxpzsp_224/202101/t20210118_2032.html
- Drug trace-code 医保结算：https://www.nhsa.gov.cn/art/2025/3/19/art_104_16045.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm Robotics RB5：https://www.qualcomm.com/developer/hardware/robotics-rb5-development-kit
- Qualcomm Aware：https://www.qualcomm.com/internet-of-things/solutions/aware
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- GS1 EPCIS：https://ref.gs1.org/standards/epcis/
- GS1 CBV：https://ref.gs1.org/standards/cbv/
- MassRobotics AMR interoperability：https://github.com/MassRobotics-AMR/AMR_Interop_Standard
