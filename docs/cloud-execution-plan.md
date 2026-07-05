# Cloud Execution Plan

更新时间：2026-07-05。价格和库存会变化，正式训练前必须再次在供应商控制台确认。

## Decision

比赛阶段建议采用“双路径、单接口”：

- 中国演示路径：阿里云 PAI DSW/DLC 或 AutoDL。
- 海外演示路径：Runpod Pods 或 Lambda Instances。
- 异步评估/导出：Modal。

统一接口是一个训练任务规范，而不是绑定单一云：

```yaml
job_name: act-grasp-v3
robot_profile: qcs8550_tabletop_arm
dataset_uri: lerobot://robotmac/tabletop-pick-v1
policy: act
gpu_target:
  china: autodl_or_pai
  global: runpod_or_lambda
budget:
  max_gpu_hours: 8
  preferred_gpu: a100_80g
export:
  target: qualcomm_edge_package
metrics:
  - success_rate
  - latency_ms
  - action_smoothness
  - failure_recovery_count
```

## Provider Roles

| Role | China version | Overseas version | Why |
| --- | --- | --- | --- |
| Fast experiment | AutoDL | Runpod | Low-friction GPU rental and fast developer workflow. |
| Enterprise story | 阿里云 PAI / 华为 ModelArts | Lambda | More credible for enterprise AI workflow and account governance. |
| Async utility jobs | 阿里云 PAI DLC / 腾讯云 GPU | Modal | Good for evaluation, export, and short-lived jobs. |
| Final commercial story | PAI + ModelArts options | Runpod + Lambda + Modal | Avoid single-provider dependency. |

## Current Public Price Anchors

Use these only as pitch feasibility anchors:

- Runpod pricing page currently shows H200 SXM at about `$4.31/hr` and A100 SXM at about `$1.79/hr`, with per-hour/per-second display.
- Lambda pricing page currently shows B200 SXM6 at `$6.69/GPU/hr`, H100 SXM at `$3.99/GPU/hr`, A100 80GB at `$2.79/GPU/hr`, A100 40GB at `$1.99/GPU/hr`, and V100 at `$0.79/GPU/hr`.
- Modal pricing page currently lists H100 at `$0.001097/sec` and L40S at `$0.000542/sec`; its GPU docs list support for T4, L4, A10, L40S, A100, H100, H200, B200 and related variants.
- Tencent Cloud GPU billing page states GPU 云服务器 supports 包年包月、按量计费、竞价实例和包销计费.
- Huawei ModelArts billing docs state ModelArts supports 包年/包月 and 按需计费, with compute resource charges including GPU/NPU.
- Alibaba PAI pricing/product pages describe PAI-DSW for notebook-style development, PAI-DLC for deep learning training, PAI-EAS for deployment, and PAI-Designer for visual modeling.

## Budget Story For The Proposal

Do not promise exact cost. Promise a controllable budget envelope:

1. Early demo: 2-8 GPU hours on A100/4090-class resources.
2. Serious training: 8-40 GPU hours depending on dataset size, policy, and number of experiments.
3. Final competition video: budget at least two full retraining cycles plus failure recovery data.

Pitch line:

> The product does not sell cheap GPUs. It makes robot training predictable: choose a task, choose a market version, cap GPU-hours, train, evaluate, deploy to Qualcomm edge.

## Implementation Plan

### Stage 1: No cloud account dependency

- Use static mock training jobs in the prototype dashboard.
- Define the job spec and provider adapter interface.
- Use public LeRobot examples for code structure.

### Stage 2: One real overseas run

- Runpod Pod or Lambda instance.
- Pull LeRobot repo.
- Train ACT on a small dataset.
- Export artifact manifest.

### Stage 3: One real China run

- AutoDL for quick run or Alibaba PAI DSW/DLC for enterprise story.
- Match the same job spec.
- Compare output artifacts and dashboard fields.

### Stage 4: Product adapter layer

- `src/cloud_adapters/base.py`
- `src/cloud_adapters/runpod.py`
- `src/cloud_adapters/lambda_cloud.py`
- `src/cloud_adapters/autodl.py`
- `src/cloud_adapters/pai.py`

## Sources

- Runpod pricing：https://www.runpod.io/pricing
- Runpod Cloud GPUs：https://www.runpod.io/product/cloud-gpus
- Lambda pricing：https://lambda.ai/pricing
- Modal pricing：https://modal.com/pricing
- Modal GPU docs：https://modal.com/docs/guide/gpu
- 阿里云 PAI 定价：https://www.aliyun.com/page-source/price/detail/machinelearning_price
- 阿里云 PAI DSW：https://www.aliyun.com/activity/bigdata/pai/dsw
- 腾讯云 GPU 计费：https://buy.cloud.tencent.com/price/gpu
- 华为云 ModelArts 计费：https://support.huaweicloud.com/intl/zh-cn/price-modelarts/price-modelarts-0035.html
- AutoDL：https://www.autodl.com/
