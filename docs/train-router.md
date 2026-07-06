# TrainRouter Pitch

更新时间：2026-07-06。云 GPU 价格、库存、区域和计费规则变化很快，正式训练前必须在供应商控制台再次确认。本页按照 YC / Airbnb 风格重新组织：先讲问题和时机，再讲解决方案、市场、商业模型、竞争、壁垒、演示和 Qualcomm 请求。

## One-Line Pitch

TrainRouter 是 LeRobot CloudTwin 背后的机器人训练交付层：把一份 `LeRobot job contract` 路由到中国云或海外云，并强制执行预算上限、数据边界、可复现评估和 Qualcomm edge artifact export。

用户不应该为了训练机器人策略而理解每家云的实例名、价格页、镜像差异、账单规则和停机风险。用户应该提交任务、数据、目标硬件和预算，平台自动选择合适训练路径，最后得到一个可部署、可回滚、可审计的机器人技能版本。

## Problem

机器人团队经常可以完成 demo，但很难完成可交付训练：

- GPU 价格和库存变化快，固定绑定一家 provider 会让成本和交付不可控。
- 中国客户和海外客户面对不同账号、付款、区域、数据合规和网络访问条件。
- 同一个 LeRobot 训练任务在不同云上跑，输出结果必须可比较。
- 最终产品价值不在云端，而在模型能否部署回 Qualcomm edge target。
- 企业客户需要预算、数据边界、审计、回滚和验收指标，不只是一个模型权重文件。

## Why Now

时机来自三条趋势叠加：

1. LeRobot 正在把真实机器人学习标准化。LeRobot 文档已经覆盖数据、训练、策略、teleoperation、robot processors 和 deployment；LeRobotDataset v3 将多模态时间序列、视频和元数据组织成可训练和可流式读取的数据层。
2. 机器人部署规模正在扩大。IFR 2025 报告显示 2024 年工业机器人安装量约 542,000 台，亚洲占 74%，中国占全球部署 54%。中国版和海外版是产品现实。
3. Qualcomm 边缘 AI 工具链正在给部署证据提供标准目标。Qualcomm AI Hub Workbench 支持模型转换、on-device profile、数值正确性验证和 QAIRT/QNN runtime 路径。

## Insight

TrainRouter 的商业定位不是“卖便宜 GPU”。便宜 GPU 会被供应商价格战吞掉。

真正的产品洞察是：机器人训练不是租算力，而是发布一个可审计的 skill release。

每次 release 都应该绑定：

- `dataset_hash`
- `dataset_region`
- `policy_type`
- `container_digest`
- `split_manifest`
- `seed`
- `budget_guard`
- `provider_adapter`
- `eval_harness`
- `qualcomm_target_profile`
- `edge_artifact_manifest`
- `rollback_package`

这些交付物才是商业客户愿意购买和复购的确定性。

## Solution

TrainRouter 把训练拆成五步：

1. Contract：写入 dataset、policy、target profile、budget、region 和 eval gate。
2. Route：按 China / Overseas / Auto lane 选择 AutoDL、阿里云 PAI、腾讯云 GPU、华为 ModelArts、Runpod、Lambda 或 Modal。
3. Train：锁定容器、split、seed、checkpoint、timeout 和 retry。
4. Evaluate：统一评估成功率、失败类型、动作平滑度、baseline delta 和 replay metrics。
5. Export：输出 Qualcomm edge policy package、runtime evidence、回滚包和 SkillDock 发布凭证。

## Job Contract Example

```yaml
job_name: labforge-act-transfer-v4
dataset_uri: lerobot://labforge/sample-transfer-v1
dataset_hash: sha256:demo-placeholder
dataset_region: china
privacy: private
policy: act
target_profile: dragonwing.qcs8550.robotmac.core
budget:
  max_gpu_hours: 8
  max_cost_usd_equivalent: 80
  warning_at_percent: 70
  checkpoint_at_percent: 85
  stop_at_percent: 95
routing:
  preferred_lane: china
  allowed_providers: [autodl, aliyun_pai, tencent_gpu]
  require_private_storage: true
  allow_cross_region: false
eval:
  split_manifest: split_manifest.json
  seed: 20260706
  min_success_rate: 0.75
  compare_against_baseline: true
export:
  artifact: qualcomm_edge_policy_package
  runtime_targets: [qairt, qnn, onnxruntime_qnn]
  rollback_package: required
```

## Product Modules

### 1. Job Contract Builder

把训练任务描述成一份可执行合约：

- Dataset：LeRobot-compatible dataset URI、版本、隐私级别和数据地域。
- Policy：ACT、Diffusion Policy、SmolVLA 或后续策略类型。
- Target：QCS8550 / QCS6490 / Dragonwing / IQ 系列边缘部署 profile。
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

训练前估算费用，训练中监控 GPU-hour 和日志：

- 70%：warning。
- 85%：force checkpoint。
- 95%：stop 或 human approval。
- 超出上限：deny retry，保存日志与 checkpoint。

### 4. Data Boundary

客户数据默认不跨区域：

- China lane：AutoDL / PAI / Tencent / ModelArts。
- Overseas lane：Runpod / Lambda / Modal。
- Auto lane：只允许公开 demo、合成数据，或显式 cross-region approval。
- 平台声称“执行路由与审计策略”，不声称自动满足 PIPL/GDPR/行业合规。

### 5. Eval Harness

所有 provider 输出的模型都用同一套评估脚本、同一套 dataset split 和同一套任务指标，避免不同云训练结果不可比较。

### 6. Edge Artifact Export

