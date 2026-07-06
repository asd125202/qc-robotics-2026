# RobotCoreOS Pitch

更新时间：2026-07-06。底层 OS、BSP、驱动、secure boot、OTA 和性能指标必须按最终开发板、SDK、散热、电源和供应商支持重新验证。

## One-Liner

RobotCoreOS 是给机器人公司的商业化运行底座：把每个团队都在重复自建的系统镜像、驱动、ROS 2、OTA、回滚、设备身份、数据回流、策略运行器、安全边界和 fleet 运维，做成一套 Qualcomm-first 可交付 runtime OS。

## Problem

机器人团队不缺 Demo，缺的是把 Demo 变成可维护产品的基础设施。

每做一款机器人，团队都要重新处理：

- OS image、BSP、kernel、driver、camera、IO、NPU/GPU/CPU runtime。
- ROS 2 launch、topic contract、lifecycle、time sync、日志和健康检查。
- LeRobot / policy artifact 的输入输出、版本、权限、回滚包和数据回流。
- OTA、A/B rollback、recovery mode、device identity、证书、客户归属和审计。
- 现场故障恢复、版本追溯、SBOM、CVE、企业 IT 问答和责任边界。

买方害怕的不是算法不够酷，而是升级变砖、现场无人能修、版本不可追溯、安全边界不清、20 台机器没人管。

## Why Now

具身智能正在从“能跑一次”走向“能部署一批”：

- ROS Noetic 已在 2025 年 5 月到达 EOL，商业队列需要 LTS image、迁移窗口、补丁策略和冻结验证。
- ROS 2 Jazzy 面向 Ubuntu 24.04 时代，适合作为比赛 demo lane 的默认开发基线。
- LeRobot 让真实数据采集、训练、策略导出和社区复用更开放。
- Qualcomm Dragonwing、AI Hub、QNN/QAIRT、Qualcomm Linux、Device Cloud 和 Profiler 正在补齐边缘 AI 工具链。
- RaaS 和企业试点要求 uptime、远程诊断、proof-of-work、灰度发布、审计、SBOM 和恢复流程。

现在缺的是一个把云训练结果安全、可观测、可审计、可回滚地跑在机器人本体上的标准产品层。

## Solution

> RobotCoreOS = Qualcomm board profile + validated drivers + ROS 2 bridge + LeRobot hooks + QNN/QAIRT policy runner + SafetyOps + signed OTA + A/B rollback + fleet identity + runtime manifest。

RobotCoreOS 不替代 ROS 2，而是把 ROS 2 放进可维护的产品运行环境。

RobotCoreOS 不替代 Viam、Formant、Foxglove，而是给这些云层提供可信的本体 endpoint。

RobotCoreOS 不只是 OTA agent，而是绑定系统镜像、机器人应用、技能包、模型、数据、硬件 profile 和安全边界的 runtime contract。

## Product Workflow

1. 选择目标硬件：RB3 Gen 2 / QCS6490 / QCS8550 / IQ 系列 profile。
2. 烧录 RobotCoreOS golden image，绑定 SoC、BSP、kernel、driver、sensor 和 recovery profile。
3. 首次开机完成 device identity、客户归属、证书、网络和 fleet enrollment。
4. 自动验证 camera、IMU、CAN/UART/PWM、gripper、base、arm、battery、e-stop 和 accelerator。
5. 安装通过 SkillCertKit 的 policy package，记录模型 hash、输入输出、权限、安全边界和 rollback package。
6. 本地运行感知、策略、控制、安全边界、telemetry、episode capture 和日志。
7. 导出 runtime manifest：SoC、OS image、QNN/QAIRT、模型 artifact、sensor topology、latency、memory、thermal、power、rollback package。
8. 对 image、app、skill、model 和 config 做 signed OTA、staged rollout、health gate 和 A/B rollback。
9. 把失败片段、低置信度、人工接管和任务 episode 回流到 LeRobot 训练闭环。
10. 生成 SBOM、签名、发布记录、现场恢复报告和审计 bundle。

## Market

第一批客户不是“所有机器人公司”，而是最怕现场失控的人：

- 机器人 OEM VP Engineering / Platform Lead：需要 reproducible BSP + Linux + ROS + driver + OTA baseline，避免长期养发行版团队。
- 机器人 OEM Product / GM：需要降低现场故障、缩短客户部署、给企业买方一个可维护产品故事。
- 系统集成商：需要 installable image、known-good ROS/driver stack、远程支持、rollback 和项目交付模板。
- Fleet Operator / RaaS Ops：需要 uptime、remote diagnostics、device identity、telemetry、proof-of-work、staged rollout 和审计。
- Enterprise IT / Security：需要 device identity、patch SLA、SBOM/CVE、访问控制、审计日志和 fleet inventory。
- Education / Dev Kit Vendor：需要学生和开发者可以直接刷机、恢复、运行示例，而不是先修嵌入式 Linux。

## Business Model

RobotCoreOS 的定价应高于 generic IoT device management，低于完整 RobOps platform。卖点不是“便宜设备管理”，而是减少系统团队、现场返工、版本事故、集成工时和采购疑虑。

