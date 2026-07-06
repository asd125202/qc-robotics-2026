# TouchForge 触觉力控技能工厂 Pitch

更新时间：2026-07-06。

## One-Line Company

TouchForge 让机器人学会拿捏：

> 把人类示教、触觉、力矩、视觉、失败回放和 LeRobot HIL 纠错铸成可部署的接触技能，让连接器插入、压合、柔性抓取、扭矩受限拧紧和易损件处理在 Qualcomm edge AI 上低延迟运行。

它不卖单一触觉传感器，也不声称通用灵巧手已完成。它做的是 last-centimeter contact skill factory。

## Problem

机器人不缺眼睛，缺手感。

- 工业机器人能到达零件附近，但失败发生在最后一厘米。
- 典型问题：插头半插、针脚弯曲、螺丝滑牙、压合过力、柔性件打滑、易损件刮伤、仓储拣选掉落。
- 传统集成商为每个工位调夹具、轨迹和阈值，换产品/机器人/传感器就重新来。
- 视觉、触觉、F/T、马达电流、动作、HIL 接管、质量结果和 MES 记录不在同一条 episode。
- 大模型缺真实接触数据、失败恢复和现场回放。

## Why Now

- Physical Intelligence 2025 年获 600M 美元 B 轮，机器人 foundation model 进入资本主赛道。
- Apptronik 2026 年 Series A 累计超过 935M 美元，并把资金用于产品化、客户部署和数据采集设施。
- Amazon Vulcan 2025 年将触觉机器人用于仓储拣选/上架。
- Tutor Intelligence、XDOF 等把 robot data factory / teleoperation data infrastructure 产品化。
- IFR 2026 数据显示中国运营中的工业机器人约 200 万台，是全球最大部署市场。
- 中国 MIIT/SASAC 2026 行动明确要求真实场景训练数据、力位曲线、异常扰动和时序逻辑。
- Qualcomm RB3 / Dragonwing / AI Hub / QNN 让云训练 + 边缘推理路径更可信。

## Insight

不要先做通用机器人脑，先把高价值接触动作变成可复用技能。

> 客户不会为“触觉很酷”付费，但会为连接器一次插对、螺丝不滑牙、柔性件不掉、力曲线可追溯、人工接管减少和小于 12 个月回本付费。

## Solution

TouchForge 是接触式操作的数据与技能工厂。

1. 给工位加 wrist F/T、触觉指尖、前视/腕部相机、马达电流和安全限位。
2. 操作员示教 50-200 次，系统记录成功、失败、恢复和低置信度。
3. 同步记录 RGB、触觉图、力/力矩、马达电流、动作、夹爪状态、失败原因和人工接管。
4. 用 LeRobotDataset v3、BC/ACT/HIL 纠错和云 GPU 训练，生成接触策略、成功判别器和异常检测器。
5. 导出固定形状 ONNX/PyTorch，经 AI Hub profile、QNN/QAIRT 或 ONNX Runtime QNN 部署到 Qualcomm edge。
6. 每个客户工位继续回收失败、恢复和质量结果，形成可复用 skill primitive。

## Product Workflow

状态对象：

- `skill_id`
- `task_family`
- `object_id`
- `fixture_id`
- `observation.state`
- `observation.images`
- `observation.tactile`
- `action`
- `intervention_active`
- `success_label`
- `failure_reason`
- `quality_result`
- `edge_profile`

流程：

1. Instrument workcell。
2. Demonstrate task。
3. Record multimodal episode。
4. Train compact policy。
5. Profile edge runtime。
6. Deploy skill。
7. Replay failures。
8. Update model。

## Market Wedge

第一批高 ROI 接触动作：

- 连接器插入：半插、针脚弯曲、线束变形、下游测试失败。
- 扭矩受限拧紧：错位、滑牙、错扭矩、漏打、交叉螺纹。
- 压合 / 卡扣：过力损坏、压力不足、装配不到位。
- 柔性/易损抓取：打滑、变形、刮伤、掉落、包装损坏。
- 3C / EV 装配：平板测试、连接器、线束、胶合、精密上下料、电池相关工位。
- 仓储拣选：不规则、反光、软包和易损 SKU。

## Business Model

收入模型：

> paid pilot + per-cell runtime + skill license + success fee

建议价格：

- 90 天试点：8.5 万美元/工位任务族，覆盖一个 cell、1-3 个 SKU/零件变体、数据采集、技能调优和 ROI 报告。
- 运行订阅：5k-12k 美元/cell/月，包含技能 runtime、漂移监测、失败回放、模型更新和质量报表。
- 按周期计费：高量客户每成功周期 0.005-0.03 美元。
- 成功费：达成 KPI 后收取 2 万美元 success fee；试点 50% 可抵扣年度订阅。

ROI 公式：

`Annual Savings = defect reduction * cost/defect * annual volume + scrap reduction * unit scrap cost + downtime hours avoided * downtime cost/hour + labor redeployment value + throughput contribution - TouchForge annual cost`

90 天 KPI：

- Connector / insertion：first-pass success >=99%，或插入失败下降 50%+，100% 力曲线可追溯。
- Screwdriving：cross-thread / missed-fastener / stripped-thread / torque NOK 下降 50%+。
- Fragile handling：掉落、刮伤、裂纹、变形报废下降 50-80%。
- Warehouse picking：first-attempt pick success >=98.5%，human exception touches 下降 30-50%。
- Economic gate：年化验证节省 >= 年度订阅 3 倍，回本小于 12 个月。

