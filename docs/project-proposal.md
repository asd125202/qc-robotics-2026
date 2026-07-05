# Project Proposal Draft

Use this as the source document for the preliminary submission before 2026-07-20.

## 1. Project Name

TBD

## 2. One-Sentence Summary

TBD: A concise description of the robot capability, target user, and measurable benefit.

## 3. Competition Track / Hardware Target

- Track: TBD
- Candidate hardware: Qualcomm/AidLux-supported robotics development board, to be selected or confirmed after registration.
- Robot form factor: TBD, for example mobile base, arm, quadruped, or tabletop robot.

## 4. Problem Statement

Describe the real-world robotics pain point:

- Who has the problem?
- What task is difficult, expensive, unsafe, or repetitive today?
- Why does embodied intelligence help more than a pure web/mobile app?

## 5. Proposed Solution

Describe the robot system:

- Perception: camera, depth, audio, IMU, lidar, or other sensors.
- Understanding: object detection, scene understanding, speech/language interface, or multimodal reasoning.
- Planning: task planning, navigation, manipulation, or inspection workflow.
- Action: robot movement, actuator control, alerts, reports, or human handoff.
- Edge deployment: what runs locally on the board and why.

## 6. Innovation Points

- Edge-first inference and low-latency closed-loop behavior.
- Practical demo scenario with measurable success criteria.
- Modular software stack that can migrate across Qualcomm robotics hardware.
- Human-friendly interaction for non-expert users.

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

- What can be demonstrated before receiving hardware?
- What needs the official development board?
- What fallback demo can run in simulation or on a laptop?

## 9. Evaluation Metrics

- Latency: target end-to-end perception-to-action latency.
- Accuracy: task-specific perception or decision metric.
- Robustness: number of successful task runs out of total trials.
- Usability: setup time, operator steps, and demo clarity.
- Edge performance: CPU/GPU/NPU utilization, memory use, and power notes when available.

## 10. Milestones

See `docs/milestones.md`.

## 11. Team / Contact

TBD

## 12. Submission Assets

- Project proposal PDF.
- Demo video.
- Source repository.
- Cloudflare-hosted project page.
- Installation and reproduction instructions.
