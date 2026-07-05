# ScaleFoundry Pitch

更新时间：2026-07-05。硬件产品化、认证、供应链和法规随地区与产品类别变化很大，真实交付前必须按具体 SKU、目标市场、实验室和制造伙伴重新验证。

## Core Thesis

RobotMac / Qualcomm robotics 的商业化不能停在开发板和 demo。客户最终需要的是可复购、可维修、可认证、可制造、可长期供应的 robot compute SKU。

> ScaleFoundry = devkit / prototype -> field pilot appliance -> certification evidence -> manufacturing launch pack -> lifecycle assurance。

它不是“我们自己开工厂”，而是 Qualcomm-first 的 prototype-to-SKU infrastructure：

- SKU definition。
- enclosure / thermal / power / I/O。
- DFM / DFT。
- EVT / DVT / PVT gates。
- factory test fixtures。
- certification technical file。
- CM / JDM / ODM handoff。
- BOM / PCN / PDN lifecycle watch。
- FRU / spare parts / repairability model。

## Five-Thread Research Synthesis

### 1. Hardware Productization

ScaleFoundry 应该卖 stage gate，而不是卖“规模化口号”：

- EVT：工程样机、基本功能、接口、电源、热、bring-up 和 early DFM。
- DVT：可靠性、EMC pre-scan、环境测试、固件稳定性、safety evidence、test fixture。
- PVT：小批试产、yield、工艺、MES traceability、golden sample、CM handoff。
- MP：量产发布、ECO、供应链、质量、field failure feedback。

核心 artifact：

- EVT exit report。
- DVT compliance / reliability report。
- PVT pilot-yield report。
- locked BOM / AVL。
- DFM / DFT review。
- fixture roadmap。
- ECO process。
- CM handoff pack。

### 2. Certification Evidence

ScaleFoundry 不应该承诺“帮你认证通过”，而应该生成 market-ready technical file 和 evidence workflow：

- US：FCC SDoC / Certification、Part 15、NRTL planning、UL 1740 / UL 3100 path where applicable。
- EU：Machinery Directive / Machinery Regulation 2023/1230、EMC、RED、RoHS、Battery Regulation。
- UK：UKCA / CE reuse where allowed，GB / NI declaration management。
- Safety：ISO 12100 hazard analysis、ISO 13849-1 / IEC 62061、ISO 10218-1/2:2025、ISO/TS 15066 where applicable。
- Battery：UN 38.3、BMS、charger compatibility、transport labeling。
- Reliability：temperature、humidity、vibration、shock、IP、packaging and operating lifetime profile。
- Change control：every ECO triggers compliance impact review。

### 3. Lifecycle Assurance

机器人硬件必须能支持 7-15 年以上的部署周期：

- Semiconductor longevity is conditional: selected SoCs may have 7 / 10 / 15 year programs, but MOQ、security maintenance、migration 和 PCN / PDN 风险仍要管理。
- Robot OEM support benchmarks include long spare-parts availability, exchange units, repaired parts, warranty and service plans。
- Regulation is pushing repairability: battery replaceability, spare availability, RoHS / WEEE / REACH / SCIP and product passport direction。

ScaleFoundry modules:

- Long-Life Design-In Scorecard。
- BOM Risk & PCN / PDN Watchtower。
- FRU & Repairability Modeler。
- Spare Parts & Kit Planner。
- Repair, RMA & Warranty Ledger。
- Battery Lifecycle & Replaceability Compliance。
- Materials & Regulatory Passport。
- Lifecycle Extension Marketplace。

### 4. Qualcomm Production Ecosystem

Qualcomm already has the pieces:

- IQ10 Robotics Reference Design for high-end AMR / humanoid / industrial robotics。
- QCS6490 / RB3 Gen 2 for accessible mid-tier edge robotics。
- QCS8550 for premium edge AI boxes, AMRs, drones and vision systems。
- AI Hub for model optimization / validation / profiling。
- FoundriesFactory for Yocto, CI/CD, OTA and fleet deployment workflows。

Recommended manufacturing lanes:

- China lane：Thundercomm, Quectel, Fibocom, APLUX / AidLux, fast customization, local robot OEMs。
- Overseas / regulated lane：Advantech, VVDN, Lantronix, Taiwan / India / TAA / NDAA / long-lifecycle channels。

### 5. Business Positioning

ScaleFoundry should sell robot platform productization, not generic consulting:

- Robot Productization Audit。
- Devkit-to-Product Sprint。
- Field Pilot Appliance。
- Certification Readiness Pack。
- Manufacturing Launch Pack。
- Partner Platform License。
- Managed Robot Edge Ops。

Sharp claim:

> Qualcomm provides the reference design. ScaleFoundry turns it into your robot product.

## Product Modules

### 1. Devkit-To-SKU Sprint

