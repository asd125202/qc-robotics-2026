# EdgeRuntimeBench Pitch

更新时间：2026-07-05。

## Core Thesis

比赛评分里有独立的 `Qualcomm processor application` 项。这个项目不能只说“会部署到 Qualcomm 板子”，而要展示一条可验证的边缘运行证据链：

> 云端训练出的策略，必须经过 compile / profile / package / deploy / monitor / rollback，最后在 Qualcomm edge target 上稳定运行。

EdgeRuntimeBench 是这个证据链的产品化页面和工程计划。

## Why This Matters

LabForgePilot 能证明机器人任务闭环。EdgeRuntimeBench 证明为什么 Qualcomm 是必要的：

- 策略推理必须在本体侧低延迟执行。
- 多相机输入和机器人控制需要本体同步。
- 安全边界不能依赖公网云。
- 比赛答辩需要拿出延迟、功耗、CPU/GPU/NPU 占用、温度和失败回滚证据。
- 企业客户需要知道模型版本是否适配具体硬件 profile。

## Runtime Pipeline

### 1. Policy Artifact

来源：LeRobot / CloudTwin 训练后的 ACT 或后续策略模型。

内容：

- 模型权重。
- 输入输出契约。
- 数据集版本。
- 训练配置。
- 评估结果。

### 2. Compile Target

目标：Qualcomm edge runtime profile。

内容：

- QCS8550 / QCS6490 / IQ-8275 profile。
- 输入 shape、camera stream、action rate。
- INT8 / FP16 / mixed precision 策略。
- 设备依赖和 runtime package。

### 3. Profile Bench

指标：

- 端到端延迟。
- 推理 FPS / action rate。
- CPU/GPU/NPU 占用。
- 内存占用。
- 温度和功耗。
- 连续运行稳定性。

### 4. Deploy Package

内容：

- policy package。
- runtime dependency manifest。
- device compatibility manifest。
- rollback package。
- release note。
- SafetyOps gate result。

### 5. Runtime Monitor

内容：

- 成功/失败 episode。
- action latency。
- safety boundary trigger。
- manual takeover。
- model version。
- rollback event。

## Competition Demo Use

EdgeRuntimeBench 可以作为 LabForgePilot 的技术证据页：

1. 展示 CloudTwin 训练出的策略 artifact。
2. 展示目标硬件 profile：Rhino X1 / QCS8550。
3. 展示 compile / profile / deploy 流程。
4. 在三分钟视频中短暂出现一屏 benchmark dashboard。
5. 在答辩 PPT 中放一张 runtime evidence table。

即使最终实际硬件到货较晚，也可以先用 manifest、模拟 profile 和离线回放证明工程边界。

## Suggested Evidence Table

初赛阶段可以先定义指标，复赛阶段填入实测结果：

| Evidence | Preliminary | Final |
| --- | --- | --- |
| Target device | Rhino X1 / QCS8550 selected | Actual board profile |
| Policy format | ACT policy artifact manifest | Exported edge package |
| Latency | Target threshold defined | Measured p50/p95 |
| Stability | Test plan defined | Continuous run result |
| Safety | SafetyOps gate defined | Trigger and rollback log |
| Failure feedback | DataFlywheel queue defined | Real failure episode |

## Product Value

EdgeRuntimeBench 不只是比赛材料，也能成为商业产品能力：

- 企业客户验收：证明模型真的适配设备。
- 系统集成商交付：生成部署报告。
- SkillDock 上架：技能包必须带 hardware compatibility 和 benchmark 结果。
- EdgeFleet 运维：运行指标长期回传。
- Qualcomm 生态：把开发者训练结果导向 Qualcomm edge target。

## Why Qualcomm Should Care

如果每个技能包都需要 Qualcomm device profile、runtime benchmark 和 deployment package，那么 Qualcomm 不只是“硬件选型”，而是技能分发、企业部署和平台认证的核心目标。

这能把比赛项目从“使用 Qualcomm 设备”升级为“围绕 Qualcomm edge runtime 构建产品机制”。

## Sources

- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm RB3 Gen 2 Development Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Rhino X1 / APLUX developer page：https://developer.aidlux.com/
- LeRobot documentation：https://huggingface.co/docs/lerobot/index
