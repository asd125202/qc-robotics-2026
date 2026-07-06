# BusinessCase

更新时间：2026-07-06。

BusinessCase is the commercial pitch layer for the Qualcomm robotics competition. It reframes RobotMac from a technical stack into a buyer-ready path from robot demo to deployable business.

> Robotics does not need another impressive demo. It needs a path from demo to deployment.

## One-Line Company

BusinessCase packages RobotMac Core, LeRobot CloudTwin, TrainRouter, SkillDock, EdgeFleet, and EduForge into a commercial robotics product base for teams that need deployment, not another dev-board experiment.

Chinese pitch:

> 机器人不缺会动的 Demo，缺的是从 Demo 到可部署生意的路。

## Problem

Robotics teams often succeed at demonstrations but fail between prototype and deployment:

- hardware integration is custom and fragile;
- real-world data capture is not versioned;
- cloud training is hard to reproduce;
- edge deployment is a manual artifact;
- robot skills are not packaged for reuse;
- buyers cannot see safety boundaries, acceptance metrics, support contracts, or rollback plans;
- Qualcomm value is reduced to “we used a board” instead of becoming the default edge target.

The buyer pain is time, risk, deployment failure, maintenance cost, and unclear responsibility.

## Why Now

Signals gathered on 2026-07-06:

- IFR World Robotics 2025 reported 542,000 industrial robots installed in 2024 and 4.664 million operating globally.
- China installed about 295,000 industrial robots in 2024, about 54% of global deployments, and had more than 2 million industrial robots operating.
- China NBS reported 2025 output of 773,074 industrial robots and 18,581,081 service robots.
- IFR service robot reporting shows professional service robots and RaaS fleets growing, especially logistics and cleaning.
- Humanoid deployments such as Figure/BMW and GXO/Agility show narrow, measured production tasks are becoming real, but not yet universal humanoid labor.
- LeRobot makes robot datasets, policies, training, and open robot-learning workflows more accessible.
- Qualcomm Dragonwing, AI Hub, and edge developer tooling create a stronger path from prototype to production edge deployment.

Conclusion:

The credible opportunity is not “huge humanoid TAM.” It is a commercial robotics enablement stack for bounded tasks.

## Insight

The next robotics business is not only a robot body, a ROS distribution, a GPU rental workflow, or a dashboard.

It is a learning loop:

1. record real task data;
2. train a policy;
3. deploy to edge hardware;
4. observe failures;
5. package the improved skill;
6. sell the kit, subscription, skill, and operations contract.

## Solution

RobotMac is a Qualcomm-first commercialization layer for open robot learning:

- `RobotMac Core`: integrated edge compute, power, IO, sensors, and reference robot kit.
- `LeRobot CloudTwin`: datasets, training jobs, evaluation reports, and deployment artifacts.
- `TrainRouter`: China/overseas dual-cloud GPU routing with budget caps and data boundaries.
- `SkillDock`: robot skill packages, model versions, runtime constraints, evaluation, and marketplace distribution.
- `EdgeFleet`: logs, failures, OTA, remote support, fleet health, and recurring service contracts.
- `EduForge`: education kits, courses, competitions, and developer certification.

## Product Workflow

First-day user journey:

1. Select robot form factor and task template.
2. Capture LeRobot-compatible demonstrations through TeleopStudio.
3. Route training through TrainRouter.
4. Generate evaluation report and deployment package.
5. Deploy to Qualcomm edge target.
6. Run the robot and capture failures.
7. Convert failure clips into the next dataset/version.
8. Package the skill for internal reuse or marketplace distribution.

## Market Wedge

First buyers:

| Buyer | Why they pay |
| --- | --- |
| Universities / training camps | Need a complete course from data capture to edge deployment, not only a robot arm. |
| Robotics startups | Need to avoid spending months on power, drivers, training infrastructure, and deployment tooling. |
| System integrators | Need reusable templates, skill packages, acceptance evidence, and support contracts. |
| SME pilots | Need fixed-scope 60-90 day automation trials with clear KPIs and low CapEx risk. |
| Enterprise innovation teams | Need a path from one pilot to fleet operations and private skill libraries. |

## Business Model

One-line model:

> Sell the kit, then monetize the learning loop.

Revenue layers:

1. Hardware kit margin.
2. Cloud training subscription.
3. Skill marketplace take rate.
4. Fleet operations contract.
5. Education/course licensing.
6. Certification or target-validation service.

## Package Strategy

### Developer / Edu Kit

Low-cost LeRobot-compatible desktop arm, optional Qualcomm edge target, course materials, dataset templates, and cloud credits.

### Pro Kit

Competition/startup package with RobotMac Core, TeleopStudio, CloudTwin, edge deployment manifest, and dashboard.

### SME Pilot

60-90 day fixed-scope paid pilot for one bounded workflow such as inspection, pick/place, kitting, machine tending, cleaning, or lab transfer.

### Enterprise / RaaS

Industry kit, private data plane, fleet operations, SLA support, maintenance, and monthly/RaaS packaging.

## Go To Market

Path:

1. Competition demo and public Chinese pitch site.
2. Developer samples and repo documentation.
3. Education pilots with EduForge.
4. Integrator templates for bounded workflows.
5. Enterprise pilot and private skill library.
6. Fleet operations and recurring support.

## Dual Cloud Training

