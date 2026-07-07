# DragonWorks Pitch

更新时间：2026-07-07。本页按 YC / Airbnb 风格重写：问题、现有替代方案为什么失败、解决方案、为什么现在、产品、API/证据、市场、竞争壁垒、为什么 Qualcomm、演示和请求。

## One-Line Pitch

DragonWorks 是面向 Dragonwing 机器人的开发者工作台和部署 API：把 ROS 2、传感器、LeRobot episode、双云训练、AI Hub / QAIRT / QNN profile、Dragonwing runtime、SkillCertKit 门禁、SkillDock 发布和 EdgeFleet 现场证据打包成一条从 demo 到量产的机器人生产流水线。

## Thesis

机器人硬件和 AI 模型都在爆发，但商业化瓶颈正在转移：

> 样机越来越快，量产越来越难。

机器人团队今天不是缺芯片、缺 ROS、缺模型、缺云 GPU，而是缺一条稳定的工程路径：从真实机器人数据到训练，从训练到 Qualcomm edge profile，从 profile 到可安装技能，从安装到现场证据，从现场失败回到下一轮训练。

DragonWorks 的定位不是“又一个机器人操作系统”，而是：

> Dragonwing production layer for robot teams: build, optimize, deploy, observe.

## 01 · Problem

机器人开发今天被切成四段：

1. ROS / 仿真 / 硬件 bring-up。
2. 遥操作数据、LeRobot dataset、训练和评估。
3. 边缘部署、AI Hub、QAIRT / QNN、runtime、thermal / power / camera profile。
4. 现场发布、日志、事故复盘、回滚、质保和比赛/客户材料。

每一段都有工具，但跨段交付靠人工胶水。结果是：

- demo 能跑，但团队说不清模型来自哪份数据、哪个训练 job、哪个代码 commit。
- 训练结果不错，但没有绑定 Dragonwing board、runtime、input shape、NPU backend、thermal 和 camera health。
- ROS bag 和 LeRobot dataset 分开存，原始现场行为和训练样本无法追溯。
- release 是一个权重文件或 Docker image，不是带 evidence、rollback、SBOM、权限和安全边界的技能包。
- 比赛提交、客户投标、售后复盘靠手工截图和视频拼装，无法证明可复现。

一句话：机器人团队能做样机，但缺少把样机变成可部署、可维护、可证明产品的路径。

## 02 · Current Alternatives Fail

现有工具都很强，但它们各自解决一段问题，没有把 Qualcomm / Dragonwing 生态里的端到端产品化串起来。

### ROS / Gazebo / Nav2 / MoveIt

开放基础层足够重要，但不是商业交付层。ROS 帮团队构建机器人应用，Gazebo / Isaac / MuJoCo 帮团队仿真，Nav2 / MoveIt 解决导航和运动规划；它们不会自动生成 Dragonwing profile、QNN artifact、SkillCertKit gate、EdgeFleet incident capsule 或客户提交包。

### NVIDIA Isaac

Isaac / Omniverse / GR00T / Isaac Lab 是 GPU-first robotics stack，仿真、synthetic data、robot learning 和 Jetson 路径很强。对 Qualcomm 来说，正确反应不是“复制 Isaac”，而是建立 Dragonwing 上从开发到部署的最短路径。

### Edge ML / Model Tools

Edge Impulse、AI Hub、ONNX Runtime、TensorRT、AIMET、QNN 等能处理模型训练、转换、优化或推理，但 robot skill 不是一个孤立模型。真实交付还需要 ROS topic、传感器时序、地图、动作边界、远程协助、版本、回滚和现场证据。

### RobOps / FleetOps

Formant、InOrbit、Foxglove、Viam、Boston Dynamics Orbit、OEM fleet cloud 都证明 fleet ops 有预算。问题是它们通常从“运行中的机器人”开始，而不是从 LeRobot 数据、AI Hub profile、Dragonwing target、技能门禁和开发者提交路径开始。

### OEM 自研

