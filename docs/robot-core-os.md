# RobotCoreOS Pitch

更新时间：2026-07-06。所有 Qualcomm 板卡能力、secure boot、OTA、QNN/QAIRT 性能、功耗、温度、传感器和驱动支持，必须按最终开发板、SDK、散热、电源和供应商文档重新验证。

## One-Liner

RobotCoreOS 是面向 Qualcomm Dragonwing/ARM 机器人的生产运行层：把 ROS 2 原型、LeRobot 数据闭环、AI Hub/QNN 端侧推理、签名 OTA、回滚、设备身份、SBOM、运行证据和 fleet 运维，打包成机器人公司可以继承的 commercial runtime OS。

核心叙事：

> 机器人行业已经有足够多 Demo，缺的是像 Mac/Windows 之于个人电脑一样的产品化底座。RobotCoreOS 不是替代 ROS 2，而是把 ROS 2、Qualcomm Linux、LeRobot 和云训练结果变成可交付、可更新、可回滚、可审计的机器人产品机制。

## 01 · Problem

机器人团队不是缺一个能跑起来的 Demo，而是缺从 Demo 到 10 台、100 台、1000 台客户现场机器的生产底座。

每做一款机器人，团队都会被迫重复建设：

- OS image、BSP、kernel、driver、camera、IO、NPU/GPU/CPU runtime。
- ROS 2 launch、lifecycle、topic contract、SROS2/DDS 安全配置、time sync、日志和健康检查。
- LeRobot policy 的输入输出、模型 hash、checkpoint lineage、runtime target、权限、安全边界和回滚包。
- OTA、A/B rollback、recovery mode、device identity、证书、客户归属、审计和 CVE 响应。
- 现场故障恢复、版本追溯、SBOM、provenance、企业 IT 问答和责任边界。

买方害怕的不是算法不够酷，而是：

- 谁能证明现场每台机器到底跑了哪个 image、ROS graph、模型、参数和传感器 profile？
- 如果新模型让机器人动作变差，能否自动阻止发布或回滚？
- 如果出现 CVE、驱动 bug、温度降频、传感器漂移，能否知道哪些客户受影响？
- 如果训练云在中国和海外分开，模型和数据 lineage 能否仍然可追溯？

## 02 · Current Alternatives Fail

现有工具都重要，但它们没有单独解决“Qualcomm 机器人从原型到商业队列”的完整问题。

- ROS 2 是机器人事实开发生态和中间件，但不是 secure product OS、fleet updater、rollback layer、发布证据系统或商业运行镜像。
- Qualcomm Linux、Ubuntu 24.04、Yocto、Ubuntu Core 提供 OS/BSP/长期维护基础，但不定义机器人技能、LeRobot lineage、ROS topic contract、motion safety、QNN policy artifact 和现场 incident bundle。
- Mender、RAUC、Balena、FoundriesFactory 证明签名 OTA、A/B、TUF、atomic update 和 rollback 是刚需，但它们默认不理解机器人 app、ROS graph、AI model、MCU firmware、校准 schema 和传感器拓扑的一致发布。
- Viam、Formant、InOrbit、Foxglove 证明 robot ops、fleet telemetry、数据回放和 dashboard 有付费意愿，但它们不是 bootable Qualcomm runtime image，也不负责 board profile、驱动矩阵和 QNN/QAIRT edge release。
- NVIDIA Isaac/Jetson 证明 physical AI 需要强软件栈和硬件加速，但它把生态重心放在 NVIDIA；Qualcomm 需要一个 Dragonwing-first 的等价产品化路径。
- 中国的 M-Robots/OpenHarmony、openEuler ROS、AGIROS 等说明“机器人 OS/生态”不是空白市场；RobotCoreOS 的差异化必须是 Qualcomm-first、ROS-compatible、LeRobot-ready、cloud-agnostic、可出海也可本地化。

因此，RobotCoreOS 不应该说“我们发明机器人 OS”，而应该说：我们把通用 OS、ROS 2、OTA、安全、边缘 AI、数据闭环和 fleet 运维，组装成 Qualcomm 机器人可复用的生产层。

## 03 · Solution

RobotCoreOS = Qualcomm board profile + golden image + runtime agent + ROS 2 lifecycle supervisor + LeRobot hooks + QNN/QAIRT policy runner + signed rollout + A/B rollback + evidence pack + fleet identity。

它解决的不是“写一个新内核”，而是把机器人产品化的脏活标准化：

