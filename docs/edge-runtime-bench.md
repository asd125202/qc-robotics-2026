# EdgeRuntimeBench Pitch

更新时间：2026-07-07。

## One-Line Thesis

EdgeRuntimeBench 是 Physical AI 的运行时证据层：把 LeRobot / ACT / SmolVLA / VLM 机器人策略从“demo 能跑”，变成“有证据地在 Qualcomm Dragonwing 边缘设备上上线、门禁、验收、计费和回滚”。

一句话：

> 它是边缘 AI 运行时的 CI benchmark + safety gate + procurement scorecard。

它连接：

- LabForgePilot：产生真实样本转移任务。
- RobotAppLayer：执行 `.rap` 技能包。
- SafetyOps：设定 release gate 和运动权限。
- SkillDock：发布认证技能。
- EdgeFleet：灰度部署、监控和回滚。
- RevenueStack：把性能、可靠性和节省转成价格与合同。

## 01 · Problem

机器人团队现在不缺模型，缺的是“能上线的证据”。

同一技能在不同设备、运行时、量化路径、温度、电量、相机、固件和网络条件下，结果会变。采购、CTO、安全负责人和评委真正问的不是 TOPS，而是：

- p99 延迟多少？
- 会不会热降频掉帧？
- 断网还能不能跑？
- 是否真的走 QNN / NPU，还是静默 fallback 到 CPU？
- 每 1,000 次任务成本多少？
- SafetyOps gate 是否通过？
- 出错后能否回滚到 previous-known-good？

机器人场景尤其痛：

- 模型延迟不等于机器人端到端动作延迟。
- `tokens/sec` 不能回答 AMR、机械臂、实验台 robot 是否能安全完成任务。
- camera frame age、preprocess、inference、postprocess、action serialization 和 actuator ack 都会影响动作。
- dataset revision、LeRobot version、checkpoint、camera schema、normalization stats 和 action schema 如果没锁定，策略不可追溯。

## 02 · Current Alternatives Fail

EdgeRuntimeBench 不替代 Qualcomm AI Hub、QAIRT/QNN、ONNX Runtime、LiteRT、ExecuTorch、Edge Impulse、MLPerf、Roboflow、Greengrass、Viam 或测试认证。它把这些底层能力组织成一个机器人上线证据图。

- MLPerf / MLMark：权威，但定位是标准化推理性能，不是客户私有机器人任务、运行时选择、安全门和采购决策。
- Qualcomm AI Hub：能 optimize、compile、profile、run inference，并在 hosted Qualcomm devices 上执行；但不是端到端机器人技能认证、fleet 回归和 ROI 报告层。
- QAIRT / QNN scripts：能生成 context binary、CSV、QHAS/optrace，但证据分散在命令、bin、log 和 wrapper 里。
- ONNX Runtime QNN / LiteRT-QNN / ExecuTorch-QNN：运行时入口越来越多，团队需要知道“哪条路径可上线”，不是再读一堆 SDK 文档。
- Edge Impulse：真实数据、训练、优化、部署和 drift 工作流很强；但作为 Qualcomm 生态资产，也更适合成为输入/渠道，而不是独立采购证据层。
- Roboflow / Ultralytics：视觉开发和导出体验好；不覆盖机器人安全门、fleet rollback、ODD 和客户验收。
- AWS Greengrass / Viam / Peridio / balena：部署和 fleet 能力强；不回答某个模型、runtime、device、OS、thermal envelope 是否适合这个物理任务。

现状通常是 spreadsheet + profiler + demo video。它不能复现，不能审计，不能进入采购语言。

## 03 · Solution

EdgeRuntimeBench 输入模型、机器人技能、目标设备、运行时、量化策略和场景约束，输出 `ship / no-ship` 证据卡、最佳 runtime route、成本评分和安全评分。

核心流程：

```text
Policy package
→ Lineage lock
→ Runtime matrix
→ Replay parity
→ Live edge loop
→ SafetyOps release gate
→ Evidence card
→ SkillDock certification
→ EdgeFleet canary
→ RevenueStack ROI
```

它回答四个问题：

