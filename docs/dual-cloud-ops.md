# DualCloudOps Pitch

更新时间：2026-07-06。GPU 云价格、容量、区域、合规和 LeRobot 工具链变化很快；正式提交和客户交付前必须重新核对 provider SKU、价格、数据出境规则、Qualcomm AI Hub / QNN 支持矩阵和目标开发板。

## One-Line Pitch

> 一个 LeRobot 训练任务，自动选择中国云或海外云，生成可验签的 Qualcomm 边缘部署包。

DualCloudOps 不卖另一朵 GPU 云。它卖的是机器人策略训练的执行和发布层：从真实 episode、LeRobotDataset、双云训练、仿真/真实评估，到 Qualcomm AI Runtime / QNN profile、签名、SBOM、provenance 和可回滚 edge release。

## Required Deck Spine

### 01 · Problem

机器人团队不是缺 GPU，而是缺一条能交付的训练流水线。

- 真实机器人数据包含视频、音频、地图、工艺流程、人员、工牌、动作轨迹和客户现场信息。
- 中国客户要求数据驻留、ICP/等保式材料、国内云采购、日志留存、本地合同和发票。
- 海外客户要求 SOC2-style evidence、SBOM、signed artifacts、reproducible provenance、GDPR/enterprise governance。
- LeRobot 原型可以很快跑通，但训练脚本、dataset commit、container、seed、eval、checkpoint 和 edge deployment 很难变成客户验收材料。
- 云端 checkpoint 不是 Qualcomm edge 上的部署包；还需要 ONNX/QNN/Qualcomm AI Runtime profile、延迟/内存报告、签名和 rollback。

### 02 · Current Alternatives Fail

现有工具各自强，但没有把机器人策略变成可发布 artifact。

- Hyperscaler：AWS、GCP、Azure、阿里云、腾讯云可信，但 quota、成本、区域、销售流程和上板链路都要团队自己拼。
- Neocloud：Lambda、RunPod、CoreWeave、Modal 快，但客户仍要决定数据能不能去、如何复现、如何审计。
- GPU marketplace：Vast、AutoDL、潞晨云便宜，但敏感 robot video、客户工厂数据和长期 SLA 需要更强分类和隔离。
- MLOps：W&B、MLflow、SageMaker、Vertex 追踪实验很好，但不天然理解 LeRobot episode、robot body、动作成功率、QNN profile。
- Robot fleet tools：Foxglove、Formant、Viam、InOrbit 收集和观察机器人数据，但不是以 train/eval/export release 为核心。
- 自建脚本：启动快，商业化慢；一旦进入中国/海外双市场、客户审计和边缘量产，维护成本迅速上升。

### 03 · Solution

DualCloudOps 用一份 Robot Training Contract 连接双云训练和 Qualcomm edge release。

流程：

1. Contract：声明 dataset、policy、robot body、camera schema、预算、区域、隐私等级、目标芯片和验收指标。
2. Route：按数据敏感度、区域、成本、GPU 可用性、采购策略和合规边界选择中国或海外 provider。
3. Train：生成 provider runner，固定 container digest、LeRobot version、Git SHA、random seed、dataset commit 和 checkpoint cadence。
4. Gate：用 sim、real rollout、failure replay、latency、intervention rate 和 rollback 规则做 release decision。
5. Ship：输出 ONNX/QNN candidate、runtime config、profile report、SBOM、SLSA/in-toto provenance、cosign signature 和回滚包。

### 04 · Why Now

云 GPU 访问已经不是稀缺能力；被治理的 GPU 路由才是商业化能力。

- LeRobot 形成真实机器人训练底座：teleoperation、LeRobotDataset、ACT/SmolVLA、rollout、sim eval、Hub workflow。
- GPU 供应高度碎片化：hyperscaler 可信但重，neocloud 快且透明，marketplace 便宜但需要 workload classification。
- 中国和海外市场的合规、账号、发票、数据边界和支持语言不同，但 robot training contract 不应该分裂。
- Qualcomm edge AI、AI Hub、QNN/Qualcomm AI Runtime 让云端训练结果可以变成低延迟、低功耗、可离线执行的本体策略。
- 客户、评委、保险、质量团队需要 dataset hash、model hash、SBOM、签名、profile 和可回滚 release，而不是一段 notebook。