- Board Profile：记录 SoC、BSP、kernel、driver、camera、IO、IMU/CAN/UART/PWM、accelerator、thermal、power 和 recovery capability。
- Golden Image：在 Qualcomm Linux/Ubuntu 24.04/Jazzy/Yocto 等基础上冻结可复现 image，分离 immutable base 和 robot data 分区。
- Runtime Agent：负责 device identity、fleet enrollment、health gate、watchdog、telemetry、log capture、MCAP/OTel、rollback state 和 audit trail。
- Lifecycle Supervisor：把 camera、perception、policy runner、SafetyOps、telemetry、bridge、nav/control 节点纳入 ROS 2 managed lifecycle。
- Policy Runner：把 LeRobot/ONNX/QNN_DLC/QAIRT artifact 当成可发布单元，绑定输入、输出、模型 hash、runtime target、权限、安全边界和 fallback。
- Release Evidence：每次发布都产出 SBOM、SLSA-style provenance、runtime manifest、QNN profile、ROS graph、CVE/KEV triage、rollback drill 和 incident bundle。

RobotCoreOS 不替代 ROS 2，而是把 ROS 2 产品化、托管化、安全化。它也不替代 Viam、Formant、Foxglove，而是给这些云层提供可信的本体 endpoint。

## 04 · Why Now

现在是做 RobotCoreOS 的窗口期，因为机器人行业、ROS 生态、LeRobot、Qualcomm 和合规采购同时进入生产化阶段。

- 机器人部署已经到软件基础设施阶段：IFR 报告 2024 年全球工业机器人新装约 54.2 万台，运行存量约 466.4 万台；中国占新装约 54%，存量超过 200 万台。服务机器人和 RaaS 队列也在增长。
- ROS 2 正在成为默认路线：2025 ROS Metrics 报告显示 ROS 包下载接近 9.84 亿次，ROS 2 占 91.2%，ROS 公司名单增至 1,579 家。
- ROS 2 Jazzy LTS 对齐 Ubuntu 24.04，支持到 2029 年 5 月；Humble 仍支持到 2027 年 5 月，但新一代 ARM64/Ubuntu 24.04/Qualcomm 路线应优先 Jazzy。
- LeRobot 已经把 teleop、dataset v3、policy training、HF Jobs、checkpoint lineage、rollout、DAgger/HIL 和失败片段采集串成可复用 workflow。
- Qualcomm 正在把 Dragonwing、RB3 Gen 2/QCS6490、QCS8550、IQ 系列、AI Hub、QNN/QAIRT、Device Cloud、Profiler、Qualcomm Linux 2.0 和 Robotics Hub 组合成机器人开发者生态。
- 安全和供应链证据从加分项变成采购语言：SBOM、provenance、CVE 响应、签名更新、灰度发布、审计和漏洞报告义务，会越来越早进入企业机器人采购。

过去做 RobotCoreOS 太早，因为没有足够统一的模型、数据、边缘 AI 和 fleet 需求。现在缺口变成产品机会。

## 05 · Product

RobotCoreOS 的第一版不是“通用机器人宇宙平台”，而是一个很窄但高价值的 wedge：

> 从 Qualcomm 裸板或 RobotMac Core 原型，15 分钟进入可注册、可观测、可更新、可回滚的 ROS 2/LeRobot 机器人运行环境。

产品工作流：

1. Flash：烧录 golden image，绑定 SoC、BSP、kernel、driver、传感器和 recovery profile。
2. Enroll：首次开机生成 device identity，完成客户归属、证书、网络、fleet enrollment 和 SROS2/DDS 安全材料。
3. Validate：自动验证 camera、IO、IMU、CAN/UART、急停、NPU/GPU/CPU placement、ROS lifecycle 和 thermal headroom。
4. Install：安装通过 SkillCertKit 的 policy package，记录模型 hash、输入输出、权限、安全边界和 rollback package。
5. Operate：本地执行感知、策略、控制、安全边界、telemetry、episode capture、logs 和 incident upload。
6. Profile：导出 latency、FPS、memory、accelerator utilization、温度、功耗、QNN/QAIRT backend 和 runtime manifest。
7. Update：对 OS/rootfs、ROS app、AI model、MCU firmware、校准 schema 和 config 做签名发布、灰度、健康门禁和 stop-loss。
8. Rollback：失败启动、性能退化、policy crash、安全门禁失败时回到上一稳定版本或安全模式。
9. Capture：把失败片段、低置信度、人工接管、safety hit 和 scheduled sample 回流到 LeRobot 数据闭环。
10. Audit：导出 SBOM、签名、provenance、发布记录、硬件 profile、模型 lineage 和现场恢复报告。

