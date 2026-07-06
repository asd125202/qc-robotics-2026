# ComputeLoop 智算异常闭环台

ComputeLoop is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames AI data center operations as an exception-closure problem: GPU faults, inference latency, liquid-cooling anomalies, leak detection, thermal hotspots, PDU/UPS/CDU alarms, energy/PUE drift, robot inspection findings, and SLA impact should become owned, verified, auditable cases.

Public page: https://qc-robotics-2026.pages.dev/compute-loop/

## One-Line Pitch

> 值班团队不该靠群聊守住万卡集群。

ComputeLoop serves AI data center operators, enterprise/private compute platforms, neoclouds, liquid-cooled pod teams, critical-facilities teams, SRE/platform teams, and compliance/customer-success owners. The product unit is not an alarm. It is a verified recovery event.

## Problem

AI data centers already have many systems:

- DCIM, BMS, EMS, NMS, SOC, CMDB, PDU, UPS, CDU, leak sensors, GPU telemetry, K8s/Slurm, model-serving metrics, logs, traces, work orders, robot inspections, and maintenance reports.
- These systems see signals, but incidents still travel through human chat, screenshots, calls, spreadsheets, and postmortem documents.
- An inference-latency spike, GPU drop, liquid-cooling issue, thermal hotspot, leak event, PUE drift, or power alarm often lacks one impact graph, one owner, one runbook, one approval trail, and one verification packet.

## Why Now

Global:

- IEA projects global data-center electricity use to reach about 945 TWh by 2030.
- AI workloads are pushing rack density, liquid cooling, power constraints, staffing pressure, and outage economics.
- Uptime Institute reports that significant data center outages can cost hundreds of thousands to millions of dollars and are often preventable through better management, process, or configuration.
- Operators are more willing to use AI for alarm analytics and prioritization than for unrestricted autonomous M&E control. This supports an assisted-closure wedge.

China:

- National policy is pushing data centers toward hub clusters, higher utilization, lower PUE, green power, monitoring, dispatchability, and safety.
- The green/low-carbon data center action plan sets targets around average PUE, rack utilization, hub-cluster PUE, and green-power share.
- AI+Energy policy now links compute, power, efficient cooling, energy-intelligent management, demand response, and compute facilities as flexible loads.
- China deployment should emphasize local/private deployment, data residency, role permissions, audit logs, cloud-security/equal-protection context, and traceable PUE/WUE/green-power/incident evidence.

## Product Workflow

1. Ingest: metrics, logs, traces, K8s/Slurm, BMC, PDU, UPS, CDU, leak sensors, thermal cameras, robot inspection, work orders, and SLA data.
2. Merge: compress noisy alerts by rack, node, GPU, job, customer, cooling branch, power chain, and time window.
3. Explain: build an impact graph across workload, hardware, network, cooling, power, customer, and SLA.
4. Recommend: propose runbook, owner, MOP/EOP/SOP, evidence required, rollback condition, and approval path.
5. Execute: in the first version, shadow mode and human-approved actions only; no uncontrolled power/cooling/fire changes.
6. Verify: check p99 latency, utilization, job failures, thermal image, leak state, PUE, power chain, and work-order status.
7. Learn: convert final verdicts, false positives, effective actions, and robot evidence into a site-specific incident graph.

## Market Wedge

Start narrow:

- 500-5000 GPU/card AI data centers.
- 20-50 high-density or liquid-cooled racks.
- One pod or site, up to 1MW IT-load scope.
- Three to five data sources: BMS/DCIM, PDU/UPS, CDU/leak, GPU telemetry, work orders, robot evidence.
- Eight closure playbooks: power chain, UPS/battery, cooling capacity, CDU/liquid cooling, leak, thermal/PUE drift, sensor failure, overdue maintenance.

Expand later:

- Multi-site command center.
- Capacity derating and sellable-kW recovery.
- SLA and audit packages.
- Liquid cooling and leak closure.
- PUE/energy optimization.
- Robot inspection ingestion.
- 7x24 managed closure service.

## Buyer Economics

Primary value drivers:

- Avoided downtime or faster recovery.
- Faster MTTD/MTTA/MTTR for P1/P2 incidents.
- Reduced noisy alerts and duplicated work.
- Fewer thermal/leak/cooling incidents escalating into serious events.
- Reduced remote-hands and patrol labor.
- Avoided capacity derating and faster return of sellable kW/GPU hours.
- SLA credit avoidance and cleaner customer postmortems.
- PUE/energy anomaly reduction.
- Faster audit and compliance evidence assembly.

Pilot:

- 8 weeks.
- Fixed fee: RMB 180k-300k, creditable toward annual contract.
- Scope: one AI compute pod, 20-50 high-density racks, up to 1MW IT load.
- Conservative success criteria: critical anomaly MTTD under 5 minutes, P1/P2 MTTA down 30-50%, MTTR down 10-20%, noisy alerts down 20-30%, closure evidence completeness above 90%, patrol/remote-hands work down 10-20%, and PUE improvement of 0.01-0.03 or proven abnormal-energy-hour reduction.

