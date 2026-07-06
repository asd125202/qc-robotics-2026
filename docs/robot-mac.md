# RobotMac Core Pitch

更新时间：2026-07-06。

所有硬件、电源、热、性能、QNN/QAIRT 路径、camera、I/O 和安全相关表述都必须在最终开发板、SDK、散热、电源、执行器和传感器组合上重新验证。

## One-Line Thesis

RobotMac Core 是装进商业机器人身体里的“机器人电脑”：把 Qualcomm edge AI、12-24V robot power、camera/robot I/O、安全边界、ROS 2 runtime、LeRobot data loop、AI Hub/QNN deployment、fleet telemetry、signed OTA 和 rollback 打包成一个可购买的 robot compute appliance。

关键判断：

> Robots are no longer scarce. Deployment engineers are scarce.

## 01 · Problem

机器人团队不缺开发板，缺的是能从 demo 走到现场部署的产品底座。

开发板解决“能跑”，不解决“能卖、能维护、能扩张”。每个团队仍要重复处理：

- 12/24V power、brownout、reverse polarity、motor/logic rail isolation、E-stop、watchdog、thermal。
- cameras、USB、Ethernet、CAN/CAN-FD、UART、PWM、GPIO、IMU、LiDAR、ToF、time sync。
- ROS 2 lifecycle、drivers、DDS QoS、SROS2 security、logs、device identity、local safety state。
- LeRobot episode capture、cloud training、ONNX/QNN/QAIRT、policy package、runtime profile、rollback。
- signed OTA、SBOM、audit trail、remote diagnostics、fleet update、field recovery、enterprise IT review。

买方真正担心的不是“机器人能不能动”，而是版本不可追溯、更新不可恢复、安全边界不清、现场没人能修、5-100 台 fleet 没人能维护。

## 02 · Current Alternatives Fail

现有方案都重要，但没有把机器人从 prototype 带到 fieldable product。

- SBC / dev kit：RB3、Q6A、Jetson、Raspberry Pi 类产品适合原型和开发，但团队仍要做 enclosure、power、camera、safety I/O、OTA、rollback、fleet ops。
- ROS 2：事实标准中间件，但不是产品。install drift、driver quality、networking、security、observability 和 update discipline 仍然难。
- Viam / Formant / Foxglove / InOrbit：强在 RobOps、fleet、telemetry、visualization，但通常假设一台可靠 robot computer 已经存在。
- Balena / Mender / Ubuntu Core / Yocto：强在 IoT OS 和 OTA，但不理解 robot action space、ROS graph health、sensor timing、safety gate 和 autonomy rollback。
- Unitree / AgileX / Husarion / Clearpath：整机或 chassis 强，但每个 robot body 都有自己的 compute/runtime 差异。
- PLC / industrial controllers：确定性控制和 safety 强，但不是围绕 LeRobot/VLA/AI Hub/cloud training loop 设计的 AI autonomy appliance。

RobotMac Core 不替代这些层。它把这些能力组织成一个 robot-native deployment appliance。

## 03 · Solution

RobotMac Core 是 dev kit 和全定制 electronics 之间的 robot compute box。

> RobotMac Core = Qualcomm compute + robot-native power + camera/I/O carrier + safety supervisor boundary + RobotCoreOS + LeRobot/AI Hub bridge + fleet runtime + release evidence.

它的承诺不是 raw TOPS，而是减少从 prototype 到 field fleet 的集成时间和现场失败：

1. `Known-good hardware`：12-24V input、brownout handling、camera carrier、CAN-FD、USB3、2.5GbE、M.2、debug/service port。
2. `RobotCoreOS`：Ubuntu/Yocto base、ROS 2 LTS、lifecycle services、device identity、signed A/B OTA、rollback。
3. `AI edge path`：LeRobot -> ONNX -> AI Hub compile/profile/validate -> QNN/QAIRT or ONNX Runtime QNN where verified。
4. `Safety boundary`：Linux/ROS/AI 不作为 certified safety controller；E-stop、watchdog、motor enable、safe state 走独立边界。
5. `Fleet evidence`：OpenTelemetry、ROS diagnostics、MCAP/logs、runtime manifest、SBOM、episode capture、incident ledger。
6. `Pilot handoff`：EdgeRuntimeBench、SafetyOps 和 PilotContractKit 直接生成客户验收材料。

## 04 · Why Now

机器人供给变多，部署工程师变少。

