# HarnessLoop 线束异常闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

HarnessLoop 是智能车的物理 Bug Tracker：

> 把 EOL 测试、视觉检测、导通图、连接器/孔位、返工动作、供应商 8D/CAPA 和人工签核变成同一条可追溯闭环，让线束异常从“发现了”走到“验证通过、责任关闭、训练回流”。

它不是全自动线束工厂，也不是另一个横向 QMS。它做的是 EV harness exception closure layer。

## YC-Style Opening

软件定义汽车，仍然会被一根线束拖住发布。

每次电池、智驾、座舱、快充或区域架构改动，都会触发设计、BOM、工装、供应商、EOL 测试、返工和客户放行。车厂和 Tier-1 不是没有检测工具，真正的问题是异常证据散落在 MES、QMS、Excel、照片、微信群、测试机和工程师脑子里。

HarnessLoop 把线束异常变成可以像软件 bug 一样打开、定位、分派、修复、验证、签核和复盘的物理 bug。

## Problem

EV/SDV 团队不是缺检测，而是被线束变更、EOL NOK、8D 和供应商证据拖慢。

- Launch Quality：新车型爬坡期最怕 EOL 电气 NOK、首批客户问题、yard hold、stop-ship 和第一 90 天质量指标失控。
- Supplier Quality：SQE/STA 要在 24 小时内围堵、推进 8D、证明根因和纠正有效，但证据跨 OEM、Tier-1 和连接器供应商。
- Plant Quality：Tier-1 工厂面对复测、返工队列、false fail、客户 PPM、第三方 sorting 和 chargeback。
- Test Engineering：导通、HiPot、绝缘、视觉和 terminal seating 数据被困在测试站，难以连到 PFMEA、控制计划和供应商 scorecard。

## Why Now

EV 规模、出口、快速换代、召回监管和线束自动化同时逼近拐点。

关键证据：

- IEA Global EV Outlook 2026 显示，2025 年全球 electric car sales 超过 2000 万辆，约占新车销量 25%；2026 年预计约 2300 万辆、28%。
- 新华社转引中汽协数据：2025 年中国 NEV 销量 1649 万辆，连续 11 年全球第一。
- 2026 年 5 月，中国 NEV 销量占新车销量 56.9%。
- 2026 年 5 月，中国汽车出口 93 万辆，同比增长 68.7%；NEV 出口 44.6 万辆，同比翻倍以上。
- 中国 2025 年汽车召回 190 次、684.6 万辆；NEV 召回 105 次、265.2 万辆。
- GB/T 37133-2025《电动汽车用高压连接系统》已于 2025-02-28 发布并实施，供应链质量证据更具体。
- Aptiv EDS 拆分成 Versigent，2025 年收入约 88 亿美元，证明电气分配系统是独立大市场。
- Luxshare 增持 Leoni，说明线束供应链正在跨中国/欧洲整合。
- Q5D、Komax、Agile Robots 和 EOL 测试厂商证明自动化正在发生。
- Siemens downtime report 估算汽车行业非计划停机成本可达约 230 万美元/小时。

## Insight

难点不是发现缺陷，而是把缺陷从发现关到验证通过、8D 关闭和供应商责任关闭。

现有视觉检测、EOL 测试、MES、QMS、PLM、ECAD、机器人 cell 都在贡献碎片。高混线束需要一个懂 connector/cavity/wire/lot/VIN/tester 的 system of closure，而不是又一个横向工单系统。

一句话：

> 模型可以建议，导通/映射图决定，人工签核关闭。

## Solution

HarnessLoop 是高混线束自动化的中立闭环控制层。

它不替代 Siemens Capital、Zuken、Q5D、Komax、MES、QMS 或测试站。它补的是最丑但最值钱的一层：把检测、返工、复测、责任人、供应商、工程变更、8D/CAPA 和客户放行绑成一条证据链。

