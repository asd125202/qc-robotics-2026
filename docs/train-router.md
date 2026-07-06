# TrainRouter Pitch

更新时间：2026-07-06。云 GPU 价格、库存、区域、计费规则、spot/竞价中断、LeRobot 版本、AI Hub/QNN/QAIRT 支持矩阵和 Qualcomm 设备可用性变化很快；正式训练前必须在供应商控制台、AI Hub、目标板卡和数据合规要求中再次确认。

## One-Line Pitch

TrainRouter 是 LeRobot CloudTwin 背后的受控机器人训练执行平面：把一份不可变的 `LeRobot robot job contract` 路由到中国云、海外云或私有 lane，并强制执行预算 admission、数据边界、checkpoint 恢复、固定评测、artifact provenance 和 Qualcomm edge export gate。

核心叙事：

> 机器人训练不是“找一块便宜 GPU 跑脚本”，而是发布一个可审计、可复现、可回滚、可部署到 Qualcomm edge 的 skill release。TrainRouter 把通用云 runner 变成机器人训练供应链。

## 01 · Problem

机器人团队能录数据，也能训练一次模型，但很难把训练变成交付。

真实痛点不是“没有 GPU”，而是：

- 成本不可控：云预算通常不是天然硬封顶；spot/竞价会中断；GPU 价格、库存、区域和存储费用变化很快。
- 数据边界不可见：中国客户、海外客户、公开 demo 数据和企业私有数据面对不同区域、账号、付款、发票、访问和合规约束。
- 训练不可复现：不同 provider、镜像、dataset revision、split、seed、checkpoint 和代码版本会让结果不可比较。
- 评测不可采购：训练 loss 下降不等于机器人任务变好；客户需要固定 eval protocol、失败类型、回放视频、人工确认和 release verdict。
- 边缘导出断裂：云端 checkpoint 不是产品，必须进入 ONNX/PT2、AI Hub/QNN/QAIRT、profile、inference 校验、artifact hash 和 rollback package。
- 买方不止 ML 团队：FinOps、Procurement、Security、Legal、Data Governance 都会问预算、区域、审计、权限、数据驻留和责任边界。

## 02 · Current Alternatives Fail

现有工具强在“运行任务”，弱在“机器人训练交付”。

- Kubernetes Job 负责让 Pod 跑到完成，但不理解 LeRobot dataset、observation/action schema、机器人 embodiment、传感器校准、eval gate 和 edge export。
- SkyPilot 很强在跨云 GPU 提交、成本/容量选择和失败恢复，但它不提供机器人训练 contract、数据权利、Qualcomm artifact receipt 和 policy promotion gate。
- Ray Jobs、Kubeflow、AWS Batch/SageMaker、Vertex AI、Azure ML 提供训练 job schema 或 pipeline，但通常停在云内资源、容器、输入输出和模型 registry。
- W&B、MLflow、HF Jobs 支持 experiment tracking、队列、artifact、model registry 和复现实验，但不会强制机器人专用 preflight、behavior gate、edge gate 和 rollback drill。
- RunPod、Lambda、Modal、CoreWeave、AutoDL、阿里 PAI、腾讯 GPU、华为 ModelArts 提供算力或训练环境，不负责把训练结果变成 Qualcomm edge skill release。
- RobotOps / data tools 如 Viam、Formant、Foxglove 解决 fleet、teleop、数据可视化或运维，但不是受控训练执行平面。

TrainRouter 不替代这些工具，而是站在它们上面：它把 runner 当 backend，把机器人 job contract、routing policy、evidence bundle 和 Qualcomm export gate 做成产品层。

## 03 · Solution

TrainRouter = Robot Job Contract + Lane Policy + Budget Admission + Data Boundary + Reproducible Eval + Artifact Provenance + Qualcomm Export Gate。

它把训练拆成五个受控动作：

