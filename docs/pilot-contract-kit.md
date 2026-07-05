# PilotContractKit Pitch

更新时间：2026-07-05。

## Core Thesis

商业化机器人平台不能只靠“我们可以做 demo”。企业客户需要一个低风险采购入口：

> PilotContractKit = 4-8 周试点合同 + 明确任务范围 + KPI + 验收标准 + 数据权益 + 云训练额度 + 边缘运行证据 + 扩展到 Fleet Kit 的路径。

它把 RobotMac 从技术愿景变成客户能采购、法务能审查、采购经理能批准的试点产品。

## Why This Matters

企业机器人采购的难点通常不是客户完全不感兴趣，而是风险太不清楚：

- 试点到底做什么任务？
- 用什么硬件？
- 数据归谁？
- 成功标准是什么？
- 失败后怎么处理？
- 试点结束后继续买什么？
- 供应商是否承担维护和训练责任？

PilotContractKit 的作用是把这些问题写成产品包，而不是每个客户都重新谈一遍。

## Pilot Package

### 1. Scope

定义一个小而明确的任务：

- LabForge 样品转移。
- FactoryPilot 指针/状态灯巡检。
- LogisticsMove 固定路线搬运。
- EduForge 教学训练闭环。

每个试点只选一个主任务，避免范围失控。

### 2. Baseline

试点开始前记录：

- 当前人工流程。
- 任务频率。
- 失败类型。
- 安全边界。
- 可采集数据。
- 预期节省或学习价值。

### 3. Deliverables

交付物：

- RobotMac Core / BoardBringupKit。
- Teleop Studio 采集流程。
- LeRobot-compatible dataset。
- CloudTwin 训练报告。
- EdgeRuntimeBench 运行证据。
- SafetyOps 发布和回滚记录。
- 三分钟试点复盘视频。

### 4. Acceptance Metrics

试点验收指标：

- 任务成功率。
- 单次任务时间。
- 人工接管次数。
- 失败回流样本数量。
- 运行稳定性。
- 数据集质量。
- 边缘推理延迟。
- 客户团队可复现程度。

### 5. Expansion Path

试点成功后进入：

- Fleet Kit：多机运维和订阅。
- Industry Pack：行业模板和私有技能包。
- SafetyOps：企业权限和审计。
- DataFlywheel：持续训练数据资产。

## Contract Structure

### Phase 0: Discovery

1 周。确认场景、任务、数据边界、硬件限制和验收标准。

### Phase 1: Bring-up

1-2 周。BoardBringupKit、相机、IO、安全、遥操作和数据采集。

### Phase 2: Train

1-2 周。CloudTwin 训练、评估、EdgeRuntimeBench profile 和部署包。

### Phase 3: Pilot Run

1-2 周。真实任务运行、失败接管、日志记录、复盘和扩展方案。

## Pricing Logic

不要一开始卖“完整机器人替代方案”。先卖可控试点：

- 固定试点费用：覆盖硬件、集成、工程和支持。
- 云训练额度：按任务或 GPU-hour 包计。
- 数据/技能交付：根据客户是否需要私有技能包定价。
- 运维订阅：试点成功后进入 Fleet Kit。
- 行业模板：多个客户复用后形成 Industry Pack。

## Competition Story

在项目书和答辩中，PilotContractKit 证明商业潜力不是空话：

- 有明确买家：实验室、工厂、系统集成商、高校。
- 有明确入口：4-8 周试点。
- 有明确验收：任务成功率、延迟、数据、失败回流。
- 有明确扩展：Fleet Kit / Industry Pack / Training subscription。
- 有 Qualcomm 价值：每个试点都导向 Qualcomm edge runtime。

## Why Qualcomm Should Care

如果 RobotMac 能把每个客户试点都包装成 Qualcomm edge deployment evidence，那么 Qualcomm 获得的不只是一次比赛曝光，而是：

- 企业客户接触 Qualcomm edge AI。
- 开发者围绕 Qualcomm target 训练和部署策略。
- 试点成功后进入多机运维和长期运行。
- 行业模板沉淀为可复用参考设计。

## Sources

- IFR service robots growth：https://ifr.org/news/service-robots-see-global-growth-boom
- Formic robot-as-a-service company：https://formic.co/
- Agility Robotics：https://www.agilityrobotics.com/
- GXO Logistics：https://gxo.com/
- LeRobot documentation：https://huggingface.co/docs/lerobot/index
- Qualcomm AI Hub：https://aihub.qualcomm.com/
