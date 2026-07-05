# 项目书中文草稿

## 项目名称

RobotMac Core + LeRobot CloudTwin：面向商业化机器人的一体化边缘计算与云训练平台

## 一句话简介

本项目构建一个基于 Qualcomm Dragonwing 边缘 AI 硬件、LeRobot 真实机器人学习工作流和中国/海外双云 GPU 训练体系的一体化机器人产品平台，让开发者和企业不再从电源、开发板、驱动、训练环境和部署工具开始造机器人，而是像使用电脑或手机一样构建机器人应用。

## 背景与痛点

当前机器人开发仍然高度碎片化。一个团队要做出可演示、可部署、可迭代的机器人，通常需要同时解决硬件选型、电源设计、传感器同步、执行器控制、数据采集、GPU 训练、模型转换、边缘部署、远程展示和售后维护等问题。这使大量开发者和企业把时间消耗在底层工程，而不是机器人应用本身。

个人电脑和智能手机的普及说明，真正的大规模市场来自平台化：用户不需要从主板、电源、操作系统和驱动开始，开发者也不需要为每个设备重新构建基础设施。机器人行业同样需要一个商业化产品底座。

## 解决方案

项目分为四个核心层：

1. RobotMac Core：一体化机器人计算、电源、IO、安全和运行时核心。
2. LeRobot CloudTwin：真实机器人数据采集、云 GPU 训练、评估和模型部署闭环。
3. SkillDock：面向未来的机器人技能包与技能市场。
4. Embodied Kit / DragonWorks / EdgeFleet / EduForge：面向企业、开发者和教育市场的不同商业包装。

首个比赛 demo 建议采用 `LabForgePilot`：桌面机械臂样品转移工作站。它通过相机识别样品、托盘和目标位，遥操作采集 10-20 条示教轨迹，在 CloudTwin 上训练 ACT 策略，导出 Qualcomm edge deployment package，再由本体完成抓取、放置、扫码/状态记录，并把一次失败接管片段回流到下一轮训练。

## 技术路线

### 边缘端

- 目标硬件：优先 APLUX Rhino X1 / Qualcomm Dragonwing QCS8550。
- 可迁移硬件：Radxa Dragon Q6A / QCS6490，Arduino VENTUNO Q / IQ-8275。
- 本地能力：摄像头采集、策略推理、机器人控制、安全边界、日志记录、离线运行。

### 云端

- 中国版候选：阿里云 PAI、腾讯云 GPU、华为 ModelArts、AutoDL。
- 海外版候选：Runpod、Lambda、Modal、Paperspace。
- 云端能力：数据集版本、训练 job、评估报告、模型导出、部署包生成。

### 模型与数据

- 保底策略：ACT，适合比赛快速落地和精细操作。
- 前瞻策略：SmolVLA、X-VLA、HIL 数据回流。
- 数据格式：LeRobot-compatible dataset。
- 主 demo 数据：LabForgePilot 桌面样品转移 episode，优先保证小场景、低风险、可复现。

## 创新点

- 把 LeRobot 从研究/开源工具链产品化为机器人训练闭环。
- 用 Qualcomm Dragonwing 作为机器人技能的边缘部署与认证目标。
- 同时设计中国版和海外版云 GPU 训练路径。
- 把机器人能力抽象成可安装、可评估、可升级的技能包。
- 从硬件、云训练、技能市场、运维平台和教育套件形成完整商业模式。

## 商业价值

目标客户包括：

- 高校和开发者训练营。
- 机器人创业团队。
- 工厂/园区系统集成商。
- 需要快速试点的企业创新部门。
- 服务机器人和移动机器人公司。

收入来源包括：

- 一体化硬件核心和行业套件。
- 云训练订阅和 GPU 训练任务。
- 技能市场抽成。
- 企业私有化部署和运维服务。
- 教育课程与比赛套件。

## Qualcomm 支持价值

Qualcomm 可以通过该项目获得一个端到端机器人生态样板：

- 从开发板走向可采购机器人产品核心。
- 从单次 demo 走向可复用技能生态。
- 从硬件参数展示走向低延迟、低功耗、多媒体、连接、安全和长期供货的整体价值展示。
- 通过中国/海外双云训练路径拓展全球开发者和中国本地客户。

## 初赛可提交资产

- 中文项目书。
- GitHub repository。
- Cloudflare Pages 中文路演网站：https://qc-robotics-2026.pages.dev/
- RobotCoreOS 黄金系统镜像页：https://qc-robotics-2026.pages.dev/robot-core-os/
- LabForgePilot 比赛主 demo 页：https://qc-robotics-2026.pages.dev/labforge-pilot/
- TeleopStudio 示教数据采集工位页：https://qc-robotics-2026.pages.dev/teleop-studio/
- TrainRouter 双云 GPU 训练路由页：https://qc-robotics-2026.pages.dev/train-router/
- EdgeRuntimeBench Qualcomm 运行证据页：https://qc-robotics-2026.pages.dev/edge-runtime-bench/
- HomeCore 家用机器人技能内核页：https://qc-robotics-2026.pages.dev/home-core/
- WorldForge 仿真数据工厂页：https://qc-robotics-2026.pages.dev/worldforge/
- RoboTrust 具身数信云页：https://qc-robotics-2026.pages.dev/robotrust/
- RoboPort 机器人模组港页：https://qc-robotics-2026.pages.dev/roboport/
- IntegratorForge 集成交付生态页：https://qc-robotics-2026.pages.dev/integrator-forge/
- RobotLeaseOps RaaS 订阅控制面页：https://qc-robotics-2026.pages.dev/robot-lease-ops/
- RiskLedger 机器人风险账本页：https://qc-robotics-2026.pages.dev/risk-ledger/
- ScaleFoundry 硬件产品化工厂页：https://qc-robotics-2026.pages.dev/scale-foundry/
- FleetConductor 机器人塔台页：https://qc-robotics-2026.pages.dev/fleet-conductor/
- CareOps 院内智运平台页：https://qc-robotics-2026.pages.dev/care-ops/
- FieldOps 野巡户外机器人平台页：https://qc-robotics-2026.pages.dev/field-ops/
- PilotContractKit 商业试点合同页：https://qc-robotics-2026.pages.dev/pilot-contract-kit/
- SkillCertKit 技能认证体系页：https://qc-robotics-2026.pages.dev/skill-cert-kit/
- OpsConnector 企业集成桥页：https://qc-robotics-2026.pages.dev/ops-connector/
- 产品主张、竞品研究、云 GPU 研究、评分对齐表。
- 三分钟 demo storyboard、LabForgePilot 构建计划和 fallback dashboard 计划。
