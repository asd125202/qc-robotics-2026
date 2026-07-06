# HarnessLoop 线束异常闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

HarnessLoop 是智能车的物理 Bug Tracker：

> 关闭电动车线束和连接器异常：把半插连接器、错路线束、漏夹扣、导通失败、返工证据和供应商签核变成同一条可追溯闭环，让软件定义汽车不被物理神经系统卡住交付。

## Problem

EV OEM 和 Tier-1 并不缺检测工具，缺的是异常闭环系统。

- EOL 测试、视觉检测、MES、QMS、Excel、照片、微信群和工程师经验都在记录局部事实。
- 线束异常需要跨 connector、cavity、wire、terminal lot、VIN、工位、供应商、返工和复测。
- 一个连接器半插、错孔、漏夹扣或导通失败，可能造成下线返工、整批围堵、客户投诉、发布延期或召回风险。
- 通用 QMS 只看 ticket；HarnessLoop 看线束语义和物理证据链。

## Why Now

市场正在被 EV 规模和供应链压力推到拐点：

- 新华社转引中汽协数据：2025 年中国新能源汽车销量 1649 万辆，同比增长 28.2%。
- 新华社转引中汽协数据：2026 年 5 月中国新能源汽车新车销量占比达到 56.9%。
- IEA Global EV Outlook 2026 显示，2025 年全球 electric car sales 超过 2000 万辆，中国接近 55% 新车销售占比。
- Q5D 2025 年称线束制造仍高度人工化，电动化正在放大自动化需求。
- Q5D 2025 年融资 1350 万美元，说明资本已经看到线束自动化痛点。
- Agile Robots 2025 线束挑战展示双臂、相机、力矩传感和 AI 视觉，但行业仍把线束视为最难自动化环节之一。
- Siemens 2024 停机研究估算大型汽车工厂非计划停机成本可达每小时约 230 万美元。
- 中国 GB/T 37133-2025 等高压连接系统标准让线束质量和证据变得更具体。

## Core Insight

难点不是发现缺陷，而是把缺陷从发现关到验证通过。

现有视觉、EOL、MES、QMS、PLM 和机器人自动化都贡献碎片。HarnessLoop 的产品位置是专用的 system of closure：

`connector C214 / cavity 17 / terminal lot / wire ID / vehicle variant / EOL failure / rework proof / supplier signoff`

## Solution

HarnessLoop 不替代 MES、QMS 或线束设计软件。它补现场异常关闭层：

1. Open：从 EOL 测试、视觉检测、扫码、人工发现或机器人力曲线打开异常。
2. Route：按 connector、cavity、wire、terminal lot、车辆项目、供应商和工位自动派给责任人。
3. Recover：机器人或人工在受限夹具内复位、重插、补夹扣、拍照、复测并记录过程。
4. Close：生成包含 before/after、力曲线、导通表、HIL 片段、签核和 CAPA 的闭环包。
5. Learn：异常、人工接管和恢复片段写入 LeRobotDataset，训练下一版边缘检测和恢复策略。

## Product Workflow

第一版切口：连接器异常闭环。

状态对象：

- `exception_id`
- `vehicle_program`
- `harness_instance_id`
- `connector_id`
- `cavity_id`
- `wire_id`
- `terminal_lot`
- `station_id`
- `supplier_id`
- `eol_test_result`
- `vision_result`
- `insertion_force_curve`
- `continuity_result`
- `hil_interventions`
- `closure_status`
- `closure_basis`

流程：

1. Detect：EOL NOK、视觉缺陷、半插力曲线、漏夹扣、错路线束或供应商 NCR 打开异常。
2. Correlate：关联 VIN、工位、线束件号、连接器、端子批次、测试项、操作员和供应商。
3. Recover：HIL 模式下完成重插、补夹、复位、低压导通复测和 before/after 影像采集。
4. Verify：力位移曲线、视觉状态、导通表、复测记录和人工签核共同判断是否关闭。
5. Learn：把异常、接管和恢复片段写入 LeRobotDataset。

## Market Wedge

