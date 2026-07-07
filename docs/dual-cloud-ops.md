# DualCloudOps Pitch

更新时间：2026-07-07。GPU 云价格、容量、区域、合规和 LeRobot 工具链变化很快；正式提交和客户交付前必须重新核对 provider SKU、价格、数据出境规则、Qualcomm AI Hub / QAIRT / QNN 支持矩阵和目标开发板。

## One-Line Pitch

DualCloudOps 是 LeRobot-to-Qualcomm 的双云训练执行层：一个 robot training contract，按数据边界、预算、GPU 可用性和采购策略自动选择中国云或海外云，最后生成可验签、可评估、可回滚的 Qualcomm edge release package。

## Thesis

机器人团队不是缺 GPU，而是缺一条能交付的训练流水线。

云 GPU 能把模型训出来；商业化要回答另外的问题：

> 数据能不能去那朵云？训练能不能复现？成本能不能封顶？模型能不能上 Qualcomm 边缘？失败后能不能回滚？

DualCloudOps 不卖另一朵 GPU 云，也不承诺最便宜 GPU。它卖的是：

> governed routing, reproducibility, data boundary, and Qualcomm edge evidence.

## 01 · Problem

LeRobot、低成本机械臂和云 GPU 让原型更快，但商业客户要的是交付证据。

真实机器人训练数据包含：

- 多相机视频、音频、深度、LiDAR、IMU、状态/action 时间序列。
- 工厂地图、工艺流程、设备布局、人员、工牌、客户现场和安全区域。
- operator log、manual takeover、failure clips、质量标签和现场异常。

问题不在于能不能开一张 GPU，而在于：

- 中国客户要求数据驻留、国内云采购、发票、日志留存、ICP/等保式材料和本地支持。
- 海外客户要求 enterprise controls、SOC2-style evidence、private registry、signed artifacts、SBOM、GDPR/enterprise governance。
- LeRobot 原型可以很快跑通，但 dataset commit、container digest、LeRobot version、seed、eval、checkpoint 和 edge profile 很难变成客户验收材料。
- GPU job 完成后只是 checkpoint，不是 Qualcomm edge 上的部署包；还需要 ONNX / QAIRT / QNN candidate、AI Hub profile、EdgeRuntimeBench、SafetyOps gate、签名和 rollback。

一句话：云端训练不是产品，能被客户采购和上板的 release 才是产品。

## 02 · Current Alternatives Fail

现有工具各自强，但没有把机器人策略变成可发布 artifact。

### Hyperscalers

AWS、GCP、Azure、阿里云、腾讯云、华为云、百度、火山引擎可信，企业采购和安全能力强，但 quota、成本、区域、GPU SKU、数据出境、训练脚本和机器人上板链路都要团队自己拼。

### Neoclouds

CoreWeave、Lambda、RunPod、Modal、Hugging Face Jobs、Together 等访问快、价格透明、适合 startup iteration，但不会替机器人团队判断哪些 robot video 可以去、哪些必须留在 region、哪些能进入 Qualcomm release gate。

### GPU Marketplaces

Vast、AutoDL、潞晨云等便宜，适合低敏实验和容错作业；但敏感工厂视频、客户地图、可识别人员和长期 SLA 需要更强分类、隔离、审计和 support。

### MLOps

W&B、MLflow、SageMaker、Vertex 能追踪实验，但不天然理解 LeRobotDataset v3、robot body、sensor schema、动作成功率、intervention rate、SafetyOps gate 或 QNN profile。

### Robot Data / Fleet Tools

Foxglove、Formant、Viam、InOrbit 收集和观察机器人数据，但不是以 train -> eval -> export -> edge release 为核心。

### Self-Built Scripts

自建脚本启动最快，商业化最慢。一旦进入中国/海外双市场、客户审计、发票、数据分类、provider policy、edge package 和回滚，维护成本迅速上升。

DualCloudOps 的准确位置：

> not another GPU cloud, not another MLOps dashboard, but the robotics training execution and release layer between LeRobot data and Qualcomm edge deployment.

## 03 · Solution

DualCloudOps 用一份 `Robot Training Contract` 连接双云训练和 Qualcomm edge release。

核心流程：

