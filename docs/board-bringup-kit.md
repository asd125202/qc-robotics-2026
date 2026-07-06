# BoardBringupKit Pitch

更新时间：2026-07-06。

## One-Line Thesis

BoardBringupKit 是 Qualcomm 机器人开发板的商业化 bring-up 层：把一块比赛开发板从“能开机”变成“能被复现、验收、交付、量产迁移的 RobotMac Core 候选核心”。

比赛版本的窄切口：

> 帮参加 2026 高通具身智能与机器人开发者大赛的团队，把 Rhino Pi-X1 / QCS8550 或 Radxa Dragon Q6A / QCS6490 从开箱到跑通 ROS 2、摄像头、I/O、安全急停、LeRobot episode 和 Qualcomm runtime 证据，从一两周缩短到 48 小时内。

## 01 · Problem

开发板不是机器人产品。真正危险的不是买不到板，而是收到板之后每个团队都在重复踩同一批坑：

- 电源电压、峰值电流、USB 供电和热降频不稳定。
- 摄像头 MIPI/USB、V4L2/GStreamer、标定和帧率掉帧难复现。
- GPIO/CAN/UART/I2C/SPI 电平、pinmux、transceiver、terminator 和驱动版本不一致。
- ROS 2/ros2_control 生命周期、QoS、topic rate、诊断和启动顺序没有工程门禁。
- 物理急停、watchdog、软边界和 actuator power-cut 常常在 demo 后才补。
- runtime image、firmware、driver、QNN/QAIRT、ONNX、LeRobot、dataset hash 没有版本锁定。

结果是：团队把 8-10 月复赛最宝贵的时间花在底层 bring-up，而不是机器人任务、数据飞轮和商业产品定义。

## 02 · Current Alternatives Fail

现有方案都解决一部分问题，但没有把“板卡进入机器人产品”做成可复用验收工作流。

- Vendor docs：能告诉你接口、烧录、SDK，但通常不会覆盖完整机器人 I/O、传感器、E-stop、ROS 2、HIL、部署和客户验收。
- ROS 2 tutorials：能让节点通信，但不会验证电源、热、相机 lane、USB bandwidth、CAN transceiver、安全停机和生产镜像。
- Jetson / Isaac ecosystem：强在 AI 和参考流程，但生产化仍需要 carrier board、pinmux、device tree、BSP、thermal 和 validation。
- Clearpath / Husarion / AgileX / Unitree / Elephant：强在整机/教育/研发平台，不解决客户自己的 robot electronics、BOM、factory flash 和合规证据。
- Fleet tools：Foxglove、Formant、InOrbit 能运营已有机器人，但不会替你做 first boot、硬件 fixture、IO bring-up 和安全边界。
- One-off integrator service：可以救一个项目，但很难沉淀成可复制 board recipe、test fixture、golden image 和证据包。

## 03 · Solution

BoardBringupKit 把 board-to-robot bring-up 做成可执行产品，而不是 PDF checklist。

核心输出：

1. `board_profile`：SoC、board revision、OS、kernel、BSP、firmware、QNN/QAIRT、ROS distro、LeRobot version、image digest。
2. `power_harness`：输入电压、峰值电流、分路供电、保险、状态灯、E-stop power-cut、undervoltage/thermal flags。
3. `sensor_recipe`：MIPI/USB camera、depth camera/LiDAR、V4L2/GStreamer test、标定、frame drop、timestamp 和 cable/hub matrix。
4. `robot_io_adapter`：CAN/UART/GPIO/PWM/I2C/SPI loopback、level shifting、motor/arm/gripper ping、ros2_control hardware interface。
5. `safety_gate`：硬急停、software watchdog、command timeout、soft boundary、SafeOps/SafetyOps decision 和 incident log。
6. `runtime_image`：可复现镜像、依赖锁定、CloudTwin agent、EdgeRuntimeBench profiler、SkillDock bundle hook 和 rollback。
7. `acceptance_report`：time-to-first-camera、time-to-first-actuator、time-to-first-episode、time-to-first-edge-run、失败项和复现命令。

## 04 · Why Now

2026 年的时机来自三件事叠加：

- 具身智能和机器人比赛把 Qualcomm board 推到更多开发者面前，但比赛窗口短，底层集成失败会直接拖垮项目。
- QCS6490/QCS8550/RB3 Gen 2/IQ 系列让 Qualcomm 在机器人边缘 AI 上有清晰入口，但开发者需要板卡进入机器人系统的路径。
- 企业客户正在从 demo 走向试点，采购要看的不是“我会接线”，而是 wiring map、image digest、power/thermal evidence、safety log、runtime profile 和 rollback record。

当前板卡策略：

- `Dragon Q6A / QCS6490`：最现实的 immediate target，可作为 Core Lite、教育版和备用板。
- `Rhino Pi-X1 / QCS8550`：标准赛道高性能 target，用于 LabForgePilot、EdgeRuntimeBench 和 RobotMac Core Pro。
- `RB3 Gen 2 / QCS6490`：真实 dev kit 和生态参考，不写成官方比赛板。
- `VENTUNO Q / IQ-8275`：先行者赛道/partner-supplied target，等实物和 SDK 稳定后接入。
- `IQ10 RRD`：企业版 roadmap / early access ask，不作为 2026 年 7 月承诺。

