# 初赛项目书可粘贴版本

建议文件名：`RobotMac Core + LeRobot CloudTwin-[团队名]`

提交截止：`2026-07-20 11:59:59`

建议提交格式：`.docx` 或 `.pdf`

## 1. 项目名称

RobotMac Core + LeRobot CloudTwin：面向商业化机器人的一体化边缘计算与云训练平台

## 2. 项目简介

本项目面向 2026 高通具身智能与机器人大赛，提出一个可商业化的一体化机器人产品平台：用户不再从开发板、电源、驱动、训练环境、模型部署和运维系统开始造机器人，而是使用一个像电脑/手机一样可购买、可训练、可升级的机器人底座。

平台由 Qualcomm Dragonwing 边缘 AI 硬件、LeRobot 真实机器人学习工作流、中国/海外双云 GPU 训练路径、技能包机制和行业交付套件组成。云端负责数据管理、GPU 训练和评估；机器人本体负责低延迟感知、策略推理、安全边界和控制执行。最终形成“真实数据采集 -> 云端训练 -> 边缘部署 -> 本地执行 -> 失败片段回流”的持续学习闭环。

## 3. 参赛赛道与硬件选择

建议主赛道：标准赛道。

首选硬件：APLUX Rhino X1 / Qualcomm Dragonwing QCS8550。

原因：

- 标准赛道明确支持 QCS8550 / QCS6490。
- Rhino X1 官方展示 48 TOPS INT8 AI 算力，适合展示边缘 AI、视觉、多媒体和机器人实时闭环。
- QCS8550 适合作为 RobotMac Core Pro 的比赛主线，后续可向 QCS6490 Lite、IQ-8275 Industrial 和 IQ10 future SKU 迁移。

备选硬件：

- Radxa Dragon Q6A / QCS6490：适合 Core Lite、教育和紧凑机器人套件。
- Arduino VENTUNO Q / IQ-8275：适合 Pioneer Track、工业控制和双脑架构叙事。

## 4. 背景与痛点

机器人行业仍处于高度碎片化阶段。一个团队要做出可部署、可迭代的机器人，通常要同时处理：

- 开发板选型和边缘算力部署。
- 电源、散热、线束、IO、安全急停。
- 摄像头、传感器、执行器和机器人控制。
- 真实机器人数据采集和 episode 管理。
- 云 GPU 训练、环境复现和模型评估。
- 模型转换、边缘部署、版本回滚和运维。

这让很多开发者和企业的精力消耗在底层工程，而不是机器人应用和商业场景本身。个人电脑和智能手机的普及说明，只有当硬件、运行时、开发工具、应用/技能生态和服务体系被产品化之后，大规模商业化才会发生。

本项目的核心判断是：机器人也需要自己的 Mac / Windows / phone-like platform。

## 5. 解决方案

项目包括四个核心产品层：

### 5.1 RobotMac Core

一体化机器人计算、电源、IO、安全和运行时核心。它不是“开发板外壳”，而是把以下模块产品化：

- Qualcomm Dragonwing edge AI compute。
- 电池/外部供电、稳压、电源隔离、状态灯。
- 摄像头、CAN-FD、UART、PWM、GPIO、IMU、雷达/深度相机扩展。
- 急停、watchdog、本地安全状态机、断云可运行。
- 设备身份、skill compatibility manifest、deployment package registry。

### 5.2 LeRobot CloudTwin

真实机器人训练闭环：

1. 机器人采集示教 episode。
2. 数据转为 LeRobot-compatible dataset。
3. 中国云或海外云启动 GPU 训练任务。
4. 生成评估报告和模型 artifact。
5. 导出 Qualcomm edge deployment package。
6. 部署回本体，本地执行并记录失败片段。

### 5.3 SkillDock

机器人技能包与未来技能市场。技能包包含：

- 模型权重和推理配置。
- 输入/输出契约。
- 目标硬件兼容性。
- 安全边界、回滚版本和评估报告。
- 数据来源和版本信息。

### 5.4 Embodied Kit / DragonWorks / EdgeFleet / EduForge

面向不同商业场景的包装：

