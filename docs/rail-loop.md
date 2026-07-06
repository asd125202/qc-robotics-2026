# RailLoop 轨交异常闭环

Public page: https://qc-robotics-2026.pages.dev/rail-loop/

RailLoop is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames metro and rail operations as an exception-closure problem, not a detection-only AI problem and not a safety-critical control problem.

## One-Line Pitch

> 轨交不缺告警，缺的是从发现到销号的同一个异常 ID。

RailLoop is a vendor-neutral exception closure layer for rail and metro operations. It connects CCTV, ISCS, BAS/FAS, platform screen doors, escalators/elevators, pumps/flood readiness, inspection robots, manual patrols, passenger complaints, and EAM/CMMS work orders into owned, verified, auditable cases.

## Problem

Metro operators already have many systems and many people watching signals, but one exception often gets split across video, equipment alarms, calls, chat groups, OCC logs, contractor photos, work orders, spreadsheets, and weekly reports.

The missing product unit is one exception ID with:

- one location and asset identity;
- one responsible owner and escalation path;
- one SOP card and deadline;
- one evidence packet;
- one verification result;
- one closure record;
- one training label for future AI/robot improvement.

## Why Solve It

Exception closure matters because it touches multiple executive priorities:

- Delay minutes and service impact.
- Elevator/escalator and station asset availability.
- Platform screen door reliability and dwell-time impact.
- Flood readiness and climate resilience.
- Safety-quality audit trails and hidden-danger closure.
- Contractor quality, repeat faults, invoice evidence, and renewal prioritization.
- AI training data that reflects real final outcomes, not just raw detections.

## Why Now

China:

- MOT reported 54 Chinese cities operating 343 urban rail lines, 11,710.3 km, 6,680 stations, and about 33.24B annual passenger trips by the end of 2025.
- MOT rules require lifecycle equipment maintenance, risk databases, hidden-danger ledgers, verification, cancellation, and information sharing.
- New-build investment pressure makes renewal, safety, efficiency, and intelligent O&M easier to justify than broad transformation decks.

Global:

- FTA/Volpe estimated the U.S. transit state-of-good-repair backlog at about $140.2B.
- MTA's 2025-2029 Capital Plan is about $68.4B, with more than 90% focused on rebuilding and improving the existing system.
- Flood resilience, accessibility, station assets, and inspection evidence are visible political and operating pain points.
- Inspection robots and AI detection are increasingly accepted, but detection signals still need to become work orders, evidence, and closure.

## Insight

Detection models sell probability. Closure systems sell responsibility.

The same RailLoop exception ID follows an issue from detection to dispatch to repair to reinspection to final acceptance. Once the exception is closed, the result becomes a training label for vision models, priority models, robot inspection policies, and SOP refinement.

## Solution

RailLoop does not replace CBTC/ATP, OCC dispatch, SCADA, ISCS, EAM/CMMS, station video, equipment vendor diagnostics, inspection robots, or qualified maintainers.

RailLoop sits beside them:

1. Ingest read-only signals from existing systems.
2. Correlate duplicate alerts by station, asset, time, image, alarm, work order, and service impact.
3. Dispatch responsible owners with SOP cards, deadlines, evidence requirements, and escalation paths.
4. Verify recovery through images, device state, sensor clear, human acceptance, and complaint trends.
5. Close the case into audit ledgers, risk databases, contractor QA records, and training datasets.

## First Product

The first product should avoid safety-critical train control and focus on high-frequency station and facility exceptions:

- Platform screen-door obstruction, fault, repeat alarm, and verification.
- Escalator/elevator outage, barricade status, repair evidence, and availability reporting.
- Water intrusion, pump/flood readiness, station entrance/fan pavilion/tunnel checks.
- Equipment-room alarms and robot/manual patrol evidence.
- Visible trackside defects, foreign objects, seepage, labels, and cable-tray issues under read-only inspection workflow.

Pilot scope:

- 90-120 days.
- One line or depot.
- Three to five stations or a bounded station-asset domain.
- 50-150 monitored assets.
- Three to five exception types.
- Read-only integration, mobile evidence capture, human approval, and audit export.

## Market

China version:

- Buyer language: safety production, intelligent O&M, hidden-danger investigation and rectification, facility/equipment lifecycle maintenance, flood prevention, equipment renewal, and regulator-ready ledgers.
- Buyer functions: operations center, facility/equipment department, MEP center, signaling/communications center, track/works center, safety-quality department, station management, digital department, and chief engineer office.
- Deployment: private cloud or local deployment, local data residency, role permissions, logs, evidence retention, and cybersecurity review.

Overseas version:

- Buyer language: state of good repair, accessibility asset uptime, flood resilience, inspection evidence, EAM/CMMS quality, capital planning, and audit reporting.
- Buyer functions: operations, maintenance, asset management, accessibility, safety compliance, CIO/digital, and CFO/strategy.
- Deployment: integration layer around existing EAM/CMMS, video, inspection and incident-management systems.

## Business Model

China:

- Pilot: RMB 300k-800k for 90-120 days.
- Production: RMB 800k-2.5M per line per year.
- Network edition: RMB 5M-20M per year.
- One-time integration: RMB 500k-2M depending on system access and data quality.

Overseas:

- Pilot: USD 75k-200k.
- Production: USD 250k-750k per line or asset domain per year.
- Enterprise/network: USD 1M-3M per year.
- One-time integration: USD 150k-1M.

Pricing rule: keep first-year cost below 15%-25% of validated annual benefit, with a target payback period under 12 months.

## ROI And Pilot KPIs

Annual gross benefit can be modeled as:

delay savings + asset downtime savings + emergency labor savings + inspection/reporting labor savings + avoided duplicate dispatches + lower contractor dispute cost + flood/safety/compliance risk reduction.

90-day acceptance targets:

- 95%+ pilot assets mapped to EAM/CMMS IDs and responsible departments.
- 90%+ closed exceptions contain complete evidence packets.
- 30% reduction in alert-to-work-order or alert-to-action-card time.
- 20% reduction in overdue high-risk hidden dangers.
- 20%-30% reduction in manual report and audit-material preparation time.
- Weekly evidence export accepted by operations, maintenance, and safety-quality teams.

## Go-To-Market

Start with station asset reliability and hidden-danger closure, not a broad "AI metro brain".

China:

- Partner through rail system integrators, design institutes, equipment vendors, maintenance service providers, and domestic robot OEMs.
- Use procurement keywords around intelligent O&M, hidden-danger closure, safety production, flood readiness, facility/equipment maintenance, and operating production digitization.

Overseas:

- Partner with EAM/CMMS vendors, rail OEMs, engineering consultants, and asset-management programs.
- Target aging networks, accessibility assets, flood exposure, public outage complaints, and state-of-good-repair programs.

## Competition

RailLoop integrates with, rather than replaces:

- Siemens Mobility, Alstom, Hitachi Rail, Wabtec, Stadler, and other rail OEM/control ecosystems.
- IBM Maximo, SAP EAM, Hexagon, Bentley, Trimble, Cityworks, and similar asset-management systems.
- Track and infrastructure inspection systems, including geometry cars, LiDAR/video analytics, condition-monitoring vendors, and robot inspection vendors.
- Station BMS, VMS, SCADA, ISCS, platform-door, escalator/elevator, pump, and fire systems.

Differentiation:

- Unified exception ID across systems.
- Closure-first workflow instead of detection-only analytics.
- SOP, risk-database, and responsible-position mapping.
- Evidence standard for verification and cancellation.
- Contractor QA and audit-ready export.
- Closed-case data flywheel for AI and LeRobot experiments.

## Moat

The moat is not a single foundation model. It is the operator-specific closed-loop dataset:

- asset naming and system mappings;
- station and line topology;
- SOP and risk database mappings;
- role and escalation patterns;
- evidence standards for each exception type;
- repeat-fault history and contractor performance;
- final human verdicts and closure labels.

## Architecture

Engineering principles:

- read-only integration first;
- no safety-critical train control;
- human approval for operational closure;
- deterministic safety supervisor in the demo;
- local/private deployment preference;
- evidence logs, model versions, role permissions, and audit export.

Reference architecture:

- Station Edge: cameras, sensors, mobile photos, robot observations, local cache, and QNN candidate inference.
- Event Bus: correlation by station, asset, timestamp, image, alarm, work order, and impact.
- Closure Engine: classification, owner assignment, SOP card, SLA, verification rule, and audit ledger.
- Training Loop: LeRobotDataset episodes, vision labels, priority-model feedback, and false-positive review.
- Governance: evidence hashes, model/version logs, permissions, cybersecurity review, and human confirmation.