1. 这份 policy 从哪个 LeRobotDataset v3、哪个 checkpoint、哪个训练命令来？
2. 它在 RB3/QCS6490、QCS8550、IQ-series 或 proxy device 上走哪条 runtime path？
3. 它在真实 robot loop 里是否满足 p99、jitter、frame age、thermal、memory、unsafe stop 和 cloud call 门槛？
4. 它能否被签名发布、审计、灰度、回滚和收费？

## 04 · Why Now

边缘 AI 已经进入采购窗口。Fortune Business Insights 估算全球 Edge AI 市场 2026 年约 469.6 亿美元，到 2034 年约 4457.5 亿美元；Edge AI hardware 2026 年约 66.5 亿美元，到 2034 年约 226.6 亿美元。Grand View Research 估算 AI in Robotics 2026 年约 261 亿美元，到 2033 年约 1827 亿美元。

技术窗口也刚好打开：

- LeRobot v0.6.0 在 2026-07-06 发布，2026-07-07 博客发布，强化 `lerobot-rollout`、DAgger-style HIL corrections、unified `lerobot-eval`、benchmark families、depth/language dataset 和 HF Jobs。
- LeRobotDataset v3 已经把 state/action/timestamps、MP4 camera streams、metadata、stats、tasks、normalization 和 episode split 组织成可追溯数据格式。
- ACT 是可靠 baseline；SmolVLA 是语言条件升级；RTC 让高延迟 VLA 可以异步 chunk 执行。
- Qualcomm 在 Dragonwing、AI Hub、QAIRT/QNN、ONNX Runtime QNN、Edge Impulse 和 IoT ecosystem 上持续加码。
- Qualcomm 2026-06-24 宣布拟收购 Modular，强化 edge-to-cloud、开放、异构 AI 软件生态方向。

为什么比赛里要做：

- LabForgePilot 给真实物理任务。
- EdgeRuntimeBench 证明策略不只是 notebook checkpoint。
- SafetyOps 证明这个策略能否移动机器人。
- Qualcomm 的价值被落到 compile/profile/runtime/fallback/evidence，而不是一句“用了高通板卡”。

## 05 · Product

EdgeRuntimeBench 的核心界面四块：

1. `Runtime Matrix`：比较 `device x runtime x quantization x firmware x thermal profile x network profile`。
2. `Scenario Lab`：把 LabForgePilot、仓储拣货、巡检、安防、实验室机械臂操作变成任务脚本。
3. `Evidence Card`：p50/p95/p99、jitter、load time、memory、NPU/GPU/CPU utilization、energy/task、thermal throttle、task success、unsafe stop、cloud calls、cost/1k tasks。
4. `Fleet Rollout`：通过 EdgeFleet 做 canary；SafetyOps 失败即阻断；通过后写入 SkillDock 认证版本。

产品状态：

- `Ready`
- `Needs Quantization`
- `Unsupported`
- `Runtime Risk`
- `Blocked by SafetyOps`
- `Rollback Required`

产品模块：

- `Lineage Graph`：dataset -> train config -> checkpoint -> policy card -> export candidate -> eval -> edge package -> HIL feedback。
- `Contract Inspector`：检查 camera names、image size、FPS、state/action shape、task prompt、control mode、normalization stats。
- `Export Matrix`：PyTorch native、ONNX、ONNX+QNN、LiteRT-QNN、ExecuTorch-QNN、TensorRT、native RTC，标记 supported / experimental / blocked。
- `Replay Parity`：用 held-out LeRobot episode 比较 PyTorch vs export 的 action chunks、drift、latency 和 queue gaps。
- `Live Edge Loop`：camera -> preprocess -> inference -> postprocess -> action commit -> actuator ack 的端到端 trace。
- `Release Dossier`：device registry、policy manifest、Qualcomm export manifest、edge profile、install audit、SafetyOps gate、SBOM、provenance、rollback。

## 06 · Product API/Evidence

API 不是替代 AI Hub，而是把 AI Hub 和本地 robot rig 的低层指标升级成“这个技能能否上线、采购哪块板、卖多少钱”的证据。

示例命令：

