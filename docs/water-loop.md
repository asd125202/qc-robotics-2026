# WaterLoop 水务异常闭环

WaterLoop is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames water utility operations as an anomaly-closure problem: leaks, pressure drops, pump anomalies, water-quality drift, sewer/stormwater risk, customer calls, and field evidence should become owned, verified, learnable cases.

Public page: https://qc-robotics-2026.pages.dev/water-loop/

## One-Line Pitch

> 让每一次水务异常，都有闭环。

WaterLoop serves utility dispatchers, non-revenue-water teams, pump-station operators, sewer/stormwater teams, field crews, and compliance owners. The product unit is not an alert. It is a resolved anomaly with evidence.

## Problem

Water utilities already have many data sources:

- SCADA, AMI/AMR, GIS, CMMS/EAM, CRM/customer calls, lab/LIMS, weather, field photos, CCTV inspection, and smart-water dashboards.
- These systems see signals, but people still chase context across tools and spreadsheets.
- A pressure drop, night-flow spike, pump anomaly, turbidity drift, customer call, or sewer-level alarm often lacks one owner, one timeline, one action path, and one verification packet.

## Why Now

Global:

- EPA's 7th drinking-water needs survey estimates about $625B needed over 20 years for U.S. drinking-water infrastructure.
- AWWA's 2026 State of the Water Industry again identifies aging infrastructure renewal and replacement as a top challenge.
- Global non-revenue water is estimated around 126B m3/year with tens of billions of dollars of economic impact.
- PFAS, lead service lines, sewer overflow, drought/flood resilience, and energy pressure are adding regulatory and operating load.

China:

- Leakage-control pilots and MOHURD mechanisms push DMA metering, pressure control, GIS/data sharing, old-pipe renewal, secondary supply O&M, smart construction, and financing mechanisms.
- City-renewal and underground-pipe investment is now a major policy and funding track.
- Buyers include municipal housing/urban-management/water bureaus, local SOE water groups, drainage groups, city-investment platforms, industrial-park wastewater operators, EPCs, and design institutes.
- China deployment should be local/private, with "数据不出域, 结果可上报" as the posture.

## Product Workflow

1. Ingest: SCADA, AMI/AMR, GIS, CMMS, CRM, LIMS/lab, weather, field photos, CCTV, robot inspection, and edge sensors.
2. Detect: night-flow spikes, pressure drops, burst signatures, pump-energy anomalies, sewer surcharge risk, turbidity/water-quality drift, and customer-cluster anomalies.
3. Explain: combine pipe age, valve context, recent work orders, weather, pressure zone, and customer calls into one case.
4. Assign: create work orders with owner, GIS context, valve/isolation notes, SLA, and recommended playbook.
5. Verify: confirm with flow/pressure recovery, photos, sampling, CCTV, robot reinspection, or pump-energy metrics.
6. Learn: feed false positives, missed events, human labels, and verified fixes into the anomaly library and LeRobot-compatible datasets.

## Market Wedge

Start narrow:

- 1-3 district metered areas with AMI/SCADA but limited analytics staff.
- One pump-station cluster.
- One drainage catchment with overflow risk.
- One industrial water network.

Expand later:

- Pump energy optimization.
- Water-quality incident workflows.
- Sewer/stormwater monitoring.
- Compliance package generation.
- Capital planning and pipe-renewal prioritization.

## Buyer Economics

Primary value drivers:

- Real leakage savings: `MG saved x marginal production cost`.
- Apparent loss recovery: `underbilled kgal x retail rate x collection rate`.
- Avoided emergency breaks: `breaks avoided x event cost`.
- SSO/CSO risk: cleanup, bypass, lab, notification, claims, and penalties.
- Pump energy: `baseline kWh x reduction x $/kWh`.
- Truck rolls: `avoided dispatches x loaded truck-roll cost`.
- CCTV/cleaning prioritization: `feet avoided/reprioritized x cost/ft`.
- Reporting labor: hours saved on compliance and audit packages.

Pilot:

- 90-120 days.
- Overseas price: $30k-$75k.
- China price: project/package pricing by zone, pump station, drainage catchment, or city-renewal work package.
- Goal: show payback under 12 months using only hard-dollar validated actions; large incident avoidance is upside, not the base case.

## Competition

WaterLoop should integrate, not replace:

- SCADA/historians.
- Digital water platforms: Autodesk Info360, Bentley OpenFlows WaterSight, Xylem Vue, TaKaDu.
- Leak detection and analytics: FIDO AI and similar tools.
- Sewer/CCTV AI: SewerAI, VAPAR.
- Robotics/inspection: RedZone, ACWA Robotics, PIPEON-style robotics.
- Smart sewer monitoring: SmartCover/UDlive-style systems.

Differentiation:

- Closure-first workflow layer.
- Field proof loop and edge evidence.
- Chinese/local deployment option.
- LeRobot/Qualcomm edge path for repeatable robot-learning experiments.

## Qualcomm Fit

Water operations need edge AI because many sites are bandwidth-limited, cyber-sensitive, intermittent, or physically remote:

- Pump stations.
- Valve vaults.
- Pipe galleries.
- Temporary construction zones.
- Field crews.
- Tablet/robot inspection workflows.

QNN/AI Hub candidate models:

- Acoustic leak classification.
- Pump anomaly classification.
- Analog gauge OCR.
- Valve-status vision.
- Water-region/leak/drip segmentation.
- Turbidity and visual anomaly classification.

## Safe Competition Demo

Demo scope:

- Clear acrylic pipe loop and clear open channel.
- Clean water or dyed clean water only.
- 5-12V small pump, flow sensor, current sensor, leak valve, partial blockage insert, turbidity cup.
- RGB, thermal, depth/ToF, external acoustic contact mic/hydrophone, turbidity, flow, pump current, and e-stop.
- Small rover/crawler beside the rig, not inside live municipal pipes.
- ROS 2 inspection actions, evidence packet, human approval, and LeRobotDataset episode export.

Claims to avoid:

- Municipal-grade leak detection.
- Certified water-quality monitoring.
- Flood or contamination prevention.
- Real sewer/stormwater deployment.
- Autonomous utility incident closure.
- SCADA-ready or cybersecure production claims before testing.
- Exact Qualcomm NPU FPS before profiling on the target device.

Safe claim:

> Tabletop clean-water anomaly closed-loop demo using multimodal sensing, ROS 2 action workflow, human-reviewed evidence packets, LeRobot-compatible data, and a candidate Qualcomm AI Hub/QNN edge path.

## Sources

- EPA Drinking Water Infrastructure Needs Survey: https://www.epa.gov/dwsrf/epas-7th-drinking-water-infrastructure-needs-survey-and-assessment
- AWWA State of the Water Industry 2026: https://www.awwa.org/state-of-the-water-industry/
- Proparco non-revenue water article: https://www.proparco.fr/en/article/non-revenue-water-water-wasted-resource-wasted
- China leakage-control pilot notice: https://www.ndrc.gov.cn/xwdt/tzgg/202203/t20220315_1319313_ext.html
- Xinhua urban leakage target summary: https://www.news.cn/politics/2022-02/04/c_1128330675.htm
- EPA energy efficiency for water utilities: https://www.epa.gov/sustainable-water-infrastructure/energy-efficiency-water-utilities
- EPA sanitary sewer overflows: https://www.epa.gov/npdes/sanitary-sewer-overflows-ssos
- Qualcomm QCS6490: https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490
- Qualcomm RB3 Gen 2: https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub: https://aihub.qualcomm.com/
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
