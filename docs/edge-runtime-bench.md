# EdgeRuntimeBench Pitch

更新时间：2026-07-06。

## One-Line Thesis

EdgeRuntimeBench 是 physical AI 的运行时证据层：把机器人策略从“能跑”变成“有证据地跑在 Qualcomm 边缘设备上”。

它为每个 LeRobot / ACT / SmolVLA 策略生成可复现证据包：

- lineage。
- compile。
- profile。
- fallback。
- runtime。
- SafetyOps gate。
- deploy。
- rollback。

## 01 · Problem

机器人 demo 能跑，不代表企业敢买、集成商敢交付、评委相信用了高通。

真正的问题：

- 模型可能静默 fallback 到 CPU。
- 模型延迟不等于机器人端到端动作延迟。
- INT8 / FP16 / static shape / unsupported op 可能改变策略行为。
- 相机替换、firmware 更新、热降频、site lighting、ROS pipeline 都会影响结果。
- dataset revision、checkpoint、camera config、normalization stats 和 action schema 如果没锁定，策略不可追溯。
- 买家、SI、保险、marketplace 和评委需要同一份 evidence pack，而不是各看一堆脚本和截图。

## 02 · Current Alternatives Fail

EdgeRuntimeBench 不替代 Qualcomm AI Hub、QAIRT/QNN、ONNX Runtime、Foxglove、Formant、InOrbit 或测试认证。它把这些结果组织成面向机器人策略发布和商业验收的 evidence graph。

- Qualcomm AI Hub：能 compile、profile、run inference，但更像模型工作台；不覆盖 ROS pipeline、机器人动作、长时运行和部署审计。
- QAIRT / QNN scripts：能生成 context binary、CSV、QHAS/optrace，但证据分散在命令、bin、log 和 wrapper 里。
- ONNX Runtime QNN：能接 QNN backend，但团队仍要证明 provider options、context cache、profiling、fallback 和 unsupported ops。
- MLOps/eval tools：擅长软件模型追踪和云端 eval；对 device power、thermal、firmware、ROS/PLC/CAN、FAT/SAT 和安全记录较弱。
- MLPerf / MLMark：适合标准芯片/模型比较；不是客户项目、机器人 workload、site acceptance 或 marketplace 上架证据。
- Fleet ops：Foxglove、Formant、InOrbit 能运营 fleet，但不是独立证明每个模型/runtime 更新能安全部署的报告层。

## 03 · Solution

EdgeRuntimeBench 接收 LeRobot policy、ONNX、QNN artifact 或已部署包，锁定 lineage，运行 export matrix、replay parity、edge profile、live loop、soak test 和 rollback trial，最后输出 buyer-facing Evidence Pack。

核心流程：

1. `Lineage`：锁定 dataset repo、policy revision、LeRobot version、checkpoint、camera config、FPS、task prompt、normalization。
2. `Compile`：AI Hub / QAIRT / QNN / ONNX Runtime QNN 生成 context binary、precompiled QNN ONNX，或标记 unsupported。
3. `Benchmark`：model microbench、pipeline replay、live edge loop、soak、rollback trial，分开标记 measured/proxy/simulated。
4. `Gate`：SafetyOps 根据 p95 latency、deadline miss、frame age、jitter、memory、thermal、fallback 和 ODD 决定能否发布。
5. `Pack`：生成 `judge-audit-pack.zip`、SkillDock bundle、RobotAppLayer adapter、rollback record 和 video proof index。

## 04 · Why Now

- 工业机器人已经大规模部署。
- edge AI 软硬件支出继续增长。
- LeRobot 让 robot policy lineage、dataset、rollout、HIL 和 policy card 进入更多团队。
- AI Act、ISO 10218、ISO 3691-4、保险、RFP、marketplace 和 SkillDock 上架都会要求更多技术文档、日志、准确性、鲁棒性、网络安全和 post-market monitoring 证据。
- AI Hub、QAIRT/QNN、ONNX Runtime QNN 和 Qualcomm Plugin EP 正在形成 Qualcomm runtime 入口。

## 05 · Product

EdgeRuntimeBench 把一个 policy package 分成明确状态：

- `Ready`
- `Needs Quantization`
- `Unsupported`
- `Runtime Risk`
- `Blocked by SafetyOps`

