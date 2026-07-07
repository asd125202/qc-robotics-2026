# QC Robotics 2026

Repository for the 2026 Qualcomm Embodied Intelligence and Robotics Developer Competition.

Official competition page: https://qc-robotics-dev.aidlux.com/2026/

## Competition Timeline

- Before 2026-07-20: register, submit project proposal, and complete the preliminary round.
- Before 2026-07-31: organizer ships development boards to shortlisted developers.
- 2026-08 to 2026-11-01: submit final-round work online.
- End of 2026: Qualcomm developer ecosystem conference and awards ceremony.

## Project Direction

This repository is prepared for a commercial-ready robotics platform concept for the 2026 Qualcomm Embodied Intelligence and Robotics Developer Competition.

Working concept:

> An all-in-one robotics product platform that combines Qualcomm Dragonwing edge AI hardware, LeRobot-compatible real-world data workflows, and China/overseas cloud GPU training so users can build robot applications without starting from power supply, compute board, drivers, and training infrastructure.

The current first-batch pitch directions are:

- `RobotMac Core`: YC-style Qualcomm-first robot compute appliance pitch for turning prototypes into fieldable robots with 12-24V power, camera/robot IO, safety boundaries, RobotCoreOS, LeRobot data loops, AI Hub/QNN deployment, fleet telemetry, signed OTA, rollback, and release evidence.
- `RobotCoreOS`: YC-style Qualcomm-first robot production runtime pitch that turns ROS 2 / LeRobot prototypes into fleetable products with golden images, runtime agents, QNN policy releases, signed OTA, rollback, SBOM/provenance, release evidence, and Qualcomm edge profiles.
- `LeRobot CloudTwin`: YC-style Qualcomm-first robot learning and policy release pitch for turning real episodes into LeRobotDataset v3, China/overseas GPU training jobs, locked eval gates, data-rights evidence, LeRobot-to-QNN export bridges, rollback packages, and failure mining loops.
- `TrainRouter`: YC-style controlled robot training execution pitch for immutable LeRobot job contracts, China/overseas/private GPU lanes, budget admission, data-boundary routing, checkpoint recovery, fixed eval gates, artifact provenance, and Qualcomm edge export receipts.
- `TeleopStudio`: YC-style Qualcomm-first teleoperation data factory pitch for turning human demonstrations, camera/state/action streams, failure takeovers, quality gates, LeRobotDataset exports, TrainRouter handoffs, and edge-origin evidence into a commercial robot-learning workstation.
- `SkillDock`: YC-style trusted robot skill distribution and governance pitch for private skill libraries, signed bundles, SkillCertKit passports, Qualcomm edge profiles, install gates, staged rollout, telemetry, rollback, procurement, and revenue routing.
- `SkillCertKit`: YC-style pre-install robot skill trust-gate pitch that turns policy models, ROS packages, LeRobot lineage, SBOM/VEX, signatures, Qualcomm edge profiles, safety boundaries, rollout gates, and rollback metadata into a signed Skill Passport.
- `Embodied Kit`: procurement-ready industry kit for factories, labs, education, and service robotics teams.
- `DragonWorks`: YC-style Qualcomm-first production layer that turns ROS 2 projects, LeRobot episodes, dual-cloud training, AI Hub/QAIRT/QNN profile evidence, Dragonwing runtime packages, SkillCertKit gates, SkillDock releases, EdgeFleet feedback, and submission packets into a demo-to-production workflow.
- `EdgeFleet`: YC-style Qualcomm-first robot progressive delivery and fleet evidence pitch for staged rollout, QNN artifact traceability, remote-assist boundaries, incident capsules, rollback, RaaS uptime, warranty evidence, and failure feedback into TeleopStudio / TrainRouter.
- `EduForge`: education and developer kit for teaching the full LeRobot-to-Qualcomm edge deployment loop.
- `JudgeDeck`: judge-facing scoring alignment and three-minute demo storyboard.
- `Prototype`: interactive static dashboard that simulates devices, datasets, cloud training, model deployment, and skill packages.
- `CloudPlan`: provider execution and budget story for China and overseas cloud GPU training.
- `HardwareMap`: physical product-line and BOM story for QCS6490, QCS8550, IQ-8275, and future IQ10.
- `HomeCore`: privacy-first home robot skill layer for app-like skills, local perception, family co-care, LeRobot training, and Qualcomm edge execution.
- `骁工 XiaoGong`: task-bounded commercial humanoid platform for factory, logistics, retail and campus pilots, with task capability ledgers, human-assist loops, LeRobot data flywheels, and Qualcomm edge autonomy.
- `SiteLedger 工地实录`: construction-site memory and evidence platform for layout verification, progress/QA capture, safety observations, payment evidence, BIM/CDE integration, and LeRobot data loops.
- `StoreLoop 门店异常闭环`: retail store exception-closure platform for shelf gaps, price mismatches, expiry/cold-chain issues, returns, instant-retail picking, pharmacy compliance, proof-of-closure, and LeRobot training loops.
- `FoodLoop 餐饮异常闭环`: restaurant exception-closure platform for KDS/POS tickets, tray/bag verification, delivery/bussing, cleaning proof, food-safety logs, waste/rework attribution, and LeRobot HIL loops.
- `护元 CareOS 照护异常闭环`: eldercare exception-closure platform for home, community, and facility care tasks, privacy-first Qualcomm edge execution, caregiver escalation, service evidence, and LeRobot HIL loops.
- `WarehouseLoop 仓务异常闭环`: warehouse exception-closure platform for WMS mismatches, receiving/putaway errors, returns grading, photo/barcode proof, WMS writeback, and LeRobot HIL loops.
- `QualityLoop 质检闭环`: manufacturing quality closed-loop system for defect evidence, RCA/CAPA, re-inspection, MES/QMS writeback, edge vision governance, and LeRobot HIL loops.
- `AgriLoop 农务闭环`: verified farm-work operating loop for scouting, prescriptions, farm-service dispatch, robot/drone execution, proof-of-work, traceability, cost, and LeRobot HIL loops.
- `ColdChainLoop 冷链闭环`: temperature-sensitive logistics exception-closure platform for excursions, dwell, proof-of-recovery, WMS/TMS/QMS writeback, audit bundles, and LeRobot HIL loops.
- `LabLoop 实验室闭环`: lab operations and provenance layer for sample identity, instruments, robots, raw data, QC exceptions, LIMS/ELN/QMS writeback, and LeRobot HIL loops.
- `CleanLoop 商业清洁闭环`: commercial cleaning operations tower for demand-triggered tasks, robot/human dispatch, coverage proof, SLA reports, privacy-first edge perception, and LeRobot HIL loops.
- `InfraLoop 设施巡检闭环`: critical facility inspection loop for data centers, substations, BESS, pump stations, robots/drones/cameras, CMMS/EAM writeback, verified repair evidence, and LeRobot HIL loops.
- `YardLoop 港场异常闭环`: container-yard exception-closure platform for gate OCR, seal/damage/chassis proof, yard slot mismatches, TOS/YMS writeback, and LeRobot HIL loops.
- `ShipyardLoop 船厂生产证据闭环`: shipyard work-package trust layer that turns weld, coating, QA, rework, acceptance, settlement, robot telemetry, MES/QMS/ERP writeback, and LeRobot HIL loops into auditable evidence closure.
- `CircularLoop 城市矿山价值路由`: asset-level electronics circularity router that sends each retired phone, laptop, SSD, server module, and battery to the highest-value compliant next step with data-wipe proof, battery quarantine, audit packets, and LeRobot HIL loops.
- `RampLoop 机坪异常闭环`: airport ramp exception-closure layer that turns FOD, late GSE, baggage/catering/cleaning blockers, safety-zone violations, SLA disputes, owner assignment, verified evidence, and LeRobot HIL loops into controllable delay-minute reduction.
- `SterileLoop 手术器械异常闭环`: sterile processing and OR instrument-tray exception-closure platform for missing/wrong instruments, cycle evidence, UDI/RFID proof, human signoff, and LeRobot HIL loops.
- `TouchForge 触觉力控技能工厂`: tactile and force-control data factory for last-centimeter contact skills, LeRobot HIL episodes, Qualcomm edge deployment, and industrial ROI evidence.
- `HarnessLoop 线束异常闭环`: EV wire-harness and connector exception-closure platform for half-mated connectors, misroutes, missing clips, continuity failures, rework evidence, LeRobot HIL recovery, and Qualcomm edge verification.
- `SurfaceLoop 表面工程证据闭环`: industrial surface-prep, coating inspection, rework, release-packet, LeRobot HIL, and Qualcomm edge evidence platform for shipyards, steel assets, wind blades, auto paint, rail, and aerospace MRO.
- `BatteryRouter 电池入仓路由`: first-hour battery intake routing workcell for retired lithium packs/modules, mock diagnostics, human-approved reuse/repair/recycle/quarantine routing, LeRobot HIL, and Qualcomm edge evidence packets.
- `SolarLoop 光场异常闭环`: solar-site exception-closure platform for RGB/thermal inspection, soiling and fault work orders, robot cleaning/verification, LeRobot HIL, and Qualcomm edge evidence packets.
- `MineLoop 智矿异常闭环`: mine-site exception-closure platform for alarms, robot inspection, conveyor/haulage downtime, slope/tailings monitoring, hidden-danger ledgers, LeRobot HIL, and Qualcomm edge evidence packets.
- `WaterLoop 水务异常闭环`: water-utility exception-closure platform for leaks, pressure drops, pump anomalies, water-quality drift, sewer/stormwater risk, robot inspection, LeRobot HIL, and Qualcomm edge evidence packets.
- `GridLoop 配网异常闭环`: distribution-grid exception-closure platform for voltage anomalies, transformer overload, thermal defects, vegetation/wildfire/storm risk, DER/EV constraints, robot/drone inspection, LeRobot HIL, and Qualcomm edge evidence packets.
- `RailLoop 轨交异常闭环层`: vendor-neutral rail/metro exception-closure pitch around one exception ID, hidden-danger closure, station assets, flood readiness, inspection robots, LeRobot HIL, and Qualcomm edge evidence packets.
- `ComputeLoop 智算异常闭环台`: AI factory exception-closure pitch that links GPU/job issues, RoCE/network, liquid cooling, power, PUE, robot inspection, SLA impact, LeRobot HIL, and Qualcomm edge evidence into verified recovery events.
- `BuildLoop 安闭环`: construction safety exception-closure evidence pitch for AI alerts, inspections, subcontractor remediation, owner/regulator/insurer audit packets, symbolic tabletop demo, LeRobot HIL, and Qualcomm edge evidence.
- `RoboPort 机器人模组港`: robot-module compatibility evidence pitch for CR-ready module passports, ROS 2 driver capsules, LeRobot metadata, compatibility tests, marketplace distribution, and Qualcomm edge certification targets.
- `BusinessCase`: demo-to-deployment business pitch for RobotMac, covering problem, why now, market wedge, dual-cloud training economics, package strategy, competition, moat, Qualcomm value, demo, and ask.
- `SubmissionKit`: preliminary project-book structure, official upload constraints, and submission readiness checklist.
- `VerticalPlaybooks`: factory, logistics, lab, campus/service, and education market product packages.
- `DataFlywheel`: teleoperation, dataset ledger, cloud training, edge deployment, and failure-mining loop.
- `RoboTrust`: robot data trust cloud for regional data planes, dataset rights, training authorization, and enterprise audit evidence.
- `WorldForge`: simulation CI and synthetic-data factory for LeRobot datasets, failure mining, and Qualcomm edge validation.
- `IntegratorForge`: certified system integrator marketplace and deployment evidence system for RobotMac / Qualcomm edge projects.
- `RobotLeaseOps`: Dragonwing lease-ready robot asset operations layer for RaaS, leasing, uptime SLA, service history, AI Hub/QNN evidence, maintenance, financing, invoices, and bankable robot capacity.
- `UptimeOS`: YC-style pitch for a Dragonwing aftermarket service OS that turns telemetry, AI Hub/QNN evidence, remote diagnostics, FRU/RMA, technician workflows, warranty history, and SLA invoices into robot health passports and auditable uptime ledgers.
- `RiskLedger`: Physical AI EDR / robot claims exchange pitch for tamper-evident incident capture, MCAP/QNN evidence bundles, insurance underwriting data, finance diligence, warranty disputes, SLA evidence, and redacted incident replay.
- `ScaleFoundry`: Dragonwing prototype-to-SKU productization layer for BOM/AVL, EVT/DVT/PVT gates, factory tests, certification evidence, golden images, FRU/spares, PCN/PDN, lifecycle ledgers, and field CAPA loops.
- `CertForge`: YC-style Dragonwing robot compliance CI/CD pitch for turning every model, firmware, SBOM/VEX, ROS/MCAP, QNN profile, HIL/field test, risk decision, and supplier proof into auditable launch dossiers for labs, customers, investors, and market-entry workflows.
- `能栈 NengStack`: YC-style robot energy operations pitch for coordinating robot battery state, charging reservations, tasks, site power envelopes, battery health, Dragonwing edge energy telemetry, and RaaS/leasing margin evidence.
- `FleetConductor`: YC-style local edge robot tower pitch for second-vendor rollout, mixed-vendor AMR orchestration, VDA 5050/Open-RMF adapters, site graph, traffic reservations, doors/elevators/chargers, incident replay, and LeRobot feedback.
- `CareOps`: YC-style hospital logistics control-plane pitch for sealed specimen transport, medication/supply handoff, LIS/LIMS/FHIR-style workflow, privacy-first edge vision, chain-of-custody evidence, China/overseas data lanes, and Qualcomm AI Hub/QNN deployment proof.
- `FieldOps`: YC-style new-energy field evidence pitch for solar/remote-asset exception closure, mixed drone/UGV/quadruped missions, weak-network execution, ODD safety envelopes, EvidencePackage APIs, China/overseas training lanes, and Qualcomm AI Hub/QNN release gates.
- `SafetyOps`: YC-style robot skill release-gate and remote-assist evidence governance pitch for permissions, ODD/safety envelopes, AI Hub/QAIRT/QNN profile evidence, ROS/DDS command admission, JIT access sessions, SBOM/VEX, incident ledgers, rollback, insurer/customer audit packs, and China/overseas trust shells.
- `机御 Zero`: YC-style motion-level zero trust pitch for proving who can make a robot move, binding Qualcomm-rooted robot passports, ROS/DDS least privilege, JIT remote access, signed OTA, SBOM/VEX, SOC export, and auditable motion command policy into a commercial security layer.
- `DualCloudOps`: YC-style LeRobot-to-Qualcomm release pitch for routing one robot training contract across China or overseas GPU clouds, preserving data boundaries, reproducible eval gates, signed artifacts, and Qualcomm edge deployment evidence.
- `RevenueStack`: YC-style robot revenue operating-system pitch for turning hardware, RaaS/leasing, skill packages, cloud training credits, SLA/warranty, channel settlement, usage metering, and Qualcomm AI Hub/QNN profile evidence into recurring revenue.
- `RobotAppLayer`: YC-style robotics application-layer pitch for turning ROS 2, LeRobot policies, signed skill bundles, physical permissions, compatibility testing, Qualcomm AI Hub/QNN evidence, marketplace distribution, billing, and rollback into one app release workflow.
- `OpsConnector`: YC-style enterprise robot workflow-contract pitch for turning WMS, MES, LIMS, SCADA, ERP, operator approvals, robot execution, edge gateway evidence, exceptions, and audit writeback into reusable connector/workflow packs.
- `LabForgePilot`: YC-style main-demo and first-commercial-wedge pitch for a desktop sample-transfer workcell that turns LeRobot data collection, ACT/HIL training, Qualcomm edge evidence, barcode/sample verification, LIMS writeback, and failure mining into a purchasable lab/QC/education product.
- `EdgeRuntimeBench`: YC-style physical-AI runtime evidence pitch for proving LeRobot/ACT/SmolVLA policies are traceable, exportable or explicitly blocked, profiled on Qualcomm AI Hub/QNN/ONNX Runtime targets, gated by SafetyOps, packaged for SkillDock, deployed, monitored, and rolled back with signed evidence packs.
- `BoardBringupKit`: YC-style Qualcomm board-to-robot commercialization pitch for turning Rhino X1/QCS8550, Dragon Q6A/QCS6490, power, camera, IO, safety, ROS 2, LeRobot, runtime image, HIL gates, and bring-up evidence into a reusable RobotMac Core candidate.
- `PilotContractKit`: YC-style commercial OS for paid robot pilots, turning demos into procurement-ready SOWs, baseline packs, KPI scorecards, FAT/SAT protocols, risk/data/cyber boundaries, Qualcomm edge evidence, support SLAs, and rollout contracts.

