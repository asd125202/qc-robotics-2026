# Hardware Product Form Factors

更新时间：2026-07-05。

## Product Principle

RobotMac Core 不应该被定义为“某一块开发板的外壳”。它应该是一条产品线：

- 统一软件/云训练/技能包体验。
- 按算力、IO、实时控制、安全和成本拆成不同 SKU。
- 第一阶段用比赛板卡实现 demo，未来迁移到更高端 Qualcomm reference design。

## Three Practical SKUs

| SKU | Target | Board / SoC direction | Why |
| --- | --- | --- | --- |
| Core Lite | 教育、开发者、小车、简单机械臂 | Radxa Dragon Q6A / QCS6490 | 紧凑、低功耗、工业 IoT/edge AI 定位，适合入门和批量教学。 |
| Core Pro | 比赛主线、服务机器人、桌面机械臂 | APLUX Rhino X1 / QCS8550 | 48 TOPS INT8、强多媒体与边缘 AI，适合 Standard Track 主 demo。 |
| Core Industrial | 工业控制、确定性执行、高端机械臂 | Arduino VENTUNO Q / IQ-8275 + STM32H5 | 双脑架构：AI compute + real-time microcontroller，适合把 perception/decision/action 放到同一板级系统。 |

## Future SKU

### Core IQ10 Robotics

Qualcomm Dragonwing IQ10 Robotics Reference Design 的公开资料强调“production-ready platform”以及 compute、AI、sensors、software 的组合。相关 product brief 提到面向 sensor-heavy systems，并支持多路高速 GMSL2 cameras、LiDAR、IMU、ToF 等传感器。

这适合作为长期路线：

- AMR / humanoid / 高端服务机器人。
- 多摄像头 360 度感知。
- 本地 AI、确定性 IO、网络和 fleet 管理。
- 不是初赛保底，但非常适合作为“Qualcomm 未来支持价值”的前瞻路线。

## RobotMac Core BOM Blocks

### 1. Compute Module

- Qualcomm Dragonwing edge AI board / SOM.
- Storage for model packages and local episodes.
- Wi-Fi / Ethernet / optional cellular.
- Secure boot / device identity plan.

### 2. Power Module

- Battery input and external DC input.
- Protected regulated rails.
- Separate logic and motor power domains.
- Fuse, reverse-polarity protection, current sensing.
- Power button, status LED, battery telemetry.

### 3. Robot IO Module

- Camera interfaces: MIPI CSI / USB camera / future GMSL2.
- Motor and actuator interfaces: CAN-FD, UART, PWM, GPIO.
- Sensor interfaces: IMU, depth camera, LiDAR, ToF, audio.
- Expansion connector for robot-specific carrier.

### 4. Safety Module

- Physical emergency stop.
- Watchdog.
- Local safety state machine.
- Brownout / thermal / overcurrent handling.
- Cloud-disconnect safe behavior.

### 5. Thermal and Enclosure

- Metal enclosure or heat spreader.
- Replaceable fan/heat sink options.
- Cable strain relief.
- Mounting rail for robot chassis.
- Service-friendly port labeling.

### 6. Software Identity

- Device ID.
- Robot profile.
- Skill compatibility manifest.
- Deployment package registry.
- Telemetry schema.

## Competition Hardware Recommendation

Primary:

- APLUX Rhino X1 / QCS8550.
- Reason: Standard Track, 48 TOPS INT8, strong fit for edge AI + multimedia demo.

Fallback:

- Radxa Dragon Q6A / QCS6490.
- Reason: compact and industrial IoT/edge AI positioning; useful for Core Lite story.

Forward-looking:

- Arduino VENTUNO Q / IQ-8275.
- Reason: dual-brain architecture with STM32H5 for deterministic actuation; strong Pioneer Track and industrial narrative.

## Website / Demo Story

The pitch should show hardware as a packaged product, not as a naked dev board:

1. Open product case with compute, power, IO and sensors.
2. Board tier map: Lite / Pro / Industrial / IQ10 future.
3. Safety boundary: local control, physical e-stop, cloud only for training/telemetry.
4. Upgrade path: same CloudTwin and SkillDock software across hardware SKUs.

## Sources

- Rhino Pi-X1 docs：https://rhinopi.docs.aidlux.com/en/rhino-x1-aidlux/
- Radxa Dragon Q6A docs：https://docs.radxa.com/en/dragon/q6a
- Radxa Dragon Q6A product page：https://www.radxa.com/products/dragon/q6a/
- Arduino VENTUNO Q：https://www.arduino.cc/product-ventuno-q
- Qualcomm IQ-8275：https://www.qualcomm.com/internet-of-things/products/iq8-series/iq-8275
- Qualcomm IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm IQ10 Series：https://www.qualcomm.com/internet-of-things/products/iq10-series
