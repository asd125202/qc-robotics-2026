# SkillDock Pitch

更新时间：2026-07-06。本页按 YC / Airbnb 风格重写：问题、现有替代方案为什么失败、解决方案、为什么现在、产品、API/证据、市场、竞争壁垒、为什么 Qualcomm、演示和请求。

## One-Line Pitch

SkillDock 是生产机器人技能的可信分发与治理层：把模型、ROS 包、LeRobot lineage、SkillCertKit passport、SBOM/VEX、签名、Qualcomm edge profile、权限、灰度发布、遥测和回滚变成企业可采购、可安装、可审计、可续费的私有技能库。

## Thesis

机器人技能市场不会像手机 App Store 一样从海量低风险应用开始。它更像 `AWS/Microsoft private marketplace + Atlassian trust badges + UR+ approved ecosystem`。

买家不缺“能下载的代码”，缺的是这个问题的答案：

> 这个技能能否在这台机器人、这个现场、这个传感器、这个 runtime、这个安全边界、这个 Qualcomm edge target 上被允许安装？

SkillDock 要做的不是世界上最大的机器人 app store，而是把 ad hoc code drop 变成 verified, versioned, deployable robot skill asset。

## 01 · Problem

机器人行业的复用断在最后一公里。

同一个抓取、巡检、分拣、质检、搬运、清洁或实验室转移技能，每个客户、每台机器人、每套相机、每个夹爪、每张地图、每个 runtime 和每个现场安全边界都要重新集成。

真实痛点：

- 开发者无法把好技能卖第二次。
- 系统集成商无法把一次性项目变成可复用软件收入。
- 企业买家不敢把陌生模型装到生产机器人上。
- OEM 想做生态，但不想承担每个第三方技能的无限责任。
- RaaS/fleet operator 需要安全灰度、回滚、租户隔离、用量计费和支持路由。
- Qualcomm 如果只提供芯片和模型工具，无法进入技能分发生态的交易与治理环节。

一句话：机器人技能不是缺“下载按钮”，而是缺“可信安装与持续治理”。

## 02 · Current Alternatives Fail

### Universal Robot App Store

历史上的 RobotAppStore 和今天的 humanoid/consumer app store 说明“机器人应用”有吸引力，但 broad any-robot any-app 叙事失败在机器人没有手机那样统一的硬件、传感器、安全和支持边界。

### OEM Marketplaces

UR+、MiR Go、KUKA、FANUC、ABB 证明 approved ecosystem 可以降低部署风险；问题是它们通常绑定单一 OEM、主要围绕组件/附件/插件/工具，而不是跨 robot profile 的 AI skill release governance。

### ROS Index / Open Source

ROS Index、ROS-Industrial、MoveIt、LeRobot 和 Hugging Face 很适合发现代码、包、模型和数据；但 open package 不等于 deployable skill。缺少采购、签名、SBOM、权限、site policy、runtime gate、rollout、rollback 和支持责任。

### Fleet Ops Platforms

Viam、Formant、InOrbit、Foxglove、Rapyuta 等能做 fleet、可观测、远程控制或机器人 DevOps；但它们不是面向机器人技能交易、私有库、证据卡、发行门禁和开发者分成的完整商业层。

### Cloud Robotics Platforms

Cloud robotics 有价值，但不能把安全关键控制闭环放到云上，也不能忽视边缘延迟、隐私、网络和互操作问题。AWS RoboMaker 的退场提醒我们：不要把“全栈云机器人平台”当成核心叙事。

### Consumer/Humanoid App Stores

Reachy Mini、Unitree UniStore、OpenMind OM1 等是新信号，但 consumer/social/humanoid app store 不能直接证明工业客户会安装未经证据治理的技能。

## 03 · Solution

SkillDock = `Private Skill Library + Signed Distribution + Install Policy + Staged Rollout + Runtime Telemetry + Revenue/Support Routing`。

它位于产品链路末端：

```text
TeleopStudio
  -> CloudTwin
  -> TrainRouter
  -> EdgeRuntimeBench
  -> SkillCertKit
  -> SkillDock
  -> EdgeFleet staged install / upgrade / rollback
```

