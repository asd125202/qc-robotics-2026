# LeRobot CloudTwin Pitch

更新时间：2026-07-06。云 GPU 价格、区域、库存、计费规则、LeRobot 版本、AI Hub/QNN/QAIRT 支持矩阵、ONNX 导出路径和 Qualcomm 板卡性能变化很快；正式训练和复赛实测前必须按供应商控制台、SDK、板卡、模型、数据集和数据合规要求重新验证。

## One-Liner

LeRobot CloudTwin 是 Qualcomm-first 的机器人学习与发布控制面：把真实机器人 episode 变成 LeRobotDataset v3，路由到中国或海外 GPU 训练，锁定评测门禁，再打包成带 lineage、data rights、QNN/QAIRT profile、rollback 和 release evidence 的 Qualcomm edge policy。

核心叙事：

> 机器人公司现在可以很快训练一个策略，但很难把它安全、可复现、可审计、可回滚地部署到客户现场。CloudTwin 像机器人技能的 GitHub Actions + TestFlight：每个 policy release 都有数据来源、云训练记录、评测门禁、Qualcomm edge profile、灰度发布、回滚包和失败回流。

## 01 · Problem

机器人团队不是缺一个模型名词，也不是缺一个 GPU 链接，而是缺一条从真实经验到可交付技能的生产闭环。

今天的常见断点：

- 数据散：视频、状态、动作、时间戳、任务文本、操作者、接管、失败、安全事件和现场上下文散在不同脚本和文件夹。
- 训练碎：HF Jobs、RunPod、Modal、AutoDL、阿里 PAI、腾讯 GPU、华为 ModelArts 等都能跑，但账号、镜像、区域、预算、checkpoint、抢占恢复和日志互不统一。
- 权利不清：客户现场数据、工厂视频、个人信息、跨境传输、商业训练授权、保留期和删除权没有写进训练 contract。
- 评测不可比：同一任务在不同 split、seed、机器人、现场、云 GPU 和 policy 版本下训练，成功率不能直接比较。
- 边缘部署断裂：LeRobot 主要是 PyTorch/训练工作流；通用 ONNX/QNN 一键导出仍是缺口，模型权重不是可交付产品。
- 失败不增值：低置信、人工接管、任务超时、安全触发和客户拒收如果没有回流，就只是事故，不是下一轮训练资产。

买方真正问的是：这版技能用了哪些数据？能不能留在中国或海外指定区域？评测是否锁定？能不能跑在 Qualcomm edge？如果坏了，能否回滚？失败能不能让下一版更好？

## 02 · Current Alternatives Fail

现有替代方案都能解决一部分，但没有把 episode、训练、评测、边缘发布和失败回流连成商业产品。

- LeRobot 给了开源机器人学习引擎、Dataset v3、teleop、rollout、HIL/DAgger 和 policy 训练，但不是企业数据权利、双云训练、edge packaging、release governance 和客户审计系统。
- Hugging Face Jobs、RunPod、Lambda、Modal、AutoDL、阿里 PAI、腾讯 GPU、华为 ModelArts 卖算力或训练环境，但不理解 robot episode、policy safety gate、Qualcomm target profile 和 rollback。
- Foxglove、Formant、Viam 提供数据、fleet、teleop、ops 和观测能力，但 CloudTwin 聚焦 training/evaluation/deployment loop，把失败变成下一版可部署技能。
- NVIDIA Isaac、GR00T、Cosmos、Physical AI Data Factory 把竞争定义为 GPU-first data factory；CloudTwin 不做另一家 foundation model，而做 Qualcomm-first、LeRobot-compatible、双云可采购的 policy release factory。
- Physical Intelligence、Skild、Figure、Google Gemini Robotics 证明 generalist robot policy、现场数据和 embodied reasoning 正在升温，但中小机器人公司仍缺一条可复现、可回滚、可采购的窄任务训练闭环。
- 中国 AgiBot World、Unitree 和本土机器人数据生态说明国内也在形成数据供给；CloudTwin 的差异化是同时支持中国 lane、海外 lane、数据驻留、LeRobot 格式和 Qualcomm edge 发布。