Expansion pricing assumptions:

- Core annual fee: RMB 500-1,200 per cabinet/month, higher for high-density/liquid cooling.
- Site minimum: RMB 300k-600k/year.
- Modules: liquid-cooling/leak closure, PUE/energy optimization, capacity derating, SLA/audit evidence, 7x24 managed closure, and multi-site command center.

## Competition

ComputeLoop should integrate, not replace:

- Metrics/monitoring: Prometheus, Grafana, Zabbix, Datadog, Splunk, Elastic.
- DCIM and facility systems: Schneider EcoStruxure IT, Nlyte, Sunbird, Eaton Brightlayer, ABB Ability, FNT, Cormant.
- ITSM/incident: ServiceNow, PagerDuty, Jira Service Management.
- Hardware/liquid cooling/leak detection vendors: Vertiv, Schneider/Motivair, CoolIT/Ecolab, Submer, LiquidStack, RLE, TTK, Molex, nVent.
- Robotics/inspection: Boston Dynamics Spot, Ghost Robotics, thermal-camera vendors, security patrol robots.

Differentiation:

- AI compute-specific impact graph.
- Closure-first workflow across workload, facility, hardware, network, and customer impact.
- Evidence packet and audit export.
- Local/private deployment option.
- Human-approved runbooks instead of unrestricted autonomous control.
- LeRobot/Qualcomm edge path for repeatable robot-inspection experiments.

## Qualcomm Fit

ComputeLoop connects Qualcomm's edge AI and data-center story:

- Edge AI for thermal hotspot, leak tray, airflow, rack/object detection, and robot inspection evidence.
- AI Hub/QNN path for compiling and profiling candidate models.
- Qualcomm data-center inference positioning benefits from an operations layer that proves stable delivery, energy efficiency, and TCO.
- LeRobot feedback loop converts robot inspection failures, human verdicts, and closure results into reusable datasets.

## Safe Competition Demo

Demo scope:

- 1.2m x 0.8m low-voltage tabletop AI data center.
- Four to six rack mockups, hot/cold aisles, labels/AprilTags, LED load bank, rack status lights.
- 5V/12V/24V DC only, external certified power adapter, fuses, current limiting, physical E-stop, transparent guard.
- PTC/resistor thermal source with thermostat and thermal fuse; no flame, smoke, or burn hazard.
- Isolated leak tray with colored water/wet sponge and leak sensor, physically separated from electronics.
- 5V fan, baffle, ribbon/airflow sensor or pressure sensor as airflow/cooling surrogate.
- INA219/INA260-style low-voltage current sensing for PDU simulator.
- Slow rover with RGB, thermal, depth/ToF, odometry, bumper, safety interlock, and manual override.
- ROS 2 inspection actions, evidence packet, human approval, demo-only mitigation, reinspection, and LeRobotDataset export.

Claims to avoid:

- Automatically controls real data center distribution, cooling, or fire systems.
- Replaces DCIM/BMS/fire alarm/leak detection.
- Zero false positives.
- Certified NFPA/UL/CE/ISO compliance.
- Direct connection to real PDU, UPS, CRAC, CDU, chiller, or fire suppression.
- Autonomous fire suppression or emergency shutdown.
- Exact Qualcomm NPU FPS before profiling on target hardware.

Safe claim:

> Low-voltage tabletop AI data center exception-closure demo using multimodal sensing, ROS 2 workflow, human-reviewed evidence packets, LeRobot-compatible data, and a candidate Qualcomm AI Hub/QNN edge path.

## Sources

- IEA Energy and AI data center electricity demand: https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
- Uptime Institute 2025 Annual Data Center Survey: https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2025.Annual.Survey.Report.pdf?version=0
- Dell'Oro data center physical infrastructure forecast: https://www.delloro.com/news/data-center-physical-infrastructure-market-to-surpass-80-billion-by-2030/
- NDRC green/low-carbon data center action plan: https://www.ndrc.gov.cn/xwdt/tzgg/202407/P020240723625616053849.pdf
- NEA AI+Energy action plan: https://www.nea.gov.cn/20260508/4dae97ca01d348e4871bb8654be34b3a/c.html
- Qualcomm Data Center: https://www.qualcomm.com/data-center
- Qualcomm AI Inference Suite: https://www.qualcomm.com/developer/software/qualcomm-ai-inference-suite
- Qualcomm AI Hub: https://aihub.qualcomm.com/
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- OSHA electrical safety: https://www.osha.gov/electrical
- NFPA 75: https://www.nfpa.org/codes-and-standards/nfpa-75-standard-development/75