1. Contract：写入 kind、dataset revision、policy、robot profile、budget、data class、region、eval protocol 和 edge target。
2. Route：按 China / Overseas / Private lane 选择 AutoDL、阿里 PAI、腾讯 GPU、华为 ModelArts、RunPod、Lambda、Modal、CoreWeave 或 BYOC runner。
3. Train：锁定 LeRobot version、container digest、full CLI、split、seed、checkpoint policy、timeout、retry、spot policy 和 logs。
4. Evaluate：运行固定 eval gate，输出 success、failure tags、intervention rate、replay evidence、baseline delta 和 gate verdict。
5. Export：提交 Qualcomm edge export gate，返回 compile/profile/inference/download receipt、runtime evidence、artifact hash 和 rollback package。

一句话：TrainRouter 不承诺“自动选最便宜 GPU 就能稳定交付”，它承诺每一次训练都在明确边界内运行、留下证据，并把结果推到 Qualcomm edge 可验证门槛。

## 04 · Why Now

时机来自三条趋势叠加：

- LeRobot 正在把机器人训练标准化：`lerobot-train`、HF Jobs、LeRobotDataset v3、`lerobot-eval`、`lerobot-rollout`、HIL/DAgger 和 policy zoo 已经给出共同语言。
- 双云训练成为现实：海外有 RunPod、Modal、Lambda、CoreWeave；中国有 AutoDL、阿里 PAI、腾讯 GPU、华为 ModelArts。价格、库存、spot 中断和企业采购差异，让路由层变得有价值。
- 企业买方需要受控执行：预算硬停、数据驻留、跨境审批、审计日志、RBAC/SSO、artifact provenance、SIEM 导出和证据包正在进入 AI/机器人采购语言。
- Qualcomm edge AI 工具链补齐部署目标：AI Hub、QNN/QAIRT、ONNX Runtime QNN、Device Cloud、Profiler、Qualcomm Linux 和 QIR SDK 让 edge export gate 可以被产品化。
- CloudTwin 已经定义了 episode-to-policy release，TrainRouter 正好承担其中最难标准化的执行层。

## 05 · Product

用户看到的是训练订单和验收单，不是云厂商控制台。

产品工作流：

1. Build Contract：选择 `train/eval/rollout/hil/dataset_op`、LeRobot dataset、policy、robot profile、target board、data class、region 和 budget。
2. Preflight Admission：检查 dataset v3 schema、camera keys/FPS、stats、task text、policy input/output features、data region、spot_allowed 和 checkpoint policy。
3. Route Lane：按规则选择 China / Overseas / Private lane；非幂等、无 checkpoint、敏感数据禁止 spot/community；紧急交付走 on-demand/预留/专属。
4. Estimate & Guard：生成 cost estimate、max_cost、hard_stop_policy、warning/checkpoint/stop thresholds 和 approval flow。
5. Execute Job：渲染完整 LeRobot CLI，提交 HF Jobs、SkyPilot、Kubernetes、Ray、PAI、AutoDL、Modal 或 BYOC adapter，记录 job id、logs 和 resource metrics。
6. Recover：spot/竞价中断时根据 checkpoint_interval、fallback_pool 和 retry policy 恢复；无法安全恢复则停止并导出 recovery log。
7. Evaluate Gate：固定 dataset/model/code/container revision、split、seed 和 eval protocol；仿真、回放和真实机器人指标分开标注。
8. Export Edge：把通过 gate 的模型送到 Qualcomm export gate，记录 AI Hub job IDs、runtime、device、latency、memory、op fallback 和 artifact hash。
9. Package Release：生成 skill release package、rollback package、qualcomm_export_manifest 和 SkillCertKit/SkillDock 凭证。
10. Audit：输出 Budget/FinOps Pack、Data Boundary Pack、Governance/Provenance Pack 和评委版 evidence table。

## 06 · Product API/Evidence

TrainRouter 的核心不是“发起训练”，而是保存不可变 robot job contract。

示例：

