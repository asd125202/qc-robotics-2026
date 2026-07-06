# WaterLoop 水务异常闭环层

Public page: https://qc-robotics-2026.pages.dev/water-loop/

## One-Line Pitch

> 水务公司每年把数百亿美元埋在地下，我们把异常从检测带到已验证修复。

WaterLoop is a vendor-neutral water utility exception-closure layer. It does not replace SCADA, AMI, DMA, GIS, CMMS, LIMS, CCTV inspection, leak detection, hydraulic models, or field crews. It connects their signals into assigned, time-bound, evidence-backed, ROI-tracked operational closeout.

## Problem

Water utilities already have detection systems:

- SCADA, AMI/AMR, DMA, GIS, CMMS/EAM, CRM, LIMS/lab, weather, field photos, CCTV inspection, video, pump monitoring, and smart-water dashboards.

But the operating workflow is still broken:

- Which alert is real?
- Which pipe, pressure zone, valve, customer group, pump, or sewer basin is affected?
- Who owns the action?
- What is the SLA?
- What evidence proves closure?
- What value was recovered?
- Can the event support regulatory reporting and audit?

## Why We Solve It

Every unclosed water anomaly is water, money, trust, and compliance risk:

- Non-revenue water means water has already been abstracted, treated, pumped, and distributed but did not become revenue or service value.
- Pump anomalies waste energy and increase O&M cost.
- Sewer overflows and water-quality events create public, regulatory, and reputation pressure.
- Manual reporting consumes staff time and often lacks source-data lineage.
- The most valuable AI dataset is not the alert; it is the verified repair path.

WaterLoop should sell verified operational savings, not smart-water dashboards.

## Why Now

Global:

- Global non-revenue water is estimated at around 126 billion m3/year with about $50B/year economic impact.
- U.S. drinking-water infrastructure needs are estimated at about $625B over 20 years.
- U.S. water losses cost utilities billions of dollars annually, with most losses from real leakage/bursts.
- PFAS, stormwater/sewer overflow transparency, drought/flood resilience, and aging mains are increasing compliance pressure.
- AMI, pressure sensors, SCADA historians, GIS, and CCTV AI are creating more alerts than teams can close.

China:

- China targets urban public water-supply leakage <=9% by 2025.
- Leakage-control pilot cities must reach district-metering coverage by 2025; selected pilot areas must reach <=7%-8% leakage depending on baseline.
- The 2024 water-saving regulation says losses above national leakage-control standards cannot be included in public water utility tariff costs.
- Municipal equipment renewal through 2027 covers waterworks, secondary supply, wastewater monitoring/autocontrol, and city-lifeline IoT sensing.
- The 2026-2030 city-renewal cycle points toward large-scale underground-pipeline renovation and smart monitoring.

## Insight

Leak detection, AMI, SCADA, hydraulic modeling, and CCTV AI mostly answer: what might be wrong?

WaterLoop answers:

- What case is this?
- Who owns it?
- What action should happen today?
- What evidence proves it worked?
- What value did we recover?
- What should the model learn?

The moat is the “signal-to-repair” library for each utility.

## Solution

WaterLoop provides:

1. Observe: read SCADA, AMI, DMA, GIS, CMMS, CRM, LIMS, weather, CCTV, robot inspection, and edge sensors.
2. Correlate: combine alerts by pressure zone, asset, pipe age, valve state, customer impact, work-order history, and weather.
3. Decide: classify NRW/leak, apparent loss, pump anomaly, sewer overflow risk, water-quality drift, CCTV defect, or false alarm.
4. Act: write tasks to CMMS/mobile work, sampling plans, handover notes, customer-notice drafts, or inspection requests.
5. Verify: close only after flow/pressure recovery, lab sample, photo/video, CCTV, robot reinspection, or human signoff.
6. Learn: feed false positives, missed events, field outcomes, and closure evidence into LeRobot/CloudTwin datasets.

First-phase principle: read-only OT integration, human approval, no direct SCADA control.

## Product Wedge

Do not pilot the whole city. Start with one measurable unit:

- 1-3 DMAs.
- One pressure zone.
- One pump station.
- One sewer basin.
- One industrial water network.

90-day objective:

- Reduce minimum night flow or verified m3/day loss.
- Reduce alert-to-crew assignment time.
- Improve first-visit resolution.
- Reduce kWh/m3 for selected pump assets.
- Produce audit-ready evidence packets.

## Market

China version:

- Position as “漏损控制 + 厂网一体 + 城市生命线”.
- Buyers: water bureaus, housing/urban-rural construction bureaus, city-management/drainage bureaus, water affairs groups, wastewater operators, city-renewal platform SOEs, industrial parks.
- Requirements: local/private deployment, Chinese UI, DingTalk/WeCom workflow, domestic GIS/database options, 等保/信创/密评 posture, data residency, regulator-facing exports.

Overseas version:

- Position as NRW + exception closure for utilities that already have data but lack operational closeout.
- Targets: US/Canada/UK/EU/Australia utilities with 50k-1M connections, NRW >15%, aging mains, AMI/SCADA installed, or sewer overflow scrutiny.
- Requirements: Esri/Cityworks/Maximo/OpenGov/SCADA historian APIs, NPDES/SDWA/CCR/UWWTD exports, consultant-friendly audit packs, SOC 2/ISO-style security posture.

## Business Model

China pricing, excluding hardware:

- 90-day paid pilot: RMB 180k-600k, credited if converted.
- Starter county/small city: RMB 300k-800k/year.
- Standard city utility: RMB 800k-2.5M/year.
- Enterprise water group/private cloud: RMB 2.5M-8M/year.
- Implementation: RMB 200k-2M depending on SCADA/GIS/CMMS complexity.
- Optional success fee: 5%-12% of verified savings, capped.

Overseas pricing, excluding hardware:

- 90-day paid pilot: $35k-$120k.
- Mid-size utility subscription: $75k-$300k/year.
- Large utility/multi-module: $300k-$1.2M/year.
- Implementation: 15%-30% of year-one subscription.
- Optional success fee: 5%-15% of verified savings, capped.

Expansion modules:

- NRW/leakage.
- Pump energy.
- Sewer overflow.
- Water-quality incident workflow.
- CCTV/inspection defect closure.
- Regulatory reporting.
- Edge evidence nodes.

## ROI

Hard ROI formula:

```text
ROI = (annual verified benefit - annual WaterLoop cost) / annual WaterLoop cost
Payback months = 12 * year-one WaterLoop cost / annual verified benefit

Annual verified benefit =
  m3 real water saved * variable production cost
+ m3 recovered billed * tariff * collection rate
+ avoided breaks * average break cost
+ crew hours saved * loaded labor rate
+ kWh saved * electricity price
+ truck rolls avoided * cost per roll
+ reporting hours saved * loaded labor rate
+ hard-to-audit risk reduction kept separate as upside
```

90-day pilot KPIs:

- >90% selected assets mapped.
- >95% tag mapping for selected assets.
- 5%-15% minimum night flow reduction or validated m3/day saved.
- >60% precision on actionable alerts.
- 20%-40% reduction in alert-to-crew assignment time.
- >75% first-visit resolution for generated jobs.
- 3%-8% kWh/m3 reduction at selected pump assets without service violations.
- Mobile closeout completeness >90%.
- Annualized gross benefit at least 3x proposed annual software fee.

## Competition

Do not claim to be:

- Leak detector.
- AMI/MDM network.
- SCADA/HMI.
- GIS.
- Hydraulic model.
- Sewer CCTV AI.
- CMMS/EAM.
- Water-quality certified instrument.

Integrate with:

- Xylem/Xylem Vue/Sensus.
- Itron, Badger, Aclara.
- TaKaDu.
- FIDO and acoustic leak tools.
- Fracta, Bentley OpenFlows, Autodesk Info360.
- Esri.
- Trimble Unity/Cityworks.
- Seeq.
- Schneider/AVEVA and Siemens.
- RedZone, SewerAI, VAPAR-style inspection systems.

Wedge:

> WaterLoop closes the operational gap between detection and done.

Metrics:

- Exception aging.
- MTTA/MTTR.
- Duplicate suppression.
- Owner assignment.
- Evidence completeness.
- Reopened exceptions.
- Verified volume saved.
- CMMS/GIS feedback.

## Moat