## Competition

TouchForge 不替代已有玩家：

- Physical Intelligence / Skild / Google DeepMind / NVIDIA：通用模型强；TouchForge 做接触数据、工位技能和 edge runtime。
- GelSight / XELA / Daimon / PaXini / Unitree：触觉和灵巧硬件强；TouchForge 做跨硬件 episode 和可部署技能。
- 传统集成商：单个 cell 交付强；TouchForge 把每次交付变成可复用数据和 skill primitive。
- LeRobot / RobOmni / academic benchmarks：标准和社区强；TouchForge 做商业工位 KPI 和 ROI 报告。

## Moat

壁垒是接触 episode 到质量结果的闭环数据。

会积累的资产：

- 视觉、触觉、F/T、马达电流、动作和干预标记同步成可训练 episode。
- 半插、过力、打滑、掉落、刮伤和 cross-thread 可检索失败案例。
- 插接、压合、拧紧、柔性抓取和易损件处理形成跨客户复用 primitive。
- 固定序列长度、量化校准、QNN/QAIRT profile、回滚和安全门禁部署资产。

## Architecture

### Sensors

- Wrist force/torque sensor。
- Tactile skin arrays。
- GelSight / DIGIT-style vision tactile。
- Motor current proxy。
- Front RGB camera。
- Wrist RGB camera。

### Dataset

- ROS bags as lossless source。
- LeRobotDataset v3 as canonical training format。
- State/action in Parquet。
- MP4/image streams。
- Metadata for skill, fixture, intervention, success/failure, calibration。

### Training

- Collect 50-200 demos per task variant。
- BC / ACT / small multimodal policy。
- RGB/tactile encoders + proprio/F/T MLP + temporal head。
- HIL correction episodes for fine-tuning。
- Optional HIL-SERL only for narrow bounded tasks。

### Edge Deployment

- Qualcomm edge for inference/profile, not live training。
- PyTorch/ONNX -> AI Hub compile/profile/quantize。
- QNN/QAIRT or ONNX Runtime QNN policy runner。
- Fixed sequence lengths。
- Representative calibration samples before quantization。

### Safety

- Workspace bounds。
- Speed limits。
- Force limits。
- E-stop。
- Fixture constraints。
- Human takeover。
- Learned model produces bounded setpoints; hard safety remains outside policy。

## Competition Demo

3 分钟 demo：

1. Low-force tabletop fixture, tactile gripper, wrist F/T, two cameras, E-stop, dashboard。
2. Operator teleoperates a short insertion attempt and deliberately corrects misalignment。
3. System records RGB, tactile, F/T, motor current, action and intervention metadata。
4. Bad start: policy approaches misaligned peg; contact rim creates force spike / tactile heatmap。
5. Human intervenes and performs small search correction。
6. System replays recovery episode and shows LeRobot dataset card。
7. Show AI Hub / QNN profile path and edge inference panel。
8. Robot completes chamfered peg insertion, soft grasp, or torque-limited screwdriving proxy within safe fixture。

## Why Qualcomm

TouchForge 是 Qualcomm 机器人边缘 AI 的高价值样板：

- 接触控制不能把每个触觉帧、力曲线和动作决策发到云端等待。
- 低延迟多传感器融合适合 RB3 / RB6 / Dragonwing。
- AI Hub / QNN / QAIRT 可展示从模型到设备的 profile、部署和回滚。
- 工厂数据、失败回放和生产参数需要本地化/区域化部署。
- 商业上连接触觉传感、灵巧手、工业机器人、3C/EV 装配和物理 AI 标准。

## Ask

比赛阶段需要：

- RB3 Gen 2 / RB6 / Dragonwing dev kit。
- ROS 2 arm or LeRobot-supported arm。
- Wrist F/T sensor。
- Tactile fingertips。
- Two RGB cameras。
- Low-force insertion fixture, torque-limited fastener, soft object tray。
- 50-200 demos and failure/recovery episodes。
- AI Hub / QNN profile support。

## Claims To Avoid

- 不说通用灵巧。
- 不说工厂级螺丝/插接已完成。
- 不说零样本触觉操作。
- 不把马达电流说成标定力传感。
- 不说 Qualcomm edge 现场训练策略。
- 不说任意 PyTorch 模型可直接跑 QNN。
- 不说已获得安全人机协作认证。
- 不承诺跨任意机器人、夹爪、零件和传感器迁移。

## Sources

- Amazon Vulcan：https://www.aboutamazon.com/news/operations/amazon-vulcan-robot-pick-stow-touch
- Apptronik Series A：https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a
- Tutor Data Factory：https://tutorintelligence.com/blog/building-a-100-robot-data-factory-toward-factory-ready-ai
- IFR China robots：https://ifr.org/ifr-press-releases/news/china-makes-ai-powered-robots-core-of-national-strategy
- AgiBot factory deployment：https://www.agibot.com/article/231/detail/60.html
- Unitree Dex3-1：https://www.unitree.com/mobile/Dex3-1/
- Siemens downtime cost：https://assets.new.siemens.com/siemens/assets/api/uuid:1b43afb5-2d07-47f7-9eb7-893fe7d0bc59/TCOD-2024_original.pdf
- Peg-in-hole review：https://link.springer.com/article/10.1186/s10033-025-01349-w
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/general_introduction.html