## 05 · Product

BoardBringupKit 的产品不是一套线，而是一个 bring-up operating system。

产品模块：

- `Board Recipe Library`：Q6A、Rhino X1、RB3 Gen 2、VENTUNO Q 的 board manifest、known-good image、接口图、版本锁。
- `Harness BOM`：电源、E-stop、camera mount、USB/CSI cable、CAN transceiver、IO terminal、level shifter、status light。
- `First Boot Runner`：boot、network、storage、clock、thermal、fan、USB speed、serial log、kernel flags。
- `Sensor Gate`：camera enumerate、V4L2/GStreamer capture、frame age、drop rate、calibration snapshot。
- `Actuator Gate`：机械臂/夹爪/底盘 ping、single-axis move、command timeout、ros2_control lifecycle。
- `Safety Gate`：E-stop trigger、watchdog loss、soft boundary、manual takeover、incident ledger。
- `Runtime Gate`：LeRobot episode capture、policy replay、AI Hub/QNN/ONNX profile placeholder 或真实 profile、deploy manifest。
- `Evidence Export`：judge/enterprise audit pack、factory bring-up report、SI handoff packet。

## 06 · Evidence Objects

BoardBringupKit 必须让评委、工程师、SI、客户和供应链都能读懂同一组证据。

- `board-bringup-manifest.json`：board、SoC、serial、OS、kernel、BSP、image digest、runtime versions。
- `wiring-map.svg`：power rails、camera、IO、E-stop、actuator、network 和安全边界。
- `power-thermal-log.jsonl`：input voltage、current estimate、temperature、throttling flags、fan state、load scenario。
- `camera-gate-report.json`：device path、driver、resolution、FPS、drop rate、latency、calibration image hash。
- `robot-io-report.json`：CAN/UART/GPIO/PWM/I2C/SPI test、motor/arm/gripper ping、ros2_control lifecycle state。
- `safety-event-ledger.jsonl`：E-stop、watchdog、command timeout、soft-boundary deny、manual takeover。
- `runtime-image.lock`：package versions、containers、QNN/QAIRT/ONNX/LeRobot versions、CloudTwin/EdgeRuntime hooks。
- `acceptance-report.md`：pass/fail、failed gates、measured/proxy/simulated labels、reproduction command、next action。
- `judge-demo-index.md`：三分钟视频时间码映射到 board profile、task run、failure recovery 和 evidence artifact。

## 07 · Market & Business Model

硬件本身越来越便宜，真正贵的是一个失败 bring-up cycle。

买家：

- 机器人创业公司：从 dev kit 走向第一个集成样机。
- 系统集成商：把 AMR、机械臂、质检、实验室、教育项目做成可复用交付包。
- SOM/dev-board 厂商：把芯片/板卡 demo 变成 reference robot package。
- 高校、企业实验室、赛事团队：快速跑通真实机器人闭环。
- RobotMac Core 后续客户：把 BoardBringupKit 变成硬件认证和量产迁移门槛。

定价假设：

- Free/open：board profile、公开 checklist、兼容矩阵。
- Builder Kit：中国 ¥3,999-19,800，海外 $499-2,500，含镜像、BOM、诊断和模板。
- Pilot Sprint：中国 ¥50k-180k，海外 $25k-75k，bring up 一块板 + 一个机器人 + 一套 sensor/IO。
- Production Pack：中国 ¥180k-600k，海外 $75k-200k，含 BSP/device-tree、HIL fixture、factory flash、cert-readiness。
- Team Pro：中国 ¥30k-120k/year，海外 $10k-25k/year，持续 CI/HIL、兼容矩阵、版本回归和远程支持。
- Board-vendor Co-sell：每个 board recipe NRE + reference design 维护费。

ROI 语言：

> 如果 BoardBringupKit 避免一次 2-8 周的 BSP/driver/power/thermal/debug 循环，它就已经比一次外包救火便宜。

## 08 · Competition & Moat

不要把 BoardBringupKit 做成“又一个机器人套件”。市场上已经有很多套件。它的壁垒是 accumulated validation data。

竞争地图：

- Jetson / Isaac：生态强，但生产 carrier/BSP/thermal/device-tree 仍要自己做。
- ROS-Industrial：middleware 和工业驱动强，但不负责生产镜像、安全证据和硬件验收。
- Clearpath / Husarion / AgileX / Unitree / Elephant：整机强，但用户的自研产品仍需要自己的 compute stack。
- Foxglove / Formant / InOrbit：运营强，但通常从机器人已经存在之后开始。
- Vendor reference designs：展示 SoC 能力，但很少沉淀跨机器人、跨传感器、跨工厂的 evidence workflow。

壁垒：