核心对象不是“app listing”，而是 `Skill Card + Skill Passport + Runtime Gate`：

- 哪些 robot profiles 被测试。
- 哪些传感器、执行器、地图、固件和 ROS/DDS runtime 被要求。
- 来自哪些 LeRobot datasets 和 training jobs。
- 在 Qualcomm edge target 上的 latency、memory、thermal、backend、fallback 和 unsupported-op 状态。
- 需要哪些权限、网络、数据和现场安全边界。
- 安装前 policy 是 allow、warn、deny、needs approval、simulate first 还是 rollback only。
- 谁卖、谁支持、谁承担现场集成责任、谁获得 revenue share。

## 04 · Why Now

四个趋势让 SkillDock 现在可做：

1. **机器人已形成足够装机基数**：IFR 2025 显示 2024 年全球工业机器人新增安装约 542,000 台，专业服务机器人销量接近 200,000 台，其中物流机器人是最大品类。
2. **机器人生态已经证明 marketplace 需求**：UR+、MiR Go、KUKA、FANUC、ABB、ROS Index、Reachy apps、Unitree、OpenMind 都说明机器人能力会走向 catalog / registry / marketplace。
3. **企业采购开始要求私有市场和治理**：AWS/Microsoft private marketplace、Atlassian trust badges、Shopify/Apple developer economics 都说明企业和开发者需要交易、审批、证据和分成机制。
4. **Qualcomm edge 可以成为技能默认运行目标**：Dragonwing、AI Hub、QNN/QAIRT、RB3/QCS/IQ profiles、Robotics Hub 让每张技能卡都能带可验证 edge evidence。

时机不是“模型突然够强”，而是模型、数据、edge profile、供应链证据和企业采购流程同时成熟。

## 05 · Product

### 5.1 Private Skill Library

企业/OEM/SI/RaaS 的私有技能目录：

- RBAC / SSO。
- 审批流。
- approved robot/site list。
- 私有报价。
- 版本冻结。
- 审计导出。
- 离线安装包。
- emergency revoke。

### 5.2 Skill Card

每张卡不是营销页，而是 install contract：

- `skill_id`
- `version`
- `digest`
- `task_boundary`
- `compatible_robot_profiles`
- `qualcomm_target_profile`
- `sensor_contract`
- `permissions`
- `data_egress_label`
- `safety_boundary`
- `evidence_level`
- `support_owner`
- `pricing`
- `rollback_plan`

### 5.3 Distribution Control Plane

技术上不是普通下载：

- OCI artifact digest。
- OCI referrers for signatures / SBOM / VEX / provenance / tests。
- TUF metadata for freshness, delegations, rollback/freeze protection。
- Uptane-style target assignment for robots with multiple controllers。
- OPA/Rego-style install policy。
- ROS/DDS permission generation。
- staged rollout and rollback audit log。

### 5.4 Revenue and Support Routing

每个技能都绑定 publisher、OEM、SI、support owner、warranty boundary、channel split 和 incident routing。SkillDock 不替代集成商，而是让集成商更快交付并获得可续费软件收入。

## 06 · Product API/Evidence

### API Surface

```text
POST /v1/skills
GET  /v1/skills/{id}/supply-chain
POST /v1/policies/evaluate
POST /v1/robots/{id}/preflight
POST /v1/robots/{id}/installs
POST /v1/fleets/{id}/rollouts
POST /v1/robots/{id}/rollback
POST /v1/sites/{id}/airgap-export
GET  /v1/audit/events
```

### SkillDock Bundle

