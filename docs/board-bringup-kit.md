# BoardBringupKit Pitch

更新时间：2026-07-07。

## One-Line Thesis

BoardBringupKit 是 Qualcomm board-to-robot 的可执行验收层：把 RB3 Gen 2 / QCS6490、Rhino Pi-X1 / QCS8550、Dragon Q6A / QCS6490、IQ-9075 等板卡，从“桌上能开机”，变成 48 小时内能被复现、验收、交付、量产迁移的 RobotMac Core 候选核心。

一句话：

> 机器人团队不缺开发板，缺的是“收到板 48 小时内变成可验收机器人核心”的路径。

栈内位置：

- BoardBringupKit：first robot-ready。
- RobotMac Core：可购买 appliance。
- EdgeRuntimeBench：runtime evidence。
- SafetyOps：上线门禁和运动权限。
- ScaleFoundry：EVT/DVT/PVT、BOM/AVL、工厂测试和量产迁移。
- CertForge：合规证据。
- RevenueStack：把 evidence 变成报价、订阅、保修和 SLA。

## 01 · Problem

开发板不是机器人产品。

2026 高通具身智能与机器人开发者大赛把 Rhino Pi-X1/QCS8550、Radxa Dragon Q6A/QCS6490、VENTUNO Q/IQ-8275 推到开发者手里，但团队真正卡住的是：

- 12/24V 机器人电源输入、峰值电流、brownout、热降频、USB 供电和线束松动。
- MIPI/USB/GMSL 相机、V4L2/GStreamer、标定、frame drop 和 timestamp。
- CAN/RS-485/GPIO/PWM/I2C/SPI 的电平、隔离、transceiver、terminator、pinmux 和 loopback。
- ROS 2、DDS、ros2_control lifecycle、QoS、topic rate、diagnostics 和启动顺序。
- 硬急停、watchdog、command timeout、soft boundary 和 actuator power-cut。
- OS image、kernel/device tree、BSP、firmware、QNN/QAIRT、LeRobot、dataset hash 和 image digest 的版本锁定。

结果：8-11 月复赛最宝贵的时间被底层 bring-up 吃掉，而不是投入机器人任务、数据飞轮、端侧证据和商业包装。

## 02 · Current Alternatives Fail

现有方案都解决一部分问题，但没有把 first robot bring-up 产品化。

- Vendor docs：讲接口、烧录和 SDK，不讲完整机器人线束、E-stop、sensor timing、ROS graph、HIL fixture 和客户验收包。
- ROS 2 / ros2_control tutorials：能让节点通信，但团队仍要写 hardware component、处理 lifecycle、实时调度、fallback 和诊断。
- NVIDIA Jetson / Isaac：生态强，公开证明姿态强；但 NVIDIA 自己也区分 developer kit 和 production，carrier、flashing、thermal、power、mechanical 和 validation 仍要团队负责。
- Raspberry Pi / Orange Pi：便宜、社区大、适合 prototyping；但要进入企业机器人，还需要 serious hardening、BSP 成熟度、长供、safety 和 validation。
- Intel / AMD industrial PC：工厂买家熟悉，但更像 PC/IPC，不是低功耗 camera-first robot brain。
- Seeed / Advantech / AAEON / ADLINK：会把模块包装成工业盒子；但不是 developer-first、robot-to-board 的可复用 bring-up kit。
- Luxonis / OAK：smart sensor 很强，能减轻 perception 压力，但不替代主控、power、OTA、安全和 productization stack。
- 一次性 SI：能救一个项目，但难沉淀成 board recipe、golden image、HIL fixture 和 evidence corpus。

市场不缺 edge AI boards，缺的是从 dev board on a bench 到 mounted, powered, cooled, sensed, updated, validated on a real robot 的确定路径。

## 03 · Solution

BoardBringupKit 是一套可执行的 board-to-robot acceptance workflow。

它把裸板变成 RobotMac Core 候选核心：

```text
board_profile
+ protected_power_harness
+ sensor_recipe
+ robot_io_adapter
+ safety_gate
+ runtime_image
+ release_evidence
+ acceptance_report
```

核心流程：

