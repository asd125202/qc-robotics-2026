# EdgeFleet Pitch

更新时间：2026-07-06。机器人 fleet ops、LeRobot 数据结构、Qualcomm AI Hub/QNN、Dragonwing reference designs、中国数据合规和机器人市场数据都变化很快；正式提交前需要复核来源、SDK、板卡、价格和部署边界。

## One-Line Pitch

EdgeFleet 是 Qualcomm-powered robots 的 fleet evidence control plane：

> 把 LeRobot 数据、AI Hub/QNN 产物、Dragonwing 设备、灰度发布、远程协助、事故回放和训练回流串成一条可运营、可回滚、可审计的队列证据链。

它不是又一个普通机器人看板。它解决的是机器人商业化进入客户现场之后最难回答的问题：

- 哪台机器人在运行哪个模型、哪个技能、哪个 QNN artifact、哪个 OS image。
- 这次失败来自传感器、模型、网络、现场、任务配置还是操作员。
- 更新后能否灰度、暂停、回滚和复盘。
- 远程协助是否有权限、TTL、命令边界、本体 safety gate 和审计日志。
- 现场失败片段能否回流到下一轮 LeRobot / TrainRouter 训练。

## Why Now

机器人正在从 demo 进入队列运营阶段：

- IFR 2025：2024 年全球工业机器人新增安装约 542,000 台，连续第四年超过 500,000 台；中国占全球新增部署约 54%。
- IFR 2025：专业服务机器人 2024 年销量接近 200,000 台，RaaS fleet 增长 31%，运输物流机器人是最大类别。
- LeRobot Dataset v3.0 已把多模态时间序列、sensorimotor signals、多相机视频和 metadata 做成标准格式。
- Qualcomm AI Hub Workbench 已提供 compile/profile/run inference 等工作流，profile job 可以回答 latency、memory、NPU leverage 等部署问题。
- Dragonwing / RB / QCS / IQ 路线正在把 Qualcomm 边缘 AI 从开发板叙事推向机器人生产部署叙事。

## Product Thesis

EdgeFleet 站在 DragonWorks、SkillCertKit、SkillDock 之后：

1. DragonWorks 让团队把真实机器人数据训练成 Qualcomm-first release candidate。
2. SkillCertKit 判断技能是否具备安装前 evidence。
3. SkillDock 负责技能分发。
4. EdgeFleet 负责真实客户现场的 staged rollout、telemetry、remote assist、incident capsule、rollback 和 training feedback。

一句话：从 checkpoint 到 paid deployment 的 Qualcomm-first RobotOps + evidence control plane。

## Architecture

### 1. EdgeFleet Agent

运行在机器人本体或站点边缘节点上，作为 ROS 2 旁路代理。

- 不替代本体 autonomy stack。
- 不越过 safety controller。
- 通过 ROS 2 topics/services/actions、MCAP、OpenTelemetry、CloudEvents 和本地 ring buffer 采集证据。
- 对远程协助命令执行 TTL、权限、速率限制、区域限制和本体 safety gate。

### 2. Skill Release Registry

把模型作为一等发布资产：

`dataset -> training code commit -> checkpoint -> quantization/calibration -> AI Hub compile/profile -> QNN/QAIRT artifact -> skill release -> deployment cohort -> robot instance -> incident`

每个节点记录 digest、toolchain version、target device、runtime、latency、memory、accuracy/eval、生成时间、签名和 claim boundaries。

### 3. FleetOps Console

按客户、站点、机器人、任务、技能和模型版本观察：

- online / offline / degraded。
- autonomy rate、intervention rate、failure clusters。
- latency、memory、thermal、battery、camera health、QoS deadline miss。
- release cohort、canary 状态、rollback 状态。
- incident capsule、operator session、support ticket 和 training feedback。

### 4. Incident Capsule

每次异常自动生成证据包：

- `incident_id`、`robot_id`、`site_id`、`skill_id`、`model_digest`、`artifact_digest`。
- 触发前后 MCAP / rosbag2 片段、视频、LiDAR/IMU/pose、command/action、operator input。
- safety state、autonomy state、network state、thermal/power、QNN profile。
- map/config snapshot、firmware/app version、SBOM/ref、release record。
- hash、signature、custody log、review annotations、retention policy。

关键定位：EdgeFleet 不判定法律责任，不声称安全认证；它保全可复核事实，支持 root-cause review、SLA、质保、客户复盘和下一轮训练。

### 5. Replay Lab

把 incident capsule 变成训练和发布门禁：