- Resolution dataset: signals, root cause, actions, repairs, recovery curves, photos/videos, reports.
- Utility playbooks: valves, roads, sampling, notices, crews, SLA, regulatory fields.
- Integration lock-in: SCADA, AMI, GIS, CMMS, CRM, LIMS, CCTV, smart-water platform.
- Edge evidence: pump stations, valve vaults, pipe galleries, and inspection robots generate local proof.

## Qualcomm Fit

WaterLoop needs:

- Offline-first edge inference for pump stations, valve vaults, pipe galleries, construction sites, and mobile crews.
- Multimodal fusion: acoustic, RGB, depth, thermal, flow, pressure, current, turbidity, and position.
- Qualcomm AI Hub/QNN compile/profile path for leak-mask, acoustic classification, meter OCR, pump anomaly, and visual evidence models.
- ROS 2 action workflow for inspection, evidence capture, human approval, and episode export.
- LeRobotDataset episodes from tabletop HIL and future field inspection loops.

## Safe Competition Demo

Safe rig:

- 1-2 L reservoir.
- Clear silicone/PVC loop.
- 12V DC pump.
- Normally-closed valves or servo pinch valves.
- Bypass loop, leak simulation valve, flush-to-waste cup.
- Mechanical pressure relief.
- Inline fuse, GFCI upstream, catch tray, splash shield, drip loops.

Sensors:

- Main and branch flow.
- Upstream/downstream pressure.
- pH/turbidity demo sample cup.
- Pump current.
- RGB, depth, thermal.
- Leak tray sensor.

3-minute script:

1. Show clear low-voltage rig, E-stop, catch tray, and dashboard.
2. Run normal flow; display pressure, flow, turbidity, current, and camera feeds.
3. Trigger a small leak and cloudy slug.
4. System detects pressure drop, flow mismatch, visual leak mask, and turbidity rise.
5. Operator approves the suggested closure.
6. System lowers pump, isolates segment, opens bypass, flushes demo segment, then verifies recovery.
7. Ticket closes with before/after metrics and a LeRobotDataset episode.

Safe claims:

- Tabletop clean-water analog of water utility exception closure.
- Edge AI-assisted detection, supervised response, and verification.
- Qualcomm AI Hub/QNN path for exported models.
- LeRobot for dataset capture, teleoperation, and bounded policy experiments.

Avoid claims:

- Guarantees safe drinking water.
- Detects all leaks or contaminants.
- EPA/NSF/AWWA certified.
- Production-ready for municipal infrastructure.
- Replaces SCADA or operators.
- Fully autonomous public-health decision system.
- Qualcomm/Hugging Face/ROS endorsement.

## Sources

- Proparco NRW: https://www.proparco.fr/en/article/non-revenue-water-water-wasted-resource-wasted
- Bluefield US water losses: https://www.bluefieldresearch.com/ns/water-losses-cost-u-s-utilities-us6-4-billion-annually/
- EPA DWINSA: https://www.epa.gov/dwsrf/epas-7th-drinking-water-infrastructure-needs-survey-and-assessment
- China leakage target: https://www.ndrc.gov.cn/fggz/hjyzy/sjyybh/202202/t20220217_1315750.html
- China leakage pilots: https://www.ndrc.gov.cn/xwdt/tzgg/202203/t20220315_1319313_ext.html
- Water-saving regulation: https://www.mee.gov.cn/zcwj/gwywj/202403/t20240325_1069149.shtml
- Municipal infrastructure equipment renewal: https://www.ndrc.gov.cn/xwdt/ztzl/tddgmsbgxhxfpyjhx/gzdt/202404/t20240417_1365729.html
- EPA water energy: https://www.epa.gov/sustainable-water-infrastructure/energy-efficiency-water-utilities
- EPA PFAS: https://www.epa.gov/sdwa/and-polyfluoroalkyl-substances-pfas
- EPA SSO: https://www.epa.gov/npdes/sanitary-sewer-overflows-ssos
- Xylem Vue: https://www.xylem.com/en-us/brand/xylem-vue/
- TaKaDu CEM: https://www.takadu.com/
- FIDO AI: https://fido.tech/
- Qualcomm AI Hub Workbench: https://workbench.aihub.qualcomm.com/docs/
- Qualcomm RB3 Gen 2: https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
