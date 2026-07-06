# TouchForge 触觉力控技能工厂 Pitch

更新时间：2026-07-06。

## One-Line Company

TouchForge 是跨硬件的接触技能层：

> 把触觉、力/力矩、视觉、关节状态、人工接管和质量结果变成可复用的插接、压合、拧紧、柔性抓取和仓储拣选技能；云端训练，Qualcomm edge 本地推理，让每次触碰都可控、可追溯、可改进。

它不卖单一触觉传感器、夹爪、灵巧手或人形机器人。它做的是 contact-skill operating layer。

## YC-Style Opening

机器人会看、会走，却会在最后一毫米卡住生产。

工厂和仓库已经买了机器人、相机、夹爪、F/T 传感器和安全 PLC，但最贵的失败常常发生在接触瞬间：

- 连接器半插。
- FPC / 线束弯折。
- 压装不到位或过力。
- 螺丝滑牙或交叉螺纹。
- 柔性件打滑。
- 易损件刮伤。
- 仓储拣选掉落。

TouchForge 把这些失败变成可记录、可回放、可训练、可部署的接触技能。

## Problem

视觉自动化能把机器人带到零件旁边，但不能保证插进去、压到位、拧好、不刮伤。

- 停线来自最后一毫米：机器人到达位置后，一个错位插接、过力压合或滑牙螺丝就会触发停线、返工、报废和人工介入。
- 质量证据不够细：很多工位只记录 pass/fail 或终点值，没有把力位曲线、触觉热图、接管动作和质量结果绑定到每个周期。
- 每个项目重新集成：换机器人、换夹爪、换触觉传感器、换 SKU 后，轨迹、阈值、恢复策略和日志格式往往重新来。
- 大模型缺接触闭环：机器人基础模型需要真实触觉、力控、失败恢复和质量标签，而不是只靠互联网视觉和漂亮 demo。

## Why Now

2025-2026 年的信号很清楚：

- Physical Intelligence 发布 π0.7 和 RLT，强调跨机器人迁移和插入、拧螺丝等接触任务。
- Skild AI 2026 年融资 14 亿美元，主张 one brain for any robot/task。
- Google DeepMind Gemini Robotics 1.5 和 ER 1.6 把 embodied reasoning 与动作模型拆开推进。
- NVIDIA 推出 Physical AI Data Factory Blueprint，把有限真实数据扩成模型可用数据。
- Amazon Vulcan 把触觉/力反馈带进仓储生产，宣称可处理约 75% 商品。
- GelSight/DIGIT、XELA、PaXini、Daimon、Unitree、Shadow、Robotiq、ATI 等让触觉/力控硬件快速丰富。
- IFR 数据显示中国 2024 年新增工业机器人 29.5 万台，占全球 54%，运行存量超过 200 万台。
- IEA 数据显示中国 2024 年 EV 产量约 1240 万辆，占全球 70%+，带来电池、电驱、总装、质检和物流接触作业需求。
- 中国 2026 实景实训行动明确要求真实机器人数据、全身轨迹、力位控制曲线、操作序列和时序逻辑。
- Siemens downtime report 估算汽车行业非计划停机成本可达约 230 万美元/小时。

## Insight

不要再做一个机器人脑，先把昂贵、重复、可验收的接触动作产品化。

> 客户不会为“触觉很酷”付费，也不会因为通用机器人愿景下单；他们会为连接器一次插对、压装曲线合格、螺丝不滑牙、柔性件不掉、异常可回放、12 个月内回本付费。

## Solution

TouchForge 是跨硬件的触觉智能层，把每次接触变成可部署技能。

它把 GelSight/DIGIT/XELA/AnySkin/Unitree/Shadow/ATI/Robotiq/OnRobot 等不同硬件的触觉和力数据标准化，连接 LeRobot HIL、云 GPU 训练、Qualcomm edge runtime 和工厂 KPI：

1. Normalize：把触觉图、wrist F/T、马达电流、RGB、动作、夹爪状态和 MES/质检结果对齐到同一条 episode。
2. Forge：用 LeRobotDataset v3、BC/ACT/HIL-SERL 和云 GPU 训练接触策略、成功判别器和异常检测器。
3. Deploy：将可 profile 的触觉 encoder、reward classifier 或小策略经 AI Hub / QNN / QAIRT 部署到 Qualcomm edge。
4. Improve：每次打滑、卡滞、过力、接管、恢复和质量结果都进入下一轮 skill update。

## Product

第一版只卖三个东西：

> Contact Data Pipeline + Skill Pack + Quality Evidence Dashboard

