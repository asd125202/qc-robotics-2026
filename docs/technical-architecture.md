# Technical Architecture

## Target System

The project should be structured as an edge robotics application with clear boundaries between sensing, model inference, planning, control, and demo presentation.

```text
Sensors
  -> perception pipeline
  -> scene/task state
  -> planner
  -> robot control or user-facing action
  -> logs, metrics, and web dashboard
```

## Software Modules

- `src/perception/`: camera and sensor ingestion, detection, tracking, scene features.
- `src/planning/`: task state machine, policy, route/action decisions.
- `src/control/`: robot command adapters and safety constraints.
- `src/ui/`: local dashboard or demo UI if needed.
- `src/eval/`: metrics, replay, benchmark scripts.

## Edge Deployment Goals

- Run core inference locally on the robot board.
- Keep the control loop functional without cloud dependency.
- Use cloud only for demo sharing, logs, optional model updates, or non-critical visualization.

## Cloudflare Demo Role

Cloudflare is for public project presentation and remote demo access:

- Cloudflare Pages for static project/demo pages.
- `cf-local-tunnel <port>` for temporary live previews from this server.

Do not route robot safety-critical control through a public tunnel.

## Open Questions

- Final board and available acceleration runtime.
- Robot chassis and sensor package.
- Required AidLux runtime version.
- Final competition submission format.
