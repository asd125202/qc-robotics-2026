# BatteryRouter 电池入仓路由 Pitch

更新时间：2026-07-06。

说明：`BatteryRouter` 是本页使用的产品名；`BatteryLoop` 只作为内部概念名。市场上已有 Stena 旗下 BatteryLoop 等同名实体，本项目不代表任何关联、授权或合作。

## One-Line Company

退役电池进仓第一小时，决定利润和风险。

> BatteryRouter 把未知电池先变成可路由资产：扫码、拍照、热像、模拟电压/阻抗、BMS 数据、人工审批和机器人辅助分拣，把每块电池导向复用、维修、拆解、回收或隔离，并生成可审计证据包。

## Problem

回收商和二次利用团队收到的不是“电池”，而是一堆未知风险。

- 身份、损伤、历史、热风险、剩余价值和合规去向都不清楚。
- 分错箱会带来火灾风险、价值损失、人工低效、缺失审计证据。
- 本该复用或维修的电池可能被直接打碎回收。
- 该隔离的电池可能进入普通库位。

## Why Now

- IEA 2026：2025 年 EV 电池部署约 1.2TWh，同比增长接近 30%。
- IEA 2026：2025 年全球新增电池储能约 108GW，较 2024 年增长约 40%。
- Moss Landing 2025 火灾让 BESS 安全和公众信任成为董事会问题。
- 欧盟电池法规要求 EV、LMT 和大于 2kWh 工业电池进入 QR / battery passport 监管阶段。
- 中国动力电池回收新规于 2026-04-01 生效，要求数字身份、编码、回收网络、流向监控和定时报送。
- 中国 GB 38031-2025 于 2026-07-01 生效，提高 EV 动力电池安全门槛。
- 2026 年 NHTSA 多起电池召回显示，真实问题往往要追溯到具体 cell/module、供应商工艺、软件补救和热风险。

## Core Insight

最大的价值不是最后回收得更好，而是一开始路由得更对。

一块本可复用、维修或梯次利用的电池，如果被直接扔进破碎线，会损失价值；一块该隔离的电池，如果进入普通库位，会放大安全风险。

## Solution

BatteryRouter 是低风险入仓工位 + 电池证据包系统：

1. Identify：读取 QR、铭牌、OCR、包装/运输记录和可用 BMS/护照数据。
2. Inspect：采集 RGB、热像、重量、模拟电压/阻抗、外观缺陷和人工备注。
3. Route：推荐复用、维修、人工复核/隔离、拆解、材料回收或退回供应方。
4. Approve：人工审批、复测或纠正模型建议。
5. Record：导出证据包，包含模型版本、传感数据、人工审批、去向、哈希和报送字段。
6. Learn：路由建议与真实复用、维修、回收和隔离结果闭环，更新 edge model。

## Product Workflow

第一版从中小型混合锂电池和 EV 模组开始，不从整包高压拆解开始。

状态对象：

- `intake_case_id`
- `pack_or_module_uid`
- `source_owner`
- `qr_payload_hash`
- `chemistry_label`
- `visual_condition`
- `thermal_features`
- `mock_voltage_features`
- `mock_impedance_features`
- `bms_import_status`
- `route_recommendation`
- `human_approval`
- `final_destination`
- `evidence_packet_hash`

流程：

1. Receive：入仓扫码、称重、拍照、读取运输/客户来源。
2. Diagnose：采集热像、外观、模拟或可用的 BMS/电压/阻抗字段，标记缺失数据。
3. Review：系统给出路由建议和 reason code，人工批准或要求复测/隔离。
4. Sort：机器人辅助贴标、搬运轻量模组或指引人工放入复用/维修/隔离/回收路径。
5. Report：生成数字身份、生命周期流向、客户审计和合规报送所需证据字段。

## Market Wedge

先做混合中型电池入仓，再进入 EV/BESS 大资产闭环。

第一批资产：

- e-bike / scooter packs。
- 机器人 / AMR / 电动工具电池。
- 小型 ESS / UPS 模组。
- EV modules before full pack automation。

