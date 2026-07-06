# GridLoop 配网异常闭环

GridLoop is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames distribution-grid operations as an exception-closure problem: voltage anomalies, transformer overload, hot connectors, vegetation risk, feeder trips, storm damage, reverse power flow, EV charging peaks, and field inspection evidence should become owned, verified, learnable cases.

Public page: https://qc-robotics-2026.pages.dev/grid-loop/

## One-Line Pitch

> 让每一次配网异常都有结论、有动作、有复盘。

GridLoop serves distribution-grid dispatchers, inspection and maintenance teams, utility digital departments, industrial parks, charging-heavy cities, and DER-rich feeders. The product unit is not an alert. It is a resolved exception with evidence.

## Problem

Distribution utilities already have many systems:

- SCADA, AMI, OMS, GIS, CMMS/EAM, weather, charger telemetry, distributed PV telemetry, drone inspection, robot inspection, and field photos.
- These systems see signals, but people still chase context across tools, calls, spreadsheets, and post-event reports.
- A voltage complaint, transformer overload, thermal hotspot, vegetation issue, storm damage report, reverse-power event, or feeder trip often lacks one owner, one timeline, one action path, and one verification packet.

## Why Now

Global:

- IEA says grid investment needs to nearly double by 2030 to more than $600B per year.
- EIA reported that U.S. customers averaged almost 11 hours of power interruptions in 2024, with major storms driving most outage hours.
- ASCE reports that distribution-system failures cause the overwhelming majority of customer interruptions in the United States.
- DER, EV charging, extreme weather, wildfire, transformer shortages, and aging assets are pushing utilities toward faster, evidence-rich field operations.

China:

- Distribution grids are a core bottleneck for distributed renewables, charging infrastructure, local flexibility, disaster resilience, and digital-grid operations.
- Policy language around 2024-2027 distribution-grid action emphasizes carrying capacity, resilience, intelligent monitoring, and high-quality distribution development.
- 2030 policy targets for distributed new energy and charging infrastructure make feeder-level visibility and closure more important.
- China deployment should emphasize local/private deployment, edge AI, only-read OT integration, human approval, and "数据不出域, 证据可上报".

## Product Workflow

1. Ingest: SCADA, AMI, OMS, GIS, CMMS, weather, EV chargers, distributed PV, drone footage, robot sensing, and field photos.
2. Detect: voltage drift, transformer overload, feeder trip, line-loss spike, reverse power, hot connector, vegetation risk, acoustic anomaly, and customer-cluster complaint.
3. Explain: combine topology, time sequence, asset history, nearby work orders, weather, and field evidence into one case.
4. Assign: create human-approved tasks with owner, risk, impacted users, recommended evidence, and SLA.
5. Verify: confirm telemetry recovery, AMI voltage recovery, thermal rescan, photos, crew verdict, or customer-complaint decline.
6. Learn: feed false positives, missed events, human labels, and verified fixes into the anomaly graph and LeRobot-compatible datasets.

## Market Wedge

Start narrow:

- DER/EV-heavy feeders.
- Transformer overload and low-voltage complaint closure.
- Thermal defects and connector inspection.
- Vegetation or wildfire-risk evidence closure.
- Storm-damage triage after major weather.
- Industrial parks with private distribution networks and energy teams.

Expand later:

- DER hosting-capacity workflow.
- Vegetation and wildfire module.
- Storm restoration and estimated-time-to-restore module.
- Equipment-health module.
- Reliability reporting and compliance package generation.

## Buyer Economics

Primary value drivers:

- Reliability: avoided customer-minutes interrupted, improved SAIDI/SAIFI, repeat-incident reduction, and faster restoration.
- Field operations: fewer low-value patrols, better truck-roll targeting, less cross-system investigation time, fewer repeat visits.
- Vegetation and wildfire: prioritized high-risk spans, better evidence before/after work, and faster closure of risk work orders.
- Equipment health: earlier hot connector or transformer overload discovery, less emergency work, better replacement timing.
- DER/EV: delayed or better-targeted upgrades through feeder-level visibility and action tracking.
- Compliance and reporting: less manual reconstruction of incident timelines and evidence.

Pilot:

- 4-6 months.
- Scope: 10-30 feeders or 50k-150k meters.
- Overseas price: $150k-$250k.
- China price: project/package pricing through utility digital-grid, inspection, or local integrator budget.
- Goal: show payback using hard-dollar actions such as avoided truck rolls, investigation time saved, repeated incident reduction, and deferred low-priority work. Reliability and public-safety value is upside.

## Competition

GridLoop should integrate, not replace:

- ADMS/OMS/SCADA: GE Vernova, Schneider Electric, Siemens, Oracle Utilities, Hitachi Energy, and others.
- DERMS/VPP: AutoGrid, EnergyHub, Schneider DERMS, Enbala/Generac-style platforms.
- Inspection and imagery: AiDash, Overstory, Buzz Solutions, Noteworthy AI, DroneDeploy, Cyberhawk, Pix4D, and drone OEMs.
- EAM/GIS/workforce: Esri, SAP, IBM Maximo, Oracle WAM, ServiceNow, and utility work-management tools.

Differentiation:

- Closure-first workflow layer.
- Topology-aware exception graph.
- Field proof loop and edge evidence packets.
- China/local deployment option.
- LeRobot/Qualcomm edge path for repeatable robot-learning experiments.

## Qualcomm Fit

Distribution-grid operations need edge AI because many sites are bandwidth-limited, cyber-sensitive, intermittent, or physically remote:

- Substations and distribution rooms.
- Feeder corridors.
- Utility trucks.
- Drone/robot inspection workflows.
- Industrial parks and charging-heavy sites.
- Storm response and weak-network environments.

QNN/AI Hub candidate models:

- Thermal hotspot classification.
- Vegetation/contact segmentation.
- Asset detector for transformer, pole, insulator, switch, and connector.
- Acoustic anomaly classification from spectrograms.
- Electrical telemetry anomaly model.
- Multimodal fusion model for case priority and likely cause.

## Safe Competition Demo

Demo scope:

- 12-24V tabletop feeder, current-limited supply, fuses, e-stop, and clear cover.
- 3D-printed pole/transformer/connector props and LED/resistor load bank.
- Low-voltage PTC/heater pad under a connector prop with thermostat and thermal fuse.
- Foam or plastic branch with marker/contact switch as vegetation surrogate.
- Speaker-played buzz/hum samples for acoustic anomaly, not corona/arcing.
- Small rover, pan-tilt camera mast, or drone shell with propellers removed/guarded.
- RGB, thermal, depth/ToF, acoustic, voltage/current, IMU/odom, and safety interlock.
- ROS 2 topics, evidence packet, human approval, and LeRobotDataset episode export.

Claims to avoid:

- Detects real distribution-grid faults.
- Prevents outages, fires, or electrocution.
- Safe around live utility equipment.
- Autonomously isolates, recloses, or reconfigures feeders.
- Equivalent to protection, SCADA, FLISR, relay logic, or certified electrical-safety procedure.
- Real-time Qualcomm NPU performance before profiling on target hardware.

Safe claim:

> Tabletop low-voltage distribution-grid exception-closure demo using multimodal sensing, ROS 2 action workflow, human-reviewed evidence packets, LeRobot-compatible data, and a candidate Qualcomm AI Hub/QNN edge path.

## Sources

- IEA Electricity Grids and Secure Energy Transitions: https://www.iea.org/reports/electricity-grids-and-secure-energy-transitions/executive-summary
- EIA U.S. outage duration summary: https://www.eia.gov/todayinenergy/detail.php?id=66744
- ASCE Energy Infrastructure Report Card: https://infrastructurereportcard.org/cat-item/energy-infrastructure/
- DOE GRIP program projects: https://www.energy.gov/oe/grid-resilience-and-innovation-partnerships-grip-program-projects
- National Energy Administration distribution-grid action plan: https://zfxxgk.nea.gov.cn/2024-08/02/c_1310784260.htm
- NDRC/NEA high-quality grid development opinion: https://www.ndrc.gov.cn/xxgk/zcfb/tz/202512/t20251231_1402949.html
- Qualcomm AI Hub: https://aihub.qualcomm.com/
- Qualcomm RB3 Gen 2 Development Kit: https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Hugging Face LeRobot docs: https://huggingface.co/docs/lerobot/en/index
- OSHA 1910.333: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333
