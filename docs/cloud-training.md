# LeRobot CloudTwin Pitch

更新时间：2026-07-06。云 GPU 价格、区域、库存、计费规则、AI Hub / QNN / QAIRT 支持矩阵和模型转换路径变化很快；正式训练和复赛实测前必须按供应商控制台、SDK、板卡、模型和数据集重新验证。

## One-Liner

LeRobot CloudTwin 是 RobotMac Core 的云端训练工厂：把真实机器人 episode 变成 LeRobot 数据集，路由到中国或海外 GPU 训练，统一评测，再打包成带 lineage、runtime profile、rollback 和证据表的 Qualcomm edge policy。

## Problem

机器人团队能做 demo，但难把 demo 变成可交付技能：

- 数据格式散：视频、状态、动作、时间戳、操作者、任务标签、失败接管和安全事件常散在不同文件夹里。
- 训练云分裂：中国和海外面对不同账号、GPU、镜像、付款、网络、数据边界和支持渠道。
- 评测不可比：同一任务在不同云、不同 split、不同 seed 训练，输出结果很难被采购经理和工程负责人共同信任。
- 部署靠手工：模型权重不是产品交付物，还需要输入输出契约、runtime 依赖、硬件 profile、rollback 和运行证据。
- 失败没进入飞轮：部署失败、人工接管、低置信度和任务超时如果没有回流，就只是事故，不是下一轮训练资产。
- Qualcomm 价值没沉淀：如果每次训练结果只是“最终跑一下”，就无法把 Qualcomm edge 变成默认 deployment target。

## Why Now

- LeRobot 已经把真实机器人数据、模仿学习、HIL 数据采集、数据集格式和策略训练推到开发者可用层。
- LeRobotDataset v3 用 Parquet、video shards、metadata、tasks 和 episode 边界组织多模态时间序列。
- HIL 数据采集让人工接管和恢复动作成为下一轮训练数据。
- GPU 供给足够碎片化：RunPod、Lambda、Modal、阿里云 PAI、腾讯 GPU、华为 ModelArts、AutoDL 都能训练，但没有统一机器人 job contract。
- NVIDIA 的 Physical AI Data Factory、Google/DeepMind robot data、PI/Skild/Figure 等方向共同证明：机器人数据、策略训练、边缘部署和持续学习正在成为平台类别。
- Qualcomm 正在强调 prototype-to-production edge AI；CloudTwin 把云训练自然导向 Qualcomm edge 执行。

## Insight

机器人技能不是“下载一个模型”，而是像 SaaS release 一样发布：

> capture -> dataset -> train -> evaluate -> package -> profile -> deploy -> monitor -> rollback -> mine failures -> retrain。

真正可卖的不是 GPU 小时，也不是模型权重，而是每个任务的可验证学习循环：

- episode lineage。
- locked split。
- training job record。
- eval gate。
- Qualcomm edge profile。
- runtime evidence。
- rollback。
- failure mining。

## Solution

CloudTwin = `Dataset Ledger + TrainRouter + Eval Harness + Edge Policy Packager + Runtime Evidence + Failure Mining`。

输入：

- RobotMac Core / TeleopStudio 采集的多相机视频、状态、动作、接管、成功/失败标签和安全事件。

输出：

- Qualcomm edge policy package，包含模型、输入输出契约、数据集版本、评测报告、硬件 profile、依赖、rollback 包和运行证据模板。

CloudTwin 的清晰定位：

- 不是 another foundation model：ACT 起步，SmolVLA、X-VLA、π0、GR00T-style policy 以后可插拔。
- 不是 another GPU cloud：价值是 robot-aware job spec、metrics、safety bounds、budget guard、data boundary 和 edge deployment。
- 不是 another fleet dashboard：闭环只有在 policy 跑到 Qualcomm edge 并把失败 episode 回流之后才结束。

## Product Workflow

1. Capture：RobotMac Core / TeleopStudio 记录 video、state、action、timestamps、operator、robot profile、success/failure、human takeover。
2. Ledger：转成 LeRobot-compatible dataset，写入版本、hash、隐私级别、region、rights passport 和 task tags。
3. Route：TrainRouter 根据数据地域、预算、GPU class 和 provider availability 选择 China / Overseas / Auto lane。
4. Train：ACT 起步，扩展 Diffusion、SmolVLA、X-VLA；保存 config、seed、container digest、cost、logs 和 checkpoints。
5. Evaluate：输出 success rate、failure type、action smoothness、latency budget、replay examples 和 fixed split report。
6. Package：生成 Qualcomm edge package：policy hash、ONNX/QNN artifacts、runtime deps、rollback 和 manifest。
7. Profile：AI Hub / Device Cloud / Profiler 记录 latency、load time、memory、compute target、thermal 和 power。
8. Deploy：Skill package 进入 RobotCoreOS / SkillCertKit，在本体本地执行，不依赖云端实时控制。
9. Recover：坏模型、坏配置或安全 gate 失败触发 admission denial、safe mode 或 rollback。
10. Mine：失败片段、低置信度、接管和客户反馈进入下一轮训练队列和 regression test。