1. Ingest：接入 ECAD/BOM/wire-list、EOL tester、视觉、MES/QMS、供应商 NCR 和机器人/HIL 事件。
2. Route：按 connector、cavity、wire、terminal lot、车辆项目、供应商、工位和 8D SLA 自动派给责任人。
3. Recover：人、cobot、测试工装或机器人在受限夹具内复位、重插、补夹扣、拍照、复测并记录过程。
4. Close：生成 before/after、导通矩阵、力曲线、HIL 片段、PFMEA/control-plan 更新和签核证据包。
5. Learn：异常、人工接管和恢复片段写入 LeRobotDataset，训练下一版边缘检测和指导策略。

## Product

第一版切口：

> Connector / EOL Exception Closure

第一版不是全自动线束工厂。它先解决发布爬坡和 EOL 电气失败最疼的一段，再扩展到线束路由、夹扣、扎带、高压连接、供应商门户和 ECO-to-floor。

状态对象：

- `exception_id`
- `vehicle_program`
- `harness_family`
- `harness_instance_id`
- `connector_id`
- `cavity_id`
- `wire_id`
- `terminal_lot`
- `connector_lot`
- `tester_id`
- `station_id`
- `supplier_id`
- `eol_test_result`
- `continuity_matrix`
- `visual_result`
- `insertion_force_curve`
- `hil_interventions`
- `closure_status`
- `closure_basis`

流程：

1. Detect：EOL NOK、terminal seating vision、导通/HiPot/绝缘异常、错路线束或供应商 NCR 打开异常。
2. Correlate：关联 VIN、工位、线束件号、连接器、孔位、端子批次、测试项、操作员和供应商。
3. Recover：人或 HIL 模式下完成重插、补夹、复位、低压导通复测和 before/after 影像采集。
4. Verify：模型可以建议，导通/映射图决定；PASS 必须满足预期 pin-to-pin mapping 且无 open/short/bridge。
5. Learn：把异常、接管、恢复、复测和关闭结果写入 LeRobotDataset。

## Market Wedge

先打发布爬坡期的 EOL/连接器异常，再进入整车电气质量网络。

发布爬坡期最愿意付费，因为质量团队每天都在跟 EOL NOK、供应商围堵、客户 audit、PPAP/APQP、8D 和停线风险赛跑。HarnessLoop 用一个窄入口拿到关键数据模型，然后扩展到全项目、全工厂和供应商网络。

第一批场景：

- EOL 电气 NOK：把 open、short、wrong mapping、HiPot/绝缘失败定位到 connector/cavity/wire 可执行动作。
- 连接器半插：视觉看起来像合格，CPA/锁止可能欺骗人眼，力曲线、复拍和导通复测能补证据。
- 错线 / 错孔：按 connector-cavity-wire ID 建模，把错误孔位和错误电路映射到返工指导。
- 漏夹扣 / 错路线：路线偏差、clip vacancy 和扎带缺失通过 overhead vision、工装反馈和返工证据关闭。
- 批次围堵：按 terminal lot、connector lot、tester、工位时间窗和车辆范围快速定位 suspect population。
- 8D / 客户 Audit：自动生成闭环证据包：问题、围堵、根因、纠正、复测、签核和有效性验证。

目标买家：

- EV OEM Supplier Quality / STA / SQE for EDS/HV harness。
- EV OEM Launch Quality / Plant Quality。
- Tier-1 Harness Plant Quality Manager。
- Tier-1 Ops / Plant GM。
- Test / Manufacturing Engineering。
- Procurement / Value Analysis。

## Business Model

用停线、围堵、返工、质保和 8D 人工的钱，为闭环系统付费。

收入模型：

> paid KPI pilot + site/program subscription + supplier-quality package + edge workcell package

建议价格：