```bash
edgebench run lab_transfer.yaml \
  --targets rb3-qcs6490:onnx-qnn,qcs8550:onnx-qnn,rb3-qcs6490:litert-qnn \
  --gates "p99<80ms,task_success>98%,unsafe_stop=0,throttle<1%,cloud_calls=0"
```

输出：

```text
ship_score=91
winner=rb3-qcs6490/onnx-qnn/int8
p99=61ms
energy=measured-by-us
thermal_throttle=0.2%
cloud_calls=0
SafetyOps=pass
release=ready-for-canary
```

所有指标必须标注来源：

- `measured-on-board`
- `AI-Hub-device-cloud`
- `proxy`
- `replay-eval`
- `simulated`
- `customer-site`

核心对象：

- `RunSpec`：scenario、robot、policy、device targets、runtime targets、gates、ODD、network mode。
- `LineageManifest`：LeRobot version、dataset repo、dataset hash、model card、checkpoint、training command、license、camera schema、normalization stats。
- `SUTManifest`：board、SoC、OS、kernel、firmware、runtime、ORT/QNN/LiteRT/ExecuTorch version、container digest、driver stack。
- `CycleTrace`：capture、preprocess、inference、postprocess、action commit、actuator ack、deadline、safety state、backend used。
- `ProfileSummary`：latency p50/p95/p99、action rate、control FPS、jitter、deadline miss、frame age、memory、thermal、power。
- `BackendReport`：HTP/GPU/CPU backend、fallback、unsupported ops、context cache、QNN profile CSV、optrace/QHAS links。
- `SafetyReleaseGate`：ODD、permissions、thresholds、SafetyOps decision、fail reasons、rollback pointer、previous-known-good。
- `ReleaseDossier`：SBOM、SLSA/provenance、model/system card、NIST AI RMF mapping、NIST SSDF checks、VEX/KEV status、approvals。
- `VideoProofIndex`：把三分钟视频时间码映射到 model hash、device log、profile chart、incident 和 rollback artifact。

比赛证据包：

- `device-registry.json`
- `policy-artifact-manifest.json`
- `lerobot-lineage.json`
- `qualcomm-export-manifest.json`
- `edge-profile.qualcomm.json`
- `runtime-matrix.csv`
- `safetyops-release-gate.json`
- `release-dossier.json`
- `install-audit-log.jsonl`
- `incident-ledger.jsonl`
- `rollback-record.json`
- `video-proof-index.md`

## 07 · Market & Business Model

EdgeRuntimeBench 在钱发生的地方收费：采购、验收、保险、上架、更新和持续回归。

客户：

1. Robot OEM：赢 RFP，证明 SKU claims，缩短 design-in 周期。
2. System integrators：FAT/SAT acceptance，里程碑付款证明，减少争议。
3. Enterprises / factories / labs：供应商选择、uptime risk、EHS/compliance、audit trail。
4. Regulated robotics buyers：AI Act readiness、ISO 机器人安全流程、技术文档和 post-market monitoring。
5. Insurers / financiers：underwriting、performance-risk pricing、lease-ready diligence。
6. Marketplace operators：trust badge、seller evidence API、certified skill 上架。

中国版：

- OEM SKU evidence campaign：¥29,800-98,000/campaign。
- SI FAT/SAT project pack：¥80,000-300,000/project。
- Enterprise site license：¥180,000-800,000/site/year。
- Continuous device monitoring：¥50-200/device/month。
- Marketplace evidence badge：¥10,000-50,000/listing/year。

海外版：

- Team SaaS：$2,000-$8,000/month。
- OEM evidence pack：$7,500-$25,000/campaign。
- SI project pack：$20,000-$75,000/project。
- Enterprise site license：$60,000-$250,000/site/year。
- Monitoring：$20-$100/device/month。
- Certified skill badge：$2,500-$15,000/listing/year。

90 天 design-partner KPI：

- 10 个 design partners。
- 5 类 Qualcomm / Dragonwing / Snapdragon target。
- 30 个 certified skills。
- 评估周期从 2-3 周降到 48 小时内。
- runtime regression 复现率 >95%。
- 首批付费 pipeline >$250k。

## 08 · Competition & Moat