从 EV 发布爬坡期的连接器异常进入：

- 连接器半插。
- 错线 / 错孔。
- 漏夹扣 / 错路线。
- 批次围堵。
- 供应商 NCR。
- 客户 audit 证据包。

目标买家：

- EV OEM 制造质量、SQE、EOL、制造工程。
- Tier-1 线束供应商。
- 连接器和端子供应商。
- 发布爬坡和质量攻关团队。

中国目标生态：

- BYD、Geely、SAIC、Changan、GAC、NIO、Xpeng、Li Auto、Xiaomi Auto。
- Huguang、THB/Tianhai、Jinting、Deren、Luxshare/Leoni、JONHON、Yonggui、Recodeal。

## Business Model

收入模型：

> paid pilot + site subscription + supplier portal + edge workcell package

建议价格：

- 90 天试点：7.5 万美元/工厂/项目，覆盖 1 条发布线、3 个重点连接器工位和 EOL failure feed。
- 年度站点订阅：18-24 万美元/site/year，按线体、车型项目、活跃线束族和供应商协同范围分层。
- 供应商门户：OEM 赞助供应商网络，Tier-1 和连接器供应商按 seat / program 参与。
- 边缘工位包：相机、低力夹具、导通 mock、robot/HIL adapter、Qualcomm edge runtime 和实施服务。

ROI 公式：

`90-day value = avoided rework events * cost/event + closure minutes saved * loaded labor rate + downtime minutes avoided * line cost/min + avoided containment vehicles * dealer/service cost per vehicle + warranty claims avoided * avg claim cost`

90 天 KPI：

- 目标缺陷 repeat PPM 下降 20-30%。
- 目标 EOL 电气 NOK/复测率下降 15-25%。
- 平均诊断/返工/关闭时间下降 20-30%。
- 超过 24 小时未关闭异常减少 50%。
- 95%+ 目标异常带站点、VIN/lot、证据、处置、根因、围堵责任人和复测结果。
- suspect population trace time 小于 30 分钟。

## Competition

HarnessLoop 不直接替代已有系统：

- Siemens Capital / Zuken / ECAD：强在设计和制造文档，弱在现场异常和返工闭环。
- MES / QMS：强在生产记录和 CAPA 流程，弱在线束语义、传感器证据和 HIL 数据。
- 视觉检测 / EOL：强在检测，弱在责任、返工、复测、签核和训练样本。
- Q5D / Agile Robots / 自动化公司：强在动作自动化，弱在跨系统异常关闭和供应商证据网络。

HarnessLoop 的位置是异常关闭层，把已有系统输出转成可签核、可复盘、可训练的数据资产。

## Moat

护城河是线束异常到关闭结果的数据结构：

- Harness graph：连接器、端子、线束分支、车型变体、工位、供应商和测试项。
- Evidence corpus：before/after 图片、力曲线、导通表、HIL 片段和签核记录。
- Recovery episodes：人工修复变成 LeRobot 训练样本。
- Supplier network：OEM / Tier-1 / 连接器供应商共享同一个事实层。

## Architecture

比赛版本使用安全低压桌面线束板，不接触真实 EV 高压。

### Robot / Control Plane

- ROS 2。
- 低力机械臂或 LeRobot-supported arm。
- 二指夹爪、软/触觉指尖、wrist camera。
- wrist F/T sensor 或夹具 load cell。
- 3D 打印线束板、clip、低压连接器、pogo pin / JST / Molex 类测试座。

### Edge AI / Exception Plane

- Qualcomm RB3 Gen 2 / QCS6490 类设备运行本地视觉、力曲线分类和证据打包。
- AI Hub / QNN / QAIRT 用于固定输入模型的 compile/profile/quantize。
- 云端训练，边缘推理；不声称 Qualcomm 现场训练整套机器人策略。

ROS 2 topics：

- `/camera/overhead/image_raw`
- `/camera/wrist/image_raw`
- `/wrist_ft`
- `/joint_states`
- `/continuity/result`
- `/harness/route_state`
- `/connector/insertion_curve`
- `/exception/event`
- `/hil/state`