```yaml
apiVersion: skilldock.io/v1alpha1
kind: Skill
metadata:
  name: labforge.sample-transfer
  version: 1.0.0
  digest: sha256:demo
  evidenceLevel: bench_real
spec:
  task:
    domain: lab-automation
    intent: sample-transfer
    allowedObjects: [tube, tray, rack]
    forbiddenActions: [human-contact, free-space-throw]
  io:
    sensors: [front_camera, wrist_camera, joint_state]
    actuators: [arm, gripper]
    actionRateHz: 20
  targets:
    robotProfile: labforge.arm.v1
    qualcommProfile: dragonwing-rb3-qcs6490-vision-v1
    runtime: qnn-or-onnxruntime-qnn
  permissions:
    rosTopics: [/camera/front, /joint_states, /cmd_action]
    networkEgress: none
    devices: [camera, npu]
  safety:
    workspace: bounded-tabletop-cell
    speed: limited
    estop: required
    takeover: required
    failClosed: true
  release:
    channel: staged
    previousKnownGood: sha256:previous
    rollback: rollback-plan.yaml
```

### Evidence Artifacts

- `skilldock.yaml`
- `skill-card.json`
- `skill-passport.json`
- `skillcertkit-policy-decision.json`
- `edge-profile.qualcomm.json`
- `runtime-constraints.yaml`
- `safety-boundary.yaml`
- `permissions.sros2.xml`
- `sbom.cdx.json`
- `vex.openvex.json`
- `signature.bundle`
- `tuf-metadata/`
- `oci-referrers.json`
- `rollout-plan.yaml`
- `rollback-plan.yaml`
- `install-audit-log.jsonl`
- `revenue-share.yaml`
- `support-boundary.md`

### Gate Outcomes

- `allow`
- `warn`
- `deny`
- `needs_approval`
- `simulate_first`
- `rollback_only`

## 07 · Market & Business Model

SkillDock 应该 enterprise-first、marketplace-second。

第一批客户：

- Enterprise ops / EHS / CISO：私有目录、审批、审计、site policy、rollback、incident log。
- Robot OEM：白标技能商店、SDK、兼容测试、签名包格式、生态收入。
- System integrator：复用部署模板、客户定制 fork、服务续费收入。
- RaaS provider：租户隔离、远程 provisioning、usage metering、SLA dashboard、fleet-safe rollout。
- Skill developer / ISV：分发、计费、trust packaging、支持渠道。

### Initial Verticals

先选明确、重复、低监管摩擦的技能：

- warehouse/logistics AMR。
- manufacturing/cobot cell。
- lab sample transfer / light QA。
- facility cleaning / inspection。
- machine-tending assist。

暂缓医疗、养老和公共场景高自治 humanoid，避免合规和责任过早拖慢。

### Pricing

- Developer/SI Sandbox：免费或 `$99-$299/seat/month`。
- Private Skill Library：`$10k-$50k/year/site` 或 `$2k-$5k/site/month`。
- Per-Robot Runtime Gate：`$20-$250/robot/month`，按 telemetry、policy、rollback 和支持等级区分。
- Certification/Review Fee：`$1k-$10k/skill/version/profile`。
- Enterprise Fleet：`$10k-$50k/month minimum`。
- Public/Partner Marketplace：10%-15% take rate；早期开发者前 `$50k-$250k` 可 0% 抽成。
- Private Offers / Channel Deals：3%-8% platform fee。
- Managed Runtime + Monitoring + Rollback：10%-20%。
- RaaS Usage Add-on：1%-5% metered RaaS revenue。

### Business Sequence

1. 手工和 3-5 个 OEM/SI launch partners 做 5-10 个可信技能。
2. 先卖 private library 和 enterprise approval workflow。
3. 再开放 partner marketplace。
4. 通过 SkillCertKit review、runtime gate、telemetry、support routing 和 transaction fee 形成复合收入。

## 08 · Competition & Moat

不能说“第一个机器人 App Store”。正确说法：

> SkillDock is trusted distribution and procurement for production robot skills.

竞争和相邻产品：

- UR+ / MiR Go / KUKA / FANUC / ABB：OEM-scoped approved ecosystem。
- ROS Index / ROS-Industrial / MoveIt：open package discovery and robotics dev substrate。
- Reachy Mini / Unitree / OpenMind：emerging robot app store signals。
- Viam / Formant / InOrbit / Foxglove / Rapyuta：fleet ops, observability, DevOps。
- NVIDIA Isaac / GR00T / Intrinsic Flowstate：physical AI creation and deployment tooling。
- AWS/Microsoft private marketplace、Atlassian、Shopify：enterprise procurement and developer economics analogy。