竞争不是“谁有 profiler”，而是谁能成为上线、验收、保险和 marketplace 共同接受的证据格式。

竞争图：

- NVIDIA Jetson / TensorRT / TAO / public benchmarks：证明姿态强，特别适合 performance narrative。
- Qualcomm AI Hub / Edge Impulse：底层能力和生态渠道强，是合作 substrate，也是潜在内建竞争。
- MLCommons / EEMBC：标准强，但不是客户私有场景 CI。
- Roboflow / Ultralytics：视觉模型 workflow 强，不覆盖机器人 release dossier。
- Greengrass / Viam / Peridio / balena：fleet 和 OTA 强，不做 runtime procurement scorecard。
- Testing labs / certification bodies：权威强，但慢、贵，不适合每周模型更新。

Moat：

- `Evidence Graph`：hardware、firmware、runtime、model、dataset、sensor、environment、power、thermal、robot workload 和 outcome 绑定。
- `Raw Artifacts`：profile CSV、QNN log、optrace、rosbag、JSONL、hash、manifest 和复现命令。
- `Scenario Packs`：LabForgePilot、AMR picking、inspection、retail shelf、security patrol、smart camera 等真实任务包。
- `SafetyOps Labels`：unsafe stop、human override、ODD violation、latency miss、fallback 和 rollback 事件成为训练和验收资产。
- `Acceptance Language`：进入 RFP、FAT/SAT、marketplace、保险和客户验收模板后形成路径依赖。
- `Continuous Revenue`：每次模型、firmware、runtime、camera、site 条件变化都要求 refresh evidence。

## 09 · Why Qualcomm

EdgeRuntimeBench 把“用了 Qualcomm”变成比赛和商业都能检查的证据链。

Qualcomm-specific 路线：

- RB3 Gen 2 / QCS6490：2026 年 7 月最现实的比赛 MVP target，可做本地板端或 AI Hub device-cloud/proxy evidence。
- QCS8550：高性能扩展 target，适合多相机、多模型和更高 edge AI workload。
- IQ-series / IQ-9075 / IQ9：工业高端 bridge，可用于 rugged robot runtime story。
- IQ10 RRD：roadmap / early access ask；不写成 2026 年 7 月已集成量产硬件。
- AI Hub Workbench + QAIRT/QNN：生成 compile、profile、backend、context cache、fallback、runtime/load/memory evidence。
- ONNX Runtime QNN / LiteRT-QNN / ExecuTorch-QNN：比较不同 deployment route，给出上线建议。
- QRB ROS / QIR path：把 QNN 推理接入 ROS camera/inference nodes，并记录 topic timing 和 pipeline delay。

对 Qualcomm 的价值：

- 缩短 design-in 周期。
- 减少 SDK support 摩擦。
- 提高 Dragonwing / Snapdragon attach rate。
- 用 performance-per-watt、offline safety 和 release evidence 对抗 NVIDIA 的公开 benchmark 叙事。
- 把 AI Hub profile 从 developer artifact 升级成 procurement artifact。

边界：

- 不声称改进 Qualcomm 编译器或 NPU 性能。
- 不说“全链路 NPU”除非已经验证禁用 fallback。
- 不把 IQ10 写成当前比赛硬件。
- 不把模型 profile 误写成系统级安全认证。

## 10 · Demo & Ask

Demo 叙事：

> LabForgePilot creates the real robot task. EdgeRuntimeBench proves the trained policy was compiled/profiled/deployed against a Qualcomm target. SafetyOps decides whether that exact policy may move the robot.

3 分钟视频：

1. 0:00-0:20：LabForgePilot 导入样本转移任务，展示 board、camera、robot、E-stop、runtime terminal。
2. 0:20-0:55：EdgeRuntimeBench 读取 LeRobotDataset v3、ACT checkpoint、model card 和 training command，生成 lineage。
3. 0:55-1:25：选择 RB3/QCS6490 和 QCS8550 target，运行 ONNX-QNN、LiteRT-QNN、CPU fallback 路线对比。
4. 1:25-1:55：RobotAppLayer 执行本地感知、pick/place/verify/log，明确 cloud not in control loop。
5. 1:55-2:20：SafetyOps 注入 latency miss、wrong sample 或 unsafe raw command，系统 pause/deny 并记录 incident。
6. 2:20-2:45：展示 winner route、p99、thermal throttle、cloud_calls、fallback status、ship_score 和 release gate。
7. 2:45-3:00：导出 `judge-audit-pack.zip`，一键进入 SkillDock certification 和 EdgeFleet canary。