1. 重放事故前后片段。
2. 对比 previous-known-good 与 candidate skill。
3. 生成 regression test。
4. 把失败片段加入 LeRobot-compatible dataset。
5. 进入 TrainRouter 训练任务。
6. 新版本通过 SkillCertKit 后，EdgeFleet 做 shadow / canary / rollout。

## China / Global Deployment

EdgeFleet 应采用“双栈同源”：

- 中国内地独立部署。
- 全球多云部署。
- 共享产品抽象、schema、robot profile 和 Qualcomm/QNN artifact pipeline。
- 账号、密钥、日志、用户数据、工业遥测、视频、模型输入输出和合规流程隔离。

### 中国版

默认原则：

- 中国用户数据、工业遥测、视频/音频、日志、模型输入输出、密钥留在中国区。
- 公开网站/App/CDN 按需处理 ICP；按客户要求准备公安联网备案、等保测评协同材料。
- 跨境只同步低敏摘要、匿名聚合指标、版本号、artifact hash 和模型性能摘要。
- 如果涉及个人信息或重要数据出境，按 CAC 2024 数据出境规则评估安全评估、标准合同或认证路径。

云路线：

- 默认 POC：阿里云或腾讯云。
- 工业/政企/强合规：华为云或私有化。
- AI 原生/实时互动：火山引擎。

### 全球版

默认路线：

- Cloudflare：DNS/CDN/WAF/Zero Trust/Workers 入口。
- AWS/GCP/Azure：主控制面、企业集成、对象存储、日志、身份和审计。
- CoreWeave/Lambda/Runpod/Vultr 等 GPU cloud：训练、batch eval、弹性推理。
- on-prem / edge appliance：强隐私或低延迟客户。

## Business Model

第一批买家不是单店客户，而是有真实队列、售后压力和运营 KPI 的人：

- 机器人 OEM：需要交付后运维、远程支持、版本记录、客户门户和出海售后。
- 系统集成商：需要把一次性项目变成持续服务收入。
- RaaS operator：需要 uptime、SLA、remote diagnostics、rollback 和客户报告。
- 企业客户：需要事故复盘、合规证据、IT 审计、数据留存和集成能力。

### 中国价格思路

- AMR / 物流：500-2,000 元/台/月；大站点 20 万-100 万元/年；OEM 白标 50-300 元/台/月。
- 巡检 / 能源 / 工业：1,000-5,000 元/台/月；关键站点 30 万-300 万元/年项目制。
- 服务 / 清洁 / 物业：单台 ARPU 低，优先多站点连锁、物业集团和 OEM 云平台补强。
- 人形试点：5,000-30,000 元/台/月或试点项目制，卖数据采集、远程接管、安全审批和任务成功率。

### 海外价格思路

- AMR / 物流：200-800 美元/台/月 + 1,000-5,000 美元/站点/月 + 集成费。
- 巡检 / 能源 / 数据中心：500-2,000 美元/台/月 + 站点费。
- 农业 / 高价值作物：按设备/月、亩/acre 或季节包。
- 人形试点：2,000-10,000 美元/台/月 + enterprise integration / operator fee。

## Competition

EdgeFleet 不要正面替代所有现有工具。更准确的竞争地图：

- Formant：fleet observability、teleop、incident/ticketing 强；EdgeFleet 切 release evidence + model lineage。
- Viam：硬件抽象、fleet deployment、ML model rollout、registry 强；EdgeFleet 切 Qualcomm-first target、LeRobot lineage、安全证据和现场复盘。
- Foxglove：robotics data、visualization、log search、dataset curation 强；EdgeFleet 接其数据能力，但主打发布治理和现场证据。
- InOrbit：RobOps、fleet orchestration、VDA 5050 / MassRobotics / Open-RMF 互操作强；EdgeFleet 切 AI skill release governance。
- Boston Dynamics Orbit：Spot/Stretch/Atlas 企业 fleet 强，但偏 OEM 封闭生态；EdgeFleet 做跨硬件/跨模型。
- NVIDIA Isaac / Metropolis：GPU-first robotics / vision AI stack 强；EdgeFleet 做 Qualcomm-first edge evidence。
- Open-RMF / MassRobotics / VDA 5050：协议和互操作层，不是商业发布证据系统；EdgeFleet 应兼容。
- 中国 Geek+ / HAI / SEER / Pudu / Keenon / Gausium / Agibot：OEM/场景云平台强；EdgeFleet 做中立的模型、技能、审计和出海运维层。

## Moat

