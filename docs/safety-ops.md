# SafetyOps Pitch

更新时间：2026-07-06。该版本按 YC / Airbnb 风格 pitch spine 重写：先讲 robot skill / model 变更为什么阻塞商业部署，再讲现有工具缺口、解决方案、为什么现在、产品、商业模式、竞争壁垒、为什么 Qualcomm、比赛演示和 claims guardrails。

## One-Liner

SafetyOps 是机器人模型和技能上线前的安全门禁：

> 谁批准、能控制什么、在哪些场景运行、失败后如何停用、证据如何交给客户、认证和保险。

更具体：

> 把技能权限、ODD、安全包络、模型证据、ROS/DDS 指令边界、事故账本、回放测试和回滚变成企业可验收的产品流程。

## 1. Problem

企业不是怕机器人不聪明，而是怕策略不可控。

Demo 阶段只要机器人能动；生产阶段必须回答：

- 这个模型是谁批准的？
- 它可以控制哪些传感器、执行器、ROS/DDS topic 和服务？
- 它在哪个 ODD 生效？
- 出现 human proximity、越界、延迟飙升、传感器失效、网络异常时如何停用？
- 事故后如何证明模型版本、权限、传感器状态、命令、停机、人工接管和恢复动作？
- 证据如何给客户、EHS、认证实验室、保险、RaaS financier 和评委看？

痛点不是 “robot safety training”，而是 production change control。

## 2. Current Alternatives Fail

今天的工具各管一层，但没人把“模型变更到现场事故”串成证据链。

- PDF / spreadsheet risk assessment：不跟模型版本、skill permissions、OTA、site config 和现场日志联动。
- Safety PLC / certified controller：保护机器和产线，但不记录 AI model lineage、dataset、QNN profile、skill approval 和 release decision。
- Fleet ops：Formant、InOrbit 管 telemetry、incident、teleop 和 fleet workflows，但不是以 release gate / safety-case evidence 为核心。
- Robot logs：Foxglove、MCAP、ROS bag 很适合调试，但还需要权限、审批、回滚和客户可读 audit pack。
- AI governance：Credo、IBM、Holistic 等管数字 AI 风险，但通常不理解 ROS topics、执行器、E-stop、ODD、边缘延迟和 physical incident replay。
- OT cyber tools：能看到 cyber risk，但不能回答 “这个 learned policy 今天是否应该移动这个 actuator”。

## 3. Solution

SafetyOps 是机器人技能上线前的安全门禁和事故证据层。

第一阶段 wedge：`Skill Release Safety Gate`

每个技能上线前必须声明：

- sensors / actuators / ROS-DDS allow-deny。
- ODD / risk level / safety envelope。
- dataset hash / eval score / replay regression。
- HIL recovery clips。
- AI Hub / QNN edge profile。
- robot profile compatibility。
- approvals / canary rules / rollout gates。
- rollback target。

运行时再由边缘 safety-agent 执行：

- command admission。
- local envelope checks。
- sensor / thermal / network / E-stop monitoring。
- incident ring buffer。
- append-only ledger。
- rollback record。

## 4. Why Now

机器人规模、AI 策略更新和监管压力同时把 release gate 变成刚需。

关键信号：

- IFR 报告 2024 年全球工业机器人新增安装约 542,000 台，在役量约 4.66M；中国新增约 295,000 台，在役量超过 2M。
- 2024 年专业服务机器人销量接近 20 万台，logistics 是最大类别之一，RaaS fleets 增长。
- OSHA 指出很多机器人事故发生在 programming、maintenance、testing、setup、adjustment 等变更/调试阶段。
- OSHA 也说明美国目前没有 robotics-specific OSHA standards，企业需要 ISO/ANSI evidence、risk assessment、EHS records 和 insurer/customer requirements。
- ISO 10218 于 2025 大幅更新，功能安全、软件和 network attack / unauthorized access 语境更重要。
- EU Machinery Regulation 将于 2027-01-20 适用，autonomous mobile machinery / robots 更明确进入监管周期。
- EU Cyber Resilience Act 的报告义务从 2026-09-11 开始，主体义务 2027-12-11 适用。
- Physical AI 让保险难以定价，因为 software version、operating limits、sites 和 sensors 会在部署后变化。

## 5. Product

从 release gate 切入，再扩展到 fleet safety passport。

### Edge Side