## Repo Layout

```text
.
├── demos/                 # Demo scripts, videos, and reproducible walkthroughs
├── docs/                  # Competition proposal, schedule, architecture, checklist
├── hardware/              # Board notes, wiring, sensors, robot chassis notes
├── models/                # Model conversion/deployment notes; avoid committing large weights
├── scripts/               # Build, deploy, and utility scripts
└── src/                   # Application source code
```

## Near-Term Tasks

- Finalize the project name and one-sentence value proposition.
- Complete `docs/project-proposal.md` before the 2026-07-20 preliminary deadline.
- Use `docs/product-thesis.md`, `docs/concept-portfolio.md`, and `sites/` as the first concept batch.
- Use `docs/competition-info.md` as the local contest reference when shaping the proposal and demo plan.
- Decide the target board and robot form factor.
- Build a small browser-based demo page and deploy it through Cloudflare Pages for judges/reviewers.
- Add the first runnable perception/control prototype under `src/`.

## Deployment Notes

This server has Wrangler and cloudflared configured for publishing demos.

- Static demo site: deploy with Cloudflare Pages.
- Current Chinese pitch site: https://qc-robotics-2026.pages.dev/
- Temporary local preview: run `cf-local-tunnel <port>`.

Do not commit Cloudflare credentials, model secrets, API keys, or private VPN/client config files.
