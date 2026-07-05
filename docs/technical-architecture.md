# Technical Architecture

## Target System

The project should be structured as an all-in-one robotics product platform with clear boundaries between robot hardware, edge runtime, LeRobot-compatible data/training workflows, cloud GPU adapters, and demo presentation.

```text
Robot sensors / actuators
  -> RobotMac Core edge runtime
  -> perception + policy inference
  -> local safety boundary + robot control
  -> logs + LeRobotDataset recording
  -> China / overseas cloud GPU training
  -> evaluation + deployment package
  -> Qualcomm edge device update
  -> public pitch/demo dashboard
```

## Software Modules

- `src/edge_runtime/`: Qualcomm device services, sensor ingestion, local inference, logs, and health reporting.
- `src/robot_io/`: camera, motor, CAN/UART/PWM, IMU, audio, and emergency-stop adapters.
- `src/lerobot_bridge/`: dataset recording, metadata conversion, policy training config, and deployment package export.
- `src/cloud_adapters/`: China and overseas cloud GPU job adapters.
- `src/skills/`: skill package manifest, compatibility metadata, safety boundary, and evaluation report.
- `src/ui/`: local dashboard, pitch demo UI, and public Cloudflare Pages presentation.
- `src/eval/`: replay, latency, success rate, smoothness, power/resource measurements.

## Edge Deployment Goals

- Run core perception, policy inference, safety checks, and control locally on the robot board.
- Keep the robot functional without public cloud dependency after a model is deployed.
- Use cloud GPU for training and evaluation, not safety-critical runtime control.
- Demonstrate why Qualcomm edge AI matters: low latency, privacy, power, camera/multimedia, connectivity, and migration across Dragonwing boards.

## Cloudflare Demo Role

Cloudflare is for public project presentation and remote demo access:

- Cloudflare Pages for static Chinese pitch websites and public demo pages.
- `cf-local-tunnel <port>` for temporary live previews from this server.

Do not route robot safety-critical control through a public tunnel.

## Open Questions

- Final board and available acceleration runtime.
- Robot chassis and sensor package.
- Required AidLux runtime version.
- Whether the first real demo should prioritize tabletop manipulation or mobile inspection.
- Which China/overseas cloud providers can be wired first without account friction.
