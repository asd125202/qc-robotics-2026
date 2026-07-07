# SafetyOps Pitch

更新时间：2026-07-07。本页按 YC / Airbnb 风格重写：问题、现有替代方案为什么失败、解决方案、为什么现在、产品、API/证据、市场、竞争壁垒、为什么 Qualcomm、演示和请求。

## One-Line Pitch

SafetyOps 是机器人技能上线前的 release gate 与 evidence governance layer：让每次模型/技能/远程协助/OTA 变更都有权限、ODD、安全包络、Qualcomm edge profile、SBOM/VEX、command admission、事故回放、回滚和客户/保险/审计证据。

## Thesis

机器人商业化不是从“能动”开始，而是从“客户敢让它动”开始。

企业不是怕机器人不聪明，而是怕策略不可控：

> 谁能让机器人动？它能动到哪里？出了事如何证明当时发生了什么？下一次发布为什么可以继续？

SafetyOps 的定位不是认证机构、不是 safety PLC、不是 CE/GB/ISO 合规保证。它是机器人团队的：

> audit-ready release evidence layer for physical AI.

## 01 · Problem

Demo 阶段只要机器人能动；生产阶段客户会问完全不同的问题：

- 这个技能是谁批准的？
- 它能读哪些传感器、写哪些 ROS/DDS topic、控制哪些执行器？
- 它在哪个 ODD、速度、区域、人机距离、payload、网络和传感器状态下允许运行？
- 远程接管是谁发起的、谁批准的、允许哪些命令、持续多久、有没有录像和命令日志？
- 事故后如何证明模型版本、传感器状态、QNN runtime、命令、停机、人工接管和回滚？
- 客户、EHS、保险、RaaS financier、认证顾问和比赛评委能否看懂这些证据？

OSHA 机器人安全资料长期强调，很多机器人事故发生在 programming、maintenance、testing、setup、adjustment 等非正常/变更状态，而不是稳定生产状态。SafetyOps 的核心痛点正是 production change control。

一句话：机器人公司缺的不是更多 dashboard，而是每次 robot skill 变更的责任链。

## 02 · Current Alternatives Fail

现有方案都重要，但没有把“模型变更 -> 远程接管 -> 现场命令 -> 事故证据 -> 回滚 -> 审计包”串成产品链路。

### Safety PLC / Certified Controller

认证安全控制器保护机器和产线，仍然是必要组件。但它通常不记录 AI model lineage、dataset hash、AI Hub / QNN profile、skill approval、SBOM/VEX、remote-assist session 或 customer audit pack。

### PDF / Spreadsheet Risk Assessment

风险评估表和验收文档能支撑项目交付，但部署后跟不上模型更新、OTA、site config、漏洞处置和 incident replay。

### Fleet Ops

Formant、InOrbit、Viam、OEM fleet portals 管 telemetry、teleop、fleet workflows 和 incident，但不是以 release gate、command authorization、standards evidence 和 insurer/customer audit pack 为核心。

### Robot Logs

Foxglove、MCAP、ROS bag 很适合工程调试，但还需要 approval、permission、rollback、SBOM/VEX、remote-access evidence、chain-of-custody 和客户可读 summary。

### AI Governance / GRC

Credo、IBM、Holistic、传统 GRC 工具理解模型风险和企业流程，但通常不理解 ROS topic、执行器、E-stop、ODD、QNN runtime、sensor health、edge latency 和 physical incident replay。

### Cybersecurity Tools

OT security、SBOM、vulnerability、remote access 工具能回答一部分 cyber 问题，但不回答 “这个 learned policy 今天是否应该移动这个 actuator”。

SafetyOps 的 wedge：机器人技能发布的安全证据，而不是通用 fleet management。

## 03 · Solution

SafetyOps = `Skill Release Safety Gate + Remote Assist Governance + Runtime Evidence Vault + Audit Pack Builder`。

每个 robot skill 上线前必须声明和验证：

