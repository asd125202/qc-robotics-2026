# SkillCertKit Pitch

更新时间：2026-07-06。本页按 YC / Airbnb 风格重写：问题、现有替代方案为什么失败、解决方案、为什么现在、产品、API/证据、市场、竞争壁垒、为什么 Qualcomm、演示和请求。

## One-Line Pitch

SkillCertKit 是机器人技能安装前的信任门：把一个策略模型、ROS 包或机器人 app 变成 signed Skill Passport，证明它能否在某个命名 robot profile、某个 Qualcomm edge target、某个现场边界下被允许安装、灰度发布和回滚。

## Thesis

机器人技能市场不会先靠 SKU 数量成功。它会先靠信任成功。

Airbnb 的早期信任来自照片、身份、评价和支付保障；机器人技能市场的信任来自证据卡、签名 artifact、SBOM/VEX、数据血缘、硬件兼容、现场边界、安装门禁、审计日志和回滚历史。

SkillCertKit 的定位不是“官方认证机构”，而是 `skill exists` 到 `skill may run here` 之间的 CI/CD trust gate。

## 01 · Problem

企业不会把陌生模型随手装进真实机器人。

一个技能 demo 能跑，不代表它适合买家的相机、机械臂、夹爪、AMR、runtime、网络、安全 IO、数据权限和现场边界。普通 App 崩溃是软件问题；机器人技能失败会影响设备、人员、现场和责任。

今天的真实问题：

- Skill developer 很难把同一个技能卖给第二个客户，因为没有兼容矩阵和证据包。
- System integrator 每个项目都重复验证相机、payload、速度、工作空间、网络、回滚和安全接管。
- Enterprise IT / EHS / Security 无法审计依赖、漏洞、数据流、权限、签名和升级策略。
- Fleet operator 每次升级都担心 uptime、责任边界和回滚。
- SkillDock 如果只有“下载按钮”，会变成高风险模型仓库。
- Qualcomm edge value 不会沉淀，除非每个技能都声明并验证 target profile。

一句话：没有安装前信任门，机器人技能就无法像软件一样分发。

## 02 · Current Alternatives Fail

### Robot App Store

“机器人 app store”不是新概念。历史上已经有 RobotAppStore，今天也有 humanoid、consumer、education 和开源机器人 app store。它们证明需求存在，但大多缺少工业级 safety evidence、site-specific approval、rollback policy 和企业采购包。

### OEM Ecosystem

UR+、MiR Go、KUKA iiQKA、FANUC CRX、ABB RobotStudio/AppStudio 都证明买家愿意相信被测试过的生态产品。问题是这些信任通常锁在单一 OEM 里，更多是附件、插件、组件或集成工具，而不是跨机器人、跨 skill、跨现场的证据层。

### ROS / MoveIt / LeRobot

ROS、MoveIt 和 LeRobot 是重要底座，但包、模型和数据集本身不会自动回答：能不能装在这个客户现场？是否有 SBOM？是否能回滚？是否匹配相机和安全 IO？是否通过 Qualcomm target profile？

### Fleet Ops / Observability

Viam、Formant、InOrbit、Foxglove 能告诉你机器人部署后发生了什么；SkillCertKit 要解决的是部署前是否允许发生。

### Simulation / Physical AI Stack

NVIDIA Isaac、GR00T、Cosmos、Intrinsic Flowstate 等帮助创建、仿真、训练或部署技能；但仿真通过不等于生产安全，模型可运行不等于企业可采购。

### Formal Certification Labs

UL、TUV、Intertek、A3 / integrator certification 等非常重要，但它们不会替代每个 skill release 的日常证据、版本、签名、SBOM、profile gate 和 rollback metadata。

## 03 · Solution

SkillCertKit 生成一个 `Skill Passport`：一个 digest-addressed, signed, profile-scoped evidence bundle。

它回答 6 个安装前问题：

1. 这个技能是什么任务，边界在哪里，哪些动作禁止？
2. 它来自哪些数据、训练、模型、代码和构建流程？
3. 它依赖哪些 ROS 包、容器、系统库、模型 runtime、网络和设备权限？
4. 它在哪些 robot profile、相机、执行器、固件、calibration 和安全 IO 上测试过？
5. 它在 Qualcomm edge target 上的 latency、memory、thermal、fallback 和 unsupported-op 状态如何？
6. 如果安装失败、health check 失败或现场事件发生，如何阻止、降级、回滚和审计？

输出不是“永久安全证书”，而是安装前可执行门禁：

- `allow`：允许 staged rollout。
- `warn`：需要人工确认或现场 commissioning。
- `block`：缺证据、不兼容、风险过高或违反客户 policy。

## 04 · Why Now

四个趋势让 SkillCertKit 现在值得做：