OEM 自研最可控，但每家公司都在重复造 dashboard、VPN、OTA、日志、teleop、训练数据、客户报告和售后证据。它无法形成 Dragonwing developer network effect。

DragonWorks 的切口是：不替代这些工具，而是把它们组织成 Qualcomm-first release graph。

## 03 · Solution

DragonWorks = Dragonwing 机器人的 `build -> optimize -> deploy -> observe -> improve` 控制平面。

开发者上传 ROS 2 package、模型、传感器配置和 LeRobot dataset；DragonWorks 生成 Dragonwing target profile、训练 job、AI Hub / QNN evidence、runtime package、skill release、fleet rollout 和 submission packet。

核心链路：

```text
Robot Workspace
  -> Episode Capture
  -> Dataset Registry
  -> TrainRouter
  -> Qualcomm Edge Profile
  -> SkillCertKit Gate
  -> SkillDock Release
  -> EdgeFleet Evidence
  -> Submission Builder
```

三件事让它不像普通 dashboard：

1. **Lineage-first**：每个模型都能追到 episode、ROS bag、dataset split、训练环境、checkpoint、profile、artifact、runtime、robot、site 和 incident。
2. **Qualcomm-first**：项目从创建时就选择 RB3 / QCS6490 / QCS8550 / IQ / Dragonwing target，而不是最后才想部署硬件。
3. **Production-first**：release 不是“跑通一次”，而是有 evidence、gate、rollback、known limitations、support boundary 和 field feedback。

## 04 · Why Now

2026 是 Qualcomm 做机器人开发平台的窗口期，因为四件事同时发生：

### 4.1 Dragonwing 正在变成 robotics / industrial edge 品牌

Qualcomm 已经把 Dragonwing 用在 industrial / embedded IoT、edge AI、connectivity 和 robotics 叙事中。Dragonwing Robotics Hub 也在把开发者入口放到 Arduino Project Hub，目标是让开发者更快做出 working demos。

### 4.2 AI Hub / QAIRT / QNN 已经像产品流水线

AI Hub Workbench 支持 compile、profile、inference 和 deployment 路径；QAIRT / QNN context binary、QNN DLC、ONNX Runtime QNN EP 让 DragonWorks 可以把模型从 cloud training 送到具体 Dragonwing device profile。

### 4.3 LeRobot 正在把真实机器人数据标准化

LeRobotDataset v3 把多相机视频、state/action、metadata、indexing、Hub visualization 和 episode workflow 变成标准资产。LeRobot v0.6 又强化了 eval、rollout、VLM annotation、HF Jobs training 和 failure-to-training-data loop。

### 4.4 机器人商业化从 demo 转向 fleet learning

IFR 2025 显示 2024 年全球工业机器人新增安装约 542,000 台，中国占 54%；专业服务机器人销量接近 200,000 台，RaaS fleet 增长 31%。市场正在从“能不能动”走向“能不能部署、运营、复盘、续费”。

机会不是再做一个机器人 demo，而是做 Qualcomm 机器人生态的生产流水线。

## 05 · Product

DragonWorks 应该像开发者每天打开的工作台，而不是比赛 PPT。

### 5.1 Workspace

- 项目、机器人形态、target board、ROS 2 graph、camera、actuator、calibration、runtime、container、launch profile。
- 支持 sim / lab / field 三种 target。
- 第一版聚焦两个 archetype：AMR / inspection 和视觉抓取，不声称支持所有机器人。

### 5.2 Episode Capture Studio

- 从 ROS 2 / rosbag2 / TeleopStudio 采集原始证据。
- 同步相机、state、action、operator note、failure tag、network / FPS / latency。
- 输出 LeRobot-compatible dataset 和 raw evidence pointer。

### 5.3 Dataset Registry

- LeRobotDataset viewer、metadata search、quality score、train/val/test split、rights、region、redaction、lineage。
- 连接 CloudTwin / TrainRouter，用于 sim eval、real eval 和 retraining queue。

### 5.4 Training Orchestrator

