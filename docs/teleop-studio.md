# TeleopStudio Pitch

更新时间：2026-07-05。

## Core Thesis

机器人学习平台的第一道商业瓶颈不是 GPU，而是高质量真实示教数据。没有稳定的遥操作工位、同步相机、episode 记录、数据质检和回放机制，CloudTwin、SkillDock 和 SkillCertKit 都没有足够可靠的输入。

> TeleopStudio = operator controls + synchronized cameras + edge recorder + LeRobot dataset adapter + quality gates + cloud handoff。

它把“采几条示教轨迹”产品化为一个客户、学校、系统集成商和比赛团队都能购买和复现的数据采集工作站。

## Why This Matters

LeRobot 生态已经把机器人数据、模型训练和真实机器人工作流变得更容易进入；LeRobotDataset v3 进一步强调了可记录、可上传、可训练和可流式读取的数据结构。ACT / ALOHA 和 Mobile ALOHA 这类工作也说明，示教数据质量直接决定策略学习效果。

商业化平台要解决的问题不是“能不能录一次 demo”，而是：

- 同一个任务能不能让不同操作员稳定录出可训练 episode？
- 相机、状态、动作和结果是否同步？
- 失败、接管、重置和异常是否被保留下来？
- 数据能不能直接进入中国版或海外版 CloudTwin？
- 客户是否能把采集过程作为试点交付物验收？

## Product Package

### 1. Operator Station

支持手柄、leader arm、键鼠、手机或 3D mouse 等输入。比赛阶段优先使用最可靠的本地工位，后续再扩展云端多人遥操作。

### 2. Capture Cell

桌面机械臂、样品托盘、固定光照、相机支架、标定板和 reset tray，保证每个 episode 的起点、目标和环境尽量可复现。

### 3. Edge Recorder

RobotMac Core / Qualcomm edge box 负责相机采集、动作时间戳、低延迟预览、本地缓存和断网保护。

### 4. Quality Gates

采集时实时检查：

- 相机画面是否遮挡。
- action stream 是否丢帧。
- episode 是否完成目标。
- reset 是否合规。
- 操作员是否过度抖动或频繁接管。
- 数据是否满足训练最低样本量。

### 5. LeRobot Adapter

把 episode 转换成 LeRobot-compatible dataset，带上任务说明、相机配置、robot profile、成功/失败标签和版本信息。

### 6. Cloud Handoff

数据通过中国云或海外云 adapter 进入 CloudTwin 训练队列，训练后的策略再进入 EdgeRuntimeBench 和 SkillCertKit。

## Competition Use

TeleopStudio 能强化初赛和复赛两条线：

- 初赛：展示数据采集工作站、episode 结构、质检规则和 CloudTwin job contract。
- 复赛：真实录制 LabForgePilot 样品转移 episode，训练 ACT 策略并回放失败样本。
- 视频：一屏展示操作员遥控、相机预览、episode 时间轴、数据质检和上传状态。
- 答辩：解释为什么平台能从单次 demo 扩展为客户可购买的数据生产线。

## Commercial Value

TeleopStudio 可以独立销售，也可以作为 RobotMac 套件的第一步：

- 高校：机器人学习实验台和课程套件。
- 企业试点：4-8 周内先购买数据采集与可行性验证。
- 系统集成商：标准化采集工位，复用到多个客户场景。
- 开发者：采集私有技能数据，进入 SkillDock 认证。
- Qualcomm：让真实数据采集、边缘预处理、低延迟预览和本地安全都发生在 Dragonwing edge target 上。

## Product Loop

```text
TeleopStudio
  -> LeRobot-compatible dataset
  -> CloudTwin training job
  -> EdgeRuntimeBench deployment evidence
  -> SkillCertKit certification
  -> SkillDock marketplace
  -> EdgeFleet runtime feedback
  -> new TeleopStudio failure episode
```

## Sources

- LeRobot documentation：https://huggingface.co/docs/lerobot/index
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- ACT / ALOHA paper：https://arxiv.org/abs/2304.13705
- Mobile ALOHA paper：https://arxiv.org/abs/2401.02117
- COBALT cloud teleoperation paper：https://arxiv.org/abs/2605.19138
- Qualcomm AI Hub：https://aihub.qualcomm.com/
