# RoboPort 机器人模组港

Public page: https://qc-robotics-2026.pages.dev/roboport/

RoboPort is a Chinese pitch-deck concept for the Qualcomm robotics competition. It frames robot modularity as a compatibility-evidence problem, not a generic hardware marketplace or universal plug-and-play claim.

## One-Line Pitch

> 机器人不缺零部件，缺的是可信兼容证据。

English positioning:

> RoboPort is the evidence graph for robot-cell compatibility, change impact, and certification readiness.

RoboPort provides CR-ready module passports, ROS 2 driver capsules, LeRobot metadata, compatibility tests, versioned evidence packs, and a curated module/skill marketplace.

## Problem

Robot projects often fail in the final integration layer:

- mechanical flange, tool changer, gripper, camera, sensor, PLC, safety scanner, controller, fieldbus, wiring, firmware, ROS driver, URDF/USD model, calibration, timestamping, LeRobot schema, and risk assessment all come from different vendors;
- each part can be good, but the final combination may be unknown;
- upgrades, firmware changes, driver drift, calibration changes, or tooling swaps can invalidate a previously working robot cell;
- system integrators preserve much of this knowledge in tribal notes rather than queryable evidence.

The missing product object is a validated configuration, not a product listing.

## Why Solve It

Robot adoption needs a platform layer:

- OEMs need more modules and skills per robot body.
- Tool and sensor vendors need a route to many robot models without custom integration every time.
- System integrators need reusable evidence and fewer repeated mistakes.
- Manufacturing engineers need faster commissioning and less version uncertainty.
- Quality/EHS/legal teams need audit trails, risk boundaries, and rollback records.
- Developers need one SDK and marketplace path to sell robot skills.

## Why Now

Global:

- IFR reports robotics has reached platform-scale volume, with hundreds of thousands of new industrial robot installs annually and millions of robots operating globally.
- Peripherals, vision, process design, and integrator capability remain adoption bottlenecks, especially for SMEs.
- UR+, Isaac, ROS 2, Viam, Foxglove, Open-RMF, VDA 5050, OPC UA Robotics, and SRCI all validate the pull toward robot ecosystems, but they solve different layers.

China:

- China is the robotics volume market, with millions of industrial robots operating and the largest share of new installations.
- China policy around humanoids, embodied intelligence, AI+manufacturing, industrial agents, benchmark lines, training fields, and standardization points directly at modular robot infrastructure.
- 2025-2026 standards plans include perception, motion control, operation, simulation testing, safety, body communication interfaces, cloud-edge-end systems, controllers, model training platforms, and data training fields.

## Insight

The next robotics platform is not only an app store. It is a trust stack:

1. Can this module physically and electrically connect?
2. Which driver and firmware version work?
3. Which ROS 2 interfaces, frames, calibration files, and LeRobot schemas are valid?
4. Which safety evidence and risk boundaries changed?
5. Who tested the combination, under what scope, with what limitations?
6. Can the configuration be installed, sold, monitored, and rolled back?

## Solution

RoboPort does not replace EtherCAT, CANopen, IO-Link, OPC UA, SRCI, ROS 2, UR+, Isaac, Viam, Foxglove, TÜV, UL, CE, ISO, or accredited safety certification.

RoboPort sits between them:

1. Module Passport: hardware identity, power, interfaces, mass, frames, calibration, firmware, driver, LeRobot features, limitations, and signature.
2. Driver Capsule: ROS 2 lifecycle node, ros2_control interfaces, QoS, diagnostics, SBOM, license, dependencies, version matrix, and rollback.
3. Compatibility Test: electrical, thermal, latency, timestamp drift, fault recovery, firmware update, soak, and negative evidence.
4. Evidence Graph: robot, controller, EOAT, sensor, PLC, fieldbus, safety component, firmware, driver, CAD/URDF/USD, certificate, and reviewer relationships.
5. Marketplace: certified configurations, skill packs, module bundles, integrator support, and enterprise deployment records.

## First Product

Start with cobot end effectors and sensors:

- ISO 9409-1 gives a mechanical flange baseline, but not power, data, safety, calibration, drivers, LeRobot metadata, or app distribution.
- Cobot cells already use repeatable combinations of robot arms, grippers, tool changers, force sensors, cameras, safety scanners, PLCs, and application skills.
- Evidence is fragmented across manuals, URCaps, distributor notes, PLC projects, ROS packages, CAD files, and integrator experience.