```yaml
kind: train
job_name: labforge-act-transfer-v4
runner: autodl_or_pai_or_runpod_or_modal_or_byoc
dataset:
  repo: lerobot://labforge/sample-transfer-v1
  revision: full_commit_hash
  split_manifest: split_manifest.json
  episode_indices: [0, 1, 2, 3]
  region: china
  data_class: private_factory_video
policy:
  type: act
  base_checkpoint: sha256:...
  train_steps: 50000
  batch_size: 64
  seed: 20260706
execution:
  image_digest: sha256:...
  full_cli: lerobot-train ...
  max_cost_usd_equivalent: 80
  hard_stop_policy: checkpoint_then_stop
  spot_allowed: false
  checkpoint_interval_minutes: 20
eval:
  protocol: pinned_replay_and_real_smoke
  min_success_rate: 0.75
  max_intervention_rate: 0.10
  baseline_policy: policy_v3
export:
  target: qualcomm_ai_hub
  runtime_targets: [onnxruntime_qnn, qairt_dlc, qnn_context]
  target_devices: [rb3_gen2_qcs6490, qcs8550]
  rollback_package: required
audit:
  artifact_provenance: required
  audit_sink: siem_or_jsonl
```

每个 job 必须返回 evidence bundle：

- Rendered command、runner adapter、job id/url、status、logs、resource metrics、cost estimate vs actual。
- Dataset commit、split/episode ids、LeRobot version、container digest、seed、train_config、checkpoint hash。
- Eval artifacts：`eval_info.json`、rollout videos、failure/intervention episode ids、gate verdict、human approval。
- Budget/FinOps Pack：阈值审批流、kill-switch 演练、spot 中断恢复测试。
- Data Boundary Pack：region allowlist、data class、跨境审批状态、storage/log/artifact residency notes。
- Governance/Provenance Pack：SSO/RBAC role matrix、immutable audit log、SBOM、SLSA/in-toto-style provenance。
- Qualcomm Export Receipt：compile/profile/inference/download job IDs、target device/SoC/OS、runtime、latency/load time/memory、op fallback、artifact hash。

## 07 · Market & Business Model

第一批客户不是“所有 AI 团队”，而是已经把真实机器人数据变成交付压力的人。

客户：

- LeRobot 开发者和高校实验室：需要低摩擦训练、固定预算、比赛展示和 reproducible eval pack。
- 机器人初创公司：需要把 demo 变成可复现版本发布，避免云脚本、数据和边缘部署断裂。
- OEM / 模组厂 / 机器人平台商：需要给开发者提供从数据到 Qualcomm edge 的训练与部署路径。
- 系统集成商：需要把训练成本、数据边界、验收指标和回滚写进 4-8 周试点合同。
- 企业工厂、仓储、实验室、服务机器人创新部门：需要数据不乱跑、预算不失控、结果可验收、审计可导出。
- FinOps / Security / Legal / Procurement：需要 hard stop、approval、RBAC、region allowlist、SIEM audit 和 evidence bundle。

商业模式：

- Developer Starter：固定小预算训练额度、公开/非敏感数据 lane、基础 eval 和 edge export skeleton。
- Pro Lab：平台订阅费 + compute pass-through + orchestration margin，支持多次 train/eval/retry loop。
- SI Pilot：4-8 周固定试点包，包含数据采集、训练迭代、Qualcomm edge evidence 和验收报告。
- Enterprise Private Lane：BYOC/VPC、私有存储、区域策略、SSO/RBAC、审计日志、指定 provider、年度平台费。
- Governance Pack：FinOps、Data Boundary、Provenance、EU/China evidence export 作为企业附加模块。

推荐 lane defaults：

- Overseas dev：Modal 短任务/批处理，RunPod Secure 或 Lambda 单机训练，可中断任务才用 interruptible/spot。
- Overseas enterprise：CoreWeave Flex/Reserved/On-Demand 或 Lambda clusters，spot 只给可在 2-5 分钟安全 checkpoint 的任务。
- China dev：AutoDL 按量 + 同区文件存储，不能把本地盘当可靠 checkpoint。
- China enterprise：阿里 PAI-DLC/DSW 优先，腾讯/华为作为 IaaS、专属资源池或采购偏好 fallback。

## 08 · Competition & Moat

TrainRouter 不正面竞争云 GPU 供应商和调度框架，而是成为机器人训练控制面。

竞争层：

- GPU/Cloud：RunPod、Lambda、Modal、CoreWeave、AutoDL、阿里 PAI、腾讯 GPU、华为 ModelArts。
- Generic orchestration：Kubernetes Jobs、SkyPilot、Ray Jobs、Kubeflow、AWS Batch/SageMaker、Vertex AI、Azure ML。
- MLOps/Registry：W&B Launch、MLflow、HF Jobs、model registry、artifact tracking。
- RobotOps/Data：Viam、Formant、Foxglove、CloudTwin、RobotCoreOS 等上下游。