- 90 天试点：35k-75k 美元/站点，覆盖 1-2 个线束族、1-3 个 tester/data integration、weekly value review 和采购可读 ROI。
- Production SaaS：90k-180k 美元/site/year 给 Tier-1 工厂质量；重集成另收 15k-75k 美元实施费。
- OEM supplier-quality package：150k-300k 美元/program/year，覆盖一个 commodity/program 与指定供应商质量 cockpit。
- Enterprise：多站点/多项目可达 500k+ ARR。
- Edge workcell package：相机、低压导通夹具、load cell/F/T、robot/HIL adapter、Qualcomm edge runtime 和实施服务。

ROI 公式：

`ROI = (Avoided rework/scrap + avoided containment/sort + avoided downtime + avoided premium freight + avoided warranty/recall exposure + 8D labor saved - HarnessLoop cost) / HarnessLoop cost`

细分：

- Avoided downtime = minutes avoided * downtime cost/min。
- Siemens 大型汽车工厂口径约等于 38k 美元/分钟。
- Tier-1 应用客户 chargeback、line-down claims、sort cost、premium freight 和 NCR/SCAR 历史数据估算。

## Go-To-Market

90 天只证明一件事：一个线束族的 EOL 异常关得更快、更干净、更可追溯。

试点设计：

1. 锁定一个 KPI owner、一个线束族、1-3 个测试/数据源和一套闭环 SLA。
2. 2 周 baseline：EOL FPY、rework hours、Top Pareto defects、false fail、8D SLA、trace coverage。
3. 4-8 周 live：接入 tester/vision/MES/QMS/返工证据，每周输出 Pareto 和 ROI。
4. 结题：输出 value-analysis packet 给采购，包含 dollars saved、before/after、8D closure evidence 和扩展路径。

90 天 KPI：

- EOL first-pass yield 提升 2-5 个点。
- Rework hours / 100 harnesses 下降 20-40%。
- Top 3 repeat EOL failure modes 下降 30%。
- False-fail / no-trouble-found 下降 15-30%。
- Defect detection-to-containment same shift 或小于 24 小时。
- 8D SLA：围堵小于 24 小时，根因/PCA 计划小于 14 天，验证关闭小于 30 天。
- Customer PPM / escaped defects on pilot family 出现下降趋势或 zero escapes。
- Traceability coverage：95%+ pilot harnesses 将 EOL 结果关联到 build lot、operator、tester、fixture 和 closure evidence。

## Competition

设计软件管上游，MES/QMS 管流程，机器人公司管动作；跨系统闭环证据层没人真正拥有。

- Siemens Capital / Zuken / ECAD：强在设计和制造文档，弱在现场异常、返工证据和供应商协同闭环。
- Q5D / Komax / Agile Robots / FAPS：强在动作、设备和自动化 cell，弱在跨工位、跨供应商、跨车型的商业闭环模型。
- CAMI / Cirris / Vitrek / EOL testers：强在 continuity、HiPot、insulation 和测试报告，弱在责任、返工、签核、chargeback 和训练样本。
- MES / QMS：强在生产记录和 CAPA 流程，弱在线束语义、传感器证据、测试图谱和 HIL 数据。
- Vision inspection：强在 terminal seating / occupancy 检测，弱在把检测失败转成闭环责任。

定位：

> HarnessLoop makes Q5D/Komax/Agile-style cells, guided assembly, vision and EOL testers easier to deploy, validate and continuously improve.

## Moat

护城河不是模型参数，而是线束异常到关闭结果的数据结构。

会积累的资产：

- Harness Graph：连接器、孔位、端子、线束分支、车型变体、工位、供应商、tester 和测试项。
- Evidence Corpus：before/after 图片、导通矩阵、力曲线、HIL 片段、复测和签核记录。
- Recovery Episodes：每次人工修复都不是丢失的现场经验，而是下一轮 LeRobot 训练和边缘 profile 的样本。
- Supplier Network：从单站点扩到 OEM/Tier-1/连接器供应商，网络越大，重复问题越早被发现和围堵。
- Closure Benchmarks：按 harness family、defect type、supplier、tester 和 closure SLA 形成运营基准。

## Architecture

