# LabForgePilot Pitch

更新时间：2026-07-06。

## One-Line Thesis

LabForgePilot 是 RobotMac 平台的第一个商业楔子：一个桌面样品转移工作站，把 Qualcomm 边缘 AI、LeRobot 数据/策略训练、RobotAppLayer 可安装应用、OpsConnector 写回和 SafetyOps 证据链，压缩进实验台上能购买的产品。

一句话：

> 把样本转移这件小事，变成可训练、可审计、可写回系统的桌面机器人工作站。

## 01 · Problem

实验室最贵的浪费，不是一次拿放，而是样本记录和物理动作断裂。

- 中小型研发、QC、诊断和转化实验室里，大量样本转移仍靠人手、条码枪、Excel、LIMS/ELN 补录和事后复核。
- 真正成本是慢、不一致、错样、漏扫、夜间等待、失败原因丢失，以及无法证明谁在何时把哪个样本转到了哪里。
- 夹取失败、孔位偏移、遮挡、错样和人工接管通常被当场修掉，没有进入训练集。
- 低成本机械臂越来越便宜，但缺少夹具、样品模板、数据采集、应用、日志、培训和维护体系。

## 02 · Current Alternatives Fail

LabForgePilot 不和 Hamilton、Tecan、Beckman、Opentrons 正面争“液体处理精度”。它从更窄的样本物流、扫码、视觉核对、失败学习和边缘证据切入。

- 人工 + Excel：便宜但不可复制；GxP 或客户审计下，很难证明样本链路、操作者、失败和修正动作。
- Opentrons Flex：开放、低价、适合自动移液；视觉、失败学习、LeRobot 数据、LIMS 证据链仍需要用户自己拼。
- Automata / Biosero / Cellario：跨设备编排和整实验室调度很强，但部署、销售和集成较重，更适合成熟自动化团队。
- Hamilton / Tecan / Beckman：高可靠液体处理和条码/LIMS 能力成熟；不是围绕低成本机器人、失败回流和 edge AI 数据闭环设计。
- myCobot / Dobot / xArm / SO-101：硬件商品化证明成本下降，但客户买到的是手臂，不是可购买、可培训、可维护的实验台工作站。
- 大型 SI 项目：能做非标交付，但每个项目重新设计夹具、软件、记录、培训和维护，难以沉淀成商品。

## 03 · Solution

桌面 sample-transfer workcell：

1. 扫条码识别源样本与目标孔位。
2. 机器人执行转移。
3. 摄像头捕捉关键动作。
4. 失败自动标注。
5. 生成可训练的 LeRobot / ACT 数据集。
6. 边缘端部署视觉和策略包。
7. 成功、失败、异常、操作者确认写回 Benchling/LIMS 或审计包。

第一版只做三件高频事：

- tube-to-plate。
- plate-to-plate。
- plate-to-tube。

每次动作都绑定：

- sample ID。
- source / destination。
- operator。
- timestamp。
- vision snapshot。
- robot trajectory。
- failure class。
- LIMS writeback status。

## 04 · Why Now

- 实验室自动化市场已经有预算，很多小批量、多变化流程仍缺低门槛自动化入口。
- LeRobot / ACT / SO-101 把机器人采集和模仿学习门槛拉低。
- LeRobot v3 数据以 Parquet 低维状态/动作、MP4 多相机视频、JSON/Parquet 元数据组织，适合清晰展示数据闭环。
- ACT 是 LeRobot 推荐的新手 baseline，适合用约 50 demos 起步。
- HIL / DAgger、`lerobot-rollout`、failure clip 和 replay 让“失败也有价值”变成可演示能力。
- Qualcomm AI Hub / QNN / RB3 Gen 2 提供可展示的本地 edge AI 路线。

## 05 · Product

核心应用：

- `TubeRackTransfer`
- `PlateStaging`
- `BarcodeVerify`
- `QCPhoto`
- `LoadUnload`
- `FailureMining`

核心模块：