因此，CloudTwin 不该说“我们也是大模型公司”或“我们卖最便宜 GPU”。更可信的定位是：把机器人失败变成下一版可部署、可审计、可回滚的 Qualcomm edge 技能。

## 03 · Solution

CloudTwin = Dataset Ledger + Dual-Cloud TrainRouter + Eval Gate + Data Rights Passport + LeRobot-to-Qualcomm Export Bridge + Edge Policy Packager + Failure Mining。

输入：

- RobotMac Core、TeleopStudio 或真实机器人采集的多相机视频、状态、动作、任务文本、operator role、success/failure、takeover、safety events、robot profile 和 site metadata。

输出：

- Qualcomm edge policy package，包含 policy hash、dataset lineage、data rights、固定 split、训练 job record、eval report、ONNX/TorchScript/QNN candidate、target board profile、runtime dependencies、rollback package 和 evidence bundle。

CloudTwin 的关键边界：

- 云端训练和持续改进，机器人本体端侧推理。
- 先从 ACT / SO-100 / SO-101 / 桌面机械臂窄任务做可演示闭环，再扩展 Diffusion、SmolVLA、Pi0、GR00T-style policy。
- 不声称 LeRobot 已一键导出所有模型到 Qualcomm NPU；CloudTwin 的价值正是补上 LeRobot checkpoint 到 ONNX/TorchScript 到 AI Hub/QNN 的工程桥。
- 不让云进入 safety-critical control loop；RobotCoreOS / SkillCertKit / SafetyOps 在本体侧做 admission、runtime gate 和 rollback。

## 04 · Why Now

机器人学习正在从论文和 notebook 变成产品交付流程。

- LeRobot v0.6.0 已把 `lerobot-rollout`、DAgger/HIL、`lerobot-eval`、HF Jobs 云训练、VLA/世界模型入口和真实机器人 workflow 推进到开发者可用层。
- LeRobotDataset v3 用 Parquet、MP4 chunk、metadata、tasks 和 episode 边界组织多模态时间序列，适合建立 episode ledger。
- 开源 policy 族谱已经足够丰富：ACT 适合作为比赛保底，Diffusion / SmolVLA / Pi0 / GR00T / Multitask DiT 形成可插拔升级路径。
- 海外 GPU 供给变成弹性市场：RunPod、Modal、Lambda、CoreWeave 能满足不同训练/评测/批处理需求。
- 中国 GPU lane 也足够实际：AutoDL 适合比赛和开发者速度，阿里 PAI 适合企业全链路，腾讯/华为适合已有采购和数据区域要求。
- 企业 AI 市场已经默认要求客户数据不进通用训练、区域数据驻留、数据权利、日志、人工监督、版本治理和回滚。
- Qualcomm 正在补齐 Dragonwing、AI Hub、QNN/QAIRT、Device Cloud、Profiler、Qualcomm Linux/QIR SDK 和 Robotics Hub，正好需要一个 LeRobot-to-edge 的开发者样板。

过去做 CloudTwin 太早，因为机器人学习工具和边缘部署链都不成熟。现在真正的新瓶颈变成：如何把策略安全、可复现、可审计地部署到现场。

## 05 · Product

第一版 wedge：

> 30-50 条真实示教 episode -> LeRobotDataset v3 -> 中国/海外训练 job -> 固定 eval gate -> Qualcomm edge package -> 本体运行 -> 失败回流。

产品工作流：