- `safety-agent`：运行在 ROS 2 stack 旁，观察 topics/actions/services、ODD state、sensor health、thermal、network、E-stop、QNN runtime。
- `command-admission`：高风险命令 allow/deny，阻止 raw `/cmd_vel`、arm trajectory、gripper force、map change、OTA，除非 policy 允许。
- `local-envelope`：speed、force、workspace、keepout zones、speed zones、payload、human-distance、confidence/OOD、battery/thermal limits。
- `ring-buffer`：持续记录 `T-60s -> T+180s` MCAP/video/runtime slices。

### Control Plane

- `skill-registry`：signed skill manifest、robot profile compatibility、SBOM、model lineage。
- `release-gate`：eval、replay、HIL、QNN/AI Hub profile、approvals、canary rules。
- `incident-ledger`：append-only event/custody ledger with hashes and replay pointers。
- `audit-pack-builder`：buyer/judge/insurer pack：manifest、gate result、profile evidence、incident timeline、rollback proof。
- `data-lane-router`：China lane and overseas lane share schemas, not raw sensitive data by default。

### Core Schemas

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
      subscribe: [/camera/*, /tf, /odom, /safety/state]
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

```json
{
  "release_gate.v1": {
    "release_id": "rel_2026_07_safetyops_004",
    "dataset_hash": "sha256:...",
    "eval": {
      "success_rate": 0.94,
      "intervention_rate": 0.03,
      "replay_regressions": 0
    },
    "edge_profile": {
      "ai_hub_job_id": "hub_profile_...",
      "target_device": "Dragonwing RB3 Gen 2 Vision Kit",
      "runtime": "QNN",
      "latency_p95_ms": 28,
      "peak_memory_mb": 214,
      "compute_units": ["NPU", "CPU_fallback"],
      "numeric_delta_ok": true
    },
    "decision": "allow_canary",
    "approvals": ["safety_owner", "fleet_admin"]
  }
}
```

APIs:

- `POST /v1/skills:submit`
- `POST /v1/releases/{id}:evaluate`
- `POST /v1/releases/{id}:approve`
- `POST /v1/robots/{id}/commands:authorize`
- `POST /v1/incidents`
- `POST /v1/replay-tests`
- `POST /v1/rollbacks`
- `GET /v1/audit-packs/{id}.zip`

## 6. Market And Business Model

卖给机器人公司的是更快进 pilot，卖给企业的是更少部署风险。

### Buyers

- Robot OEM：CTO、VP Safety、VP Product、compliance lead、customer-success lead。
- Enterprise deployer：EHS、plant/warehouse operations、automation engineering、OT security/CISO、legal/risk、procurement。
- System integrator：需要标准化 risk assessment deliverables 和 liability protection。
- Insurer / RaaS financier：需要 signed telemetry、incident replay 和 per-unit risk scoring。

预算来源：

- Certification / safety engineering。
- Warranty reserve。
- Enterprise pilot enablement。
- EHS software。
- OT security。
- Automation capex。
- Insurance / vendor risk management。

ROI:

- 避免一次事故、罚款或停线。
- 减少 release review 时间。
- 减少 warranty / SLA disputes。
- 让 fleet 更容易被客户、保险和 RaaS financier 接受。
- 50 台 RaaS fleet 延迟一个月部署，可能就是 $50k-$150k idle subscription value。

### Pricing Hypotheses

China:

- OEM pilot：人民币 20k-80k / year for release gate + audit pack。
- Factory/site：人民币 50k-150k / site-year + 人民币 50-200 / robot / month。
- Enterprise/OEM scale：人民币 200k-800k / year for multi-site governance、standards mapping、warranty/insurer evidence API。

Overseas:

- OEM/SI：$10k-$50k / year dev/test governance，plus $2k-$10k per formal release/certification evidence pack。
- Enterprise：$25k-$100k / site-year + $20-$100 / robot / month。
- High-risk multi-site：$150k-$500k / year。
- RaaS / insurer evidence API：2%-5% of robot monthly subscription，roughly $20-$150 / robot / month。

## 7. Competition And Moat

竞争证明需求真实，但 SafetyOps 的位置在 physical AI release evidence。

Competitors / adjacent:

- Veo Robotics / Symbotic：dynamic 3D robot safeguarding；更偏 cell/hardware safety。
- FORT Robotics / 3Laws：安全 runtime 和 control；更偏 command safety。
- NVIDIA Isaac + Halos：NVIDIA-first full-stack physical AI safety。
- InOrbit / Formant：fleet ops、telemetry、incident、teleop；不是 release-gate-first。
- Foxglove：MCAP、log search、replay、dataset curation；不是 deployment authorization。
- Viam：developer runtime、fleet、OTA、canary、rollback；不是 safety/compliance as hero product。
- ROS 2 DDS Security：low-level enclave / permission primitive；缺少产品化 policy、approval、audit pack。
- Siemens / Rockwell / Pilz / SICK：certified safety controllers and machine safety；不管 AI model lineage 和 skill approval。
- Alias RIS / SBOM vendors：cyber controls；不回答 physical command authorization。
- AI governance platforms：digital AI governance；弱在 ROS、actuators、E-stop、edge latency、physical replay。

Moat:

- Cross-OEM safety event schema。
- Release-gate integrations。
- Hazard / skill library。
- Insurer-ready evidence graph。
- Edge-signed telemetry。
- Qualcomm AI Hub/QNN profile as deployment evidence。
- China/overseas data lanes with same schema and different trust shell。

## 8. Why Qualcomm

Qualcomm 不只需要机器人跑 AI，还需要 AI 策略能被批准上线。

SafetyOps 把 Qualcomm edge 从推理目标升级成 physical AI release target：

- 每个模型都有 AI Hub/QNN profile。
- runtime artifact、latency/memory、numeric delta、target device、rollback 和 incident evidence 都进入 release gate。
- edge safety-agent 在本体检查 ODD、sensor health、network、thermal 和 command policy。
- signed logs、MCAP replay、QNN runtime、incident timeline 进入客户验收包。
- OEM、SI、企业客户、认证实验室、保险和 RaaS financier 围绕 Qualcomm-ready evidence 协作。

需要 Qualcomm 支持：

- RB3 Gen 2 / Dragonwing / IQ hardware profile。
- AI Hub / QNN profiling guidance。
- Robot OEM / SI pilot introduction。
- 将 SafetyOps 作为 Qualcomm-edge physical AI release gate reference workflow。

## 9. Competition Demo

8 分钟演示：`dock-assist-v2` 技能被门禁拦截、限权上线、触发 incident、再回滚。

Demo flow:

1. 打开中文页面：企业不怕机器人不聪明，怕策略不可控。
2. 展示 `dock-assist-v2` skill card：permissions、ODD、risk level、rollback target。
3. SafetyOps gate 拦截：缺少 human-proximity validation / HIL / replay evidence。
4. 补上 release gate：dataset hash、replay pass、HIL clips、approver checklist。
5. 展示 Qualcomm evidence：AI Hub/QNN profile with latency、memory、compute unit、runtime artifact。
6. 部署到 canary robot/simulator：DDS policy 拒绝 unsafe raw `/cmd_vel`，只允许 `/safety/cmd_vel_limited`。
7. 触发 incident：human enters keepout zone or QoS deadline miss；robot slows/stops，ledger records event。
8. Replay lab 打开 MCAP slice，比对 `v1` vs `v2`，失败片段进入 LeRobot/HIL dataset。
9. One-click rollback to previous-known-good。
10. 导出 `judge-audit-pack.zip`，切换 China/Overseas lane，展示 raw video stays regional，only hashes/summary cross lanes。

## Standards Mapping

SafetyOps 不是认证工具，但输出的 evidence workflow 可映射到以下框架：

- ISO 12100：hazard identification、risk estimation、risk reduction、residual risk。
- ISO 13849-1 / IEC 62061 / IEC 61508：PL/SIL 目标和 safety-related control evidence。
- ISO 10218-1/2:2025：industrial robot / robot-cell safety。
- ISO 13482：personal care / service robots。
- ISO 3691-4：AGV / AMR / driverless industrial trucks。
- ANSI/RIA R15.08：industrial mobile robots and applications。
- EU Machinery Regulation：technical documentation、conformity evidence、change control。
- EU AI Act：high-risk AI governance vocabulary where AI is a safety component or embedded in regulated products。
- NIST AI RMF：govern、map、measure、manage。
- ISA/IEC 62443 / NIST SP 800-82 / CISA ICS：OT security, remote access, patching, supply chain。
- OSHA：robotics guidance, technical manual, LOTO, General Duty Clause context。
- China GB / GB/T：GB/T 15706、GB/T 16855.1、GB 11291.1/2、GB/T 36530、GB/T 10827.4。

## Claims To Avoid

- 不说 SafetyOps certifies robots / makes robots compliant。
- 不说 ISO/CE/OSHA/EU AI Act compliant，除非有具体 assessment 和 scope。
- 不说 zero accidents / guaranteed safe。
- 不说 LLM makes safety decisions。
- 不说 replaces safety engineers、safety PLCs、certified safety controllers、or certification labs。
- 不说 one standard covers all robots。
- 不说 cybersecurity is optional。
- 不说 cloud is real-time safety controller。
- 正确说法：helps teams align evidence workflows with ISO/IEC/ANSI/EU/China safety frameworks。
- 正确说法：audit-ready evidence、safety-case preparation support、Qualcomm-edge-ready candidate workflow。

## Sources

- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- OSHA robotics：https://www.osha.gov/robotics
- OSHA robotics standards：https://www.osha.gov/robotics/standards
- OSHA penalties：https://www.osha.gov/penalties
- NSC work injury cost：https://injuryfacts.nsc.org/work/work-overview/work-safety-introduction/
- NSC workers compensation cost：https://injuryfacts.nsc.org/work/costs/workers-compensation-costs/
- ISO 12100：https://www.iso.org/standard/51528.html
- ISO 13849-1：https://www.iso.org/standard/73481.html
- IEC 62061：https://webstore.iec.ch/en/publication/59927
- IEC 61508：https://iec.ch/functional-safety
- ISO 10218-1：https://www.iso.org/standard/73933.html
- ISO 10218-2：https://www.iso.org/standard/73934.html
- ISO 13482：https://www.iso.org/standard/53820.html
- ISO 3691-4：https://www.iso.org/standard/83545.html
- ANSI/RIA R15.08-1：https://webstore.ansi.org/standards/ria/ansiriar15082020
- ANSI/A3 R15.08-2：https://webstore.ansi.org/standards/ria/ansia3r15082023
- A3 ISO 10218 FAQ：https://www.automate.org/robotics/blogs/updated-iso-10218-faq
- EU Machinery Regulation：https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng
- EU AI Act：https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- EU AI regulatory framework：https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU Cyber Resilience Act：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- NIST AI RMF：https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Playbook：https://airc.nist.gov/airmf-resources/playbook/
- NIST OT Security：https://csrc.nist.gov/pubs/sp/800/82/r3/final
- CISA ICS：https://www.cisa.gov/topics/industrial-control-systems
- ROS 2 DDS Security：https://design.ros2.org/articles/ros2_dds_security.html
- DDS Security：https://www.omg.org/spec/DDS-SECURITY/1.2/About-DDS-SECURITY
- MCAP ROS 2：https://mcap.dev/guides/getting-started/ros-2
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
- Nav2 keepout filter：https://docs.nav2.org/tutorials/docs/navigation2_with_keepout_filter.html
- Nav2 speed filter：https://docs.nav2.org/tutorials/docs/navigation2_with_speed_filter.html
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm AI Hub profile examples：https://workbench.aihub.qualcomm.com/docs/hub/profile_examples.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- FORT Robotics：https://www.fortrobotics.com/
- 3Laws funding：https://www.prnewswire.com/news-releases/3laws-secures-4-1m-in-seed-funding-to-enable-safe-unsupervised-robot-operation-in-dynamic-environments-302266960.html
- NVIDIA Halos：https://www.nvidia.com/en-us/ai-trust-center/halos/robotics/
- Symbotic / Veo Robotics：https://www.symbotic.com/news/symbotic-acquires-veo-robotics-to-enhance-efficiency-and-safety-innovation/
- InOrbit：https://www.inorbit.ai/
- Formant fleet observability：https://docs.formant.io/docs/fleet-observability
- Foxglove：https://foxglove.dev/
- Viam：https://www.viam.com/
- Siemens safety systems：https://docs.tia.siemens.cloud/
- Rockwell safety controllers：https://www.rockwellautomation.com/en-us/products/hardware/safety-products/safety-controllers.html
- Pilz controllers：https://www.pilz.com/en-US/products/small-controllers
- SICK Flexi Soft：https://www.sick.com/gb/en/catalog/products/safety/safety-controllers/flexi-soft/c/g186176
- Alias RIS：https://aliasrobotics.com/ris.php
- IBM watsonx governance：https://www.ibm.com/products/watsonx-governance
- China GB/T 15706：https://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7E121D3A7E05397BE0A0AB82A
- China GB/T 16855.1-2025：https://std.samr.gov.cn/gb/search/gbDetailed?id=3DBA213286C30D16E06397BE0A0A8119
- China GB/T 10827.4-2023：https://std.samr.gov.cn/gb/search/gbDetailedCNF?id=FC816D04FECA62EBE05397BE0A0AD5FA
- CAC cross-border data provisions：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- Alibaba Cloud machine learning：https://www.alibabacloud.com/en/product/machine-learning
- Tencent GPU：https://www.tencentcloud.com/product/gpu
- Huawei ModelArts：https://www.huaweicloud.com/intl/en-us/product/modelarts.html
- RunPod pricing：https://www.runpod.io/pricing
- Lambda instances：https://lambda.ai/instances
- Modal training：https://modal.com/products/training
- CoreWeave training：https://www.coreweave.com/solutions/ai-model-training