- LeRobot config、policy family、seed、dataset version、GPU lane、budget guard、checkpoint comparison。
- 中国版走阿里云 / 腾讯云 / 华为云 / 百度智能云 / 火山引擎等内地区域；全球版走 AWS / GCP / Azure / CoreWeave / Lambda / RunPod 等。

### 5.5 Qualcomm Optimizer

- 调用 AI Hub Workbench / QAIRT / QNN / ONNX Runtime QNN path。
- 生成 latency、memory、NPU/backend、thermal、power、camera pipeline、unsupported ops、fallback evidence。
- 支持 `qnn_context_binary`、`qnn_dlc`、ONNX Runtime QNN EP 等 artifact strategy。

### 5.6 Runtime + Fleet Evidence

- Dragonwing device agent 记录 artifact hash、runtime、camera health、thermal zone、power mode、latency、FPS、dropped frames。
- 接入 SkillCertKit / SkillDock / EdgeFleet，形成 install audit、staged rollout、incident capsule、rollback 和 failure-to-training loop。

### 5.7 Submission Builder

- 自动导出比赛/客户需要的 evidence table、BOM、architecture、demo storyboard、source links、screenshots、metrics、claim boundaries。

## 06 · Product API/Evidence

DragonWorks 必须让评委相信它不是概念页，而是可被开发者调用的产品。

### CLI

```bash
dragonworks init --template amr-inspection --target rb3-gen2
dragonworks capture --robot lab-amr-01 --format lerobot+rosbag2
dragonworks train --lane china --provider aliyun --budget 800rmb
dragonworks profile --target qcs6490 --runtime qnn-context-binary
dragonworks release --skill inspect-pallet-v4 --gate skillcert --rollout lab
dragonworks export-submission --competition qc-robotics-2026
```

### API Objects

```json
{
  "release_id": "dw_rel_2026_07_07_001",
  "target": "dragonwing-rb3-gen2-qcs6490",
  "dataset": "lerobot://warehouse-inspection/v12",
  "ros_bag": "mcap://capture/lab-amr-01/episode-8842",
  "train_job": "trainrouter://china/aliyun/job-92811",
  "artifact": {
    "onnx_hash": "sha256:...",
    "qnn_context_hash": "sha256:...",
    "runtime": "QAIRT/QNN",
    "ai_hub_profile_job": "profile://..."
  },
  "gate": {
    "skillcert": "allow_with_limits",
    "known_limits": ["indoor-only", "human-supervised-rollout"],
    "rollback": "dw_rel_previous_known_good"
  }
}
```

### Evidence Packet

- `robot_workspace.json`
- `device-registry.json`
- `sensor-calibration.json`
- `rosbag_manifest.json`
- `lerobot_dataset_card.json`
- `split_manifest.json`
- `training_run_card.json`
- `eval_report.json`
- `qualcomm_profile.json`
- `qnn_artifact_manifest.json`
- `skillcert_policy_decision.json`
- `release_record.json`
- `edgefleet_incident_links.json`
- `submission_packet.json`

### Pilot Metrics

必须用真实 pilot 验证，不能空喊：

- 手工集成从 3-6 周降到 1-3 天。
- 每个 release 100% 记录 dataset、checkpoint、artifact、target、runtime、gate、rollback。
- RB3 / QCS6490 或 IQ10 RRD 目标上完成至少 5 个模型/任务 benchmark。
- 现场失败能在 24 小时内变成可复盘 clip、标签、regression case 和 retraining candidate。

## 07 · Market & Business Model

DragonWorks 的第一批买家不是“整个机器人行业”，而是正在把 10-1,000 台机器人部署到客户现场的团队：

- 中国机器人 OEM 出海团队。
- 使用 Dragonwing / RB / QCS / IQ 的开发者、SI、教育和实验室团队。
- AMR、视觉巡检、服务机器人、仓储机器人、安防巡逻、工业视觉团队。
- RaaS operator 和需要 uptime / warranty evidence 的 fleet owner。

### China Version