Use one job contract and two regional data planes.

China lane:

- Primary anchor: Alibaba Cloud PAI.
- Demo/dev adapters: AutoDL.
- Industrial/government options: Huawei ModelArts and Tencent GPU.
- Raw robot video, teleop data, customer layouts, and sensitive data stay in mainland China.

Overseas lane:

- Primary developer-cost anchor: Runpod.
- Enterprise/team option: Lambda.
- Short evaluation/export jobs: Modal.
- Region, DPA/SCC, HIPAA/BAA, export-control, and GPU availability must be rechecked before real quotation.

The product does not sell cheap GPUs. It sells predictable robotics training: data boundary, budget cap, provider routing, common evaluation, and Qualcomm edge artifact export.

## Competition

Respectful map:

- ROS / ROS 2: developer substrate, not commercial product packaging.
- NVIDIA Jetson / Isaac: strong physical AI stack, but GPU-centric and not Qualcomm-first.
- Hugging Face LeRobot: strong open robot-learning engine, but not a managed commercial training/deployment platform.
- Viam / Foxglove / Formant: validate robot SaaS, observability, and fleet operations, but do not start from hardware kit and LeRobot-native learning loop.
- UR+ / ABB / MiR ecosystems: prove marketplace and certified accessories reduce risk, but are brand/workcell-specific.
- Unitree / AgileX / AgiBot / UBTECH / Fourier and other China players: prove hardware supply and embodied-AI demand, but many are body-first.
- Figure / Agility / 1X / Apptronik: prove long-term humanoid ambition, but they sell their own bodies and closed ecosystems.

BusinessCase wedge:

> RobotMac Core is not another robot body, another ROS distribution, or another cloud dashboard. It is the commercialization layer that turns open robot learning into deployable Qualcomm-edge robot products.

## Moat

Accumulating advantages:

- Task data and failed episodes.
- Skill packages and evaluation reports.
- Hardware compatibility and deployment evidence.
- Education and integrator distribution.
- Qualcomm edge target familiarity.
- Private enterprise skill libraries.
- Fleet operations history and support contracts.

Every failed attempt becomes a better deployable skill.

## Why Qualcomm

Qualcomm should be framed as commercially necessary, not decorative.

Robots need:

- low-latency local inference;
- multi-camera and sensor input;
- power and thermal control;
- offline/weak-network resilience;
- connectivity;
- secure deployment;
- edge profiling and optimization;
- a developer ecosystem that can move from prototype to production.

Qualcomm value:

- Dragonwing becomes the default robotics edge target.
- AI Hub / Qualcomm AI Stack can become the skill optimization, profiling, and deployment evidence layer.
- Education kits, integrator pilots, and enterprise fleets bring developers and buyers back to Qualcomm platforms.

## Demo

Recommended demo:

`LabForgePilot` desktop arm sample-transfer workcell.

Three-minute story:

1. Capture 10-20 demonstration episodes.
2. Convert to LeRobot-compatible dataset.
3. Train through CloudTwin / TrainRouter.
4. Generate model version and evaluation report.
5. Export Qualcomm edge package.
6. Run pick/place/sample transfer.
7. Show one failure or human intervention.
8. Send that clip back to the next training loop.

Fallback:

If target hardware is not available before the contest stage, show web dashboard, recorded data, mock edge metrics clearly marked as simulated/target/pending validation.

## Ask

Ask Qualcomm for:

1. Target hardware or reference-design testing path.
2. AI Hub / Qualcomm AI Stack deployment guidance.
3. Dragonwing Robotics Hub developer publication support.
4. Lightweight “Qualcomm validated robot skill package” criteria.
5. Education, developer, system-integrator, or enterprise pilot introductions.

## Claim Boundaries

Do not claim:

- official Qualcomm certification;
- actual AI Hub validation before testing;
- possession of a specific development board unless confirmed;
- simulated dashboard metrics as real measurements;
- Cloudflare public pages as part of the safety-control chain;
- universal humanoid replacement or safety-certified robot autonomy.

Can claim:

- a proposed Qualcomm-first commercial robotics path;
- LeRobot-compatible workflow;
- dual-cloud training architecture;
- demo-to-deployment business model;
- clear verification and partnership asks.

## Sources

- IFR industrial robots 2025: https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots 2025 executive summary: https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Service_Robots.pdf
- China NBS 2025 robot output: https://www.stats.gov.cn/english/PressRelease/202601/t20260120_1962350.html
- A3 North America robot orders 2025: https://www.automate.org/robotics/news/robot-orders-grow-6-6-in-2025-as-general-industries-drive-broader-automation-adoption
- Figure BMW production update: https://www.figure.ai/news/production-at-bmw
- Hugging Face LeRobot: https://huggingface.co/docs/lerobot/en/index
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Qualcomm Dragonwing Robotics Hub: https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Dragonwing prototype to deployment: https://www.qualcomm.com/developer/blog/2026/05/edge-ai-prototype-deployment-qualcomm-dragonwing-developer-ecosystem
- Qualcomm AI Hub: https://aihub.qualcomm.com/
- Alibaba Cloud PAI: https://www.alibabacloud.com/en/product/machine-learning?_p_lc=1
- Runpod pricing: https://www.runpod.io/pricing
- Lambda GPU pricing: https://lambda.ai/instances
- Modal pricing: https://modal.com/pricing