First verified combinations:

- robot model/controller/software version;
- EOAT/tool changer/force sensor;
- vision/sensor device;
- PLC/fieldbus/safety component;
- driver capsule;
- CAD/URDF/USD assets;
- test method and limitations;
- LeRobot metadata and optional skill pack.

## Market

China version:

- Buyers: robot OEMs, system integrators, module vendors, smart-factory buyers, vocational schools, industrial parks, test/certification platforms, mid-test bases, and training fields.
- Procurement language: `机器人模块可信互联平台`, `CR-ready 模块护照`, `软硬件接口标准化`, `本体通信接口`, `云边端协同接口`, `中试验证与场景适配`, `供应链协同与质量追溯`, `安全/EMC/可靠性/功能安全/信息安全/智能化等级评价`.
- Positioning: let OEMs select joints, hands, sensors, controllers, and skill modules with test reports, interface protocols, and compliance files before pilot, procurement, and mass production.

Overseas version:

- Buyers: system integrators, robot OEM ecosystem teams, manufacturing engineering, quality/compliance, EHS/legal, ISVs, education, insurers/safety reviewers.
- Positioning: certified compatibility and evidence layer above UR+, ROS 2, Isaac, Viam, Foxglove, Open-RMF, VDA 5050, OPC UA Robotics, and formal certification bodies.
- Target sectors: warehouses/3PL, electronics manufacturing, food/logistics, healthcare logistics, cleaning, inspection, machine tending, education.

## Business Model

Pilot:

- China: RMB 50k-300k.
- Overseas: USD 15k-75k.
- Scope: one workflow, one or two robot models, two or three modules/skills, simulator + safety manifest + evidence pack.

Runtime:

- China: RMB 99-499 per robot/month.
- Overseas: USD 99-499 per robot/month.
- Enterprise fleet discounts.

Certification:

- Software validation: USD 500-1.5k.
- Physical robot/app validation: USD 5k-25k.
- Robot-family adapter certification: USD 10k-50k.

Marketplace:

- Default take rate: 15%.
- Managed enterprise sales/support/insurance bundles: 25%-30%.
- Developer account: free community, paid pro around USD 99/year or RMB 699/year, free for schools.

## Pilot KPI

90-day pilot:

- app/module install and config under 30 minutes;
- >95% runtime uptime during supervised shifts;
- no unresolved safety events in pilot scope;
- driver capsule rollback proven;
- LeRobot episode metadata exported;
- evidence pack accepted by OEM/SI/quality reviewer;
- one workflow payback model under 12-18 months;
- one RoboPort Verified configuration ready for marketplace listing.

## Competition

RoboPort integrates with, rather than replaces:

- EOAT/tool ecosystems: OnRobot, Robotiq, Schunk, Zimmer, Piab, ATI.
- Robot marketplaces: Universal Robots UR+.
- Sensors/vision/IO: SICK, Keyence, Cognex, Balluff, Turck, Festo.
- Controls and PLC: Siemens, Beckhoff, PLCopen/SRCI.
- Open robotics software: ROS-Industrial, ROS 2 ecosystem.
- Simulation/digital twin: NVIDIA Isaac Sim, OpenUSD/AOUSD, Gazebo, Vention.
- Robotics ops/data: Formant, Viam, Tangram Vision, Foxglove/MCAP.
- Safety/certification: TÜV, UL, ISO 10218, ANSI/A3 R15.06, ISO 13849, ISO/TS 15066 lineage.

Avoid claims:

- universal plug-and-play;
- replacement for integrators;
- certified robot-cell safety;
- simulation-proven production readiness;
- neutral marketplace without transparent limitations;
- a brand-new standard that ignores existing buses, drivers, and certification systems.

## Moat

The moat is a cross-OEM compatibility evidence network:

- validated robot-module-skill combinations;
- negative evidence and known limitations;
- runtime telemetry and integration failures;
- driver capsule versions and rollback history;
- skill-marketplace distribution;
- module vendor/OEM/SI relationships;
- evidence accepted by quality, compliance, and safety reviewers.

## Architecture

