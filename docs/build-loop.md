# BuildLoop 安闭环

BuildLoop is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames construction safety operations as an exception-closure problem: fall-edge hazards, missing guardrails, PPE exceptions, crane/exclusion-zone entry, temporary electrical hazards, hot-work/fire surrogates, confined-space controls, and subcontractor remediation evidence should become owned, verified, auditable cases.

Public page: https://qc-robotics-2026.pages.dev/build-loop/

## One-Line Pitch

> 工地安全异常，件件闭环。

BuildLoop serves general contractors, owners, project safety managers, supervisors, subcontractor managers, insurers, and risk-control teams. The product unit is not an alert. It is a closed safety exception with responsibility, deadline, evidence, and reinspection.

## Problem

Construction sites already have many signals:

- Cameras, mobile patrol photos, smart-site platforms, worker reports, supervisor inspections, subcontractor chat groups, EHS software, regulator templates, and insurer/risk-engineering checklists.
- These systems can see risk, but the operational break is after discovery: who owns it, how fast it is assigned, whether it was actually fixed, whether evidence is complete, and whether it recurs.
- Safety teams often lose time to screenshots, phone calls, spreadsheets, WeChat/group messages, and missing audit evidence.

## Why Now

Global:

- OSHA's construction Focus Four highlights falls, caught-in/between, struck-by, and electrocution as core fatal-risk categories.
- U.S. BLS 2024 fatal-injury data still shows high construction and extraction occupational fatalities.
- Injury and workers' compensation costs make leading indicators valuable to owners, insurers, and contractors.
- Construction software, AI safety, reality capture, and robotics have proven buyers exist, but alert-to-remediation closure remains fragmented.

China:

- The Safety Production Law and construction safety regulations require hidden-danger investigation, records, responsibility, and rectification.
- The 2024 major-hazard standard gives a current checklist for housing and municipal construction major hidden dangers.
- The 2024-2026 safety-production campaign and MOHURD construction actions emphasize major-hazard dynamic clearing, closed-loop rectification, databases, digital warning, and insurance/risk-prevention mechanisms.
- China deployment should use official language: `重大事故隐患动态清零`, `隐患排查、整改、督办、销号闭环`, `双重预防机制`, `责任到人、履职留痕`, `危大工程全过程管控`, and `安责险事故预防服务`.

## Product Workflow

1. Ingest: fixed cameras, mobile patrols, rover/robot inspection, worker reports, thermal/depth/audio surrogates, project organization table, and subcontractor list.
2. Detect: PPE marker, fall-edge/guardrail, exclusion-zone, temporary electrical, hot-work/fire surrogate, scaffold, material-staging, and confined-space control exceptions.
3. Assign: map exception to zone, floor, trade, subcontractor, responsible person, SLA, severity, required evidence, and reviewer.
4. Remediate: subcontractor or responsible team uploads fix evidence and comments.
5. Verify: safety manager/supervisor reviews before/after evidence, location, timestamp, signature, and optional robot revisit.
6. Close: update hidden-danger ledger, weekly report, subcontractor scorecard, recurrence analysis, and regulator/insurer export.
7. Learn: false positives, rejected evidence, recurrence, and reinspection results feed the anomaly library and LeRobot-compatible datasets.

## Market Wedge

Start narrow:

- One to three jobsites.
- Three to five camera/inspection zones.
- Visible, high-frequency safety exceptions: fall-edge/guardrail, PPE, crane/equipment exclusion zone, temporary electrical/trip hazard, hot-work/fire-watch surrogate, and high-risk patrol findings.
- Mobile remediation and reinspection evidence.

Expand later:

- Dangerous subprojects (`危大工程`) evidence chain.
- Owner/group dashboard.
- Regulator export.
- Subcontractor scorecard.
- Insurance/risk-prevention package.
- Quality defects, schedule variance, and civilized-construction workflows.

## Buyer Economics

Primary value drivers:

- Lower high-risk open-days.
- Faster assignment and closure.
- Lower overdue high-risk exception count.
- Higher evidence completeness.
- Less inspection/report/audit preparation labor.
- Fewer subcontractor disputes and clearer accountability.
- Lower stop-work, rework, and schedule-risk exposure.
- Better insurer/risk-engineering data and renewal discussions.

Pilot:

- 90 days.
- Scope: one to three jobsites, project safety team, supervisors, major subcontractors, mobile app, evidence ledger, weekly dashboard, and ROI report.
- China price: RMB 80k-180k for the pilot.
- U.S. price assumption: $15k-$30k pilot.
- Conservative success criteria: 95%+ high-risk exceptions assigned within 24h, 85%+ high-risk exceptions closed within SLA, average closure time down 30-50%, overdue high-risk open-days down 50%+, audit/report prep time down 30%+, evidence completeness above 95%, repeat hazard rate down 20%+.

## Competition

BuildLoop should integrate, not replace:

- Construction management and safety modules: Procore, Autodesk Build, Oracle Construction Intelligence, HammerTech, Raken, Safesite, HCSS Safety.
- EHS and contractor compliance: SafetyCulture, KPA, Cority, Intelex.
- AI safety and vision: viAct, Voxel, Intenseye, Oracle/Newmetrix.
- Reality capture and progress AI: OpenSpace, DroneDeploy, Buildots, Doxel.
- Construction robots: Dusty Robotics, Built Robotics, Canvas/JLG, and similar narrow-task robots.

Differentiation:

- Closure-first safety exception workflow.
- Responsibility and subcontractor accountability.
- High-risk open-days as a measurable KPI.
- Evidence packet and regulator/insurer export.
- Local/edge deployment option for weak-network and privacy-sensitive jobsites.
- LeRobot/Qualcomm edge path for repeatable robot-safety observation demos.

## Qualcomm Fit

Construction sites need edge AI because networks are unreliable, video is privacy-sensitive, alerts need low latency, and robots need on-device inference.

QNN/AI Hub candidate models:

- Worker/PPE marker detection.
- Equipment/exclusion-zone detection.
- Guardrail/fall-edge/walkway segmentation.
- Temporary electrical/trip hazard detection.
- Thermal/fire surrogate classification.
- Audio alarm/tool-noise surrogate classification.
- Lightweight crop classifier for hard-hat/vest marker presence.

## Safe Competition Demo

Demo scope:

- 1.5m x 1m tabletop construction site.
- Foam-board terrain, taped zones, mock scaffolding, removable guardrail tokens, toy equipment, mini worker markers, and fixed edge camera.
- Low-speed rover with physical boundary, bumper, wheel guards, geofence, remote E-stop, RGB, overhead camera support, depth/ToF, thermal camera, microphone, IMU, and odometry.
- PPE marker missing, proximity-zone entry, fall-edge/guardrail missing, fire LED/warm pack surrogate, and 5V electrical prop/trip hazard.
- No flame, smoke, aerosol, fuel, mains voltage, energized conductor, load-bearing scaffold, or real fall/electrical/fire scenario.
- ROS 2 patrol, evidence, closure, reinspection, and export actions.
- Human review required before closure; robot only observes and revisits.

Claims to avoid:

- Prevents accidents.
- OSHA/MOHURD compliant or guarantees compliance.
- Detects all construction hazards.
- Certified safety system.
- Replaces safety officers or supervisors.
- Real fire/electrical/fall detection.
- Autonomous enforcement around workers.
- Production-ready for active construction sites.
- Exact Qualcomm NPU FPS before profiling on target hardware.

Safe claim:

> Tabletop low-risk construction safety anomaly-closure demo using multimodal sensing, ROS 2 workflow, human-reviewed evidence packets, LeRobot-compatible data, and a candidate Qualcomm AI Hub/QNN edge path.

## Sources

- OSHA Focus Four construction hazards: https://www.osha.gov/training/outreach/construction/focus-four
- BLS fatal occupational injuries 2024: https://www.bls.gov/news.release/pdf/cfoi.pdf
- NSC work injury costs: https://injuryfacts.nsc.org/work/costs/work-injury-costs/
- OSHA penalties: https://www.osha.gov/penalties
- Safety Production Law: https://www.mem.gov.cn/fw/flfgbz/fg/202107/t20210716_416558.shtml
- MOHURD 2024 major hidden-danger standard PDF mirror: https://www.nbjz.org.cn/upload/1/editor/1737526246958.pdf
- Safety-production three-year action: https://www.mem.gov.cn/gk/zfxxgkpt/fdzdgknr/202402/t20240222_478449.shtml
- Safety production liability insurance measures: https://www.mem.gov.cn/gk/zfxxgkpt/fdzdgknr/202504/t20250402_531687.shtml
- Qualcomm AI Hub: https://aihub.qualcomm.com/
- Qualcomm Robotics ROS: https://www.qualcomm.com/developer/project/robotics-ros
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