1. **机器人装机基数足够大**：IFR 2025 显示 2024 年全球工业机器人新增安装约 542,000 台，专业服务机器人接近 200,000 台，物流 RaaS 也在增长。
2. **技能正在软件化**：LeRobot、DROID、Open X-Embodiment、VLA、ACT、sim-to-real 和 cloud training 让策略模型更容易复用，但复用前需要 trust gate。
3. **采购和法规正在要求软件证据**：SBOM/VEX、NIST SSDF、EU Machinery Regulation 2023/1230、EU Cyber Resilience Act、EU Product Liability Directive、AI Act 风险文档，都把软件更新、AI 模型和责任边界推到采购前台。
4. **Qualcomm 正在从芯片走向机器人 reference platform**：Dragonwing / RB3 / AI Hub / QNN / QAIRT / Robotics Hub / IQ10 RRD 都需要一个 release-gate layer，把工具链产物变成技能上架证据。

这不是“再做一个市场”；这是在市场形成前先补信任基础设施。

## 05 · Product

### 5.1 Skill Submit

开发者提交：

- policy/model/container/ROS package。
- `skill.yaml`。
- task boundary。
- target robot profiles。
- required sensors / actuators。
- permissions。
- evidence level。
- support owner。

### 5.2 Evidence Builder

系统绑定：

- LeRobot / TeleopStudio / CloudTwin lineage。
- model card、dataset card、eval report。
- SPDX / CycloneDX SBOM。
- VEX / VDR。
- SLSA / in-toto provenance。
- Sigstore/cosign signature。
- TUF/Uptane-style update metadata。
- Qualcomm AI Hub / QNN / QAIRT edge profile。

### 5.3 Gate Engine

按 robot profile、site、region、customer policy 运行门禁：

- signature。
- dependency/license/vulnerability。
- safety boundary。
- runtime constraints。
- hardware compatibility。
- edge performance。
- data-region rule。
- rollout/rollback readiness。

### 5.4 Skill Passport

生成面向 SkillDock、企业采购、SI、OEM 和 insurer 的人类可读 + 机器可读证据室。

### 5.5 Runtime Gate

安装前 preflight，安装后 staged rollout，健康阈值触发 rollback 和 recertification。

## 06 · Product API/Evidence

### Core API

```text
POST /v1/skills:submit
POST /v1/skills/{digest}/sbom
POST /v1/skills/{digest}/vex
POST /v1/skills/{digest}/provenance
POST /v1/skills/{digest}/model-evidence
POST /v1/gates:evaluate
POST /v1/install:preflight
POST /v1/rollouts
POST /v1/rollbacks
GET  /v1/skills/{digest}/evidence
GET  /v1/audit-log?skill=&robot=&site=
```

### Skill Passport Object

```json
{
  "skill": "labforge.sample-transfer.v1",
  "digest": "sha256:7d8f...",
  "evidence_level": "bench_real",
  "target_profile": "dragonwing-rb3-qcs6490-vision-v1",
  "robot_profile": "single-arm-lab-cell-v1",
  "task_boundary": "move labeled vial from tray A to rack B",
  "forbidden_actions": ["uncapped needle handling", "human-proximity operation"],
  "lineage": {
    "dataset": "lerobot://org/sample-transfer-v3@sha256:...",
    "training_job": "trainrouter://job_20260706_0912",
    "model": "sha256:..."
  },
  "supply_chain": {
    "sbom": "cyclonedx-1.7",
    "provenance": "slsa-v1.2",
    "signature": "sigstore-bundle"
  },
  "qualcomm_edge": {
    "ai_hub_job": "job_ref",
    "qnn_artifact": "sha256:...",
    "latency_p95_ms": 10,
    "memory_peak_mb": 20,
    "profile_scope": "model inference only"
  },
  "gate": {
    "decision": "allow",
    "rollout": "one-robot-canary",
    "rollback": "previous-known-good"
  }
}
```

### Evidence Artifacts

- `skill.yaml`
- `skill-passport.json`
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
- `policy-decision.json`
- `tuf-metadata/`
- `rollback-plan.yaml`
- `install-audit-log.jsonl`
- `claim-boundaries.md`

### Evidence Levels

- `simulated`
- `hardware_in_loop`
- `bench_real`
- `site_real`

兼容标签必须区分：

- `tested_on`
- `expected_compatible`
- `not_validated`

## 07 · Market & Business Model

第一批客户不是消费者，而是为部署信任付费的人。

### Beachhead

最好的 wedge 是 lab automation sample transfer / light QA：工作空间受控、文档价值高、安全边界清楚、能用 TeleopStudio 采集、TrainRouter 训练、Qualcomm edge profile 验证、SkillDock 上架。

下一批：

