# 研究笔记：竞品与平台空位

更新时间：2026-07-05。

## 结论先行

机器人平台赛道不是空白。NVIDIA 已经用 Jetson + Isaac ROS 把“GPU 加速机器人开发”讲得非常清楚；ROS 是事实上的开源机器人软件基础；Unitree、AgileX 等公司正在把机器人本体和 SDK 打包给开发者；云 GPU 厂商正在解决训练算力。但这些能力仍然分散。

本项目的空位不是再做一个 ROS，也不是正面替代 Jetson，而是做一个“商业化机器人产品底座”：把 Qualcomm 边缘硬件、LeRobot 数据/训练、双云 GPU、技能包和行业套件放进同一条用户旅程。

## NVIDIA Jetson / Isaac ROS

NVIDIA 的强项：

- Jetson Thor 官方页面强调面向 physical robotics / agentic AI，最高 2070 FP4 TFLOPS、128GB memory、40-130W power。
- Isaac ROS 官方页面强调面向 ROS 的加速包，覆盖 navigation、perception，并可部署到 workstation 和 Jetson。
- Jetson AI Lab、CUDA、GPU 生态和开发者心智非常强。

对我们的启发：

- 竞品叙事不是“开发板”，而是“robot brain / physical AI platform”。
- Qualcomm 需要一个同样清晰的机器人产品化叙事：不是只说 TOPS，而是说如何从 prototype 到 production。

我们的差异：

- 更强调一体化产品：电源、IO、安全、线束、训练接口和交付套件。
- 更强调 LeRobot 与云训练闭环，而不是只强调本地 GPU 推理。
- 更强调中国/海外双市场，而不是单一全球云/生态路径。

## ROS / ROS 2

ROS 官方定义是用于构建机器人应用的软件库和工具集合。它的价值是庞大的软件生态、消息机制、驱动、导航、可视化和开发者社区。

对我们的启发：

- 不应该替代 ROS，而应该兼容 ROS。
- RobotMac Core 可以把 ROS 作为可选运行层；LeRobot Bridge 负责数据和策略训练；Qualcomm runtime 负责边缘部署优化。

我们的差异：

- ROS 解决“机器人软件开发”，但不解决商业产品的一体化硬件、电源、云训练、技能分发和采购包装。
- 本项目可以把 ROS 视为底层工具之一，而不是最终产品体验。

## Unitree / 机器人整机公司

Unitree 的强项：

- 已经有消费级和工业级腿式/人形机器人产品。
- 官方文档和 GitHub 生态为 H1/G1/Go2 等机器人提供 SDK。
- 它把高性能机器人本体带到开发者可购买范围。

我们的差异：

- Unitree 卖的是具体机器人形态；本项目卖的是跨形态的计算、训练和技能底座。
- 我们可以支持机械臂、小车、巡检车、教学平台和未来人形，而不押注单一机器人形态。

## AgileX / ROS-ready 套件

AgileX、RobotLAB 等渠道已经证明“预集成移动机器人研发套件”有市场。公开产品页中可以看到 ROS-ready、LiDAR、depth camera、IMU、NVIDIA Jetson 等组合，价格可到上万美元级别。

对我们的启发：

- 企业和高校愿意为“省去集成时间”付费。
- 套件化不是低端包装，而是降低试点风险的商业产品。

我们的差异：

- AgileX 更像移动底盘与 ROS 研发套件；本项目强调 Qualcomm 边缘 AI、LeRobot 云训练、技能包和中国/海外双云。

## 云 GPU / MLOps 平台

Runpod、Lambda、Modal、阿里云 PAI、腾讯云 GPU、华为 ModelArts、AutoDL 都能承担训练算力或 AI 工程平台角色。

我们的差异：

- 云厂商不拥有机器人本体闭环，也不天然理解动作空间、安全边界和硬件部署。
- 本项目把云 GPU 变成机器人技能训练工厂的一部分，而不是把 notebook 放到云上。

## 机会矩阵

| 方向 | 市场已有强者 | 本项目空位 |
| --- | --- | --- |
| 边缘机器人算力 | NVIDIA Jetson, Qualcomm Dragonwing | Qualcomm-first 产品化机器人核心 |
| 机器人软件框架 | ROS / ROS 2 | 面向商业用户的一体化 runtime + training bridge |
| 机器人学习 | LeRobot, imitation/VLA papers | LeRobot 工作流产品化和云端 job 化 |
| 云训练 | Runpod, Lambda, Modal, PAI, ModelArts | 面向机器人数据、动作和边缘部署的训练控制台 |
| 整机机器人 | Unitree, AgileX, 大量 AMR/机械臂厂商 | 跨形态的产品底座、技能包和行业套件 |
| 商业交付 | 系统集成商 | 可复制的套件、技能市场和认证生态 |

## 信息来源

- NVIDIA Jetson Thor：https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- NVIDIA Isaac ROS：https://developer.nvidia.com/isaac/ros
- Isaac ROS docs：https://nvidia-isaac-ros.github.io/getting_started/index.html
- ROS 官方：https://www.ros.org/
- ROS 2 GitHub：https://github.com/ros2
- Unitree GitHub：https://github.com/unitreerobotics
- Unitree G1 SDK docs：https://support.unitree.com/home/en/G1_developer
- AgileX Robotics：https://global.agilex.ai/
- AgileX ROS2 NAV Kit：https://global.agilex.ai/blogs/news/the-world-s-first-ros2-mobile-robot-navigation-open-source-education-kit-released