### 05 · Product

第一版做一个完整闭环：

> 采集 50-100 个真实 episode -> LeRobotDataset -> 中国/海外 lane -> ACT/SmolVLA training -> sim/real eval -> Qualcomm edge release package。

模块：

- Training Contract Builder：dataset、policy、robot body、camera schema、预算、区域、隐私等级、目标芯片和验收指标。
- Provider Router：阿里云/腾讯云/华为云/百度、AWS/GCP/Azure、Lambda/RunPod/CoreWeave/Modal、Hugging Face Jobs。
- Cost & Risk Guard：训练前预算、spend cap、spot/preempt retry、data egress rule、敏感数据 provider blocklist。
- Eval Harness：固定 split、sim benchmark、real rollout、intervention labels、failure replay、latency、rollback gate。
- Edge Release Exporter：ONNX/QNN candidate、Qualcomm AI Hub / QNN profile、SBOM、SLSA/in-toto provenance、cosign signature。

### 06 · Product API

关键对象：

- `TrainingContract`: dataset_repo、policy_type、robot_body、sensors、privacy_tier、region_lane、budget_cap、target_device。
- `DatasetLedger`: LeRobotDataset version、episode ids、rights、redaction、calibration hash、firmware hash、train/val/test split。
- `ProviderRun`: cloud、region、GPU SKU、container digest、LeRobot version、git SHA、seed、checkpoint cadence、spend。
- `EvalGate`: sim success、real rollout、intervention rate、latency p95、failure class、rollback target、release decision。
- `EdgeProfile`: Qualcomm target、ONNX/QNN artifact、runtime、CPU/NPU fallback、memory、thermal envelope、offline mode。
- `SignedRelease`: model hash、dataset hash、SBOM、provenance、signature、attestation note、install manifest、rollback receipt。

示例：

```yaml
training_contract.v1:
  dataset: hf://private-org/so101-pick-place@sha256:...
  policy: {type: ACT, lerobot_version: "pinned", seed: 42}
  region_lane: china
  privacy_tier: factory_video_sensitive
  budget: {max_cost: 800, currency: CNY, max_hours: 4}
  provider_policy:
    allow: [aliyun, tencent, baidu]
    block: [community_gpu, overseas_public]
  eval_gate:
    min_success_rate: 0.82
    max_latency_ms: 60
    max_intervention_rate: 0.12
  edge_target:
    device: Qualcomm RB3 Gen 2
    export: [onnx, qnn_candidate, profile_report, signed_release]
```

### 07 · Market & Business Model

第一批买家：

- 机器人 OEM CTO / AI 负责人：LeRobot 原型跑通了，但训练、量化、边缘部署不可重复。
- 制造业自动化负责人：工厂视频、动作数据、良率数据不能随便出境。
- 数据安全/法务：不清楚哪些数据能跨境，模型包来源不可追踪。
- 采购/IT：GPU、云、板卡、SI、发票、日志和权限分散在不同系统。
- Qualcomm FAE/BD：客户有模型但不会稳定落到 Dragonwing/RB3/IQ10。

商业模式：

- Developer / education：starter credits、templates、LeRobot dataset conversion、basic eval report。
- Startup / team：workspace subscription、training concurrency、private registry、edge export targets、compute pass-through。
- SI pilot package：4-8 周固定费用，交付 capture -> train -> evaluate -> export。
- Enterprise private lane：年度合同，包含中国/海外数据边界、SSO/RBAC、audit logs、private artifact store、support SLA。
- Marketplace later：validated robot skill packages with hardware/runtime compatibility metadata。

Pricing hypothesis:

- 中国团队版：人民币 3k-20k / month + compute pass-through。
- 中国企业/私有化：人民币 100k-800k / year。
- 海外团队版：$499-$5k / month + compute pass-through。
- SI pilot package：$20k-$80k / 4-8 weeks。
- Enterprise lane：$100k-$500k / year。

