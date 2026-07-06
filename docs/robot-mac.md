# RobotMac Core Pitch

更新时间：2026-07-06。所有硬件接口、电源、热、性能、QNN/QAIRT 路径和安全相关表述必须在最终开发板、SDK、散热、电源、执行器和传感器组合上重新验证。

## One-Liner

RobotMac Core 是装进商业机器人身体里的“机器人电脑”：把 Qualcomm 边缘计算、电源、机器人 IO、安全边界、RobotCoreOS、LeRobot 云训练接口和 fleet runtime 打包成一体，让团队直接做机器人应用，而不是从电源板、开发板、驱动、OTA 和现场恢复重新拼起。

## Problem

机器人团队不缺 demo，缺的是可交付底座。

开发板解决“能跑”，不解决“能卖”。每个团队仍要重复处理：

- 电池/外部电源、稳压、逻辑/电机供电隔离、保险丝、急停、过流、低压、散热和状态灯。
- 相机、以太网、USB、CAN、UART、PWM、GPIO、IMU、LiDAR、ToF、音频和传感器同步。
- ROS 2、driver、lifecycle、time sync、日志、设备身份和本地安全状态机。
- LeRobot 数据采集、模型部署、QNN/QAIRT/ONNX runtime、policy package、rollback 和 failure episode。
- OTA、A/B rollback、SBOM、审计、现场恢复、客户归属、远程诊断和企业 IT 问答。

买方真正担心的不是算法不够酷，而是版本不可追溯、更新不可恢复、安全边界不清、现场没人能修、20 台机器没人维护。

## Why Now

- LeRobot 正在把真实机器人数据、模仿学习、数据集和策略训练流程推向标准化。
- RaaS 和多机试点把 uptime、远程诊断、staged OTA、proof-of-work 和 SLA 变成采购问题。
- Qualcomm Dragonwing、AI Hub、QNN/QAIRT、Qualcomm Linux、Device Cloud、Profiler 和 IQ10 Robotics Reference Design 正在形成从 prototype 到 production 的边缘 AI 路径。
- IFR 报告 2024 年工业机器人安装量约 54.2 万台，全球运行存量约 466.4 万台；中国占全球工业机器人安装量过半。
- 专业服务机器人 2024 年销量接近 20 万台，物流机器人和 RaaS 持续增长。

现在缺的是一个 Qualcomm-first 的 robot core appliance，让机器人团队不再从裸板、电源、IO、运行时和云训练接口开始。

## Insight

机器人应用的最小商业单元不是“模型”，也不是“底盘”，而是一个可验证 runtime slot：

- 电源预算。
- IO 拓扑。
- 传感器时序。
- 模型 hash。
- 动作权限。
- 安全边界。
- 运行日志。
- OTA 和 rollback。
- 现场恢复路径。

PC 普及不是因为每个人会装主板；机器人普及也不会靠每个团队重新做电源、驱动和运行时。

## Solution

> RobotMac Core = Qualcomm compute + protected power plane + robot IO plane + safety supervisor + RobotCoreOS + LeRobot / AI Hub deployment bridge + fleet runtime。

它不是另一块 SBC，也不是另一个云 dashboard。它是 Qualcomm-first 的机器人核心，把 edge AI hardware 变成可交付机器人产品：

- compute。
- power。
- IO。
- safety。
- runtime。
- data capture。
- cloud training handoff。
- edge skill deployment。
- fleet hooks。
- release evidence。

## Product Architecture

### Hardware Layers

- Qualcomm edge compute module。
- Power carrier。
- Robot IO carrier。
- Safety IO harness。
- Thermal enclosure。
- Runtime image。
- Policy package layer。

### Power

产品目标是 separate logic / motor rails、fused input、reverse-polarity / overcurrent / brownout monitoring、battery telemetry 和 safe-state handling。最终 voltage range 不能在 carrier 验证前承诺。

### Safety IO

产品目标是 physical e-stop、watchdog、limit / door / bumper inputs、safety-state GPIO、cloud-disconnect safe state。RobotMac Core 不是 certified safety controller，工业风险降低仍需要外部 safety-rated controller 或合规安全架构。

### Interfaces

比赛 baseline：USB、Ethernet、camera。

扩展：UART、I2C、SPI、PWM、GPIO 经 GPIO / MCU adapters。

