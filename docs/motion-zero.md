# 机御 Zero Pitch

更新时间：2026-07-06。网络安全、OT 安全、机器人安全、数据合规和远程运维要求变化很快；真实交付前必须按目标市场、客户等级、机器人类型和部署网络重新做威胁建模与合规复核。

## One-Line Pitch

机御 Zero 是机器人动作级零信任平台：

> 远程运维能不能让机器人动，动了谁负责，出事后能不能回放。

它不是通用 OT 安全大屏，也不是机器人杀毒软件。它把机器人、ROS/DDS 节点、操作员、更新包、模型、地图和远程会话都绑定到硬件根身份与运行时策略上，让每一次高风险动作先验证、再执行、可追溯。

## Required Deck Spine

### 01 · Problem

机器人安全的终点不是网络访问，而是物理动作。

- AMR、协作臂、服务机器人和巡检机器人会移动、抓取、升降、靠近人、进出门梯和连接产线。
- ROS/DDS 节点、远程运维、OTA、模型、标定、地图、WMS/MES 和云训练都可能影响真实动作。
- 客户要问的是：谁能发布 `/cmd_vel`、抓取、轨迹、地图、OTA 或接管命令？为什么被允许？出事后如何回放？
- 普通日志很难回答身份、证书、策略、上下文、拒绝原因、远程会话和恢复路径。

### 02 · Current Alternatives Fail

现有工具各管一层，但没有把“机器人动作”作为授权对象。

- VPN / bastion：证明谁能登录，不证明这次会话能不能让机器人动。
- OT/xOT security：Claroty、Nozomi、Dragos、Armis、Forescout、Defender for IoT 擅长资产、流量、暴露面和 SOC 工作流，但通常不做动作前 ROS/DDS 语义授权。
- ROS 2 / DDS Security：提供 authentication、access control 和 crypto primitives，但企业还需要 fleet policy、证书生命周期、策略编译、运行时门禁和 SOC evidence。
- Safety controller：保护功能安全底线，但不负责软件供应链、远程访问审批、SBOM/VEX、OTA 和客户审计。
- OTA / SBOM tools：证明包和组件状态，但没有把漏洞状态、更新状态与机器人当前动作权限联动。

### 03 · Solution

机御 Zero 是机器人动作级零信任证据层。

架构：

1. Qualcomm secure boot / hardware root 采集启动链、rootfs、firmware、ROS graph、model/QNN profile 和 policy hash。
2. Robot Passport 记录机器人身份、站点、数据区域、SBOM/VEX、OTA ring、远程访问策略和最近风险状态。
3. SafetyOps 策略编译成 DDS governance、SROS2 enclave、topic/service/action 权限和现场动作边界。
4. Motion Firewall 在动作发生前结合身份、任务、地图、人距、传感器、网络、电池、热状态和风险等级做 allow / limit_speed / require_approval / deny / quarantine。
5. RiskLedger 记录证书、命令、策略、拒绝原因、远程会话、OTA receipt 和恢复路径。
6. SOC Export 把 robot-native 事件输出给 Sentinel、Splunk、ServiceNow、Claroty、Nozomi、Dragos、国内 SIEM / SOC 和客户审计包。

### 04 · Why Now

机器人规模、远程运维和监管时间表同时把动作级零信任推到台前。

- IFR 报告 2024 年全球工业机器人在役量约 466.4 万台；中国新增安装约 29.5 万台，继续是最大市场。
- IFR 报告 2024 年专业服务机器人接近 20 万台，物流/运输是最大类别之一。
- EU CRA 已于 2024-12-10 生效；漏洞和严重事件报告义务从 2026-09-11 开始；主要产品义务从 2027-12-11 开始。
- NIST SSDF、NIST OT、NIST Zero Trust、IEC 62443、CISA Secure by Design / Secure by Demand 正在进入企业采购语言。
- 中国客户还会要求 MLPS-style evidence、PIPL/DSL 数据清单、网络数据安全、远程运维审批、数据驻留和工业/服务机器人信息安全材料。
- 机器人控制器漏洞和远程访问风险正在变成业务连续性、质保、保险和出口问题。