## China / Overseas Cloud Lanes

### China Lane

目标用户：

- 国内高校、工厂、系统集成商、开发者社区。
- 数据不适合出境的企业试点。
- 需要中文支持、国内付款和国内 GPU 区域的客户。

首批 adapter：

- Alibaba Cloud PAI。
- Tencent Cloud GPU。
- Huawei ModelArts。
- AutoDL。

### Overseas Lane

目标用户：

- 海外开发者、开源社区、国际机器人团队。
- 需要快速获取 A100/H100/4090 等 GPU 的实验团队。
- 需要和 Hugging Face / GitHub workflow 更紧密结合的团队。

首批 adapter：

- RunPod。
- Lambda。
- Modal。
- Paperspace / CoreWeave 作为后续候选。

## Market

第一批客户买的是“可交付训练闭环”，不是便宜 GPU：

- LeRobot developer / research lab：需要低摩擦 ACT、Diffusion、SmolVLA training from demos，购买 starter credits、templates、dataset conversion、eval reports。
- Robotics startup / OEM autonomy lead：有 prototype，但没有可靠 data/train/deploy loop，购买 dataset ledger、training job contracts、regression evals、model export 和 rollback packages。
- System integrator / pilot delivery team：卖 4-8 周 automation pilot，需要固定范围 “capture demos, train policy, deliver edge package”。
- Enterprise factory / warehouse innovation owner：关心 uptime、audit、data residency、ROI、budget guardrails、approved rollout 和 compliance reports。
- RaaS / fleet operator：购买 per-active-robot learning loops、failure mining、fleet replay、canary rollout、OTA updates 和 success dashboards。
- China domestic robotics team：需要中文 billing、low-latency access、data-local training、local support 和国内 GPU provider。

## Business Model

两段式收费：

- Platform fee。
- Metered compute pass-through。

Package dimensions：

- active robots。
- storage / TB。
- teleop seats。
- captured demo-hours。
- training jobs / concurrency。
- GPU class。
- private data lane。
- eval reports。
- edge export targets。
- support SLA。

收入层：

- Kit attach：随 RobotMac Core、TeleopStudio、教育套件或行业 demo kit 附带初始训练额度。
- CloudTwin SaaS：dataset ledger、training jobs、eval reports、edge export、private registry、policy lineage、rollout gates。
- GPU routing：GPU 成本透传，叠加 orchestration margin、budget guard、preemption handling、logs 和 artifact storage。
- Enterprise private lane：中国/海外私有 lane、SSO/RBAC、数据边界、审计报告、on-prem artifact registry 和 edge validation sprint。
- Skill marketplace：经验证 skill package 上架抽成，按 Qualcomm hardware profile 匹配。

## Go-To-Market

1. 比赛闭环：桌面机械臂 10-20 条 episode，ACT 小训练，eval，Qualcomm edge package，runtime evidence。
2. 教育课程：LeRobot-to-Qualcomm 课程包，做到第一天能跑、第一周能训练、第一月能部署。
3. SI 试点：pick/place、扫码、巡检、质检、lab transfer 做成 60-90 天 bounded-task pilot。
4. 企业私有 lane：数据地域、预算、审计、approved rollout 和 failure mining 进入企业采购语言。
5. Qualcomm ecosystem：争取 Dragonwing Robotics Hub tutorial、AI Hub workflow、board profile validation checklist。

## Competition