Industrial / future profile：CAN/CAN-FD、GMSL2、多摄像头、TSN/EtherCAT 或 safety island 依赖具体板卡与 carrier。

### Software

- RobotCoreOS。
- board profile。
- hardware self-test。
- ROS 2 bridge。
- lifecycle-managed services。
- LeRobot data hooks。
- QNN/QAIRT/ONNX policy runner path。
- signed skill package。
- telemetry。
- OTA and rollback。
- runtime manifest。

## SKU Strategy

- Core Lite：教育、开发者、小车、简单机械臂。方向：QCS6490 / Radxa Dragon Q6A。目标价格区间可在 $799-$1,199，教育补贴版可更低。
- Core Pro：比赛主线、服务机器人、桌面机械臂、商业试点。方向：QCS8550 / APLUX Rhino X1。目标价格区间可在 $1,999-$3,499。
- Core Industrial：AMR、人形、工业控制、高端机械臂。方向：IQ-8275 / Arduino VENTUNO Q + STM32H5，或后续 IQ9/IQ10 路线。目标 eval 价可在 $4,999-$9,999，加 NRE。
- Core IQ10 Future：前瞻路线，围绕 IQ10 Robotics Reference Design 的 AMR、humanoid、collaborative robot、sensor-heavy systems 和 functional-safety framing。

以上价格是 pitch anchor，不是正式报价。

## Product Workflow

1. 选择机器人形态：桌面机械臂、移动底盘、巡检车、教学套件或行业夹具。
2. 接入 RobotMac Core：电源、相机、执行器、急停、网络和传感器。
3. 运行硬件自检：camera、IMU、USB、Ethernet、GPIO、UART、PWM、CAN adapter、motor/gripper smoke test。
4. 采集 LeRobot episode：视频、状态、动作、人类示教、接管、成功/失败标签。
5. CloudTwin / TrainRouter 调度中国或海外 GPU，训练 policy 并生成评估报告。
6. AI Hub / QNN / QAIRT / ONNX 路径进行 compile/profile/deploy，产出 signed skill package。
7. 本体本地执行感知、策略、安全检查和控制，云端不进入 safety-critical loop。
8. 导出 runtime evidence：FPS、p50/p95 latency、placement、memory、power、temperature、success rate、safety events。
9. 坏模型、坏配置或传感器异常触发 admission denial、safe mode 或 rollback。
10. 失败 episode 回流到下一轮数据和策略训练。

## Market

第一批买家不是“所有机器人公司”，而是最怕基础集成拖慢商业化的人：

- 机器人 OEM platform lead：需要 reproducible hardware profile、BSP、ROS 2 image、drivers、OTA rollback、telemetry 和 camera/IO validation。
- 机器人 OEM GM / product lead：需要对企业客户证明可以 update、recover、audit、support fleet。
- 系统集成商：需要 known-good core、harness map、ROS package set、remote support 和 repeatable install checklist。
- RaaS / fleet operator：需要 uptime、remote diagnostics、staged OTA、logs、incident replay、teleop hooks 和 SLA evidence。
- Enterprise IT / Security：需要 identity、patching、SBOM、CVE、access control、audit logs 和 lifecycle support。
- 教育 / dev kit buyer：需要 day-one working、classroom reset、sample skills、curriculum 和 safe IO。

## Business Model

- Hardware：Core Lite / Pro / Industrial 分层销售。
- Runtime license：按设备/年收取 signed image、hardware profile、rollback channel、SBOM/exported runtime manifest。
- Fleet plan：按机器人/月收取 telemetry、OTA stages、rollback、logs、diagnostics、model/skill deployment、episode capture。
- Cloud training：按团队、项目或训练任务收费；GPU 成本 pass-through，叠加数据/训练/评估工作流服务费。
- Enterprise integration：board/profile bring-up、custom carrier、safety validation support、private registry、regulated deployment evidence 和长期维护。

买方不是把 RobotMac Core 和 $169 SBC 或 $249 Jetson 直接比较，而是和几个月集成、现场失败、远程支持缺口、定制 OTA、SBOM/security 和企业采购风险比较。

## Go-To-Market