1. `bbk init`：选择 board、robot、sensor、actuator、OS image，生成 board profile、wiring map 和 image digest。
2. `bbk gate boot,camera,io,safety,runtime`：按门禁跑 first boot、camera、I/O、actuator、watchdog、E-stop、runtime。
3. `bbk record`：采集 LeRobotDataset v3 episode，确认相机、动作、时间戳和 metadata。
4. `bbk profile`：调用 EdgeRuntimeBench / AI Hub / QNN 路径，标注 measured / device-cloud / proxy / simulated。
5. `bbk export`：生成 judge / SI / enterprise audit pack。

第一版 wedge：

> 48-hour Qualcomm Robot Bring-up Sprint。

目标：

- <2h first camera。
- <4h first actuator ping。
- <8h first LeRobot episode。
- <24h first edge profile。
- <48h board-to-robot acceptance。

## 04 · Why Now

机器人部署已经进入规模窗口。IFR 报告 2024 年全球工业机器人安装约 542,000 台，全球运行存量约 4.664M，中国占新装机 54%。专业服务机器人、RaaS 和物流机器人也在增长。

Qualcomm 机器人板卡窗口也打开了：

- Dragonwing 是 Qualcomm 2025-02-25 推出的 industrial / embedded IoT / networking / infrastructure brand。
- RB3 Gen 2 / QCS6490 是最稳的 accessible bring-up target：官方 dev kit、Ubuntu 24.04 certified images、AI Hub、Edge Impulse、QIR/ROS path、camera-first I/O，QCS6490 longevity listed to July 2036。
- QCS8550 是 premium compute target：面向 compute-intensive IoT、AMR、drone、edge AI、多相机、Wi-Fi 7；但 AI Hub 常见为 QCS8550 Proxy，不能把 proxy 当真实板端性能。
- IQ-9075 是 high-end industrial/robotics path：Ubuntu 24.04 certified、36 GB LPDDR5 ECC、128 GB UFS、2.5GbE、PCIe、CAN-FD、USB-C、MIPI CSI、longevity listing to 2038，但目前应按 sampling/partner path 谨慎表述。
- IQ10 RRD 证明方向正确：Qualcomm 正在把 compute、AI acceleration、camera/sensor interfaces、motion control、networking 和 robotics software stack 打成 reference design；全球可用性指向 2026 年 9 月，不作为 2026 年 7 月比赛硬件承诺。

软件窗口也打开了：

- LeRobot v0.6.0 于 2026-07-06 发布，强化 rollout、HIL corrections、eval、benchmarks 和 dataset tooling。
- LeRobotDataset v3 把多相机视频、state/action、metadata、stats、task 和 normalization 标准化。
- Qualcomm AI Hub / QAIRT / QNN / ONNX Runtime QNN 提供可展示的模型转换、profile 和 runtime 证据。

## 05 · Product

BoardBringupKit 不是一套线，而是一个 bring-up operating system。

核心模块：

- `Board Recipe Library`：Q6A、Rhino X1、RB3 Gen 2、IQ-9075、VENTUNO Q 的 board manifest、known-good image、接口图、版本锁。
- `Protected Harness BOM`：12/24V keyed connector、fuse/eFuse、reverse-polarity、over/undervoltage、inrush、TVS/surge、power-good gate、E-stop cut path。
- `Production Carrier Pattern`：power sequencing、watchdog、RTC option、debug/recovery、test pads、keyed harness、wide input、GbE、USB、CAN、M.2、fan、camera expansion。
- `Sensor Gate`：MIPI/USB/GMSL camera map、V4L2/media topology、GStreamer pipelines、frame age、drop rate、calibration snapshot。
- `Robot I/O Gate`：protected CAN/CAN-FD、RS-485、24V industrial GPIO、PWM/I2C/SPI loopback、motor/arm/gripper ping。
- `Safety Gate`：dual-channel E-stop input、reset/restart interlock、watchdog loss、command timeout、soft-boundary deny、manual takeover。
- `Runtime Gate`：LeRobot episode capture、policy replay、AI Hub/QNN/ONNX profile hook、EdgeRuntimeBench route、SkillDock package hook。
- `Factory/EOL Gate`：flash image、program serial/MAC/keys、verify rails、USB、Ethernet、CAN、RS-485、GPIO、camera lanes、fan/tach、storage、LED/buttons、thermal smoke test。
- `Evidence Export`：judge-audit-pack、SI handoff packet、factory bring-up report、certification-prep archive。

产品状态：

- `Ready`
- `Sensor Risk`
- `I/O Risk`
- `Runtime Risk`
- `Safety Blocked`
- `Needs BSP Fix`
- `Production Migration Required`

