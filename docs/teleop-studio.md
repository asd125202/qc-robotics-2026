# TeleopStudio Pitch

更新时间：2026-07-06。本页按 YC / Airbnb 风格重写：问题、现有替代方案为什么失败、解决方案、为什么现在、产品、证据 API、市场、竞争壁垒、为什么 Qualcomm、演示和请求。

## One-Line Pitch

TeleopStudio 是机器人学习的数据入口：一台 Qualcomm-first 遥操作和示教数据工位，把人类操作、相机、状态、动作、失败接管和质量门禁变成可训练、可审计、可交给 TrainRouter 的 LeRobot episode。

## Thesis

未来商业机器人公司的核心资产不是“某次 demo 跑通了”，而是持续生产高质量 real-world episodes 的能力。TeleopStudio 要做的是 embodied AI 时代的“数据工厂工位”：像拍电影有摄影棚、场记和质检一样，机器人学习也需要标准化 capture cell、operator workflow、edge recorder、quality gate 和 dataset handoff。

## 01 · Problem

机器人团队今天的问题不是不会录视频，而是录出来的数据不能稳定训练、不能复现、不能审计、不能交付给客户。

典型失败链路：

- 相机、关节、夹爪、底盘、teleop input 和安全事件没有统一时间轴。
- reset 协议靠人记，下一条 episode 的起点和目标发生漂移。
- 失败、接管、碰撞前停止、遮挡和人类修正没有结构化标签。
- metadata 不完整，训练前才发现 robot profile、camera calibration、action schema 或 task prompt 缺失。
- 操作员质量差异巨大，但团队只统计“录了多少小时”，不统计“每小时有效 episode 产出”。
- 坏 episode 直接进入 GPU 训练，CloudTwin、TrainRouter、SkillCertKit 和 Qualcomm edge release 都被污染。

一句话：没有数据生产线，就没有机器人软件平台。

## 02 · Current Alternatives Fail

现有方案都解决了一部分，但没有把“遥操作到可训练 episode”做成商业化入口。

### DIY MP4 / ROS bag

能记录，但不等于可训练。视频、状态、动作、时间戳、标定、任务语言、成功/失败和隐私规则没有形成一个 dataset contract。到训练阶段才清洗，成本最高。

### LeRobot / phosphobot

它们是非常重要的开源底座，解决了 teleop、record、dataset、train 的开发者流程；但商业客户还需要固定工位、质量门禁、操作员管理、数据地域、审计证据、Qualcomm edge recorder 和售后支持。

### ALOHA / Trossen / GELLO / UMI / Open-TeleVision / DexCap

它们证明了高质量示教和更好输入设备的价值，但大多聚焦硬件、控制方式或研究系统。客户仍然要自己拼接 dataset schema、QC、云训练、模型 release 和现场交付。

### DROID / Open X-Embodiment

它们证明大规模真实机器人数据集很重要，但不能替代每个公司自己的场景数据、客户任务、硬件 profile 和合规边界。

### Formant / Viam / Foxglove / Rerun

它们强在 fleet ops、远程控制、日志和可视化；TeleopStudio 的切入点更窄：把 human-in-the-loop session 变成 model-ready dataset 和训练合约。

### Scale / Encord / Labelbox Terra

它们说明 physical AI data 正在成为企业级服务，但对很多机器人初创、实验室、OEM 和系统集成商来说，第一步需要的是可购买、可本地部署、可复用的采集工位，而不是一次性的黑盒数据外包。

## 03 · Solution

TeleopStudio = `Operator Station + Capture Cell + Qualcomm Edge Recorder + Quality Gates + LeRobot Adapter + TrainRouter Handoff`。

核心不是再做一个遥控器，而是把每次遥操作变成结构化生产事件：

- 先定义任务、成功标准、变化维度、reset 协议和目标样本量。
- 操作员在固定工位完成示教或 HIL 接管。
- Qualcomm edge recorder 同步记录多相机、state/action、teleop input、时间戳、安全事件和本地缓存。
- QC gate 在采集时拒绝坏数据：遮挡、丢帧、短 episode、metadata 缺失、timestamp skew、action jitter、隐私风险。
- 通过 LeRobotDataset v3、MCAP/ROS bag、manifest、dataset card 和 TrainRouter job contract 导出。
- 训练、评测和 edge deployment 结果回流，指导下一轮采集哪些失败片段。

产品承诺不是“自动获得好模型”，而是“把真实示教数据的产出率、可复现性和可训练性变成可管理指标”。

## 04 · Why Now

