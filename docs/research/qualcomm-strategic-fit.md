# 研究笔记：为什么 Qualcomm 应该支持这个产品

更新时间：2026-07-05。

## 结论先行

这个项目对 Qualcomm 的价值，不是“参赛者用了某块板子”，而是把 Dragonwing 变成机器人商业化路径里的默认边缘 AI 底座。它把 Qualcomm 的硬件、AI Hub、Dragonwing Robotics Hub、开发板、边缘 AI 叙事和机器人比赛连接到一个可被开发者理解的产品故事。

## Qualcomm 官方战略已经指向这个方向

Qualcomm 2026 Dragonwing developer ecosystem 文章强调，AI 正在从集中式云环境移动到靠近数据和决策的位置，边缘 AI 带来实时响应、韧性和数据隐私。该文章的主题是把 edge AI 从 prototype 推向 deployment。

Qualcomm Dragonwing Robotics Hub 官方文章强调，Robotics Hub 是 Arduino Project Hub 上的协作开发者空间，提供样例机器人应用，并帮助开发者在 Dragonwing 平台上从 prototype 到 production。

这与本项目高度一致：

- RobotMac Core：把 Dragonwing 从开发板变成机器人产品核心。
- LeRobot CloudTwin：把训练和部署路径串起来。
- SkillDock：让样例应用升级为可认证、可分发的技能生态。
- Embodied Kit：让 prototype 到 production 之间有可采购套件。

## Qualcomm 的优势不只是 TOPS

机器人商业化需要：

- 本体低延迟：感知、策略和控制不能依赖公网。
- 隐私和韧性：工厂、家庭、学校和医疗场景的数据不能随意上云。
- 多媒体与连接：机器人天然依赖多摄像头、视频、音频、Wi-Fi、蓝牙、蜂窝等。
- 功耗和散热：移动机器人比桌面工作站更在乎能耗。
- 产品寿命：工业和企业客户需要长期供货和稳定软件栈。
- 生态迁移：从 QCS6490 到 QCS8550，再到 IQ-8275 / IQ10，需要可迁移软件层。

因此比赛方案不应只写“用了 Qualcomm 算力”，而要写“这个产品只有在 Qualcomm 异构边缘平台上才像商业产品”。

## 与 NVIDIA 竞争的正确方式

NVIDIA 已经拥有强大的 Jetson + Isaac ROS 心智。Qualcomm 不应只在峰值算力叙事中被比较，而应强调：

- 更完整的移动/连接/多媒体 DNA。
- 更适合功耗受限、摄像头丰富、需要长期部署的机器人。
- 通过 Arduino、Dragonwing Robotics Hub、AI Hub 和比赛生态触达开发者。
- 通过中国合作伙伴和本地云训练路径贴近中国机器人市场。

本项目可以作为一个“Qualcomm-first robotics platform”样板，而不是单点 demo。

## 可以向评委明确提出的合作价值

1. 让 Qualcomm 板卡从“开发者硬件”升级为“可交付机器人产品核心”。
2. 让 Dragonwing Robotics Hub 有更完整的端到端示范：硬件、数据、训练、部署、技能。
3. 让 AI Hub / Edge Impulse 等模型优化工具未来可以接入机器人技能发布流程。
4. 让比赛作品具备后续商业化路径：教育套件、企业套件、技能市场、云训练订阅。
5. 让中国市场和海外市场使用同一套 Qualcomm edge target，但云训练供应商按市场本地化。

## 比赛演示中的 Qualcomm 露出点

- 启动界面展示目标硬件：QCS8550 / QCS6490 / IQ-8275 路线。
- 指标展示边缘推理：延迟、帧率、CPU/GPU/NPU 占用、温度、功耗。
- 云训练展示分工：云端训练，边缘执行；公网不可用时机器人仍能运行已部署技能。
- 技能包展示兼容性：哪些技能通过 Qualcomm 目标硬件验证。
- 网站展示商业价值：如果 Qualcomm 支持这个平台，可以把更多开发者、教育团队和企业试点导向 Dragonwing。

## 信息来源

- Qualcomm Dragonwing developer ecosystem：https://www.qualcomm.com/developer/blog/2026/05/edge-ai-prototype-deployment-qualcomm-dragonwing-developer-ecosystem
- Qualcomm Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Qualcomm AI Hub：https://aihub.qualcomm.com/models
- Android on Dragonwing / IoT ISI：https://www.qualcomm.com/developer/software/android-on-dragonwing
- Qualcomm Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