- 低成本桌面机械臂 / SO-101 风格 follower arm。
- leader arm 或 teleop station。
- front + top/side camera。
- 固定托盘、管架、孔板、样本盒、灯箱、AprilTag/ArUco/颜色标记。
- LeRobot v3 dataset collector。
- ACT baseline trainer。
- HIL correction queue。
- Qualcomm edge profile viewer。
- LIMS/Benchling mock writeback。
- Safety boundary 和急停。

第一版定位：

- research。
- education。
- QC workflow automation。

不承诺：

- 临床诊断。
- GMP/CLIA/IVD 认证。
- 高精度液体处理替代。

## 06 · Product API Objects

- `Episode`：一次完整尝试，含 reset、teleop、policy、HIL、success/failure、front/top video 和 joint/action parquet。
- `Task`：`transfer_sample_tube_from_rack_to_slot`，带自然语言、sample ID、rack slot、target slot 和 worklist。
- `Variation`：rack 位置、目标槽、光照、管子朝向、背景扰动、遮挡和随机布局。
- `FailureClip`：从 rollout ring buffer 保存失败前后 10-30 秒，标记 miss grasp、wrong slot、drop、collision、timeout。
- `PolicyCard`：ACT/SmolVLA checkpoint、dataset hash、camera config、训练步数、success@20、interventions/min 和 latency。
- `EdgeProfile`：p50/p95 延迟、control FPS、QNN/CPU/GPU path、memory、model hash、device id 和 runtime version。

## 07 · Market & Business Model

第一批买家排序：

1. 高校/职业院校/机器人 AI 课程：买 5-20 台教学/竞赛/实训套件。
2. 科研实验室与共享平台：买 1-3 台 pilot kit，用于管架/孔板/样品盒转移、扫码核对、拍照记录、上机前后 staging。
3. 小型 QC 实验室/轻工厂：食品、材料、电池、化妆品、化学品的小批量质检台。
4. 系统集成商：买 fleet kit 作为可复制机器人应用底座。
5. 机器人/OEM 厂商：后续授权 RobotAppLayer / OpsConnector。

中国版定价假设：

- Edu/Starter Kit：¥29,800-49,800。
- Lab Pilot Kit：¥68,000-98,000。
- Fleet Kit 5-pack：¥298,000-498,000。
- Software：¥599-1,999/机器人/月。
- Training credits：¥500-800/小时，或 ¥10,000 包。
- Support：硬件价 15%-20%/年。

海外版定价假设：

- Pilot Kit：$9,900-$14,900。
- Fleet Kit 5-pack：$39,000-$69,000。
- Software：$199-$499/robot/month。
- Training：$150-$250/hour。
- Support：$2,000-$8,000/year。

定价逻辑：

- 低于 Opentrons Flex 和大型 NGS workstation。
- 明显高于裸机械臂，因为卖的是工作站、应用、培训、日志、部署和运维。

## 08 · Competition & Moat

壁垒不是机械臂，而是实验室样本转移数据资产。

- Labware templates：管架、孔板、样品盒、检测槽、夹具和灯箱模板。
- Failure dataset：每个错夹、掉落、遮挡、错位和人工接管都能训练下一版策略。
- Audit semantics：sample ID、operator、timestamp、source/destination、worklist、image evidence 和 policy version 绑定。
- Robot apps：TubeRackTransfer、PlateStaging、BarcodeVerify、QCPhoto、LoadUnload 可进入 RobotAppLayer / SkillDock。
- Edge evidence：QNN profile、latency、memory、model hash、device ID 和 local runtime logs。
- Channel loop：学校、SI、OEM、科研平台和 QC 实验室共同沉淀课程、模板、应用和维护手册。

## 09 · Why Qualcomm

比赛必须证明：这不是云端遥控，而是可量化的实验台边缘部署。

边缘架构：