- `dragonworks.cn`：内地部署、内地数据库、内地对象存储、内地日志、内地 identity、内地模型/GPU lane。
- 数据策略：机器人视频、facility map、operator log、客户遥测默认留在中国。
- 云策略：阿里云 / 腾讯云 做通用 POC，华为云 / 百度 / 火山引擎用于国产算力、政企或模型生态需求。
- 商业模式：pilot fee + 年费 + 每机器人/月 + 训练/仿真 credits + 私有部署/集成费。

### Global Version

- `dragonworks.ai`：海外控制平面，AWS / GCP / Azure 用于企业采购和 SLA，CoreWeave / Lambda / RunPod 等用于弹性训练和仿真。
- 训练云和生产控制云分离，GPU 短缺不能影响机器人现场运行。
- 商业模式：developer free tier、team SaaS、enterprise/OEM per-device runtime license、support package、reference design integration。

### Bottom-Up Revenue Logic

早期不要讲“拿 1% TAM”。更可信的讲法：

- 10 个 design partners。
- 每个 partner 10-100 台机器人。
- 每台机器人每月软件/证据/运行授权。
- 额外按 training / simulation / validation / private deployment 收费。
- Qualcomm 战略价值来自更高 Dragonwing attach rate、更短 design-win 到 production 周期和开发者粘性。

## 08 · Competition & Moat

DragonWorks 不靠“功能最多”赢，而靠 Qualcomm-specific integration 和 release evidence graph 赢。

### Competition Map

- ROS / Gazebo / Nav2 / MoveIt：开放机器人基础层。
- NVIDIA Isaac / GR00T / Isaac Lab：GPU-first simulation、synthetic data、robot learning stack。
- Intrinsic Flowstate：工业 workcell、behavior trees、skills 和 sim-to-real。
- Edge Impulse：edge ML training / optimization / deployment pipeline。
- LeRobot：open robot learning datasets、policies、training、evaluation。
- Foxglove：robotics data management、MCAP、visualization、logs。
- Formant / InOrbit / Viam / Orbit：fleet ops、teleop、monitoring、data、robot app/fleet platform。
- OEM clouds：品牌内设备管理、任务调度、售后和客户看板。

### Moat

短期：

- RB3 / QCS6490 / QCS8550 / IQ / Dragonwing target templates。
- AI Hub / QAIRT / QNN workflow recipes。
- ROS 2 + LeRobot + Qualcomm edge evidence 的项目模板。

中期：

- release evidence graph：episode、rosbag、dataset、job、checkpoint、QNN artifact、skill gate、install、incident、rollback 形成查询关系。
- benchmark corpus：同一机器人任务在不同 target、runtime、model shape、camera pipeline 上的真实性能数据。
- dual-cloud architecture：China / global 两套合规数据路径，代码同源、数据隔离、key/log/identity 分离。

长期：

- developer distribution：Dragonwing Robotics Hub、Arduino Project Hub、SkillDock、SI/OEM templates、education kits 和 competition submissions 互相强化。
- field feedback：真实 deployment data 反哺 Qualcomm target profile、tooling、reference designs 和开发者教程。

## 09 · Why Qualcomm

DragonWorks 是 Qualcomm 该支持的生态层，因为它把 Qualcomm 从“一个硬件选择”变成“机器人开发默认路径”。

Qualcomm 已经有：

- Dragonwing robotics / industrial edge portfolio。
- RB3 Gen 2、QCS6490、QCS8550、IQ-8275 / IQ-9075 / IQ10 等 robotics-relevant device path。
- AI Hub Workbench、QAIRT / QNN、ONNX Runtime QNN EP、Device Cloud profile 路径。
- IM SDK、camera/video/audio stream integration、connectivity、Wi-Fi / 5G、edge AI 和 low-power compute。
- Dragonwing Robotics Hub 和 Arduino Project Hub developer entry。

DragonWorks 补上的层：

- 从项目创建开始选择 Dragonwing target。
- 从数据采集开始记录 sensor / board / runtime / region。
- 从训练开始绑定 Qualcomm profile constraints。
- 从 release 开始要求 AI Hub / QNN evidence。
- 从现场开始把 EdgeFleet failure data 回流到下一轮训练。