差异化：

- Typed robot job contract：observation/action schema、embodiment、sensor calibration、sim/real split、dataset lineage、policy type、robot target。
- Data-boundary-aware routing：China / Overseas / Private lane、region allowlist、data class、artifact/log residency。
- Robot eval gates：preflight gate、artifact gate、behavior gate、human approval、failure/intervention evidence。
- Qualcomm edge receipts：AI Hub compile/profile/inference/download、QNN/QAIRT target、device-specific context caveat、artifact hash。
- Release graph：dataset -> train job -> eval gate -> edge artifact -> rollback -> SkillDock publish。

护城河：

- Provider adapter contract library。
- LeRobot job templates and eval protocols。
- Budget/data-boundary defaults for robot workloads。
- Qualcomm board profile and edge artifact history。
- Failure/takeover/recovery evidence graph。
- Skill release graph and marketplace publish/rollback records。

## 09 · Why Qualcomm

云可以换，机器人本体上的边缘标准不能换。

TrainRouter 把“云训练完成”变成 Qualcomm 关心的交付物：

- 源 checkpoint、ONNX/PT2 导出、量化日志、AI Hub job IDs。
- 目标 device/SoC/OS、runtime、QNN/QAIRT/ONNX Runtime QNN route。
- NPU placement、latency、load time、memory、op fallback、optrace/QHAS bottleneck notes。
- PyTorch baseline vs device output 的数值差异。
- 可下载 artifact hash、runtime manifest 和 rollback package。

Qualcomm 应该支持它，因为这补齐 prototype-to-production 断点：开发者不是只说“我训练好了”，而是带着 RB3/QCS6490、QCS8550、IQ9075/IQ9/IQ8 的可审计证据来关闭性能、算子、SDK 和部署问题。

Ask：

- AI Hub API quota、组织共享和 Device Cloud/真实设备访问。
- RB3/QCS6490/QCS8550/IQ9075/IQ8/IQ9 target profile 指导。
- QAIRT/QNN `soc_model` 映射、QNN EP 插件版本矩阵、context binary 最佳实践。
- Qualcomm Linux / QIR SDK 部署样例和 Profiler 指标模板。
- ACT / robotics policy 模型官方支持路线 review。
- Robotics Hub 样例发布或技术 review。

## 10 · Demo & Ask

8 分钟 demo 要证明的不是“云能跑”，而是“训练能交付”。

Demo storyboard：

1. Contract：打开 `robot_job_contract.yaml`，选择 dataset revision、policy、target profile、China/Overseas lane、budget、spot policy、eval gate。
2. Admission：展示 preflight 结果：dataset v3 schema、camera/FPS、split hash、data class、region allowlist、estimated cost、hard stop。
3. Route：展示 lane decision：AutoDL/PAI/RunPod/Modal/Lambda/CoreWeave 的选择理由、fallback 和 checkpoint policy。
4. Execute：展示 mock 或真实 training queue，包含 rendered LeRobot CLI、job id、logs、checkpoint、cost burn 和 interruption recovery。
5. Evaluate：展示 fixed eval report：success rate、failure tags、intervention rate、baseline delta、replay videos、gate verdict。
6. Export：展示 Qualcomm export gate：AI Hub job IDs、runtime target、target device、profile metrics、op fallback、artifact hash。
7. Package：展示 rollback package、SkillCertKit gate 和 SkillDock publish status：没有 edge evidence 不可发布。
8. Evidence：一键导出 Budget/FinOps、Data Boundary、Governance/Provenance、Qualcomm Export Receipt 和 claim boundaries。

比赛请求：

- 初赛：中文 pitch website、job contract schema、provider adapter matrix、budget/data-boundary policy、demo storyboard。
- 复赛：真实或 mock LeRobot training job、fixed eval pack、Qualcomm export receipt、artifact manifest、rollback drill。
- Qualcomm support：AI Hub/Device Cloud/QNN/Profiler/QIR 指导、板卡或远程设备访问、Robotics Hub review。

## Claim Boundaries

可以声称：

