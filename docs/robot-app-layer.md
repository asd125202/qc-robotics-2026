# RobotAppLayer Pitch

更新时间：2026-07-07。机器人 app store、LeRobot、ROS 2、AI Hub/QNN/QAIRT、OTA 安全、应用备案、e-fapiao、GDPR/COPPA/EU AI Act 和机器人安全标准都在快速变化；正式提交前必须重新核对事实、版本、口径和合规边界。

## One-Line Thesis

> RobotAppLayer 是机器人世界的 App Store + MDM + CI/CD：把技能从“能跑的 demo”变成可签名、可验证、可上架、可收费、可灰度、可回滚的 app release。

它不是另一个 robot OS，也不是重写 ROS。它定义 ROS 2 + LeRobot + Qualcomm edge 之上的可信应用层：`.rap` signed skill bundle、RobotKit stable API、物理权限、兼容性矩阵、AI Hub/QNN evidence、SkillDock marketplace、RevenueStack billing 和 EdgeFleet rollout/rollback。

### 01 · Problem

机器人开发现在仍像项目制系统集成。

- ROS 2 package、launch、topic/action、驱动、模型、现场参数、权限、日志、OTA、回滚和收费各自分散。
- LeRobot policy 能训练策略，但客户买的不是 checkpoint；客户买的是“这个技能能否在这台机器人、这个现场、这个 Qualcomm edge target 上被允许安装、运行、计费、审计和回滚”。
- 开发者想写巡检、样品转移、配送、教育课程或远程运维，却先被相机、夹爪、ROS QoS、driver bring-up、模型导出和现场调参拖住。
- 企业买家需要物理权限、安全边界、数据归属、SBOM/VEX、签名来源、事故日志、回滚和责任证明，但机器人应用通常还停留在脚本和项目文件夹阶段。
- 没有可信兼容性、认证、分发、试用、授权、用量计费和开发者分成，机器人技能生态很难越过一次性集成项目。

### 02 · Current Alternatives Fail

现有层都必要，但没有谁负责 trusted robot app release。

- ROS 2：提供 topic、service、action、lifecycle、QoS、DDS security，是基座，不是 app ABI、权限商店、计费系统或发布治理层。
- LeRobot：正在闭合 robot learning loop，但不负责签名技能包、企业上架、entitlement、billing、fleet rollback 和现场责任边界。
- Qualcomm AI Hub / QNN：能产生模型级 optimize / compile / profile / inference evidence，但这些证据还没有变成“技能能否上架和安装”的发行门禁。
- UR+、MiR Go、Unitree UniStore、OpenMind robot app store 证明方向成立，但多数锁在单一品牌或早期行为包，缺少跨硬件 release workflow。
- Viam、Intrinsic、Foxglove、Open-RMF、Isaac / GR00T 各解决开发、数据、调度、仿真或 foundation model 问题，但不把物理权限、edge profile、商业分发和回滚做成中立应用层。
- 普通移动 app store 模型不够：机器人 app 不是只访问相机/位置，它会移动、抓取、开门、靠近人、上传现场数据和影响真实资产。

### 03 · Solution

RobotAppLayer = 机器人应用 ABI + trusted release workflow。

核心对象：

- `.rap` signed skill bundle：app id、publisher signature、SBOM/VEX/provenance、OCI artifact、container/Wasm component、ROS interface map、launch graph、LeRobot policy binding、robot profile、Qualcomm target profile、permission policy、billing SKU、rollback target。
- `RobotKit` stable API：`observe / move / grasp / speak / record / train / profile / install / monitor / rollback`，底层映射到 ROS 2 actions/services、LeRobot datasets/policies、AI Hub/QNN/ONNX Runtime QNN、marketplace entitlement。
- Safety broker：app 提交 intent，例如“巡检 A 区货架”或“抓取样本管”，不直接发布 raw motor / cmd_vel / joint trajectory；broker 执行 geofence、speed/force、E-stop、人距、payload、site policy 和 ODD 检查。
- SkillDock marketplace：公开市场、企业私有商店、OEM 商店和 SI 套件共享一套签名、兼容、授权、计费和分成对象。
- EdgeFleet rollout：canary、cohort targeting、health gate、incident capsule、kill switch、A/B rollback 和 audit export。

