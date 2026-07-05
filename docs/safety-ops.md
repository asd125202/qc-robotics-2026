# SafetyOps Pitch

更新时间：2026-07-05。

## Core Thesis

如果 RobotMac 要成为“机器人世界的 Mac/Windows”，它不能只提供开发体验，还必须提供商业部署所需的安全、治理和证据链。

SafetyOps 是面向企业客户和评委的产品层：

- 本体安全运行时。
- 技能权限和模型发布门禁。
- 训练数据、模型、部署包和现场日志的审计链。
- 回滚、停用和失败复盘。
- 面向 ISO / NIST / AI 治理要求的证据包。

目标不是承诺自动通过任何认证，而是让每一次机器人策略上线都有可解释、可审计、可回滚的流程。

## Why This Is Commercial

企业购买机器人时，阻力通常不是“demo 不够酷”，而是：

- 谁批准这个模型上线？
- 它可以控制哪些电机、夹爪、相机和任务？
- 出现异常后谁能停用？
- 现场日志在哪里？
- 失败样本如何回到训练流程？
- 如果换一个版本，能不能回滚？

SafetyOps 把这些问题变成可销售能力：

- 安全部署包。
- 企业审计日志。
- 技能权限管理。
- 模型发布审批。
- 运维合规模板。
- 行业交付证据包。

## Product Modules

### 1. Edge Safety Runtime

能力：

- 安全关键动作在机器人本体执行。
- 速度、力矩、区域、任务边界和急停状态本地检查。
- 云端训练和资产管理不直接控制实时动作。
- 离线状态下也能执行保守策略。

Qualcomm 价值：

- 本地低延迟。
- 多传感器融合。
- 稳定运行和低功耗。
- 适合把 edge AI target 变成产品默认目标。

### 2. Skill Permission System

能力：

- 每个技能包声明可用传感器、可控执行器、任务范围和风险等级。
- 企业管理员批准后才能部署到设备。
- 教育版、实验室版、工厂版使用不同权限模板。
- 高风险技能必须经过评估门禁。

商业价值：

- SkillDock 不再只是应用商店，而是有权限、有评级、有责任边界的机器人软件分发系统。

### 3. Model Release Gates

能力：

- 数据集版本、训练配置、评估分数、边缘设备兼容性绑定。
- 未通过最低评估阈值不能进入生产部署。
- 灰度发布、回滚包和停用按钮。
- 现场失败自动生成下一轮训练任务。

商业价值：

- 企业愿意为“可控上线流程”付费。
- 系统集成商可以把门禁报告放进交付文档。

### 4. Audit Ledger

能力：

- 记录谁采集数据、谁训练模型、谁批准上线、部署到哪台机器人、何时回滚。
- 记录异常停止、人工接管、版本变化和安全边界触发。
- 支持导出评委版证据包和企业验收包。

商业价值：

- 将机器人部署从口头保证变成可检查证据。

### 5. Compliance Pack

能力：

- 对齐 ISO 机器人安全标准、NIST AI 风险管理框架和 AI 治理要求的内部检查表。
- 输出面向客户的安全说明、部署边界、模型版本和日志摘要。
- 明确区分“辅助准备认证材料”和“已经获得认证”。

商业价值：

- 这是工业客户愿意为平台化工具付费的重要原因。

## Competition Story

SafetyOps 可以成为评委答辩中的关键补强：

1. 先展示 DataFlywheel：采集、训练、部署、失败回流。
2. 再展示 SafetyOps：策略不是直接上线，而是经过权限、评估、发布和回滚门禁。
3. 最后展示 Qualcomm 价值：本体侧安全 runtime 与边缘推理是整个系统可信部署的基础。

一句话：

> 这个项目不是把大模型接到机器人上，而是把机器人策略变成可以被企业批准、部署、追踪和改进的产品资产。

## Demo Ideas

初赛可以做静态可视化和交互原型：

- 一个技能包卡片显示传感器权限、执行器权限、风险等级和评估分数。
- 一个发布门禁从“训练完成”到“评估通过”再到“部署到设备”。
- 一个异常事件进入日志并触发回滚。
- 一个失败片段进入 DataFlywheel 训练队列。

复赛可以接真实设备：

- 桌面机械臂执行任务时触发软边界。
- 管理员在控制台停用某个策略版本。
- 设备离线时仍按本地安全策略运行。

## Research Anchors

- ISO 机器人安全标准是工业机器人商业部署必须尊重的基础语境。
- NIST AI Risk Management Framework 强调对 AI 风险进行治理、映射、测量和管理。
- 欧盟 AI Act 的高风险分类与治理讨论说明，AI 系统进入实体世界时，风险分级和责任边界会越来越重要。
- Qualcomm RB3 Gen 2 等开发硬件强调 edge AI、摄像头、多媒体和开发者工作流，适合作为本体侧安全运行与策略部署目标。

## Sources

- ISO robotics standards：https://www.iso.org/sectors/engineering/robotics
- NIST AI Risk Management Framework：https://www.nist.gov/itl/ai-risk-management-framework
- EU AI regulatory framework：https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- Qualcomm RB3 Gen 2 Development Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