```text
Teleop / robot data
  -> LeRobotDataset v3
  -> Robot Training Contract
  -> China / overseas / HF Jobs / BYOC lane
  -> pinned train + eval
  -> export candidate
  -> AI Hub / QAIRT / QNN profile
  -> EdgeRuntimeBench evidence
  -> SafetyOps release gate
  -> signed rollbackable edge package
```

五个动作：

1. **Contract**：声明 dataset、policy、robot body、sensor schema、预算、隐私等级、区域、目标芯片和验收指标。
2. **Route**：按数据敏感度、区域、GPU 可用性、成本、interconnect、provider trust 和采购策略选择中国或海外 lane。
3. **Train**：固定 container digest、LeRobot version、Git SHA、random seed、dataset revision、checkpoint cadence 和 provider receipt。
4. **Gate**：运行 `lerobot-eval`、rollout / HIL / replay evidence、success rate、intervention rate、failure tags、latency 和 rollback rule。
5. **Ship**：输出 ONNX / QAIRT / QNN candidate、AI Hub profile、SBOM、provenance、signature、install manifest 和 rollback receipt。

重要边界：

- Cloud training is not in the safety loop。
- AI Hub profile latency is not full robot app latency。
- Cross-border access can be a data export event。
- One global model registry is not the safe default。

## 04 · Why Now

2026 年机会不是“再租一张 GPU”，而是把机器人训练变成可治理、可审计、可上板的工业流程。

### 4.1 LeRobot Is Ready For Productization

LeRobot v0.6 增加 `lerobot-eval`、`lerobot-rollout`、DAgger-style HIL correction、FSDP、HF Jobs cloud training、depth、language annotation 和更快数据加载。LeRobotDataset v3 用 Parquet / MP4 / metadata 结构化状态、动作、相机、任务和 episode offset，正适合作为 robot training contract 的数据底座。

### 4.2 GPU Supply Is Fragmented

H100 已经更普遍，H200 正在成为 serious training 常规选择，B200/GB200 可用但常受 reservation、enterprise sales 或集群门槛限制。hyperscaler 可信但重，neocloud 快，marketplace 便宜但风险更高。机器人团队需要 governed routing，而不是再多一个 provider login。

### 4.3 China And Overseas Markets Split Operationally

中国 lane 需要国内云、数据驻留、发票、账号/实名/采购、ICP、PIPL/数据出境评估和本地支持。海外 lane 需要 AWS/GCP/Azure/enterprise controls、neocloud startup speed、GDPR-style records、SOC2-style evidence、private registry 和 procurement notes。产品抽象不能分裂。

### 4.4 Qualcomm Edge Makes The Endpoint Concrete

Qualcomm AI Hub Workbench 支持 compile/profile，目标包括 ONNX、QNN DLC、QNN context binary 等路径；AI Hub profiling 能回答 latency、memory fit 和 NPU usage。DualCloudOps 把“云端训练”自然导向 Dragonwing / RB3 / QCS / IQ target。

## 05 · Product

第一版只做一个完整闭环，不做万能云平台。

### MVP

- 采集 50-100 个 SO-101 / tabletop robot episode。
- 转成 LeRobotDataset v3。
- 选择 China lane 或 Overseas lane。
- 训练 ACT；SmolVLA/VLA 只作为 forward-looking candidate，不承诺上 NPU。
- 跑固定 eval gate。
- 导出 Qualcomm edge release package。

### 5.1 Training Contract Builder

定义 dataset、policy type、robot body、camera schema、privacy tier、region lane、budget cap、target device、acceptance metrics 和 customer policy。

### 5.2 Provider Router

中国：

- CUDA Fast Path：阿里云、腾讯云、百度、火山引擎、AutoDL 等 NVIDIA A10/L20/A100-style 路线，用于最快 LeRobot pilot。
- Domestic Compliance Path：华为 Ascend、百度昆仑等，用于国产算力、主权采购或客户要求，但明确需要 porting / operator / profiling 验证。

海外：

- Enterprise Trust Path：AWS、GCP、Azure，用于 regulated data、procurement、IAM、security review。
- AI Native Path：CoreWeave、Lambda、RunPod、Modal、HF Jobs，用于快速训练、实验和 batch automation。
- Marketplace Path：Vast 等只用于低敏、可重跑、非客户生产数据。

