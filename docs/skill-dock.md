# SkillDock Pitch

更新时间：2026-07-06。本页按照 YC / Airbnb 风格整理：先讲问题、时机和洞察，再讲解决方案、商业模型、竞争、壁垒、Qualcomm 必要性、演示和证据边界。

## One-Line Pitch

SkillDock 是机器人技能可信分发层。它不是“下载模型”的仓库，而是把 LeRobot lineage、SkillCertKit、EdgeRuntimeBench、Qualcomm edge profile、SBOM、安全边界、分阶段发布和回滚做成同一张可采购、可安装、可升级、可验收的技能卡。

## Problem

机器人行业的复用断在最后一公里：

- 同一个抓取、巡检、分拣、质检技能，每个客户、每台机器人、每套相机和每个 runtime 都要重新集成。
- 开发者无法把技能卖第二次。
- 企业买家不敢把陌生模型装到真实机器人上。
- 技能没有清晰的 task boundary、sensor requirement、safety envelope、runtime evidence 和 rollback path。
- 没有统一 edge profile，技能市场会变成截图目录。

## Why Now

现在的缺口不是有没有模型，而是技能能不能可信分发。

- UR+、MiR Go、ROS Index、Viam Registry、Reachy apps、OpenMind OM1、NVIDIA Isaac / GR00T、Intrinsic Flowstate 和 Unitree SDK 已经证明机器人生态会走向 marketplace、registry 和 skill catalog。
- LeRobot 把真实机器人数据、训练和评估工作流推到开发者可用层。
- TeleopStudio、CloudTwin、TrainRouter 和 EdgeRuntimeBench 让 skill lineage 可以从 episode 追到 edge profile。
- Qualcomm AI Hub、QNN/QAIRT、Device Cloud、Dragonwing profiles 和 Robotics Hub 可以让技能卡带上真实运行证据。

## Insight

机器人技能市场的核心不是 SKU 数量，而是信任密度。

一个技能能卖，是因为买家能提前看到：

- 在哪些 robot profile 上测试过。
- 来自哪些 LeRobot datasets。
- 模型如何训练和评估。
- 在 Qualcomm edge 上延迟、内存、功耗如何。
- 安全边界是什么。
- 失败后如何回滚。
- 谁负责支持。

## Solution

SkillDock 接在链路末端：

```text
TeleopStudio
  -> CloudTwin
  -> TrainRouter
  -> EdgeRuntimeBench
  -> SkillCertKit
  -> SkillDock
  -> staged install / upgrade / rollback
```

首版技能卡字段：

- `skill_id`
- `version`
- `digest`
- `task_boundary`
- `compatible_robot_profiles`
- `qualcomm_target_profile`
- `lerobot_lineage`
- `model_version`
- `runtime_dependencies`
- `edge_benchmark`
- `evidence_level`
- `permissions`
- `safety_boundary`
- `install_conditions`
- `rollback_plan`
- `support_owner`
- `pricing`

## Skill Package Architecture

每个技能应该是 digest-addressed evidence bundle，而不是松散模型文件。可以借鉴 OCI artifact / image index 的分发方式，把签名、SBOM、attestation 和证据作为 referrers 绑定到 skill digest。

`skill.yaml` 是 admission contract：

```yaml
apiVersion: skilldock.io/v1alpha1
kind: Skill
metadata:
  name: labforge.sample-transfer
  version: 1.0.0
  digest: sha256:demo-placeholder
  evidenceLevel: bench-real
spec:
  task:
    domain: lab-automation
    intent: sample-transfer
    allowedObjects: [tube, tray, cap]
    forbiddenActions: [human-contact, free-space-throw]
  io:
    sensors: [front_camera, wrist_camera, joint_state]
    actuators: [arm, gripper]
    actionRateHz: 20
  targets:
    soc: qcs8550
    board: dragonwing-dev-profile
    runtime: qnn-or-onnxruntime-qnn
    robotProfile: labforge.arm.v1
  safety:
    workspace: bounded-tabletop-cell
    speed: limited
    estop: required
    takeover: required
    failClosed: true
  lineage:
    datasets: [lerobot://labforge/sample-transfer-v1]
    trainingRun: trainrouter://run/demo
    evalReport: edgeruntimebench://report/demo
  supplyChain:
    sbom: sbom.cdx.json
    licenses: licenses.spdx.json
    signatures: signature.bundle
  release:
    channel: staged
    rollback: rollback-plan.yaml
    previousKnownGood: sha256:previous-demo
```

## Evidence Artifacts

- `skill.yaml`
- `hardware-profile.yaml`
- `runtime-constraints.yaml`
- `safety-boundary.yaml`
- `dataset-lineage.spdx.json`
- `model-lineage.intoto.json`
- `edge-profile.json`
- `eval-report.json`
- `sbom.cdx.json`
- `licenses.spdx.json`
- `signature.bundle`
- `policy-decision.json`
- `rollback-plan.yaml`
- `release-record.json`
- `install-audit-log.jsonl`
- `claim-boundaries.md`

## Market

切入点不是所有机器人，而是已有安装基础里的高频复用技能：

- 企业机器人用户：仓库、工厂、实验室、医院、校园、清洁/安防运营方。
- RaaS / fleet operators：希望提高利用率、降低支持负担、快速 redeploy。
- OEM developers：希望自己的机器人本体更有用。
- 系统集成商：需要可重复销售的 skill templates 和 evidence packs。
- 教育/研究：需要 starter skill libraries、课程、认证路径和 reproducible lab kits。
- Skill developers / ISVs：需要验证、发布、销售和支持渠道。

