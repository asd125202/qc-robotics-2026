# SkillCertKit

更新时间：2026-07-06。

SkillCertKit is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames the robot skill marketplace problem as a trust problem: companies will not install arbitrary policies on physical robots unless each skill comes with compatibility, lineage, edge, security, safety-boundary, and rollback evidence.

> SkillCertKit is the trust layer for installable robot skills.

## One-Line Company

SkillCertKit turns a robot policy model into a marketplace-ready skill package with manifest, LeRobot dataset lineage, hardware compatibility, Qualcomm edge profile, safety boundary, SBOM/license evidence, signature, rollback, and version history.

Chinese pitch:

> 机器人技能不能只上传模型文件，必须带着可安装、可验收、可回滚的证据。

## Problem

Robot skills today look like one-off project deliveries:

- they may work in a demo but not on the buyer's camera, arm, mobile base, runtime, or safety envelope;
- developers cannot easily sell the same skill twice without compatibility evidence;
- system integrators repeat validation for every customer;
- enterprise IT/security cannot see SBOM, vulnerabilities, permissions, logs, and cloud dependencies;
- buyers cannot distinguish a reliable skill from an experimental policy file;
- Qualcomm edge value does not accumulate unless every skill declares and proves a target profile.

## Why Now

Market signals:

- UR+ and MiR Go show certified robot ecosystems and marketplaces reduce adoption risk.
- LeRobot, Open X-Embodiment, and modern robot-learning workflows make robot skills more software-like.
- Qualcomm Dragonwing, AI Hub, and QNN/QAIRT make edge target validation commercially meaningful.
- Industrial buyers do not want consumer-style robot app downloads. They pay for deployment confidence, auditability, commissioning speed, security, and uptime.

The problem is shifting from “can a model control a robot once?” to “can this skill be listed, installed, verified, upgraded, and rolled back?”

## Insight

Skill package is not the same as ROS package.

Model card is not the same as robot deployment approval.

Marketplace listing is not the same as physical trust.

Fleet operations after deployment are not enough; enterprise buyers also need a before-install certification gate and recertification triggers after field failures.

## Solution

SkillCertKit wraps a robot skill in a structured evidence package:

- skill manifest;
- model card;
- dataset card / LeRobot lineage;
- runtime dependency graph;
- hardware compatibility profile;
- Qualcomm edge profile;
- latency/power benchmark;
- safety boundary;
- SBOM/license report;
- vulnerability gate;
- data-rights record;
- semantic versions;
- simulation vs real evidence labels;
- rollback package;
- marketplace review.

It is not a legal certification authority and does not claim official Qualcomm certification. It is a marketplace-readiness and deployment-evidence workflow.

## Product Workflow

1. Developer submits `skill.yaml`, model artifact, task boundary, dependencies, and target robot profile.
2. SkillCertKit checks manifest, ROS/SDK dependencies, sensors, actuators, permissions, runtime, and hardware assumptions.
3. Dataset lineage records LeRobot-compatible dataset IDs, versions, episodes, success/failure labels, license, and coverage gaps.
4. Qualcomm profile flow compiles/profiles/deploys selected artifacts through AI Hub / QNN / QAIRT where possible.
5. Safety gate checks workspace, speed/force class, emergency stop, human takeover, audit log, and fail-closed behavior.
6. SBOM/license/vulnerability gate records dependencies and release-blocking issues.
7. Marketplace card lists tested profiles, expected-compatible profiles, unsupported profiles, evidence level, versions, and support terms.
8. Field failures trigger recertification or rollback.

## Evidence Pack

Minimum fields:

| Evidence | What it records |
| --- | --- |
| Model artifact | name, hash, format, producer, training code, export path, quantization/compile settings, input/output schema, intended task |
| Dataset lineage | dataset IDs, versions, hashes, robot embodiment, sensor setup, episode count, success/failure labels, split, license/rights |
| Runtime graph | ROS manifests, container digest, OS/firmware, Python/C++ locks, QNN/ONNX/runtime versions, calibration files |
| Hardware profile | processor, accelerator, camera, arm/gripper, payload, controller firmware, safety IO, network, calibration |
| Edge profile | target device, accelerator path, runtime backend, compile job, memory, thermal state, sustained run, fallback |
| Metrics | p50/p95/p99 latency, cold start, control-loop deadline, dropped frames, memory peak, temperature, power where instrumented |
| Safety boundary | workspace, max speed/force, object classes, human proximity assumptions, emergency stop, manual takeover, forbidden motions |
| Rollback | previous-known-good artifact, version pins, trigger thresholds, state cleanup, operator confirmation, audit log |
| SBOM/license | SPDX/CycloneDX, dependency relationships, license metadata, vulnerability gate |
| Evidence level | simulated, hardware_in_loop, bench_real, field_real |

## Market Wedge

First users:

- automation engineers and controls engineers;
- system integrators;
- manufacturing operations managers;
- enterprise IT/security reviewers;
- fleet/RaaS operators;
- robot accessory/app developers;
- educators and research labs.

The first paid use case is not a consumer app store. It is certification, packaging, and deployment evidence for robot skills and accessories.

## Business Model

Revenue layers:

- Open Dev Tier: free/low-cost manifest generation and local tests for education/open-source experiments.
- Marketplace Ready: paid package for product-page artifacts, integration docs, test matrices, Qualcomm edge profile, and publish evidence.
- Enterprise Trust Pack: SBOM, vulnerability process, signed package, rollback plan, fleet observability hooks, network diagram, procurement questionnaire.
- Profile Fee: per skill package, hardware profile, private benchmark, or real-device test.
- Marketplace Take Rate: SkillDock transactions, enterprise private skill libraries, support subscriptions, and SI revenue share.

## Go To Market

Start with a reference skill:

`labforge.sample-transfer.v1`

Demo path:

1. Create skill manifest.
2. Attach LeRobot dataset lineage.
3. Generate Qualcomm edge profile.
4. Run SafetyOps gate.
5. Publish SkillDock card.
6. Block install on incompatible robot profile.
7. Allow staged rollout on compatible profile.

Then invite 10-20 developers and system integrators to submit skills and refine the evidence schema.

## Competition

SkillCertKit does not replace:

- ROS / ROS-Industrial;
- LeRobot;
- NVIDIA Isaac / Jetson / GR00T;
- Viam Registry / Modules;
- Foxglove data platform;
- Formant operations;
- Intrinsic Flowstate;
- UR+ / MiR Go / KUKA Creator Portal.

It sits between them:

- ROS gives package metadata.
- LeRobot gives datasets and policies.
- AI Hub/QNN gives edge profiling and deployment path.
- Foxglove/Formant-like tools can provide logs and field evidence.
- SkillCertKit turns these artifacts into install-before-trust evidence.

## Moat

The moat is an evidence network:

- skill manifests;
- robot profiles;
- dataset lineage;
- benchmark reports;
- failure episodes;
- safety boundaries;
- version histories;
- buyer acceptance records;
- Qualcomm edge profiles;
- recertification triggers.

Every certified skill makes the next skill easier to trust and makes the Qualcomm edge target more valuable.

## Why Qualcomm

Qualcomm value:

- every skill declares a Dragonwing target;
- AI Hub generates profile evidence;
- QNN/QAIRT package becomes a deployable skill artifact;
- edge metrics become buyer-facing evidence;
- reference skills can be published through Robotics Hub-style examples;
- Qualcomm becomes a robotics skill ecosystem standard, not only a hardware BOM line.

Claim boundary:

This is not official Qualcomm certification. It is a proposed Qualcomm-edge-oriented validation workflow.

## Demo

Three-minute competition demo:

1. Show `labforge.sample-transfer.v1` inside SkillDock.
2. Open `skill.yaml`: cameras, arm, gripper, workspace, permissions, target profile.
3. Show LeRobot episodes, failed samples, training version, and rights boundary.
4. Trigger certification: model artifact -> AI Hub/QNN profile -> edge metrics.
5. Run SafetyOps gate: emergency stop, speed, workspace, human takeover, rollback.
6. Publish marketplace card.
7. Try install on another robot profile:
   - incompatible profile blocks install;
   - compatible profile allows staged rollout.

## Ask

Ask Qualcomm for:

1. recommended contest-stage target path: RB3 Gen 2, QCS6490/QCS8550, or IQ route equivalent;
2. AI Hub / QNN / QAIRT profiling guidance;
3. a lightweight Dragonwing Skill Validation template;
4. support to publish 2-3 reference skills;
5. introductions to education kits, system integrators, robot OEMs, and automation buyers.

## Claim Boundaries

Do not claim:

- official Qualcomm certification;
- Qualcomm partnership or endorsement;
- cross-all-robot compatibility;
- zero-risk deployment;
- automatic safety/legal/regulatory compliance;
- all LeRobot/ACT/VLA models compile to QNN without changes;
- simulated profile metrics are measured hardware results.

Can claim:

- structured certification evidence for a robot skill package;
- marketplace-readiness workflow;
- evidence against named robot profiles and test conditions;
- Qualcomm-edge-deployable skill evidence layer;
- distinction between simulated, hardware-in-loop, bench-real, and field-real evidence.

## Sources

- Universal Robots UR+ Marketplace: https://www.universal-robots.com/marketplace/
- MiR Go: https://mobile-industrial-robots.com/products/mir-go
- Hugging Face LeRobot: https://github.com/huggingface/lerobot
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- ROS package manifest REP-149: https://www.ros.org/reps/rep-0149.html
- NIST SSDF SP 800-218: https://csrc.nist.gov/pubs/sp/800/218/final
- Hugging Face model cards: https://huggingface.co/docs/hub/en/model-cards
- Hugging Face dataset cards: https://huggingface.co/docs/hub/en/datasets-cards
- CycloneDX SBOM: https://owasp.org/www-project-cyclonedx/
- Qualcomm AI Hub deployment docs: https://workbench.aihub.qualcomm.com/docs/hub/deployment.html
- Qualcomm AI Engine Direct / QNN: https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk
- Qualcomm Dragonwing Robotics Hub: https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Qualcomm IQ10 Robotics Reference Design: https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- NEURA + Qualcomm collaboration: https://www.qualcomm.com/news/releases/2026/03/neura-robotics-and-qualcomm--enter-strategic-collaboration-to-ad