四个趋势让这个产品现在可做：

1. **LeRobot 标准化了开发者路径**：真实机器人 teleoperation、record、visualize、train、evaluate 和 dataset v3 已经成为可以接入的开源基座。
2. **Physical AI 的瓶颈转向真实数据**：ALOHA、Mobile ALOHA、DROID、Open X-Embodiment 让行业看到真实示教和跨场景数据的价值。
3. **数据服务正在商业化**：Scale、Labelbox Terra、Encord 等玩家把 collection、labeling、teleop 和 evaluation 推向企业预算，说明客户愿意为 physical AI data 付费。
4. **Qualcomm edge 已经适合做数据原点**：Dragonwing / RB3 / QCS6490 的多相机、视频编码、NPU 推理、AI Hub、QNN 和 profiler 能把采集、质检、隐私过滤和部署证据放在机器人旁边。

过去是“先造机器人，再临时录点数据”。现在应该倒过来：先把数据工位产品化，机器人能力才有持续改进的基础。

## 05 · Product

### 5.1 Operator Station

支持手柄、leader arm、SpaceMouse、键鼠、移动端或 XR 输入。比赛阶段优先选择最稳定的本地工位，后续扩展远程专家、多人排班和跨站点采集。

### 5.2 Capture Cell

桌面机械臂、样品托盘、固定光照、相机支架、标定板、reset tray 和任务道具。第一批任务聚焦样品转移、扫码、分拣、按钮/抽屉/门把手、实验室耗材搬运等窄任务。

### 5.3 Qualcomm Edge Recorder

端侧负责：

- 多相机 ingest 和低延迟预览。
- H.264/H.265 编码、本地缓存和断网保护。
- state/action/teleop input 时间戳对齐。
- dropped frame、timestamp skew、action jitter、camera visibility 和存储压力记录。
- 本地隐私过滤、blur/occlusion 检测和低成本质量评分。
- 每条 episode 的 hash、manifest 和 evidence receipt。

### 5.4 Quality Gates

采集时实时决定接受、拒绝或转人工复核：

- `frame_count_ok`
- `camera_visibility_ok`
- `timestamp_skew_ms`
- `dropped_frame_rate`
- `action_state_schema_ok`
- `reset_protocol_ok`
- `success_label_present`
- `takeover_segment_tagged`
- `privacy_gate_passed`
- `trainability_score`

### 5.5 LeRobot Adapter

输出 LeRobot-compatible dataset，并保留 robot profile、camera profile、task language、episode boundaries、operator、success/failure、takeover segments、dataset stats 和 dataset card。

### 5.6 Cloud Handoff

合格 episode 进入 TrainRouter，按 China / Overseas / private lane 选择 GPU、数据地域、预算、评测 gate 和 Qualcomm target profile。训练结果再进入 EdgeRuntimeBench、SkillCertKit 和 SkillDock。

## 06 · Product API/Evidence

TeleopStudio 的商业价值要落在数据合约，而不是页面截图。

### Episode Object

```json
{
  "episode_id": "ep_20260706_lab_pick_00042",
  "task_id": "sample_transfer_v1",
  "operator_id": "operator_07",
  "robot_profile": "so_arm101_qcs6490_station_v1",
  "camera_profile": "front_wrist_overhead_v1",
  "action_schema": "joint_delta_gripper_v1",
  "segments": ["demo", "pre_intervention", "intervention", "recovery", "success"],
  "quality": {
    "timestamp_skew_ms_p95": 18,
    "dropped_frame_rate": 0.003,
    "trainability_score": 0.87,
    "privacy_gate": "passed"
  },
  "exports": {
    "lerobot_dataset": "hf://org/task_dataset_v3",
    "raw_mcap": "s3://private-bucket/raw/ep_00042.mcap",
    "trainrouter_job": "job_20260706_0912"
  }
}
```

### Evidence Bundle

首版每次采集批次都要生成：

- `raw_recording.mcap`：原始 topic、camera info、TF、metadata、attachments、hash。
- `episode_manifest.parquet`：episode、step、segment、operator、task、policy、robot、camera、success/failure。
- `qa_report.json`：missing topic、frame drop、timestamp skew、lag、jitter、calibration、takeover rate、success rate、privacy gate。
- `dataset_card.md`：motivation、composition、collection、preprocessing、license、limitations、maintenance。
- `trainrouter_job_contract.yaml`：dataset hash、cloud lane、budget、eval suite、target Qualcomm profile。
- `qualcomm_edge_capture_profile.yaml`：board、SDK/runtime、camera、codec、thermal/power assumptions、run count。