### 5.3 Cost & Risk Guard

- budget cap、GPU quote、expected duration、storage、egress、idle disk、reservation commitment。
- spot/preempt restart policy and checkpoint cadence。
- provider allow/block list。
- data movement approval。
- region-specific object store affinity。

### 5.4 Eval Harness

- `lerobot-eval`。
- rollout / HIL correction。
- replay eval。
- success rate。
- intervention rate。
- failure classes。
- latency and deadline misses。
- baseline delta and release decision。

### 5.5 Edge Release Exporter

- PyTorch / ONNX / PT2 candidate。
- AI Hub compile/profile job receipts。
- QAIRT / QNN path。
- unsupported ops / fallback report。
- EdgeRuntimeBench profile。
- SafetyOps release gate。
- signed install manifest and rollback receipt。

## 06 · Product API/Evidence

卖点不是接了几朵云，而是每次训练都有合同、账本和 release evidence。

### APIs

```text
POST /v1/training-contracts
POST /v1/datasets/{id}:classify
POST /v1/contracts/{id}:route
POST /v1/contracts/{id}:launch
GET  /v1/provider-runs/{id}
POST /v1/eval-gates/{id}:run
POST /v1/edge-exports
POST /v1/qualcomm-profiles
POST /v1/signed-releases
GET  /v1/audit-packs/{id}.zip
```

### Core Objects

- `TrainingContract`: dataset、policy、robot_body、sensors、privacy_tier、region_lane、budget_cap、target_device。
- `DatasetLedger`: LeRobotDataset version、episode ids、rights、redaction、calibration hash、firmware hash、train/val/test split。
- `ProviderRun`: cloud、region、GPU SKU、container digest、LeRobot version、git SHA、seed、checkpoint cadence、spend。
- `EvalGate`: sim success、real rollout、intervention rate、latency p95、failure class、release decision。
- `ExportGate`: PyTorch / ONNX / PT2 candidate、unsupported ops、quantization plan、calibration data、fallback check。
- `EdgeProfile`: Qualcomm target、AI Hub compile/profile IDs、ONNX/QNN artifact、runtime、backend、memory、thermal envelope、offline mode。
- `SignedRelease`: model hash、dataset hash、SBOM、provenance、signature、attestation note、install manifest、rollback receipt。

### Example Contract

```yaml
robot_training_contract.v1:
  dataset:
    type: lerobot_dataset_v3
    repo: cn://customer-private/so101-pick-place
    revision: sha256:...
    privacy_tier: factory_video_sensitive
    region: mainland_china
  policy:
    type: act
    lerobot_version: pinned
    seed: 42
  lane:
    requested: china
    allowed_providers: [aliyun, tencent, baidu]
    blocked_providers: [community_gpu, overseas_public]
  budget:
    max_cost: 800
    currency: CNY
    max_hours: 4
  eval_gate:
    min_success_rate: 0.82
    max_intervention_rate: 0.12
    require_replay_eval: true
  edge_target:
    device: rb3-gen2-qcs6490
    outputs: [onnx_candidate, qnn_candidate, profile_report, signed_release]
```

### Evidence Pack

- `robot_training_contract.yaml`
- `dataset-ledger.json`
- `data-classification.json`
- `rendered-lerobot-command.txt`
- `provider-run-receipt.json`
- `cost-and-egress-report.json`
- `eval_info.json`
- `rollout-video-index.json`
- `failure-intervention-ledger.jsonl`
- `qualcomm-export-manifest.json`
- `ai-hub-job-receipts.json`
- `qnn-backend-report.json`
- `edge-profile.qualcomm.json`
- `safetyops-release-gate.json`
- `signed-release.intoto.jsonl`
- `rollback-record.json`
- `judge-audit-pack.zip`

## 07 · Market & Business Model

先卖给从 LeRobot demo 走向客户 pilot 的机器人团队。

### First Buyers

- 机器人 OEM CTO / AI 负责人：LeRobot 原型跑通了，但训练、量化、边缘部署不可重复。
- 系统集成商 / 具身智能实验室：需要 4-8 周交付 capture -> train -> evaluate -> export。
- 制造业自动化团队：工厂视频、动作数据、良率数据不能随便出境。
- 数据安全 / 法务 / 采购：需要 provider policy、data boundary、artifact provenance、发票、日志和权限。
- Qualcomm FAE / BD：客户有模型但不会稳定落到 Dragonwing / RB / QCS / IQ。