比赛版本使用 5-24V current-limited 低压桌面线束板，不接触真实 EV 高压。

### Fixture

- 2-3 个 mock automotive connectors。
- 12-24 个 cavities。
- Keyed non-conductive nests。
- Pogo/spring probes。
- LED cavity highlight。
- Muxed continuity matrix。
- Optional resistance metadata。
- Load cell or small F/T sensor。

### Robot / Control Plane

- ROS 2。
- 低力机械臂或 LeRobot-supported arm。
- 二指夹爪、软/触觉指尖、wrist camera。
- Load cell / wrist F/T。
- 3D 打印线束板、clip、低压连接器、pogo pin / JST / Molex 类测试座。

ROS 2 topics:

- `/camera/overhead/image_raw`
- `/camera/wrist/image_raw`
- `/wrist_ft`
- `/joint_states`
- `/continuity/result`
- `/harness/route_state`
- `/connector/insertion_curve`
- `/exception/event`
- `/hil/state`

### Edge AI / Exception Plane

- Qualcomm RB3 Gen 2 / QCS6490 类设备运行本地视觉、异常分类和证据打包。
- AI Hub / QNN / QAIRT 用于固定输入模型的 compile/profile/quantize。
- 云端训练，边缘推理；不声称 Qualcomm 现场训练整套机器人策略。
- 模型建议，导通图决定。
- PASS 必须匹配 nominal graph 且无 open/short/bridge。

### Dataset

- ROS bag 作为原始同步数据。
- LeRobotDataset v3 保存 state/action、视频、Parquet 和 metadata。
- HIL 记录 pause、takeover、recovery、return-to-policy 和 quality result。

## Competition Demo

3 分钟演示一个完整闭环：从错孔到导通验证通过。

1. Operator 扫描 mock harness，UI 加载 connector/cavity graph，并显示 safe low-voltage fixture status。
2. 故意把一个 terminal 放错 cavity 或制造 open circuit。
3. 相机识别连接器方向/孔位，导通矩阵报 `A03 -> B07 expected, observed B08` 或 `C12 open`。
4. Qualcomm edge inference 本地运行视觉/异常分类，图谱映射到具体 cavity 并提示 closure step。
5. 操作者暂停策略并通过 LeRobot 接管，移动 dummy terminal 或探针对准正确 cavity。
6. Load cell/F/T 记录 seating/force trace，episode 记录 human recovery。
7. Retest：导通图从 fail 变 pass，复拍视觉状态，系统保存 force/load trace 和 before/after。
8. Learning loop：episode 进入 LeRobotDataset，云端 fine-tune classifier/policy，compact model export/profile 到 Qualcomm edge。

## Why Qualcomm

Qualcomm 不只卖智能车大脑，也应该守住智能车的物理神经系统。

- 相机、load cell/F/T、导通矩阵和异常证据在工位本地融合，不适合全部上云。
- Qualcomm 已在智能座舱、ADAS 和 SDV 中进入车厂；HarnessLoop 把价值延伸到制造质量。
- 中国 NEV 产量、出口、供应链深度、数据本地化和快速发布周期，让本地 edge-first 方案更有说服力。
- AI Hub、QNN/QAIRT、LeRobot HIL、ROS 2 和云训练可以被包装成真实商业产品路径。

## Ask

比赛阶段需要一个线束异常闭环样板，而不是真实汽车产线。

需要：

- RB3 Gen 2 / QCS6490 类开发板。
- 低力机械臂。
- 双相机。
- Load cell / F/T。
- MCU 导通矩阵。
- 3D 打印线束板。
- 彩色线束。
- 2-3 个低压连接器。
- 12-24 个 cavity。
- Pogo pin。
- LED highlight。
- ROS 2 / LeRobot adapter。
- AI Hub / QNN profile 支持。
- 2-3 位线束质量、EOL 测试、SQE/8D 顾问。

## Claims To Avoid