### 05 · Product

第一版做两个商业形态：

- `机御 Zero OEM Embedded`：SDK/agent 给 robot OEM。包括 robot passport、secure boot / attestation hooks、ROS/DDS least privilege、motion firewall、signed OTA、SBOM/VEX、PSIRT evidence。商业模式：NRE + per-robot royalty/subscription。
- `机御 Zero Site/Fleet Gateway`：edge appliance 或私有化 SaaS 给仓库、工厂、医院、能源、RaaS fleet。包括 JIT vendor access、session recording、SOC/SIEM export、motion-event replay、WMS/MES/CMMS connectors、insurer/audit reports。商业模式：4-8 周付费 pilot + per-site + per-robot subscription。

核心模块：

- Robot Passport：设备身份、Qualcomm SKU、secure boot、firmware / OS / rootfs hash、ROS graph hash、SROS2 enclave、SBOM/VEX、OTA ring、站点和数据区域。
- ROS/DDS Least Privilege：按 enclave 管 topic / service / action；高风险 publishers 单独证书和策略。
- Motion Firewall：速度、抓取、升降、转向、越区、靠近人、远程接管和禁区进入都经过策略检查。
- JIT Remote Access：默认无入站 SSH；工单审批、MFA、短期证书、命令 allowlist、会话录屏和文件传输审计。
- Signed OTA：TUF/Uptane 风格 metadata、A/B slot、canary、health gate、防回滚、rollback receipt。
- SBOM/VEX：SPDX / CycloneDX / OpenVEX 状态进入机器人运行策略。

### 06 · Product API

关键对象：

- `RobotPassport`: robot_id、owner、site、chip_target、boot_state、rootfs_hash、ros_graph_hash、model_hash、sbom_digest、ota_ring。
- `MotionAuthorize`: subject、topic/action、task_id、zone、human_distance、sensor_health、network_state、policy_version、decision。
- `RemoteAccessGrant`: ticket、operator、MFA、short_cert、allowed_commands、recording_ref、break_glass_reason。
- `OTARelease`: targets metadata、snapshot、timestamp、A/B slot、canary gate、rollback receipt、anti_rollback。
- `VEXPolicy`: affected、not_affected、fixed、under_investigation、robot rings、motion restrictions、expiry。
- `SOCEvent`: attestation.failed、dds.authz.denied、rogue.publisher、unsafe_motion.blocked、jit.session.started、ota.rollback。

示例：

```yaml
motion_authorize.v1:
  robot_id: mz-rb3-042
  command: {type: base_velocity, topic: /cmd_vel, vx: 0.8, wz: 0.2}
  subject: {kind: ros_node, spiffe_id: spiffe://motionzero/site-a/nav2}
  context: {task_id: dock_778, zone: judge_table, human_distance_m: 0.9}
  evidence: {passport_id: rp_042, attestation: trusted, policy: safetyops_17}
  decision: {action: limit_speed, max_vx: 0.25, reason: human_distance_below_policy}
```

### 07 · Market & Business Model

第一批买家：

- Robot OEM：VP Product、Security、PSIRT、Compliance、field service。
- Enterprise operator：CISO、OT security、plant GM、automation director、warehouse operations。
- System integrator：project director、managed service owner、commissioning risk owner。
- Insurer / warranty：risk engineering、claims、product liability、SLA owner。

预算线：

- OEM：product security、PSIRT、CRA/CE/Machinery preparation、OTA platform、field service、warranty reserve。
- Operator：OT security、ZTNA/PAM/vendor access、SOC/SIEM、robot fleet management、cyber insurance、safety/compliance。
- SI：commissioning package、remote support、managed service SLA。

