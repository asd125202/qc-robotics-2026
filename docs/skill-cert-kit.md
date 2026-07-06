# SkillCertKit Pitch

更新时间：2026-07-06。本页按照 YC / Airbnb 风格重写：先讲安装风险和为什么现在，再讲解决方案、证据包、商业模型、竞争、壁垒、Qualcomm 请求和 claim boundaries。

## One-Line Pitch

SkillCertKit 是机器人技能上架前的信任层：把一个策略模型变成 profile-scoped evidence package，包含数据血缘、硬件兼容、Qualcomm edge profile、安全边界、SBOM、签名、安装门禁、回滚和版本记录，先过信任门，再进入 SkillDock。

## Problem

企业不会把陌生模型随手装进真实机器人。

今天的机器人技能常常是一次性集成项目：

- demo 能跑，但不代表适配买家的相机、机械臂、底盘、runtime、网络、安全 IO、数据权限和现场边界；
- 开发者无法把同一个技能卖给第二个客户；
- 系统集成商重复验证；
- 企业 IT / 安全无法审计；
- SkillDock 如果直接做“下载按钮”，会变成高风险模型仓库；
- Qualcomm edge value 不会沉淀，除非每个技能声明并验证 target profile。

## Why Now

机器人技能正在软件化，但物理世界还缺信任层。

- UR+ 和 MiR Go 说明机器人买家接受通过认证生态降低部署风险。
- IFR 2025 显示 2024 年全球新增工业机器人约 542,000 台，专业服务机器人接近 200,000 台，硬件基数足够大。
- LeRobot、DROID、Open X-Embodiment 等让真实机器人数据和策略更可复用。
- Qualcomm AI Hub、QNN/QAIRT、Device Cloud、Profiler、Dragonwing Robotics Hub 和 IQ10 RRD 让端侧 profile 与部署证据可产品化。
- 企业采购、EU CRA readiness、NIST SSDF、SBOM/VEX 和 secure update 让“软件证据”越来越接近采购必要条件。

## Insight

机器人技能市场的关键不是 SKU 数量，而是安装前信任密度。

- ROS package 不是 skill package。
- Model card 不是部署批准。
- Marketplace listing 不是物理信任。
- Fleet ops 发生在部署后，但买家还需要安装前门禁。

真正可卖的机器人技能必须回答：

- 在哪些 robot profile 上测试过？
- 数据来自哪里？
- 训练、导出和评估过程是否可追踪？
- Qualcomm edge 上延迟、内存、功耗如何？
- 安全边界是什么？
- 哪些安装会被阻止？
- 失败后如何回滚？
- 谁负责支持？

## Solution

SkillCertKit 生成一个 `digest-addressed evidence bundle`，作为 SkillDock 上架前门禁。

核心输出：

- `skill.yaml`：任务边界、传感器、执行器、权限、runtime、目标 robot profile。
- Dataset / model lineage：LeRobot dataset、episode、失败样本、license、训练版本、评估报告。
- Hardware compatibility：processor、camera、arm/gripper、payload、firmware、安全 IO、calibration。
- Qualcomm edge profile：AI Hub / QNN / QAIRT compile/profile/deploy evidence，latency、memory、thermal、fallback。
- Trust gates：SBOM、license、VEX、漏洞、签名、安装条件、安全边界、人工接管、rollback plan。
- Evidence levels：`simulated`、`hardware_in_loop`、`bench_real`、`field_real`。

## Evidence Architecture

根对象是：

```text
skill_id:version@sha256
```

可以借鉴 OCI artifact / image index，把模型、容器、`skill.yaml`、model card、dataset card、SBOM、VEX、签名、SLSA/in-toto provenance、edge profile、safety evidence、policy decision 和 rollback metadata 作为 referrers 绑定到同一个 digest。

## Evidence Artifacts

