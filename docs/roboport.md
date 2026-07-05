# RoboPort Pitch

更新时间：2026-07-05。

## Core Thesis

真正像 Mac / Windows / iPhone 一样的机器人平台，不能每接一个相机、夹爪、伺服、传感器和安全模块都重新布线、重写驱动、重新标定、重新做风险文件。

RoboPort 是机器人模组港：

> Qualcomm edge core + 标准化机器人端口 + 模组护照 + ROS 2 / LeRobot 元数据 + 兼容测试 + 安全证据包 + 认证模块市场。

它不是承诺“一个万能接口支持所有设备”，而是把机器人扩展拆成四类可交付端口：

1. **Motion / I/O Port**：EtherCAT、CANopen、24V industrial I/O、STO、安全控制器桥接。
2. **Smart Tool Port**：夹爪、吸盘、力控、IO-Link、RS-485/Modbus、工具供电与诊断。
3. **Perception Port**：MIPI CSI-2、GMSL/FPD-Link、GigE Vision、PoE、trigger、PTP timestamp。
4. **Internal Expansion Port**：M.2、PCIe、USB、radio、storage、accelerator、capture card。

每个模块必须带上自己的硬件边界、软件驱动、坐标系、LeRobot schema、功耗、固件版本、风险提示和测试结果。

## Why This Matters

机器人项目常常死在最后 20%：

- 线束、电源、地线、屏蔽、热设计没有统一边界。
- 相机、夹爪、驱动器和安全 IO 的 ROS 节点互相不兼容。
- URDF、camera calibration、frame、QoS、timestamp 和 LeRobot feature schema 缺失。
- 供应商固件升级后现场部署失效。
- 新末端工具改变了风险评估，但证据文件没有跟上。
- 客户采购看到的是零散 BOM，而不是可测试、可追溯、可维护的模块系统。

RoboPort 的价值是把这些隐性集成工作前置成产品标准。

## Product Modules

### 1. RoboPort Edge Core

Qualcomm edge SoC 作为机器人扩展中枢。

- 多摄像头、AI 推理、连接、ROS 2 graph、模块发现和本地诊断。
- 模型部署和 LeRobot 数据采集都围绕同一个 edge target。
- 支持未来 Dragonwing / RB / QCS / IQ 系列硬件路线。

### 2. SmartPort Physical Layer

不是一个万能插头，而是一组清晰分层的端口规范。

- 每类端口定义机械定位、键位、防呆、电压、电流、热设计、e-fuse、隔离、接地、屏蔽和热插拔边界。
- 低功率传感器可以快速发现，高功率执行器必须经过失能、识别、授权、上电流程。
- 安全链路与 AI/Linux/cloud 解耦，急停、STO 和安全控制器不依赖普通应用进程。

### 3. Module Passport

模块护照是机器人外设的软件说明书。

- vendor、product、serial、firmware hash、port class、power class、driver image、firmware ABI。
- URDF/xacro、frame、calibration、camera info、ros2_control interface、MoveIt snippet。
- LeRobot observation/action feature、shape、dtype、unit、FPS、timestamp source。
- 支持 udev / CAN / Ethernet / USB / EEPROM / secure ID 的稳定识别。

### 4. Driver Capsule

把驱动变成可测试、可回滚、可发布的胶囊。

- ROS 2 driver / controller 容器化，带版本、依赖、license、SBOM、签名和兼容矩阵。
- 测试启动顺序、QoS、断连恢复、延迟、CPU/GPU/内存占用、固件升级和回滚。
- 模块 Manager 只有在 Manifest、驱动、固件和测试结果匹配时才允许激活。

### 5. SafePort Evidence Pack

兼容不是口号，是证据包。

- 模块分类：sensor、end effector、drive、safety I/O、battery、radio、tool、partly completed machinery。
- 记录 intended use、prohibited use、payload、force、torque、speed、environment、compatible robots、firmware versions。
- 输出电气、EMC/RF、热、故障注入、急停/STO、安全 IO、risk assessment delta 和 change-control 文件。
- 明确边界：RoboPort Certified 是兼容性与交付证据认证，不替代系统级 ISO/UL/CE 风险评估。

### 6. CertLab + Marketplace

把模块生态做成商业市场，而不是 PDF 列表。

- 供应商提交模块，测试夹具生成兼容评分、性能曲线、故障记录和证据包。
- 集成商按场景组合：3D vision kit、force-gripper kit、AMR safety kit、CiA 402 servo bridge。
- 客户按认证等级、兼容机器人、交付周期、功耗、总线、ROS 2、LeRobot schema 和证据包采购。

## Competition Demo

比赛不需要真的做完整生态，先展示一条可信流程：

1. RobotMac / Rhino X1 / QCS8550 edge core 接入两个模块：相机与夹爪。
2. 系统识别 module passport，自动加载 ROS 2 节点、URDF frame 和 LeRobot feature schema。
3. 换一个末端工具，界面显示 action schema、功耗、payload 和安全边界变化。
4. 用 LeRobot 录制一段新任务 episode，证明数据天然带硬件元数据。
5. 输出一个兼容测试报告：latency、timestamp、calibration、driver version、safe stop signal、risk note。

评委看到的不是“插个外设”，而是一套从硬件接口到训练数据、技能部署和企业交付的产品化扩展体系。

## Why Qualcomm Should Care

Qualcomm 做机器人生态，不能只卖开发板或 reference design。开发者和企业真正需要的是：

- 哪些传感器和末端工具能稳定接上？
- 哪些驱动能跑在 Qualcomm edge 上？
- 哪些模块会产出正确的 LeRobot 数据？
- 哪些模块能通过边缘性能测试和安全边界审查？
- 哪些供应商可以一起进入市场？

RoboPort 把 Qualcomm edge hardware 变成机器人模块生态的默认认证目标。每一个通过认证的相机、夹爪、驱动器和安全 IO，都在扩大 Qualcomm 的开发者入口和商业交付半径。

## Claims To Avoid

- 不声称一个 universal port 能替代 EtherCAT、CANopen、IO-Link、GigE Vision、MIPI CSI、USB、PCIe 和 safety I/O 的差异。
- 不声称 USB-C 可以替代工业 I/O 或安全链路。
- 不声称 ROS 2、MoveIt、LeRobot 或 Linux 本身具备功能安全认证。
- 不声称 RoboPort Certified 等于 CE、UL、ISO 10218、ISO 13849 或 IEC 62061 认证。
- 不声称任何模块都能即插即用；真实世界仍需要驱动、标定、风险评估和版本匹配。

## Sources

- Qualcomm Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm RB3 Gen 2 Development Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6 Robotics Platform：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- EtherCAT Technology：https://www.ethercat.org/en/technology.html
- CANopen / CiA：https://www.can-cia.org/can-knowledge/standardized-higher-layer-protocols
- IO-Link：https://io-link.com/
- MIPI CSI-2：https://www.mipi.org/specifications/csi-2
- GigE Vision：https://www.automate.org/vision/vision-standards/vision-standards-gige-vision
- ros2_control：https://control.ros.org/rolling/doc/getting_started/getting_started.html
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Universal Robots marketplace：https://www.universal-robots.com/marketplace/
- ISO robotics standards overview：https://www.iso.org/sectors/engineering/robotics