### China Version

- RMB 3k-20k / month team SaaS + compute pass-through。
- RMB 20k-80k pilot package for one task / one robot / one target。
- RMB 100k-800k / year enterprise private lane with China cloud adapters、SSO/RBAC、audit logs、private artifact store、local runner、fapiao/support。
- 收入重点不是 GPU margin，而是 training ops、procurement intelligence、private lane、validation and edge release。

### Global Version

- $499-$5k / month team SaaS + compute pass-through。
- $20k-$80k SI pilot package / 4-8 weeks。
- $100k-$500k / year enterprise lane with private registry、provider policies、audit logs、reserved-capacity planning、support SLA。
- HF / neocloud fast path for startups，hyperscaler path for enterprise customers。

## 08 · Competition & Moat

Provider adapter 容易复制；机器人 release evidence graph 不容易复制。

### Competition

- GPU orchestration：NVIDIA Run:ai。
- AI cloud / neocloud：CoreWeave、Lambda、RunPod、Modal、Vast、HF Jobs、Together、Replicate。
- MLOps：W&B、MLflow、SageMaker、Vertex。
- Robot data / fleet ops：Foxglove、Viam、Formant、InOrbit。
- China cloud / AI platforms：阿里云 PAI、腾讯 TI-ONE、华为 ModelArts、百度千帆/昆仑、火山引擎、AutoDL、智元/Unitree ecosystem。
- Internal scripts：every robotics lab starts here。

### Moat

短期：

- LeRobot job templates for ACT / Diffusion Policy / SmolVLA candidate。
- China / overseas provider policies。
- Qualcomm edge profile export recipes。

中期：

- Episode ledger：failure、takeover、rights、region、sensor manifest、calibration、robot profile。
- Eval harness：fixed splits、robot task metrics、regression gates、rollout/HIL evidence。
- Edge compatibility graph：policy + robot body + sensor config + Qualcomm target + latency / memory / backend / thermal evidence。
- Dual-region playbook：provider rules、data movement, budget, fapiao / invoice, support language, procurement notes。

长期：

- Procurement evidence：lineage、cost、eval、SafetyOps gate、rollback、SBOM、edge profile。
- Distribution through LeRobot community、Qualcomm robotics ecosystem、education kits and SI pilot templates。

## 09 · Why Qualcomm

DualCloudOps 把全球 GPU 云的不确定性，转化成 Qualcomm edge 的确定性需求。

- 每个 LeRobot job 从开始就声明 Qualcomm target，而不是训练完临时找部署路径。
- AI Hub / Workbench 成为 compile、quantize、profile、hosted-device validation 的标准最后一步。
- QAIRT / QNN / ONNX Runtime QNN profile 把 edge performance 从口头承诺变成报告。
- 中国云、海外云、neocloud、HF workflow 的训练结果都导向 Dragonwing / RB3 / QCS / IQ target。
- 对 Qualcomm FAE / BD：同一份 LeRobot job，切换中国/海外云，最后上同一块 board，是可复制 demo。
- 对比赛评委：这不是“用了开发板”，而是深度使用 Qualcomm processor application、AI Hub / QNN 和 edge runtime evidence。

## 10 · Demo & Ask

8 分钟 demo：同一份 LeRobot job，两条云路径，一份可验签边缘包。

### Demo Flow

1. 选择 SO-101 / tabletop arm 任务、LeRobotDataset v3、ACT policy、预算、数据等级和 `rb3-gen2-qcs6490` target。
2. 切换 China lane：阿里云 / 腾讯 / 百度 CUDA fast path；显示 data residency、no raw video export、provider runner、GPU、dataset hash、cost guard。
3. 切换 Overseas lane：AWS / GCP / Azure enterprise path 或 Lambda / RunPod / HF Jobs fast path；显示 egress、checkpointing、trust tier。
4. Launch job：生成 provider-specific runner，固定 container、LeRobot version、seed 和 job receipt。
5. Training complete：跑 `lerobot-eval`、rollout / replay eval，选择通过 success/intervention/latency gate 的 checkpoint。
6. Qualcomm export：导出 ONNX candidate，进入 AI Hub / QAIRT / QNN profile，记录 unsupported ops、backend、latency、memory、fallback。
7. Edge release：生成 SBOM、SLSA/in-toto provenance、cosign signature、install manifest、SafetyOps gate 和 rollback receipt。
8. Edge verify：在机器人 edge board 或模拟 target 验签，本地推理，展示 `cloud trained, edge executed, audit ready`。

