# 研究笔记：云 GPU 与训练供应商组合

更新时间：2026-07-05。价格、地域和库存会变化，正式提交或演示前需要再次确认。

## 产品设计原则

这不是“选择一家云”。机器人商业化产品需要支持两个版本：

- 中国版：优先保证国内访问、中文控制台、企业付款、数据合规和现场售后。
- 海外版：优先保证快速启动、按秒/按小时弹性、容器体验、全球区域和开发者生态。

底层训练规范保持一致，上层供应商 adapter 可替换。这样可以避免把产品商业命运绑定在单一云厂商的 GPU 库存、价格和区域策略上。

## 中国版候选

| 供应商 | 适合角色 | 优点 | 风险/注意 |
| --- | --- | --- | --- |
| 阿里云 PAI | 企业版主路径 | PAI 覆盖标注、开发、训练、部署；DSW/DLC/EAS 能形成完整 AI 工程流程；国内区域丰富。 | GPU 价格、资源计划和区域库存需以控制台为准；产品 adapter 会偏企业化。 |
| 腾讯云 GPU + TI-ONE | 互联网/自动驾驶风格任务 | GPU 云服务器支持深度学习训练，官方页面强调按秒计费、小时结算、弹性购买释放。 | 需要区分 IaaS GPU 与 TI-ONE 平台能力；价格需按地域核算。 |
| 华为云 ModelArts | 政企/工业客户 | 一站式 AI 开发平台，适合强调合规、工业客户和企业交付。 | 海外/国内控制台、资源和生态差异要验证。 |
| AutoDL | 开发者/比赛快速试验 | 国内开发者熟悉、门槛低、适合快速租卡跑训练。 | 企业级权限、审计、SLA 和私有数据合规能力需要补充。 |

### 中国版建议组合

- Demo / 初赛：AutoDL 或阿里云 PAI DSW，快速展示 ACT 训练闭环。
- 企业故事：阿里云 PAI 或华为 ModelArts，强调数据、训练、部署、审计。
- 弹性算力：腾讯云 GPU，强调按需释放和高性能训练。

## 海外版候选

| 供应商 | 适合角色 | 优点 | 风险/注意 |
| --- | --- | --- | --- |
| Runpod | 开发者默认路径 | 官方 pricing 显示 Pods、Serverless、Clusters；多区域、按秒/按小时；A100/H100/H200/B200 等选择清楚。 | 社区云与安全云边界要明确；企业合规需单独评估。 |
| Lambda | 高可信训练集群 | 官方 pricing 强调 Instances、1-Click Clusters、Superclusters；B200/H100/A100 实例价格透明。 | 更偏 AI infra，机器人产品需要自己补训练控制台体验。 |
| Modal | Serverless 训练/评估任务 | 按秒计费、自动伸缩，适合短训练、评估、数据处理和异步 job。 | 对长时间大规模训练可能不如专用实例直观；区域溢价需计算。 |
| Paperspace | 简化 notebook 体验 | 适合个人和小团队 notebook/实验。 | 当前产品线和 GPU 库存需实测。 |

### 海外版建议组合

- Demo / 海外开发者：Runpod Pods 跑 LeRobot 训练，简单、便宜、快。
- 团队/集群：Lambda 1-Click Clusters，用作高可信训练基础设施。
- 异步 job：Modal 跑评估、模型导出、数据转换和 Web API。

## 价格锚点

只作为 pitch 里的“可行性锚点”，不要写死为长期承诺：

- Runpod pricing 页面展示了 L4、A40、A100、H100、H200、B200 等 GPU 的按小时价格，并标注 Pods 支持按秒/按小时。
- Lambda pricing 页面展示了 NVIDIA B200、H100、A100、GH200 等实例和 1-Click Cluster 价格。
- Modal pricing 页面展示了 GPU task 按秒计费，例如 H100、A100、L40S、L4、T4 等。
- 腾讯云 GPU 页面展示了深度学习训练场景、自动驾驶场景，以及按秒计费、小时结算的 pay-as-you-go 描述。
- 阿里云 PAI 产品说明覆盖 PAI-iTAG、PAI-Designer、PAI-DSW、PAI-DLC、PAI-EAS 等全流程能力。

## 对产品的结论

云 GPU 不是卖点本身，卖点是“训练不再是机器人团队的系统工程”。用户只需要提交任务、数据和目标硬件；平台负责把 job 跑在合适云上，把结果带回 Qualcomm 边缘设备。

## 信息来源

- 阿里云 PAI：https://www.alibabacloud.com/en/product/machine-learning
- 阿里云 PAI 购买与计费指南：https://help.aliyun.com/en/pai/product-overview/pai-product-purchase-guidelines
- 腾讯云 GPU：https://www.tencentcloud.com/products/gpu
- 华为云 ModelArts：https://www.huaweicloud.com/intl/en-us/product/modelarts.html
- AutoDL：https://www.autodl.com/
- Runpod pricing：https://www.runpod.io/pricing
- Lambda pricing：https://lambda.ai/pricing
- Modal pricing：https://modal.com/pricing