### Segment Taxonomy

`demo / autonomous / pre_intervention / intervention / recovery / failure / abort / success`

这让失败片段不再被丢掉，而是成为下一轮 HIL fine-tuning 的高价值数据。

## 07 · Market & Business Model

客户买的不是遥操作按钮，而是更快得到可训练数据和可交付 demo。

### Beachhead Customers

- 具身智能和机器人初创：需要把融资 demo 变成可复现产品能力。
- 高校和企业实验室：需要课程、论文、复现实验和硬件平台。
- Robot OEM：希望自己的机械臂、夹爪、移动底盘更容易变成 AI-ready kit。
- 系统集成商：需要把客户现场任务快速采集、训练、评估和试点。
- 数据工厂和城市创新中心：需要采集 SOP、质量统计、操作员管理和本地部署。

### Overseas Packages

- Developer / BYO robot：`$2k-$6k/year`，软件、recorder、dataset export、ROS 2/Python adapters。
- Education / starter station：`$6k-$12k`，低成本 arm、相机、edge box、课程和支持。
- Research station：`$12k-$35k`，单臂/双臂、leader arm 或 handheld teleop、QC tooling。
- Pro data collection station：`$35k-$80k`，多相机、数据管理、私有存储、企业支持。
- Enterprise data ops：`$20k-$100k/year` 平台费，加 station 月费、存储、compute 和 professional service。

### China Packages

- Starter / education：`¥30k-¥80k`，中文课程、本地硬件、基础支持。
- Lab station：`¥80k-¥250k`，研究工位、边缘采集、LeRobot/TrainRouter 联动。
- Pro data collection station：`¥250k-¥600k`，多工位、操作员管理、质检、私有部署。
- Data factory / OEM：`¥100k-¥500k/year` 平台费，加每工位月费、现场集成、培训和 SLA。

### Wedge

先卖给“已经有机器人，但缺数据生产线”的团队。交付口径不是“训练一个万能机器人”，而是 4-8 周内把一个明确任务从 `50 条合格 episode` 做到 `可训练、可评测、可部署证据包`。

## 08 · Competition & Moat

TeleopStudio 不声称自己是第一个遥操作平台。它的差异是把数据质量、证据和 Qualcomm edge profile 放在遥操作入口。

### Competitive Map

- **Open-source learning stack**：LeRobot、phosphobot。
- **Teleop hardware and kits**：Trossen ALOHA、GELLO、UMI、Open-TeleVision、DexCap。
- **Fleet/cloud ops**：Viam、Formant。
- **Visualization and logs**：Foxglove、Rerun、MCAP tooling。
- **Simulation and GPU-first stack**：NVIDIA Isaac、GR00T、Cosmos。
- **Enterprise physical AI data service**：Scale、Labelbox Terra、Encord。

### Moat

短期壁垒：

- 任务模板、reset protocol、variation plan 和 dataset card。
- Qualcomm edge recorder profile。
- QC gate rules 和 episode schema。
- LeRobot / MCAP / TrainRouter adapters。

中期壁垒：

- operator valid-yield benchmark。
- failure / takeover taxonomy。
- dataset lineage 和 replay-eval history。
- 不同行业任务的采集 SOP。

长期壁垒：

- 哪些任务、相机、硬件、operator pattern、dataset quality 和 policy 组合能稳定部署到哪些 Qualcomm edge target。
- 从采集、训练、评测、部署、事故回放到再采集的 skill release graph。

## 09 · Why Qualcomm

Qualcomm 不应该只出现在机器人学习闭环最后的“推理部署”阶段。TeleopStudio 让 Qualcomm 成为数据原点。

### Why It Matters To Qualcomm

- 多相机采集、视频编码、低延迟预览、端侧缓存、隐私过滤和质量检查都是 Dragonwing / RB3 / QCS edge 的真实 workload。
- AI Hub / QNN / QAIRT / ONNX Runtime QNN 的价值会更强，因为它们从一开始就绑定 episode lineage 和 target profile。
- Qualcomm 可以把“LeRobot capture to Qualcomm edge deployment”做成开发者生态样例，区别于纯 GPU-first 叙事。
- 如果 Qualcomm 支持数据工位标准，后续 OEM、系统集成商、教育套件和 data factory 都会围绕 Dragonwing board 选型。

### 6-8 Week Qualcomm Validation Sprint

请求支持：

