# TeleopStudio Pitch

更新时间：2026-07-06。本页按照 YC / Airbnb 风格重写：先讲数据问题和时机，再讲解决方案、市场、竞争、壁垒、Qualcomm 必要性、演示和证据边界。

## One-Line Pitch

TeleopStudio 是 LeRobot CloudTwin 的上游数据入口：一台产品化遥操作和示教数据采集站，把操作员、相机、状态、动作、失败接管和质检规则变成可训练 episode，再交给 TrainRouter 训练并回到 Qualcomm edge 部署。

## Problem

机器人团队不缺“能录一段视频”的 demo，缺的是可复现、可训练、可验收的示教数据生产线：

- 相机不同步。
- reset 不一致。
- 失败没标注。
- 动作流丢帧。
- 操作者差异太大。
- 视频、状态、动作和安全事件没有统一时间轴。
- 训练前没有数据质量验收，GPU 预算被坏数据浪费。

坏数据会污染后续全部链路：CloudTwin、TrainRouter、EdgeRuntimeBench、SkillCertKit 和 SkillDock 都依赖采集端。

## Why Now

时机来自四个变化：

1. LeRobot 已经把真实机器人 teleoperation、record、visualize、replay、train 和 evaluate 工作流推到开发者可用层。
2. LeRobotDataset v3 用视频、表格和 metadata 组织多模态时间序列 episode，给商业化数据合约提供统一出口。
3. ALOHA / ACT、Mobile ALOHA、DROID、Open X-Embodiment 等项目证明：机器人学习的竞争正在转向真实示教数据质量和规模。
4. Qualcomm Dragonwing / RB3 / AI Hub / QNN / QAIRT 让端侧采集、预处理、profile 和部署证据有了硬件目标。

## Insight

真正稀缺的不是 GPU，也不是又一个 foundation model，而是合格的人机交互 episode 供应。

如果采集端没有时间戳、相机同步、失败标签、质量门禁和 robot profile，后面的训练路由、评测和边缘部署都救不回来。

## Solution

TeleopStudio = `Operator Station + Capture Cell + Qualcomm Edge Recorder + Quality Gates + LeRobot Adapter + Cloud Handoff`。

先从桌面机械臂样品转移、扫码、pick-place 做窄场景，先手工把供给做标准。每条 episode 都绑定：

- `task_id`
- `operator_id`
- `robot_profile`
- `camera_profile`
- `calibration_hash`
- `reset_protocol`
- `variation_label`
- `state_action_schema`
- `success_failure_takeover`
- `timestamp_skew`
- `dropped_frames`
- `privacy_region`
- `dataset_hash`
- `trainability_score`

## Product Package

### 1. Operator Station

支持手柄、leader arm、键鼠、SpaceMouse、手机或 XR 输入。比赛阶段优先选择最可靠的本地工位，后续再扩展多人远程采集。

### 2. Capture Cell

桌面机械臂、样品托盘、固定光照、相机支架、标定板和 reset tray，保证每个 episode 的起点、目标和环境尽量可复现。

### 3. Qualcomm Edge Recorder

RobotMac Core / Qualcomm edge box 负责：

- 多相机采集。
- 低延迟预览。
- 时间戳和 dropped-frame 记录。
- 动作状态同步。
- 本地缓存和断网保护。
- 端侧 blur / occlusion / action jitter 检查。
- 原始数据本地保留和可选脱敏上传。

### 4. Quality Gates

采集时实时检查：

- 帧数是否足够。
- 相机是否遮挡。
- action stream 是否丢帧。
- metadata 是否完整。
- state/action shape 是否一致。
- episode 是否完成目标。
- reset 是否合规。
- 操作员是否过度抖动或频繁接管。
- 数据是否满足训练最低样本量。

### 5. LeRobot Adapter

把 episode 转换成 LeRobot-compatible dataset，带上任务说明、相机配置、robot profile、成功/失败标签、接管标记和版本信息。

### 6. Cloud Handoff

数据通过中国云或海外云 adapter 进入 CloudTwin / TrainRouter，训练后的策略再进入 EdgeRuntimeBench 和 SkillCertKit。

## Market

首批客户不是所有机器人公司，而是正在把 demo 变成交付的团队：

- Embodied-AI / robotics startups：需要内部数据飞轮和融资/客户 demo。
- University / corporate labs：需要可复现实验、课程和论文数据流程。
- Robot OEMs：希望自己的机械臂、夹爪或移动底盘更容易变成 AI-ready kit。
- System integrators：需要更快原型和更可复用的客户试点流程。
- Education / vocational：需要可教学、耐用、低 setup 的机器人学习工位。
- Warehouse / factory / lab users：需要为现场任务采集示教、远程协助和训练数据。

IFR 2025 报告显示 2024 年工业机器人安装量约 542,000 台，中国约 295,000 台，占全球 54%。专业服务机器人也在增长。市场不缺机器人，缺的是把机器人变成持续学习资产的工作流。

## Business Model

海外版建议：

- Developer / BYO robot：`$2k-$6k/year` 软件，teleop UI、recorder、dataset export、ROS 2/Python adapters。
- Education / starter station：`$6k-$12k`，低成本 arm、相机、边缘计算、课程和有限支持。
- Research single-arm station：`$10k-$18k`，leader/follower 或 handheld teleop、相机、标定、recorder。
- Bimanual pro workstation：`$24k-$45k`，双臂 setup、QA 工具、支持和训练联动。
- OEM / industrial package：`$50k-$150k+`，定制 robot adapter、安全 review、现场集成和 SLA。
- Managed data add-on：按项目或 episode 包收费，提供采集、清洗和质检。

中国版建议：

