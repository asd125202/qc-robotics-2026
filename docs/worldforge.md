# WorldForge Pitch

更新时间：2026-07-05。机器人基础模型、仿真平台、云 GPU 与 Qualcomm edge 工具链变化很快，真实交付前需要按目标硬件、仿真后端和客户数据边界重新验证。

## Core Thesis

WorldForge 是 RobotMac / LeRobot / Qualcomm 体系里的机器人技能工厂：

> real demos -> synthetic variants -> simulation CI -> LeRobot dataset -> cloud training -> Qualcomm edge validation -> field feedback。

它不替代 Isaac、MuJoCo、Gazebo 或 Genesis，而是在这些工具之上做 orchestration、dataset factory、failure mining、evaluation harness 和 Qualcomm deployment gate。

核心主张：

- 仿真不是目的，规模化可验证机器人数据工厂才是产品。
- 具身智能的瓶颈正在从“有没有大模型”转向“有没有可规模化的数据闭环”。
- 从 demo 到 deployment，需要合成数据、失败样本、回归评测、延迟 / 功耗验证和真实部署反馈。
- WorldForge 不和 GR00T、Gemini Robotics、pi0、Helix 竞争，而是做它们都需要的数据、评测和端侧部署中间层。

## Five-Thread Research Synthesis

### 1. Foundation Model Trend

NVIDIA GR00T / Cosmos / Isaac、Google Gemini Robotics、Physical Intelligence OpenPI、Skild AI、Covariant RFM、Figure Helix 都在说明同一件事：机器人智能正在从单个 demo 进入数据飞轮、合成数据、评测和端侧部署阶段。

可以安全表达的判断：

- Physical AI 正在变成 data factory problem。
- Foundation policy 仍然需要 post-training、failure replay、human correction 和 deployment regression tests。
- 仓储机器人已经证明 RFM / VLA 类模型可以进入商业部署，通用机器人会沿用同样的数据与评测逻辑。

### 2. Simulation Backend Trend

WorldForge 应该做 simulator-agnostic orchestration：

- Isaac Sim / Isaac Lab / Replicator：高保真视觉、传感器、USD 资产、合成标注和轨迹扩增。
- MuJoCo / MJX / Warp：快速动力学、RL、system identification 和便宜 rollout。
- Gazebo / ROS 2：SDF、Nav2、ROS 生态和客户已有工程兼容。
- Genesis：作为新兴多物理仿真和高速 rollout 的实验后端。
- robosuite / RoboCasa / RoboVerse：作为 task pack、benchmark pack 和 research-to-product 桥接层。

产品边界：WorldForge 不需要重新做一个物理引擎，而是把 CAD / URDF / ROS bag / real demo 变成多后端可运行场景，并输出 LeRobot-compatible dataset、evaluation score 和 deployment report。

### 3. Data Flywheel Trend

LeRobot 已经形成了适合开源生态的 rails：数据集、policy、teleoperation、HIL correction、benchmark integration 和 Hugging Face Hub 工作流。

WorldForge 应该围绕 `LeRobotDataset` 做：

- video / image stream。
- robot state / action。
- language instruction。
- object and scene metadata。
- sim parameters。
- intervention flag。
- failure taxonomy。
- train / validation split。
- provenance and calibration report。

### 4. Business Landscape

客户痛点非常具体：

- 真实机器人数据采集慢、贵、脏、难复现。
- sim-to-real gap、接触 / 摩擦 / 传感器噪声、端侧延迟会杀死试点。
- 团队必须把 CAD、URDF、ROS 2、相机 / LiDAR 数据、ML training、fleet update 和安全验证缝在一起。
- 仓库、工厂、实验室愿意为更快切换 SKU / protocol / station、减少失败安装和降低机器人专家依赖付费。

商业包装：

- Developer tier：小型任务包、公开 benchmark 和本地导出。
- Team Studio：数据版本、仿真任务、云训练、LeRobot export。
- Vertical Pack：new SKU pack、lab workflow pack、AMR route-risk pack、factory inspection pack。
- Qualcomm Edge Readiness Report：AI Hub / QNN / ONNX / real-board validation。
- Enterprise / On-prem：私有资产库、私有仿真、审计、SLA 和系统集成支持。

### 5. Qualcomm Cloud-Edge Trend

WorldForge 必须把 Qualcomm 价值写进工作流，而不是只在项目书里提硬件：

```text
PyTorch checkpoint
  -> ONNX / static-shape export
  -> quantization / calibration
  -> Qualcomm AI Hub compile and profile
  -> QNN / QAIRT / TFLite / ONNX Runtime target
  -> RB3 / QCS6490 / QCS8550 / IQ10 validation
  -> signed policy bundle and rollback
```

关键约束：