Layers:

- Physical Port: mechanical/load class, power, thermal, e-fuse, shielding, grounding, EtherCAT, CANopen, IO-Link, USB, PCIe, MIPI/GigE/GMSL where relevant.
- Passport: EEPROM/secure ID, firmware hash, power budget, mass, frames, calibration hash, signature.
- Driver Capsule: ROS 2 lifecycle, ros2_control, QoS, diagnostics, SBOM, license, dependency lock, compatibility matrix.
- Data Schema: LeRobot observation/action features, dtype, unit, FPS, timestamp source, module ID, policy boundary.
- Evidence Pack: test scope, limitations, negative evidence, risk delta, CAD/URDF/USD, certificates, reviewer, install record.

## Qualcomm Fit

Qualcomm should care because a robotics ecosystem cannot rely only on development boards. It needs module vendors to target Qualcomm edge hardware by default.

RoboPort turns Qualcomm edge into:

- a default certification/performance target;
- an AI Hub/QNN profile target for sensors and perception modules;
- a LeRobot-compatible data target;
- a robotics developer kit and classroom kit path;
- an OEM preinstall and marketplace path;
- a recurring ecosystem revenue story.

## Safe Competition Demo

Demo scope:

- tabletop low-voltage module dock, not a moving robot;
- three to four keyed module bays;
- 5V USB-C only, current limit, PTC/eFuse, recessed contacts, no exposed live pins;
- safety MCU owns port power and safe-off;
- modules: RGB camera, IMU/contact/touch, LED/e-paper output, intentionally incompatible/fault module;
- Qualcomm edge board runs ROS 2, UI, QNN assist, recorder, diagnostics;
- no batteries, high voltage, motors, grippers, wheels, solenoids, heaters, lasers, sharp parts, or payload lifting.

Demo flow:

1. Insert valid module; read signed passport.
2. Check policy, current budget, and compatibility matrix.
3. Activate ROS 2 lifecycle driver after safety MCU approval.
4. QNN model checks visual module label/orientation as compatibility assist.
5. Insert invalid/expired/wrong-voltage module; dock remains safe-off.
6. Export LeRobot episode and evidence report.

Safety rule:

> AI and ROS may veto activation. Only the independent safety MCU may enable port power.

Claims to avoid:

- safety-certified;
- universal plug-and-play;
- production-ready industrial robot interface;
- AI-controlled safety;
- QNN validation guarantees correctness;
- LeRobot compatibility means policy transfer works.

## Ask

Support requested:

- Qualcomm edge board and low-voltage I/O guidance.
- AI Hub/QNN profiling path for module-recognition assist model.
- ROS 2 lifecycle and LeRobot metadata review.
- Introductions to module vendors, robot OEMs, SIs, and certification advisors.
- Feedback on “RoboPort Certified” boundary language.

## Sources

- IFR China robotics release: https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_Chinese.pdf
- IFR World Robotics 2025 industrial robots: https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- National Bureau of Statistics May 2026 robot output: https://www.stats.gov.cn/sj/zxfb/202606/t20260616_1963953.html
- AI+Manufacturing action plan: https://www.nda.gov.cn/sjj/zwgk/zcfb/0112/20260107214358696030895_pc.html
- ISO 9409-1 mechanical interfaces: https://www.iso.org/standard/36578.html
- ISO 10218-1:2025 industrial robot safety: https://www.iso.org/standard/73933.html
- ANSI/A3 R15.06-2025 robot safety: https://www.automate.org/robotics/news/new-ansi-a3-r15-06-2025-american-national-standard-for-industrial-robot-safety-now-available-for-purchase
- Universal Robots Marketplace: https://www.universal-robots.com/marketplace/
- IO-Link: https://io-link.com/
- EtherCAT: https://www.ethercat.org/en/technology.html
- ROS-Industrial FAQ: https://rosindustrial.org/about/faq
- ros2_control hardware interfaces: https://control.ros.org/rolling/doc/ros2_control/hardware_interface/doc/hardware_interface_types_userdoc.html
- Qualcomm AI Hub compile documentation: https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- Hugging Face LeRobot: https://github.com/huggingface/lerobot
- ROS 2 managed node lifecycle: https://design.ros2.org/articles/node_lifecycle.html