1. 比赛样板：用 Rhino X1/QCS8550 或 RB3/Q6A 跑通采集、训练、部署、运行、故障回流和 runtime manifest。
2. 教育入口：做 Qualcomm robot core starter kit，配课程、示例技能、刷机恢复、课堂安全和 LeRobot-to-edge 教学闭环。
3. 系统集成商模板：把 power/IO/safety/runtime 做成可重复交付包。
4. 90 天试点：给 1 个实验室或 SI 交付 3-5 台 Core、2 个技能、fleet dashboard、rollback demo 和验收报告。
5. 双云销售：中国适配阿里云、腾讯云、华为、AutoDL；海外适配 RunPod、Lambda、Modal、AWS；边缘 runtime 保持一致。

## Competition

- NVIDIA Jetson / Isaac：强 GPU 与 robotics 软件生态。RobotMac 避免 TOPS 战，强调 Qualcomm-first、低功耗 connected edge、power/IO/safety/runtime 和训练闭环。
- ROS 2：事实标准中间件。RobotMac 不替代 ROS，而是把 ROS 放进可采购、可维护、可回滚的产品边界。
- Viam / Formant / InOrbit：强 fleet、telemetry、remote control 和 RobOps。RobotMac 从本体侧 compute、IO、power、runtime、data capture 开始。
- Foxglove：强 multimodal data、MCAP、visualization 和 log search。RobotMac 默认生成干净 sensor/action episodes、runtime metrics、safety events、model versions 和 Qualcomm accelerator placement。
- Mender / Balena / Ubuntu Core / Yocto：强 OTA、OS、IoT 管理。RobotMac 增加机器人动作空间、安全边界、LeRobot lineage、Qualcomm profile 和 runtime manifest。
- Unitree / AgileX / modular robot kits：卖具体机器人本体、移动底盘、机械臂或 ROS-ready 套件。RobotMac 卖跨形态 core，可以接入这些本体。
- Industrial controllers / PLCs：可靠、安全、现场工程强，但不是围绕 LeRobot / VLA / AI Hub / cloud training loop 设计的新型 robot learning core。

## Moat

- Board profile library：Qualcomm board、camera、IO、sensor timing、thermal、power、accelerator path 的验证矩阵。
- Skill compatibility graph：技能包与硬件、ROS graph、模型 runtime、动作权限、安全 envelope、rollback package 的兼容关系。
- Runtime evidence：SBOM、签名、OTA、rollback、latency、thermal、power、episode、incident report。
- Field data flywheel：失败片段、人工接管、传感器漂移、更新事故和现场恢复都会变成下一版 runtime rule。
- Ecosystem wedge：比赛、课程、开发套件、系统集成商和 Qualcomm Dragonwing 伙伴形成复用网络。

## Evidence Matrix

使用 claim label：

- `Validated`：已经在当前 repo / demo / 本地环境验证。
- `Competition target`：比赛阶段要完成并标注模拟/实测。
- `Product target`：产品化阶段目标，不在初赛承诺已完成。
- `Future profile`：依赖未来板卡、reference design 或 partner。
- `Standards reference`：用于论证方向，不等于认证通过。

验收项目：

- Bring-up：boot、network、storage、camera enumeration、USB/Ethernet、GPIO/UART/PWM、CAN adapter、IMU、motor/gripper smoke test。
- Safety：E-stop blocks actuator command path、watchdog restart、thermal/brownout safe state、cloud disconnect safe behavior。
- Runtime：ROS graph active、lifecycle transitions、LeRobot episode export、QNN/QAIRT profile、p50/p95 latency、CPU/GPU/NPU/memory、power、temperature。
- OTA：signed install、failed-update rollback、previous-known-good restore、manifest audit。
- Burn-in：competition target 4-8h soak；product target 24h acceptance plus 72h pilot burn-in。

## Why Qualcomm

RobotMac Core 把 Dragonwing 从开发板变成机器人产品核心：

- QCS8550 / Core Pro：适合比赛主线和性能型 service robot / desktop arm demo。
- RB3 Gen 2 / QCS6490 / Core Lite：适合 robotics、AI vision、smart security、multi-OS、camera、USB、Ethernet、GPIO 和 AI Hub 入口。
- IQ-8275 / VENTUNO Q / Core Industrial：适合 AI compute + MCU deterministic control 的工业叙事。
- IQ10 / Future：支持更高端 AMR、humanoid、sensor-heavy systems 和 reference design 路线。
- Qualcomm Linux：提供更可信的 production Linux / Yocto / OTA / security / ROS 2 / AI SDK hook 叙事。
- AI Hub + QNN/QAIRT + Profiler + Device Cloud：把“模型能跑”变成可测量的 compile、profile、validate、deploy、latency、memory、compute-unit、thermal、power 和 real-device test 证据。