一句话：RobotAppLayer 把 `ROS 2 + LeRobot policy + Qualcomm edge evidence + signed bundle + marketplace + billing + rollback` 串成一个 app release。

### 04 · Why Now

2026 年，机器人 app store 从概念变成市场信号。

- UR+ 已有 over 500 certified kits / components / software / accessories；MiR Go 有 160+ applications / top modules。工业客户已经为“认证兼容性”和“降低集成风险”付费。
- Unitree UniStore、OpenMind robot app store 和 humanoid / quadruped 行为包说明机器人 app store 正在从工业组件扩展到通用技能和动作。
- Viam Registry、ROS Index、NVIDIA Isaac ROS Assets 说明机器人开发者已经接受 package / registry / semantic versioning / asset distribution 形态。
- LeRobot v0.6.0 在 2026-07-07 强调 deployment CLI、HIL corrections、HF Jobs、benchmarks 和 robot learning loop；RobotAppLayer 补上 release loop。
- LeRobotDataset v3、MCAP/Foxglove、Open-RMF、VDA 5050、ROS 2 Jazzy LTS、OCI 1.1、Sigstore/TUF/Uptane 给应用包、数据、调度、签名和 OTA 提供可组合基座。
- Qualcomm Dragonwing Robotics Hub、RB3 Gen 2、QCS6490/QCS8550、AI Hub、QNN/QAIRT 和 IQ / Dragonwing production path 让 edge-first robot apps 有清晰 target。

### 05 · Product

MVP 不做“所有机器人通用 app store”。先做 ROS 2 + LeRobot + Qualcomm edge 的受控子集，从低风险高复用场景切入。

第一批场景：

- LabForge 样品转移 / light QA。
- warehouse aisle scan / indoor inspection。
- education / research kit lessons。
- teleop data collection / failure replay。
- 低力矩操作技能和 facility connectors。

产品模块：

- RobotApp SDK：Python / TypeScript API，面向 observe、move、grasp、record、train、profile、deploy、monitor。
- Permission Manifest：camera、mic、map-read、navigate-zone、drive-low-speed、manipulate-object、open-door、remote-control、near-human-operation、cloud upload、train-on-customer-data。
- Compatibility Registry：robot profile、sensor、effector、ROS distro、LeRobot version、ONNX/QAIRT/QNN runtime、Qualcomm target、compute budget、ODD。
- Certification CI：static manifest、ROS graph contract、MCAP replay、sim smoke、HIL、latency budget、collision/intervention/success gates、SBOM/VEX、rollback test。
- Qualcomm EdgeProfile Builder：AI Hub / QNN / ONNX Runtime QNN profile；明确 `model inference only`，另测 end-to-end camera-to-action p95。
- SkillDock Store：公开 listing、企业私有商店、OEM 商店、试用、订阅、用量计费、developer settlement、support boundary。
- EdgeFleet Runtime：签名安装、canary、telemetry、incident capsule、kill switch、data feedback、version rollback、site audit。

### 06 · Product API/Evidence

评委需要看到它不是“平台口号”，而是一套 app release API 和 evidence pack。

核心对象：