- `skill.yaml`
- `model-card.md`
- `dataset-card.md`
- `lerobot-lineage.json`
- `provenance.intoto.jsonl`
- `sbom.cdx.json`
- `sbom.spdx.json`
- `vex.openvex.json`
- `signature.bundle`
- `hardware-profile.yaml`
- `edge-profile.qualcomm.json`
- `safety-boundary.yaml`
- `runtime-constraints.yaml`
- `opa-input.json`
- `policy-decision.json`
- `tuf-metadata/`
- `rollback-plan.yaml`
- `install-audit-log.jsonl`
- `claim-boundaries.md`

## Policy Gates

最小门禁：

1. 验证 root artifact 和 required referrers 的签名。
2. SLSA / in-toto provenance 的 subject digest 必须匹配 skill package。
3. SBOM 必须存在；blocking license / CVE 需要 VEX 或修复说明。
4. Robot profile 必须满足 sensors、actuators、firmware、calibration、安全 IO 和 edge target。
5. Evidence level 必须满足发布要求。
6. Safety boundary 必须包含 e-stop、takeover、fail-closed、workspace、max speed/force、forbidden actions。
7. Runtime constraints 拒绝 privileged container、host path、unconfined seccomp、额外设备和未管理网络出口。
8. Rollback metadata 必须声明 previous-known-good digest 和触发阈值。

## Market

第一批客户不是消费者，而是为“部署信任”付费的人：

- Skill developers / ISVs：让技能可销售。
- Robot OEMs：让自己的硬件生态更有用。
- System integrators：减少每个客户的重复验证。
- RaaS / fleet operators：每个技能更新都影响 uptime、支持负担、责任和 redeploy speed。
- Enterprise IT / Security / EHS：需要 SBOM、漏洞流程、数据流、rollback、audit、procurement material。
- Education / research labs：需要 open dev tier、课程、可重复实验和技能证据训练。

Beachhead：

- `labforge.sample-transfer.v1`
- vision grasping
- AMR inspection
- visual tracking
- light QA
- 教育实验任务

## Business Model

先卖 evidence pack，再开技能市场。

建议价格层：

- Open Dev Tier：免费到 `$499/skill`。
- Marketplace Ready Pack：`$2.5k-$12k/skill`。
- Additional Robot/Profile Test：`$1k-$5k/profile`。
- Bench/Lab Validation：`$15k-$60k/skill/profile`。
- Field Evidence Pack：`$25k-$150k/workflow/site`。
- Enterprise Trust Pack：`$10k-$50k` add-on。
- Private Skill Library：`$25k-$150k/year/site`，大型项目 `$150k-$500k/year`。
- Per-Robot Runtime Gate：`$25-$250/robot/month`。
- SkillDock marketplace take：公开技能 10%-20%，大型私有交易/服务 3%-5%。

商业顺序：

1. Sell SkillCertKit evidence packs。
2. 用 evidence packs 生成可信 SkillDock cards。
3. 卖 private SkillDock libraries 给 OEM、SI、RaaS 和 enterprises。
4. 有足够 validated supply 后，再开 curated public marketplace。
5. 通过 recertification、private libraries、per-robot runtime gates、support subscriptions 和 transaction take 形成经常性收入。

## Competition

不能说“第一个机器人 App Store”。

SkillCertKit 不替代：

- ROS / ROS-Industrial；
- LeRobot；
- NVIDIA Isaac / GR00T；
- Viam Registry / Fleet；
- Foxglove / Formant；
- Intrinsic Flowstate；
- UR+ / MiR Go / KUKA Creator Portal；
- UL / TUV / Intertek 等正式认证实验室。

SkillCertKit 的准确位置：

> profile-scoped robot-skill evidence package for marketplace review, enterprise procurement, safety-case preparation, cybersecurity review, and regional compliance readiness.

它不是法律认证机构，不声称正式安全/法规认证。

## Moat

护城河是技能证据网络：

- skill manifests；
- robot profiles；
- dataset lineage；
- model lineage；
- benchmark reports；
- failure episodes；
- safety boundaries；
- version histories；
- buyer acceptance records；
- Qualcomm edge profiles；
- recertification triggers。