## 06 · Product API/Evidence

RobotCoreOS 的产品 API 不是只给开发者看的 SDK，而是给工程、运维、采购、安全和评委共同理解的 runtime contract。

示例 manifest：

```yaml
robotcore:
  board_profile:
    soc: qcs6490
    base_os: ubuntu_24_04_or_qualcomm_linux
    ros_distro: jazzy
    cameras: [front_rgbd, wrist_rgb]
    accelerators: [cpu, gpu, npu_qnn]
  policy:
    format: lerobot_or_onnx_or_qnn_dlc
    model_hash: sha256:...
    inputs: [camera.front, joint_state, gripper_state]
    outputs: [arm_command, gripper_command]
    max_rate_hz: 30
    safety_boundary: desktop_arm_pick_place_v1
  release:
    sbom: spdx_or_cyclonedx
    provenance: slsa_style
    rollout: canary_1_10_100
    rollback_slot: B
    health_gate: latency_p95_and_safety_hits
```

每次 release evidence bundle 必须包含：

- Golden image digest、board profile、driver matrix、factory recovery path、reproducible build log。
- Device identity、certificate enrollment、SROS2/DDS permission notes、network allowlist、no-secrets scan。
- SPDX/CycloneDX SBOM、license report、CVE/KEV triage、VEX/exception notes。
- Signed OTA payload、A/B or OSTree update state、candidate marking、health gate、rollback cause。
- ROS 2 graph、managed lifecycle transitions、watchdog events、SafetyOps hits、topic permission summary。
- LeRobot dataset/policy lineage、checkpoint revision、model artifact hash、QNN/QAIRT compile/profile metadata。
- MCAP/ROS bag/OTel export、latency/FPS/memory/power/thermal/accelerator placement、incident replay link。

这份 evidence bundle 是 RobotCoreOS 的核心产品资产：它让客户相信机器人不是一次性 Demo，而是可运营资产。

## 07 · Market & Business Model

第一批客户不是“所有机器人公司”，而是最怕现场失控的人：

- 10-1000 台规模的机器人 OEM：需要可复现的 BSP、Linux、ROS、driver、OTA baseline，避免长期养发行版团队。
- 系统集成商：需要 installable image、known-good ROS/driver stack、远程支持、rollback 和项目交付模板，保护项目毛利。
- RaaS/fleet operator：需要 uptime、remote diagnostics、device identity、telemetry、proof-of-work、staged rollout 和审计。
- 企业 IT / 安全：需要 device identity、patch SLA、SBOM/CVE、访问控制、审计日志和 fleet inventory。
- 教育、比赛、开发套件厂商：需要学生和开发者可以直接刷机、恢复、运行 ROS/LeRobot 示例，而不是先修嵌入式 Linux。

商业模式：

- Community：免费开发镜像、示例 profile、课程、比赛模板和论坛支持，获取高校、开发套件和早期生态。
- Runtime License：按设备授权，包含 signed image、ROS 2 baseline、rollback OTA client、device identity、SBOM 和 update channel。
- Fleet Subscription：按机器人/月订阅，包含 registry、fleet groups、staged OTA、telemetry、remote diagnostics、logs、audit trail 和版本治理。
- OEM / SI Bring-Up：收取 board profile、driver integration、secure boot/OTA/recovery partition、private channel、CI image validation 和行业模板费用。
- Enterprise / China Private Deployment：私有化、数据驻留、CVE backport、SBOM export、on-prem registry、SLA 和行业合规支持。

市场叙事不应该把 TAM 写成整个机器人硬件市场。更可信的说法是：RobotCoreOS 赚的是机器人软件基础设施、设备管理、release evidence、fleet ops 和板级 productization 的钱。

## 08 · Competition & Moat

竞争不是一个公司，而是客户今天用来拼凑生产化的七类替代方案：

- 自建脚本和 SSH：便宜、快，但不可审计、不可复制、不可灰度、不可解释给企业客户。
- ROS 2 原生工程：生态强，但缺生产发布、fleet identity、OTA、evidence 和客户现场恢复机制。
- Embedded Linux/Ubuntu Core/Yocto/Foundries：系统基础强，但不天然理解 robot skill、LeRobot lineage、ROS graph、QNN artifact 和 safety assumptions。
- Mender/Balena/RAUC：OTA 可靠，但不负责机器人多组件一致发布和 AI policy admission。
- Viam/Formant/InOrbit/Foxglove：RobOps/data/fleet 强，但不是 Qualcomm bootable runtime layer。
- NVIDIA Isaac/Jetson：强平台级对手，尤其在大模型和 CUDA 生态上领先；RobotCoreOS 必须用 Qualcomm 低功耗、多摄像头、连接、端侧隐私和 Dragonwing 生态打差异化。
- 中国机器人 OS/生态：说明市场正在形成，但也要求 RobotCoreOS 提供本地云、私有化、中文开发者生态和国产供应链叙事。

