# MineLoop 智矿异常闭环层

Public page: https://qc-robotics-2026.pages.dev/mine-loop/

## One-Line Pitch

> 矿山已经有无人矿卡和智能大屏，真正缺的是把异常变成已验证的行动。

MineLoop is a mixed-vendor mine exception management layer. It does not replace FMS, SCADA, CAS, CMMS, slope/tailings monitoring, drones, robots, or OEM autonomy systems. It connects them into one accountable loop: observe, correlate, decide, act, verify, learn.

## Problem

Modern mines have many systems that detect problems:

- Dispatch/FMS, autonomous haulage, CAS, PLC/SCADA, conveyor protection, video AI, personnel positioning, slope radar, tailings monitoring, drones, inspection robots, CMMS/EAM, manual reports.

But after detection, the workflow is broken:

- Who confirmed the event?
- Which SOP applies?
- Who owns the action?
- Was the action completed?
- Did a second inspection verify closure?
- What was the production and financial impact?
- Can the evidence support regulatory reporting, group audit, insurance, and restart approval?

## Why We Solve It

Mine exception closure hits four budgets at once:

- Safety governance: hidden-danger dynamic clearing, ledgers, five responsibilities, acceptance, closeout, review.
- Production: crusher/conveyor downtime, haulage queueing, idle fleet hours, delayed restart.
- Maintenance: PdM alerts must become work orders, planned windows, parts, and verification.
- Group management: multi-site benchmarking, overdue issue tracking, standardization, evidence quality.

The product should be sold as closed-loop operational loss recovery, not as a generic dashboard or AI platform.

## Why Now

China:

- Smart-mine policy targets 2026 for data interconnection, intelligent disaster warning, intelligent capacity, robot substitution, and underground personnel reduction.
- The 2024-2026 campaign makes “重大事故隐患动态清零” a workflow requirement: databases, list management, dynamic updates, shared information,整改销号.
- Non-coal mines have explicit monthly checks, ledgers, “五落实”,整改验收, and quarterly reporting duties.
- Deployment must be local/private: mine edge box + group private cloud + regulator-facing exports.

Global:

- PwC Mine 2026 reports 2025 revenue of $909B and net profit of $120B for the Top 40 miners.
- IEA expects major critical-mineral demand growth and around $500B of new mine capex by 2040 under STEPS.
- Autonomous haulage, drones, LiDAR, robotics, CAS, and remote operations have scaled, but cross-vendor exception closure remains fragmented.
- Downtime remains a large and auditable profit pool.

## Insight

After automation scales, the most valuable mine dataset is not the alert itself. It is the full closure path:

- Which alerts were correlated?
- Which person approved the action?
- Which robot or worker inspected it?
- What evidence proved closure?
- Did production recover?
- Did the same issue repeat?

That loop becomes the training data for the next generation of mine robotics and edge AI.

## Solution

MineLoop adds a neutral layer above existing systems:

1. Observe: ingest FMS/OEM telemetry, CAS, video AI, historian/SCADA, CMMS, slope/tailings monitoring, personnel positioning, drones, and robots.
2. Correlate: build an event graph across asset, location, shift, operator/team, SOP, hazard, work order, and production impact.
3. Decide: recommend owner, priority, deadline, SOP, escalation rule, and verification condition.
4. Act: create/update tasks in approved systems such as CMMS work orders, inspection requests, handover notes, risk reviews, FMS advisories, or robot missions.
5. Verify: close events only after evidence, second inspection, telemetry recovery, or human signoff.
6. Learn: feed false positives, missed events, human corrections, failed robot missions, and closure outcomes into LeRobot/CloudTwin datasets.

## Product Wedge

Start with one mine, one bottleneck, one measurable loss pool:

- Conveyor/crusher downtime.
- Haulage queue/idle.
- Critical asset predictive maintenance.
- Slope/tailings threshold and TARP closure.
- Hidden-danger ledger and safety audit packet.

The first deployment should not promise a full digital twin. It should prove a 90-day exception closure package that reduces loss and produces audit-ready evidence.

## Market

China version:

- Position as “重大隐患动态清零 + 双重预防 + 集团台账监管”.
- Sell group-first, mine-second.
- Support local/private deployment, data-residency posture, Chinese safety terminology, regulator-facing exports, and connectors to safety monitoring, personnel positioning, GIS, SCADA, dispatch, video AI, and CMMS.

Global version:

- Position as mixed-vendor mine exception management.
- Target open-pit metals, coal, aggregates, and mineral processing sites with existing FMS/OEM automation, 20+ mobile assets, bottleneck fixed plant, remote operations, or visible safety-action backlog.

## Business Model

Recommended pricing:

- 90-day paid pilot: RMB 300k-800k per China mine, or $75k-$150k per overseas site.
- Core site SaaS: RMB 800k-1.5M per mine per year, or $120k-$300k per site per year.
- Production/dispatch package: site fee plus mobile asset fee.
- Fixed plant package: per critical conveyor/crusher/pump/fan asset.
- Edge node: hardware one-time fee plus annual edge subscription.
- Group enterprise layer: multi-site governance, benchmarking, SSO, audit, and reporting.
- Optional success fee: 5%-10% of audited savings, capped.

ROI formula:

```text
Annual benefit =
  avoided downtime hours x bottleneck margin/hour
+ reduced queue/idle hours x fuel/wear/operator/productive-hour value
+ avoided failures x downtime, repair, expediting, and overtime savings
+ admin hours saved x fully loaded labor rate
+ risk-adjusted safety/compliance savings

Net ROI = (annual benefit - annual MineLoop cost) / annual MineLoop cost
Payback months = upfront + first-year cost / monthly verified benefit
```