- IFR 报告 2024 年全球工业机器人新增约 542,000 台，运行存量约 4.66M 台。
- 中国 2024 年新增约 295,000 台工业机器人，约占全球 54%，国产供应商份额继续上升。
- 2024 年专业服务机器人销量超过 199,000 台，logistics、cleaning、medical 和 RaaS 都在增长。
- ROS 2、LeRobot、AI Hub、QNN/QAIRT、ONNX Runtime、OTA 工具和 robot fleet tools 已经成熟到可以被产品化。
- NVIDIA、Intel、Qualcomm、Canonical、Viam、Formant、Foxglove 等都在验证“edge AI + ROS + fleet + lifecycle”方向。
- 企业和 SI 的瓶颈不是买不到机器人，而是 power、camera、I/O、security、updates、logs、SLA 和现场支持拼不起来。

现在需要一个 Qualcomm-first 的 robot appliance，把低功耗 edge AI、多摄像头、连接、端侧隐私和 prototype-to-production tooling 压成可交付产品。

## 05 · Product

RobotMac Core 的产品体验应该像 appliance 开箱，而不是工程板 bring-up。

产品模块：

- `Core S`：QCS6490-class，12 TOPS，8-16GB RAM，128GB storage，12-24V input，2.5GbE，CAN-FD，USB3，M.2，2-3 validated cameras。
- `Core Vision`：Core S + CSI/GMSL camera carrier、sync trigger、IMU、calibrated camera bundle、vision dataset templates。
- `Core Pro`：QCS8550-class，48 INT8 TOPS target，16GB RAM，128/256GB storage，4-6 cameras，Wi-Fi 7，higher thermal envelope。
- `Core Dev`：RB3/Q6A/Rhino/VENTUNO-compatible SDK image 和 harness，只卖开发，不假装是量产 appliance。
- `Core Max`：IQ10-based roadmap/reference design exploration，不在 2026 年 7 月写成近期开售 SKU。

软件/运行层：

- Base OS：Ubuntu/Yocto、secure boot、signed A/B rootfs、watchdog mark-good、immutable runtime partitions。
- ROS runtime：ROS 2 LTS、lifecycle nodes、DDS QoS profiles、SROS2/DDS-Security、driver health。
- AI runtime：LeRobot data、ONNX interchange、AI Hub compile/profile/validate、QAIRT/QNN/ONNX Runtime QNN where verified。
- Fleet runtime：hardware-bound identity、mTLS、device twin、OpenTelemetry、ROS diagnostics、selective bag/video upload。
- Update runtime：signed OTA bundles、phased rollout、canary cohorts、rollback、separate model/map/app artifacts。

## 06 · Evidence Objects

RobotMac Core 要让客户买到的不是盒子，而是可验收的 robot runtime slot。

- `robotmac-board-profile.json`：SoC、board、carrier、OS、kernel、BSP、camera stack、runtime versions、image digest。
- `power-io-manifest.yaml`：12/24V rails、motor/logic isolation、E-stop、watchdog、CAN/UART/GPIO/PWM、camera topology。
- `runtime-slot.manifest`：ROS graph、LeRobot dataset schema、policy hash、model runtime、permissions、safety envelope。
- `edge-profile.qualcomm.json`：AI Hub/QNN/QAIRT/ONNX path、latency p50/p95、memory、temperature、power、fallback labels。
- `fleet-identity.sbom`：device identity、cert chain、SBOM、container/image digest、CVE review status。
- `ota-rollback-record.json`：bundle signature、cohort、install result、mark-good、rollback pointer、previous-known-good。
- `episode-ledger.mcap`：camera frames、state/action、operator takeover、failure clip、safety event、dataset lineage。
- `pilot-audit-pack.zip`：BoardBringupKit + EdgeRuntimeBench + SafetyOps + PilotContractKit evidence bundle。

Metric labels：

- `validated-on-board`
- `AI-Hub-device-cloud`
- `proxy`
- `simulated`
- `product-target`
- `future-profile`

## 07 · Market & Business Model

RobotMac Core 不按 Raspberry Pi 或 cheap SBC 定价。它按“避免几个月集成和一次现场失败”定价。

第一批买家：

- 中国 robot OEM：AMR、service robot、lab automation、industrial inspection、清洁、教育、具身智能创业公司。
- 系统集成商：需要可重复交付的 robot core、harness、runtime、logs、remote support 和 acceptance pack。
- 海外 robotics startup / SI：需要更强 security、lifecycle、documentation、support、cert-readiness 和 long-term supply story。
- RaaS/fleet operator：需要 staged OTA、remote diagnostics、incident replay、SLA evidence、field recovery。
- 教育/比赛/开发者：需要 day-one working、classroom reset、safe I/O、LeRobot-to-edge curriculum。

收入结构：