- RB3 Gen 2 Vision Kit 或等价 QCS6490 / Dragonwing 开发板。
- 多相机 ingest、timestamp、encoding、preview、storage 和 thermal 指导。
- Qualcomm Linux / IM SDK / GStreamer / QNN office hour。
- AI Hub compile/profile/deploy 路径 review。
- Device profiling quota。
- Robotics Hub 或开发者博客联合样例 review。

验证指标：

- `3x1080p30` 连续 30 分钟采集的 FPS、drop frame、P95 timestamp skew、storage throughput 和 thermal behavior。
- `4x1080p30` 或 `1x4K30 + auxiliary cameras` 的编码码率、CPU、功耗和 latency。
- edge QC/privacy 模型的 QNN latency、FPS/power overhead、upload reduction 和 false reject rate。

## 10 · Demo & Ask

### 3-Minute Demo

1. **0:00-0:25**：展示“录视频不是数据资产”的问题，打开一个 bad episode。
2. **0:25-0:55**：操作员遥控桌面机械臂完成样品转移，UI 同屏显示三路相机、state/action timeline、timestamp 和 robot profile。
3. **0:55-1:25**：故意遮挡或丢帧，QC gate 拒绝 episode，并说明拒绝原因。
4. **1:25-1:55**：制造一次接管，标注 `pre_intervention / intervention / recovery`，把失败变成高价值 HIL 样本。
5. **1:55-2:25**：导出 LeRobotDataset v3、dataset card、qa report、manifest 和 TrainRouter job contract。
6. **2:25-2:50**：TrainRouter 选择 China / Overseas lane 和 Qualcomm target profile。
7. **2:50-3:00**：收束：TeleopStudio 不是机械臂表演，而是 Qualcomm edge robot skill release 的数据入口。

### Competition Ask

主办方和 Qualcomm 给我们开发板、AI Hub/QNN 路线 review、多相机采集建议和生态引荐；我们交付一个可复用样例：从真实遥操作 episode 到 LeRobot 数据集、云训练、Qualcomm edge profile 和比赛展示网站。

## Claim Boundaries

可以声称：

- Qualcomm-first edge recorder concept。
- LeRobot-compatible dataset export。
- 支持具名硬件和输入方式的 episode capture workflow。
- 质量门禁、数据 lineage 和 TrainRouter handoff。

不能声称：

- 第一个或唯一遥操作平台。
- 已获得 Qualcomm 官方认证或合作。
- 任意机器人硬件都已支持。
- MP4/Parquet 自动等于高质量训练数据。
- HIL 消除了人类操作需求。
- 数据采集自动满足所有合规要求。
- 性能一定优于 NVIDIA / x86 / Jetson。

所有性能指标必须标注：`simulated`、`replay-eval` 或 `measured-on-device`，并附日期、板卡、SDK/runtime、相机、功耗/散热假设和 run count。

## Sources

- LeRobot GitHub：https://github.com/huggingface/lerobot
- LeRobot real-world robot workflow：https://huggingface.co/docs/lerobot/main/en/getting_started_real_world_robot
- LeRobot LeLab：https://huggingface.co/docs/lerobot/en/lelab
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot dataset v3 blog：https://huggingface.co/blog/lerobot-datasets-v3
- LeRobot HIL data collection：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobot action representations：https://huggingface.co/docs/lerobot/en/action_representations
- ALOHA / ACT：https://tonyzhaozh.github.io/aloha/
- Mobile ALOHA：https://arxiv.org/abs/2401.02117
- DROID：https://droid-dataset.github.io/
- Open X-Embodiment：https://robotics-transformer-x.github.io/
- GELLO：https://wuphilipp.github.io/gello_site/
- UMI：https://umi-gripper.github.io/
- Open-TeleVision：https://robot-tv.github.io/
- DexCap：https://dex-cap.github.io/
- MCAP specification：https://mcap.dev/spec
- Foxglove local data / MCAP guide：https://docs.foxglove.dev/docs/visualization/connecting/local-data
- RLDS format：https://github.com/google-research/rlds
- Datasheets for Datasets：https://arxiv.org/abs/1803.09010
- Hugging Face Dataset Cards：https://huggingface.co/docs/hub/datasets-cards
- Scale Physical AI Data Engine：https://scale.com/blog/physical-ai
- Labelbox Terra：https://labelbox.com/products/terra/
- Viam platform：https://www.viam.com/platform/overview
- Viam pricing：https://www.viam.com/pricing
- Formant teleoperation：https://docs.formant.io/docs/getting-started-teleoperation
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm RB3 Gen 2 Vision Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