### Dataset

- ROS bag 作为原始同步数据。
- LeRobotDataset v3 保存 state/action、视频、Parquet 和 metadata。
- HIL 记录 pause、takeover、recovery、return-to-policy 和 quality result。

## Competition Demo

3 分钟 demo：

1. Operator 加载低压 mock harness job。
2. overhead camera 识别 route、clip、connector 和 socket。
3. 故意 staged misroute 或半插连接器。
4. HarnessLoop 打开 `ROUTE_DEVIATION_CLIP_B` 或 `CONNECTOR_X3_PARTIAL_SEAT`。
5. 机器人低速尝试复位或插接，力曲线异常时停止。
6. 人工通过 LeRobot HIL 接管并恢复。
7. 复拍 before/after，导通 mock 从 fail 变 pass。
8. 系统关闭异常，生成 evidence packet 和 LeRobot episode。

## Why Qualcomm

HarnessLoop 是 Qualcomm 机器人和汽车生态的交叉点：

- 相机、力曲线、触觉、导通测试和异常证据需要端侧融合。
- 工厂和汽车供应链数据需要本地化/区域化部署。
- Qualcomm 已在智能座舱、ADAS 和 SDV 进入车厂；HarnessLoop 把价值延伸到制造质量。
- AI Hub、QNN/QAIRT、LeRobot HIL、ROS 2 和双云训练可以被包装成真实商业产品路径。

## Claims To Avoid

- 不说全自动汽车线束装配。
- 不说真实 EV 高压验证。
- 不说 ASIL、ISO 26262、IPC/WHMA 或 OEM 量产合规已完成。
- 不说 QNN 跑完整 LeRobot policy，除非实际转换和 profile。
- 不说任意连接器全自动插接。
- 不说力曲线单独证明产品质量。
- 不说无人关闭异常；应说 operator approval 或 evidence-backed closure recommendation。
- 不说桌面 demo 已验证生产节拍提升。

## Sources

- Xinhua / CAAM 2025 NEV: https://www.news.cn/fortune/20260114/cbbd861081c349d8ae238167ca418fa3/c.html
- Xinhua / CAAM May 2026: https://www.news.cn/fortune/20260610/24116a9f8ff14182a8c052eb4d380392/c.html
- IEA Global EV Outlook 2026: https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars
- Q5D automated harness production: https://q5d.com/news/fully-automated-wire-harness-production-demonstrated/
- Q5D funding: https://q5d.com/news/q5d-secures-13-5-million-in-funding-for-wiring-automation-including-series-a-venture-round-led-by-lockheed-martin/
- Agile Robots harness challenge: https://www.agile-robots.com/en/news/detail/robotik-challenge-2025-the-solution-behind-the-award/
- Robotic connector mating paper: https://arxiv.org/html/2503.09409v2
- Aptiv EDS separation: https://www.aptiv.com/en/newsroom/article/aptiv-announces-intention-to-separate-its-electrical-distribution-systems-business
- Versigent launch: https://ir.versigent.com/news/news-details/2026/Versigent-Launches-as-New-Publicly-Traded-Company/default.aspx
- GB/T 37133-2025: https://std.samr.gov.cn/gb/search/gbDetailed?id=2FF37940EB8DD753E06397BE0A0A413F
- Siemens downtime study: https://assets.new.siemens.com/siemens/assets/api/uuid:1b43afb5-2d07-47f7-9eb7-893fe7d0bc59/TCOD-2024_original.pdf
- WarrantyWeek auto warranty: https://www.warrantyweek.com/archive/ww20250911.html
- NHTSA recall example: https://static.nhtsa.gov/odi/rcl/2025/RCLRPT-25V769-7927.pdf
- LeRobot HIL: https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Qualcomm RB3 Gen 2: https://www.qualcomm.com/developer/blog/2025/03/powering-iot-developers-with-edge-ai-qualcomm-rb3-gen2-kit-now-integrated-with-edge-impulse
- Qualcomm AI Hub: https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT: https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/general_introduction.html