- Hardware margin：Core S / Vision / Pro / Industrial kit。
- Per-device runtime license：signed image、hardware profile、SBOM、runtime manifest、rollback channel。
- Fleet plan：robot/month，覆盖 telemetry、OTA stages、model/skill deployment、logs、diagnostics、episode capture。
- Cloud training add-on：TrainRouter/CloudTwin 按项目、训练任务、团队席位或 GPU pass-through 加服务费。
- Integration / certification-readiness：custom carrier、camera tuning、safety validation support、private registry、regulated evidence。
- Certified robot packs：Unitree、AgileX、Husarion、Clearpath、UR arms、LiDAR、depth camera、电池、传感器组合。

定价 pitch anchor：

- Core S dev/education：$799-$1,499 or ¥4,999-12,999。
- Core Pro pilot kit：$2,499-$5,999 or ¥19,800-49,800。
- Industrial / Vision pack：$7,500-$25,000 or ¥60,000-200,000。
- Runtime/fleet：$20-$200 per robot/month or ¥50-800 per robot/month。
- 90-day pilot pack：$50k-$250k or ¥30万-150万，含 3-5 台 Core、2 个技能、fleet evidence 和 support。

## 08 · Competition & Moat

不要打“谁的板子更便宜”，要打“谁能把机器人变成可交付产品”。

竞争地图：

- NVIDIA Jetson / Isaac：强 GPU 和 robotics 软件生态。RobotMac 不打 TOPS 战，强调 Qualcomm-first、低功耗 connected edge、camera-rich I/O、power/safety/runtime。
- ROS / ROS-Industrial：事实标准中间件。RobotMac 把 ROS 放进可采购、可维护、可回滚、可审计的产品边界。
- Viam / Formant / Foxglove / InOrbit：强 fleet/data/ops。RobotMac 是它们可以运行或接入的 trusted edge substrate。
- Balena / Mender / Ubuntu Core / Yocto：强 OTA/OS/IoT。RobotMac 增加 robot action space、LeRobot lineage、safety gate、runtime evidence。
- Unitree / AgileX / Husarion / Clearpath：强 robot bodies。RobotMac 提供跨 chassis 的 common core。
- PLC / industrial controllers：强 deterministic control 和 safety。RobotMac 是旁边的 AI/autonomy appliance，不替代 safety PLC。

护城河：

- `Compatibility matrix`：board + carrier + camera + LiDAR + motor controller + power stack + ROS distro + kernel/BSP。
- `Robot I/O carrier`：proprietary harness、timing、watchdog、recovery、diagnostics、safe-state interface。
- `Certified robot packs`：tested configs for common chassis, arms, cameras, LiDAR, batteries, fieldbus。
- `Fleet failure memory`：OTA failure、driver drift、thermal throttling、sensor mismatch、runtime fallback、incident patterns。
- `Evidence standard`：每个 skill 和 update 都绑定 hardware、runtime、data、safety、rollback 和 acceptance packet。
- `Channel network`：比赛、课程、SI、OEM、Qualcomm ecosystem、developer tutorials 和 reference projects。

## 09 · Why Qualcomm

RobotMac Core 把 Dragonwing 从开发板变成机器人产品核心。

Qualcomm-specific strategy：

- `QCS6490 / Core S`：low-power robotics/AI vision baseline，适合教育、AMR、service robot、smart camera 和 fallback target。
- `QCS8550 / Core Pro`：高性能视觉和多模型边缘 AI target，适合 LabForgePilot、robot arm、multi-camera inspection。
- `RB3 Gen 2`：成熟 dev kit 和 robotics ecosystem reference，可做海外 Core S validation path。
- `Dragon Q6A / Rhino Pi-X1`：比赛和中国开发者生态里的现实 target，用 BoardBringupKit 转成 RobotMac candidate。
- `VENTUNO Q / IQ-8275`：AI + MCU/deterministic control 的 industrial story，但作为 partner-supplied / roadmap target。
- `IQ10 RRD`：enterprise/future Max path，不能写成 2026 年 7 月已量产可用。
- `AI Hub / QNN / QAIRT / Qualcomm Linux / Profiler`：让模型、runtime、latency、memory、thermal、power 和 deployment evidence 进入客户验收。

对 Qualcomm 的价值：

- 从“提供 board”升级为“帮助开发者把 board 变成 robot product core”。
- 给 FAE、Robotics Hub、FIRST/education、SI 和 OEM 一套 reproducible evidence workflow。
- 让 LeRobot/Hugging Face 开源机器人学习和 Qualcomm edge runtime 形成可信桥梁。
- 把低功耗、多摄像头、connected edge、端侧隐私和长生命周期变成可购买产品语言。

## 10 · Demo & Ask

三分钟 demo 证明：RobotMac Core 是 competition-to-production proof harness，不是开发板实验。

Demo flow：

