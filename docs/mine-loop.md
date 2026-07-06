# MineLoop 智矿异常闭环

MineLoop is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames smart mining as an exception-closure problem: alarms, video AI, personnel location, SCADA, FMS, CMMS, drones, robots, slope monitoring, and tailings monitoring should become assigned work, verified fixes, evidence packets, and learning data.

Public page: https://qc-robotics-2026.pages.dev/mine-loop/

## One-Line Pitch

> 矿山不是缺报警，缺的是异常闭环。

MineLoop serves mine managers, safety directors, dispatch centers, equipment maintenance teams, and group-level safety/production/IT teams. It turns fragmented mine-site exceptions into accountable, auditable, closed-loop work orders.

## Problem

Mines already have many detection systems:

- Gas, ventilation, water, belt, vehicle, slope, tailings, and personnel-location monitoring.
- Video AI, SCADA, FMS, CMMS/EAM, drone surveys, robotic inspection, and manual reports.
- Group dashboards and regulatory reporting systems.

The gap is after detection:

- Who confirmed the exception?
- Which SOP applied?
- Who owns the work?
- Was the work completed?
- Did second inspection verify closure?
- Can the evidence support internal audit, regulatory reporting, insurance, and production review?

## Why Now

China:

- 2024 smart-mine guidance sets explicit 2026 targets around smart coal capacity, intelligent workfaces, equipment/robot substitution, and underground personnel reduction.
- 2026 NMSA materials emphasize safety-risk/hidden-danger ledgers, closed-loop management, monthly major-hidden-danger inspections, and quarterly reporting.
- Revised hidden-danger standards and risk-monitoring approaches make "预警-处置-反馈-销号" a direct product wedge.
- China deployment should be local/private: mine edge box + group private cloud + regulator-facing exports, with data kept in-mine or within the group.

Global:

- Critical minerals and energy-transition demand are increasing scrutiny on mining productivity and resilience.
- The largest miners still have technology budgets, but many have struggled to industrialize pilots.
- Autonomous haulage, drones, LiDAR, robotic inspection, collision avoidance, and remote operations have scaled; cross-system exception closure is still fragmented.

## Product Workflow

1. Sense: capture RGB, thermal, depth, vibration, current, gas, positioning, FMS, SCADA, slope/tailings, and robot state.
2. Merge: combine multiple alerts into one event card.
3. Rank: score by safety risk, production impact, equipment criticality, SLA, and evidence quality.
4. Assign: generate a work order with owner, SOP, deadline, and verification condition.
5. Verify: collect photos, video, telemetry, robot reinspection, and operator signoff.
6. Close: produce ledger, audit packet, regulatory fields, and LeRobot HIL dataset slices.
7. Learn: feed false positives, missed events, human corrections, and failed robot missions into the next model iteration.

## Market Wedge

Start with high-risk, high-downtime, regulated exception workflows:

- Conveyor and crushing: hot spots, belt drift, blockage, foreign object, transfer-point spillage, motor current spikes.
- Haulage: queueing, idle time, haul-road defects, spillage, abnormal stops, people/vehicle proximity.
- Slope and tailings: rainfall, displacement, cracks, turbidity, freeboard, threshold/TARP workflows.
- Underground inspection: ventilation, gas, water, personnel location, robot inspection, and equipment-state fusion.
- Group safety governance: hidden-danger closure rate, overdue events, repeated issues, evidence completeness.
- Overseas autonomous mines: cross-vendor closure across AHS, FMS, drones, robots, CAS, SCADA, and CMMS.

## Buyer Economics

Use hard ROI first:

- Conveyor/crushing downtime reduction.
- Haul-truck queue and idle reduction.
- Predictive maintenance and emergency work-order reduction.
- Fuel/electricity reduction.
- Faster hidden-danger ledgers, audits, and reports.

Avoid selling disaster prevention as the first payback case. Keep tailings, slope, and major incident reduction as risk-governance upside.

Pilot model:

- 8-12 week paid pilot: RMB 300k-800k per mine site.
- Connect 2-4 data classes: dispatch/FMS, CMMS/EAM, belt/PLC/SCADA, safety hidden-danger ledger, slope/tailings monitoring, video, or robot inspection.
- Success metrics: direct hard benefit at least 3x pilot fee, red-event MTTA under 10 minutes, key-event on-time closure above 90%, repeated/overdue exceptions down 30%+, evidence-packet generation time down 70%+.

Annual model:

- Platform base: RMB 800k-1.5M per mine site per year.
- Add asset packages by truck, belt-km, critical asset, slope/tailings facility, or safety-compliance package.
- Optional success fee on verified savings, capped to avoid procurement resistance.

## Competition

MineLoop should integrate, not replace:

- OEM autonomy: Komatsu FrontRunner, Cat MineStar Command, Sandvik AutoMine, Epiroc autonomous drilling, Liebherr/Fortescue AHS.
- Safety/situational awareness: Hexagon CAS and similar systems.
- Robotics/drones: Emesent, Exyn, Percepto, ANYbotics, Gecko, ABB/Point Laz.
- Systems of record: SAP, IBM Maximo, Pronto, Ellipse, ServiceNow, Hexagon EAM.

Differentiation:

- MineLoop is not another robot or another dashboard.
- It is the exception operating layer connecting detection, assignment, action, verification, audit, and model learning.

## Qualcomm Fit

MineLoop needs:

- Local AI in dusty, weak-network, safety-sensitive environments.
- Multimodal sensor fusion: RGB, thermal, depth, vibration, current, gas, positioning, and robot state.
- Multi-camera edge pipelines and private-network connectivity.
- AI Hub / QNN compile and profile evidence for detection, segmentation, depth, thermal anomaly, and sensor-fusion models.
- A path from competition tabletop prototype to industrial edge nodes.

## Safe Competition Demo

Demo scope:

- Desktop conveyor, sorting gate, slope rover area, transparent tailings mock tank, and low-voltage motor load box.
- RGB, thermal, depth/ToF, vibration/IMU, current/voltage, encoder, and limit-switch sensing.
- A small rover or XY gantry only performs low-force actions: approach, capture evidence, move foam/plastic objects, actuate a sorting gate, return home.
- ROS 2 actions for inspect, pause conveyor request, light sorting, evidence capture, and return home.
- Evidence packet with event ID, timestamps, telemetry, images, model version, QNN/AI Hub profile ID, ROS bag URI, LeRobot episode ID, hash, and operator approval.

Claims to avoid:

- Direct deployment in real mines, underground workings, or tailings dams.
- Explosion-proof, SIL, IEC 61508, certified safety, or functional-safety claims.
- Zero accidents, worker replacement, collapse prediction, or automatic accident handling.
- Qualcomm official certification or partnership unless separately granted.

Safe claim:

> 面向机器人比赛和教学演示的低压桌面矿山异常闭环原型，展示多模态感知、ROS 2 action 编排、人在回路确认、Qualcomm edge inference path、LeRobot HIL 数据和证据包复盘。

## Sources

- China smart-mine guidance: https://www.mem.gov.cn/gk/zfxxgkpt/fdzdgknr/202404/t20240430_486617.shtml
- NMSA closed-loop hidden-danger management: https://www.chinamine-safety.gov.cn/zfxxgk/fdzdgknr/tzgg/202606/t20260623_608824.shtml
- IEA Global Critical Minerals Outlook 2025: https://www.iea.org/reports/global-critical-minerals-outlook-2025
- PwC Mine 2026: https://www.pwc.com/gx/en/industries/energy-utilities-resources/publications/mine.html
- Komatsu 1000 autonomous haul trucks: https://www.komatsu.com/en-us/newsroom/2026/komatsu-becomes-first-oem-to-commission-1000-ultra-class-autonomous-haul-trucks
- MSHA powered haulage safety: https://www.msha.gov/safety-and-health/safety-and-health-initiatives/powered-haulage-safety
- Emesent mining robotics: https://www.emesent.com/industry/mining/
- Gecko mining robotics: https://www.geckorobotics.com/mining
- Qualcomm Robotics Processors: https://www.qualcomm.com/internet-of-things/applications/robotics-processors
- Qualcomm AI Hub: https://aihub.qualcomm.com/
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
