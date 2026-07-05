# TrainRouter Pitch

更新时间：2026-07-05。云 GPU 价格、库存、区域和计费规则变化很快，正式训练前必须在供应商控制台再次确认。

## Core Thesis

CloudPlan 说明“可以在哪些云训练”，DualCloudOps 说明“双云如何保持同一个 job contract”。TrainRouter 则把这件事产品化：

> TrainRouter = LeRobot job contract + China/overseas provider routing + budget guard + data boundary + evaluation harness + Qualcomm edge artifact export。

用户不应该为了训练机器人策略而理解每家云的实例名、价格页、镜像差异、账单规则和停机风险。用户应该提交任务、数据、目标硬件和预算，平台自动选择合适训练路径。

## Why This Matters

机器人云训练有四个现实问题：

- GPU 价格和库存会变，固定绑定一家 provider 会让成本和交付不可控。
- 中国客户和海外客户面对不同账号、付款、区域、数据合规和网络访问条件。
- 同一个 LeRobot 训练任务在不同云上跑，输出结果必须可比较。
- 最终产品价值不在云端，而在模型能否部署回 Qualcomm edge target。

TrainRouter 的商业定位不是“卖便宜 GPU”，而是卖训练确定性：预算可控、数据边界可控、训练结果可比较、部署包可落地。

## Product Modules

### 1. Job Contract Builder

把训练任务描述成一份可执行合约：

- Dataset：LeRobot-compatible dataset URI、版本、隐私级别和数据地域。
- Policy：ACT、Diffusion Policy、SmolVLA 或后续策略类型。
- Target：QCS8550 / QCS6490 / IQ 系列边缘部署 profile。
- Budget：最大 GPU-hour、最大费用、最长运行时间和 fallback GPU。
- Region：China、Overseas 或 Auto。
- Eval：成功率、失败类型、动作平滑度、训练日志和 artifact 指标。

### 2. Provider Router

根据任务约束选择 provider：

- 中国开发者快速试验：AutoDL。
- 中国企业训练路径：阿里云 PAI / 华为 ModelArts。
- 中国弹性 GPU：腾讯云 GPU。
- 海外快速试验：Runpod。
- 海外团队训练：Lambda。
- 海外短任务和评估：Modal。

### 3. Budget Guard

训练前估算费用，训练中监控 GPU-hour 和日志，超出预算自动停机、降级或进入人工确认。

### 4. Data Boundary

客户数据默认不跨区域。中国版 job 留在中国 lane，海外版 job 进入 overseas lane。公共 demo 数据可以选择 Auto。

### 5. Eval Harness

所有 provider 输出的模型都用同一套评估脚本、同一套 dataset split 和同一套任务指标，避免不同云训练结果不可比较。

### 6. Edge Artifact Export

训练结束后输出统一的 Qualcomm edge policy package，进入 EdgeRuntimeBench、SkillCertKit 和 SkillDock。

## Routing Contract Example

```yaml
job_name: labforge-act-transfer-v4
dataset_uri: lerobot://labforge/sample-transfer-v1
dataset_region: china
policy: act
target_profile: robotmac.core.pro.qcs8550
budget:
  max_gpu_hours: 8
  max_cost_usd_equivalent: 80
  fallback_gpu: a10_or_4090
routing:
  preferred_lane: china
  allowed_providers: [autodl, aliyun_pai]
  require_private_storage: true
eval:
  min_success_rate: 0.75
  compare_against_baseline: true
export:
  artifact: qualcomm_edge_policy_package
  rollback_package: required
```

## Competition Story

TrainRouter answers a concrete judge question: “你们说支持中国云和海外云，具体怎么落地？”

初赛阶段可以展示：

- 一个 LeRobot job contract。
- 一个 China / Overseas provider router dashboard。
- 一个预算和数据边界策略。
- 一个 mock training queue。
- 一个统一 edge artifact manifest。

复赛阶段可以真实跑：

- 一次海外 Runpod 或 Lambda 小训练。
- 一次中国 AutoDL 或 PAI 小训练。
- 同一份评估报告结构。
- 同一种 Qualcomm edge deployment package。

## Commercial Value

TrainRouter 让云训练成为可销售订阅：

- 开发者购买 GPU-hour 包，而不是自己管理云账号。
- 企业购买私有训练 lane、预算控制和审计报告。
- 系统集成商把训练成本写进 4-8 周试点合同。
- SkillDock 开发者把训练结果转成可认证技能包。
- Qualcomm 获得跨云训练后的稳定边缘部署目标。

## Sources

- Runpod pricing：https://www.runpod.io/pricing
- Lambda pricing：https://lambda.ai/pricing
- Modal pricing：https://modal.com/pricing
- Alibaba Cloud PAI：https://www.alibabacloud.com/product/machine-learning
- Tencent Cloud GPU：https://www.tencentcloud.com/products/gpu
- Huawei Cloud ModelArts：https://www.huaweicloud.com/intl/en-us/product/modelarts.html
- AutoDL：https://www.autodl.com/
- LeRobot documentation：https://huggingface.co/docs/lerobot/index
- Qualcomm AI Hub：https://aihub.qualcomm.com/