请求 Qualcomm 支持不是一句“战略支持”，而是一次 90 天 validation sprint。

## 10 · Demo & Ask

### 90-Day Demo

目标：用 RB3 Gen 2 / QCS6490 作为第一目标，如果能拿到 IQ10 RRD 则作为 premium target。

演示两个 reference workflows：

1. AMR / warehouse inspection：ROS 2 navigation + camera perception + LeRobot failure clips + QNN profile + staged rollout。
2. Vision grasping / tabletop manipulation：TeleopStudio episode + LeRobot training + sim/real eval + SkillCertKit gate + SkillDock release。

7 分钟演示：

1. 创建 DragonWorks 项目，选择 `rb3-gen2` target、camera、actuator、task template。
2. 连接 ROS 2 robot，采集 rosbag2 + LeRobot episode。
3. 在 TrainRouter 选择 China / Global GPU lane，生成 training run card。
4. 通过 AI Hub / QAIRT / QNN profile，显示 latency、memory、backend、thermal、camera evidence。
5. SkillCertKit 阻止不兼容 release，允许带限制的 Dragonwing target release。
6. SkillDock 生成 skill card，EdgeFleet 做 lab rollout 和 rollback pointer。
7. Submission Builder 导出比赛项目书、evidence table、BOM、代码步骤和三分钟答辩 storyboard。

### Qualcomm Ask

- Hardware：RB3 Gen 2 Vision Kit / QCS6490，QCS8550-class kit，IQ10 RRD access or guidance。
- Tooling：AI Hub Workbench quota、Device Cloud profile access、QAIRT / QNN workflow office hours。
- Engineering：每周 review unsupported ops、input shape、quantization、NPU fallback、camera pipeline、thermal/power evidence。
- Ecosystem：Dragonwing Robotics Hub / Arduino Project Hub publishing path，MassRobotics / SI / OEM introductions。
- Validation：10 个 design partners，至少 3 个 LOI / paid pilot，明确 KPI：部署时间、性能、功耗、现场故障率、incident-to-training-loop。

### Claim Boundaries

可以说：

- Qualcomm-first robotics workbench concept。
- LeRobot-compatible workflow。
- AI Hub / QAIRT / QNN-ready evidence path。
- Dragonwing target profile and release graph。
- pilot developer platform / validation sprint。

不能说：

- official Qualcomm product。
- Qualcomm certification / endorsement。
- production-ready universal robot OS。
- replaces ROS / LeRobot / Isaac / Viam / Formant / Foxglove。
- all models compile to QNN without changes。
- measured power / latency / uptime unless来自真实设备或 Device Cloud profile。

## Sources

- Qualcomm Dragonwing：https://www.qualcomm.com/dragonwing
- Qualcomm Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Qualcomm AI Hub：https://aihub.qualcomm.com/get-started
- AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- AI Hub profile examples：https://workbench.aihub.qualcomm.com/docs/hub/profile_examples.html
- AI Hub compile examples：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- AI Hub deployment：https://workbench.aihub.qualcomm.com/docs/hub/deployment.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- LeRobot v0.6：https://huggingface.co/blog/lerobot-release-v060
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- ROS 2 Jazzy：https://discourse.openrobotics.org/t/ros-2-jazzy-jalisco-released/37862
- rosbag2：https://github.com/ros2/rosbag2
- NVIDIA Isaac：https://developer.nvidia.com/isaac/sim
- NVIDIA Isaac Lab：https://developer.nvidia.com/isaac/lab
- Intrinsic Flowstate：https://www.intrinsic.ai/flowstate
- Viam：https://docs.viam.com/what-is-viam/
- Foxglove：https://foxglove.dev/
- Formant：https://docs.formant.io/docs/fleet-observability
- InOrbit：https://www.inorbit.ai/overview
- IFR 2025 industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR 2025 service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Cloudflare ICP overview：https://developers.cloudflare.com/china-network/concepts/icp/