## 06 · Product API/Evidence

核心命令：

```bash
bbk init --board rb3-gen2-qcs6490 --robot lab-transfer-arm
bbk gate boot,camera,io,safety,runtime
bbk record --format lerobot-v3 --episodes 5
bbk profile --route onnx-qnn --target rb3-gen2
bbk export --pack board-bringup-audit-pack.zip
```

核心证据对象：

- `board-bringup-manifest.json`：board、SoC、serial、OS、kernel、BSP、image digest、runtime versions、container digest。
- `wiring-map.svg`：power rails、camera、I/O、E-stop、actuator、network、safety boundary、connector photo index。
- `power-thermal-log.jsonl`：input voltage、current estimate、temperature、throttling flags、fan state、load scenario。
- `camera-gate-report.json`：device path、driver、V4L2/media topology、GStreamer pipeline、resolution、FPS、drop rate、latency、calibration hash。
- `robot-io-report.json`：CAN/UART/GPIO/PWM/I2C/SPI tests、motor/arm/gripper ping、ros2_control lifecycle state。
- `safety-event-ledger.jsonl`：E-stop、watchdog、command timeout、soft-boundary deny、manual takeover、rollback pointer。
- `runtime-image.lock`：OS image、Yocto/Ubuntu rootfs、kernel/device-tree、packages、containers、QNN/QAIRT/ONNX/LeRobot versions。
- `edge-profile.qualcomm.json`：AI Hub / QNN / ONNX Runtime QNN profile job、device/proxy label、latency、load、backend、fallback。
- `release-evidence.json`：SBOM/provenance、OTA signing status、secure-boot state, vulnerability triage、approvals。
- `acceptance-report.md`：pass/fail、failed gates、measured/proxy/simulated labels、reproduction command、next action。
- `judge-demo-index.md`：三分钟视频时间码映射到 board profile、task run、failure recovery 和 evidence artifact。

所有指标标注来源：

- `measured-on-board`
- `AI-Hub-device-cloud`
- `proxy`
- `vendor-doc`
- `simulated`
- `blocked`

合规/安全口径：

- 可说：BoardBringupKit collects and packages engineering evidence intended to support bring-up, release review, supplier audits, and certification preparation。
- 不说：certified、compliant、production approved、secure boot enabled、OTA safe 或 regulator approved，除非有签名 release evidence 和第三方认证结果。

## 07 · Market & Business Model

硬件本身越来越便宜，失败的 bring-up cycle 很贵。

ICP：

1. 参赛团队和高校实验室：48 小时跑通 first robot。
2. 机器人创业公司：从 dev kit 到第一个可交付样机。
3. 系统集成商：把 AMR、机械臂、质检、实验室、教育项目做成可复用交付包。
4. SOM / dev-board 厂商：把芯片/板卡 demo 变成 reference robot recipe。
5. 企业实验室：内部 PoC 要求 evidence，而不只是 demo video。
6. RobotMac Core 客户：把 BoardBringupKit 变成硬件认证和量产迁移门槛。

中国版：

- Free checklist：公开 board profile、检查清单、兼容矩阵。
- Builder Kit：¥3,999-19,800，含镜像、BOM、诊断和模板。
- Pilot Sprint：¥50,000-180,000，bring up 一块板 + 一台机器人 + 一套 sensor/IO。
- Production Pack：¥180,000-600,000，含 BSP/device-tree、HIL fixture、factory flash、cert-prep。
- Team Pro：¥30,000-120,000/year，持续 CI/HIL、兼容矩阵、版本回归和远程支持。
- Board-vendor Co-sell：board recipe NRE + reference design maintenance。

海外版：

- Builder Kit：$499-$2,500。
- Pilot Sprint：$25,000-$75,000。
- Production Pack：$75,000-$200,000。
- Team Pro：$10,000-$25,000/year。
- Board-vendor / SOM-vendor recipe package：NRE + yearly maintenance。

ROI：

> 如果 BoardBringupKit 避免一次 2-8 周 BSP、driver、power、thermal、sensor、ROS 和 safety debug 循环，它就比一次外包救火便宜。

RevenueStack 连接点：

- board recipe 变成 SKU。
- support boundary 变成合同条款。
- warranty/SLA 绑定 evidence pack。
- runtime entitlement 接 EdgeRuntimeBench / SkillDock。
- RobotMac Core attach 进入硬件与订阅收入。

