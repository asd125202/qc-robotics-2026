# Project Proposal Draft

Use this as the source document for the preliminary submission before 2026-07-20. Competition facts extracted from the official page are in `docs/competition-info.md`.

## 1. Project Name

Working title: `RobotMac Core + LeRobot CloudTwin`

## 2. One-Sentence Summary

An all-in-one Qualcomm-powered robotics platform that lets developers collect real robot data, train robot policies in China or overseas cloud GPU environments through LeRobot-compatible workflows, and deploy the resulting skills back to edge robot hardware without rebuilding power, compute, IO, and training infrastructure from scratch.

## 3. Competition Track / Hardware Target

- Track: Standard Track first; Pioneer Track can be framed as a high-end industrial extension.
- Candidate hardware: APLUX Rhino X1 / Qualcomm Dragonwing QCS8550 first, with Radxa Dragon Q6A / QCS6490 as compact standard-track migration and Arduino VENTUNO Q / IQ-8275 as future high-end industrial line.
- Robot form factor: tabletop manipulator or compact mobile manipulator for the first demo, because it can clearly show data collection, policy training, edge deployment, and commercial packaging.

## 4. Problem Statement

Robotics developers, education teams, system integrators, and early-stage service robot companies still need to assemble too much low-level infrastructure before they can build a useful robot application. They must choose development boards, design power supply, handle motor and sensor IO, record data, rent GPUs, train models, convert models, deploy to edge hardware, and debug the result in the real world.

This makes robotics feel like building a personal computer from raw parts before the Mac/Windows era. The commercial opportunity is to make a robotics product platform where the hardware, runtime, training pipeline, and deployment workflow are integrated enough that users can focus on the robot task and business scenario.

## 5. Proposed Solution

The proposed product combines four layers:

- `RobotMac Core`: Qualcomm-powered edge AI compute, power management, robot IO, safety boundary, logging, and local runtime.
- `LeRobot CloudTwin`: data collection, LeRobotDataset conversion, cloud GPU training, evaluation, and deployment package generation.
- `SkillDock`: a future robot skill marketplace where trained skills include model weights, dependencies, IO contract, evaluation report, safety boundary, and target hardware compatibility.
- `Embodied Kit`: a procurement-ready hardware and software bundle for education, factories, labs, service robotics teams, and system integrators.

The first competition demo should show a compact robot recording demonstration data, training an ACT policy in the cloud, deploying it back to Qualcomm edge hardware, and displaying metrics through a public Chinese pitch website.

## 6. Innovation Points

- Productizing the LeRobot workflow instead of showing a one-off algorithm demo.
- China and overseas cloud-training versions with the same training job specification.
- Qualcomm edge AI as the real-time local execution target, not just a generic compute board.
- Skill package concept that can turn robot capabilities into installable, certified, upgradable products.
- Commercial framing around hardware kits, training subscription, skill marketplace, and enterprise services.

## 7. Technical Architecture

Summarize the architecture in a few layers:

- Sensors and robot hardware.
- Runtime services.
- Model inference.
- Control loop.
- Web dashboard or demo interface.
- Logging and evaluation.

See `docs/technical-architecture.md`.

## 8. Feasibility Plan

- Before receiving hardware: Chinese pitch websites, LeRobot dataset/training mock workflow, cloud provider adapter design, simulated or laptop-based training dashboard, and a recorded workflow using public LeRobot examples.
- After receiving hardware: camera/robot IO bring-up, real data collection, edge inference profiling, robot control loop, demo video showing the model running on the device.
- Fallback: laptop or cloud-hosted browser demo that shows data collection, training job submission, model versioning, and deployment package generation without safety-critical remote control.

## 9. Evaluation Metrics

- Latency: target end-to-end perception-to-action latency.
- Accuracy: task-specific perception or decision metric.
- Robustness: number of successful task runs out of total trials.
- Usability: setup time, operator steps, and demo clarity.
- Edge performance: CPU/GPU/NPU utilization, memory use, and power notes when available.

## 10. Milestones

See `docs/milestones.md`.

## 11. Team / Contact

Registration owner and final team-member details should be filled from the official competition registration form before submission.

## 12. Submission Assets

- Project proposal PDF.
- Demo video.
- Source repository.
- Cloudflare-hosted project page.
- Installation and reproduction instructions.
