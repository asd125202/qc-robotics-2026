# RobotAppLayer Pitch

更新时间：2026-07-05。

## Core Thesis

如果目标是“机器人世界的 Mac/Windows”，最终用户不应该每天处理开发板、电源、驱动、ROS topic、训练脚本和 GPU 云细节。

RobotAppLayer 是放在底座之上的应用层：

- 给应用开发者一个稳定 SDK。
- 把 ROS 2、LeRobot、SkillDock、EdgeFleet 和 Qualcomm edge deployment 封装在后面。
- 让上层开发者写“任务应用”，而不是从硬件接口开始集成。

一句话：

> 硬件底座解决机器人能不能跑，AppLayer 解决开发者能不能像写软件一样构建机器人应用。

## Why It Matters

机器人商业化很难扩张的一个原因是：每个项目都像系统集成。

开发者必须理解：

- 机器人型号。
- 相机和电机接口。
- ROS 2 通信。
- 数据采集格式。
- 模型训练和部署。
- 任务调度和日志。

如果这些都暴露给应用开发者，平台就很难像 Mac/Windows/手机那样形成生态。

RobotAppLayer 的目标是让开发者调用高层能力：

- observe：看见场景。
- move：移动或执行动作。
- grasp：抓取和放置。
- train：用现场数据训练技能。
- deploy：把技能部署到本体。
- monitor：观察任务结果和失败。

## Layer Model

### 1. Hardware Abstraction

把机械臂、移动底盘、相机、夹爪、电源和 IO 归一化成设备能力，而不是裸驱动。

### 2. ROS Bridge

保留 ROS 2 的生态价值，但不要求每个上层开发者直接处理 topic、service、action 和 launch 文件。

### 3. Skill Runtime

把训练出的策略和手写任务逻辑封装成技能包，统一安装、权限、版本和回滚。

### 4. Data API

现场数据、失败片段、任务结果和评估指标进入 DataFlywheel，而不是散落在项目文件夹里。

### 5. Fleet API

单机任务和多机运维都通过 EdgeFleet 管理设备状态、日志、更新和异常。

### 6. Edge Deployment

最终模型部署目标是 Qualcomm edge runtime。云端训练不改变本体侧执行 API。

## Developer Personas

### Robotics Builder

想要接底层能力，但不想重复搭建电源、相机、驱动和部署链路。

### AI Researcher

想要快速采集 LeRobot 数据、训练策略、部署到真实机器人验证。

### Enterprise Integrator

想要把机器人接入客户流程、权限、日志和验收文档。

### App Developer

想要写具体应用：巡检、配送、实验室流程、教学课程，而不是重写机器人底层。

## Product Surface

RobotAppLayer 可以呈现为：

- Web 控制台。
- Python SDK。
- ROS 2 bridge package。
- Skill manifest。
- Dataset schema。
- Edge deployment CLI。
- 企业权限和日志 API。

初赛不需要全部实现，但需要把接口边界画清楚。

## Competition Demo

建议 demo 做一个可解释的三层结构：

1. 上层应用：LabForge 样品转移 app。
2. 中间层：RobotAppLayer 调用 observe、grasp、train、deploy、monitor。
3. 底层：ROS 2 / LeRobot / Qualcomm edge runtime。

评委看到的是：

- 这不是一次性机械臂脚本。
- 这是一套能让其他应用复用的机器人软件平台。
- Qualcomm 支持这个平台，能获得更多默认部署目标。

## Why Qualcomm Should Care

开发者生态不是让大家买一次开发板，而是让应用开发者默认把 Qualcomm edge 当作机器人策略运行目标。

RobotAppLayer 能把 Qualcomm 放在三个入口：

- SDK 默认 target。
- Skill package 默认 edge runtime。
- 企业部署默认设备 profile。

这比单个 demo 更有生态价值。

## Sources

- ROS 2 documentation：https://docs.ros.org/
- OSRF multi-robot / Open-RMF book：https://osrf.github.io/ros2multirobotbook/
- LeRobot documentation：https://huggingface.co/docs/lerobot/index
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm RB3 Gen 2 Development Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