- Community：免费开发镜像、示例 profile、课程和论坛支持，用于高校、比赛、开发套件和早期评估。
- Runtime：每台机器人授权，包含 signed image、ROS 2 baseline、rollback OTA client、device identity、SBOM 和 update channel。
- Fleet：按机器人/月订阅，包含 registry、fleet groups、staged OTA、telemetry、remote diagnostics、logs、audit trail 和版本治理。
- OEM / SI：收取 board bring-up、secure boot、recovery partition、private channel、long-term ROS/Ubuntu maintenance、CI image validation 和行业模板费用。
- Enterprise Maintainability：CVE backport、SBOM export、private registry、on-prem option、SLA 和监管场景支持。

## Go-To-Market

1. 用 Qualcomm 比赛做可信样板：展示从启动、策略安装、运行、OTA 失败、自动回滚到数据回流的闭环。
2. 进入高校课程、开发者套件和比赛生态，让 RobotCoreOS 成为默认刷机环境。
3. 给系统集成商提供行业 runtime template：工厂、仓库、实验室、园区、教育和服务机器人。
4. 卖给已经有 5-50 台试点机器人的企业客户，先解决 uptime、更新、日志、现场恢复和审计。
5. 通过 Qualcomm Dragonwing ecosystem 和硬件伙伴做 reference runtime project。

## Competition

RobotCoreOS 的竞争不是单一公司，而是四类工具拼起来的临时方案：

- ROS 2：默认机器人中间件和工具生态，但不是 secure product OS、fleet updater、rollback layer 或发布证据系统。
- Ubuntu Core / Yocto / FoundriesFactory：强 OS 和嵌入式构建基础，但不定义机器人技能、ROS topic contract、LeRobot lineage、motion safety 和 runtime manifest。
- Mender / Balena：验证 A/B OTA 和设备管理是刚需，但机器人还需要 policy manifest、episode 数据、硬件 profile、SafetyOps 和 accelerator profiling。
- Viam / Formant / InOrbit：验证 fleet ops、telemetry、teleop、orchestration 和 RobOps 市场，但不是 bootable Qualcomm BSP/runtime layer。
- Foxglove：验证 robotics data、MCAP、visualization 和 log search，但不是系统镜像、OTA、driver validation 或 safety runtime。
- NVIDIA Jetson / Isaac：证明 physical AI 需要完整硬件加速和工具栈；RobotCoreOS 的差异化是 Qualcomm-native、低功耗、camera-rich、connected edge。
- 中国生态：OpenHarmony / M-Robots OS、D-Robotics TogetheROS.Bot、Unitree SDK/ROS2 说明中国市场也在推机器人 OS/中间件，但 RobotCoreOS 的切入点是 Qualcomm-first、ROS-compatible、cloud-agnostic 的商业运行底座。

## Moat

护城河来自运行证据，而不是某个功能：

- Hardware profile library：Qualcomm board、driver、camera、IO、accelerator、sensor timing、thermal 和 power 矩阵。
- Release evidence：SBOM、provenance、签名、OTA、rollback、health gate、watchdog、audit trail 和 recovery report。
- Skill compatibility graph：技能包与硬件、ROS graph、模型 runtime、输入输出、权限、安全边界和 rollback package 的兼容关系。
- Field incident memory：每次失败 OTA、传感器漂移、降频、人工接管和客户恢复，都会沉淀成下一版 runtime rule。
- Ecosystem channel：OEM、系统集成商、教育套件、行业模板和 Qualcomm developer ecosystem 的复用网络。

## Runtime Evidence Bundle

每个 golden image 都必须带 release evidence bundle：

- Golden image：immutable base OS/BSP/kernel/driver set、独立 `/data` 分区、signed image digest、board profile、factory recovery path、reproducible build log。
- Secure lifecycle：secure boot/FDE 可用性说明、device certificate、factory identity、customer enrollment、workload identity、no secrets baked into image。
- SBOM：系统、container、app、model、skill package 的 SPDX/CycloneDX，附 vulnerability scan、license report 和 VEX/exception notes。
- OTA rollback：双 boot slot、inactive slot update、signed payload、candidate marking、runtime health gate、failed boot/health 自动回滚。
- ROS lifecycle：核心 drivers、bridges、policy runner、SafetyOps 和 log service 暴露 managed lifecycle；policy execution 只在依赖 active 后启动。
- Policy admission：声明 model hash、runtime target、sensor inputs、actuator outputs、max rate、max speed/force/zone、capture hooks、rollback package。
- Telemetry：latency、FPS、memory、NPU/GPU/CPU placement、thermal、power、lifecycle transitions、safety hits、update state、rollback cause。
- Network permissions：default deny inbound、fleet/update/telemetry/time sync allowlist、ROS domain isolation、DDS/SROS 2 topic permissions。
- Data capture：manual、failure、safety event、low-confidence、operator takeover、scheduled sample 等触发器。
- Test gates：boot verification、SBOM、vulnerability threshold、signed OTA install、rollback drill、lifecycle activation、secret absence scan、telemetry export、safety fault injection、watchdog restart、hardware smoke test、edge profile benchmark。

