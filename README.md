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

- `RobotMac Core`: all-in-one robotics compute, power, IO, safety, and runtime core.
- `RobotCoreOS`: golden robot runtime image with board support, ROS 2 bridge, LeRobot hooks, policy runner, OTA, rollback, and fleet identity.
- `LeRobot CloudTwin`: real robot data collection, cloud GPU training, and Qualcomm edge deployment loop.
- `TrainRouter`: dual-cloud GPU training router for China/overseas provider selection, budget guards, data boundaries, evaluation, and Qualcomm edge artifact export.
- `TeleopStudio`: productized teleoperation and demonstration-data capture station with synchronized cameras, quality gates, LeRobot dataset export, and cloud handoff.
- `SkillDock`: robot skill marketplace where trained skills can be installed, certified, and upgraded.
- `SkillCertKit`: robot skill certification package for manifests, dataset lineage, hardware compatibility, edge benchmarks, safety gates, and marketplace publishing.
- `Embodied Kit`: procurement-ready industry kit for factories, labs, education, and service robotics teams.
- `DragonWorks`: Qualcomm-first robotics developer workbench for devices, datasets, training, deployment, and skills.
- `EdgeFleet`: fleet operations layer for enterprise robot maintenance, logging, updates, and training feedback.
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
- `ComputeLoop 智算异常闭环台`: AI data center exception-closure platform for GPU faults, liquid cooling, thermal/leak/power/PUE anomalies, robot inspection, LeRobot HIL, and Qualcomm edge evidence packets.
- `BuildLoop 安闭环`: construction-site safety exception-closure platform for fall-edge, PPE, exclusion-zone, temporary electrical, hot-work, confined-space, subcontractor remediation, LeRobot HIL, and Qualcomm edge evidence packets.
- `RoboPort`: certified robot module port ecosystem for sensors, tools, drives, safety IO, ROS 2 drivers, LeRobot metadata, and compatibility evidence.
- `BusinessCase`: commercialization, buyer personas, package strategy, and recurring revenue flywheel.
- `SubmissionKit`: preliminary project-book structure, official upload constraints, and submission readiness checklist.
- `VerticalPlaybooks`: factory, logistics, lab, campus/service, and education market product packages.
- `DataFlywheel`: teleoperation, dataset ledger, cloud training, edge deployment, and failure-mining loop.
- `RoboTrust`: robot data trust cloud for regional data planes, dataset rights, training authorization, and enterprise audit evidence.
- `WorldForge`: simulation CI and synthetic-data factory for LeRobot datasets, failure mining, and Qualcomm edge validation.
- `IntegratorForge`: certified system integrator marketplace and deployment evidence system for RobotMac / Qualcomm edge projects.
- `RobotLeaseOps`: RaaS, leasing, uptime SLA, service ledger, and subscription control plane for bankable robot capacity.
- `UptimeOS`: aftermarket service operating system for health passports, predictive maintenance, remote diagnostics, FRU/spares, technician workflows, warranty evidence, and RaaS uptime ledgers.
- `RiskLedger`: robot risk evidence ledger for black-box event capture, insurance underwriting data, finance diligence, warranty analytics, SLA evidence, and tamper-evident incident replay.
- `ScaleFoundry`: prototype-to-SKU hardware productization, certification evidence, manufacturing launch, and lifecycle assurance.
- `CertForge`: compliance evidence factory for Qualcomm-powered robots, covering standards mapping, safety cases, SBOM/VEX, CRA readiness, radio, battery, CE/FCC/CCC/SRRC workflow, and launch dossier exports.
- `能栈 NengStack`: robot energy OS for fleet charging schedules, dock/charger mesh, battery passports, site power planning, Qualcomm power budgets, and RaaS energy evidence.
- `FleetConductor`: local edge robot tower for mixed-vendor fleet orchestration, maps, traffic, doors, elevators, chargers, incidents, and LeRobot feedback.
- `CareOps`: hospital and lab operations robot workflow platform for non-clinical logistics, specimen chain-of-custody, privacy-first edge AI, and audit evidence.
- `FieldOps`: outdoor inspection, agriculture, energy, and infrastructure robotics platform with rugged kits, sensor pods, resilient connectivity, teleoperation fallback, evidence packages, and a LeRobot field-data flywheel.
- `SafetyOps`: safety runtime, skill permissions, model release gates, audit ledger, and compliance evidence pack.
- `机御 Zero`: motion-level zero trust fabric for robot identity, ROS/DDS least privilege, JIT remote access, signed OTA, SBOM/VEX, SOC export, and auditable motion command policy.
- `DualCloudOps`: China/overseas GPU-cloud provider adapters behind one LeRobot training job contract.
- `RevenueStack`: pricing ladder, pilot contracts, recurring revenue lines, and Qualcomm ecosystem economics.
- `RobotAppLayer`: stable application SDK above ROS 2, LeRobot data/policies, fleet operations, and Qualcomm edge deployment.
- `OpsConnector`: enterprise integration bridge for WMS, MES, ERP, LIMS, SCADA, operator approval, robot task contracts, and audit writeback.
- `LabForgePilot`: competition main-demo package for desktop arm sample transfer, training, edge deployment, and failure feedback.
- `EdgeRuntimeBench`: Qualcomm edge compile/profile/deploy evidence chain for policy packages and runtime metrics.
- `BoardBringupKit`: board-to-robot bring-up package for power, camera, IO, safety, runtime image, and validation gates.
- `PilotContractKit`: 4-8 week enterprise pilot contract package with KPIs, acceptance criteria, training deliverables, and expansion path.

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