- 不说全自动汽车线束装配。
- 不说真实 EV 高压验证。
- 不说 ASIL、ISO 26262、ISO 6469、IPC/WHMA-A-620、PPAP 或 OEM 量产合规已完成。
- 不说 QNN 跑完整 LeRobot/VLA policy，除非实际转换、compile、profile 和 verified。
- 不说任意连接器全自动插接。
- 不说视觉模型是质量最终判定；质量 gate 是导通/映射图和人工签核。
- 不说力曲线单独证明产品质量。
- 不说无人关闭异常；应说 operator approval 或 evidence-backed closure recommendation。
- 不说桌面 demo 已验证生产节拍提升。

## Sources

- IEA Global EV Outlook 2026：https://www.iea.org/reports/global-ev-outlook-2026/executive-summary
- Xinhua / CAAM 2025 NEV：https://www.news.cn/fortune/20260114/cbbd861081c349d8ae238167ca418fa3/c.html
- Xinhua / CAAM May 2026：https://www.news.cn/fortune/20260610/24116a9f8ff14182a8c052eb4d380392/c.html
- Xinhua English NEV May 2026：https://english.news.cn/20260610/8ddd911ea0fe477287e3bb37f6839cd1/c.html
- China auto recall 2025：https://www.samrdprc.org.cn/xwdt/gzdt/202603/t20260320_115273.html
- Q5D automated harness production：https://q5d.com/news/fully-automated-wire-harness-production-demonstrated/
- Q5D HaaS：https://q5d.com/product/haas/
- Komax harness manufacturing：https://www.komaxgroup.com/en-us/products/wire-processing/higher-automation-platforms/harness-manufacturing
- Q5D funding：https://q5d.com/news/q5d-secures-13-5-million-in-funding-for-wiring-automation-including-series-a-venture-round-led-by-lockheed-martin/
- Agile Robots harness challenge：https://www.agile-robots.com/en/news/detail/robotik-challenge-2025-the-solution-behind-the-award/
- FAPS Robotik Challenge：https://www.leitungssatz-hub.de/en/robotik-challenge/robotik-challenge-2025/ergebnisse-der-robotik-challenge/
- Robotic connector mating paper：https://arxiv.org/html/2503.09409v2
- Wire harness automation survey：https://arxiv.org/html/2309.13744v3
- Cable routing robotics：https://lianwenzhao.github.io/cable_routing.pdf
- Aptiv EDS separation：https://www.aptiv.com/en/newsroom/article/aptiv-announces-intention-to-separate-its-electrical-distribution-systems-business
- Versigent launch：https://ir.versigent.com/news/news-details/2026/Versigent-Launches-as-New-Publicly-Traded-Company/default.aspx
- Versigent investor presentation：https://s21.q4cdn.com/812040547/files/doc_presentation/Versigent_Investor_Presentation.pdf
- Luxshare / Leoni：https://www.leoni.com/press/press-releases/luxshare-increases-shareholding-in-leoni-ag
- GB/T 37133-2025：https://std.samr.gov.cn/gb/search/gbDetailed?id=2FF37940EB8DD753E06397BE0A0A413F
- Siemens downtime study：https://assets.new.siemens.com/siemens/assets/api/uuid:1b43afb5-2d07-47f7-9eb7-893fe7d0bc59/TCOD-2024_original.pdf
- WarrantyWeek auto warranty：https://www.warrantyweek.com/archive/ww20250911.html
- NHTSA recall example：https://static.nhtsa.gov/odi/rcl/2025/RCLRPT-25V769-7927.pdf
- Harness testing methods：https://vitrek.com/wire-harness-testing-methods-continuity-hipot-and-insulation-resistance-explained/
- Harness test fixtures：https://wiringharnessnews.com/wire-harness-testing-evolution-and-the-advent-of-test-fixtures/
- IEC SELV glossary：https://products.iec.ch/view/glossary/ff408fdf27132bf5a1924ffefd02220c
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/general_introduction.html