- Choose QCS6490 / QCS8550 / IQ9 / IQ10 lane。
- Sensor and I/O map。
- ROS 2 / RobotCoreOS baseline。
- AI Hub / QNN deployment target。
- Thermal / enclosure / power plan。
- Service/debug port plan。
- 90-day field pilot plan。

### 2. Manufacturing Readiness Gates

- EVT checklist。
- DVT checklist。
- PVT checklist。
- CM qualification。
- ISO 9001 / IPC-A-610 workmanship evidence target。
- Factory traveler。
- Golden sample。
- Serial number / firmware / BOM lot traceability。
- Pilot build yield dashboard。

### 3. Certification Evidence Room

- Product classification。
- Requirements matrix。
- Safety case。
- Functional safety file。
- EMC / wireless package。
- NRTL / electrical package。
- Battery package。
- Reliability evidence。
- Technical construction file index。
- Labels / manuals / declarations。
- Post-market evidence。

### 4. Lifecycle Assurance

- Long-life SoC and module scorecard。
- BOM / AVL risk。
- PCN / PDN alerts。
- FRU graph。
- Spare parts kit。
- repair procedure。
- battery lifecycle。
- RoHS / REACH / WEEE / SCIP passport。
- end-of-life migration plan。

### 5. Partner Lane Manager

- China lane：speed, local supply chain, local docs, cost-sensitive robots。
- Overseas lane：regulated customers, strict BOM control, TAA / NDAA / India / Taiwan manufacturing。
- JDM / ODM decision records。
- IP ownership and responsibility split。
- co-sell evidence with Qualcomm ecosystem partners。

## Competition Demo

ScaleFoundry can be shown as a “prototype-to-SKU room”:

1. Start from LabForgePilot / RobotMac prototype。
2. Select QCS target and hardware form factor。
3. Generate DFM / DFT checklist and fixture roadmap。
4. Show EVT / DVT / PVT gates and evidence placeholders。
5. Show compliance matrix for US / EU / China。
6. Show BOM lifecycle and FRU / spare-parts model。
7. Export a manufacturing launch pack and field pilot appliance page。

This answers a key judge question: how does the project become a real product instead of a one-off competition build?

## Why Qualcomm Should Care

Qualcomm should treat robotics hardware as a production ecosystem, not only a chipset sale:

- Robotics customers buy sensor integration, thermal design, motion I/O, safety, OS, OTA, certification path and lifecycle support。
- ScaleFoundry turns Dragonwing reference designs into repeatable robot edge appliances。
- Partner lanes let Qualcomm serve both China speed/cost markets and regulated overseas industrial markets。
- Manufacturing evidence, lifecycle scorecards and field data make Qualcomm harder to replace after design-in。

一句话：

> ScaleFoundry turns Qualcomm reference designs into manufacturable robot SKUs.

## Sources

- Dragonwing IQ10 robotics reference design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- IQ10 product brief：https://docs.qualcomm.com/doc/87-A0789-1/87-A0789-1_REV_A_Qualcomm_Dragonwing_IQ10_Robotics_Reference_Design_Product_Brief.pdf
- Qualcomm QCS6490：https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490
- Qualcomm product longevity：https://www.qualcomm.com/internet-of-things/products/product-longevity-program
- FoundriesFactory：https://www.qualcomm.com/developer/software/foundriesfactory
- Altium DFT guide：https://resources.altium.com/p/designing-for-testability-dft
- Keysight in-circuit test：https://www.keysight.com/us/en/products/in-circuit-test-for-manufacturing.html
- ISO 9001：https://www.iso.org/standard/62085.html
- UL robotics safety：https://www.ul.com/services/robotic-safety-security-and-performance
- UL EMC testing：https://www.ul.com/services/testing/emc-testing
- FCC equipment authorization：https://www.fcc.gov/general/equipment-authorization
- OSHA NRTL：https://www.osha.gov/nationally-recognized-testing-laboratory-program
- EU Machinery Regulation：https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/machinery_en
- KUKA spare parts：https://www.kuka.com/en-us/services/spare-parts
- FANUC robot support：https://www.fanucamerica.com/support/robot
- EU Battery Regulation：https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L:2023:191:FULL
- HAX program：https://hax.co/program/
- MassRobotics accelerator：https://www.massrobotics.org/massrobotics-accelerator/
- Thundercomm RB5 development kit：https://www.thundercomm.com/product/qualcomm-rb5-gen-2-development-kit/
- Advantech edge AI systems：https://www.advantech.com/en-us/solutions/edge-computing-and-wise-edge/edge-ai-systems
- VVDN Qualcomm partner：https://www.vvdntech.com/en-us/partners/qualcomm
- Lantronix Open-Q 8550CS：https://www.lantronix.com/newsroom/press-releases/lantronix-launches-new-open-q-8550cs/