护城河来自运行证据和兼容图谱，而不是一个 dashboard：

- Qualcomm board profile library：QCS6490、QCS8550、IQ 系列、driver、camera、IO、accelerator、thermal、power 和 recovery 矩阵。
- Hardware CI and benchmark memory：每次 SDK、kernel、driver、QNN、ROS 包、policy runtime 变化都留下可比较 profile。
- Release evidence graph：SBOM、provenance、签名、OTA、回滚、health gate、watchdog、audit trail 和 recovery report。
- Skill compatibility graph：技能包与硬件、ROS graph、模型 runtime、输入输出、权限、安全边界和 rollback package 的兼容关系。
- Field incident memory：失败 OTA、传感器漂移、温度降频、人工接管、客户恢复都会变成下一版 runtime rule。
- Ecosystem channel：RobotMac Core、BoardBringupKit、EdgeRuntimeBench、SkillCertKit、SafetyOps、PilotContractKit 共同形成从硬件到交付的产品族。

## 09 · Why Qualcomm

Qualcomm 的机会不只是让比赛项目“使用一块开发板”，而是让 Dragonwing 成为机器人技能的默认边缘目标。

RobotCoreOS 对 Qualcomm 的价值：

- 把 Dragonwing 的低功耗、多摄像头、连接、端侧 AI 和 industrial edge 定位，翻译成开发者可直接使用的 runtime product。
- 把 AI Hub、QNN/QAIRT、Device Cloud、Profiler、Qualcomm Linux、Robotics Hub 接成从训练 artifact 到边缘发布证据的闭环。
- 让每个 demo 都输出 Qualcomm edge profile：latency、memory、FPS/W、thermal headroom、accelerator placement、rollback evidence。
- 给 Qualcomm 生态一个可发布的 reference runtime project，而不是只有单点 sample code。
- 在中国和海外两个版本中同时讲清楚：端侧推理、云端训练、数据驻留、企业私有化和跨云模型 lineage。

对 Qualcomm 的请求应该具体：

- 90 天 Dragonwing validation sprint。
- RB3 Gen 2 Vision Kit、QCS8550 kit，或 IQ 系列 Robotics Reference Design 的 loaner/early access。
- AI Hub、Device Cloud、QNN/QAIRT、Qualcomm Profiler 的 quota 和 office hours。
- Qualcomm Linux 2.0 / Yocto / Ubuntu 24.04 路线 review。
- 允许把 RobotCoreOS demo 做成 Dragonwing Robotics Hub reference project 或 developer tutorial。
- 引荐 Thundercomm、Advantech、Edge Impulse、系统集成商或教育套件伙伴。

## 10 · Demo & Ask

三分钟 Demo 要证明一件事：这不是 Demo 机器，而是可交付机器。

Demo storyboard：

1. Boot：开发板启动 RobotCoreOS console，展示 board profile、image digest、ROS 2 Jazzy baseline、device identity 和 SROS2/DDS status。
2. Enroll：设备进入 fleet dashboard，自动生成 runtime manifest 和初始 health check。
3. Run：安装一个 LeRobot/ACT policy package，走 AI Hub/QNN profile，运行桌面机械臂或移动底盘任务，展示 camera、ROS topics、latency、memory、NPU placement。
4. Fail：推送一个会 crash 或延迟超标的 ROS/policy 更新，canary health gate 失败，系统停止 rollout 并回滚到上一稳定 slot。
5. Capture：把失败 episode、MCAP/OTel、rollback cause、QNN profile 和 safety hits 回流到训练队列。
6. Export：导出 SBOM、provenance、runtime manifest、release record、CVE impact view、demo video 和评委版 evidence bundle。

初赛可以先用模拟 dashboard、本地样例流程和已有资产证明闭环；复赛拿到开发板后补真实 Qualcomm profile、视频、功耗、温度、延迟和稳定性数据。

比赛提交的 ask：