### Qualcomm Ask

- Hardware：QCS6490 / QCS8550 / RB3 / IQ target guidance。
- Tooling：AI Hub / QAIRT / QNN / ONNX Runtime QNN office hours。
- Cloud：比赛云训练额度或合作云账户。
- Ecosystem：一个 OEM / SI / education kit pilot。
- Output：Dragonwing Robotics Hub 的 LeRobot-to-edge reference workflow 候选。

### Claim Guardrails

不能说：

- 自动合规。
- 绕过数据出境或出口管制。
- 所有 VLA 都能高性能跑 NPU。
- 最便宜 GPU。
- AI Hub profile latency 等于最终 robot app latency。
- 一份 QNN artifact 适合所有 Qualcomm device。
- 云训练在 safety loop。
- Qualcomm 官方认证或已合作。

必须说：

- governed routing。
- reproducibility。
- data boundary。
- edge evidence。
- metrics are labeled: simulated、replay-eval、AI-Hub-device-cloud、proxy、measured-on-board。

## Sources

- LeRobot docs：https://huggingface.co/docs/lerobot/en/index
- LeRobot v0.6：https://huggingface.co/blog/lerobot-release-v060
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot ACT：https://huggingface.co/docs/lerobot/en/act
- LeRobot multi-GPU：https://huggingface.co/docs/lerobot/en/multi_gpu_training
- Hugging Face Jobs：https://huggingface.co/docs/huggingface_hub/en/guides/jobs
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- AI Hub compile docs：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- AI Hub profile docs：https://workbench.aihub.qualcomm.com/docs/hub/profile_examples.html
- AI Hub quantize docs：https://workbench.aihub.qualcomm.com/docs/hub/quantize_examples.html
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Qualcomm IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Alibaba Cloud GPU：https://cn.aliyun.com/product/egs
- Alibaba PAI-Lingjun：https://cn.aliyun.com/product/bigdata/learn/pailingjun
- Tencent GPU Cloud：https://cloud.tencent.com/product/gpu
- Huawei Ascend Cloud：https://www.huaweicloud.com/product/modelarts/ascend-cloud.html
- Baidu GPU Cloud：https://cloud.baidu.com/product/gpu.html
- Volcengine ML Platform：https://www.volcengine.com/product/ml-platform
- Alibaba ICP guide：https://www.alibabacloud.com/en/icp
- Tencent ICP guide：https://www.tencentcloud.com/solutions/icp-registration-support
- AWS P6：https://aws.amazon.com/ec2/instance-types/p6/
- AWS Capacity Blocks：https://aws.amazon.com/ec2/capacityblocks/pricing/
- GCP GPUs：https://docs.cloud.google.com/compute/docs/gpus
- Azure ND H100 v5：https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndh100v5-series
- Lambda pricing：https://lambda.ai/pricing
- CoreWeave pricing：https://www.coreweave.com/pricing
- RunPod pricing：https://www.runpod.io/product/cloud-gpus
- Vast pricing：https://vast.ai/pricing
- Modal pricing：https://modal.com/pricing
- CAC data export Q&A：https://www.cac.gov.cn/2022-07/07/c_1658811536800962.htm
- CAC cross-border data provisions：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- CAC export threshold summary：https://www.cac.gov.cn/2024-03/22/c_1712776612187994.htm
- PIPL summary：https://www.pcpd.org.hk/english/data_privacy_law/mainland_law/mainland_law.html
- GDPR：https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- BIS Entity List：https://www.bis.gov/entity-list
- NVIDIA Run:ai：https://www.nvidia.com/en-us/software/run-ai/
- Foxglove：https://foxglove.dev/
- Formant：https://formant.io/
- SLSA：https://slsa.dev/
- Sigstore cosign：https://docs.sigstore.dev/cosign/signing/signing_with_containers/