1. 0:00-0:20：展示 RobotMac Core appliance、board profile、image digest、device identity、power/I/O/safety map。
2. 0:20-0:50：BoardBringupKit 过门禁：camera、network、runtime、NPU/AI path、watchdog、E-stop。
3. 0:50-1:25：LeRobot CloudTwin 采集 episode：synced video、state/action、operator takeover、task label。
4. 1:25-2:05：EdgeRuntimeBench 展示 AI Hub/QNN/ONNX status、latency p50/p95、memory、thermal、power、model hash。
5. 2:05-2:35：SafetyOps 触发 stale sensor、confidence drop 或 unsafe zone，RobotMac pause/deny/rollback。
6. 2:35-3:00：PilotContractKit 导出 pilot packet：BOM、setup checklist、dataset policy、safety checklist、benchmark report、ask sheet。

向 Qualcomm 的 ask：

- Hardware：Rhino X1/QCS8550、RB3 Gen 2 Vision Kit、Radxa Q6A、VENTUNO Q 或 future IQ10 RRD validation path。
- AI Hub / Device Cloud credits。
- QNN / QAIRT / ONNX Runtime QNN profiling office hours。
- Qualcomm Linux/BSP guidance：camera、GStreamer、ROS 2、CAN/UART/GPIO、OTA、watchdog。
- Profiler methodology review before public performance claims。
- Permission/path to publish Dragonwing Robotics Hub reference runtime project。
- Intro to APLUX、Radxa、Thundercomm、Lantronix、Arduino、education/FIRST-style partners、robot SI/OEM partners。

## Claim Boundaries

可以说：

- RobotMac Core 是 Qualcomm-first robot compute/power/I/O/runtime appliance concept。
- 目标是降低机器人从 demo 到 deployment 的工程成本。
- 它把 LeRobot data、cloud training、Qualcomm edge deployment、runtime evidence 和 fleet hooks 接到同一产品路径。

不能说：

- 已获 Qualcomm 官方认证、合作、投资或官方背书。
- 已通过 safety certification、SIL、PL、IP rating、functional safety。
- RobotMac 替代 safety PLC / safety controller。
- 开箱支持所有机器人。
- 性能优于 Jetson/x86。
- 任意 PyTorch/VLA/LeRobot policy 都能自动跑到 QNN。
- 云端控制可以替代本地 safety。

所有 TOPS、功耗、延迟、温度、FPS、成功率、加速路径和 rollback time 必须标注日期、开发板、SDK、散热、电源、模型版本和是否模拟。

## Sources

- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- China industrial robots：https://chinapower.csis.org/china-industrial-robots/
- ROS 2 Jazzy LTS：https://www.openrobotics.org/blog/2024/5/ros-jazzy-jalisco-released
- ROS 2 lifecycle：https://design.ros2.org/articles/node_lifecycle.html
- ROS 2 DDS security：https://design.ros2.org/articles/ros2_dds_security.html
- SROS2：https://github.com/ros2/sros2
- LeRobot docs：https://huggingface.co/docs/lerobot/en/index
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB3 Gen 2 product brief：https://docs.qualcomm.com/doc/87-74789-1/87-74789-1_REV_A_Qualcomm_RB3_Gen_2_Development_Kit_Product_Brief.pdf
- Qualcomm QCS8550 product brief：https://docs.qualcomm.com/doc/87-61717-1/87-61717-1_REV_D_Qualcomm_Dragonwing_QCS8550_QCM8550_Processors_Product_Brief.pdf
- Open-Q 8550CS SOM：https://www.lantronix.com/products/open-q-8550cs-som/
- Radxa Dragon Q6A：https://docs.radxa.com/en/dragon/q6a
- Rhino Pi-X1：https://rhinopi.docs.aidlux.com/en/rhino-x1-aidlux/
- Arduino VENTUNO Q：https://www.arduino.cc/product-ventuno-q
- IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm Linux：https://www.qualcomm.com/developer/software/qualcomm-linux
- Qualcomm Profiler：https://www.qualcomm.com/developer/software/qualcomm-profiler
- FoundriesFactory for Qualcomm：https://www.qualcomm.com/developer/software/foundriesfactory
- NVIDIA Isaac ROS：https://developer.nvidia.com/isaac/ros
- Viam Fleet Management：https://www.viam.com/platform/fleet-management
- Formant Fleet Observability：https://docs.formant.io/docs/fleet-observability
- Foxglove：https://foxglove.dev/
- Ubuntu Core：https://ubuntu.com/core
- RAUC：https://rauc.io/
- Mender：https://github.com/mendersoftware/mender
- NIST SSDF：https://csrc.nist.gov/pubs/sp/800/218/final