护城河来自现场证据，不来自看板 UI：

- Release evidence graph：每个 dataset、model、QNN artifact、skill、robot、cohort、incident、rollback 的关系图。
- Hardware profile library：Dragonwing / RB / QCS / IQ 的 camera、NPU、thermal、power、network、runtime 和 offline behavior。
- Incident memory：每次失败、接管、回滚、热降频、QoS miss、客户复盘都会变成下一版 rule。
- Connector compound：WMS/MES/CMMS/ERP、ROS 2、Open-RMF、VDA 5050、MassRobotics、OEM API、charger/door/elevator。
- Channel compound：OEM、SI、RaaS operator、Qualcomm developer ecosystem 和 SkillDock。

## Demo Storyboard

三分钟演示：

1. 注册三台机器人：canary、stable、offline-cache。
2. 上传 `dock-assist-v2` 技能，展示 dataset、model digest、SBOM、QNN profile、compatibility matrix。
3. EdgeFleet 检查 pre-install gate：设备 profile、runtime、battery、task idle、safety boundary。
4. canary 机器人激活新技能。
5. 制造低置信度、QoS deadline miss 或远程接管事件。
6. EdgeFleet 生成 incident capsule：MCAP、CloudEvents、OTel、视频、operator audit、model/artifact digest。
7. replay lab 对比 `dock-assist-v1` 和 `v2`。
8. 执行 rollback 到 previous-known-good。
9. 失败片段进入 LeRobot dataset 和 TrainRouter。
10. 展示 release graph：事故追溯到机器人、站点、模型、AI Hub profile job、训练数据和源码 commit。

## Why Qualcomm

EdgeFleet 让 Qualcomm 不只是边缘推理芯片，而是机器人队列运营的默认证据底座：

- Dragonwing attach：每个 reference workflow 都绑定 Qualcomm target。
- AI Hub/QNN adoption：compile/profile/run evidence 变成上线门禁。
- Enterprise confidence：灰度、回滚、断网、远程诊断、事故回放给客户采购和 IT 审查更清晰的证据。
- China/global proof：同一机器人产品抽象可以在中国数据驻留版、全球多云版和离线私有版中复用。
- Developer ecosystem：DragonWorks -> SkillCertKit -> SkillDock -> EdgeFleet 形成完整的 Qualcomm-first 机器人开发和商业化旅程。

## Claim Boundaries

可以讲：

- EdgeFleet 是 audit-ready、incident-ready、compliance-assist 的 fleet evidence system。
- EdgeFleet 帮助客户记录、回放、回滚和改进机器人部署。
- EdgeFleet 可以对接 ROS 2、MCAP、OpenTelemetry、CloudEvents、AI Hub/QNN、SkillCertKit 和 SkillDock。
- EdgeFleet 支持中国数据驻留和全球多云两套参考部署架构。

避免讲：

- 已获得 Qualcomm 官方认证、合作或投资。
- 自动满足中国法律、等保、SOC 2、ISO 或任何安全认证。
- 保证零事故、零停机、机器人一定比人更安全。
- 能立刻统一控制所有机器人、所有模型、所有 OEM fleet manager。
- 所有 LeRobot policy 都能无缝变成 QNN artifact。
- 远程协助可以绕过本体安全控制器。

## Sources

- IFR industrial robot demand：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Qualcomm AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm AI Hub profiling：https://workbench.aihub.qualcomm.com/docs/hub/profile_examples.html
- Qualcomm AI Hub compiling：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- ONNX Runtime QNN Execution Provider：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- MCAP spec：https://mcap.dev/spec
- MCAP ROS 2 guide：https://mcap.dev/guides/getting-started/ros-2
- CloudEvents：https://cloudevents.io/
- OpenTelemetry semantic conventions：https://opentelemetry.io/docs/specs/semconv/
- ROS 2 lifecycle：https://design.ros2.org/articles/node_lifecycle.html
- ROS 2 DDS Security：https://design.ros2.org/articles/ros2_dds_security.html
- Viam fleet management：https://www.viam.com/platform/fleet-management
- Formant fleet observability：https://docs.formant.io/docs/fleet-observability
- Foxglove product：https://foxglove.dev/product
- InOrbit overview：https://www.inorbit.ai/overview
- Open-RMF：https://www.open-rmf.org/
- MassRobotics AMR Interoperability：https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/
- VDA 5050：https://www.vda.de/en/topics/automotive-industry/vda-5050
- Cloudflare China Network：https://developers.cloudflare.com/china-network/
- CAC data export rules 2024：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
