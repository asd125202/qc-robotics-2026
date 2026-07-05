# DataFlywheel Pitch

更新时间：2026-07-05。

## Core Thesis

RobotMac 不能只卖硬件，也不能只卖云训练额度。真正有商业壁垒的是一条可重复的数据生产线：

1. 用户用遥操作或示教采集真实任务。
2. 数据进入 LeRobot 兼容格式，自动带上设备、相机、动作、失败片段和环境标签。
3. 中国版和海外版云 GPU 管线分别训练和评估策略。
4. 合格策略被打包成 Qualcomm edge target，在机器人本体低延迟运行。
5. 现场失败片段回流，形成下一轮训练样本。

这就是 DataFlywheel：把机器人从一次性项目交付，变成持续积累数据资产、模型资产和行业技能资产的产品。

## Why It Is Commercial

企业客户不会因为“模型很先进”而采购机器人。企业会采购一个能持续降低试错成本的系统：

- 数据采集有标准。
- 训练过程可复现。
- 评估结果能被采购经理和安全负责人看懂。
- 部署包能稳定跑在本体边缘计算上。
- 每次失败都能转化为下一轮改进。

这使收入结构从一次性硬件变成组合收入：

- RobotMac Core 硬件。
- CloudTwin 训练订阅。
- DataFlywheel 数据治理包。
- SkillDock 行业技能包。
- EdgeFleet 运维与模型更新。

## Product Modules

### 1. Teleop Studio

用途：降低真实任务数据采集门槛。

能力：

- 遥操作、键鼠/手柄/示教器接入。
- 多相机同步采集。
- 失败接管和片段标记。
- 任务模板：抓取、放置、扫码、巡检、跟随。

销售对象：

- 实验室自动化团队。
- 高校机器人课程。
- 工厂质检试点。
- 系统集成商。

### 2. Dataset Ledger

用途：把机器人数据变成可审计资产。

能力：

- LeRobot 数据集格式。
- 设备、传感器、任务、场景和操作者版本记录。
- 隐私等级和出境策略。
- 失败片段优先队列。

销售对象：

- 企业 AI / 自动化团队。
- 需要私有部署或合规审计的客户。

### 3. CloudTwin Trainer

用途：让中国版和海外版训练路线都可落地。

能力：

- 国内云 GPU adapter。
- 海外云 GPU adapter。
- ACT / Diffusion Policy / VLA 后续扩展。
- 训练成本、时长和评估结果记录。

销售对象：

- 比赛团队。
- 高校实验室。
- 企业 POC 团队。

### 4. Edge Policy Packager

用途：把云训练结果变成能上机的产品交付物。

能力：

- 策略版本、输入输出契约、依赖包和回滚包。
- Qualcomm edge runtime target。
- 本体低延迟执行。
- 云端只负责训练和资产管理，不控制安全关键实时动作。

销售对象：

- 希望量产的机器人公司。
- 使用 Qualcomm Dragonwing/RB3/RB5 系列硬件的开发者。

### 5. Failure Mining

用途：把现场失败变成训练飞轮。

能力：

- 低置信动作、人工接管、异常停止、任务超时自动入库。
- 按行业模板聚合失败模式。
- 下一轮训练任务自动生成。
- 评委 demo 可以直接展示“失败一次，数据回流，策略变好”。

销售对象：

- 对长期运维负责的企业客户。
- 需要持续优化的服务机器人场景。

## Competition Demo Plan

初赛/复赛主 demo 不需要铺开所有模块。建议只展示一个可控闭环：

1. 桌面机械臂执行样品转移或扫码任务。
2. 遥操作采集 10-20 条示教。
3. LeRobot 格式数据进入 CloudTwin。
4. 云端训练 ACT 策略。
5. 策略部署到 Qualcomm edge target。
6. 一次失败被人工接管并回流为新样本。

评委看到的是完整产品逻辑，不只是一个机械臂表演。

## Why Qualcomm Should Care

DataFlywheel 把 Qualcomm 的价值放在产品链路核心：

- 数据采集端需要多相机、连接、低功耗和本地缓存。
- 推理端需要本体低延迟和安全边界。
- 商业化端需要把开发者训练成果变成可部署的 edge policy。
- 生态端可以把 AI Hub、开发板、Dragonwing 机器人硬件和教育/开发者社区连起来。

如果 Qualcomm 支持这个产品方向，它支持的不只是某个参赛 demo，而是一个让更多机器人开发者选择 Qualcomm 作为默认边缘计算目标的工作流。

## Research Anchors

- LeRobot 官方文档把机器人学习工作流拆成数据、策略训练、评估和真实机器人使用。
- DROID 和 Open X-Embodiment 证明机器人数据规模与跨形态任务数据正在成为行业共识。
- NVIDIA Isaac GR00T 方向说明机器人基础模型、合成数据和仿真工作流会继续推高数据生产线的重要性。
- Qualcomm RB3 Gen 2 开发套件页面强调边缘 AI、摄像头、多媒体、连接和开发者工作流，这些正好落在 DataFlywheel 的本体侧。

## Sources

- LeRobot documentation：https://huggingface.co/docs/lerobot/index
- DROID dataset：https://droid-dataset.github.io/
- Open X-Embodiment：https://robotics-transformer-x.github.io/
- NVIDIA Isaac GR00T：https://developer.nvidia.com/isaac/gr00t
- Qualcomm RB3 Gen 2 Development Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