第一版不追求泛化到任意机器人和任意零件。它先在夹具、低速、低力和明确安全边界内，把一个昂贵接触任务做成可采购、可验收、可复用的产品。

核心 workflow：

1. Instrument：给工位加 wrist F/T、触觉指尖、前视/腕部相机、关节/电流遥测和安全限位。
2. Record：操作员示教、接管和纠错，系统记录成功、失败、恢复、force signature 和质量标签。
3. Train：云端训练 BC/ACT/HIL-SERL 策略、成功判别器、触觉 encoder 和异常 force/tactile signature。
4. Deploy：导出固定形状模型，AI Hub profile 后将小模型或 encoder 部署到 QNN/QAIRT edge runner。
5. Prove：每个周期输出力位曲线、触觉摘要、最大力、接管记录、质量结果和 ROI 报表。

## Market Wedge

先做一类高 ROI 接触动作，不从万能灵巧手开始。

最好的第一批客户不是想看 demo 的展厅，而是已经因为错误接触付钱的 3C、EV、汽车零部件、医疗器械和仓储自动化团队。

第一批技能包：

- 连接器 / FPC 插入：半插、针脚弯曲、线束变形和下游测试失败，适合力曲线、触觉状态和恢复策略闭环。
- 扭矩受限拧紧：错位、滑牙、错扭矩、漏打和交叉螺纹，用轴向力、电流、扭矩和视觉共同判断。
- 压合 / 卡扣：压力过大损坏零件，压力不足导致装配不良，force-displacement signature 是天然证据。
- 柔性/易损抓取：打滑、变形、刮伤、掉落和包装损坏，触觉 slip score 和夹持调整能直接创造 ROI。
- 3C / EV 装配：中国切口是平板测试上下料、连接器/FPC、线束、胶合、精密搬运和电池压装。
- 仓储拣选：不规则、反光、软包和易损 SKU 的掉落/错拣是触觉机器人早期商业场景。

## Business Model

采购语言不是“触觉很先进”，而是少停线、少报废、少返工、少人工异常。

收入模型：

> paid KPI pilot + per-cell/per-robot runtime subscription + integration/OEM channel + optional success fee

建议价格：

- 90 天工厂 cell 试点：35k-75k 美元，覆盖一个接触任务族、数据采集、技能调优和 ROI 报告。
- 90 天仓储 flow 试点：50k-150k 美元，覆盖 WMS/exception integration 和人机协同流程。
- 运行订阅：按 cell、机器人或工作流订阅，包含技能 runtime、漂移监测、失败回放、模型更新和质量报表。
- No-CapEx 选项：与集成商/OEM 打包 RaaS，降低一次性采购阻力，把付费绑定到产线可用性和支持 SLA。
- 成功费：对经验证的停机、报废、返工、人工异常和仓储 exception 下降收取 success fee。

ROI 公式：

`Monthly net benefit = labor savings + avoided downtime + avoided scrap/rework/warranty + added contribution margin from throughput + warehouse exception savings - TouchForge recurring cost - incremental robot/support cost`

`Payback months = upfront pilot/integration cost / monthly net benefit`

细分：

- Warehouse exception savings = monthly picks * exception rate reduction * minutes per exception / 60 * loaded labor rate。
- Quality savings = monthly units * baseline defect rate * defect reduction * cost per defect。
- Downtime savings = downtime hours avoided * cost per downtime hour。

90 天 KPI：

- Uptime、MTBF、MTTR、unplanned stops。
- Cycle time、units/hour、OEE availability/performance。
- First-pass yield、scrap rate、rework hours、defect escapes。
- Connector：half-mate rate、bent-pin rate、insertion force pass rate、retry rate。
- Screwdriving：torque/angle pass rate、missing/cross-thread/stripped screw detections。
- Press-fit：force-displacement pass rate、seating-depth pass rate、trace record completeness。
- Fragile handling：damage rate、drop/slip rate、force-limit violations、SKU coverage。
- Warehouse：picks/hour、first-attempt pick success、human intervention rate、teleop minutes/1k picks、cost per pick。
- Deployment：time to teach new SKU/task、changeover time、operator interventions、data completeness。

## Go-To-Market

90 天证明：接触失败下降，力/触觉证据可追溯，12 个月内回本。

试点设计：

1. 2 周 baseline：记录缺陷、报废、停机小时、人工介入、cycle time、质量证据完整率。
2. 4-6 周数据采集：收集示教、失败、恢复、人工接管和 quality outcome。
3. 2-4 周 shadow / limited production：跑 10 个班次或 10k 周期。
4. 每周报告：将接触失败、力曲线、触觉状态、异常恢复和质量结果转换成 CFO/Plant Manager 能读的 ROI。
5. 扩展路径：从一个接触任务族扩到相邻 SKU、相邻 cell、同类工厂和 OEM/集成商渠道。