1. `Sensing`：RB3 Gen 2 Vision Kit 的 CSI 摄像头、可选 USB camera、IMU/压力/磁力传感器；样本架可加 AprilTag/ArUco/颜色标记降低风险。
2. `Camera Pipeline`：Qualcomm Linux / Ubuntu / GStreamer 接入 camera stream，把帧送入视觉模型。
3. `Vision Models`：检测试管、孔位、tip、液面/颜色、夹爪或移液器末端，输出 rack pose、well id、confidence 和 occlusion。
4. `Sample-transfer Policy`：小型 ONNX policy 或规则+学习混合策略生成动作候选；安全边界、限位和碰撞停止由确定性控制器执行。
5. `Evidence Runtime`：记录视频帧 hash、模型 hash、QNN/QAIRT version、device id、latency、NPU/CPU fallback、成功/失败原因和动作时间线。

谨慎表述：

- RB3 Gen 2 / QCS6490 是比赛 MVP edge target。
- QCS8550 是高性能扩展 profile。
- IQ10 RRD 只写 roadmap / early access ask；截至 2026-07-06 不写成已量产或已集成硬件。
- 如果 AI Hub 使用 `QCS6490 (Proxy)`，标注为 proxy/device-cloud profile。
- 如果模型有 CPU fallback，单独报告；只有禁用 fallback 且成功运行后，才写 full NPU path。

## 10 · Demo & Ask

3 分钟视频：

1. 0:00-0:10：人工实验台混乱、手工记录和错样风险。
2. 0:10-0:30：LabForgePilot 实物和工作站。
3. 0:30-0:55：SOP、视觉、计划、策略、校验、日志架构。
4. 0:55-1:35：完整任务一镜到底：抓取、放置、检测、记录。
5. 1:35-1:55：扰动恢复：移动物体，系统重新定位或安全停机。
6. 1:55-2:15：Qualcomm 特写：板卡、端侧推理指标、断网运行、延迟数字。
7. 2:15-2:35：非脚本证明：三个随机布局、两个任务模板、运行成功率。
8. 2:35-3:00：商业场景和路线图。

7 分钟现场 demo：

1. 一句话问题 + 实物台面亮相。
2. 输入新任务：找到 A 样本，转移到检测位，拍照确认并记录。
3. 场景感知：物体识别、位姿、置信度、风险区域。
4. 自动生成计划：observe -> pick -> place -> verify -> log。
5. 执行动作：至少 3 个连续动作，并显示实时状态。
6. 人为扰动：移动样本或放入错误物体，系统重新识别、暂停、重规划或拒绝错误动作。
7. Qualcomm 证明：断网运行、本地推理延迟、CPU/NPU/GPU 占用、功耗/温度。
8. 输出实验日志：时间戳、图像证据、动作轨迹、异常记录。

Fallback：

- Green：真实策略可跑，展示闭环策略和扰动恢复。
- Yellow：策略不稳，改成学习感知 + 规划器 + 运动原语。
- Red：真实机器人不稳，展示仿真策略 + 真实台面感知 + 机械臂执行一个安全子任务。
- 最低可交付：端侧识别、任务规划、动作日志、一个物理动作成功，不能退化成纯视频或纯网页。

Ask：

- RB3 Gen 2 Vision/Core Kit。
- QCS8550 profile target。
- IQ10 RRD roadmap 评审。
- AI Hub/QNN office hours。
- 允许提交 QNN profiling artifacts。
- 10 个付费试点：4 个科研/平台实验室，3 个高校/职业院校 fleet，2 个系统集成商，1 个机械臂/OEM 伙伴。

## Sources

- Competition page：https://qc-robotics-dev.aidlux.com/2026/
- LeRobot：https://github.com/huggingface/lerobot
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot ACT：https://huggingface.co/docs/lerobot/en/act
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
- LeRobot SO-101：https://huggingface.co/docs/lerobot/en/so101
- Opentrons Flex：https://opentrons.com/robots/flex
- Automata LINQ：https://www.automata.tech/linq
- Biosero GBG：https://biosero.com/products/green-button-go-orchestrator/
- HighRes Cellario：https://www.highres.com/lab-orchestration
- Benchling LIMS：https://www.benchling.com/lims-software
- 21 CFR Part 11：https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm QCS6490：https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490
- Qualcomm QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
