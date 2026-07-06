# ComputeLoop 智算异常闭环台

Public page: https://qc-robotics-2026.pages.dev/compute-loop/

ComputeLoop is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames AI data center operations as an exception-closure problem, not a generic AIOps, DCIM, or cooling-control problem.

## One-Line Pitch

> AI 工厂不缺 GPU，缺的是把每次异常关成可验证恢复。

ComputeLoop connects GPU/NPU telemetry, RoCE/network signals, job schedulers, storage, liquid cooling, leak sensors, power chain, PUE, robot inspection, work orders, and SLA impact into one exception ID with ownership, evidence, verification, and reporting.

China tagline:

> 智算中心异常闭环台：把 GPU、网络、液冷、电力、PUE 和工单打成一条闭环。

## Problem

AI factories are tightly coupled machines:

- GPUs/NPUs, RoCE, storage, schedulers, model-serving systems, CDUs, liquid-cooling loops, PDUs, UPS systems, leak sensors, energy systems, DCIM/BMS/EPMS, observability stacks, work orders, robot inspection, and customer SLAs all produce signals.
- Existing tools see parts of the problem, but the final incident often travels through chat, screenshots, calls, spreadsheets, and postmortems.
- One latency spike, GPU drop, cooling branch anomaly, PUE drift, leak event, or power alarm often lacks one impact graph, one owner, one approved runbook, one evidence packet, and one verified recovery record.

## Why Solve It

Stable compute is now a revenue, energy, and governance problem:

- Lost training or inference time wastes scarce GPU capacity.
- Inference p99 and job failure rates affect customer SLAs.
- Liquid cooling creates new operational failure modes around flow, pressure, coolant, leak detection, and maintenance procedures.
- Power and grid constraints make capacity derating and load swings commercially painful.
- PUE, green power, utilization, and national/provincial compute monitoring are becoming operating requirements.
- Incident evidence affects customer trust, insurance, audit, government reporting, and renewal decisions.

## Why Now

Global:

- IEA reports that the largest technology companies are spending hundreds of billions of dollars on AI infrastructure, while global data center electricity demand could approach 950 TWh by 2030.
- AI racks are becoming higher density, more liquid-cooled, and more variable in power demand.
- Uptime Institute reporting continues to show serious outage cost and operator concern around power, capacity, energy performance, cost, and staffing.
- Hyperscalers have strong internal tooling, but colos, neoclouds, sovereign AI projects, and enterprise AI platforms need packaged operations layers.

China:

- Policy language has moved from building AI compute to making compute schedulable, green, reliable, and nationally observable.
- `东数西算`, `全国一体化算力网`, `算电协同`, `绿色低碳数据中心`, and `AI+能源` all point toward monitored, dispatchable, efficient compute infrastructure.
- National Data Bureau disclosures report rapid intelligent-compute expansion and connection of a large share of capacity into national monitoring platforms.
- Operators must sell usable compute, not just installed PFLOPS.

## Insight

Monitoring sells visibility. Closure sells recovery.

The minimum commercial unit for AI data center operations is not an alarm. It is a verified recovery event:

1. What happened?
2. Which racks, GPUs, jobs, customers, cooling loops, and power chains were affected?
3. Who owned the response?
4. Which runbook was approved?
5. What evidence proved recovery?
6. What label should the system learn for next time?

## Solution

ComputeLoop does not replace DCIM, BMS, EPMS, ITSM, AIOps, GPU schedulers, liquid-cooling controls, leak detection, fire systems, or qualified facility operators.

ComputeLoop sits above and between them:

1. Ingest read-only signals from IT, facility, cooling, power, work-order, and robot systems.
2. Correlate duplicate signals by site, room, rack, server, GPU, job, customer, cooling loop, power chain, and time window.
3. Build an impact graph that connects facility physics to workload and SLA impact.
4. Recommend human-approved SOP/MOP/EOP actions with rollback and evidence requirements.
5. Dispatch work orders, robot inspection, and customer/operations notifications.
6. Verify recovery through p99, utilization, job failures, thermal imagery, leak status, flow, PUE, power state, and work-order closure.
7. Write final verdicts into an operator-specific incident graph and training loop.

## First Product

Beachhead:

- 500-5000 GPU/card AI data centers.
- High-density or liquid-cooled pods.
- Colocation, neocloud, enterprise/private AI, sovereign AI, local government data groups, telecom/cloud arms, and industry inference platforms.
- Mixed vendors and painful handoffs between facility teams and platform/SRE teams.

First module:

- GPU/job anomaly closure.
- Liquid cooling and leak assurance.
- Power-chain and capacity-derating events.
- PUE/energy anomaly response.
- Robot inspection evidence.
- Work-order and SLA incident package.

## Market

China version:

- Buyers: telecom operators and cloud arms, provincial/city data groups, local SOE investment platforms, AIDC operators, compute-scheduling platform operators, EPC/SI firms, DCIM/动环 vendors, liquid-cooling vendors, and energy groups.
- Procurement language: `算力互联`, `纳管`, `监测`, `调度`, `运营`, `算电协同`, `告警收敛`, `自动诊断`, `综合运维健康度`, `跨平台稳定性风险识别`, `液冷漏液检测`, `PUE 可视可管可控`, `上联省级/国家级算力监测调度平台`.
- Deployment: private/on-prem, local data residency, 国产适配, role permissions, evidence logs, cybersecurity review, audit exports.

Overseas version:

- Buyers: colocation operators, neoclouds, AI infrastructure operators, enterprise AI platform teams, sovereign AI operators, data center O&M providers, and high-density retrofit programs.
- Procurement language: AI factory uptime, liquid cooling assurance, capacity forecasting, energy performance, power availability, incident evidence, compliance/insurance reports, and SLA risk.
- Deployment: on-prem/BYOC/SaaS depending on tenant and data sensitivity.

## Business Model

China:

- 90-day pilot: RMB 300k-800k.
- Scope: one pod or hall, 20-60 high-density racks, three to five anomaly classes.
- Production: RMB 800k-3M per site per year.
- Multi-site/network edition: RMB 5M-20M per year.
- One-time integration and optional驻场 service priced separately.

Overseas:

- Pilot: USD 75k-200k.
- Production: USD 250k-1M per site or AI hall per year.
- Enterprise/multi-site: USD 1M-3M+ per year.
- Optional pricing by MW, rack, edge node, or managed closure service.

Pricing rule: keep first-year cost below 15%-25% of validated annual benefit, with a target payback period under 12 months.

## ROI And Pilot KPIs

Annual benefit:

avoidable downtime + faster MTTR + recovered sellable GPU hours + reduced capacity derating + avoided SLA credits + abnormal energy-hour reduction + patrol/remote-hands labor savings + faster audit/postmortem preparation.

90-day acceptance targets:

- 95%+ pilot racks/GPU nodes mapped to operational graph.
- 30% reduction in duplicate alerts for P1/P2 incidents.
- 30%-50% MTTA reduction.
- 10%-20% MTTR reduction for selected incident classes.
- 90%+ closed events with complete evidence packets.
- Weekly incident export accepted by facility, platform/SRE, and customer-success teams.
- A conservative payback model based on verified GPU hours, capacity derating, energy anomaly, and labor savings.

## Go-To-Market

Do not sell broad AIOps. Sell liquid-cooling safety, SLA assurance, and compute-energy coordination.

China:

- Enter through telecom/cloud operators, local data groups, EPC/O&M integrators, DCIM/动环 vendors, liquid-cooling OEMs, and energy-service companies.
- Lead with read-only integration, alarm convergence, fault diagnosis, PUE visibility, liquid-cooling risk, and evidence exports.

Overseas:

- Enter through colos, neoclouds, liquid-cooling retrofit programs, EAM/ITSM partners, data center O&M firms, and robot inspection vendors.
- Lead with capacity recovery, high-density operations, incident evidence, and AI factory uptime.

## Competition

ComputeLoop integrates with, rather than replaces:

- OEM/DCIM suites: Schneider EcoStruxure IT, Vertiv Environet/Alert, Eaton Brightlayer, Johnson Controls OpenBlue.
- Independent DCIM/ITAM/CMDB: Sunbird, Nlyte, Device42.
- AIOps/observability/ITSM: ServiceNow, Datadog, Prometheus Alertmanager, Grafana IRM, Splunk, Elastic.
- Thermal/liquid/leak vendors: Schneider/Motivair, Eaton/Boyd Thermal, CoolIT, Submer, LiquidStack, EkkoSense, Vigilent, RLE, TraceTek, TTK.
- Robotics inspection: ANYbotics, Boston Dynamics Spot, Ghost Robotics, Korial/Energy Robotics, Boost Robotics.
- Hyperscaler internal tooling from Google/DeepMind, Microsoft, AWS, and Meta.

Position:

> ComputeLoop does not replace DCIM, ITSM, or cooling controls. It closes the operational gap between them.

Avoid claims:

- first AI data center operations platform;
- DCIM replacement;
- unrestricted closed-loop control of chillers, CDUs, PDUs, UPS systems, or safety systems;
- zero downtime, zero leaks, or guaranteed PUE savings;
- root cause certainty without technician validation;
- certified safety/compliance status before certification.

## Moat

The moat is an operator-specific AI factory incident graph:

- site, room, rack, server, GPU, job, customer, cooling loop, power chain, owner, and SLA relationships;
- SOP/MOP/EOP mappings and approval rules;
- evidence standards for each exception type;
- false positives, repeat faults, and effective actions;
- robot inspection episodes, human interventions, and final verdicts;
- local deployment, integration depth, and audit history.