- LeRobot：开放机器人学习引擎。CloudTwin 是商业 job、数据边界、评测、edge packaging 和 release governance。
- Physical Intelligence / Skild / Figure：证明 generalist robot policy 和 VLA 方向。CloudTwin 不做另一家 foundation model，而做可插拔生产闭环。
- NVIDIA Isaac / GR00T / Omniverse / Isaac Lab / Jetson：强 physical AI 全栈和 GPU-first 叙事。CloudTwin 是 Qualcomm-first counter-position：双云训练、低功耗 edge、AI Hub/QNN packaging。
- Google / DeepMind robotics data：证明跨机器人数据、VLA reasoning、fleet-scale data collection 方向。CloudTwin 把这些思想做成比赛团队和中小机器人公司可用的控制面。
- Viam / Formant / InOrbit / Foxglove：强 fleet、teleop、ops、data observability。CloudTwin 聚焦 training/evaluation/deployment loop，并导出可运维 artifact。
- Cloud GPU providers：RunPod、Lambda、Modal、CoreWeave、Alibaba PAI、Huawei ModelArts、Tencent GPU 卖算力。CloudTwin 卖 robot-aware job spec、metrics、safety bounds、data boundary 和 edge export。
- Chinese robot learning / cloud ecosystems：AgiBot World、Unitree、Dataa/HARIX 等证明中国有数据、硬件、云和生态需求。CloudTwin 做 bilingual / dual-cloud / LeRobot-compatible / Qualcomm-edge bridge。

## Moat

- Episode ledger：成功、失败、接管、恢复、场景标签长期积累。
- Eval harness：同一 dataset split、同一指标、不同云训练结果可比较。
- Qualcomm board profile library：camera、IO、runtime、thermal、power、accelerator path 的验证矩阵。
- Skill compatibility graph：任务、模型、硬件、动作权限、安全 envelope、rollback 的关系网。
- Distribution moat：教育课程、SI 模板、企业私有 skill library、Qualcomm 开发者生态。

## Release Evidence

CloudTwin 的可 defend claim：

> LeRobot-compatible robot episodes can be turned into auditable policy releases, routed through China or overseas GPU lanes, evaluated against fixed gates, and packaged for Qualcomm edge deployment.

证据包：

- Episode schema：episode_id、dataset/version/hash、task、robot profile、sensor manifest、timestamps/clock source、camera shards、observation.state、action、autonomy mode、human takeover、success/failure、safety events、region、rights passport、hashes/signature。
- Dataset lineage：dataset card、source episode hashes、robot/site/operator role、collection date、transforms、redaction、QC rejects、dedupe、augmentation、license/use rights、retention、derived graph。
- Train/eval split：split_manifest.json，按 site/day/object/operator 分割，锁定 test split，记录 simulation/replay/physical eval。
- Policy artifact manifest：policy_id、parent policy、algorithm、LeRobot version、git commit、container digest、dataset split hashes、seeds、hyperparams、checkpoint hash、ONNX/QNN artifacts、eval report、rollback pointer。
- Cloud GPU job record：provider、lane、region、GPU SKU、image digest、command、start/end time、budget cap、logs hash、checkpoint hash、preemption notes、cost estimate。
- Reproducibility：runbook、lockfile、container digest、seed list、dataset hash、eval script hash；re-run metrics within tolerance。
- Safety/admission gates：rights、privacy/redaction、dataset QC、split-lock、eval threshold、edge-profile、numerical validation、safety-boundary sim、human approval、signed rollback。
- QNN/QAIRT/ONNX packaging：ONNX export、optional QNN ONNX folder、QNN context/DLC where applicable、QAIRT/QNN version、target device、backend、input shapes、quantization/calibration、AI Hub job IDs。
- Edge evaluation：p50/p95/p99 latency、action rate、jitter、CPU/GPU/NPU utilization、memory、temperature、power、dropped frames、safety triggers、manual takeovers、success rate、rollback result。
- Metric labels：simulated、replay-eval、measured-on-device，不能混成一个数字。

## Why Qualcomm

云负责训练，Qualcomm edge 负责执行。

机器人 policy 需要 GPU training，但部署后的机器人需要：

- local inference。
- camera / sensor sync。
- low latency。
- offline resilience。
- privacy。
- measurable runtime behavior。

CloudTwin 让 Qualcomm 拥有 post-training deployment standard，而不只是“机器人里的那块板”：

- AI Hub Workbench：把 PyTorch/ONNX policy artifact 转成可 compile/profile/validate/deploy 的 Qualcomm runtime candidate。
- QNN / QAIRT：定义 target runtime、input shape、backend、quantization、calibration、context/DLC/ONNX Runtime QNN route。
- Device Cloud：hosted Qualcomm targets 用于 policy artifact validation。
- Qualcomm Profiler：定义 latency、load time、memory、CPU/GPU/NPU/DSP utilization、thermal、power evidence table。
- Qualcomm Linux：camera ingest、video/audio pipeline、ROS 2-friendly runtime、OTA/rollback packaging。
- Dragonwing Robotics Hub：发布 “LeRobot CloudTwin: teleop to Qualcomm edge deployment” sample。