第一批买家：

- Battery recyclers。
- Second-life integrators。
- OEM take-back teams。
- Micromobility fleets。
- Industrial robot fleet operators。
- Fleet / insurance / auction triage teams。

中国商业语言：

- `数字身份证`
- `全生命周期流向监控`
- `溯源信息平台`
- `回收服务网点`
- `梯次利用`
- `异常隔离`
- `合规报送`

## Business Model

收入模型：

> paid pilot + site SaaS + per-pack routing fee + value-share

建议价格：

- 90 天试点：6-9 万美元/站点，覆盖 250-500 个资产评估、集成、周度 triage review 和报告。
- 站点 SaaS：5k-20k 美元/site/月。
- 每件路由费：1-20 美元/pack/module。
- 成功费：按避免整包更换、二次利用增值、减少隔离范围或材料回收增收分享。

ROI 公式：

```text
Savings per triaged pack =
full_pack_replacement_cost
- module_repair_cost
- diagnostic_cost
- residual_risk_reserve

BESS downtime loss =
MW * 1000 * revenue_per_kW_year * outage_days / 365

Second-life margin =
usable_kWh * resale_$per_kWh
- acquisition_cost
- logistics
- diagnostic/grading_cost
- repurposing_cost
- warranty_reserve
```

90 天试点案例：

- 评估资产：400。
- 试点费：75,000 美元。
- 避免整包更换：8 件。
- 每件净节省：10,000 美元。
- 二次利用路由增值：25 件 * 1,200 美元。
- Resale/warranty evidence uplift：50 辆 * 500 美元。
- Gross verified benefit：135,000 美元。
- Net benefit：60,000 美元。
- Break-even：约 7.5 个避免整包更换。

## Competition

- Battery analytics：ACCURE、TWAICE、Zitara、Voltaiq。
- Battery health / used-EV data：Recurrent、Geotab、ReJoule。
- Second-life integrators：Redwood Energy、Element Energy、Moment Energy、B2U、Smartville。
- Recyclers/materials：Redwood、Glencore/Li-Cycle、Ascend Elements、Cirba、Fortum。
- Robotic dismantling：R3 Robotics、Comau、ORNL research-style automation。

BatteryRouter 的差异：在它们之前，把未知来料变成带证据的路由资产。

## Moat

- Route outcome graph：来源、检测、建议、审批、去向和真实后续结果。
- Rare-event HIL：罕见 pack 形态、接触不良、热像偏移和人工纠错进入 LeRobot 训练数据。
- Compliance workflows：数字身份证、全生命周期流向、环保合规、客户审计和保险证据。
- Edge profiles：RGB/thermal/impedance 模型的 AI Hub/QNN profile、哈希、延迟和回滚记录。

## Architecture

比赛 demo 只使用 3D 打印 mock 模组、USB/5-12V 电路、模拟电压/阻抗和温和热源。

### Hardware

- 3D-printed mock modules with removable plastic cells。
- QR label per module/cell。
- MCU with USB or current-limited 5-12V DC。
- Mock cell voltages from DAC/resistor ladder。
- Synthetic impedance from RC ladder。
- Small thermal hotspot resistor with cutoff, capped warm-to-touch。
- RGB camera and thermal camera。
- Low-force desktop robot arm or gantry。
- Qualcomm RB3 Gen 2 / QCS6490-class edge board。

### ROS 2 Topics

- `/camera/rgb/image_raw`
- `/camera/thermal/image_raw`
- `/batteryrouter/qr_scan`
- `/batteryrouter/mock_voltage`
- `/batteryrouter/mock_impedance`
- `/batteryrouter/inspection/features`
- `/batteryrouter/ai/result`
- `/batteryrouter/hil/correction`
- `/batteryrouter/sort/decision`
- `/batteryrouter/evidence_packet`
- `/joint_states`
- `/tf`
- `/safety/e_stop`
- `/diagnostics`

### Edge AI

Good QNN targets:

- RGB/thermal anomaly classifier。
- Object detector / segmenter for dents, labels, hotspot ROI。
- Electrical-feature MLP or 1D CNN over impedance / voltage vectors。
- Multimodal fusion model with fixed-shape image embedding and numeric features。
- HIL residual/correction model if neural。

Keep off QNN:

- ROS 2 / DDS middleware。
- Robot planning/control loops。
- QR decoding after detection。
- Evidence hashing/signing。
- Database/cloud sync。
- Dataset encoding。
- Cloud training。
- Safety interlocks。

## Competition Demo

3 分钟 demo：

1. Robot picks a mock module and places it under cameras。
2. System scans QR and displays mock passport record。
3. Thermal camera sees a simulated hotspot; MCU returns synthetic voltage / impedance。
4. Deliberate bad pogo contact creates false high impedance。
5. HIL detects contact bias, asks for reseat / remeasure。
6. System recommends `reuse_candidate`, `manual_review/quarantine`, or `recycle_path`。
7. Human approves route。
8. Robot sorts or labels the module。
9. Evidence packet exports sensor readings, model hash, decision trail, and route label。

## Why Qualcomm

- Battery intake sites need local camera AI, thermal sensing, weak-network operation, and privacy.
- Safety-critical workflows cannot depend on cloud inference.
- AI Hub / QNN can profile fixed-shape RGB/thermal/electrical-feature models.
- China-hosted data plane and on-prem/private cloud are required for sensitive auto/battery data.
- Robotics reference design can show Qualcomm physical AI in a regulated, high-value industrial vertical.

## Claims To Avoid

- 不说认证二次利用电池。
- 不说测量真实 SOH/RUL。
- 不说预测或防止热失控。
- 不说已满足 EU Battery Passport。
- 不说可安全处理真实 EV 电池。
- 不说自动化真实电池拆解。
- 不说整个机器人栈跑在 QNN。
- 不暗示与 Stena/BatteryLoop 或任何同名实体有关联。

## Sources

- IEA EV batteries 2026: https://www.iea.org/reports/global-ev-outlook-2026/electric-vehicle-batteries
- IEA battery storage 2026: https://www.iea.org/reports/global-energy-review-2026/technology-battery-storage
- EPA Moss Landing battery fire: https://www.epa.gov/ca/moss-landing-vistra-battery-fire
- EU Battery Regulation summary: https://eur-lex.europa.eu/EN/legal-content/summary/sustainability-rules-for-batteries-and-waste-batteries.html
- MIIT Order No.73: https://www.miit.gov.cn/gyhxxhb/jgsj/cyzcyfgs/bmgz/jdcjxl/art/2026/art_392462fdc40c415ea4a4129cac3028c2.html
- Xinhua / CAAM 2026: https://www.news.cn/20260610/4dfc520ccbeb4bbd99210ce2febfb063/c.html
- NEA China new energy storage: https://www.nea.gov.cn/20260130/b5b729cb7ad74723bcd614b663c75da6/c.html
- NHTSA VW ID.4 recall: https://static.nhtsa.gov/odi/rcl/2026/RCLRPT-26V030-0889.pdf
- R3 Robotics funding: https://www.eiturbanmobility.eu/r3-robotics-secures-e20m-to-scale-automated-disassembly-for-electric-vehicle-systems/
- ORNL automated disassembly: https://www.ornl.gov/news/automated-disassembly-line-aims-make-battery-recycling-safer-faster
- FLIR thermal monitoring for BESS: https://www.flir.com/discover/industrial/application-note-ensuring-safety-and-efficiency-with-flir-thermal-monitoring-for-battery-energy-storage-systems/
- OSHA lithium-ion safety: https://www.osha.gov/sites/default/files/publications/OSHA4480.pdf
- LeRobot HIL: https://huggingface.co/docs/lerobot/en/hil_data_collection
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Qualcomm AI Hub: https://workbench.aihub.qualcomm.com/docs/
- Qualcomm RB3 Gen 2: https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