## Architecture

Engineering principles:

- read-only integration first;
- no direct control of production power, cooling, fire, or safety systems in the first product;
- human approval for key actions;
- deterministic safety supervisor in the demo;
- local/private deployment preference;
- evidence logs, model versions, role permissions, and audit exports.

Reference architecture:

- Signal Layer: metrics/logs/events/traces, K8s/Slurm, GPU telemetry, BMC, PDU, UPS, CDU, leak sensors, thermal cameras, and robot observations.
- Impact Graph: maps workload, hardware, rack, cooling, power, tenant/customer, and SLA.
- Closure Engine: alert compression, probable-cause candidates, runbooks, approvals, work orders, robot inspection, verification, and postmortems.
- Edge Evidence: Qualcomm-oriented edge inference for thermal, leak, airflow, rack ID, indicator lights, and robot evidence.
- Training Loop: LeRobotDataset episodes, time-series anomaly labels, vision labels, and human final verdicts.

## Qualcomm Fit

Qualcomm's AI data center story now includes rack-scale inference, liquid cooling, energy efficiency, tokens/watt, and TCO. ComputeLoop adds the operations layer:

- local edge vision and sensor inference for data center evidence;
- Qualcomm AI Hub/QNN compile and profile path for small telemetry and vision models;
- low-voltage AI rack twin demonstration that safely references rack-scale operations;
- robot inspection and LeRobot data flywheel;
- a business story around stable inference delivery, not only raw accelerator performance.

## Safe Competition Demo

Demo scope:

- Low-voltage tabletop AI rack twin, not a real server rack.
- 3-5 fake accelerator sleds, LED dummy loads, fans, a sealed low-voltage cooling loop, flow sensor, leak tray, thermal sensors, current monitor, status lights, and a small rover.
- 5V/12V current-limited supplies, inline fuses, physical E-stop, transparent guard, watchdog, and firmware limits.
- ROS 2 telemetry, action servers, dashboard, evidence packets, and LeRobot-compatible data export.

Scenarios:

- thermal or flow anomaly;
- leak trip;
- power spike on a low-voltage dummy load;
- sensor dropout;
- robot inspection and human-reviewed closure.

Safety rule:

> AI recommends. A deterministic supervisor enforces safety. Human approval closes the incident.

Claims to avoid:

- production data center control;
- real PDU, UPS, CDU, chiller, fire suppression, or high-voltage operation;
- validated Qualcomm AI200/AI250 deployment unless actually tested;
- certified safety system;
- measured QNN/NPU performance before profiling on target hardware.

## Ask

Support requested:

- Qualcomm edge development board and model path guidance.
- AI Hub/QNN compile and profiling support.
- Data center and liquid-cooling mentor review.
- Feedback on safe low-voltage rack twin design.
- Partner introductions for DCIM/液冷/机房 O&M/robot inspection integration.
- Two to three design-customer interviews or pilot conversations.

## Sources

- IEA Key Questions on Energy and AI: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- IEA Energy and AI electricity demand: https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
- LBNL U.S. Data Center Energy Usage Report: https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report
- EPRI Powering Intelligence: https://powering-intelligence.epri.com/executive-summary.html
- Uptime Institute 2025 Annual Data Center Survey: https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2025.Annual.Survey.Report.pdf?version=0
- Uptime Institute Annual Outage Analysis 2026: https://intelligence.uptimeinstitute.com/resource/annual-outage-analysis-2026
- NDRC national integrated compute network guidance: https://www.ndrc.gov.cn/xxgk/zcfb/tz/202312/t20231229_1363000.html
- NDRC green and low-carbon data center action plan: https://www.ndrc.gov.cn/xwdt/tzgg/202407/P020240723625616053849.pdf
- AI+Energy action plan: https://www.nea.gov.cn/20260508/4dae97ca01d348e4871bb8654be34b3a/c.html
- National Data Bureau compute monitoring disclosure: https://www.nda.gov.cn/sjj/swdt/mtsy/0430/20260430114558848516126_pc.html
- CAICT intelligent computing infrastructure report: https://www.caict.ac.cn/kxyj/qwfb/ztbg/202409/P020241105565523891417.pdf
- Qualcomm AI200 product page: https://www.qualcomm.com/data-center/products/qualcomm-dragonfly-ai200
- Qualcomm AI200 and AI250 announcement: https://www.qualcomm.com/news/releases/2025/10/qualcomm-unveils-ai200-and-ai250-redefining-rack-scale-data-cent
- Qualcomm AI Hub compile documentation: https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- Hugging Face LeRobot: https://github.com/huggingface/lerobot
- ROS 2 Actions design: https://design.ros2.org/articles/actions.html