- LeRobot-compatible。
- Qualcomm-first。
- 双云训练路由架构。
- 预算 / data-boundary / eval / export workflow。
- 机器人技能 release evidence。
- Generic runners as backend, robot contract as product layer。

不能声称：

- 已获得 Qualcomm 官方认证或合作。
- 自动满足 PIPL/GDPR/EU AI Act/行业合规。
- 保证云成本不会超支。
- spot/竞价训练稳定不会丢进度。
- 任意模型都能无损编译到 QNN。
- 一次训练，所有 Qualcomm 设备通用。
- AI Hub profile latency 等于最终机器人 app latency。
- 性能一定优于 Jetson / x86。
- 云训练可以替代本体安全策略。

所有指标必须标注来源：`simulated`、`replay-eval`、`Device Cloud`、`measured-on-hardware`，并附日期、板卡、SDK/runtime、模型版本、dataset hash、功耗/散热假设和 run count。

## Sources

- LeRobot documentation：https://huggingface.co/docs/lerobot/en/index
- LeRobot real robot workflow：https://huggingface.co/docs/lerobot/en/il_robots
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- Hugging Face Hub Jobs：https://huggingface.co/docs/huggingface_hub/en/guides/jobs
- HF Hub revisions：https://huggingface.co/docs/huggingface_hub/en/guides/download
- RunPod billing：https://docs.runpod.io/accounts-billing/billing
- RunPod pods：https://docs.runpod.io/pods/overview
- Lambda instances：https://lambda.ai/instances
- Lambda billing：https://docs.lambda.ai/public-cloud/billing/
- Modal preemption：https://modal.com/docs/guide/preemption
- Modal long training：https://modal.com/docs/examples/long-training
- Modal GPU：https://modal.com/docs/guide/gpu
- CoreWeave capacity plans：https://docs.coreweave.com/platform/capacity-plans
- CoreWeave pricing：https://www.coreweave.com/pricing
- AutoDL pricing：https://www.autodl.com/docs/price/
- AutoDL storage：https://www.autodl.com/docs/fs/
- Alibaba PAI DLC billing：https://help.aliyun.com/zh/pai/product-overview/billing-of-dlc
- Alibaba PAI DLC：https://help.aliyun.com/zh/pai/what-is-dlc
- Alibaba PAI workspace regions：https://help.aliyun.com/zh/pai/create-and-manage-workspaces
- Tencent GPU billing：https://cloud.tencent.com/document/product/560/8025
- Tencent spot instances：https://cloud.tencent.com/document/product/213/17817
- Huawei ModelArts billing：https://support.huaweicloud.com/intl/zh-cn/price-modelarts/price-modelarts-0035.html
- Huawei ModelArts resource pools：https://support.huaweicloud.com/usermanual-standard-modelarts/resmgmt-modelarts_0003.html
- Kubernetes Job：https://kubernetes.io/docs/concepts/workloads/controllers/job/
- SkyPilot overview：https://docs.skypilot.co/en/latest/overview.html
- Ray Jobs：https://docs.ray.io/en/latest/cluster/running-applications/job-submission/index.html
- Kubeflow Trainer：https://www.kubeflow.org/docs/components/trainer/operator-guides/migration/
- AWS Batch：https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html
- AWS SageMaker CreateTrainingJob：https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html
- W&B Launch：https://docs.wandb.ai/platform/launch/walkthrough
- MLflow Model Registry：https://mlflow.org/docs/latest/ml/model-registry/
- AWS Budgets controls：https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html
- GCP budgets：https://docs.cloud.google.com/billing/docs/how-to/budgets
- Azure budgets：https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets
- AWS Spot notices：https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html
- EU Data Act：https://digital-strategy.ec.europa.eu/en/policies/data-act
- EU AI Act：https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- PIPL translation：https://digichina.stanford.edu/work/translation-personal-information-protection-law-of-the-peoples-republic-of-china-effective-nov-1-2021/
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm AI Hub models：https://aihub.qualcomm.com/models
- Qualcomm ACT：https://aihub.qualcomm.com/models/act
- ONNX Runtime QNN Execution Provider：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm Linux：https://www.qualcomm.com/developer/software/qualcomm-linux
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