### 08 · Competition & Moat

战略定位：

- Not another GPU cloud.
- Not another MLOps dashboard.
- Not another robot fleet dashboard.
- Not another foundation model company.
- The product is the robotics training execution and release layer between LeRobot data and Qualcomm edge deployment.

竞争地图：

- GPU orchestration：NVIDIA Run:ai。
- AI cloud + MLOps：CoreWeave + Weights & Biases。
- Neocloud GPU：CoreWeave、Lambda、RunPod、Modal。
- Model API / inference：Fireworks、Together、Baseten、Replicate、Modal。
- Open robot learning：Hugging Face LeRobot。
- Robot data / fleet ops：Foxglove、Viam、Formant、InOrbit。
- China analogues：Alibaba PAI/ModelScope、Tencent TI-ONE、Huawei ModelArts、AutoDL、AgiBot World、Dataa HARIX、Unitree。

壁垒不是 provider adapter。壁垒是 evidence graph：

- Episode ledger：真实 robot data、failure、takeover、rights、region、robot profile、sensor manifest。
- Eval harness：fixed splits、task metrics、replay/physical labels、regression gates。
- Edge compatibility graph：policy type + robot body + sensor config + Qualcomm target + latency/power/runtime evidence。
- Dual-region execution playbook：中国和海外 provider 的数据驻留、预算、artifact 移动规则和支持语言。
- Distribution：LeRobot community、Qualcomm robotics ecosystem、education kits、SI pilot templates。
- Procurement evidence：每个 release 带 lineage、cost、eval、safety gate、rollback、SBOM 和 edge profile。

### 09 · Why Qualcomm

DualCloudOps 把全球 GPU 云的不确定性，转化成 Qualcomm edge 的确定性需求。

- 每个训练 job 从开始就声明 Qualcomm target，而不是训练完才临时找部署路径。
- AI Hub / Workbench 可以成为 compile、quantize、profile 和 hosted-device validation 的标准最后一步。
- QNN / Qualcomm AI Runtime profile 让 edge performance 从口头承诺变成报告。
- 中国客户可以在国内云训练，海外客户可以在 AWS/GCP/Azure/Lambda/RunPod/CoreWeave/Modal 训练，但最后都导向 Qualcomm package。
- 对 FAE/BD：同一份 LeRobot job，切换中国/海外云，最后上同一块 Qualcomm board，是可复制 demo。

### 10 · Demo & Ask

8 分钟演示：

1. 选择 SO-101/桌面臂任务、LeRobotDataset、ACT/SmolVLA、预算、数据等级和 Qualcomm RB3/IQ10 target。
2. 切换“中国云/海外云”：中国模式显示阿里云/腾讯云/华为云/百度、数据驻留、no raw video export；海外模式显示 AWS/GCP/Azure/Lambda/RunPod。
3. Launch job：同一份 LeRobot config 生成 provider-specific runner，展示 GPU、dataset hash、checkpoint lineage、cost guard。
4. Training complete：选择通过 success rate / validation / latency gate 的 checkpoint。
5. Qualcomm target：导出 PyTorch/ONNX，进入 AI Hub/QNN/local toolchain profile。
6. Signed edge package：生成 model artifact、runtime config、latency/memory report、SBOM、dataset/model hashes、SLSA/in-toto provenance、cosign signature。
7. Edge verify：部署到 robot edge board，验证签名，本地推理，展示 cloud trained、edge executed、audit ready。

对 Qualcomm 的请求：

- 比赛开发板和 AI Hub / QNN profile hook。
- 云训练额度或合作云账户。
- 一个 OEM、SI、教育套件或工厂场景 pilot。
- 把 DualCloudOps 作为 Qualcomm robotics developer funnel：所有 LeRobot job 都有一条自然的 Qualcomm edge release 路径。

## China / Overseas Provider Strategy

中国 lane：

