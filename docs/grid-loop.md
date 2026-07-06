# GridLoop 配网异常闭环层

Public page: https://qc-robotics-2026.pages.dev/grid-loop/

## One-Line Pitch

> 全球不缺发电，真正卡住 AI、EV 和光伏的是配电最后一公里。

GridLoop is a vendor-neutral exception closure layer for distribution operations. It does not replace ADMS, OMS, DERMS, SCADA, AMI, GIS, EAM, protection systems, or inspection AI. It turns alerts, defects, DER constraints, voltage excursions, outage follow-ups, inspection findings, and model mismatches into assigned, evidenced, auditable closure.

## Problem

Distribution utilities already have:

- ADMS, OMS, SCADA, AMI, GIS, EAM/CMMS, DERMS, vegetation platforms, drone inspection, robot inspection, weather, field crews, and regulatory reports.

But operational closure remains slow:

- Which alert is real?
- Which feeder, transformer, switch, customer group, DER, or asset is affected?
- Who owns the action?
- What evidence is needed?
- Was the issue actually fixed?
- Did it reopen?
- Was the grid model wrong?
- Can the result support reliability reporting, wildfire mitigation evidence, rate-case justification, or DER interconnection review?

## Why We Solve It

Grid construction takes 5-15 years, but grid-edge exceptions happen today.

GridLoop helps existing distribution networks carry more load with fewer failures:

- Faster fault and likely-cause localization.
- Better truck-roll targeting.
- Closed-loop inspection defects.
- Better vegetation and wildfire mitigation evidence.
- Transformer and feeder overload prioritization.
- DER/EV hosting constraints turned into follow-up actions.
- Regulatory and investment evidence packages.

## Why Now

Global:

- ASCE 2025 gives U.S. energy infrastructure a D+ and notes most service interruptions originate in distribution systems.
- EIA reports U.S. customers averaged almost 11 outage hours in 2024, with major weather events driving most outage duration.
- IEA projects massive renewable additions through 2030, with distributed PV a large share.
- Global public EV charging points exceeded 7 million by the end of 2025, with China over 65% of the total.
- Transformer shortages and long lead times make software/edge visibility valuable while hardware catches up.

China:

- China policy frames the new power system as source-grid-load-storage coordination.
- The 2024-2027 new power system action plan requires provincial distribution-grid upgrades around carrying capacity, resilience, open-capacity warning, charging-facility capacity, and smart dispatch.
- 2025 national grid investment was RMB 639.5B, with 110kV and below distribution-grid investment around RMB 321.8B.
- China targets 28M+ charging facilities and 300GW+ public charging capacity by the end of 2027.
- Energy infrastructure is covered by critical-information-infrastructure/data-security expectations, so deployment must be local/private and security-aware.

## Insight

The valuable dataset is not raw telemetry. It is closure:

- Which anomaly was real?
- Which evidence proved it?
- Which crew or robot inspected it?
- Which action worked?
- How long did it take?
- Did it reopen?
- Did the grid model need correction?

Every closed exception improves the distribution operations model.

## Solution

GridLoop provides a closure layer:

1. Normalize: convert events from ADMS/OMS/AMI/GIS/EAM/DERMS/inspection systems into common exceptions.
2. Deduplicate: group repeated alarms by topology, time window, customers, assets, weather, and evidence.
3. Assign: create owner, SLA, evidence requirements, suggested work order, and approval path.
4. Verify: close only with telemetry recovery, AMI voltage recovery, thermal rescan, field photo, crew verdict, or complaint decline.
5. Learn: track time-to-close, reopen, false positive, root cause, recurring issue, and model correction.

First-phase boundary:

- Read-only OT integration.
- Human approval.
- No protection logic.
- No autonomous feeder switching.
- No ADMS/DERMS replacement claims.

## Product Wedge

Do not start with the whole grid. Start with one high-frequency closure loop:

- Inspection defect closure.
- AMI/grid-edge power-quality exception closure.
- DER constraint follow-up.
- GIS/ADMS model correction loops.
- Vegetation/wildfire mitigation audit trails.
- Worst-feeder outage intelligence.

Pilot scope:

- 5-20 feeders.
- 500-5,000 assets.
- 12-24 months baseline OMS/AMI/GIS history.
- Matched control feeders when possible.