Fallback：

- 如果全策略 QNN 失败，拆成 NPU vision + CPU policy fallback，并诚实标注 fallback。
- 如果板卡晚到，用 AI Hub device-cloud/proxy 并列迁移清单。
- 如果 ACT policy 不稳，demo local perception + planner + motion primitives，同时把 ACT artifact 标为 candidate。
- 如果 live robot 失败，跑一个安全物理子任务，并用同 hash/timecode 的预录 one-take board run 补证据。

Ask：

- RB3/QCS6490 或 QCS8550 target。
- AI Hub / QAIRT / QNN office hours。
- QRB ROS / QIR guidance。
- 允许提交 QNN profiling artifacts。
- IQ10 RRD roadmap review。
- 3 个 Qualcomm 生态设计客户。
- 6 个月 EdgeRuntimeBench pilot：20 个 hosted/device targets，50 张应用级 evidence cards，2026-11 前公开 demo。

## Sources

- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm AI Hub FAQ：https://workbench.aihub.qualcomm.com/docs/hub/faq.html
- Qualcomm AI Hub get started：https://aihub.qualcomm.com/get-started
- Qualcomm Dragonwing developer ecosystem：https://www.qualcomm.com/developer/blog/2026/05/edge-ai-prototype-deployment-qualcomm-dragonwing-developer-ecosystem
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm QCS6490：https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490
- Qualcomm QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Qualcomm IoT / Dragonwing：https://www.qualcomm.com/internet-of-things
- Qualcomm Modular acquisition：https://www.qualcomm.com/news/releases/2026/06/qualcomm-to-acquire-modular
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- LiteRT Qualcomm QNN：https://developers.google.com/edge/litert/next/qualcomm
- ExecuTorch Qualcomm：https://docs.pytorch.org/executorch/stable/backends-qualcomm.html
- Edge Impulse deployment：https://docs.edgeimpulse.com/studio/projects/deployment
- LeRobot v0.6.0 blog：https://huggingface.co/blog/lerobot-release-v060
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot ACT：https://huggingface.co/docs/lerobot/en/act
- LeRobot rollout：https://huggingface.co/docs/lerobot/main/inference
- LeRobot RTC：https://huggingface.co/docs/lerobot/rtc
- SmolVLA：https://huggingface.co/docs/lerobot/smolvla
- Hugging Face model cards：https://huggingface.co/docs/hub/en/model-cards
- MLPerf Edge：https://mlcommons.org/benchmarks/inference-edge/
- EEMBC MLMark：https://www.eembc.org/mlmark/
- Roboflow Deployment Manager：https://docs.roboflow.com/deploy/device-manager
- Ultralytics Benchmark：https://docs.ultralytics.com/modes/benchmark
- AWS IoT Greengrass：https://aws.amazon.com/greengrass/
- Viam Fleet Management：https://www.viam.com/platform/fleet-management
- Peridio AI-ready：https://www.peridio.com/ai-ready
- Edge AI market：https://www.fortunebusinessinsights.com/edge-ai-market-107023
- Edge AI hardware market：https://www.fortunebusinessinsights.com/edge-ai-hardware-market-115540
- AI in Robotics market：https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-robotics-market-report
- EU AI Act：https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- NIST AI RMF：https://www.nist.gov/itl/ai-risk-management-framework
- NIST SSDF：https://csrc.nist.gov/pubs/sp/800/218/final
- SLSA：https://slsa.dev/spec/v1.2/
- CISA SBOM：https://www.cisa.gov/sbom
- CISA VEX：https://www.cisa.gov/sites/default/files/2023-04/minimum-requirements-for-vex-508c.pdf
- TUF specification：https://theupdateframework.github.io/specification/latest/