- Enterprise cloud: Alibaba Cloud, Tencent Cloud, Volcano Engine, Baidu AI Cloud, Huawei Cloud。
- Flexible GPU: UCloud/Compshare, AutoDL, 潞晨云, 恒源云, 青椒云, 趋动云。
- 默认规则：敏感 factory video、person data、maps、customer site logs 留在中国云或客户私有环境；跨境只移动 hash、SBOM/VEX、model/package id、redacted metrics 和显式批准的 artifact。

Overseas lane：

- Enterprise-trust hyperscalers: AWS, GCP, Azure。
- AI-native GPU clouds: Lambda, CoreWeave, RunPod, Modal。
- Marketplace / developer clouds: Vast.ai, Hugging Face, Paperspace。
- 默认规则：sensitive real robot data 走 AWS/GCP/Azure/Lambda Secure/CoreWeave；fast iteration 走 Lambda/RunPod Secure/Modal；non-sensitive synthetic/sim 低成本实验才考虑 marketplace。

## Claim Guardrails

- 不说“自动合规”或“绕过出口管制/数据出境规则”。
- 不说“所有模型都能高性能跑在 NPU 上”；ACT 更现实，SmolVLA/VLA 需要拆分、量化和 profile。
- 不说“最便宜 GPU”；卖点是 governed routing、reproducibility、data boundary 和 edge release。
- 不说云端训练可以绕过本体 safety gate；机器人实时控制仍在边缘侧。
- 不把 Hugging Face Jobs、RunPod、Lambda、阿里云等描述成已签约合作，除非真实签约。

## Sources

- LeRobot docs：https://huggingface.co/docs/lerobot/en/index
- LeRobot real robots：https://huggingface.co/docs/lerobot/en/il_robots
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot ACT：https://huggingface.co/docs/lerobot/en/act
- LeRobot SmolVLA：https://huggingface.co/docs/lerobot/en/smolvla
- LeRobot multi-GPU：https://huggingface.co/docs/lerobot/en/multi_gpu_training
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- AI Hub compile docs：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- AWS P6：https://aws.amazon.com/ec2/instance-types/p6/
- AWS Capacity Blocks：https://aws.amazon.com/ec2/capacityblocks/pricing/
- AWS compliance：https://aws.amazon.com/compliance/
- GCP accelerator pricing：https://cloud.google.com/products/compute/pricing/accelerator-optimized
- Azure ND H100 v5：https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndh100v5-series
- Lambda pricing：https://lambda.ai/pricing
- Lambda trust：https://lambda.ai/trust
- CoreWeave pricing：https://www.coreweave.com/pricing
- RunPod GPU pricing：https://www.runpod.io/product/cloud-gpus
- RunPod secure vs community：https://docs.runpod.io/pods/choose-a-pod
- Vast pricing：https://vast.ai/pricing
- Modal pricing：https://modal.com/pricing
- Hugging Face pricing：https://huggingface.co/pricing
- Hugging Face security：https://huggingface.co/docs/hub/en/security
- Alibaba Cloud GPU：https://www.aliyun.com/product/ecs/gpu
- Alibaba ACS GPU：https://help.aliyun.com/zh/cs/user-guide/gpu/
- Tencent GPU specs：https://cloud.tencent.com/document/product/560/19700
- Volcano Engine GPU：https://www.volcengine.com/product/gpu
- Baidu GPU：https://cloud.baidu.com/product/gpu.html
- Huawei GPU：https://www.huaweicloud.com/product/gpu.html
- AutoDL：https://www.autodl.com/
- CAC cross-border data rules：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- PIPL：https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm
- MIIT ICP：https://beian.miit.gov.cn/
- NVIDIA Run:ai：https://www.nvidia.com/en-us/software/run-ai/
- CoreWeave W&B acquisition：https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases
- W&B docs：https://docs.wandb.ai/
- Foxglove：https://foxglove.dev/
- Formant：https://formant.io/
- SLSA：https://slsa.dev/
- Sigstore cosign：https://docs.sigstore.dev/cosign/signing/signing_with_containers/