1. Record：采集 camera、state、action、timestamps、task text、success/failure、operator role、takeover 和 safety events。
2. Ledger：生成 LeRobotDataset v3、dataset card、episode hash、robot profile、site tag、rights passport 和 region policy。
3. Route：根据数据区域、预算、GPU class、抢占容忍度、客户账号和 provider availability 选择 China / Overseas / Private lane。
4. Train：以 ACT 为保底，支持 Diffusion/SmolVLA/Pi0 等可插拔策略；保存 config、seed、container digest、cost、logs、checkpoint 和 resume state。
5. Evaluate：锁定 train/val/test split，输出 success rate、failure class、action smoothness、intervention rate、latency budget、replay clips 和 release gate。
6. Export：把 LeRobot checkpoint 转成 ONNX/TorchScript/候选 QNN artifact，记录 operator coverage、fallback、数值误差和 device-specific constraints。
7. Package：生成 Qualcomm edge policy package：policy hash、target board、QNN/QAIRT/ONNX path、runtime deps、input shapes、rollback package 和 manifest。
8. Deploy：进入 RobotCoreOS / SkillCertKit，本体本地执行，不依赖云端实时控制。
9. Mine：低置信、人工接管、任务超时、safety hit 和客户反馈进入下一轮 training queue 和 regression test。
10. Audit：导出 Data Rights Pack、Robot Release Gate Pack、Rollback Drill Pack 和评委版 evidence table。

## 06 · Product API/Evidence

CloudTwin 的产品 API 是一份 policy release contract，而不是一个 notebook 链接。

示例 contract：

```yaml
cloudtwin_release:
  dataset:
    format: lerobot_dataset_v3
    revision: hf_commit_or_private_registry_digest
    region: china_or_overseas_or_private
    rights: commercial_training_allowed
    split_hashes: {train: sha256..., val: sha256..., test: sha256...}
  train_job:
    lane: autodl_starter_or_alibaba_pai_or_runpod_or_modal
    gpu: a10_or_l40s_or_a100_or_h100
    image_digest: sha256...
    seed: 42
    budget_cap: 200_usd
    checkpoint_hash: sha256...
  policy:
    algorithm: act
    checkpoint: sha256...
    export_path: onnx_or_torchscript_or_qnn_candidate
    target: qcs6490_or_qcs8550_or_iq_series
    rollback_to: policy_v11
  gates:
    eval_split_locked: true
    success_threshold: task_specific
    intervention_limit: task_specific
    latency_p95_limit_ms: measured_on_device
    human_approval: required
```

三份证据包：

- Data Rights & Lineage Pack：dataset card、model card、来源/授权/许可证、PII/redaction notes、驻留区域、保留期、train/val/test split hash、HF/MLflow/W&B/DVC-style version link。
- Robot Release Gate Pack：固定 eval split、仿真/回放/实机测试矩阵、失败分类、人工接管率、near-miss/safety event、审批人、生产 alias 和 QNN profile。
- Rollback Drill Pack：从 `model_v12 + policy_v7` 回滚到 `model_v11 + policy_v6` 的审计日志、影响范围、恢复时间、降级策略和下一轮 training queue。

所有数字必须贴标签：simulated、replay-eval、measured-on-device，不能把仿真成功率、回放评估和真实板卡延迟混成一个数字。

## 07 · Market & Business Model

第一批客户买的不是“便宜 GPU”，而是可交付训练闭环。

客户：

- LeRobot developer / research lab：需要低摩擦 dataset conversion、ACT/SmolVLA templates、HF Jobs/RunPod/AutoDL orchestration、eval report 和 edge export。
- 机器人创业公司 / OEM autonomy lead：有 prototype，但没有可靠 data/train/deploy loop，需要 dataset ledger、regression eval、model export 和 rollback package。
- 系统集成商：卖 4-8 周自动化试点，需要把“采集示教、训练 policy、交付 edge package、失败回流”写进固定范围合同。
- 企业工厂 / 仓库创新团队：关心数据不外流、上线可审计、事故可追责、版本可回滚、预算 guardrail 和 ROI evidence。
- RaaS / fleet operator：按活跃机器人购买 failure mining、fleet replay、canary policy rollout、OTA updates 和 success dashboard。
- 中国本土团队：需要中文支持、国内账号、国内付款、发票、数据本地训练、AutoDL/阿里/腾讯/华为 adapter 和私有化。