## Market

China version:

- Position as “源网荷储协同下的配网异常闭环”.
- Buyers: provincial/municipal grid companies, city/county power-supply bureaus, grid digital subsidiaries, industrial parks, data centers, charging operators, PV/storage developers, VPP aggregators, local energy-service platforms.
- Procurement language: 提升承载力、可靠性、自愈、可观可测可调可控、源网荷储协同.
- Requirements: local/on-prem/private cloud, CII/data-security posture, integration with dispatch/SCADA/AMI/GIS/95598, domestic SI/design institute ecosystem.

Overseas version:

- Position as reliability + vegetation/wildfire + DER/EV exception closure.
- Buyers: VP Distribution, COO, Grid Modernization, Reliability, Vegetation/Wildfire, Asset Management, DER Planning, Storm Response, Regulatory Affairs.
- Target utilities facing reliability penalties, wildfire scrutiny, worst-feeder programs, storm restoration issues, or EV load growth.

## Business Model

Modules:

- Outage intelligence.
- Vegetation/wildfire risk closure.
- Transformer/feeder capacity.
- Inspection AI closure.
- Storm/restoration.
- Regulatory reporting.

Pricing:

- China county/city pilot: RMB 100k-500k.
- China county/city annual software: RMB 300k-2M.
- China provincial rollout: RMB 2M-10M+ annually.
- Overseas small utility/co-op pilot: $50k-$150k.
- Overseas small utility annual: $75k-$250k.
- Overseas mid/large IOU/DSO annual: $300k-$1.5M+ by module.
- Enterprise/national DSO: $1M-$5M+.
- Optional success fee: 5%-10% of verified direct savings, capped.

Hardware and field services can be sold through qualified partners.

## ROI

Annual benefit:

```text
Benefit =
  avoided customer interruption value
+ avoided truck rolls * fully loaded truck-roll cost
+ avoided vegetation events * average event cost
+ vegetation budget * efficiency gain
+ avoided transformer failures * failure cost
+ deferred capex * carrying cost
+ avoided inspection cost
+ storm overtime / mutual-aid savings
+ reporting hours saved * loaded labor rate
+ regulatory incentives or avoided penalties
```

ROI:

```text
Annual ROI = (annual benefit - annual GridLoop cost) / annual GridLoop cost
Payback months = one-time implementation cost / monthly net benefit
```

90-day KPIs:

- >95% GIS/OMS/AMI/SCADA asset/customer/feeders matched.
- >85% precision for high-severity vegetation/asset alerts.
- Fault localization within 100-300m where sensor/AMI density supports it.
- 10%-20% fewer diagnostic truck rolls on pilot feeders.
- 30%-50% reduction in time to identify likely cause/location.
- Top 5%-10% risky vegetation spans validated in field and converted to work orders.
- 7-day transformer peak forecast MAPE <10%-15%.
- DER/EV hosting pre-screen reduced from weeks to days.
- Inspection cost per mile/structure reduced 30%+ vs baseline.
- Monthly audit pack with CMI/SAIDI/SAIFI, causes, actions, and evidence trail.
- Annualized benefit/cost >2x.

## Competition

Do not claim:

- Autonomous grid.
- Single pane of glass.
- ADMS replacement.
- DERMS replacement.
- Digital twin.
- Inspection AI.
- Utility-grade protection relay/recloser.
- FLISR replacement.

Integrate with:

- Schneider EcoStruxure ADMS / DERMS.
- Siemens Spectrum Power ADMS / Gridscale X.
- GE Vernova GridOS.
- Oracle Utilities NMS / ADMS.
- AspenTech/OSI.
- Hitachi Energy Network Manager.
- Itron and Landis+Gyr.
- Uplight/AutoGrid, Smarter Grid Solutions, Camus.
- AiDash, Neara, LineVision, Prisma Photonics, Noteworthy AI, Buzz Solutions, eSmart Systems, Gridware, Heimdall.

Wedge:

> Vendor-neutral exception closure for distribution operations.

## Moat

- Topology-aware exception graph.
- Closure labels from work orders, inspections, customer complaints, telemetry recovery, and reopen events.
- Workflow embedding in ADMS/OMS/EAM/GIS/crew processes.
- Edge evidence from robots, trucks, substations, and weak-network feeder points.
- Local utility playbooks and regulatory reporting logic.

