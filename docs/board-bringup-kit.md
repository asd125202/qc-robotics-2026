# BoardBringupKit Pitch

更新时间：2026-07-05。

## Core Thesis

比赛项目不能只写“收到开发板后接机器人”。真正可执行的计划需要把 Qualcomm 开发板变成可复用的机器人核心：

> BoardBringupKit = competition board + power harness + camera rig + IO adapter + safety stop + runtime image + benchmark checklist + deployment manifest.

它把开发板从“裸板”变成 RobotMac Core 的第一版工程样机。

## Why This Matters

官方标准赛道重视系统级能力、完整闭环、稳定运行、可复现实现和真实环境部署。硬件 bring-up 是这些要求的前提：

- 没有稳定供电，就没有可靠视频和控制。
- 没有相机/IO 接口，就无法形成感知到执行闭环。
- 没有安全急停和 watchdog，就不能把机器人任务说成商业产品。
- 没有 runtime image 和部署 manifest，就不能复现。
- 没有 bring-up checklist，就无法在 8-10 月快速推进复赛。

## Target Boards

### Primary: APLUX Rhino X1 / QCS8550

用途：

- 标准赛道主目标。
- LabForgePilot 主 demo。
- EdgeRuntimeBench runtime profile。
- RobotMac Core Pro 原型。

关注点：

- 摄像头输入。
- 桌面机械臂控制。
- ACT policy 推理。
- 安全运行时。
- 48 TOPS INT8 作为初赛算力锚点。

### Fallback: Radxa Dragon Q6A / QCS6490

用途：

- Core Lite 和教育版。
- 简化感知与控制任务。
- 更紧凑的 RobotMac Core 形态。

### Pioneer Option: Arduino VENTUNO Q / IQ-8275

用途：

- Pioneer Track 前瞻叙事。
- 工业控制和异构计算探索。
- 未来 Industrial SKU。

## Bring-up Stack

### 1. Power Harness

- 桌面电源和电池输入边界。
- 稳压、保险、状态灯。
- 机械臂、相机和开发板分路供电。
- 故障断电和重启流程。

### 2. Camera Rig

- 单目/双目/深度相机安装位。
- 固定视角和标定流程。
- LabForgePilot 桌面任务视觉输入。
- 数据采集同步时间戳。

### 3. Robot IO Adapter

- 机械臂控制接口。
- 夹爪、急停、限位和状态读取。
- CAN/UART/PWM/GPIO 抽象。
- ROS 2 bridge 和 RobotAppLayer 能力映射。

### 4. Safety Harness

- 物理急停。
- 软件 watchdog。
- 软边界和低速模式。
- SafetyOps 发布门禁。
- 失败接管日志。

### 5. Runtime Image

- 系统镜像和依赖版本。
- 摄像头驱动、ROS 2 bridge、LeRobot adapter。
- CloudTwin agent。
- EdgeRuntimeBench profiler。
- Deployment manifest。

### 6. Validation Checklist

- 开机和网络。
- 摄像头采集。
- 机械臂单轴/多轴动作。
- 数据采集 episode。
- 策略部署和离线回放。
- Safety trigger 和 rollback。

## Competition Build Plan

### Before Board Arrival

- 完成 BoardBringupKit 文档和 wiring plan。
- 准备相机、桌面机械臂、样品托盘、急停、线束和电源。
- 在普通 Linux 设备上验证 LeRobot dataset 和控制台。

### Week 1 After Board Arrival

- 系统启动、网络、存储、摄像头。
- 跑通最小 runtime image。
- 记录硬件 profile 和问题清单。

### Week 2

- 接机械臂和安全急停。
- 完成遥操作采集和固定任务回放。
- 生成第一版 deployment manifest。

### Week 3-4

- 接 CloudTwin 训练输出。
- 跑 EdgeRuntimeBench profiler。
- 录制 LabForgePilot 初版素材。

## Product Value

BoardBringupKit 不是一次性比赛文档。它可以变成商业产品：

- 企业试点交付清单。
- 系统集成商快速 bring-up 包。
- RobotMac Core 硬件认证流程。
- 教育套件实验指导。
- SkillDock 技能兼容性测试前置条件。

## Why Qualcomm Should Care

开发者选择一个处理器，真正难的不是购买开发板，而是把它接进机器人完整系统。BoardBringupKit 把 Qualcomm board 的价值放进：

- 电源和 IO。
- 相机和多媒体。
- 机器人控制。
- AI policy runtime。
- 安全运行。
- 可复现部署。

这能把比赛支持从“提供板卡”升级为“帮助开发者把板卡变成机器人产品核心”。

## Sources

- Competition information：`docs/competition-info.md`
- APLUX Rhino X1 developer page：https://developer.aidlux.com/
- Rhino X1 docs：https://rhinopi.docs.aidlux.com/rhino-x1-aidlux/
- Radxa Dragon Q6A：https://radxa.com/products/dragon/q6a/
- Arduino VENTUNO Q：https://www.arduino.cc/product-ventuno-q
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm RB3 Gen 2 Development Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