商业模式：

- Starter：比赛/高校/开发者包，包含固定任务模板、少量 storage、训练额度、eval report 和 edge package skeleton。
- Platform SaaS：workspace seat + dataset ledger + training job orchestration + eval gates + policy registry + evidence export。
- Managed Compute：GPU 成本 pass-through，叠加 orchestration margin、budget guard、preemption handling、checkpoint recovery、logs 和 artifact storage。
- Enterprise Lane：中国/海外/私有 lane、SSO/RBAC、数据驻留、审计、采购支持、on-prem/private artifact registry 和 support SLA。
- Skill Marketplace：经验证 policy package 可按 Qualcomm board profile、任务、机器人形态和 safety assumptions 上架抽成。

推荐 lane：

- China default：AutoDL Starter + Alibaba PAI Enterprise；腾讯/华为作为客户采购或政企偏好 fallback。
- Overseas default：RunPod Pods + Modal Burst；Lambda 用于可预测训练窗口；CoreWeave 用于更大企业集群。

## 08 · Competition & Moat

竞争分四层：

- Model/data factory：NVIDIA Physical AI Data Factory、Isaac/GR00T、Google Gemini Robotics、Physical Intelligence、Skild。
- Robot/data owners：Figure、Unitree、AgiBot World 和垂直机器人公司。
- Data/ops platforms：Foxglove、Formant、Viam、InOrbit、W&B、MLflow、HF Hub。
- Cloud GPU providers：RunPod、Lambda、Modal、CoreWeave、AutoDL、阿里 PAI、腾讯 GPU、华为 ModelArts。

CloudTwin 的差异化不是“比它们都大”，而是一个更窄、更可采购的闭环：

- LeRobot-compatible episode ledger。
- Dual-cloud job contract with China/overseas data lanes。
- Locked eval split and release gate。
- LeRobot-to-Qualcomm export bridge。
- Qualcomm edge profile and device-specific evidence。
- Rollback package and failure mining loop。
- Data rights passport for enterprise and China deployment。

护城河：

- Episode ledger：真实示教、失败、接管、恢复、场景标签、客户 site 和任务结果长期积累。
- Eval harness：同一 split、同一指标、同一 replay harness，让不同云、不同模型和不同版本可比较。
- Edge profile library：QCS6490、QCS8550、IQ 系列、camera、runtime、thermal、power、latency、QNN operator coverage 和 rollback matrix。
- Rights graph：数据来源、授权、驻留区域、保留期、商业训练权限、删除/freeze 状态和共享改进 policy。
- Distribution：RobotMac Core、TeleopStudio、TrainRouter、RobotCoreOS、SkillCertKit 和 Qualcomm ecosystem 共同导流。

## 09 · Why Qualcomm

云负责训练，Qualcomm edge 负责执行。CloudTwin 让 Qualcomm 拥有 post-training deployment standard，而不只是“机器人里的那块板”。

Qualcomm 应该关心：

- LeRobot/Hugging Face 是机器人开源流量入口；CloudTwin 把这批开发者从 GPU 云训练自然导向 RB3、QCS6490、QCS8550 和 IQ 系列。
- AI Hub/QNN/QAIRT 可以成为 policy release 的标准出口：不是只 profile 一个模型，而是成为每个机器人技能发布证据的一部分。
- Qualcomm Linux/QIR SDK/ROS 2 节点可以承接本体侧 camera ingest、NN inference、仿真、交叉编译和部署。
- Dragonwing Robotics Hub 可以获得一个端到端样例：teleop -> LeRobotDataset v3 -> cloud training -> AI Hub/QNN -> RobotCoreOS runtime -> failure mining。
- 双云架构适合中国和海外生态：海外开发者可用 RunPod/Modal/HF，国内客户可用 AutoDL/阿里/腾讯/华为和私有化。