### Moat

短期壁垒：

- curated private skill library。
- `skilldock.yaml` manifest。
- SkillCertKit integration。
- Dragonwing profile templates。
- signed install and rollback path。

中期壁垒：

- compatibility graph。
- install/block/rollback telemetry。
- SI/OEM/RaaS channel partnerships。
- private marketplace procurement workflows。
- support and warranty routing data。

长期壁垒：

```text
skill x robot profile x sensor x runtime x edge target x site policy x incident x buyer acceptance x revenue history
```

越多技能通过，越多站点部署，越多回滚和 incident 被记录，SkillDock 越像机器人行业的 trust layer。

## 09 · Why Qualcomm

SkillDock 可以把 Dragonwing 从硬件选项，变成机器人技能的默认安装目标。

为什么 Qualcomm 应该支持：

- Robotics Hub 可以从 sample gallery 升级成 installable, signed, profile-scoped skill packages。
- AI Hub / QNN / QAIRT 产物可以从开发工具变成 buyer-facing evidence。
- 每张技能卡都能命名 target profile：`dragonwing-rb3-qcs6490-vision-v1`、`dragonwing-qcs8550-v1`、`dragonwing-iq9075-industrial-v1`、`dragonwing-iq10-rrd-v1`。
- 技能卡可以暴露 backend、QNN artifact、unsupported ops、CPU fallback、thermal drift、camera sync、rollback 和 telemetry。
- 更多技能瞄准 Dragonwing，更多机器人选择 Dragonwing 以获得可信技能目录。

### Dragonwing Skill Profile Fields

- SoC / board / OS / kernel / firmware。
- QNN / QAIRT / ONNX Runtime QNN versions。
- model artifact type and hash。
- backend and fallback policy。
- camera count / resolution / FPS / calibration hash。
- control rate and end-to-end latency。
- power mode / thermal envelope。
- rollout ring and previous-known-good digest。

### 6-8 Week Qualcomm Ask

请求：

- RB3 Gen 2 / QCS6490 profile as MVP。
- QCS8550 or IQ-9075/IQ10 roadmap profile as expansion。
- AI Hub / QNN office hour。
- 2-3 reference skill cards：visual tracking、quality inspection、vision grasping、AMR inspection。
- 审核 `Dragonwing-profiled candidate` badge language。
- 将一个 Robotics Hub sample 转成 SkillDock package：manifest、evidence、rollout、rollback。

## 10 · Demo & Ask

### 3-Minute Demo

1. **0:00-0:25**：企业管理员打开私有 SkillDock library，按 robot model、site policy、approved Qualcomm target 过滤。
2. **0:25-0:55**：SI 发布 `labforge.sample-transfer.v1` 或 `warehouse.aisle-scan.v1`，带 SBOM、测试视频、兼容矩阵、支持方和 warranty boundary。
3. **0:55-1:25**：EHS/CISO 查看权限：相机、地图、网络出口、机械臂速度、数据保留和现场边界。
4. **1:25-1:55**：SkillDock 对不兼容 profile 返回 deny，对兼容 Dragonwing profile 返回 one-robot canary。
5. **1:55-2:25**：展示 AI Hub/QNN profile、latency、memory、backend、thermal、signature、SBOM 和 rollback。
6. **2:25-2:45**：模拟 regression / safety event，触发回滚到 previous-known-good。
7. **2:45-3:00**：管理员批准 50 台机器人跨两个站点 rollout，系统显示 billing/revenue split 和 audit log。

### Ask

主办方和 Qualcomm 给我们开发板、AI Hub/QNN profile review、Dragonwing Skill Profile 建议和 Robotics Hub reference sample；我们交付一个可复用样例：从 SkillCertKit passport 到 SkillDock private library、Dragonwing-profiled skill card、安装门禁、灰度发布、回滚和收入分成。

## Claim Boundaries

可以声称：

- trusted robot skill distribution and governance。
- private skill library for enterprise/OEM/SI/RaaS。
- profile-specific install and rollout gate。
- Qualcomm-edge-ready / Dragonwing-profiled candidate workflow。
- SkillCertKit evidence to SkillDock distribution flow。