Pricing hypothesis:

- China OEM Embedded：人民币 100-500 / controller 一次性 + 人民币 2-10 / robot / month。
- China Site/Fleet Gateway：人民币 20k-80k / site-year 起；企业私有化人民币 100k-500k / year。
- Overseas OEM Embedded：$100-500 / robot one-time/NRE/royalty + $1-5 / robot / month。
- Overseas Operator SaaS：$10-50 / robot / month 基础身份/OTA/SOC；$50-150 / robot / month 高风险命令授权、会话录制和 compliance pack；site minimum $25k-75k / year。

### 08 · Competition & Moat

定位句：

> Claroty 可以告诉你机器人暴露了；机御 Zero 决定它现在能不能动。

竞争地图：

- OT/CPS platforms：Claroty、Nozomi、Dragos、Armis、Forescout、Microsoft Defender for IoT、AWS IoT Device Defender。
- Robot-native security：Alias Robotics/RIS 等。
- ROS 2 / SROS2 / DDS Security：机器人通信安全 primitives。
- Workload identity：SPIFFE/SPIRE、Teleport Machine Identity。
- Remote access / ZTNA：Tailscale SSH、Teleport、Cloudflare Access、AWS SSM Session Manager。
- OTA / signed update：TUF、Uptane、Foundries.io、Torizon 等。
- SBOM/VEX：SPDX、CycloneDX、OpenVEX、Dependency-Track、Syft/Grype。

壁垒：

- Qualcomm hardware-rooted Robot Passport。
- ROS/DDS graph hash 与 least-privilege policy compiler。
- Motion Firewall 结合身份、任务、地图、现场状态、传感器置信度和安全策略。
- RiskLedger 形成 motion decision corpus、insurance evidence、warranty evidence 和 LeRobot failure-mining 数据。
- China/overseas 双 lane：同一 schema，不同数据驻留、工单、SOC、合规和云训练接入。

### 09 · Why Qualcomm

Qualcomm 不能只被定义成算力供应商。机御 Zero 把 Qualcomm 变成机器人动作可信根。

- Secure Boot / root of trust：把机器人身份建立在硬件和启动链上。
- QTEE / SPU / crypto：保护密钥、证书、measurement 和签名操作。
- Edge AI：本体侧检测命令/里程计不一致、传感器异常、远程接管异常和 model drift。
- Connectivity：5G / Wi-Fi / BLE / 专网安全遥测和远程运维。
- AI Hub / QNN：模型 hash、runtime profile、latency evidence 和 release record 进入机器人护照。

一句话：

> Qualcomm 不只是让机器人计算更快，还可以让机器人每一次动作更可信。

### 10 · Demo & Ask

5-8 分钟演示：

1. 买方痛点：企业不怕机器人不聪明，怕不知道谁能让它动。
2. 注册两台机器人；一台 trusted，一台 rootfs / ROS graph measurement 异常。
3. 篡改机器人无法拿到短期 DDS 证书，被 SafetyOps 标记 quarantine。
4. rogue node 发布 `/cmd_vel` 或 gripper 命令；DDS deny first，Motion Firewall deny/limit second。
5. JIT remote access 会话批准后只允许 diagnostics，拒绝 raw motion 和未签名 OTA。
6. UptimeOS stages signed OTA，health gate pass，机器人重新进入 canary ring。
7. RiskLedger 回放证据：boot hash、cert decision、blocked motion、operator session、OTA rollback。
8. 导出 SOC JSON、RiskLedger bundle、OTA receipt、Judge Audit Pack，并切换中国/海外 lane 展示数据驻留。

对 Qualcomm 的请求：

- 比赛开发板和 secure boot / attestation profile。
- QNN / AI Hub model evidence hook。
- 一家 robot OEM 或仓库/工厂/医院/能源现场 pilot。
- 协助把 Robot Passport 变成 Qualcomm robot ecosystem 的标准接口。