向 Qualcomm 的请求：

- AI Hub 组织额度、Device Cloud 设备访问和 QNN/QAIRT office hours。
- ACT/LeRobot exporter 技术对接，澄清 Qualcomm ACT 在 RB3/QCS6490/QCS8550/IQ 系列上的支持和性能卡。
- RB3 Gen 2 Vision Kit / QCS6490 / QCS8550 / IQ 系列 board profile 验证。
- QIR/ROS 2 示例节点、Profiler 指标表和 Qualcomm Linux deployment review。
- 允许把 CloudTwin demo 做成 AI Hub Models/Apps、Dragonwing Robotics Hub tutorial 或比赛 reference sample。

## 10 · Demo & Ask

三分钟 demo 要证明：

> Cloud-trained. Qualcomm edge-deployed. Evidence-backed. Failure-improving.

Demo storyboard：

1. Record：SO-100/SO-101 或桌面机械臂采集 30-50 条 episode，记录 camera、state、action、timestamps、task text、success/failure 和 takeover。
2. Ledger：生成 LeRobotDataset v3、dataset card、rights passport、split hashes 和 region policy。
3. Train：提交 China/Overseas training job，展示 provider、GPU、cost cap、container digest、logs、checkpoint 和 resume state。
4. Evaluate：固定 eval split，展示 success rate、failure class、intervention rate、replay clips 和 release gate。
5. Export：输出 ONNX/TorchScript/QNN candidate，展示 operator fallback、PyTorch vs QNN action error、target board、latency/memory label。
6. Deploy：进入 RobotCoreOS / SkillCertKit，本体本地执行；云从安全控制闭环中断开。
7. Improve：触发失败或人工接管，片段进入下一轮 training queue，并生成 rollback drill。

评委画面必须出现 evidence table：

- dataset version。
- data region / rights。
- policy hash。
- provider / GPU / cost cap。
- target hardware。
- export path。
- eval status。
- edge latency / memory。
- rollback package。
- metric label: simulated / replay-eval / measured-on-device。

比赛 ask：

- 初赛：中文 pitch website、双云架构图、dataset/release contract、demo storyboard、claim boundaries、provider research。
- 复赛：真实 LeRobot dataset、CloudTwin prototype、一个训练 job、一个 eval report、一个 Qualcomm edge package、一个 rollback/failure-mining demo。
- Qualcomm support：6-8 周 validation sprint，AI Hub/QNN/Device Cloud/Profiler/QIR 指导，板卡 loaner，Robotics Hub publication 机会。

## Claim Boundaries

可以讲：

- LeRobot-compatible。
- Qualcomm-first。
- dual-cloud training architecture。
- edge evidence workflow。
- auditable policy release workflow。
- China/overseas data lane design。

避免讲：

- 已获 Qualcomm / Hugging Face / LeRobot 官方认证、合作、投资或 endorsement。
- 自动合规 EU AI Act、PIPL、GDPR、SOC 2、ISO 或功能安全认证。
- LeRobot 已一键导出所有 policy 到 ONNX/QNN。
- SmolVLA/Pi0/GR00T 已验证可直接跑在 Qualcomm NPU。
- 任意客户数据可自由跨境共享训练。
- HIL/DAgger 解决安全问题。
- Qualcomm NPU 可端侧跑所有 VLA。
- 50 条示教保证成功率。
- 性能优于 Jetson/x86。

所有 TOPS、延迟、功耗、温度、FPS、成功率必须注明日期、板卡、SDK、散热、电源、模型版本和 metric label。

## Sources