## Competition

传感器公司卖手指，大模型公司卖大脑，TouchForge 卖能通过 KPI 验收的接触技能。

- Foundation models：Physical Intelligence、Skild、Google DeepMind、NVIDIA、Covariant 推动通用模型；TouchForge 提供最后一毫米的真实接触数据和 edge skill。
- Tactile / force hardware：GelSight、DIGIT、XELA、Daimon、PaXini、Unitree、Shadow、Robotiq、OnRobot、ATI 覆盖硬件层；TouchForge 不和它们抢 BOM，而是让它们的数据可训练、可部署、可验收。
- Humanoid / robot bodies：Figure、Apptronik、Agility、AgiBot、UBTech、Unitree、Fourier 负责本体和应用部署；TouchForge 让它们在接触任务上更快通过 KPI。
- Integrators：传统集成商交付单个 cell；TouchForge 把每次交付变成标准 episode、skill pack、评测和更新。
- LeRobot / academic benchmarks：社区强在标准和研究；TouchForge 做商业工位 KPI、OT 日志和 ROI 报告。

定位：

> We make robot hands reliable by turning every touch, slip, jam, failed insertion and human recovery into deployable edge skills.

## Moat

壁垒是跨硬件接触 episode 到质量结果的闭环数据。

会积累的资产：

- Contact Episodes：视觉、触觉、F/T、马达电流、动作、夹爪状态、干预标记和质量结果同步成可训练 episode。
- Failure Replay：半插、过力、打滑、掉落、刮伤和 cross-thread 都成为可检索失败案例。
- Skill Library：插接、FPC、压合、拧紧、柔性抓取和易损件处理形成跨客户复用 primitive。
- Edge Profiles：固定序列长度、量化校准、QNN/QAIRT profile、回滚和软件门禁形成部署资产。
- Quality Evidence：每个周期的力位曲线、触觉摘要、最大力、接管、质量判定和 ROI 形成采购壁垒。

## Architecture

### Sensors

- Wrist force/torque sensor。
- Tactile skin arrays。
- GelSight / DIGIT-style vision tactile。
- Motor current and joint telemetry。
- Front RGB / RGB-D camera。
- Wrist RGB camera。

### Dataset

- ROS bags as lossless source。
- LeRobotDataset v3 as canonical training format。
- State/action/wrench/contact flags in Parquet。
- RGB and tactile MP4 streams。
- Metadata for skill, fixture, intervention, success/failure, calibration and quality result。

Suggested keys:

- `observation.images.rgb_front`
- `observation.images.rgb_wrist`
- `observation.images.tactile_left`
- `observation.wrench`
- `observation.state`
- `action`
- `teleop_action`
- `intervention_active`
- `reward`
- `success`
- `failure_reason`
- `quality_result`

### Training

- Collect 50-200 demos and recovery episodes per task variant。
- BC / ACT for the public demo。
- HIL-SERL as the improvement loop where safe and bounded。
- RGB/tactile encoders + proprio/F/T MLP + temporal head。
- Reward classifier / success classifier for traceable contact state。

### Edge Deployment

- Qualcomm edge for inference/profile, not live training。
- PyTorch/ONNX/TFLite -> AI Hub compile/profile/quantize。
- QNN/QAIRT or ONNX Runtime QNN policy runner。
- Conservative first target: tactile encoder, reward classifier, anomaly detector or small MLP policy。
- Keep full ACT fallback on CPU/GPU unless profiled.
- Fixed sequence lengths and representative calibration samples before quantization。

### Safety

- Policy publishes bounded EE delta/velocity。
- ROS 2 supervisor gates commands before `ros2_control` / MoveIt Servo。
- Workspace bounds。
- Joint limits。
- Speed limits。
- Force/torque thresholds。
- Watchdog timeout。
- E-stop and OEM safety independent from learning policy。
- Human takeover。

## Competition Demo

3 分钟 demo 只证明一件事：人类手感可以变成边缘运行的接触技能。

1. 低力桌面夹具、触觉夹爪、wrist F/T、两路相机、E-stop 和 dashboard。
2. 操作员遥操作一次轻量插接/压合，系统记录 RGB、触觉、F/T、电流、动作和干预标记。
3. 故意错位，机器人检测 rim contact、force spike 或 tactile heatmap 异常。
4. 人工接管做小范围搜索/校正，恢复后交还策略，LeRobot 记录 recovery episode。
5. 展示训练 artifact，不现场训练：demos + HIL corrections -> cloud GPU -> AI Hub profile -> QNN/QAIRT artifact。
6. Qualcomm edge box 本地运行小模型/encoder/判别器，机器人在夹具内完成受限动作。
7. 扰动零件，supervisor 限速/限力，人类短暂接管，恢复数据被记录。
8. Dashboard 输出 local inference latency、最大力、接触状态、接管时间和下一轮训练队列。