## 08 · Competition & Moat

竞争不是谁有更多线和文档，而是谁能拥有 Qualcomm robot bring-up 的验证记忆。

竞争图：

- NVIDIA Jetson / Isaac：开发者信心强，是主要对标。
- Raspberry Pi / Orange Pi：可及性强，但企业机器人硬化不足。
- Intel / AMD IPC：工厂熟悉，但更 PC-like。
- Seeed / Advantech / AAEON / ADLINK：工业包装强，但开发者 bring-up 低摩擦不足。
- Luxonis / OAK：smart sensor 强，但不是主控 productization stack。
- Unitree / robot vendors：提供 robot body，但客户仍要接 perception、policy、logging、OTA 和安全。
- Vendor docs / SI：能解决单点问题，但不形成验证语料库。

Moat：

- `Compatibility Matrix`：board + carrier + camera + LiDAR + motor controller + power stack + ROS distro + kernel/BSP。
- `HIL Fixture`：first boot、rail/current、USB/MIPI、CAN/Ethernet、thermal soak、camera timing、motor loop。
- `Machine-readable Manifests`：生成 udev、ROS launch、diagnostics、factory tests、wiring report 和 deploy manifest。
- `Golden Images`：可复现 build、OTA hooks、secure defaults、logs、health topics、rollback 和 image diff。
- `Failure Corpus`：每个失败项、驱动版本、BSP patch、传感器组合和客户现场问题都会增加路径依赖。
- `Partner Loop`：Qualcomm、Radxa、APLUX、Thundercomm、Advantech、SI、传感器厂和机器人团队共同更新 acceptance language。

## 09 · Why Qualcomm

Qualcomm 的机会不是再发一块开发板，而是让 Dragonwing board 更快进入机器人产品化标准。

Qualcomm-specific 路线：

- RB3 Gen 2 / QCS6490：practical first target，官方 dev kit、Ubuntu 24.04 certified images、AI Hub、Edge Impulse、camera-first I/O、QIR/ROS path、QCS6490 longevity listed to 2036。
- Dragon Q6A / QCS6490：比赛 immediate target，可作为 Core Lite 和 fallback。
- Rhino Pi-X1 / QCS8550：premium compute target，适合多相机、高性能边缘 AI 和 RobotMac Core Pro；AI Hub 上 QCS8550 profile 常见为 proxy，必须标注。
- IQ-9075：high-end industrial path，edge AI/robotics EVK、ECC memory、2.5GbE、CAN-FD、PCIe、MIPI CSI，当前按 partner/sampling path 谨慎推进。
- IQ10 RRD：enterprise roadmap / early-access ask，不写成 2026-07 可交付比赛硬件。
- AI Hub / QAIRT / QNN：进入 Runtime Gate，生成 measured / device-cloud / proxy evidence。

对 Qualcomm 的价值：

- 缩短 developer time-to-first-robot。
- 减少 SDK/BSP/camera/ROS support 摩擦。
- 给 Dragonwing 一个 Jetson-like developer confidence story。
- 把 AI Hub/QNN、camera/multimedia、low-power edge、wireless 和 ROS guidance 连接成真实机器人路线。
- 为未来 IQ10 RRD、RobotMac Core 和 partner modules 建立 productization path。

边界：

- 不声称 Qualcomm 官方认证。
- 不承诺所有模型跑 NPU。
- 不把 longevity listing 写成 guaranteed supply。
- 不把 secure boot / OTA / certification readiness 写成默认已完成。
- 所有性能数据必须标注硬件、SDK、散热、电源、模型和测量方式。

## 10 · Demo & Ask

三分钟只证明一件事：开发板已经变成可复现机器人核心。

Storyboard：

1. 0:00-0:15：裸板、线束、相机、机械臂、E-stop 同框，打出“开发板不是机器人产品”。
2. 0:15-0:35：`bbk init` 生成 board profile、image digest、wiring map。
3. 0:35-1:05：跑 boot、camera、I/O、actuator、watchdog、E-stop gates。
4. 1:05-1:35：采集 LeRobot episode：样品识别、抓取、放置、复核。
5. 1:35-2:05：EdgeRuntimeBench 展示 runtime route、latency、fallback、thermal。
6. 2:05-2:35：SafetyOps 注入 wrong sample / unsafe command，系统 pause/deny/recover。
7. 2:35-3:00：导出 `board-bringup-audit-pack.zip`，进入 RobotMac Core / ScaleFoundry / CertForge / RevenueStack。