- 当前原型可以以 RB3 Gen 2 / QCS6490 / QCS8550 为目标。
- 长期故事必须指向 Dragonwing IQ10 robotics reference design。
- 端侧策略需要 static tensor contract、量化校准、真实板端验证和 ROS 2 loop timing。
- 云端负责大规模仿真、训练和失败挖掘；本体负责低延迟感知、短时域策略、安全边界和离线可靠性。

## Product Architecture

### 1. Ingest

- CAD / URDF / MJCF / SDF / USD assets。
- ROS bag / camera / LiDAR / robot state。
- Teleop demo。
- HIL takeover。
- Field failure clip。
- Enterprise task context from OpsConnector。

### 2. Forge

- Real-to-sim calibration。
- Task and scenario generation。
- Object / lighting / friction / clutter / camera perturbation。
- Demo expansion from few real trajectories。
- Synthetic labels: RGB, depth, segmentation, pose, trajectory, success/failure。

### 3. Validate

- Standard benchmark: LIBERO, Meta-World, Isaac Lab Arena, robosuite task pack。
- Vertical benchmark: warehouse bin-pick, lab sample transfer, factory inspection, AMR route-risk。
- Stress tests: occlusion, slip, bad lighting, object variation, delayed action, dropped frames。
- Promotion gates: success rate, intervention rate, failure recurrence, cycle time, collision / near-miss, edge latency。

### 4. Train

- LeRobot-compatible datasets。
- ACT / diffusion policy / SmolVLA / pi0-style fine-tuning。
- China and overseas cloud GPU lanes through TrainRouter。
- Dataset provenance and model card。

### 5. Deploy

- Qualcomm AI Hub profile and compile。
- QNN / ONNX / TFLite edge artifact。
- RobotCoreOS runtime package。
- SafetyOps release gate。
- EdgeFleet canary and monitoring。

## Competition Demo

最强 demo 是“1 条真实示教变成 1000 条可验证训练样本”：

1. 用 TeleopStudio 录制一个桌面机械臂样品转移 demo。
2. WorldForge 生成位置、光照、容器、遮挡、摩擦和相机角度变体。
3. 仿真 CI 找出 policy 在 slip / occlusion / wrong-object 场景下的失败点。
4. Failure Factory 自动聚类失败片段，让操作者补一条 recovery demo。
5. TrainRouter 触发云 GPU 训练。
6. EdgeRuntimeBench 把策略导出为 Qualcomm edge artifact。
7. SafetyOps 和 EdgeFleet 只允许通过门禁的版本进入 canary。

这比单纯展示仿真更有说服力，因为它回答了企业客户最关心的问题：一个新任务、新 SKU、新 protocol 如何低成本、安全地变成可上线机器人技能？

## Why Qualcomm Should Care

WorldForge 给 Qualcomm 一个对抗 NVIDIA 生态锁定的切入点：

- NVIDIA 已经把 Isaac、Omniverse、Cosmos、GR00T 和 Jetson 串成 physical AI stack。
- Qualcomm 的机会不是复制 Isaac，而是成为 cloud-trained robot policy 的低功耗 edge deployment lane。
- WorldForge 把每个模拟场景都变成 Qualcomm 的 benchmark、优化目标、销售证据和开发者工作流。
- 如果每个技能都必须通过 Qualcomm edge readiness report，Qualcomm 就进入机器人技能分发和企业验收链路。

一句话：

> WorldForge turns Qualcomm robotics hardware into a deployable physical-AI platform with data, tests, and vertical apps。

## Sources

- NVIDIA Isaac GR00T：https://developer.nvidia.com/isaac/gr00t
- NVIDIA GR00T-Dreams：https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/
- NVIDIA Isaac Sim：https://developer.nvidia.com/isaac/sim
- Isaac Sim docs：https://docs.isaacsim.omniverse.nvidia.com/latest/index.html
- Isaac Lab docs：https://isaac-sim.github.io/IsaacLab/main/index.html
- Hugging Face LeRobot：https://huggingface.co/docs/lerobot/en/index
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot HIL data collection：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobot v0.5：https://huggingface.co/blog/lerobot-release-v050
- Open X-Embodiment：https://robotics-transformer-x.github.io/
- DROID dataset：https://droid-dataset.github.io/
- MuJoCo：https://mujoco.readthedocs.io/en/latest/
- MuJoCo Playground：https://playground.mujoco.org/
- Gazebo releases：https://gazebosim.org/docs/latest/releases/
- Genesis World：https://genesis-world.readthedocs.io/
- RoboVerse：https://roboverseorg.github.io/
- Physical Intelligence OpenPI：https://github.com/Physical-Intelligence/openpi
- Skild AI Series C：https://www.skild.ai/blogs/series-c
- Amazon and Covariant robotics AI agreement：https://www.aboutamazon.com/news/company-news/amazon-covariant-ai-robots
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- Dragonwing IQ10 robotics reference design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