## Why Qualcomm

接触技能是 Qualcomm 机器人边缘 AI 的高价值工作负载。

- 接触控制不能把每个触觉帧、力曲线和动作决策发到云端等待。
- 低延迟多传感器融合适合 RB3 / RB6 / Dragonwing。
- AI Hub / QNN / QAIRT 可展示从模型到设备的 profile、部署和回滚。
- 工厂数据、失败回放和生产参数需要本地化/区域化部署。
- 商业上连接触觉传感、灵巧手、工业机器人、3C/EV 装配、仓储拣选和物理 AI 标准。

## Ask

比赛阶段需要一个可信、低风险、可复现的接触技能样板。

需要：

- RB3 Gen 2 / RB6 / Dragonwing dev kit。
- ROS 2 arm or LeRobot-supported arm。
- Wrist F/T sensor。
- Tactile fingertips or GelSight/DIGIT-style sensor。
- Two RGB cameras。
- Low-force insertion fixture、torque-limited fastener、soft object tray。
- 50-200 demos and failure/recovery episodes。
- AI Hub / QNN profile support。
- 2-3 位制造自动化、质量工程、OT/安全顾问。

## Claims To Avoid

- 不说通用灵巧。
- 不说工厂级螺丝/插接已完成。
- 不说零样本触觉操作。
- 不把马达电流说成标定力传感。
- 不说 Qualcomm edge 现场训练策略。
- 不说任意 VLA/Transformer 可直接跑 QNN。
- 不说 ROS 2 supervisor 等同安全控制器。
- 不说已获得安全人机协作认证。
- 不承诺跨任意机器人、夹爪、零件和传感器迁移。

## Sources

- Physical Intelligence π0.7：https://www.pi.website/blog/pi07
- Physical Intelligence RLT：https://www.pi.website/research/rlt
- Skild Series C：https://www.skild.ai/blogs/series-c
- Gemini Robotics 1.5：https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/
- NVIDIA Physical AI Data Factory：https://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development
- Amazon Vulcan：https://www.aboutamazon.com/news/operations/amazon-vulcan-robot-pick-stow-touch
- Apptronik Series A：https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a
- Tutor Data Factory：https://tutorintelligence.com/blog/building-a-100-robot-data-factory-toward-factory-ready-ai
- XDOF ABC-130k：https://huggingface.co/datasets/XDOF/ABC-130k
- IFR Global Robot Demand：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IEA EV Production：https://www.iea.org/reports/global-ev-outlook-2025/trends-in-the-electric-car-industry-3
- MIIT Real-Scenario Training：https://www.ncsti.gov.cn/kjdt/tzgg/202606/t20260609_249248.html
- AgiBot Factory Deployment：https://www.agibot.com/article/231/detail/60.html
- AgiBot production livestream：https://www.agibot.com/article/231/detail/83.html
- GelSight / DIGIT 360：https://www.gelsight.com/gelsight-and-meta-ai-introduce-digit-360-tactile-sensor/
- XELA uSkin：https://xelarobotics.com/press-release/xela-robotics-unlocks-enhanced-automation-for-humanoid-and-industrial-robots/
- Daimon DM-Tac W：https://www.dmrobot.com/en/product/p1/dm-tac-w.html
- Unitree Dex3-1：https://www.unitree.com/mobile/Dex3-1/
- Siemens downtime cost：https://assets.new.siemens.com/siemens/assets/api/uuid:1b43afb5-2d07-47f7-9eb7-893fe7d0bc59/TCOD-2024_original.pdf
- I-PEX CARA：https://corp.i-pex.com/en/product/cara
- Robotiq Screwdriving：https://robotiq.com/solutions/screwdriving
- Press-fit process control：https://amdmachines.com/blog/press-fit-assembly-process-control-and-monitoring/
- Peg-in-hole review：https://link.springer.com/article/10.1186/s10033-025-01349-w
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot ACT：https://huggingface.co/docs/lerobot/main/en/act
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobot HIL-SERL：https://huggingface.co/docs/lerobot/hilserl
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/general_introduction.html
- ROS 2 control joint limits：https://control.ros.org/rolling/doc/ros2_control/hardware_interface/doc/joint_limiting.html
- MoveIt Servo：https://moveit.picknik.ai/main/doc/examples/realtime_servo/realtime_servo_tutorial.html