不能声称：

- world's first robot app store。
- works on any robot。
- certified safe。
- no integrator required。
- official Qualcomm certification。
- universal one-click install。
- cloud-only robot control。
- ROS package equals deployable robot skill。
- AI Hub model latency equals full robot control-loop latency。
- signing or SBOM proves behavior is safe。
- rollback is always safe after physical-world side effects。

所有兼容性必须写清：robot model、firmware、peripherals、site policy、evidence level、runtime、Qualcomm profile 和 support owner。

## Sources

- Universal Robots Marketplace：https://www.universal-robots.com/marketplace/
- MiR Go：https://mobile-industrial-robots.com/products/mir-go
- KUKA Marketplace：https://www.kuka.com/en-us/services/my-kuka/kuka-marketplace
- KUKA Creator Portal：https://www.kuka.com/en-us/future-production/iiqka-robots-for-the-people/creator-portal
- FANUC CRX devices：https://crx.fanucamerica.com/cobot-devices
- FANUC plug-in devices：https://www.fanuc.co.jp/en/product/robot/function/plugindevice/
- ABB AppStudio：https://www.abb.com/global/en/areas/robotics/products/software/appstudio
- ROS Index：https://index.ros.org/
- ROS-Industrial：https://rosindustrial.org/
- Reachy Mini app store：https://huggingface.co/blog/clem/reachymini-appstore
- Reachy Mini docs：https://huggingface.co/docs/reachy_mini/en/index
- Unitree Explore Robot app：https://apps.apple.com/us/app/unitree-explore-robot/id6778743889
- OpenMind OM1：https://github.com/OpenMind/OM1
- RobotAppStore historical coverage：https://techcrunch.com/2012/12/10/robotappstore-raises-250k-from-grishin-robotics-to-take-the-app-distribution-model-to-the-world-of-robots/
- AWS RoboMaker launch：https://aws.amazon.com/blogs/aws/aws-robomaker-develop-test-deploy-and-manage-intelligent-robotics-apps/
- AWS shutdown services：https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html
- Rapyuta.io：https://www.rapyuta-robotics.com/rapyuta-io/
- Apple Small Business Program：https://developer.apple.com/app-store/small-business-program/
- Shopify App Store revenue share：https://shopify.dev/docs/apps/launch/distribution/revenue-share
- Atlassian Marketplace trust：https://www.atlassian.com/trust/marketplace
- Microsoft commercial marketplace fee：https://learn.microsoft.com/en-us/partner-center/marketplace-offers/marketplace-commercial-transaction-capabilities-and-considerations
- AWS Private Marketplace：https://docs.aws.amazon.com/marketplace/latest/buyerguide/private-marketplace-current.html
- AWS channel partner private offers：https://aws.amazon.com/marketplace/features/cpprivateoffers
- OCI 1.1 referrers：https://opencontainers.org/posts/blog/2024-03-13-image-and-distribution-1-1/
- TUF：https://theupdateframework.github.io/specification/latest/
- Uptane：https://uptane.org/docs/2.1.0/standard/uptane-standard
- Open Policy Agent：https://www.openpolicyagent.org/docs
- Sigstore cosign：https://docs.sigstore.dev/quickstart/quickstart-cosign/
- SPDX：https://spdx.dev/
- CycloneDX：https://cyclonedx.org/specification/overview/
- ROS 2 DDS Security：https://design.ros2.org/articles/ros2_dds_security.html
- IFR service robots 2025：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- IFR industrial robots 2025：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- Open-RMF：https://www.open-rmf.org/
- Locus Robotics RaaS：https://locusrobotics.com/locusone/automated-warehouse-software/flexible-scalable
- Formic full-service automation：https://formic.co/full-service-automation
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm Dragonwing developer ecosystem：https://www.qualcomm.com/developer/blog/2026/05/edge-ai-prototype-deployment-qualcomm-dragonwing-developer-ecosystem
- Qualcomm Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- QCS6490：https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490
- QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