- `Embodied Kit`：企业、工厂、实验室可采购的行业套件。
- `DragonWorks`：Qualcomm-first 机器人开发者工作台。
- `EdgeFleet`：企业机器人队列运维平台。
- `EduForge`：高校和开发者教育套件。

### 5.5 LabForgePilot

比赛主 demo 采用桌面机械臂样品转移工作站：

1. 通过相机识别样品、托盘和目标位。
2. 通过遥操作采集 10-20 条示教轨迹。
3. 将数据保存为 LeRobot-compatible dataset。
4. 在中国版或海外版 CloudTwin 上训练 ACT 策略。
5. 导出 Qualcomm edge deployment package。
6. 在本体侧完成抓取、放置、扫码/状态记录。
7. 一次失败被人工接管，失败片段进入下一轮训练。

选择 LabForgePilot 的原因是场景可控、数据可复现、安全风险低、三分钟视频能讲完完整闭环，并且商业上可扩展到实验室自动化、教育训练、小工位自动化和系统集成商试点。

## 6. 技术架构

```text
机器人本体 / 仿真器
  -> 数据采集器
  -> LeRobot-compatible dataset adapter
  -> 中国 / 海外云 GPU training adapter
  -> model artifact registry
  -> Qualcomm edge deployment package
  -> edge runtime metrics
  -> Cloudflare pitch / demo dashboard
```

边缘端负责：

- 摄像头和传感器采集。
- 策略推理。
- 本地安全约束。
- 机器人控制输出。
- 日志和 episode metadata。
- 模型部署后的离线运行。

云端负责：

- 数据集存储。
- GPU 训练。
- 评估和回放。
- 模型导出。
- 部署包 registry。
- 非安全关键的遥测和演示 dashboard。

安全边界：

- Cloudflare Pages 只用于公开项目展示和 dashboard。
- 云 GPU 只用于训练和评估。
- 机器人安全关键控制不得依赖公网或 Cloudflare tunnel。
- 急停、碰撞规避、安全回退和本地控制必须保留在机器人本体。

## 7. 云训练方案

项目采用“双路径、单接口”的云训练设计。

中国版候选：

- 阿里云 PAI：企业 AI 工作流、DSW/DLC/EAS。
- 腾讯云 GPU：弹性 GPU 云服务器和按需计费。
- 华为 ModelArts：政企和工业客户叙事。
- AutoDL：开发者和比赛快速实验。

海外版候选：

- Runpod：开发者低摩擦 GPU pod。
- Lambda：可信训练实例和集群。
- Modal：短时评估、数据转换、导出 job。
- Paperspace：notebook 体验补充。

统一训练任务规范示例：

```yaml
job_name: act-grasp-v3
robot_profile: qcs8550_tabletop_arm
dataset_uri: lerobot://robotmac/tabletop-pick-v1
policy: act
gpu_target:
  china: autodl_or_pai
  global: runpod_or_lambda
budget:
  max_gpu_hours: 8
  preferred_gpu: a100_80g
export:
  target: qualcomm_edge_package
metrics:
  - success_rate
  - latency_ms
  - action_smoothness
  - failure_recovery_count
```

## 8. 竞品与差异化

已有平台与生态：

- NVIDIA Jetson / Isaac ROS：强 GPU 机器人开发生态。
- ROS / ROS 2：事实上的开源机器人软件基础。
- Unitree / AgileX：具体机器人本体和研发套件。
- 云 GPU/MLOps 平台：训练算力和 AI 工作流。

本项目差异：

- 不替代 ROS / LeRobot / 云 GPU，而是把它们组织成商业化机器人产品旅程。
- 不只是单块开发板，而是计算、电源、IO、安全、训练、部署、技能和运维一体化。
- 以 Qualcomm Dragonwing 为边缘 AI target，强调低延迟、功耗、多媒体、连接、安全和迁移路线。
- 同时支持中国版和海外版云训练，适配不同市场。

## 9. 创新点

1. 把 LeRobot 的开放机器人学习工作流产品化为训练闭环。
2. 把 Qualcomm Dragonwing 作为机器人技能部署与认证目标。
3. 把硬件、电源、IO、安全和运行时打包为可交付机器人核心。
4. 把机器人技能抽象成可安装、可评估、可升级、可售卖的 package。
5. 设计中国/海外双云训练路径，降低市场和供应商绑定风险。
6. 用教育套件、开发者工作台、企业运维和技能市场形成完整商业飞轮。

