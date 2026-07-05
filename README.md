# QC Robotics 2026

Repository for the 2026 Qualcomm Embodied Intelligence and Robotics Developer Competition.

Official competition page: https://qc-robotics-dev.aidlux.com/2026/

## Competition Timeline

- Before 2026-07-20: register, submit project proposal, and complete the preliminary round.
- Before 2026-07-31: organizer ships development boards to shortlisted developers.
- 2026-08 to 2026-11-01: submit final-round work online.
- End of 2026: Qualcomm developer ecosystem conference and awards ceremony.

## Project Direction

This repository is prepared for an edge robotics project that can run perception, reasoning, and control loops on Qualcomm/AidLux-supported robot development hardware.

Working concept:

> A multimodal edge robotics assistant that combines real-time perception, task planning, and human-friendly interaction for practical indoor service or inspection workflows.

The exact hardware target and final demo scenario should be confirmed after registration and board allocation.

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
- Decide the target board and robot form factor.
- Build a small browser-based demo page and deploy it through Cloudflare Pages for judges/reviewers.
- Add the first runnable perception/control prototype under `src/`.

## Deployment Notes

This server has Wrangler and cloudflared configured for publishing demos.

- Static demo site: deploy with Cloudflare Pages.
- Temporary local preview: run `cf-local-tunnel <port>`.

Do not commit Cloudflare credentials, model secrets, API keys, or private VPN/client config files.