- Starter：`¥30k-¥80k`。
- Research / Pro：`¥100k-¥220k`。
- OEM / Industrial：`¥250k-¥800k`。
- 默认支持中文文档、微信/飞书支持、发票、本地保修、国内硬件选项和 China-local / offline 数据路径。

## Competition

TeleopStudio 不应该声称自己是第一个遥操作平台。更准确的竞争地图：

- LeRobot / phosphobot：开源机器人学习、teleop、record、dataset、training 工具。
- Trossen ALOHA / Interbotix：leader-follower 机器人硬件和基础脚本。
- GELLO / UMI / Open-TeleVision / DexCap：输入设备、便携式采集或沉浸式遥操作。
- Formant / Viam：更宽的 fleet ops、remote control、data capture 和 dashboard。
- Foxglove / Rerun / ReductStore：日志、可视化、数据平台。
- Intrinsic Flowstate：工业自动化 workcell 和 skill tooling。
- NVIDIA Isaac / GR00T / Cosmos：仿真、合成数据和 GPU-first physical AI stack。
- Scale / Encord / Labelbox Terra：企业级 physical AI 数据服务和标注。

TeleopStudio 的位置是：真实机器人 teleoperation sessions 到 auditable, model-ready datasets 的质量控制层，开放导出到 LeRobot、MCAP/Foxglove、ROS bag、HDF5/Isaac Lab 和后续 RLDS。

## Moat

短期壁垒：

- 任务模板。
- episode schema。
- QC gates。
- Qualcomm edge capture profile。
- 支持硬件 adapter。

中期壁垒：

- failure / takeover taxonomy。
- operator quality scoring。
- dataset lineage。
- valid episode yield benchmark。
- CloudTwin eval history。

长期壁垒：

- 跨行业 skill release graph。
- policy compatibility matrix。
- 哪些任务、相机、硬件、数据质量和策略组合能稳定部署到哪些 Qualcomm edge target。

## Demo Plan

3 分钟比赛演示：

1. 0:00：展示“录视频不是数据资产”的痛点。
2. 0:25：操作员遥控桌面机械臂完成样品转移。
3. 0:55：UI 同屏显示三路相机、action/state timeline、timestamp、reset 状态。
4. 1:25：故意失败一次，人工接管，生成 HIL recovery episode。
5. 1:50：QC gate 拒绝一条遮挡/丢帧 episode，接受合格集。
6. 2:15：一键导出 LeRobot-compatible dataset card。
7. 2:35：交给 TrainRouter，选择 China / Overseas lane 和 Qualcomm target profile。
8. 2:55：收束：这不是机械臂表演，是从真实示教到 Qualcomm edge skill release 的入口。

## Qualcomm Ask

请求 Qualcomm 支持一个 6-8 周 TeleopStudio Dragonwing validation sprint：

- RB3 Gen 2 Vision Kit 或等价 QCS6490 / Dragonwing 开发板。
- 多相机 ingest、timestamp、encoding、preview 和 storage 指导。
- Qualcomm Linux / IM SDK office hour。
- AI Hub / QNN / QAIRT / ONNX Runtime QNN 路径 review。
- Device Cloud / Profiler 额度。
- Robotics Hub 样例 review。
- 与 camera module、carrier board、robotics partner 的生态引荐。

## Evidence Artifacts

首版应输出：

- `episode_manifest.json`
- `robot_profile.yaml`
- `camera_profile.yaml`
- `calibration_hash.txt`
- `operator_session.json`
- `reset_protocol.md`
- `quality_gate_report.json`
- `timestamp_sync_report.json`
- `privacy_policy.yaml`
- `lerobot_dataset_card.md`
- `trainrouter_job_contract.yaml`
- `qualcomm_edge_capture_profile.yaml`
- `handoff_audit_log.jsonl`
- `claim_boundaries.md`

## Claim Boundaries

可以声称：

- LeRobot-compatible dataset export。
- Qualcomm-first edge recorder concept。
- 支持具名硬件/输入的 episode capture workflow。
- 质量门禁、数据 lineage 和 CloudTwin / TrainRouter handoff。

不能声称：

- 第一个或唯一遥操作平台。
- 唯一 LeRobot 数据采集工具。
- 已获得 Qualcomm 官方认证或合作。
- 任意硬件都支持。
- 数据采集自动满足所有合规要求。
- 功能安全认证完成。
- 性能一定优于 NVIDIA / x86 / Jetson。

指标必须标注来源：`simulated`、`replay-eval`、`measured-on-device`，并附日期、板卡、SDK/runtime、相机、功耗/散热假设和 run count。

## Sources

- LeRobot real robot workflow：https://huggingface.co/docs/lerobot/en/il_robots
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot dataset blog：https://huggingface.co/blog/lerobot-datasets-v3
- ALOHA / ACT：https://tonyzhaozh.github.io/aloha/
- Mobile ALOHA：https://arxiv.org/abs/2401.02117
- DROID：https://droid-dataset.github.io/
- Open X-Embodiment：https://robotics-transformer-x.github.io/
- IFR industrial robots 2025：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots 2025：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Trossen ALOHA Stationary：https://www.trossenrobotics.com/aloha-stationary
- GELLO：https://wuphilipp.github.io/gello_site/
- Formant teleoperation：https://docs.formant.io/docs/getting-started-teleoperation
- Viam teleop workspaces：https://docs.viam.com/monitor/teleop-workspaces/
- Foxglove Data Platform：https://docs.foxglove.dev/docs/data
- Rerun：https://rerun.io/docs
- NVIDIA Isaac Sim：https://developer.nvidia.com/isaac/sim
- NVIDIA GR00T：https://github.com/Nvidia/Isaac-GR00T
- Qualcomm AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