每个技能都会沉淀：

```text
skill x dataset x model x robot profile x sensor x runtime x Qualcomm target x safety boundary x field failure
```

越多技能通过，兼容矩阵越准；越多失败和回滚被记录，认证规则越强；越多 Qualcomm profile 被采用，Dragonwing 越像机器人技能分发默认目标。

## Qualcomm Ask

请求 Qualcomm 支持 6-8 周 “Dragonwing SkillCertKit Validation Sprint”：

1. 确认比赛阶段 target path：RB3 Gen 2 / QCS6490 先跑通，QCS8550 或 IQ10 RRD 作为生产路线。
2. AI Hub / QNN / QAIRT / Device Cloud quota，用于 2-3 个 reference skills。
3. 每周 QNN / QAIRT office hour，生成一个真实 QNN DLC / context binary 或 ONNX Runtime QNN artifact。
4. 共同定义轻量 `Dragonwing Skill Profile v0.1`。
5. 支持 2-3 个 reference skills：vision grasping、AMR inspection、visual tracking 或 quality inspection。
6. 引荐教育 kit、SI、AMR/arm OEM、Dragonwing module partner。
7. 对外口径使用 `Dragonwing-profiled` 或 `Qualcomm-edge-ready candidate`，不称官方认证。

## Demo Plan

3 分钟演示：

1. 打开 `labforge.sample-transfer.v1`。
2. 展示 `skill.yaml`、LeRobot lineage、model hash、SBOM、VEX、license、signature。
3. 运行 SkillCertKit gate，生成 Qualcomm AI Hub / QNN profile 和 latency / memory evidence。
4. 选择不兼容 robot profile，安装被阻止并解释原因。
5. 选择兼容 Qualcomm target，允许 staged rollout 到一台设备。
6. 模拟 safety event 或 health check failure，回滚到 previous-known-good。
7. 自动生成 SkillDock 技能卡：兼容范围、证据等级、价格、支持方、claim boundaries。

## Claim Boundaries

可以声称：

- profile-scoped robot-skill evidence package。
- marketplace-readiness workflow。
- standards-aware evidence mapping。
- safety-case preparation support。
- cybersecurity / procurement review support。
- Qualcomm-edge-ready candidate workflow。

不能声称：

- official Qualcomm certification。
- Qualcomm partnership / endorsement。
- ISO 10218 certified skill。
- ISO/TS 15066 compliant model。
- CE certified / Machinery Regulation compliant / CRA compliant。
- IEC 62443 certified / ISO 27001 compliant / NIST certified。
- safe for all robots。
- universal robot compatibility。
- zero-risk deployment。
- SBOM means secure。
- all LeRobot / ACT / VLA models compile to QNN without changes。
- simulated metrics are measured hardware results。

Use `tested_on`、`expected_compatible`、`not_validated`，and label evidence as `simulated`、`hardware_in_loop`、`bench_real`、`field_real`。

## Sources

- Universal Robots Marketplace：https://www.universal-robots.com/marketplace/
- MiR Go：https://mobile-industrial-robots.com/products/mir-go
- LeRobot：https://huggingface.co/docs/lerobot/en/index
- ROS Index：https://index.ros.org/
- OCI image/distribution 1.1：https://opencontainers.org/posts/blog/2024-03-13-image-and-distribution-1-1/
- SLSA v1.2：https://slsa.dev/spec/v1.2/
- in-toto：https://in-toto.io/
- CycloneDX：https://cyclonedx.org/specification/overview/
- Open Policy Agent：https://openpolicyagent.org/docs
- TUF：https://theupdateframework.github.io/specification/latest/
- ISO 10218-1：https://www.iso.org/standard/73933.html
- ISO/TS 15066：https://www.iso.org/standard/62996.html
- NIST SSDF SP 800-218：https://csrc.nist.gov/pubs/sp/800/218/final
- Qualcomm AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm Profiler：https://www.qualcomm.com/developer/software/qualcomm-profiler
- Qualcomm Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