训练结束后输出统一的 Qualcomm edge policy package，进入 EdgeRuntimeBench、SkillCertKit 和 SkillDock。

## Market

优先客户：

- LeRobot 开发者和高校实验室：需要低摩擦训练和比赛展示。
- 机器人初创公司：需要把 demo 变成可复现的版本发布。
- OEM / 模组厂 / 机器人平台商：需要为开发者提供训练和部署路径。
- 系统集成商：需要把训练成本写进 4-8 周试点合同。
- 工厂、仓储、实验室、服务企业创新部门：需要数据不乱跑、预算不失控、结果可验收。

## Business Model

TrainRouter 可以从四个层级收费：

1. Developer Starter：固定小预算训练额度，公开或非敏感数据，基础评估与 edge export。
2. Pro Lab：平台订阅费 + compute pass-through + orchestration margin，支持多次 train/eval loop。
3. SI Pilot：4-8 周固定试点包，包含数据采集、训练迭代、Qualcomm edge evidence 和验收报告。
4. Enterprise Private Lane：私有存储、区域策略、SSO/RBAC、审计日志、指定 provider、年度平台费。

## Competition

TrainRouter 不正面竞争云 GPU 供应商，而是站在它们上面：

- Runpod / Lambda / Modal：提供海外 GPU 与 serverless AI jobs。
- AutoDL / PAI / Tencent GPU / ModelArts：提供中国云训练资源。
- Ray / SkyPilot / Kubeflow：提供通用调度或 MLOps 基础设施。
- AWS Batch / SageMaker：提供 hyperscaler-centric 训练路径。
- Viam / Formant / Foxglove：提供部分机器人运维、数据或可视化工具。
- NVIDIA Isaac：提供 GPU-first robotics stack。

缺口：没有一层把 LeRobot 数据、双云训练、预算边界、统一评估和 Qualcomm edge export 绑定成机器人商业交付物。

## Moat

短期壁垒：

- Provider adapter contract。
- Robot profile templates。
- Job contract templates。
- Budget/data-boundary defaults。

中期壁垒：

- Episode lineage。
- Failure/takeover mining。
- 固定 eval harness。
- Qualcomm board profile library。

长期壁垒：

- Skill release graph。
- Policy compatibility matrix。
- Edge runtime evidence history。
- SkillDock marketplace 上架与回滚记录。

## Demo Plan

比赛演示不应该只展示“云能跑”。它应该证明“训练能交付”。

1. 打开 LeRobot job contract，选择 dataset、policy、target profile、预算和数据地域。
2. 展示 China / Overseas / Auto route decision。
3. 展示 cost estimate、budget guard 和 data boundary。
4. 展示 mock 或真实 training queue。
5. 展示统一 eval report。
6. 展示 Qualcomm export gate：model format、AI Hub job、QAIRT/QNN target、profile metrics。
7. 展示 rollback package。
8. 展示 SkillDock 上架状态：没有 edge evidence 不可发布。

## Qualcomm Ask

为了把 TrainRouter 从网页原型推进到复赛 demo，需要向 Qualcomm 请求：

- AI Hub compile/profile 额度。
- Dragonwing / QCS8550 / RB3 Gen 2 等 target profile 指导。
- Device Cloud 或真实开发板访问。
- QAIRT / QNN / ONNX Runtime QNN 的推荐路径。
- Qualcomm Profiler 指标模板。
- Robotics Hub 样例发布或技术 review。

## Claim Boundaries

可以声称：

- LeRobot-compatible。
- Qualcomm-first。
- 双云训练路由架构。
- 预算/data-boundary/eval/export workflow。
- 机器人技能 release evidence。

不能声称：

- 已获得 Qualcomm 官方认证或合作。
- 自动满足 PIPL/GDPR/行业合规。
- 任意模型都能无损编译到 QNN。
- 性能一定优于 Jetson / x86。
- 云训练可以替代本体安全策略。

指标必须标注来源：`simulated`、`replay-eval`、`Device Cloud`、`measured-on-hardware`，并附日期、板卡、SDK/runtime、模型版本、dataset hash、功耗/散热假设和 run count。

## Evidence Artifacts

首版文档和原型应生成以下证据文件：

- `job_contract.v1.yaml`
- `provider_adapter_contract.v1.md`
- `budget_guard.json`
- `cost_estimate.json`
- `data_boundary.yaml`
- `region_policy.yaml`
- `storage_layout.txt`
- `dataset_manifest.json`
- `split_manifest.json`
- `eval_harness.lock`
- `artifact_manifest.json`
- `qualcomm_export_manifest.json`
- `run_recovery_log.jsonl`
- `audit_log.jsonl`
- `metric_labels.json`
- `claim_boundaries.md`

## Sources

- LeRobot documentation：https://huggingface.co/docs/lerobot/en/index
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- IFR World Robotics 2025：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- Runpod pricing：https://www.runpod.io/pricing
- Lambda instances：https://lambda.ai/instances
- Modal pricing：https://modal.com/pricing
- Alibaba Cloud PAI DLC billing：https://www.alibabacloud.com/help/en/pai/billing-of-dlc
- Tencent Cloud GPU：https://www.tencentcloud.com/product/gpu
- Huawei Cloud ModelArts：https://www.huaweicloud.com/intl/en-us/product/modelarts.html
- AutoDL GPU docs：https://www.autodl.com/docs/gpu/
- Ray on Kubernetes：https://docs.ray.io/en/latest/cluster/kubernetes/index.html
- SkyPilot：https://github.com/skypilot-org/skypilot
- Kubeflow：https://www.kubeflow.org/docs/started/introduction/
- Qualcomm AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN Execution Provider：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