## Demo Storyboard

三分钟 demo：

1. Record：Teleop 采集 10-20 条 episode，记录 camera、state、action、timestamps、success/failure 和 takeover。
2. Train：CloudTwin 生成 dataset card，提交 China / Overseas training job，展示 cost、logs、config、checkpoint。
3. Evaluate：Eval report 展示 split、success rate、failure type、replay clips 和 release gate。
4. Deploy：导出 Qualcomm edge package，包含 policy hash、target hardware、AI Hub/QNN status、rollback package。
5. Run local：机器人本体执行策略，云端断开 safety/control loop。
6. Improve：触发一次失败或接管，失败片段进入下一轮 training queue。

画面必须出现 evidence table：

- dataset version。
- policy hash。
- target hardware。
- latency target/measured。
- success rate。
- safety event。
- rollback package。
- metric label: simulated / replay-eval / measured-on-device。

## Ask

请求 Qualcomm 支持 6-8 周 CloudTwin validation sprint：

- Hardware path：RB3 Gen 2 Vision Kit、QCS6490、QCS8550、IQ-8275 / IQ10 guidance。
- AI Hub / QNN guidance：ACT-class policy export、fixed input shapes、quantization、QNN DLC vs context binary vs ONNX Runtime QNN。
- Device Cloud access：hosted Qualcomm targets 用于 policy artifact validation。
- Profiler support：官方 evidence table，覆盖 latency、load time、memory、utilization、thermal、power。
- Qualcomm Linux / IM SDK help：camera ingest、video/audio pipeline、ROS 2-friendly runtime、OTA/rollback packaging。
- Robotics Hub support：发布 “LeRobot CloudTwin: teleop to Qualcomm edge deployment” sample。
- Mentor review：robotics edge architect + AI Hub engineer + APLUX / Thundercomm / Advantech-style partner intro。

## Claim Boundaries

可以说：

- LeRobot-compatible。
- Qualcomm-first。
- dual-cloud training architecture。
- edge evidence workflow。
- auditable policy release workflow。

不能说：

- 已获 Qualcomm / LeRobot 官方认证、合作、投资或 endorsement。
- 自动合规。
- SOC 2 / ISO certification。
- functional safety certification。
- 任意 LeRobot / PyTorch / VLA policy 自动跑 QNN。
- AI Hub profile 等于全机器人 end-to-end latency。
- 性能优于 Jetson / x86。
- 云端可以替代本地 safety control。

所有 TOPS、延迟、功耗、温度、FPS、成功率必须注明日期、板卡、SDK、散热、电源、模型版本和 metric label。

## Sources

- LeRobot docs：https://huggingface.co/docs/lerobot/en/index
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot HIL data collection：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobot GitHub：https://github.com/huggingface/lerobot
- SmolVLA：https://huggingface.co/blog/smolvla
- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/news/service-robots-see-global-growth-boom
- RunPod pricing：https://www.runpod.io/pricing
- Lambda instances：https://lambda.ai/instances
- Modal pricing：https://modal.com/pricing
- Alibaba PAI：https://www.alibabacloud.com/product/machine-learning
- Tencent GPU：https://www.tencentcloud.com/product/gpu
- Huawei ModelArts：https://www.huaweicloud.com/intl/en-us/product/modelarts.html
- AutoDL GPU docs：https://www.autodl.com/docs/gpu/
- NVIDIA Isaac：https://developer.nvidia.com/isaac
- NVIDIA Physical AI Data Factory：https://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development
- Physical Intelligence pi0.7：https://www.pi.website/blog/pi07
- Skild AI：https://www.skild.ai/blogs/building-the-general-purpose-robotic-brain
- Figure BMW production：https://www.figure.ai/news/production-at-bmw
- Gemini Robotics：https://deepmind.google/models/gemini-robotics/
- Viam platform：https://www.viam.com/platform/overview
- Formant teleoperation：https://docs.formant.io/docs/getting-started-teleoperation
- Foxglove：https://foxglove.dev/
- Qualcomm AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- AI Hub compile examples：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm Device Cloud：https://qdc.qualcomm.com/support/user-guide/overview
- Qualcomm Profiler：https://www.qualcomm.com/developer/software/qualcomm-profiler
- Qualcomm Linux：https://www.qualcomm.com/developer/software/qualcomm-linux
- Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Qualcomm prototype-to-deployment ecosystem：https://www.qualcomm.com/developer/blog/2026/05/edge-ai-prototype-deployment-qualcomm-dragonwing-developer-ecosystem