- permissions：sensors、actuators、ROS/DDS topic/service/action allow-deny。
- ODD：地图、区域、速度、force、payload、人机距离、keepout、sensor required、network/thermal limits。
- model evidence：dataset hash、eval split、HIL clips、replay regressions、failure tags。
- Qualcomm edge profile：AI Hub job、QAIRT/QNN runtime、latency、memory、backend、numeric delta、fallback。
- release evidence：SBOM、VEX、signature、approvals、canary scope、rollback target。
- remote assist：operator identity、MFA、device posture、reason、command scope、expiry、dual approval for high-risk action。

运行时，边缘 agent 做四件事：

1. **Command admission**：只允许策略批准的命令路径，例如 `/safety/cmd_vel_limited`，拒绝 raw `/cmd_vel` 或未授权 arm trajectory。
2. **Boundary monitoring**：检查 ODD、sensor health、frame age、thermal、network、QoS deadline、human/zone proximity。
3. **Incident capture**：写入 MCAP/video/runtime ring buffer、access-session evidence、policy decision 和 signed event ledger。
4. **Rollback proof**：停用策略、切回 previous-known-good、记录 action、生成客户/保险/评委可读证据包。

边界必须清楚：

> No cloud in the safety loop. SafetyOps supports evidence, policy, monitoring, and bounded command admission; certified safety functions remain with the robot OEM/integrator safety architecture.

## 04 · Why Now

四个压力同时到点：

### 4.1 Robot Scale

IFR 2025 显示 2024 年全球工业机器人新增安装约 542,000 台，连续第四年超过 500,000 台；专业服务机器人 2024 年销量接近 200,000 台，RaaS fleets 增长 31%。机器人已经进入客户现场，事故证据和变更治理变成商业问题。

### 4.2 AI Skill Updates

LeRobot、VLA、diffusion policy、视觉语言模型和 cloud training 让 robot skill 迭代更快。迭代越快，企业越需要 release gate、ODD、eval、remote-assist evidence 和 rollback。

### 4.3 Regulation And Standards

- EU Machinery Regulation (EU) 2023/1230 将于 2027-01-20 适用，强化 risk assessment、technical documentation、software safety functions 和 cybersecurity/protection against corruption。
- EU Cyber Resilience Act reporting obligations 从 2026-09-11 开始，主体义务 2027-12-11 适用，SBOM、vulnerability handling、security updates 和 technical documentation 变得更重要。
- EU AI Act 可能在 safety component / high-risk 产品路径上影响机器人 AI，具体义务需按系统范围判断。
- ISO 10218-1/2:2025、ISO 13849-1、IEC 61508、ISO 3691-4、ANSI/RIA R15.08、GB 11291.1/2、GB/T 15706、GB/T 16855.1 都让 safety evidence workflow 成为真实采购语言。

### 4.4 Cyber-Physical Remote Operations

机器人 fleet 是 cyber-physical OT system，不是普通 IoT。NIST Zero Trust、NIST SP 800-82 OT security、IEC 62443、CISA remote access、SBOM/VEX、China vulnerability rules 都指向同一个需求：证明谁能接入、能做什么、运行什么软件、事件后有什么证据。

## 05 · Product

第一版只做一个强 wedge：`Skill Release Safety Gate`。

### 5.1 SkillManifest

- skill id、version、risk level。
- sensors / actuators / ROS-DDS allow-deny。
- ODD、speed、force、workspace、keepout、human distance。
- required sensors、network mode、thermal/power limits。
- rollback target、support boundary、known limitations。

### 5.2 ReleaseGate

- dataset hash、eval split、success/intervention/failure metrics。
- HIL clips、replay regression、incident replay comparison。
- AI Hub / QAIRT / QNN profile、runtime artifact、numeric delta、fallback check。
- SBOM/VEX snapshot、signature、approvals、canary/rollout rules。

### 5.3 RemoteAssist Governance

- JIT access approval、MFA、operator device posture。
- per-robot / per-site command scope。
- session TTL、dual approval、break-glass reason、vendor isolation。
- session video/log pointer、command log、robot state snapshots。

### 5.4 Safety Agent

运行在 ROS 2 stack 旁，或者站点边缘 gateway：

- observes topics/actions/services。
- checks ODD and sensor trust。
- denies unauthorized command path。
- monitors thermal/power/network/QoS。
- records ring buffer and signed event evidence。

