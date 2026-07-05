# RobotCoreOS Pitch

更新时间：2026-07-05。底层 OS、BSP、驱动和 OTA 方案必须按最终开发板和供应商支持重新验证。

## Core Thesis

如果 RobotMac 要像电脑或手机一样被购买和使用，就不能让客户从裸开发板、驱动、ROS 2、相机、模型运行时、日志和更新系统开始拼装。

> RobotCoreOS = golden robot image + driver validation + ROS 2 bridge + LeRobot runtime hooks + AI model runner + SafetyOps service + OTA + A/B rollback + fleet identity。

它把 Qualcomm 开发板从“可开发硬件”变成“可批量交付的机器人运行底座”。

## Why This Matters

机器人商业化最容易被低估的部分是系统镜像：

- 开发板能跑起来，不代表客户现场能稳定运行。
- 模型能部署一次，不代表未来版本能安全升级。
- ROS 2 节点能通信，不代表上层应用开发者不需要懂底层 topic 和 launch。
- 单台 demo 能成功，不代表 20 台设备能被 provision、监控、更新和回滚。

RobotCoreOS 的价值是把这些底层问题做成默认产品能力。

## Research Synthesis

五条并行研究线给出同一个结论：机器人平台的关键不是再做一个云 dashboard，而是做一个能从第一次上电就稳定工作的本体运行底座。

### Platform Startup Signals

- Viam 验证了硬件抽象、远程调试、数据、ML、fleet management 和 OTA 是真实痛点，但它更像 cloud-connected robotics developer platform。RobotCoreOS 应该成为它下方的 Qualcomm-native bootable runtime。
- Intrinsic / Flowstate 验证了工业机器人需要技能、仿真、感知和 motion planning 的一体化开发环境，但其重心在工业自动化开发套件。RobotCoreOS 的切入点应是更开放、更快安装的智能边缘机器人系统镜像。
- Foxglove 验证了 time-synced multimodal data、ROS bag/MCAP、日志检索和共享可视化的重要性。RobotCoreOS 应该默认输出干净的 telemetry、camera、NPU perf 和 episode logs。
- Formant / InOrbit 验证了部署之后的真正痛点是 uptime、teleop、incident、orchestration 和 RobOps。RobotCoreOS 应该是这些云运维层可以信任的本体 endpoint。
- NVIDIA Isaac 验证了 physical AI 需要硬件加速、ROS packages、sim/data/training/deployment tooling 的整合。RobotCoreOS 的差异化是 Qualcomm-native、功耗友好、camera-rich、connected edge。

### Embodied AI Market Signals

Figure、Physical Intelligence、Skild AI、Apptronik、Agility Robotics 等公司共同显示一个趋势：

> Winning architecture = cloud-trained, edge-executed, fleet-improved。

云端负责大模型训练、仿真、teleop coaching、数据整理和模型蒸馏；边缘端负责低延迟感知、安全、fallback autonomy、隐私数据处理、可靠运行和现场 uptime。

这正是 RobotCoreOS 的位置：它不是替代云训练，而是让云训练结果可以被安全、可审计、可回滚地运行在机器人本体上。

### OS / OTA Research Implications

- 比赛 demo 最快路径：Ubuntu 24.04 + ROS 2 Jazzy + Qualcomm board support。
- 生产路径：Ubuntu Core 或 Yocto + Mender / RAUC / SWUpdate / OSTree。
- 必须强调 signed OTA、device identity、A/B rollback、recovery mode、staged rollout、SBOM 和持久化 robot data 分区。
- 系统镜像、机器人应用、技能包和客户数据必须分层，否则升级和回滚会变成现场风险。

### Qualcomm Research Implications

Qualcomm 的强项不是云端 GPU 训练，而是生产级边缘 AI：QCS6490 / RB3 Gen 2、QCS8550、Qualcomm Linux、AI Hub Workbench、QNN artifacts、profile/compile/validation 和 partner ecosystem。

RobotCoreOS 应该把 Qualcomm edge profile 写进 runtime manifest：SoC、OS image、QAIRT / QNN 版本、模型 artifact、accelerator placement、输入规格、latency / FPS / memory、sensor timing、thermal / power 和 rollback package。

## Runtime Stack

### 1. Board Support Layer

面向 QCS8550 / QCS6490 / IQ 系列 profile 固化启动、内核、驱动、相机、网络、IO 和加速器依赖。比赛阶段先用 Ubuntu 24.04 + ROS 2 Jazzy 定义 profile，复赛拿到板后实测补齐。

### 2. Robot Runtime Layer