## Qualcomm Fit

Rail and metro station environments have many cameras, privacy constraints, weak-network moments, local audit requirements, and short response windows. This favors edge AI and on-device robot perception.

Qualcomm fit:

- multi-camera station edge inference;
- robot RGB/depth/thermal/vibration fusion;
- AI Hub/QNN compile, quantize, and profiling path;
- RB3/RB5/Dragonwing-style development hardware path;
- local deployment and hardware reference architecture for industrial robotics.

## Safe Competition Demo

Demo scope:

- 2-3m modular low-voltage tabletop metro scene.
- Acrylic platform screen-door model, non-powered train shell, equipment-room prop, tunnel/track tiles, water tray, dummy third rail/OLE props, and QR/AprilTag asset IDs.
- 5V/12V/24V current-limited supplies, fuses, independent E-stop, transparent guard, slow low-force servos, and water/electric isolation.
- Faults: foam PSD obstruction, escalator/elevator motor jam surrogate, water intrusion tray, trackside defect tiles, seepage, foreign object, missing fastener, label mismatch.
- Sensors: RGB, depth/ToF, thermal, motor current, limit switches, water/leak sensor, odometry, and robot/gantry camera.
- Software: ROS 2 topics/actions, Qualcomm/QNN candidate perception path, LeRobot teleop/data export, deterministic safety interlocks, human approval, and closure report.

Safe claim:

> Tabletop low-voltage rail/metro exception-closure demo using multimodal sensing, ROS 2 action workflow, human-reviewed evidence packets, LeRobot-compatible data, and a candidate Qualcomm AI Hub/QNN edge path.

Claims to avoid:

- certified railway safety system;
- live track or live station deployment without railway possession/isolation;
- replacement of qualified inspectors or operators;
- control of train movement, signaling, interlocking, traction power, platform doors, or dispatch;
- guaranteed detection of all defects or zero false negatives;
- measured Qualcomm NPU FPS before profiling on target hardware;
- endorsement by Qualcomm, Hugging Face, or any rail operator.

## Ask

Support requested from the competition and Qualcomm ecosystem:

- RB3/RB5/Dragonwing hardware route guidance.
- AI Hub/QNN compile and profiling support.
- Advice on multi-camera station edge design.
- Robotics mentor feedback on ROS 2 and LeRobot demo design.
- Rail/metro partner introductions for scenario validation.
- Safety-boundary review for public competition language.

## Sources

- MOT 2025 urban rail operation data: https://www.mot.gov.cn/xinwen/jiaotongyaowen/202601/t20260129_4199263.html
- MOT urban rail facility/equipment maintenance rule: https://xxgk.mot.gov.cn/xzgfxwj/202411/t20241115_4159468.html
- MOT urban rail risk and hidden-danger management rule: https://xxgk.mot.gov.cn/xzgfxwj/202411/t20241115_4159469.html
- MOT passenger organization and service management rule: https://xxgk.mot.gov.cn/xzgfxwj/202504/W020250415336381153024.pdf
- MOT flood-prevention guidance: https://xxgk.mot.gov.cn/2020/jigou/zghssjzx/202404/t20240418_4130463.html
- FTA Transit State of Good Repair National Backlog Analysis: https://www.transit.dot.gov/sites/fta.dot.gov/files/2025-01/Transit-State-of-Good-Repair-National-Backlog-Analysis_0.pdf
- MTA 2025-2029 Capital Plan announcement: https://www.mta.info/press-release/mta-releases-proposed-2025-2029-capital-plan
- MTA 2025-2029 Capital Program overview: https://www.mta.info/document/174186
- MTA Climate Resilience Roadmap update: https://www.mta.info/press-release/mta-releases-update-climate-resilience-roadmap-mitigate-impacts-of-extreme-weather
- Dubai RTA automated rail infrastructure inspection robot: https://mediaoffice.ae/en/news/2025/june/12-06/rta-rolls-out-the-automated-rail-infrastructure-inspection-system-in-dubai-metro
- AAR freight rail inspection examples: https://www.aar.org/freight-rail-innovation-week/
- Qualcomm RB3 Gen 2 Development Kit: https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub compile examples: https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- Hugging Face LeRobot: https://github.com/huggingface/lerobot
- ROS 2 Actions design: https://design.ros2.org/articles/actions.html