## 10. 商业价值

目标用户：

- 高校和开发者训练营。
- 机器人创业团队。
- 工厂/园区系统集成商。
- 企业创新部门。
- 服务机器人和移动机器人公司。

收入层：

- 硬件毛利：Core Lite / Pro / Industrial、传感器、电源、IO carrier。
- 云训练订阅：团队席位、GPU-hour 包、评估报告、部署包 registry。
- 技能市场：技能销售、开发者分成、认证费用、企业私有技能库。
- 队列运维：设备监控、日志、失败回放、版本控制、支持合同。
- 教育生态：课程授权、训练营、比赛模板、开发者认证。

## 11. Qualcomm 支持价值

本项目对 Qualcomm 的价值不是“用了某块板子”，而是把 Dragonwing 变成机器人商业化路径中的默认边缘 AI 底座。

Qualcomm 可获得：

- 从开发板到可采购机器人产品核心的样板。
- 从单次 demo 到可复用技能生态的路径。
- AI Hub / Dragonwing Robotics Hub / 比赛生态的端到端示范。
- 中国/海外双市场训练和部署故事。
- 教育、开发者、创业团队、企业试点共同导向 Dragonwing edge target 的商业路径。

## 12. 初赛可展示资产

- GitHub repo：https://github.com/asd125202/qc-robotics-2026
- Cloudflare Pages 中文路演网站：https://qc-robotics-2026.pages.dev/
- LabForgePilot 比赛主 demo 页：https://qc-robotics-2026.pages.dev/labforge-pilot/
- Prototype 可交互控制台：https://qc-robotics-2026.pages.dev/prototype/
- JudgeDeck 评分对齐页：https://qc-robotics-2026.pages.dev/judge-deck/
- BusinessCase 商业飞轮页：https://qc-robotics-2026.pages.dev/business-case/
- HardwareMap 硬件产品线页：https://qc-robotics-2026.pages.dev/hardware-map/

## 13. 实施计划

### 初赛前

- 完成项目书和报名。
- 发布中文路演网站。
- 完成 LabForgePilot 主 demo 方案、三分钟视频脚本、模拟 dashboard 和训练任务规范。
- 准备 fallback demo，不依赖真实开发板：遥操作回放、手写规则策略、模拟 dataset 和部署 manifest。

### 复赛入围后

- 拿到开发板后完成 board bring-up。
- 接入摄像头、桌面机械臂、样品托盘和机器人 IO。
- 录制 LabForgePilot 样品转移 episode 并转换为 LeRobot-compatible dataset。
- 运行一次中国或海外云端 ACT 训练，输出评估报告。
- 导出部署包并在 Qualcomm 设备上运行。

### 最终提交前

- 完成 3 分钟真实运行视频。
- 准备 PPT、代码包、部署说明和性能指标。
- 展示遥操作采集、云训练、Qualcomm 本体部署、失败回流、延迟、成功率、资源占用和商业模式。

## 14. 风险与备用方案

| 风险 | 应对 |
| --- | --- |
| 开发板到货晚 | 用 Prototype dashboard 和模拟 LeRobot dataset 展示闭环。 |
| 机器人硬件不稳定 | 主 demo 采用桌面机械臂样品转移，固定托盘、低速动作、简化抓取空间。 |
| 云 GPU 账号受限 | 先用 mock adapter，后接 Runpod/Lambda/AutoDL/PAI 中任一路径。 |
| 模型训练效果不足 | ACT 作为保底策略，任务选择简单、可量化、可重复。 |
| 边缘部署耗时 | 先展示 deployment manifest、离线回放和本体侧推理占位，再逐步接入真实推理。 |

## 15. 参考资料

- 2026 高通具身智能与机器人大赛：https://qc-robotics-dev.aidlux.com/2026/
- LeRobot：https://huggingface.co/docs/lerobot/index
- Qualcomm QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Qualcomm RB3 Gen 2 / QCS6490：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm IQ-8275：https://www.qualcomm.com/internet-of-things/products/iq8-series/iq-8275
- Qualcomm Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