它不是认证安全控制器；它是 runtime evidence and policy guardrail。

### 5.5 Robot Evidence Vault

- tamper-evident event ledger。
- access decisions。
- teleop sessions。
- OTA history。
- SBOM/VEX status。
- incident capsule。
- chain-of-custody metadata。
- audit pack export。

### 5.6 Standards Map

把 evidence 映射到 selected clauses / readiness checklists：

- EU Machinery Regulation。
- ISO 10218-1/2。
- ISO 13849-1。
- IEC 61508 / IEC 62061。
- ISO 3691-4。
- GB 11291.1/2。
- GB/T 15706。
- GB/T 16855.1。
- NIST SP 800-82 / SP 800-207 / SP 800-61。
- IEC 62443。
- EU CRA。

输出必须写明：support readiness，不等于 certification。

## 06 · Product API/Evidence

SafetyOps 的可信度来自 API 和 artifact，而不是“安全”这个词。

### APIs

```text
POST /v1/skills:submit
POST /v1/releases/{id}:evaluate
POST /v1/releases/{id}:approve
POST /v1/access-sessions
POST /v1/robots/{id}/commands:authorize
GET  /v1/robots/{id}/cyber-posture
GET  /v1/releases/{version}/sbom
GET  /v1/vulnerabilities/{cve}/vex
POST /v1/incidents
POST /v1/replay-tests
POST /v1/rollbacks
POST /v1/incidents/{id}/evidence-pack
GET  /v1/audit-packs/{id}.zip
```

### Skill Manifest Example

```yaml
skill.manifest.v1:
  skill_id: dock-assist
  version: 2.0.0
  risk_level: medium
  permissions:
    sensors: [front_rgb, depth, imu, wheel_odom]
    actuators: [base_velocity]
    ros_allow:
      publish: [/safety/cmd_vel_limited]
      subscribe: [/camera/front, /tf, /odom, /safety/state]
      deny: [/cmd_vel, /motor/raw, /estop/reset]
  odd:
    zones: [lab_demo_map_v3]
    max_speed_mps: 0.35
    keepout_layers: [human_zone, judge_table]
    min_human_distance_m: 1.2
    required_sensors: [front_rgb, depth]
  model:
    digest: sha256:...
    runtime: qnn_context_binary
    rollback_to: dock-assist@1.9.4
```

### Release Gate Example

```json
{
  "release_gate.v1": {
    "release_id": "rel_safetyops_2026_07_001",
    "dataset_hash": "sha256:...",
    "edge_profile": {
      "ai_hub_job_id": "hub_profile_...",
      "target_device": "Dragonwing RB3 Gen 2 Vision Kit",
      "runtime": "QAIRT/QNN",
      "latency_p95_ms": 28,
      "peak_memory_mb": 214,
      "compute_units": ["NPU"],
      "fallback_detected": false
    },
    "remote_assist": {
      "requires_mfa": true,
      "max_session_ttl_min": 15,
      "allowed_commands": ["/safety/cmd_vel_limited"],
      "dual_approval_for": ["estop_reset", "map_change", "ota_rollout"]
    },
    "decision": "allow_canary",
    "rollback": "dock-assist@1.9.4"
  }
}
```

### Evidence Pack

- `skill.manifest.yaml`
- `release_gate.json`
- `qualcomm_edge_profile.json`
- `runtime_policy.json`
- `sbom.cdx.json`
- `vex.json`
- `access_session_log.jsonl`
- `command_authorization_log.jsonl`
- `incident_timeline.jsonl`
- `mcap_replay_pointer.json`
- `rollback_receipt.json`
- `standards_map.csv`
- `claim_boundaries.md`

## 07 · Market & Business Model

卖给 OEM 的是更快进 pilot；卖给企业的是更少部署风险；卖给保险/RaaS 的是可核验风险证据。

### First Buyers

- Robot OEM / RaaS operator：CTO、VP Safety、VP Product、customer success。
- Enterprise deployer：EHS、automation engineering、OT security、legal/risk、procurement。
- System integrator：需要标准化验收和责任边界。
- Insurer / RaaS financier：需要 signed telemetry、incident replay、risk scoring。