封装 ROS 2 bridge、设备发现、时间同步、传感器采集、动作接口、状态机和本地日志。

### 3. AI Policy Runner

运行 CloudTwin / TrainRouter 导出的策略包，记录输入输出、延迟、资源占用和失败事件。

### 4. SafetyOps Service

急停、软边界、权限、发布门禁、审计日志和异常回滚作为系统服务运行，而不是散落在应用代码里。

### 5. LeRobot Hooks

数据采集、episode 回放、模型版本、dataset lineage 和失败片段回流都进入统一 runtime contract。

### 6. OTA And Rollback

支持 runtime image、技能包和配置包的更新。每次更新保留上一稳定版本，失败时进入 A/B rollback 或安全模式。

### 7. Runtime Manifest

每次部署输出一份 Qualcomm runtime manifest：SoC、OS image、QNN / QAIRT 版本、模型 artifact、传感器配置、输入输出规格、latency、功耗、温度和 rollback package。

### 8. Fleet Identity

每台机器人有设备身份、硬件 profile、证书、客户归属、安装技能、运行版本和运维状态。

## Product Deliverables

### Competition Stage

- RobotCoreOS manifest。
- BoardBringupKit validation checklist。
- QCS8550 target profile。
- Ubuntu 24.04 + ROS 2 Jazzy demo lane。
- Simulated OTA / rollback dashboard。
- LabForgePilot runtime service diagram。
- EdgeRuntimeBench integration plan。

### Final Product Stage

- 可烧录 golden image。
- 首次开机 provisioning flow。
- 本地控制台和远程 Fleet enrollment。
- ROS 2 / LeRobot / SkillDock runtime services。
- OTA update channel。
- A/B rollback policy。
- SBOM、artifact signing 和 runtime manifest。
- 现场恢复镜像和日志导出工具。

## Why Qualcomm Should Care

Qualcomm 的商业机会不只是卖开发板或芯片，而是成为机器人运行底座的默认硬件 target。

RobotCoreOS 让每台机器人都把 Qualcomm edge profile 写进：

- 系统镜像。
- 驱动和相机验证。
- AI policy runner。
- EdgeRuntimeBench。
- SkillCertKit。
- Fleet identity。

这比“项目使用 Qualcomm 板卡”更强：它让整个产品机制围绕 Qualcomm edge target 组织起来。

## Business Packaging

RobotCoreOS 可以成为三个收入层：

- CoreOS License：随 RobotMac Core 出厂，按设备授权。
- Fleet-safe Updates：企业订阅，包含 signed OTA、staged rollout、rollback、diagnostics 和 security updates。
- Integration Runtime：面向系统集成商，提供 Foxglove / Formant / InOrbit / Viam / MoveIt 等工具的标准 telemetry、logs、health API 和 runtime hooks。

客户购买的不是“系统镜像文件”，而是避免现场崩溃、降低集成成本、缩短上线时间和持续维护机器人的能力。

## Competition Story

RobotCoreOS 可以回答评委的一个关键疑问：

> 你们如何从一次 demo 走向可商业化、可维护、可升级的产品？

回答是：硬件产品线有 RobotMac Core，数据采集有 TeleopStudio，训练有 TrainRouter，部署证据有 EdgeRuntimeBench，而 RobotCoreOS 把这些能力装进一套可启动、可更新、可回滚的机器人系统镜像。

## Sources

- Viam platform：https://www.viam.com/platform/overview
- Intrinsic Flowstate：https://www.intrinsic.ai/flowstate
- Foxglove product：https://foxglove.dev/product
- Formant fleet management：https://docs.formant.io/docs/getting-started-fleet-management
- InOrbit orchestration：https://www.inorbit.ai/orchestration
- NVIDIA Isaac ROS：https://developer.nvidia.com/isaac/ros
- Figure production at BMW：https://www.figure.ai/news/production-at-bmw
- Physical Intelligence pi0.7：https://www.pi.website/blog/pi07
- Skild AI omni-bodied brain：https://www.skild.ai/blogs/omni-bodied
- Agility Robotics 100k totes：https://www.agilityrobotics.com/content/digit-moves-over-100k-totes
- ROS 2 documentation：https://docs.ros.org/en/jazzy/index.html
- Ubuntu Core documentation：https://ubuntu.com/core/docs
- Yocto Project documentation：https://docs.yoctoproject.org/
- Mender OTA documentation：https://docs.mender.io/
- Qualcomm Linux：https://www.qualcomm.com/developer/software/qualcomm-linux
- Qualcomm RB3 Gen 2 Development Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub：https://aihub.qualcomm.com/