## Qualcomm Fit

GridLoop needs:

- Edge AI for substations, distribution rooms, utility trucks, drone/robot inspection, and storm response.
- Multimodal inference: RGB, thermal, acoustic, voltage/current, IMU, and topology context.
- ROS 2 actions for robot inspection and evidence capture.
- Qualcomm AI Hub/QNN path for thermal hotspot, vegetation segmentation, asset detection, acoustic anomaly, and telemetry anomaly models.
- LeRobotDataset episodes from safe tabletop HIL and future inspection workflows.

## Safe Competition Demo

Demo concept:

- 24V tabletop visual feeder.
- OpenDSS or GridLAB-D digital feeder driving simulated scenarios.
- Current-limited Class 2/LPS supply where possible, branch fuses/eFuses, E-stop, and clear cover.
- Feeder segments A/B/C, normally open tie, EV load emulator, solar emulator, storage emulator, adjustable load bank, and fault/exception injector.
- Low-voltage relay/MOSFET “breakers”.
- Robot/gantry/pan-tilt camera inspection analog, not a live-grid drone.
- Per-segment V/I telemetry, relay state, temperature, RGB, thermal, and robot status.

3-minute script:

1. Show normal feeder with EV, solar/storage/load, telemetry, and power-flow animation.
2. Trigger EV inrush or hot-connector prop; UI shows voltage sag, current spike, relay open, lost load.
3. Dispatch LeRobot inspection analog to read asset tag and capture visible/thermal evidence.
4. QNN model flags no physical hazard or thermal hazard.
5. Safety checklist runs: voltage safe, current safe, thermal below threshold, contact state known, robot clear, operator approval required.
6. Demonstrate one blocked condition, then clear it.
7. Operator approves low-voltage relay closure; load restores; event closes with evidence and LeRobotDataset episode.

Safe claims:

- Low-voltage HIL demonstration of feeder exception handling.
- PMU-inspired synchronized telemetry, not IEEE C37.118 compliant PMU.
- On-device AI inference path using Qualcomm AI Hub/QNN.
- LeRobot-based inspection policy for tabletop robot/drone analog.
- Operator-in-the-loop deterministic safety-gated relay simulation.

Avoid:

- Autonomous grid restoration.
- Utility-grade protection relay/recloser.
- Safe for live distribution equipment.
- NERC/CIP, UL, IEC, NFPA, or utility interconnection compliance.
- Validated outage reduction on real feeders.

## Sources

- ASCE Energy 2025: https://infrastructurereportcard.org/wp-content/uploads/2025/03/Energy.pdf
- EIA outage duration: https://www.eia.gov/todayinenergy/detail.php?id=66744
- IEA Renewables 2025: https://www.iea.org/reports/renewables-2025/renewable-electricity
- IEA EV charging 2026: https://www.iea.org/reports/global-ev-outlook-2026/electric-vehicle-charging-chap-6-and-10
- WoodMac transformer shortage: https://www.woodmac.com/press-releases/power-transformers-and-distribution-transformers-will-face-supply-deficits-of-30-and-10-in-2025/
- China distribution-grid high-quality development: https://www.ndrc.gov.cn/xxgk/zcfb/tz/202403/t20240301_1364313.html
- New power system action plan: https://www.ndrc.gov.cn/xwdt/tzgg/202408/P020240806534738672970.pdf
- China Power Development Report 2026: https://www.nea.gov.cn/20260701/52eef0c7dc2c43968e411487618aaf06/c.html
- China charging infrastructure action: https://www.ndrc.gov.cn/xxgk/zcfb/tz/202510/P020251015595398499456.pdf
- Schneider ADMS: https://www.se.com/us/en/product-range/61751-ecostruxure-adms/
- GE Vernova GridOS ADMS: https://www.gevernova.com/software/products/gridos/advanced-distribution-management-system
- Qualcomm AI Hub compile: https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- Qualcomm RB3 Gen 2: https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- ROS 2 Actions: https://docs.ros.org/en/humble/Concepts/Basic/About-Actions.html
- LeRobot: https://github.com/huggingface/lerobot