Demo KPIs：

- 48h 内完成 board-to-robot acceptance。
- <2h first camera。
- <4h first actuator ping。
- <8h first LeRobot episode。
- <24h first edge profile。
- >90% gate pass rate。
- >95% rerun reproducibility。
- 0 unlogged safety events。
- 3 board recipes。
- 5 paid pilots。
- 2026-11 前 30 个 evidence packs。

Ask：

- Rhino Pi-X1 / QCS8550 或 Dragon Q6A / QCS6490 target board。
- RB3 Gen 2 / QCS6490 reference kit。
- AI Hub / Device Cloud quota。
- QNN / QAIRT office hours。
- Qualcomm Linux / BSP / camera / GStreamer / ROS guidance。
- 允许提交 bring-up artifacts 和 runtime evidence。
- 引荐 APLUX、Radxa、Thundercomm、Advantech、SI/OEM 和教育合作伙伴。
- IQ10 RRD roadmap review，作为企业版 RobotMac Core 的未来路线。

## Sources

- 2026 高通具身智能与机器人开发者大赛：https://qc-robotics-dev.aidlux.com/2026/
- Competition launch and official boards：https://ex.chinadaily.com.cn/exchange/partners/82/rss/channel/cn/columns/sz8srm/stories/WS69fea1a7a310942cc49ab5d5.html
- Qualcomm Dragonwing：https://www.qualcomm.com/news/onq/2025/02/unveiling-the-qualcomm-dragonwing-brand-portfolio
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB5 sample apps：https://github.com/quic/sample-apps-for-robotics-platforms
- Qualcomm Robotics RB5：https://www.qualcomm.com/developer/hardware/robotics-rb5-development-kit
- Qualcomm QCS8550 product brief：https://docs.qualcomm.com/doc/87-61717-1/87-61717-1_REV_D_Qualcomm_Dragonwing_QCS8550_QCM8550_Processors_Product_Brief.pdf
- Dragonwing IQ8/IQ9：https://www.qualcomm.com/developer/blog/2026/06/accelerate-industrial-iot-development-dragonwing-iq8-iq9
- Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Radxa Dragon Q6A docs：https://docs.radxa.com/en/dragon/q6a
- APLUX Rhino Pi-X1 docs：https://rhinopi.docs.aidlux.com/en/rhino-x1-aidlux/
- APLUX XLerobot-X1：https://github.com/APLUX-Official/XLerobot-X1
- Arduino VENTUNO Q：https://www.arduino.cc/product-ventuno-q
- Qualcomm AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- Ubuntu RB3 Gen2：https://ubuntu.com/download/qualcomm-iot
- ROS 2 Jazzy release：https://discourse.openrobotics.org/t/ros-2-jazzy-jalisco-released/37862
- ROS 2 Lyrical release：https://docs.ros.org/en/rolling/Releases/Release-Lyrical-Luth.html
- GStreamer gst-launch：https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html
- ros2_control hardware components：https://control.ros.org/rolling/doc/ros2_control/hardware_interface/doc/writing_new_hardware_component.html
- ROS safety watchdogs：https://github.com/ros-safety/software_watchdogs
- LAVA：https://docs.lavasoftware.org/lava/index.html
- OpenHTF：https://github.com/google/openhtf
- Yocto SBOM：https://docs.yoctoproject.org/dev/dev-manual/sbom.html
- TUF specification：https://theupdateframework.github.io/specification/latest/
- Uptane：https://uptane.org/docs/2.1.0/standard/uptane-standard
- FCC equipment authorization：https://www.fcc.gov/engineering-technology/laboratory-division/general/equipment-authorization
- EU RED：https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red_en
- Jetson developer FAQ：https://developer.nvidia.com/embedded/faq
- Jetson bring-up checklist：https://docs.nvidia.com/jetson/archives/r36.5/DeveloperGuide/HR/JetsonModuleAdaptationAndBringUp/Checklists.html
- IFR robot demand：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- Edge AI hardware market：https://www.marketsandmarkets.com/Market-Reports/edge-ai-hardware-market-158498281.html
- Advantech Qualcomm Dragonwing robotics：https://www.advantech.com/en-us/resources/news/advantech-unveils-new-edge-ai-solutions-for-robotics-automation-and-gen-ai-powered-by-qualcomm-dragonwing
