# 机御 Zero Pitch

更新时间：2026-07-05。网络安全、OT 安全、机器人安全、数据合规和远程运维要求变化很快；真实交付前必须按目标市场、客户等级、机器人类型和部署网络重新做威胁建模与合规复核。

## Core Thesis

机御 Zero 是面向机器人机群的动作级零信任安全平台：

> 把零信任从“谁能访问系统”推进到“谁能让机器人动、能动到哪里、在什么状态下能动、动完如何取证”。

它不是通用 OT 安全仪表盘，也不是机器人杀毒软件。它解决的是具身智能商业化里的新问题：

- 机器人不只是联网设备，它会移动、抓取、搬运、靠近人和连接产线。
- ROS / DDS 节点、远程运维、OTA、模型、传感器、PLC、WMS/MES、微信工单和云训练都可能影响真实动作。
- 企业采购正在从“能不能跑”转向“身份、固件、远程访问、漏洞、日志、数据和动作是否可信”。
- Qualcomm 的安全启动、硬件身份、边缘 AI、连接和本体实时能力，适合做机器人信任根。

一句话：机御 Zero 让每台机器人、每个节点、每条运动指令都先验证、再执行、可追溯。

## Five-Thread Research Synthesis

### 1. Regulation And Threat Landscape

机器人安全正在从可选能力变成产品生命周期和市场准入要求：

- EU CRA 已于 2024-12-10 生效；2026-09-11 起漏洞和严重事件报告义务开始适用；2027-12-11 主要产品义务开始适用。
- NIST SSDF、NIST IoT、NIST OT、CISA Secure by Design / Secure by Demand 和 ISA/IEC 62443 正在成为采购语言。
- ROS 2 / DDS 支持安全机制，但不是默认自动安全。
- 机器人漏洞、远程访问暴露和 OT 勒索已经是真实业务连续性风险。

安全表述：支持合规准备、对齐安全工程框架、降低风险；不说“保证合规”或“完全防黑客”。

### 2. Market And Competitors

OT/IoT 安全正在向 CPS / xOT exposure management 集中：

- Claroty、Nozomi、Dragos、Armis、Forescout、Microsoft Defender for IoT、AWS IoT Device Defender 解决资产、网络、暴露、威胁和 SOC 工作流。
- Alias Robotics 等机器人安全团队强调 robot-native threat model、ROS 图、运动、远程控制和传感器风险。
- 市场已经有通用 OT 可视化平台；Qualcomm 的机会是让机器人在被这些平台看到之前，先有硬件根、ROS 图、动作策略和证据链。

### 3. Zero Trust Architecture

核心规则：

> 机器人、ROS 节点、操作员、更新包和网络路径，都必须证明身份与状态，才获得权限。

架构流：

1. RobotCoreOS 在 Qualcomm edge 上启动，验证 boot chain，采集 measurement。
2. TrustAnchorAgent 输出 attestation evidence。
3. CertForge 验证证据，签发短期 device / workload / SROS2 / operator session 证书。
4. SafetyOps 作为 policy decision layer，处理 JIT access、远程命令、异常响应和 quarantine。
5. RiskLedger 保存 SBOM、VEX、漏洞、例外、证据和 fleet risk posture。
6. UptimeOS 处理 signed OTA、canary、health gate、rollback 和服务工单。

### 4. China Lane

中国版不能只讲设备安全，要按“联网设备 + 工业互联网节点 + 数据处理系统 + 售后服务系统”设计：

- 网络安全法、数据安全法、个人信息保护法、网络数据安全管理条例。
- MLPS 2.0：云、移动互联、物联网、工业控制等扩展要求。
- GB/T 39404-2020 工业机器人控制单元信息安全通用要求。
- GB/T 45502-2025 服务机器人信息安全通用要求。
- 中国数据默认留在中国；地图、视频、语音、工单、日志、训练样本要做分级、脱敏、审批和留痕。
- 远程维护默认关闭、工单审批、限时授权、MFA、堡垒机、会话录屏、命令审计和客户一键断开。

### 5. Product Positioning

名称：机御 Zero / MotionZero。

核心新意：

- 不是“OT 资产扫描”。
- 不是“机器人杀毒”。
- 是 Motion-Level Zero Trust：谁能让机器人动，能动到哪里，什么状态能动，谁签了授权，哪里被拦截，如何回放证据。

## Product Modules

### 1. Robot Passport

- 设备身份、Qualcomm SKU、secure boot 状态、firmware / OS / rootfs hash。
- ROS graph hash、SROS2 enclave、证书状态、SBOM / VEX、OTA ring。
- 站点、区域、数据驻留、服务合同和远程访问策略。

### 2. ROS / DDS Least Privilege

- 按 enclave 管 topic / service / action 权限，而不是只看主机 IP。
- navigation 节点可发布 `/odom`、订阅 `/scan`，但不能发布 `/cmd_vel`，除非证书、任务和策略允许。
- 自动生成 DDS governance / permissions、证书轮换和过期拒绝。

### 3. Motion Firewall

- 对速度、抓取、升降、转向、靠近人、越区、禁区和远程接管做策略检查。
- 结合身份、任务、地图、现场状态、传感器置信度、SafetyOps 权限和风险等级。
- 异常时不直接“黑屏停机”，而是限速、降级、拒绝高风险动作或进入 quarantine。

### 4. JIT Remote Access