- indoor AMR inspection / logistics。
- cobot vision pick-place。
- machine-tending assist。
- education/research skill supply seeding。

### Overseas GTM

卖给 enterprise EHS/security、RaaS fleets、OEM ecosystem teams、system integrators 和 insurers。证据映射到 NIST SSDF、SBOM/VEX、EU CRA reporting、EU Machinery technical docs、AI Act classification 和 Data Act connected-product data access。

### China GTM

卖给 OEM、SI、园区、实验室、教育套件和数据工厂。口径用“技能上架证据包 / 安装前门禁 / 私有技能库”，不要用“官方认证”。数据平面支持本地/BYOC，证据映射到 GB 11291、GB/T 36530、AGV 安全规范、PIPL、网络数据安全和跨境规则。

### Pricing

- Open Dev：免费到 `$499/skill`。
- Marketplace Ready Pack：`$2.5k-$12k/skill`。
- Additional Robot/Profile Test：`$1k-$5k/profile`。
- Bench/HIL Validation：`$15k-$60k/skill/profile`。
- Field Evidence Pack：`$25k-$150k/workflow/site`。
- Private Skill Library：`$25k-$150k/year/site`，大型 OEM/SI 部署 `$150k-$500k/year`。
- Runtime Install Gate：`$25-$250/robot/month`。
- SkillDock Marketplace Take：公开技能 10%-20%，私有/channel 交易 3%-5%。

### Business Sequence

1. 手工为 10 个技能和 2 个 robot profiles 做证据包。
2. 把重复 review checklist 变成 API。
3. 先卖 private Skill Library 给 OEM、SI、RaaS 和企业。
4. 有足够 validated supply 后，再开 curated public marketplace。
5. 通过 recertification、runtime gate、support subscription 和 marketplace take 形成经常性收入。

## 08 · Competition & Moat

SkillCertKit 不替代：

- ROS / ROS-Industrial / MoveIt Pro。
- LeRobot / TrainRouter / CloudTwin。
- NVIDIA Isaac / GR00T / Cosmos。
- Intrinsic Flowstate。
- Viam / Formant / InOrbit / Foxglove。
- UR+ / MiR Go / KUKA / FANUC / ABB ecosystem。
- UL / TUV / Intertek / A3 / notified body / formal certification labs。

准确位置：

> The CI/CD trust gate for robot skills: a portable evidence layer between “skill exists” and “skill may run here.”

### Moat

短期壁垒：

- `skill.yaml` schema。
- Skill Passport。
- Dragonwing Skill Profile。
- safety boundary templates。
- SBOM/VEX/provenance adapters。
- policy decision engine。

中期壁垒：

- compatibility graph。
- HIL certification recipes。
- partner-integrator acceptance records。
- staged rollout and rollback logs。
- recertification triggers。

长期壁垒：

```text
skill x dataset x model x robot profile x sensor x runtime x edge target x site failure x buyer acceptance
```

越多技能通过，兼容矩阵越准；越多失败和回滚被记录，规则越强；越多 Qualcomm profile 被采用，Dragonwing 越像机器人技能分发默认目标。

## 09 · Why Qualcomm

SkillCertKit 把 Qualcomm 工具链从“模型优化工具”提升成“机器人技能信任标准”。

为什么 Qualcomm 应该支持：

- AI Hub / QNN / QAIRT 已经能产生 compile/profile/inference evidence；SkillCertKit 把这些变成上架字段。
- Dragonwing RB3、QCS6490、QCS8550、IQ-8275、IQ10 RRD 需要一个清晰 target profile matrix，帮助伙伴知道“这个技能在哪个 Qualcomm profile 上可发布”。
- Robotics Hub 可以从 tutorial 变成 reference skill ladder：sample -> profiled candidate -> marketplace-ready evidence。
- Qualcomm 可以避免只讲 TOPS，把 latency、memory、load time、NPU placement、unsupported-op、camera-to-action latency、thermal drift 和 rollback 变成更强生态语言。
- 如果每个技能 release 都带 Qualcomm edge receipt，Dragonwing 会进入机器人 app/skill 生态的分发环节，而不只是部署末端。

### 6-8 Week Validation Sprint Ask

请求 Qualcomm 支持：

- RB3 Gen 2 Vision Kit / QCS6490 开发板和 AI Hub access。
- QNN / QAIRT / ONNX Runtime QNN profile review。
- 2-3 个 reference skills：object detect、visual tracking、sample transfer / light QA。
- 共同定义 `Dragonwing Skill Profile v0.1`。
- telemetry hooks：thermal zones、power draw、NPU/GPU/CPU utilization、QNN profiling、ROS 2 timing trace。
- 审核公开标签：`Dragonwing-profiled candidate` 或 `Qualcomm-edge-ready candidate`，不称官方认证。

### Demo Metrics