## Demo Storyboard

三分钟 demo：

1. Open：展示 RobotMac Core appliance、board profile、image digest、device identity、power/IO/safety map。
2. Capture：桌面机械臂或移动底盘记录 LeRobot episode。
3. Train：CloudTwin/TrainRouter 提交 GPU job，生成 model artifact、dataset lineage 和评估报告。
4. Deploy：AI Hub/QNN/QAIRT 或 ONNX path profile 后，signed skill package 推送到本体。
5. Run local：机器人本地执行，网络不进入 safety/control loop。
6. Evidence：展示 p50/p95 latency、memory、compute target、model version、rollback package、safety trigger、failure clip。
7. Recover：坏模型或传感器异常触发 admission denial、safe mode 或 rollback。
8. Loop：失败 episode 进入下一轮训练队列。

## Ask

请求 Qualcomm 支持一个 6-8 周 Dragonwing Robot Core validation sprint：

- Hardware access：Rhino X1/QCS8550、RB3 Gen 2 Vision Kit、Radxa Q6A 或 VENTUNO Q。
- AI Hub / Device Cloud quota。
- QNN / QAIRT workflow guidance。
- Qualcomm Linux / BSP guidance for camera、GStreamer、ROS 2、CAN/UART/GPIO、OTA、local safety services。
- Qualcomm Profiler guidance for CPU/GPU/DSP/NPU、memory、thermal、latency、power 和 long-run stability。
- Dragonwing Robotics Hub reference runtime project 或 developer tutorial 机会。
- Partner introductions for board/SOM/carrier/accessory suppliers。

## Claim Boundaries

可以说：

- RobotMac Core 是 Qualcomm-first 的机器人 compute/power/IO/runtime 原型。
- RobotMac Core 的目标是降低机器人团队从 demo 到部署的工程成本。
- RobotMac Core 把 LeRobot 数据、云训练、Qualcomm edge deployment、runtime evidence 和 fleet hooks 接到同一产品路径。

不能说：

- 已获 Qualcomm 官方认证、合作、投资或官方背书。
- 已通过安全认证、工业 IP rating、functional safety 认证。
- 开箱支持所有机器人。
- 保证零停机。
- 性能优于 Jetson/x86。
- 任意 PyTorch / VLA / LeRobot policy 都能自动跑到 QNN。
- 云端控制可以替代本地 safety。

所有 TOPS、功耗、延迟、温度、FPS、成功率、加速路径和 rollback time 必须标注日期、开发板、SDK、散热、电源、模型版本和是否模拟。

## Sources

- Competition：https://qc-robotics-dev.aidlux.com/2026/
- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- LeRobot docs：https://huggingface.co/docs/lerobot/index
- Rhino X1：https://rhinopi.docs.aidlux.com/en/rhino-x1-aidlux/
- Radxa Dragon Q6A：https://docs.radxa.com/en/dragon/q6a
- Arduino VENTUNO Q：https://www.arduino.cc/product-ventuno-q
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm QCS6490：https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490
- Qualcomm QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Qualcomm IQ-8275：https://www.qualcomm.com/internet-of-things/products/iq8-series/iq-8275
- Qualcomm IQ10 Series：https://www.qualcomm.com/internet-of-things/products/iq10-series
- IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm Linux：https://www.qualcomm.com/developer/software/qualcomm-linux
- AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm Profiler：https://www.qualcomm.com/developer/software/qualcomm-profiler
- Qualcomm Device Cloud：https://qdc.qualcomm.com/support/user-guide/overview
- NVIDIA Isaac ROS：https://developer.nvidia.com/isaac/ros
- NVIDIA Jetson Thor：https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- Viam Fleet Management：https://www.viam.com/platform/fleet-management
- Formant Fleet Observability：https://docs.formant.io/docs/fleet-observability
- Foxglove：https://foxglove.dev/
- Ubuntu ROS ESM：https://ubuntu.com/robotics/ros-esm
- Balena pricing：https://www.balena.io/pricing
- NIST SSDF：https://csrc.nist.gov/pubs/sp/800/218/final