- `RobotProfile`: ROS domain、namespace、lifecycle、sensor、effector、E-stop、payload、RB3/QCS6490/QCS8550/IQ target。
- `TaskContract`: task phases、preconditions、success criteria、operator takeover、failure labels、MCAP recording、LeRobot episode strategy。
- `SkillManifest`: app id、publisher、signature、version、OCI digest、container/Wasm、ROS interface map、LeRobot policy、rollback target、billing SKU。
- `PermissionPolicy`: physical permissions、DDS governance、network egress、data upload、remote operation、JIT approval、site/zone/time/mission scope。
- `LeRobotPolicyBinding`: dataset lineage、checkpoint、train_config、normalization stats、observation/action schema、eval metrics、embodiment compatibility。
- `QualcommEdgeProfile`: device、runtime、QNN/QAIRT version、ONNX opset、p95 latency、memory、thermal drift、fallback ops、profile date。
- `AppRelease`: install checks、canary rollout、active/degraded state、incident capsule、fleet metrics、entitlement、rollback。

Core API：

```text
POST /v1/skills
POST /v1/skills/{id}/sign
POST /v1/robots/{id}/preflight
POST /v1/profiles/qualcomm
POST /v1/permissions/grant
POST /v1/rollouts
POST /v1/meter-events
POST /v1/rollback
GET  /v1/audit/events
```

Evidence pack：

- `skill-passport.json`
- `edge-profile.qualcomm.json`
- `qnn_profile.csv`
- `mcap_replay_report.json`
- `lerobot-lineage.json`
- `permission-policy.yaml`
- `sbom.cdx.json`
- `vex.json`
- `signature.bundle`
- `rollout-plan.yaml`
- `rollback-plan.yaml`

Guardrail：AI Hub / QNN latency 只能标注为 `model inference only`；要另测 end-to-end camera-to-action p95、warm load、memory、thermal drift、unsupported fallback、safety broker rejection 和 rollback recovery。

### 07 · Market & Business Model

用户买的不是“机器人应用”这个词，而是降低集成风险、复用行为、更快部署、fleet updates、责任边界和可收费 workflow。

第一批买方：

- Robot OEM：希望让第三方技能安全进入自家机器人，但不想每个 app 都变成定制集成。
- 系统集成商 / SI：需要把行业流程包装成可复制、可计费、可维护的 skill bundle。
- RaaS / fleet operator：需要安装、灰度、权限、日志、回滚、SLA 和用量计费。
- 企业机器人团队：需要私有商店、SSO/RBAC、审计、合规、data residency 和支持责任。
- 教育 / 研究机构：需要课程、样例 app、可复现实验、低风险权限和比赛套件。
- 技能开发者：需要 discovery、认证、安装基数、billing、payout 和真实机器人 feedback。

中国版：

- 以 enterprise / education skill marketplace 进入，不做纯消费 app store。
- 支持 OEM bundle、SI 私有部署、教育/比赛套件、低 take-rate 市场、本地云/BYOC、WeChat/Alipay 分账、e-fapiao、ICP/App filing metadata、China-hosted telemetry/model endpoints。
- 重点类别：motion/action packs、venue guide/reception、餐饮/酒店/PMS/POS 配送、清洁/巡检 reporting、teleop/data collection、education lesson modules、enterprise connectors。

海外版：

- enterprise control plane + private marketplace + certified partner app。
- 支持 Stripe Connect / Merchant of Record、Apple/Google-style commission、GDPR/COPPA/EU AI Act controls、regional hosting、SSO/RBAC、audit/SLA、ROS/Open-RMF/Isaac/LeRobot integrations。

定价：

- 免费 SDK、simulator adapter、样例应用和公开 listing。
- Team / Pro：每开发者每月 $49-149，包含私有应用、CI 验证、日志、权限和仿真任务。
- Production runtime：每活跃机器人每月 $50-250，包含部署、遥测、权限、回滚、审计和 fleet runtime。
- Certification / review fee：标准应用 $1k-5k，高风险/高合规应用 $10k+。
- Enterprise site license：每站点每年 $25k-150k，包含私有市场、SSO、合规、on-prem/private cloud、WMS/MES 集成和 SLA。
- Marketplace take rate：10%-30%；工业场景可降低 take rate 并增加认证费 / 支持费。

