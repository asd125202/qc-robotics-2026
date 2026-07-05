# LabForgePilot Pitch

更新时间：2026-07-05。

## Core Thesis

前面的页面解释了平台愿景。LabForgePilot 是比赛中最稳妥的第一落地 demo：

> 用桌面机械臂完成“样品转移 + 扫码记录 + 失败接管 + 重新训练 + Qualcomm 本体部署”的完整闭环。

它不是最炫的机器人形态，但最适合比赛：

- 场景可控。
- 数据采集可复现。
- LeRobot / ACT 工作流容易解释。
- 安全风险低。
- 三分钟视频能讲完完整闭环。
- 商业上能扩展到实验室自动化、教育训练、工厂小工位和系统集成商试点。

## Demo Task

任务名称：桌面样品转移工作站。

基础流程：

1. 机械臂识别工作台上的样品、托盘和目标位。
2. 通过遥操作采集 10-20 条示教轨迹。
3. 数据以 LeRobot 兼容格式保存。
4. CloudTwin 在中国版或海外版 GPU 云训练 ACT 策略。
5. 策略部署到 Qualcomm edge target。
6. 机械臂自动完成抓取、移动、放置和状态记录。
7. 一次失败被人工接管，失败片段进入下一轮训练队列。

可选扩展：

- 扫码或视觉识别记录样品编号。
- 失败后 SafetyOps 触发回滚。
- EdgeFleet 记录设备和模型版本。
- SkillDock 把任务打包成 LabForge skill。

## Why Desktop Lab First

移动机器人、户外导航和复杂服务场景更容易出视觉、定位、路径规划、安全和场地问题。

桌面 LabForge 的优势：

- 任务空间小。
- 光照和背景可控。
- 机械臂动作可重复。
- 视频拍摄稳定。
- 数据量要求更低。
- 评委能一眼理解“真实任务闭环”。

这符合初赛和复赛的真实目标：先证明平台闭环，再证明可扩展商业场景。

## Three-Minute Video Storyboard

### 0:00-0:20 问题

实验室和小工位自动化难在每次都要重新集成硬件、驱动、训练和部署。

### 0:20-0:45 产品

RobotMac Core + LabForge 工作站 + LeRobot CloudTwin + Qualcomm edge deployment。

### 0:45-1:20 数据采集

遥操作采集样品转移轨迹，数据进入 DataFlywheel。

### 1:20-1:50 云训练

CloudTwin 启动训练任务，输出评估结果和 edge policy package。

### 1:50-2:25 本体部署

策略在 Qualcomm 本体运行，机械臂完成样品转移和扫码记录。

### 2:25-2:45 失败回流

一次失败被接管，片段进入下一轮训练队列，SafetyOps 记录版本和回滚。

### 2:45-3:00 商业扩展

同一底座可扩展到 FactoryPilot、EduForge 和 Industry Pack。

## Build Plan

### Before 2026-07-20

- 完成项目书。
- 完成中文路演网站组合。
- 完成 LabForgePilot 方案页、视频脚本和系统架构图。
- 明确首选开发板、机器人形态和风险控制。

### 2026-07-20 to 2026-07-31

- 等待入围和开发板邮寄。
- 准备机械臂、相机、样品托盘、桌面工位和采集脚本。
- 准备云训练 adapter 的最小可运行版本。

### 2026-08

- 接入开发板。
- 跑通相机输入、机械臂控制、数据采集和本地可视化。
- 完成手写保底策略和遥操作采集。

### 2026-09

- 跑通 LeRobot / ACT 训练。
- 完成 China Lane 和 Overseas Lane 的至少一个可运行训练路径。
- 完成 edge policy package 的导出和部署。

### 2026-10

- 提升稳定性。
- 录制多轮成功/失败/接管素材。
- 完成 SafetyOps、DataFlywheel、EdgeFleet 的演示视图。

### Before 2026-11-01

- 提交三分钟视频。
- 提交 PPT。
- 提交代码资源包和说明文档。

## Scoring Alignment

### Technical Completeness

感知、策略、执行、记录、部署和回滚形成完整闭环。

### Technical Innovation

不是单独训练模型，而是把数据飞轮、双云训练和边缘部署做成产品化 workflow。

### Qualcomm Processor Application

实时感知、策略推理、安全边界和本体运行都围绕 Qualcomm edge target。

### Product Definition

LabForgePilot 是明确客户场景：实验室、小工位、教育和系统集成商。

### Commercial Potential

先卖 Pilot Kit，再升级 Fleet Kit 和 Industry Pack。

## Risk Controls

- 如果真实训练不稳定，保留遥操作回放和手写规则策略作为视频保底。
- 如果机械臂控制延迟高，缩小动作空间和速度。
- 如果视觉识别不稳，先使用固定托盘和颜色/形状标记。
- 如果云训练耗时过长，预训练小模型并在视频中展示复现实验。
- 如果开发板到货晚，先在普通 Linux 设备上完成数据和控制台，再迁移 edge target。

## Sources

- Competition information：`docs/competition-info.md`
- LeRobot documentation：https://huggingface.co/docs/lerobot/index
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm RB3 Gen 2 Development Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- ROS 2 documentation：https://docs.ros.org/