- 默认无入站 SSH；远程访问走工单审批和短期证书。
- MFA、RBAC、session recording、命令 allowlist、文件传输审计和 break-glass 绑定事件。
- 支持 ServiceNow / Jira / 中国工单门户 / 企微入口，但日志和附件进入受控工单系统。

### 5. Signed OTA And SBOM

- TUF / Uptane 风格签名元数据。
- OS、应用、ROS 包、模型、skill、calibration 分层发布。
- canary、health gate、rollback、防回滚、SBOM / VEX、CertForge 合规证据。

### 6. SOC Export

- 向 Sentinel、Splunk、Defender、ServiceNow、Claroty / Nozomi / Dragos、国内 SIEM / SOC 输出 robot-native 事件。
- 事件包括 attestation failed、DDS authz denied、rogue publisher、remote access started、unsafe motion blocked、OTA rollback 和 certificate expired。

## Demo

比赛演示可以做一条机器人攻防闭环：

1. 两台机器人启动：一台 measurement 正常，一台 rootfs 被篡改。
2. CertForge 拒绝篡改机器人证书，SafetyOps 放入 quarantine。
3. 攻击者模拟 ROS 节点发布 `/cmd_vel` 或远程抓取命令。
4. Motion Firewall 判断身份不可信、任务不匹配、动作越界，拦截危险动作。
5. 机器人进入安全降级：停止危险动作、保留低风险读数据和取证。
6. RiskLedger 回放证据链：谁发起、哪个节点、哪个证书、为什么拒绝、如何恢复。
7. UptimeOS 发起 signed OTA 恢复，canary health gate 通过后重新入队。

## China / Overseas Positioning

中国版：

- MLPS 支持包、PIPL / DSL 数据清单、国内云/私有化部署、中文隐私政策。
- 国内工单、400、企微/小程序服务治理、远程运维审批留痕。
- SRRC / CCC / NAL 准入判断和安全资料交接。
- 默认本地自治，云端不直接控制安全关键链路。

海外版：

- EU CRA readiness、NIST SSDF、NIST OT、IEC 62443、SOC 2 / ISO 27001 evidence。
- Defender / Sentinel / Splunk / ServiceNow / AWS IoT / Claroty / Nozomi / Dragos integrations。
- SBOM/VEX、VDP/PSIRT、security.txt、signed OTA、JIT remote access、tenant isolation。

## Qualcomm Value

机御 Zero 是 Qualcomm 机器人生态的安全底座：

- Secure Boot / root of trust：把机器人身份建立在硬件和启动链上。
- QTEE / SPU / crypto：保护密钥、证书、measurement 和签名操作。
- Edge AI：本体侧检测异常动作、命令/里程计不一致、传感器伪造和远程接管异常。
- Connectivity：5G / Wi-Fi / BLE / 专网安全遥测和远程运维。
- AI Hub / QNN：模型哈希、runtime profile 和 release evidence 进入机器人护照。

一句话：

> Qualcomm 不只是让机器人计算更快，还可以让机器人每一次动作更可信。

## Claims To Avoid

- 不说“完全防止黑客/勒索/误动作”。
- 不说“已通过 EU CRA / IEC 62443 / 等保认证”。
- 不说替代 safety controller 或 functional safety。
- 不说 ROS 2 开启后天然安全。
- 不做无审批远程控制、隐藏远控或 AI 自动修复生产系统。

## Sources

- EU CRA：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- EUR-Lex CRA：https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202402847
- NIST SSDF：https://csrc.nist.gov/pubs/sp/800/218/final
- NIST OT Security：https://csrc.nist.gov/pubs/sp/800/82/r3/final
- CISA OT procurement guide：https://media.defense.gov/2025/Jan/13/2003626906/-1/-1/0/JOINT-GUIDE-SECURE-BY-DEMAND-PRIORITY-CONSIDERATIONS-OT-OWNERS-OPERATORS.PDF
- ISA/IEC 62443：https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
- ROS 2 DDS Security：https://design.ros2.org/articles/ros2_dds_security.html
- ROS 2 threat model：https://design.ros2.org/articles/ros2_threat_model.html
- Universal Robots CVE-2026-8153：https://www.universal-robots.com/articles/ur/cybersecurity/cve-2026-8153-command-injection-in-the-polyscope-5-dashboard-server/
- Dragos 2026 OT cybersecurity review：https://www.dragos.com/blog/dragos-2026-ot-cybersecurity-year-in-review
- Claroty：https://claroty.com/
- Nozomi Networks：https://www.nozominetworks.com/platform
- Alias Robotics：https://aliasrobotics.com/
- SPIFFE：https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
- The Update Framework：https://theupdateframework.io/
- Uptane：https://uptane.org/docs/latest/standard/uptane-standard
- Qualcomm secure boot：https://www.qualcomm.com/developer/blog/2024/12/secure-boot-as-part-of-platform-security-architecture-modern-system-on-chip
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- 中国网络安全法修正：https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm
- 数据安全法：https://www.cac.gov.cn/2021-06/11/c_1624994566919140.htm
- 个人信息保护法：https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm
- 网络数据安全管理条例：https://www.gov.cn/zhengce/zhengceku/202409/content_6977767.htm
- GB/T 39404-2020：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=57E45D47E1A9C3C053C546B18DFB1BEA
- GB/T 45502-2025：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=9E2B74F7423F548D405996E62937064A