每个判断都能追到原始 artifact。

产品模块：

- `Lineage Graph`：dataset -> train config -> checkpoint -> policy card -> export candidate -> eval -> edge package -> HIL feedback。
- `Contract Inspector`：检查 camera names、image size、FPS、state/action shape、task prompt、control mode、normalization stats。
- `Export Matrix`：PyTorch native、ONNX、ONNX+QNN、ONNX+TensorRT、native RTC，标记 supported / experimental / blocked。
- `Replay Parity`：用 held-out LeRobot episode 比较 PyTorch vs export 的 action chunks、drift、latency 和 queue gaps。
- `Live Edge Loop`：camera -> preprocess -> inference -> postprocess -> action commit -> actuator ack 的端到端 trace。
- `Evidence Pack`：device registry、policy manifest、Qualcomm export manifest、edge profile、install audit、SafetyOps gate、rollback。

## 06 · Product API Objects

所有指标都标注来源：

- `measured-on-board`
- `AI-Hub-device-cloud`
- `proxy`
- `replay-eval`
- `simulated`

关键对象：

- `sut_manifest`：board、SoC、OS、kernel、firmware、runtime、ORT/QNN version、model hash、dataset hash、container digest。
- `cycle_events`：capture、preprocess、inference、postprocess、action commit、actuator ack、deadline、safety state、backend used。
- `profile_summary`：latency p50/p95/p99、action rate、control FPS、jitter、deadline miss、frame age、memory、thermal、power。
- `qnn_backend_report`：HTP/GPU/CPU backend、fallback、unsupported ops、context cache、QNN profile CSV、optrace/QHAS links。
- `release_gate`：ODD、permissions、thresholds、SafetyOps decision、fail reasons、rollback pointer、previous-known-good。
- `video_proof_index`：把三分钟视频时间码映射到 model hash、device log、profile chart、incident 和 rollback artifact。

## 07 · Market & Business Model

证据在钱发生的地方收费：

- procurement。
- certification readiness。
- acceptance testing。
- insurance。
- marketplace listing。
- model/runtime renewal。

买家：

- Robot OEMs：赢 RFP、证明 SKU claims、支持出口和降低售前摩擦。
- System integrators：FAT/SAT acceptance、里程碑付款证明、减少争议。
- Enterprises/factories：供应商选择、uptime risk、EHS/compliance、audit trail。
- Regulated labs/factories：EU AI Act、ISO 10218、ISO 3691-4、功能安全 evidence。
- Insurers：underwriting 和 performance-risk pricing。
- Marketplace operators：trust badge、seller evidence API。

定价假设：

- Developer runner：free 到 ¥1,999/月，或 free 到 $299/月。
- OEM SKU evidence pack：¥29,800-98,000/campaign，或 $7,500-25,000/campaign。
- SI FAT/SAT project pack：¥80,000-300,000/project，或 $20,000-75,000/project。
- Enterprise site license：¥180,000-800,000/site/year，或 $60,000-250,000/site/year。
- Continuous device monitoring：¥50-200/device/month，或 $20-100/device/month。
- Marketplace evidence badge：¥10,000-50,000/listing/year，或 $2,500-15,000/listing/year。

## 08 · Competition & Moat

壁垒不是 benchmark 脚本，而是跨硬件、模型、现场和结果的证据图。

威胁：

- MLCommons / EEMBC 扩展到 audit-style edge evidence。
- Foxglove / Formant / InOrbit 加认证工作流。
- NVIDIA / Qualcomm 增加 trust badges。
- 测试实验室数字化 evidence capture。

壁垒：

- Evidence graph：hardware、firmware、runtime、model、dataset、sensor、environment、power、thermal、robot workload 和 outcome 绑定。
- Raw artifacts：profile CSV、QNN log、optrace、rosbag、JSONL、hash、manifest 和复现命令。
- Robot connectors：ROS、RobotAppLayer、SafetyOps、SkillDock、PLC/CAN/OPC、camera pipeline 和 fleet logs。
- Acceptance language：进入 RFP、FAT/SAT、marketplace、保险和客户验收模板后形成路径依赖。
- Partner loop：OEM、SI、企业、保险、测试机构和生态平台共同定义可信阈值。
- Update history：每次模型、firmware、runtime、camera、site 条件变化都要求 refresh evidence。

