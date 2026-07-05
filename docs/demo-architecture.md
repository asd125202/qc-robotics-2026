# Demo Architecture

## Demo Goal

在没有正式开发板前，先做一个可解释、可展示、可扩展的最小闭环：

1. 机器人或模拟器产生示教 episode。
2. 数据转成 LeRobot-compatible 格式。
3. 云端训练 job 被创建并显示状态。
4. 训练产物生成模型版本与评估指标。
5. 部署包被推送到目标 Qualcomm 设备。
6. 前端展示设备运行状态、延迟、成功率、失败片段和下一轮训练建议。

拿到开发板后，把第 1、5、6 步接入真实硬件。

## Recommended Demo Form

### Primary Demo: Desktop Manipulation

理由：

- 最容易展示 LeRobot 数据采集和模仿学习。
- 任务成功/失败清晰，适合三分钟视频。
- 与 ACT 策略和公开教程匹配度高。
- 对场地要求低，比赛视频更可控。

任务示例：

- 抓取目标物体并放入指定区域。
- 根据视觉状态选择不同放置区域。
- 失败后人类接管，片段进入下一轮训练数据。

### Fallback Demo: Browser Simulation

如果硬件不可用，先做一个网页模拟：

- 左侧：机器人 episode 列表和视频/状态占位。
- 中间：训练 job 状态、GPU provider、策略模板。
- 右侧：模型版本、边缘设备状态、成功率、延迟。

这可以直接部署到 Cloudflare Pages，作为初赛项目书的补充材料。

## Runtime Layers

```text
Robot / simulator
  -> data recorder
  -> LeRobot dataset adapter
  -> cloud training job adapter
  -> model artifact registry
  -> Qualcomm edge deployment package
  -> edge runtime metrics
  -> Cloudflare pitch/demo dashboard
```

## Edge Runtime Responsibilities

- Camera and sensor capture.
- Policy inference.
- Local safety constraints.
- Robot command output.
- Logging and episode metadata.
- Offline run mode after model deployment.

## Cloud Responsibilities

- Dataset storage.
- GPU training.
- Evaluation and replay.
- Model export.
- Deployment package registry.
- Non-safety-critical telemetry and pitch dashboard.

## Safety Boundary

Do:

- Use Cloudflare Pages for public pitch/demo website.
- Use cloud GPU for training and evaluation.
- Show remote telemetry, logs, dataset versions, and non-critical status.

Do not:

- Route safety-critical robot control through Cloudflare or public tunnels.
- Depend on public network for emergency stop or local collision avoidance.
- Hide the difference between demo telemetry and real robot control.

## Metrics To Show

- Task success rate.
- End-to-end inference latency.
- Control frequency.
- GPU training time and provider.
- Dataset size and number of episodes.
- Model version.
- CPU/GPU/NPU/memory utilization when hardware is available.
- Number of recovered failure cases.

## Implementation Stages

### Stage 0: Pitch Assets

- Chinese seven-page website.
- Product thesis.
- Research notes.
- Scoring alignment table.
- Demo architecture document.

### Stage 1: Simulated Product Dashboard

- Static or client-side JSON data.
- Fake but plausible training jobs and model versions.
- Device status mock for QCS8550 / QCS6490 / IQ-8275.

### Stage 2: LeRobot Workflow Prototype

- Use a public or small recorded LeRobot dataset.
- Run a minimal training/evaluation script in a cloud GPU environment.
- Generate a model artifact manifest.

### Stage 3: Hardware Integration

- Bring up camera and robot IO.
- Record real episode data.
- Run inference locally on Qualcomm target.
- Compare cloud-trained and locally deployed metrics.

### Stage 4: Final Video

- 10 seconds: problem and product.
- 30 seconds: hardware/core module and local safety boundary.
- 45 seconds: data collection.
- 45 seconds: cloud training and evaluation.
- 45 seconds: edge deployment and task execution.
- 25 seconds: commercial model and Qualcomm strategic value.