- 初赛：项目书、中文 pitch website、architecture diagram、demo storyboard、claim boundaries、source-backed market analysis。
- 复赛：真实 board profile、RobotCoreOS prototype、QNN/QAIRT benchmark、OTA rollback drill、LeRobot episode loop、evidence export。
- 高通生态：联合验证三个 benchmark：vision pipeline、multi-model sensor fusion、small VLM/LLM robot assistant。

## Claim Boundaries

可以讲：

- RobotCoreOS 降低机器人团队从 ROS/LeRobot Demo 到可维护产品的工程成本。
- RobotCoreOS 提供 Qualcomm-first runtime image、device agent、policy runner、OTA、rollback、identity、telemetry、SBOM 和 release evidence。
- RobotCoreOS 让云训练结果有可验证的边缘部署路径。
- RobotCoreOS 是签名、可更新、可回滚、可观测、可审计的机器人运行镜像和发布证据流程。

避免讲：

- 已获 Qualcomm 官方认证、合作、投资或官方支持。
- 已支持所有 Qualcomm/Dragonwing 芯片、所有机器人和所有传感器。
- secure boot、FBE、attestation 在所有板卡上开箱可用。
- 保证零停机、硬实时、安全认证、ASIL/SIL 或替代安全控制器。
- 所有 LeRobot/VLA 模型都能直接跑 Qualcomm NPU。
- 性能全面优于 Jetson、x86 或其他平台。
- edge training。更准确是云端/GPU 训练，Qualcomm 端侧推理。

## Sources

- Qualcomm Dragonwing robotics technologies：https://www.qualcomm.com/news/releases/2026/01/qualcomm-introduces-a-full-suite-of-robotics-technologies-power
- Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Qualcomm RB3 Gen 2 / QCS6490 product brief：https://docs.qualcomm.com/doc/87-28733-1/87-28733-1_REV_F_QUALCOMM_QCS6490_QCM6490_Processors_Product_Brief.pdf
- Qualcomm QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Qualcomm Linux：https://www.qualcomm.com/developer/software/qualcomm-linux
- Qualcomm Linux 2.0：https://www.qualcomm.com/developer/blog/2026/06/qualcomm-linux-2-now-available
- Qualcomm Secure Boot：https://docs.qualcomm.com/bundle/publicresource/topics/80-70017-11/secure-boot.html
- Qualcomm OTA / OSTree：https://docs.qualcomm.com/bundle/publicresource/topics/80-70023-27/update_fw_and_os_qualcomm_linux_using_capsule_and_ostree_mechanisms.html
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm ACT model：https://huggingface.co/qualcomm/ACT
- Qualcomm Device Cloud / Edge Impulse RB3 Gen 2：https://www.qualcomm.com/developer/blog/2025/03/powering-iot-developers-with-edge-ai-qualcomm-rb3-gen2-kit-now-integrated-with-edge-impulse
- ROS 2 Jazzy：https://www.openrobotics.org/blog/2024/5/ros-jazzy-jalisco-released
- ROS 2 lifecycle：https://github.com/ros2/demos/blob/rolling/lifecycle/README.rst
- ROS 2 DDS security：https://design.ros2.org/articles/ros2_dds_security.html
- ROS Metrics 2025：https://discourse.openrobotics.org/t/2025-ros-metrics-report/52575
- LeRobot docs：https://huggingface.co/docs/lerobot/en/index
- LeRobot dataset v3：https://huggingface.co/docs/lerobot/lerobot-dataset-v3
- LeRobot inference：https://huggingface.co/docs/lerobot/main/inference
- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Ubuntu Core：https://documentation.ubuntu.com/core/
- Ubuntu Core 26：https://canonical.com/blog/canonical-launches-ubuntu-core-26
- Mender pricing：https://mender.io/pricing/plans
- RAUC basics：https://rauc.readthedocs.io/en/latest/basic.html
- Balena pricing：https://www.balena.io/pricing
- FoundriesFactory：https://www.qualcomm.com/developer/software/foundriesfactory
- Viam pricing：https://www.viam.com/pricing
- Formant：https://formant.io/
- InOrbit FAQ：https://www.inorbit.ai/faq
- Foxglove pricing：https://foxglove.dev/pricing
- Foxglove data：https://docs.foxglove.dev/docs/data
- NVIDIA Isaac ROS：https://developer.nvidia.com/isaac/ros
- NVIDIA Jetson Thor：https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- MCAP：https://mcap.dev/guides
- OpenTelemetry：https://opentelemetry.io/docs/what-is-opentelemetry/
- SLSA v1.2：https://slsa.dev/spec/v1.2/
- NIST SSDF：https://csrc.nist.gov/projects/ssdf
- EU Cyber Resilience Act：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