### China Version

- 产品语言：机器人事故黑匣子、出海验收证据、GB/T readiness、数据驻留、私有化、国内云/SI 交付。
- 定价假设：人民币 50k-150k / site-year + 人民币 50-200 / robot / month；formal release / audit pack 另收费。
- 更大 OEM / 多站点：人民币 200k-800k / year。

### Global Version

- 产品语言：compliance-ready evidence layer、remote-assist governance、insurance-ready incident record。
- 定价假设：$25k-$100k / site-year + $20-$100 / robot / month。
- OEM/SI release pack：$2k-$10k / formal release。
- RaaS / insurer API：2%-5% of robot subscription 或 $20-$150 / robot / month。

### ROI

- 减少 release review 时间。
- 减少 warranty / SLA disputes。
- 提高 enterprise customer trust。
- 支持 insurer / financier underwriting and claims review。
- 避免一次事故、停线或罚款带来的不确定损失。

## 08 · Competition & Moat

竞争证明需求真实；SafetyOps 的位置是 physical AI release evidence。

### Adjacent Players

- FORT / 3Laws：runtime safety control。
- Veo / Symbotic：robot safeguarding。
- NVIDIA Halos：NVIDIA-first physical AI safety stack。
- Formant / InOrbit / Viam：fleet ops、teleop、incident。
- Foxglove / MCAP：robot data、replay、search。
- Siemens / Rockwell / Pilz / SICK：certified safety hardware。
- TÜV / UL / Intertek / Edge Case Research：certification、assurance、safety cases。
- IBM / Credo / Holistic：AI governance。
- SBOM / OT security vendors：cyber inventory and risk。

### Moat

短期：

- Skill permission / ODD manifest templates。
- Qualcomm AI Hub / QAIRT / QNN profile as release evidence。
- ROS 2 / DDS command admission recipes。

中期：

- Cross-OEM safety event schema。
- Hazard / skill library for dock assist、pick、carry、clean、patrol、elevator、charging。
- Remote-assist evidence vault and access-session replay。
- SBOM/VEX + physical incident pack。

长期：

- Insurer-readable robot risk ledger。
- China/overseas trust shells with same schema but separate data, key, log, and identity boundaries。
- Field incident dataset that improves SkillCertKit、EdgeFleet、TrainRouter and Qualcomm reference workflows。

## 09 · Why Qualcomm

Qualcomm 不只需要机器人跑 AI，还需要 AI 策略能被批准上线。

SafetyOps 把 Qualcomm edge 从推理目标升级成 physical AI release target：

- AI Hub / QAIRT / QNN profile 进入 release gate。
- Dragonwing device identity 签署 edge evidence。
- RB3 / QCS / IQ target 记录 latency、memory、thermal、sensor trust、runtime artifact 和 fallback。
- IQ10 RRD 的 sensor interfaces、domain separation、deterministic I/O、EtherCAT、CAN-FD、TSN、Wi-Fi 7 / 5G 让“local-first safety evidence”更可信。
- Qualcomm Linux / secure boot / OTA / key management / workload isolation 可支撑 signed rule bundle、rollback 和 event custody。

Qualcomm 获得的价值：

- 不只是展示 TOPS，而是展示 production readiness。
- 帮 OEM、SI、企业客户理解 Qualcomm-ready robot release evidence。
- 与 DragonWorks、EdgeRuntimeBench、SkillCertKit、SkillDock、EdgeFleet 串成完整 edge AI lifecycle。
- 对 NVIDIA/Jetson-first robotics safety narrative 形成 Qualcomm-first reference workflow。

## 10 · Demo & Ask

八分钟 demo：`dock-assist-v2` 被门禁拦截、限权上线、触发 incident、再回滚。

### Demo Flow