- AI Hub model inference latency：标注为 `model inference only`，不可当成完整机器人延迟。
- End-to-end camera-to-ROS-output p95。
- Warm load time。
- Peak memory。
- NPU placement。
- 30-minute sustained run latency drift。
- Frame drop / missed deadline。
- Rollback trigger and recovery time。

## 10 · Demo & Ask

### 3-Minute Demo

1. **0:00-0:25**：打开 `labforge.sample-transfer.v1`，展示一个只有模型文件的高风险状态。
2. **0:25-0:55**：提交 `skill.yaml`：任务边界、相机、机械臂、夹爪、工作空间、权限、目标 robot profile。
3. **0:55-1:25**：生成证据图：LeRobot lineage、model hash、SBOM、VEX、SLSA/in-toto provenance、signature、safety boundary。
4. **1:25-1:55**：运行 gate：不兼容 robot profile 被阻止，原因是相机/固件/安全 IO 或 evidence level 不满足。
5. **1:55-2:25**：切换兼容 Dragonwing profile，展示 AI Hub/QNN evidence、latency、memory、runtime、fallback，并允许 one-robot canary。
6. **2:25-2:45**：模拟 health/safety event，自动 rollback 到 previous-known-good digest。
7. **2:45-3:00**：生成 SkillDock 技能卡：兼容范围、证据等级、价格、支持方、claim boundaries。

### Ask

主办方和 Qualcomm 给我们开发板、AI Hub/QNN 路线 review、profile schema 建议和 reference skill 反馈；我们交付一个可复用样例：从 LeRobot/TrainRouter skill artifact 到 Dragonwing-profiled Skill Passport、安装门禁、灰度发布和回滚证据。

## Claim Boundaries

可以声称：

- profile-scoped robot-skill evidence package。
- marketplace-readiness workflow。
- standards-aligned safety/compliance evidence bundle。
- safety-case preparation support。
- cybersecurity / procurement review support。
- Dragonwing-profiled candidate workflow。
- Qualcomm-edge-ready candidate workflow。

不能声称：

- official Qualcomm certification。
- Qualcomm partnership / endorsement。
- ISO-certified robot skill。
- CE / CRA / AI Act compliant by default。
- IEC 61508 / ISO 13849 SIL/PL certified software。
- safe for all robots。
- universal compatibility。
- simulation-proven means production-safe。
- SBOM means secure。
- insurer-approved。
- China-approved。
- model card means model is safe。
- AI Hub benchmark equals full robot latency。

所有指标必须标注：`simulated`、`hardware_in_loop`、`bench_real`、`site_real`、`model inference only` 或 `end-to-end robot measurement`。

## Sources

- IFR industrial robots 2025：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots 2025：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Universal Robots Marketplace：https://www.universal-robots.com/marketplace/
- KUKA iiQKA certification：https://www.kuka.com/en-us/future-production/iiqka-robots-for-the-people/creator-portal/certification
- FANUC plug-in devices：https://www.fanuc.co.jp/en/product/robot/function/plugindevice/
- ABB AppStudio：https://www.abb.com/global/en/areas/robotics/products/software/appstudio
- Intrinsic Flowstate：https://www.intrinsic.ai/flowstate
- NVIDIA Isaac：https://developer.nvidia.com/isaac
- Viam fleet management：https://www.viam.com/platform/fleet-management
- Formant fleet observability：https://docs.formant.io/docs/fleet-observability
- Foxglove：https://foxglove.dev/
- ROS：https://www.ros.org/
- ROS-Industrial：https://rosindustrial.org/
- MoveIt Pro：https://picknik.ai/pro/
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- ISO 10218-1:2025：https://www.iso.org/standard/73933.html
- ISO 10218-2:2025：https://www.iso.org/standard/73934.html
- ISO 3691-4:2023：https://www.iso.org/standard/83545.html
- ISO 13849-1:2023：https://www.iso.org/standard/73481.html
- EU Machinery Regulation 2023/1230：https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng
- EU Cyber Resilience Act：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- EU Product Liability Directive 2024/2853：https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng
- SPDX 3.0.1：https://spdx.github.io/spdx-spec/v3.0.1/
- CycloneDX：https://cyclonedx.org/specification/overview/
- SLSA v1.2：https://slsa.dev/spec/v1.2/
- in-toto：https://in-toto.io/
- Sigstore cosign：https://docs.sigstore.dev/quickstart/quickstart-cosign/
- TUF：https://theupdateframework.github.io/specification/latest/
- Uptane：https://uptane.org/docs/2.1.0/standard/uptane-standard
- NIST SSDF SP 800-218：https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SP 800-218A：https://www.nist.gov/publications/secure-software-development-practices-generative-ai-and-dual-use-foundation-models-ssdf
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
