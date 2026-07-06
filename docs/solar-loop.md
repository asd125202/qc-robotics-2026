# SolarLoop 光场异常闭环

SolarLoop is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames solar O&M as an exception-closure problem: hot spots, soiling, shading, offline strings, combiner faults, tracker issues, and warranty/insurance evidence should move from detection to work order, dispatch, verification, and model learning.

Public page: https://qc-robotics-2026.pages.dev/solar-loop/

## YC-Style Narrative

One-line pitch:

> 热斑不是一张图，而是一张必须关闭的工单。

Customer pain:

- Utility-scale PV owners, O&M contractors, central SOE desert-base operators, C&I rooftop owners, PV+BESS asset managers, and warranty/insurance teams see fragmented alarms and inspection reports.
- Drone thermography, SCADA, inverter alerts, cleaning robots, and CMMS records often do not form one closure loop.
- The buyer cares about recovered MWh, avoided truck rolls, avoided uneconomic cleaning, warranty evidence, and verified proof of repair.

Core insight:

- The valuable product is not solar inspection.
- The valuable product is closing the revenue leak.
- A thermal image has value only when connected to root cause, economics, dispatch, fix verification, and evidence.

## Product

Workflow:

1. Import site map, strings, inverters, combiner boxes, roads, cleaning zones, weather, and work-order fields.
2. Capture RGB, thermal, drone, fixed camera, robot, and PV telemetry streams.
3. Detect hot spots, soiling, shading, string faults, tracker issues, and cleanable versus non-cleanable anomalies at the edge.
4. Rank work by recoverable MWh, price/curtailment window, safety risk, warranty relevance, cleaning cost, and travel cost.
5. Dispatch a human crew, drone, ground robot, cleaning robot, or expert review.
6. Reinspect, verify recovery, write back to CMMS/SCADA, and export evidence packets.
7. Feed human corrections and failed missions into LeRobot-compatible HIL datasets.

## Market Wedge

Best first wedges:

- 50-500MW utility PV sites in dusty, hot, remote, or vegetation-heavy areas.
- China desert-base subareas owned by central SOE generation groups.
- O&M contractors operating multi-site portfolios.
- C&I rooftop portfolios where access and audit evidence are painful.
- PV+BESS assets where cleaning and repairs should align with high-value generation and storage windows.

China version:

- Deploy on-prem or in China cloud.
- Keep raw energy telemetry and image data in China.
- Support local audit logs and data classification.
- Pitch as an AI+Energy intelligent O&M pilot for solar desert bases and distributed PV observable/controllable operations.

Overseas version:

- Integrate with drone inspection, solar asset-management software, CMMS, and utility-scale O&M contractors.
- Sell to asset managers that already pay for annual or high-frequency inspection and need operational closure.

## Buyer Economics

Working anchor for a 100MWdc utility PV plant:

- Specific yield: 1,700MWh/MWdc-year.
- Power price: $29/MWh.
- Annual revenue: about $4.93M.
- Value of 1% recoverable production: about $49k/year.

Conservative annual value sources:

- 0.75% recovered or avoided production loss: about $37k/year.
- Avoiding or retargeting uneconomic cleaning: about $25k-$70k/year.
- Combining or avoiding 6-8 truck rolls: about $9k-$20k/year.
- Faster prioritization of persistent string/combiner faults: about $10k-$30k/year.
- Warranty/insurance evidence: event-driven upside rather than recurring base ROI.

Pilot model:

- 90-day paid pilot around $35k for a 100MWdc site or subarea.
- Target annualized verified opportunity at least 2.5x pilot fee.
- Expansion by site/MW, edge station, robot mission volume, evidence storage, and optional success fee on verified recovery.

## Competition

Existing players prove the market is real:

- Raptor Maps and similar solar asset-management tools detect and organize anomalies.
- Zeitview/Heliolytics and drone providers scale aerial inspection.
- DJI and Percepto provide drone capture and autonomous inspection workflows.
- Ecoppia, Sunpure, and other cleaning robots execute cleaning.
- SCADA, inverter, CMMS, and EAM systems monitor performance and maintenance.

SolarLoop differentiation:

- It starts from anomaly closure rather than inspection output.
- It unifies anomaly, root cause, dispatch, robot/human action, verification, recovered MWh, warranty evidence, and LeRobot HIL data.
- It positions Qualcomm edge AI as the local inference and field-robotics layer.

## Qualcomm Fit

SolarLoop needs:

- Local RGB/thermal inference in remote, weak-network field environments.
- Multiple camera and telemetry streams.
- Low-latency robot safety and mission logic.
- QNN/AI Hub compilation and profiling evidence.
- A path from QCS6490/QCS8550/RB3-style prototypes to Dragonwing industrial edge AI deployments.

Competition demo:

- Use a low-voltage 6-24V mini PV panel and a dummy/dead panel with low-voltage heater pads.
- Simulate soiling, shading, fake cracks, bird-dropping stickers, and safe thermal anomalies.
- Use a small gantry or rail-guided ground robot with dry microfiber/brush cleaning.
- Capture RGB, thermal, PV telemetry, robot state, HIL corrections, and evidence packet.
- Avoid high-voltage PV strings, water cleaning, IEC compliance claims, autonomous drone claims, and field-yield guarantees.

## Sources

- SolarPower Europe, global solar 2025 additions and 3TW fleet: https://www.solarpowereurope.org/press-releases/new-report-global-solar-market-hits-new-record-of-664-gw-installation-in-2025-as-global-solar-fleet-passes-3-tw
- IEA Global Energy Review 2026, solar PV and wind: https://www.iea.org/reports/global-energy-review-2026/technology-solar-pv-and-wind
- NEA China 2025 PV capacity: https://www.nea.gov.cn/20260212/742b8c6a078347b0b39de676c05c5d58/c.html
- PV Tech / Raptor Maps 2026 power-loss article: https://www.pv-tech.org/pv-project-power-loss-doubled-in-last-five-years-raptor-maps/
- IEA PVPS soiling fact sheet: https://iea-pvps.org/fact-sheets/fs-soiling-losses/
- IEA PVPS soiling report: https://iea-pvps.org/wp-content/uploads/2023/01/IEA-PVPS-T13-21-2022-REPORT-Soiling-Losses-PV-Plants.pdf
- MIT solar dust cleaning article: https://news.mit.edu/2022/solar-panels-dust-magnets-0311
- NREL/Sandia/SunSpec PV and energy-storage O&M best practices: https://sunspec.org/wp-content/uploads/2025/01/BestPracticesforOperationandMaintenanceofPhotovoltaicandEnergyStorageSystems3rdEdition.pdf
- Qualcomm RB3 Gen 2 hardware: https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit/hardware
- Qualcomm Dragonwing industrial edge AI: https://www.qualcomm.com/news/onq/2026/03/how-qualcomm-dragonwing-powers-industrial-edge-ai
- Hugging Face LeRobot HIL documentation: https://huggingface.co/docs/lerobot/hil_data_collection