- 兼容矩阵：board + carrier + camera + LiDAR + motor controller + power stack + ROS distro + kernel/BSP。
- HIL fixture：first boot、rail/current、USB/MIPI、CAN/Ethernet、thermal soak、camera timing、motor loop。
- Machine-readable manifests：生成 udev、ROS launch、diagnostics、factory tests、wiring report 和 deploy manifest。
- Golden images：可复现 build、OTA hooks、secure defaults、logs、health topics、rollback。
- Evidence corpus：每个失败项、驱动版本、BSP patch、传感器组合和客户现场问题都会增加路径依赖。

## 09 · Why Qualcomm

Qualcomm 的战略机会不是多发一块开发板，而是让 Dragonwing board 进入机器人产品化标准。

BoardBringupKit 对 Qualcomm 有三层价值：

- 比赛价值：评委能看到 Qualcomm board 在真实机器人控制闭环中，而不是只出现在 PPT 和终端截图里。
- 生态价值：减少开发者 time-to-first-robot，让 QCS6490/QCS8550/RB3 Gen 2 更容易被创业团队和 SI 采用。
- 商业价值：把 AI Hub/QNN/QAIRT、camera/multimedia、low-power edge、ROS guidance 和 future IQ10 RRD 连接成从比赛到产品的路线。

主张边界：

- 不声称 Qualcomm 认证或功能安全认证。
- 不保证所有 policy 都跑在 NPU；真实 profile 必须由 EdgeRuntimeBench 标注 measured/proxy/simulated。
- 不把 IQ10 写成 2026 年 7 月可交付板卡。
- 不替代 vendor BSP、AI Hub、QNN 或 ROS 2；BoardBringupKit 是把它们接成机器人验收工作流。

## 10 · Demo & Ask

三分钟演示要证明一件事：开发板已经变成可复现机器人核心。

视频结构：

1. 0:00-0:15：展示裸板、线束、相机、机械臂、E-stop，然后打出“开发板不是机器人产品”。
2. 0:15-0:40：BoardBringupKit checklist：boot、network、camera、actuator、safety、runtime、manifest。
3. 0:40-1:20：一键 bring-up runner 过门禁：camera frame、actuator ping、E-stop/watchdog event、image digest。
4. 1:20-2:05：LabForgePilot 执行样品识别、抓取、放置、复核和日志写入。
5. 2:05-2:30：扰动：错样本、挪动目标、unsafe command；机器人 pause/deny/recover。
6. 2:30-2:50：Evidence dashboard：board profile、wiring map、camera calibration、runtime image、safety log、rollback。
7. 2:50-3:00：导出 `board-bringup-audit-pack.zip`，作为复赛和商业试点证据。

向 Qualcomm / 主办方的 ask：

- Rhino Pi-X1 / QCS8550 或 Dragon Q6A / QCS6490 target board。
- AI Hub Workbench / Device Cloud quota。
- QNN/QAIRT profiling office hours。
- Qualcomm Linux/BSP guidance：camera、GStreamer、ROS 2、GPIO/CAN/UART、OTA、watchdog。
- 允许提交 board bring-up artifacts、runtime profile 和三分钟 video proof。
- IQ10 RRD roadmap review，作为企业版 RobotMac Core 的未来路线。

## Sources

- 2026 高通具身智能与机器人开发者大赛：https://qc-robotics-dev.aidlux.com/2026/
- Competition launch and official boards：https://ex.chinadaily.com.cn/exchange/partners/82/rss/channel/cn/columns/sz8srm/stories/WS69fea1a7a310942cc49ab5d5.html
- Qualcomm AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm QCS8550 product brief：https://docs.qualcomm.com/doc/87-61717-1/87-61717-1_REV_D_Qualcomm_Dragonwing_QCS8550_QCM8550_Processors_Product_Brief.pdf
- Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Radxa Dragon Q6A docs：https://docs.radxa.com/en/dragon/q6a
- APLUX Rhino Pi-X1 docs：https://rhinopi.docs.aidlux.com/en/rhino-x1-aidlux/
- APLUX XLerobot-X1：https://github.com/APLUX-Official/XLerobot-X1
- Arduino VENTUNO Q：https://www.arduino.cc/product-ventuno-q
- NVIDIA Jetson bring-up checklist：https://docs.nvidia.com/jetson/archives/r36.5/DeveloperGuide/HR/JetsonModuleAdaptationAndBringUp/Checklists.html
- NVIDIA Jetson camera driver programming：https://docs.nvidia.com/jetson/archives/r35.1/DeveloperGuide/text/SD/CameraDevelopment/SensorSoftwareDriverProgramming.html
- ROS 2 control hardware components：https://control.ros.org/rolling/doc/ros2_control/hardware_interface/doc/writing_new_hardware_component.html
- ROS 2 controller manager：https://control.ros.org/rolling/doc/ros2_control/controller_manager/doc/userdoc.html
- ROS safety watchdogs：https://github.com/ros-safety/software_watchdogs
- Foxglove pricing：https://foxglove.dev/pricing
- PickNik services and support：https://picknik.ai/licensing