IFR 2025 报告显示 2024 年工业机器人安装量约 542,000 台，中国约占 54%；专业服务机器人销量接近 200,000 台。市场不缺机器人，缺的是可信复用的能力交付。

## Business Model

SkillDock 应使用混合模型，不只靠一个 take rate：

- Certification / profile fees：按 skill、robot profile、硬件族或 Qualcomm target 收取。
- Marketplace take rate：公开技能包、行业模板、升级包交易抽成。
- Private enterprise library：私有技能库、审批流、SSO/RBAC、审计、版本冻结、采购资料。
- Per-robot runtime：签名安装、版本控制、遥测 hook、staged rollout、rollback。
- Industry packs：重复任务包、acceptance tests、部署文档、SI 服务。
- Channel revenue share：与 SI、OEM、RaaS fleet 共享收益。

商业化顺序：

1. 先卖 SkillCertKit / evidence pack：这个技能是否能安全上架、安装、评估、升级和回滚。
2. 再做 SkillDock 私有技能库。
3. 然后做 curated public marketplace。

干净表述：机器人买一次，技能、验证、发布、证据和支持每年续费。

## Competition

不能声称“第一个机器人 App Store”。已有生态包括：

- UR+ / MiR Go：OEM marketplace，证明买家重视 approved products 和 reduced deployment risk。
- ROS Index：代码和包发现。
- Viam Registry：modules、ML models、fleet rollout、OTA 和 rollback。
- Hugging Face / LeRobot / Reachy apps：开源 AI、机器人数据和 app 分发。
- OpenMind OM1：机器人 runtime 和 app store 叙事。
- NVIDIA Isaac / GR00T：GPU-first simulation、synthetic data、robot foundation model stack。
- Intrinsic Flowstate：工业 skills catalog、行为树和 sim-to-real workflow。
- Unitree / KUKA / ABB / RoboDK：OEM / tooling plugin ecosystems。

SkillDock 的准确定位：

> SkillDock provides marketplace-readiness and deployment-evidence packaging for robot skills across named robot profiles and Qualcomm edge targets.

## Moat

短期壁垒：

- 精选技能目录。
- manifest schema。
- 兼容矩阵。
- Qualcomm profile 模板。
- reference skills。

中期壁垒：

- 每次安装、阻止、回滚、现场失败和人工接管都沉淀为 compatibility graph。
- enterprise procurement packets。
- SI/OEM/RaaS channel evidence。

长期壁垒：

- “技能 x 数据来源 x robot profile x Qualcomm target x 现场验收”的网络。
- 越多技能通过，越像机器人行业 trust layer。

## Qualcomm Ask

请求 Qualcomm 支持 6-8 周 “Dragonwing SkillDock Pilot”：

1. 提供或确认 target path：RB3 Gen 2 / QCS6490 现在可用，QCS8550 或 IQ-8275 作为下一步，IQ10 RRD 作为生产参考。
2. 每周一次 AI Hub / QNN / QAIRT office hour，定义 skill profile flow。
3. 共同定义轻量 Dragonwing Skill Profile schema。
4. 发布 2-3 个 reference skills：vision grasping、AMR inspection、visual tracking 或 quality inspection。
5. 引入 10-20 个早期测试方：教育、SI、AMR/arm OEM、Arduino/Edge Impulse/Foundries.io partners、Dragonwing module vendors。
6. 比赛期间只使用谨慎标签，例如 `Dragonwing-profiled` 或 `Qualcomm-edge-ready candidate`，不声称官方认证。

## Demo Plan

3 分钟演示：

1. 打开 `labforge.sample-transfer.v1` 技能卡。
2. 展示 task boundary、LeRobot lineage、SkillCertKit evidence、EdgeRuntimeBench profile。
3. 选择不兼容 robot profile，policy gate 阻止安装并给出原因。
4. 选择兼容 Qualcomm target profile，允许 staged rollout。
5. 展示 AI Hub / QNN / QAIRT evidence、latency、memory、signature、SBOM 和 rollback plan。
6. 运行一次 sample transfer。
7. 模拟 safety event 或 health check failure。
8. 回滚到 previous-known-good。
9. 把 failure episode 回流到 CloudTwin。

## Claim Boundaries

可以声称：

- 机器人 marketplace / app ecosystem 已被 UR+、MiR Go、Viam、ROS、Reachy 等方向验证。
- SkillDock 提供 marketplace-readiness 和 deployment-evidence packaging。
- 兼容性是 profile-specific、evidence-level-specific。
- 支持 Qualcomm-first edge readiness 叙事。

不能声称：

- 第一个机器人 App Store。
- universal robot compatibility。
- 官方 Qualcomm certification。
- legal safety certification。
- 任意 LeRobot / VLA / GR00T policy 都安全可安装。
- 任意模型都能无修改编译到 Qualcomm runtime。
- 闭源 humanoid OEM 暴露第三方 skill API，除非有公开证据。

## Sources

- UR Marketplace：https://www.universal-robots.com/marketplace/
- MiR Go：https://mobile-industrial-robots.com/products/mir-go
- ROS Index：https://index.ros.org/
- Viam fleet / registry：https://docs.viam.com/fleet/overview/
- LeRobot：https://huggingface.co/docs/lerobot/en/index
- Reachy Mini apps：https://huggingface.co/docs/reachy_mini/en/index
- NVIDIA Isaac ROS：https://developer.nvidia.com/isaac/ros
- Intrinsic Flowstate：https://www.intrinsic.ai/flowstate
- IFR industrial robots 2025：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots 2025：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Dragonwing developer ecosystem：https://www.qualcomm.com/developer/blog/2026/05/edge-ai-prototype-deployment-qualcomm-dragonwing-developer-ecosystem
