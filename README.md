# QC Robotics 2026

Repository for the 2026 Qualcomm Embodied Intelligence and Robotics Developer Competition.

Official competition page: https://qc-robotics-dev.aidlux.com/2026/

## Competition Timeline

- Before 2026-07-20: register, submit project proposal, and complete the preliminary round.
- Before 2026-07-31: organizer ships development boards to shortlisted developers.
- 2026-08 to 2026-11-01: submit final-round work online.
- End of 2026: Qualcomm developer ecosystem conference and awards ceremony.

## Project Direction

This repository is prepared for a commercial-ready robotics platform concept for the 2026 Qualcomm Embodied Intelligence and Robotics Developer Competition.

Working concept:

> An all-in-one robotics product platform that combines Qualcomm Dragonwing edge AI hardware, LeRobot-compatible real-world data workflows, and China/overseas cloud GPU training so users can build robot applications without starting from power supply, compute board, drivers, and training infrastructure.

The current first-batch pitch directions are:

- `RobotMac Core`: all-in-one robotics compute, power, IO, safety, and runtime core.
- `LeRobot CloudTwin`: real robot data collection, cloud GPU training, and Qualcomm edge deployment loop.
- `SkillDock`: robot skill marketplace where trained skills can be installed, certified, and upgraded.
- `Embodied Kit`: procurement-ready industry kit for factories, labs, education, and service robotics teams.
- `DragonWorks`: Qualcomm-first robotics developer workbench for devices, datasets, training, deployment, and skills.
- `EdgeFleet`: fleet operations layer for enterprise robot maintenance, logging, updates, and training feedback.
- `EduForge`: education and developer kit for teaching the full LeRobot-to-Qualcomm edge deployment loop.
- `JudgeDeck`: judge-facing scoring alignment and three-minute demo storyboard.
- `Prototype`: interactive static dashboard that simulates devices, datasets, cloud training, model deployment, and skill packages.
- `CloudPlan`: provider execution and budget story for China and overseas cloud GPU training.
- `HardwareMap`: physical product-line and BOM story for QCS6490, QCS8550, IQ-8275, and future IQ10.
- `BusinessCase`: commercialization, buyer personas, package strategy, and recurring revenue flywheel.
- `SubmissionKit`: preliminary project-book structure, official upload constraints, and submission readiness checklist.
- `VerticalPlaybooks`: factory, logistics, lab, campus/service, and education market product packages.
- `DataFlywheel`: teleoperation, dataset ledger, cloud training, edge deployment, and failure-mining loop.
- `SafetyOps`: safety runtime, skill permissions, model release gates, audit ledger, and compliance evidence pack.
- `DualCloudOps`: China/overseas GPU-cloud provider adapters behind one LeRobot training job contract.
- `RevenueStack`: pricing ladder, pilot contracts, recurring revenue lines, and Qualcomm ecosystem economics.
- `RobotAppLayer`: stable application SDK above ROS 2, LeRobot data/policies, fleet operations, and Qualcomm edge deployment.
- `LabForgePilot`: competition main-demo package for desktop arm sample transfer, training, edge deployment, and failure feedback.
- `EdgeRuntimeBench`: Qualcomm edge compile/profile/deploy evidence chain for policy packages and runtime metrics.
- `BoardBringupKit`: board-to-robot bring-up package for power, camera, IO, safety, runtime image, and validation gates.
- `PilotContractKit`: 4-8 week enterprise pilot contract package with KPIs, acceptance criteria, training deliverables, and expansion path.

## Repo Layout

```text
.
├── demos/                 # Demo scripts, videos, and reproducible walkthroughs
├── docs/                  # Competition proposal, schedule, architecture, checklist
├── hardware/              # Board notes, wiring, sensors, robot chassis notes
├── models/                # Model conversion/deployment notes; avoid committing large weights
├── scripts/               # Build, deploy, and utility scripts
└── src/                   # Application source code
```

## Near-Term Tasks

- Finalize the project name and one-sentence value proposition.
- Complete `docs/project-proposal.md` before the 2026-07-20 preliminary deadline.
- Use `docs/product-thesis.md`, `docs/concept-portfolio.md`, and `sites/` as the first concept batch.
- Use `docs/competition-info.md` as the local contest reference when shaping the proposal and demo plan.
- Decide the target board and robot form factor.
- Build a small browser-based demo page and deploy it through Cloudflare Pages for judges/reviewers.
- Add the first runnable perception/control prototype under `src/`.

## Deployment Notes

This server has Wrangler and cloudflared configured for publishing demos.

- Static demo site: deploy with Cloudflare Pages.
- Current Chinese pitch site: https://qc-robotics-2026.pages.dev/
- Temporary local preview: run `cf-local-tunnel <port>`.

Do not commit Cloudflare credentials, model secrets, API keys, or private VPN/client config files.