### 08 · Competition & Moat

竞争定位不是“另一个 robot OS”，而是 trusted app release layer。

相邻玩家：

- ROS Index / ROS-Industrial：package / ecosystem。
- LeRobot / Hugging Face：data、policy、training、Hub。
- Viam：registry、cloud robotics platform、usage-based infra。
- Intrinsic Flowstate：enterprise robot skill platform。
- Foxglove / MCAP：observability and robot data。
- Open-RMF / VDA 5050：fleet coordination and AMR protocol。
- NVIDIA Isaac / GR00T：simulation、robot learning、GPU-first physical AI。
- UR+ / MiR Go / PUDU / Unitree / OpenMind：OEM or category-specific marketplaces。

壁垒：

- App ABI：比 ROS topic 更稳定的 RobotKit 能力接口。
- Physical permission taxonomy：数据、传感器、地图、动作、远程控制、云训练和 near-human operation 的可审计权限图。
- Compatibility graph：`skill x robot profile x sensor x ROS distro x LeRobot policy x QNN runtime x site policy`。
- Certification corpus：sim、HIL、MCAP replay、incident replay、safety broker rejection 和 rollback recovery 的失败模式资产。
- Marketplace gravity：开发者、SI、OEM、企业客户和教育用户共享安装、试用、授权、计费和分成流程。
- Qualcomm evidence：AI Hub/QNN/QAIRT profile、低功耗边缘运行、连接、安全启动和 device attestation 成为上架门槛。

长期数据资产：`skill x robot profile x sensor x ROS distro x LeRobot policy x QNN runtime x site policy x incident x revenue history`。

### 09 · Why Qualcomm

Qualcomm 的战略价值不是“被写进硬件清单”，而是成为每个机器人技能 release 的默认 edge target。

- Dragonwing Robotics Hub sample project 可以变成 signed skill package；RB3 / QCS6490 做近期验证，QCS8550 / IQ / Dragonwing 做 production-forward profile。
- AI Hub/QNN/QAIRT evidence 从工程 artifact 升级为 buyer-facing release receipt：latency、memory、backend、NPU placement、fallback、profile date、target board。
- Qualcomm 的低功耗、多相机、连接、安全、真实设备 profile 和 Partner Network 正好适合“可上架、可部署、可回滚”的 production robotics workflow。
- 每个 app listing 都能展示 `Dragonwing-profiled candidate`：target board、runtime、model inference p95、end-to-end p95、memory、thermal、permissions、rollback、support boundary。
- 对抗 NVIDIA 的叙事不是只比 TOPS，而是“edge-efficient robot app release pipeline”：cloud trains, Qualcomm edge ships, marketplace distributes, EdgeFleet rolls back, RevenueStack bills。

公开口径：使用 `Dragonwing-profiled candidate` 或 `Qualcomm-edge-ready candidate`，不声称官方认证、官方背书或任意模型自动 QNN 化。

### 10 · Demo & Ask

7 分钟 demo：把 LabForge 样品转移从脚本变成可发布 app。

1. `robotapp init lab-transfer --target rb3-gen2` 生成 `.rap`、RobotProfile、PermissionPolicy、TaskContract。
2. 代码调用 `observe / grasp / record`，不直接暴露 raw motor topic、cmd_vel 或临时 launch file。
3. 运行 LabForge 样品转移，生成 MCAP + LeRobotDataset v3 episode。
4. 模拟失败和人工接管：HIL correction 回流到 LeRobot 训练。
5. 策略导出后走 AI Hub / QNN / ONNX Runtime QNN profile，生成 `edge-profile.qualcomm.json`。
6. SkillCertKit 通过后进入 SkillDock card：权限、兼容 profile、QNN evidence、价格、支持方、rollback plan。
7. EdgeFleet canary 安装；异常触发 rollback，并生成 meter event 和 audit export。

Ask：