- LeRobot releases：https://github.com/huggingface/lerobot/releases
- LeRobot v0.6.0：https://huggingface.co/blog/lerobot-release-v060
- LeRobot docs：https://huggingface.co/docs/lerobot/en/index
- LeRobot real robot workflow：https://huggingface.co/docs/lerobot/il_robots
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot dataset v3 blog：https://huggingface.co/blog/lerobot-datasets-v3
- LeRobot inference / rollout：https://huggingface.co/docs/lerobot/en/inference
- LeRobot HIL data collection：https://huggingface.co/docs/lerobot/en/hil_data_collection
- LeRobot ACT：https://huggingface.co/docs/lerobot/en/act
- LeRobot SmolVLA：https://huggingface.co/docs/lerobot/en/smolvla
- LeRobot ONNX export issue：https://github.com/huggingface/lerobot/issues/3146
- RunPod pricing：https://www.runpod.io/pricing
- Lambda pricing：https://lambda.ai/pricing
- Modal pricing：https://modal.com/pricing
- Modal GPU docs：https://modal.com/docs/guide/gpu
- CoreWeave pricing：https://www.coreweave.com/pricing
- Alibaba PAI billing：https://help.aliyun.com/en/pai/product-overview/pai-product-purchase-guidelines
- Alibaba ECS spot：https://help.aliyun.com/zh/ecs/spot-instance
- Tencent GPU billing：https://www.tencentcloud.com/document/product/560/75944
- Tencent spot instances：https://www.tencentcloud.com/document/product/213/17816
- Huawei ModelArts billing：https://www.huaweicloud.com/special/info-modelarts-billing.html
- AutoDL：https://www.autodl.com/
- AutoDL GPU docs：https://www.autodl.com/docs/gpu/
- Huawei regions：https://www.huaweicloud.com/intl/en-us/securecenter/data_protection/region_query.html
- Tencent COS regions：https://www.tencentcloud.com/document/product/436/6224
- NVIDIA Physical AI Data Factory：https://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development
- NVIDIA GR00T N1：https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks
- Physical Intelligence openpi：https://www.pi.website/blog/openpi
- Physical Intelligence pi0.5：https://www.pi.website/blog/pi05
- Skild Series C：https://www.skild.ai/blogs/series-c
- Figure BMW production：https://www.figure.ai/news/production-at-bmw
- Figure Series C：https://www.figure.ai/news/series-c
- Gemini Robotics：https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/
- Gemini Robotics API overview：https://ai.google.dev/gemini-api/docs/robotics-overview
- AgiBot World：https://opendrivelab.com/AgiBot-World/
- Unitree open source：https://www.unitree.com/mobile/opensource/
- Viam：https://www.viam.com/
- Foxglove：https://foxglove.dev/
- Formant：https://formant.io/
- Hugging Face dataset cards：https://huggingface.co/docs/hub/en/datasets-cards
- Hugging Face model cards：https://huggingface.co/docs/hub/en/model-cards
- MLflow dataset tracking：https://mlflow.org/docs/latest/ml/dataset/
- W&B artifact lineage：https://docs.wandb.ai/models/artifacts/explore-and-traverse-an-artifact-graph
- EU Data Act：https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained
- EU AI Act：https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- China generative AI interim measures：https://www.chinalawtranslate.com/en/generative-ai-interim/
- PIPL Article 40：https://digichina.stanford.edu/work/translation-personal-information-protection-law-of-the-peoples-republic-of-china-effective-nov-1-2021/
- NIST AI RMF：https://www.nist.gov/itl/ai-risk-management-framework
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm ACT：https://huggingface.co/qualcomm/ACT
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm QCS6490：https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490
- Qualcomm QCS8550：https://www.qualcomm.com/news/onq/2023/04/qualcomm-qcm8550-and-qcs8550-processors-for-compute-intensive-apps
- Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm Linux：https://www.qualcomm.com/developer/software/qualcomm-linux
- Qualcomm QIR SDK：https://github.com/qualcomm-linux/meta-qcom-robotics-sdk
- Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