1. 上传 `dock-assist-v2` skill card：permissions、ODD、risk、rollback。
2. Gate 拦截：缺少 human-proximity validation / HIL / replay evidence。
3. 补齐 evidence：dataset hash、replay pass、HIL clips、SBOM、VEX、approvals。
4. 展示 Qualcomm profile：AI Hub/QNN latency、memory、compute units、fallback status。
5. 创建 JIT remote-assist session：operator identity、MFA、command scope、TTL、approver。
6. Canary 部署：DDS policy 拒绝 raw `/cmd_vel`，只允许 `/safety/cmd_vel_limited`。
7. 触发 keepout / QoS deadline miss / camera stale：机器人 slow/stop，ledger 记录。
8. 打开 MCAP replay，对比 v1/v2，失败片段进入 LeRobot/HIL queue。
9. 一键 rollback，生成 `judge-audit-pack.zip`。
10. 切换 China / Global trust shell：raw video stays regional，only hashes/summary cross-region。

### Qualcomm Ask

- Hardware：RB3 Gen 2 / QCS6490，QCS8550-class board，IQ10 RRD guidance if available。
- Tooling：AI Hub / QAIRT / QNN profile quota and office hours。
- Platform：Dragonwing device identity / secure boot / OTA / runtime evidence guidance。
- Ecosystem：1-2 robot OEM/SI pilot introductions。
- Output：SafetyOps as Qualcomm-edge physical AI release gate reference workflow for the competition.

### Claim Boundaries

可以说：

- SafetyOps helps teams prepare audit-ready release evidence。
- Supports CE / GB / ISO readiness workflows。
- Maps selected requirements, hazards, tests, logs, and changes to evidence。
- Provides local-first runtime evidence and command admission guardrails。
- Helps organize CRA / SBOM / VEX / remote-access evidence。

不能说：

- certifies robots。
- guarantees safety。
- replaces safety PLC, E-stop, scanner, STO, risk assessment, notified body, TÜV/UL/Intertek, or legal compliance review。
- proves PL/SIL compliance。
- makes robots NIST / IEC 62443 / CRA / EU AI Act compliant。
- remote operation is safe because it uses VPN。
- SBOM means secure。

## Sources

- OSHA Robotics：https://www.osha.gov/robotics
- OSHA Penalties：https://www.osha.gov/penalties
- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- EU Machinery Regulation：https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng
- EU AI Act：https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- EU Cyber Resilience Act：https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EU CRA summary：https://digital-strategy.ec.europa.eu/en/policies/cra-summary
- ISO 10218-1:2025：https://www.iso.org/standard/73933.html
- ISO 10218-2:2025：https://www.iso.org/standard/73934.html
- ISO 13849-1：https://www.iso.org/standard/73481.html
- IEC Functional Safety：https://iec.ch/functional-safety
- ISO 3691-4：https://www.iso.org/standard/70660.html
- NIST Zero Trust SP 800-207：https://doi.org/10.6028/NIST.SP.800-207
- NIST OT Security SP 800-82r3：https://doi.org/10.6028/NIST.SP.800-82r3
- NIST Incident Response SP 800-61r3：https://doi.org/10.6028/NIST.SP.800-61r3
- IEC 62443：https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
- CISA SBOM：https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom
- CISA VEX：https://www.cisa.gov/resources-tools/resources/minimum-requirements-vulnerability-exploitability-exchange-vex
- China vulnerability rules：https://www.cac.gov.cn/2021-07/13/c_1627761607640342.htm
- China GB 11291.1：https://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7DB68D3A7E05397BE0A0AB82A
- China GB 11291.2：https://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E933D3A7E05397BE0A0AB82A
- China GB/T 15706：https://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E121D3A7E05397BE0A0AB82A
- ROS 2 Security Enclaves：https://design.ros2.org/articles/ros2_security_enclaves.html
- ROS 2 Security Concepts：https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Security.html
- MCAP ROS 2：https://mcap.dev/guides/getting-started/ros-2
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm AI Hub profile：https://workbench.aihub.qualcomm.com/docs/hub/profile_examples.html
- Qualcomm IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm Linux 2.0：https://www.qualcomm.com/developer/blog/2026/06/qualcomm-linux-2-now-available
- FORT Robotics：https://www.fortrobotics.com/platform
- NVIDIA Halos Robotics：https://www.nvidia.com/en-us/ai-trust-center/halos/robotics/
- Formant：https://formant.io/
- InOrbit：https://www.inorbit.ai/robops
- Foxglove：https://foxglove.dev/