## Why Qualcomm

Qualcomm 的机会不只是卖开发板或芯片，而是成为机器人运行底座的默认 edge target。

RobotCoreOS 让每台机器人都把 Qualcomm edge profile 写进：

- 系统镜像和 runtime manifest。
- 驱动、相机、IO、sensor timing 和 hardware validation。
- AI policy runner、QNN/QAIRT backend、AI Hub compile/profile/inference 结果。
- EdgeRuntimeBench、SkillCertKit、Fleet identity 和 release evidence。
- Demo video、developer tutorial、competition proposal 和 ecosystem reference project。

这比“项目使用 Qualcomm 板卡”更强：它让整个产品机制围绕 Qualcomm edge target 组织起来。

## Demo Storyboard

三分钟 demo：

1. 开机进入 RobotCoreOS console，展示 board profile、image digest、ROS 2 baseline 和 device identity。
2. 安装一个 LeRobot policy package，展示 model manifest、输入规格、权限、安全边界和 rollback package。
3. 运行桌面机械臂或移动底盘任务，显示 camera stream、ROS topics、latency、memory、accelerator placement。
4. 触发错误 OTA 或性能退化，health gate 阻止发布，系统回滚到上一稳定版本。
5. 导出 runtime manifest、失败 episode、SBOM、release record、NPU/温度/功耗 profile 和审计报告。

初赛可以模拟 dashboard 和本地样例流程；复赛拿到开发板后补真实 Qualcomm profile、视频、功耗、温度和稳定性数据。

## Ask

希望 Qualcomm 支持一个 6-8 周 Dragonwing validation sprint：

- RB3 Gen 2 或指定开发板。
- AI Hub / Device Cloud quota。
- QNN / QAIRT engineering office hours。
- Qualcomm Profiler 指导。
- Dragonwing Robotics Hub reference project 或 developer blog sample 机会。
- robotics / IoT ecosystem partner introduction。
- 共同定义 3 个 benchmark：vision pipeline、multi-model sensor fusion、small VLM/LLM robot assistant。

所有性能数字需经 Qualcomm review，并标注日期、SDK、板卡、散热、电源、模型版本和是否模拟。

## Claim Boundaries

可以讲：

- RobotCoreOS 降低机器人团队从 Demo 到可维护产品的工程成本。
- RobotCoreOS 提供 Qualcomm-first runtime image、OTA、rollback、identity、policy runner、SafetyOps、telemetry 和 fleet hooks。
- RobotCoreOS 让云训练结果有可验证的边缘部署路径。
- RobotCoreOS 是签名、可更新、可回滚、可观测、可审计的机器人运行镜像和发布证据流程。

避免讲：

- 已获 Qualcomm 官方认证、合作、投资或官方支持。
- 开箱支持所有机器人。
- 保证零停机或 universal secure boot。
- 替代 ROS 2、替代安全认证、替代硬实时安全控制器。
- 性能优于 Jetson、x86 或其他平台。
- 所有 Qualcomm 板卡都已经实测。

## Sources

- Qualcomm RB3 Gen 2 Development Kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm Linux：https://www.qualcomm.com/developer/software/qualcomm-linux
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm Device Cloud：https://qdc.qualcomm.com/support/user-guide/overview
- Qualcomm Profiler：https://www.qualcomm.com/developer/software/qualcomm-profiler
- Dragonwing Robotics Hub：https://www.qualcomm.com/news/onq/2026/03/how-qualcomm-dragonwing-powers-industrial-edge-ai
- ROS Noetic EOL：https://www.ros.org/blog/noetic-eol/
- ROS 2 Jazzy：https://www.openrobotics.org/blog/2024/5/ros-jazzy-jalisco-released
- ROS 2 lifecycle：https://design.ros2.org/articles/node_lifecycle.html
- ROS 2 DDS security：https://design.ros2.org/articles/ros2_dds_security.html
- LeRobot docs：https://huggingface.co/docs/lerobot/index
- Ubuntu ROS ESM：https://ubuntu.com/robotics/ros-esm
- Ubuntu Core：https://ubuntu.com/core/docs
- Yocto SBOM：https://docs.yoctoproject.org/dev/dev-manual/sbom.html
- Mender OTA：https://mender.io/engineers/how-mender-works
- Balena pricing：https://www.balena.io/pricing
- Viam fleet management：https://www.viam.com/platform/fleet-management
- Formant fleet management：https://docs.formant.io/docs/getting-started-fleet-management
- Foxglove product：https://foxglove.dev/product
- NVIDIA Isaac ROS：https://developer.nvidia.com/isaac/ros
- FIDO Device Onboard：https://fidoalliance.org/device-onboarding-overview/
- NIST SSDF：https://csrc.nist.gov/pubs/sp/800/218/final
- NIST container security：https://csrc.nist.gov/pubs/sp/800/190/final
- OpenTelemetry：https://opentelemetry.io/docs/
- MCAP spec：https://mcap.dev/spec