## 90-Day Pilot KPIs

- Target asset data coverage >90%.
- Critical events assigned within one shift >90%.
- High-risk hidden-danger closure by due date >85%.
- Overdue high-risk actions down 40%-60%.
- Crusher/conveyor unplanned downtime down 10%-20% normalized.
- Queue/idle hours at the chosen bottleneck down 10%-20%.
- Maintenance work-order cycle time down 15%-30%.
- Evidence packet/reporting admin time down 30%-50%.
- Annualized verified value at least 3x pilot fee.

## Competition

MineLoop should integrate, not replace:

- OEM autonomy: Komatsu FrontRunner, Cat MineStar Command, Sandvik AutoMine, Epiroc Open Autonomy.
- FMS/dispatch: Komatsu DISPATCH, Wenco, Hexagon OP Pro, Micromine Pitram, Cat MineStar Fleet.
- CAS/safety: Hexagon MineProtect, Wabtec CAS, Strata HazardAVERT, Becker PDS, Cat MineStar Detect.
- Inspection: Emesent, Exyn, Percepto, ANYbotics, Gecko.
- Slope/tailings: GroundProbe, IDS GeoRadar, Reutech, Canary Systems, Silixa.
- CMMS/EAM: SAP, IBM Maximo, Hexagon EAM, RPMGlobal AMT.
- Remote operations: Rio Tinto, BHP, Vale, ABB, AVEVA style operations centers.

Claim boundary:

- Do not claim autonomous haulage, OEM-agnostic machine control, Level 9 CAS, certified safety, slope/tailings early warning authority, FMS replacement, CMMS system of record, drone/robot autonomy stack, SCADA control, or guaranteed safety/productivity improvement.

## Moat

- Exception graph: asset, location, shift, team, SOP, evidence, work order, verification, and financial impact.
- Workflow lock-in: integrations with CMMS, FMS, SCADA, safety ledgers, dispatch, handover, and regulator exports.
- HIL dataset: human approvals, false positives, missed events, robot failures, verification failures.
- Partner surface: a neutral layer that OEMs, integrators, robot vendors, 5G providers, and EAM vendors can cooperate with.

## Qualcomm Fit

MineLoop needs:

- Local AI under weak network conditions.
- Multimodal edge fusion: RGB, thermal, depth, vibration, current, gas, positioning, and robot state.
- ROS 2 integration for sensors, actions, evidence capture, and robot tasks.
- Qualcomm AI Hub/QNN compile and profile workflow for edge inference.
- A bridge from cloud training to on-site robotic closure loops.

## Safe Competition Demo

Safe desktop rig:

- 12/24V DC tabletop conveyor.
- Current-limited supply, fuse, hardwired mushroom E-stop, guards over rollers/pulleys/nip points.
- Foam foreign objects only.
- Simulated belt drift using color edge marker or low-force servo.
- Simulated bearing fault using a guarded dummy bearing block, low-watt heater or LED thermal target, temperature sensor, thermal camera, IMU, and small vibration motor.

Demo script:

1. Show guarded rig, E-stop, foam-only objects, and dashboard.
2. Run normal belt with RGB/depth/thermal/current/vibration status.
3. Drop foam object; detect, stop, ask human approval, remove with gantry, verify closure.
4. Trigger simulated belt drift; human approves correction, camera verifies centered state.
5. Trigger current/vibration anomaly; system opens maintenance exception.
6. Trigger thermal bearing simulation; system closes only after cooldown or operator acknowledgment.
7. Show one recorded ROS bag/exported LeRobotDataset episode.

Safe claim:

> 面向机器人比赛和教学演示的低压桌面矿山异常闭环原型，展示多模态感知、ROS 2 action 编排、人在回路确认、Qualcomm edge inference path、LeRobot HIL 数据和证据包复盘。

Avoid claims:

- MSHA/OSHA certification or compliance.
- Prevents injuries, guarantees safety, replaces inspectors/operators.
- Underground deployment, intrinsically safe, explosion-proof, SIL/PL/functional-safety certification.
- Detects all hazards/failures or autonomously closes mine exceptions.
- Qualcomm-certified product.

## Sources

- China smart-mine guidance: https://www.mem.gov.cn/gk/zfxxgkpt/fdzdgknr/202404/t20240430_486617.shtml
- Hidden-danger dynamic clearing campaign: https://www.mem.gov.cn/gk/zfxxgkpt/fdzdgknr/202402/t20240222_478449.shtml
- Non-coal hidden-danger closure requirements: https://www.chinamine-safety.gov.cn/zfxxgk/fdzdgknr/tzgg/202412/t20241218_522936.shtml
- IEA Global Critical Minerals Outlook 2025: https://www.iea.org/reports/global-critical-minerals-outlook-2025/overview-of-outlook-for-key-minerals
- PwC Mine 2026: https://www.pwc.com/gx/en/industries/energy-utilities-resources/publications/mine.html
- Komatsu FrontRunner: https://www.komatsu.com/en-us/technology/smart-mining/loading-and-haulage/autonomous-haulage-system
- Komatsu DISPATCH case: https://www.komatsu.com/en-us/case-studies/dispatch-fleet-management-system-helps-mine-optimize-its-haulage
- Wipro conveyor downtime: https://www.wipro.com/natural-resources/predictive-failure-model-for-conveyor-belt-systems/
- Rockwell mining APM downtime: https://literature.rockwellautomation.com/idc/groups/literature/documents/wp/min-wp006_-en-p.pdf
- Qualcomm AI Hub Workbench: https://workbench.aihub.qualcomm.com/docs/
- Qualcomm Robotics ROS: https://www.qualcomm.com/developer/project/robotics-ros
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- ONNX Runtime QNN EP: https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