- 6-8 周 Qualcomm validation sprint。
- RB3 Gen 2 / QCS6490 target；QCS8550 / IQ / Dragonwing roadmap feedback。
- AI Hub / QNN / QAIRT office hours。
- 2-3 个 reference skills：lab-transfer、inspection、education lesson。
- Robotics Hub 发布指导。
- 5-10 个 OEM / SI / developer intro。
- 对 `Dragonwing-profiled candidate` 口径做边界确认。

## Claim Guardrails

- 不说 RobotAppLayer 替代 ROS 2、LeRobot、Viam、Intrinsic、Isaac、Open-RMF 或 OEM 商店；它是中立 app release layer。
- 不把 AI Hub/QNN profile 夸大为整机性能；明确区分 model inference 和 end-to-end robot task。
- 不声称官方 Qualcomm 认证、官方合作或任意模型自动 QNN 化。
- 不把安全权限描述成“完全防止事故”；只说降低风险、审计、门禁、回滚和证据。
- 不把中国 app store 说成无门槛消费应用市场；强调企业/教育 skill marketplace、备案、分账、e-fapiao 和数据本地化。

## Sources

- ROS 2 Actions：https://design.ros2.org/articles/actions.html
- ROS 2 Lifecycle：https://design.ros2.org/articles/node_lifecycle.html
- ROS 2 DDS Security：https://design.ros2.org/articles/ros2_dds_security.html
- ROS 2 Jazzy / REP 2000：https://reps.openrobotics.org/rep-2000/
- ROS 2 access control：https://design.ros2.org/articles/ros2_access_control_policies.html
- LeRobot v0.6.0：https://huggingface.co/blog/lerobot-release-v060
- LeRobot Dataset v3：https://huggingface.co/blog/lerobot-datasets-v3
- LeRobot docs：https://huggingface.co/docs/lerobot/en/index
- OCI 1.1 artifacts：https://opencontainers.org/posts/blog/2024-03-13-image-and-distribution-1-1/
- Sigstore Cosign：https://docs.sigstore.dev/cosign/signing/signing_with_containers/
- TUF spec：https://theupdateframework.github.io/specification/latest/
- Uptane：https://uptane.org/docs/latest/standard/uptane-standard
- CISA SBOM：https://www.cisa.gov/sbom
- CISA VEX：https://www.cisa.gov/sites/default/files/2023-04/minimum-requirements-for-vex-508c.pdf
- SLSA v1.2：https://slsa.dev/blog/2025/11/announce-slsa-v1.2
- UR+ Marketplace：https://www.universal-robots.com/marketplace/
- MiR Go：https://mobile-industrial-robots.com/products/mir-go
- Viam Registry：https://docs.viam.com/what-is-viam/
- Viam Pricing：https://www.viam.com/pricing
- Intrinsic Flowstate：https://www.intrinsic.ai/flowstate
- OpenMind App Store：https://roboticsandautomationnews.com/2026/02/02/openmind-launches-app-store-for-robots/98554/
- Unitree Explore：https://apps.apple.com/us/app/unitree-explore-robot/id6778743889
- PUDU Open Platform：https://open.pudutech.com/en
- Boston Dynamics Orbit：https://bostondynamics.com/products/orbit/
- Qualcomm Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm QNN SDK：https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm ONNX Runtime Plugin EP：https://www.qualcomm.com/developer/blog/2026/05/qualcomm-launches-the-first-onnx-runtime-plugin-execution-provider
- China Robot+ plan：https://www.ncsti.gov.cn/zcfg/zcwj/202301/t20230120_107305.html
- MIIT App filing notice：https://www.hunan.gov.cn/zqt/zcsd/202308/t20230809_29456035.html
- China e-fapiao rollout：https://fgk.chinatax.gov.cn/zcfgk/c100012/c5236067/content.html
- CAC cross-border rules：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- EU Cyber Resilience Act：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
