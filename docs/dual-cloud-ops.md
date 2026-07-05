# DualCloudOps Pitch

更新时间：2026-07-05。

## Core Thesis

机器人训练云不能只做一个版本。商业化需要两条路线：

- 中国版：面向国内客户、国内数据、国内支付和国内 GPU 供应商。
- 海外版：面向海外开发者、海外客户和国际 GPU 供应商。

但产品层不能分裂成两套系统。DualCloudOps 的目标是：

> 用同一个 LeRobot Job Contract 描述训练任务，用不同 provider adapter 执行任务，最后输出同一种 Qualcomm edge policy package。

这让 RobotMac 可以在两个市场销售，而不让用户重新理解数据格式、训练流程和部署包。

## Why It Matters

GPU 云价格、容量、地域和采购路径变化很快。把产品绑定到某一家云，会产生三类问题：

- 成本不可控：用户希望按预算选择 GPU，而不是被固定价格锁住。
- 市场不可控：中国客户和海外客户面对不同的账号、付款、数据和合规要求。
- 交付不可控：某个区域缺货时，训练任务应该能迁移到另一个 provider。

DualCloudOps 不卖“最便宜 GPU”。它卖的是一套训练执行抽象：

- 任务描述标准化。
- Provider adapter 可替换。
- 成本和时长可观测。
- 评估结果可比较。
- 输出包和本体部署保持一致。

## Job Contract

每个训练任务都被描述为一份合约：

- Dataset：LeRobot 数据集路径、版本、隐私级别。
- Policy：ACT、Diffusion Policy 或后续 VLA 模型。
- Target：Qualcomm edge device profile。
- Budget：最高预算、最长训练时长、GPU 偏好。
- Region：China 或 Overseas。
- Eval：必须通过的任务成功率、延迟、失败类型。
- Export：模型、推理依赖、回滚包和说明文档。

用户不需要关心底层云厂商的细节。企业管理员可以关心预算、数据边界和验收结果。

## China Lane

适合场景：

- 国内高校、工厂、系统集成商和开发者社区。
- 数据不适合出境的企业试点。
- 需要中文支持、国内付款和国内 GPU 区域的项目。

首批 adapter：

- Alibaba Cloud GPU products.
- Tencent Cloud GPU products.

产品策略：

- 首先支持小规模 ACT 训练和评估。
- 训练镜像保持统一，provider 差异放在 adapter 层。
- 报告输出中文成本、时长、评估和部署包摘要。

## Overseas Lane

适合场景：

- 海外开发者和开源社区。
- 需要快速获取 H100/A100/4090 等 GPU 的实验团队。
- 需要和 Hugging Face / LeRobot / GitHub workflow 更紧密结合的团队。

首批 adapter：

- RunPod GPU cloud.
- Lambda GPU cloud instances.

产品策略：

- 先支持快速原型和按需训练。
- 与 GitHub repo、Hugging Face dataset、Cloudflare Pages demo 串起来。
- 报告输出英文/中文双语成本、评估和部署包摘要。

## Product Modules

### 1. Job Contract Builder

用户选择数据集、策略类型、目标硬件、预算上限和市场区域，系统生成可执行训练合约。

### 2. Provider Adapter

不同云厂商的账号、镜像、存储、GPU SKU、计费和日志差异被封装在 adapter 内。

### 3. Cost Guard

训练开始前预估预算，训练中监控花费，超过阈值自动停机或降级。

### 4. Eval Harness

不同 provider 训练出的模型使用同一套评估脚本和指标，避免“换云以后结果不可比”。

### 5. Edge Exporter

无论云端在哪里训练，最终都输出同一种 Qualcomm edge policy package。

## Competition Story

初赛不需要真的接入所有 provider。建议做三层证据：

1. 文档：定义 LeRobot Job Contract。
2. 原型：静态 dashboard 展示 China / Overseas 两条训练 lane。
3. Demo：实际跑一个小训练任务，再把结果部署到 Qualcomm edge target。

评委能看到：

- 产品有中国版和海外版。
- 商业化不依赖单一云供应商。
- Qualcomm 本体部署目标保持稳定。
- Cloud GPU 只是训练资源，不是机器人实时控制中心。

## Why Qualcomm Should Care

DualCloudOps 把全球 GPU 云的不确定性压在云端 adapter 层，把稳定的部署目标留给 Qualcomm edge。

这对 Qualcomm 有三个价值：

- 开发者无论在哪个云训练，最后都导向 Qualcomm edge target。
- 企业客户可以选择本地合规的云，而不牺牲本体部署体验。
- Qualcomm 可以把自己的开发板、AI Hub、示例模型和认证流程包装成跨云训练后的默认落地路径。

## Sources

- Alibaba Cloud GPU products：https://www.alibabacloud.com/product/gpu
- Tencent Cloud GPU products：https://www.tencentcloud.com/products/gpu
- RunPod pricing：https://www.runpod.io/pricing
- Lambda GPU cloud instances：https://lambda.ai/instances
- LeRobot documentation：https://huggingface.co/docs/lerobot/index
- Qualcomm RB3 Gen 2 Development Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