## 09 · Why Qualcomm

EdgeRuntimeBench 把“用了 Qualcomm”变成比赛和商业都能检查的证据链。

Qualcomm-specific 路线：

- RB3 Gen 2 / QCS6490：2026 年 7 月最现实的比赛 MVP target，能做板端/AI Hub proxy evidence。
- QCS8550：高性能扩展 target，可展示多相机、多模型和更高 edge AI workload。
- IQ10 RRD：作为 roadmap / early access ask，不能在 2026-07-06 写成已量产可用。
- AI Hub / QAIRT / QNN / ONNX Runtime QNN：生成 compile、profile、backend、context cache、fallback 和 latency evidence。
- QIR / QRB ROS：把 QNN 推理接入 ROS camera/inference nodes，并记录 topic timing 和 pipeline delay。

主张边界：

- 不替代 Qualcomm AI Hub、QAIRT/QNN 或 ONNX Runtime。
- 不声称改进 Qualcomm 编译器或 NPU 性能。
- 只证明在指定设备、指定 runtime、指定模型和输入条件下的结果。
- 安全、功能安全、运动控制确定性不能只靠模型 profile 证明，需要系统级验证。

## 10 · Demo & Ask

比赛叙事：

> LabForgePilot creates the real robot task. EdgeRuntimeBench proves the trained policy was compiled/profiled/deployed against a Qualcomm target. SafetyOps decides whether that exact policy may move the robot.

3 分钟视频：

1. 0:12：硬件亮相：LabForgePilot bench、Qualcomm target board、camera、robot、E-stop、OS/runtime terminal。
2. 0:55：一镜到底执行：本地感知、pick/place/verify/log，明确标注 cloud not in control loop。
3. 1:30：EdgeRuntimeBench dashboard：policy hash、QNN/ONNX status、p95 latency、action rate、runtime path。
4. 1:55：扰动：错样本、keepout、latency miss 或 unsafe raw command；SafetyOps pause/deny 并记录 incident。
5. 2:45：导出 `judge-audit-pack.zip`：dataset -> policy -> Qualcomm profile -> SafetyOps gate -> LabForge log。

Fallback：

- 如果全策略 QNN 失败，拆成 NPU vision + CPU policy fallback。
- 如果板卡晚到，用 AI Hub device-cloud/proxy 并标注迁移清单。
- 如果 ACT policy 不稳，demo local perception + planner + motion primitives，同时把 ACT artifact 标为 candidate。
- 如果 live robot 失败，跑一个安全物理子任务，并用同 hash/timecode 的预录 one-take board run 补证据。

Artifacts：

- `device-registry.json`
- `policy-artifact-manifest.json`
- `qualcomm-export-manifest.json`
- `edge-profile.qualcomm.json`
- `deploy-manifest.yaml`
- `install-audit-log.jsonl`
- `safetyops-release-gate.json`
- `incident-ledger.jsonl`
- `rollback-record.json`
- `video-proof-index.md`

Ask：

- RB3/QCS6490 或 QCS8550 target。
- AI Hub/QNN office hours。
- QIR/ROS guidance。
- 允许提交 QNN profiling artifacts。
- IQ10 RRD roadmap review。

## Sources

- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- AI Hub compile examples：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- AI Hub profile examples：https://workbench.aihub.qualcomm.com/docs/hub/profile_examples.html
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- ONNX Runtime Plugin EP：https://onnxruntime.ai/docs/execution-providers/plugin-ep-libraries/
- onnxruntime-qnn：https://github.com/onnxruntime/onnxruntime-qnn
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm Robotics ROS：https://www.qualcomm.com/developer/project/robotics-ros
- QRB ROS NN inference：https://github.com/qualcomm-qrb-ros/qrb_ros_nn_inference
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot rollout：https://huggingface.co/docs/lerobot/main/inference
- MLPerf Edge：https://mlcommons.org/benchmarks/inference-edge/
- EEMBC MLMark：https://www.eembc.org/mlmark/
- RobotPerf：https://github.com/robotperf/benchmarks
- EU AI Act Article 11：https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-11
- EU AI Act Article 72：https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72
