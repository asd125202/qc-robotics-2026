# RailLoop 轨交异常闭环

RailLoop is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames rail and metro operations as an exception-closure problem: platform screen-door faults, escalator downtime, water intrusion, station-equipment alarms, visible trackside defects, inspection-robot findings, manual patrol findings, and contractor maintenance evidence should become owned, verified, auditable cases.

Public page: https://qc-robotics-2026.pages.dev/rail-loop/

## One-Line Pitch

> 每一次轨交异常，都有责任、有证据、有销号。

RailLoop serves station managers, OCC dispatch/statistics teams, safety and quality departments, maintenance subsidiaries, asset managers, contractor-governance teams, and digital-rail departments. The product unit is not an alert. It is a closed exception with evidence.

## Problem

Rail and metro operators already have many systems:

- CCTV, ISCS, BAS/FAS, platform screen-door systems, escalator/elevator systems, EAM/CMMS, OCC logs, station patrol forms, contractor reports, robot inspection, mobile photos, and passenger complaints.
- These systems see signals, but people still reconcile context across calls, chat groups, spreadsheets, PDFs, and work-order tools.
- A platform-door alarm, escalator outage, water intrusion, equipment-room alarm, visible trackside defect, obstruction, or repeat maintenance issue often lacks one exception ID, one owner, one timeline, one SOP, one verification packet, and one closure record.

## Why Now

China:

- By the end of 2025, China had 54 cities operating 343 urban rail lines, 11,710.3 km, 6,680 stations, and 33.24B annual passenger trips.
- MOT rules explicitly define hidden-danger investigation and rectification as closed-loop management, with requirements around risk databases, hidden-danger manuals, ledgers, verification, cancellation, and information sharing.
- The sector is moving from build-out to operations, renewal, and efficiency; operators face operating-cost pressure and subsidy dependence.
- AI + transport policy supports intelligent rail, inspection robots, monitoring, warning, intelligent O&M, and safety emergency use cases.

Global:

- FTA/Volpe estimated a U.S. transit state-of-good-repair backlog of about $140.2B in 2022 dollars.
- Network Rail CP7 allocates more than GBP 45B for operations, maintenance, and renewal from 2024-2029.
- European rail infrastructure managers report increasing climate and extreme-weather impact.
- Automated inspection and AI detection are increasingly accepted, but many inspection signals still fail to become closed maintenance actions.

## Product Workflow

1. Ingest: CCTV, station-equipment alarms, platform screen-door data, escalator/elevator status, BAS/FAS, ISCS, EAM/CMMS, mobile patrols, robot sensing, and contractor records.
2. Merge: create one exception ID by station, asset, timestamp, camera view, alarm type, and existing work order.
3. Classify: rank impact to passenger flow, operations, equipment, safety, flood prevention, compliance, and contractor SLA.
4. Dispatch: push the owner, SOP card, required evidence, deadline, spare-part hint, and escalation path.
5. Verify: use device recovery, field photos, robot reinspection, human acceptance, passenger-complaint trend, and OCC notes.
6. Close: update ledgers, audit exports, risk database, and repeat-defect analysis.
7. Learn: feed false positives, repeated defects, repair results, and final human verdicts into the anomaly library and LeRobot-compatible datasets.

## Market Wedge

Start narrow:

- One line or depot.
- 10-25 stations.
- Three to five high-frequency exception types: platform screen doors, escalators, water intrusion/flood prevention, equipment-room alarms, and visible trackside issues.
- Read-only integration plus mobile evidence capture and audit export.

Expand later:

- Network-level hidden-danger ledger.
- Contractor QA and invoice evidence.
- OCC delay attribution packages.
- Renewal and maintenance prioritization.
- Robot/drone inspection ingestion.
- Regulatory and service-quality reporting.

## Buyer Economics

Primary value drivers:

- Faster acknowledgement and shorter mean time to close eligible exceptions.
- Fewer overdue high-risk hidden dangers.
- Higher evidence completeness for closed exceptions.
- Less manual report assembly and reconciliation.
- Fewer duplicate or orphaned work orders.
- Better contractor acceptance and invoice evidence.
- Fewer repeated defects and better renewal prioritization.

Pilot:

- 90-120 days.
- Scope: one line or depot, 10-25 stations or 20-40 km, 80-150 users, three to five exception types.
- China price: RMB 280k-580k.
- Acceptance targets: 90%+ eligible exceptions logged, 95%+ closed items with complete evidence, 30% faster acknowledgement, 20% reduction in overdue high-risk items, 30% reduction in manual report assembly time.

Expansion assumptions:

- Per-line annual core: RMB 480k-1.2M.
- Network edition: RMB 2M-6M/year.
- Private cloud/on-prem setup: RMB 300k-1M one-time.
- Modules: sensor/robot ingestion, EAM integration, OCC delay attribution, contractor QA, renewal prioritization AI, and regulator/audit portal.

## Competition

RailLoop should integrate, not replace:

- Urban rail cloud, comprehensive supervision, OCC systems, ISCS, BAS/FAS, and EAM/CMMS.
- Video AI vendors and station-equipment diagnostics.
- Track geometry and rail inspection incumbents: ENSCO, MERMEC, Sperry, Herzog, Plasser & Theurer.
- Corridor AI/LiDAR and infrastructure monitoring: Cordel, Machines With Vision, KONUX, Senceive, Sensonic.
- Rolling-stock inspection portals: Duos, Wabtec KinetiX, Camlin Rail, and similar systems.
- Enterprise systems: IBM Maximo, SAP EAM, Hexagon, Bentley, Trimble, and contractor management tools.

Differentiation:

- Closure-first workflow layer.
- Unified exception ID across systems.
- SOP and risk-database mapping.
- Evidence standard for cancellation/acceptance.
- Local/private deployment option.
- LeRobot/Qualcomm edge path for repeatable robot-learning experiments.

## Qualcomm Fit

Rail operations need edge AI because station and depot environments have many cameras, strict privacy expectations, weak-network moments, short response windows, and local audit needs.

QNN/AI Hub candidate models:

- Platform screen-door and platform-edge anomaly detection.
- Escalator/elevator status classification.
- Water intrusion and floor hazard segmentation.
- Track fastener/object/cable-cover visual defect detection.
- Equipment-room analog gauge/state recognition.
- Acoustic/vibration anomaly classification.
- Multimodal priority model for exception routing.

## Safe Competition Demo

Demo scope:

- 2-3m modular low-voltage tabletop rail/metro scene.
- Platform, screen-door model, track bed, equipment-room prop, tunnel portal, cable tray, dummy third rail, dummy OLE mast, QR/AprilTag asset IDs, and swappable fault tiles.
- Fault tiles: missing fastener, loose clip, obstacle, gauge shim, water leak tray, thermal pad, asset-label mismatch, dirty/occluded marker, platform-door abnormal marker.
- 12-24V isolated supply, current limiting, fuses, physical E-stop, speed cap, clear acrylic guard, and disconnected rail-power props.
- Small rover or camera mast with onboard battery, RGB, downward camera, depth/ToF, thermal, microphone/vibration pickup, IMU, odometry, and safety interlock.
- ROS 2 inspection actions, evidence packet, mock CMMS ticket, human review, reinspection, and LeRobotDataset episode export.

Claims to avoid:

- Safe near live third rail or catenary.
- Works on active metro without possession/isolation.
- Replaces qualified inspectors.
- Certifies track safety.
- Detects all internal rail defects.
- Prevents derailments.
- Controls railway power, signal, train dispatch, or interlocking.
- Ready for unattended live-railway deployment.
- Exact Qualcomm NPU FPS before profiling on target hardware.

Safe claim:

> Tabletop low-voltage rail/metro exception-closure demo using multimodal sensing, ROS 2 action workflow, human-reviewed evidence packets, LeRobot-compatible data, and a candidate Qualcomm AI Hub/QNN edge path.

## Sources

- MOT 2025 urban rail operation data: https://www.mot.gov.cn/xinwen/jiaotongyaowen/202601/t20260129_4199263.html
- MOT urban rail hidden-danger rule: https://xxgk.mot.gov.cn/xzgfxwj/202411/t20241115_4159469.html
- MOT urban rail maintenance rule: https://xxgk.mot.gov.cn/xzgfxwj/202411/t20241115_4159468.html
- FTA Transit State of Good Repair National Backlog Analysis: https://www.transit.dot.gov/sites/fta.dot.gov/files/2025-01/Transit-State-of-Good-Repair-National-Backlog-Analysis_0.pdf
- Network Rail CP7 Delivery Summary: https://www.networkrail.co.uk/wp-content/uploads/2024/05/Network-Rail-CP7-Delivery-Summary.pdf
- ERA rail resilience and climate change: https://www.era.europa.eu/content/rail-resilience-climate-change
- UNIFE World Rail Market Study summary: https://www.unife.org/news/policymakers-and-industry-give-vote-of-confidence-as-global-rail-supply-market-continues-to-expand-despite-geopolitical-tensions/
- Qualcomm AI Hub: https://aihub.qualcomm.com/
- Qualcomm RB3 Gen 2 Development Kit: https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Network Rail third rail safety context: https://www.networkrail.co.uk/our-work/looking-after-the-railway/track/third-rail/
- OSHA control of hazardous energy: https://www.osha.gov/control-hazardous-energy