## China / Overseas Positioning

中国版：

- 国内控制面/存储，默认视频、音频、地图、日志、工单、训练样本和 operator session 留在中国境内。
- MLPS-style evidence、PIPL/DSL 数据清单、网络数据安全、GB/T 39404、GB/T 45502、远程运维审批、会话录屏、客户一键断开。
- 企微/工单/400/小程序服务治理，国内云或私有化 GPU 训练，原始数据跨境默认关闭。

海外版：

- EU CRA readiness、NIST SSDF、NIST OT、NIST ZTA、IEC 62443、SOC 2 / ISO 27001-style evidence。
- VDP/PSIRT、SBOM/VEX、signed OTA、JIT remote access、tenant isolation、Splunk/Sentinel/ServiceNow/Claroty/Nozomi/Dragos export。
- US/EU regional tenants，RunPod/Lambda/AWS/Hugging Face LeRobot training lane，但训练云只能产出签名 model/skill package，不能绕过边缘 Motion Firewall。

## Claim Guardrails

- 不说“完全防止黑客/勒索/误动作”。
- 不说“已通过 EU CRA / IEC 62443 / 等保认证”。
- 不说替代 safety controller、Safety PLC 或 functional safety。
- 不说 ROS 2 开启后天然安全。
- 不说 SBOM 单独解决供应链风险。
- 不做无审批远程控制、隐藏远控或 AI 自动修复生产系统。

## Sources

- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- EU CRA：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- CRA reporting：https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
- NIST SSDF：https://csrc.nist.gov/pubs/sp/800/218/final
- NIST OT Security：https://csrc.nist.gov/pubs/sp/800/82/r3/final
- NIST Zero Trust：https://csrc.nist.gov/pubs/sp/800/207/final
- CISA Secure by Design：https://www.cisa.gov/securebydesign
- CISA remote access guide：https://www.cisa.gov/resources-tools/resources/guide-securing-remote-access-software
- ISA/IEC 62443：https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
- ROS 2 DDS Security：https://design.ros2.org/articles/ros2_dds_security.html
- ROS 2 access control：https://design.ros2.org/articles/ros2_access_control_policies.html
- ROS 2 threat model：https://design.ros2.org/articles/ros2_threat_model.html
- OMG DDS Security：https://www.omg.org/spec/DDS-SECURITY/1.2/About-DDS-SECURITY
- Universal Robots CVE-2026-8153：https://www.universal-robots.com/articles/ur/cybersecurity/cve-2026-8153-command-injection-in-the-polyscope-5-dashboard-server/
- Claroty asset inventory：https://claroty.com/platform/asset-inventory
- Nozomi Guardian：https://www.nozominetworks.com/platform/guardian
- Dragos platform：https://www.dragos.com/cybersecurity-platform/
- Alias RIS：https://aliasrobotics.com/ris.php
- SPIFFE：https://spiffe.io/
- Teleport workload identity：https://goteleport.com/platform/machine-and-workload-identity/
- The Update Framework：https://theupdateframework.io/
- Uptane：https://uptane.org/docs/latest/standard/uptane-standard
- CISA SBOM：https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom
- CISA VEX：https://www.cisa.gov/resources-tools/resources/minimum-requirements-vulnerability-exploitability-exchange-vex
- Qualcomm secure boot：https://www.qualcomm.com/developer/blog/2024/12/secure-boot-as-part-of-platform-security-architecture-modern-system-on-chip
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- 数据安全法：https://www.cac.gov.cn/2021-06/11/c_1624994566919140.htm
- 个人信息保护法：https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm
- 网络数据安全管理条例：https://www.gov.cn/zhengce/zhengceku/202409/content_6977767.htm
- GB/T 39404-2020：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=57E45D47E1A9C3C053C546B18DFB1BEA
- GB/T 45502-2025：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=9E2B74F7423F548D405996E62937064A
