# RiskLedger Pitch

更新时间：2026-07-05。

## Core Thesis

RiskLedger 是面向商业机器人队列的风险证据账本：

> RobotShield 在 Qualcomm edge 本体侧记录黑匣子证据，RiskLedger 在云端生成事故复盘、保险承保、融资尽调、质保、SLA 和采购安全所需的可信证据包。

它不是保险公司，不替法务判定责任，也不声称认证机器人安全。它解决的是商业化中的下一个硬问题：

- 机器人运行数据是否可信。
- 事故前后事实能否回放。
- 日志是否被篡改。
- 维护、固件、模型和安全事件是否能追溯。
- 保险、设备金融和企业采购是否能拿到足够结构化的数据。

一句话：让机器人从“可演示、可部署”进一步变成“可承保、可融资、可复盘”的商业资产。

## Why This Matters

机器人数量已经足以产生保险、融资和事故证据基础设施需求：

- IFR 报告 2024 年全球工业机器人安装量约 542,000 台，运行存量约 4.66M 台，并预测 2028 年安装量超过 700,000 台。
- 专业服务机器人 2024 年销售接近 200,000 台，物流/运输类居前，RaaS fleet 增长显著。
- 企业买机器人时常常需要保险凭证、安全文档、事故历史、服务记录和供应商安全问卷。
- 保险和经纪机构需要 robot-level exposure、utilization、ODD、incident、maintenance 和 performance 数据。
- RaaS 和设备金融需要 uptime、服务合规、残值、再部署风险、资产健康和违约损失假设。

现有 SafetyOps 解决“策略如何上线和回滚”，RobotLeaseOps 解决“机器人如何订阅和融资购买”，RoboTrust 解决“数据如何采集和训练”。RiskLedger 连接这些模块，把运行事实变成外部机构也能使用的证据。

## Product Modules

### 1. RobotShield Edge Recorder

本体侧被动黑匣子。

- 监听 ROS 2 / DDS、CAN、EtherCAT、PLC、安全控制器、相机、LiDAR、IMU、关节/力矩、地图和 operator input。
- 默认不插入安全关键控制链，避免给急停和保护停增加延迟或新故障模式。
- 在明确验证前，只说“记录、保全和风险状态触发”，不说替代安全控制器。

触发条件：

- 急停、保护停、碰撞/力峰、速度区违规。
- 人员接近、近失误、禁区穿越。
- 定位丢失、autonomy disengagement、manual override。
- 通信故障、维护/LOTO 状态不匹配。
- 固件、模型、配置、debug 或网络安全异常。

### 2. Forensic Buffer

事件前后高频窗口 + 低频运营上下文。

- 类似汽车 EDR 的思路：保留短窗口、高质量、可检索的关键数据，而不是无限期上传所有原始视频。
- 高速数据保留本地，云端先同步 manifest、hash、缩略图、风险元数据和必要片段。
- 支持 legal hold、retention policy、role-based export 和 privacy redaction。

### 3. Evidence Capsule

可导出的证据包。

包含：

- package id、incident id、schema version。
- robot id、model、serial、site、cell、map version。
- event type、severity、trigger、UTC time、monotonic time、time-sync quality。
- robot pose、velocity、joint state、commands、payload、speed limit。
- safety state：E-stop、guards、scanner zones、safety function refs。
- autonomy state：planner、localization confidence、model hashes。
- media refs：video / LiDAR / MCAP / ROS bag slices、redaction status。
- software config：firmware、app version、config hash、SBOM ref。
- integrity：hash chain head、signature、custody log、reviewer annotations。

关键表述：RiskLedger 不直接判定法律责任。它保全可复核事实，支持 root-cause review、保险理赔、集成商复盘、质保判定和安全案例更新。

### 4. RiskLedger Cloud

云端风险账本。

- 事件时间线、回放、证据校验和篡改检测。
- near-miss heatmap：按通道、班次、机器人型号、任务、速度区聚类。
- corrective action tracker：问题、原因、负责人、修复、验证、复发监控。
- safety-case loop：把事故复盘转成风险评估、ODD 限制、测试场景 backlog 和 SafetyOps release gate。
- fleet dashboard：每台机器人 boot integrity、attestation、model version、patch level、last risk event 和 unresolved evidence。

### 5. Insurance And Finance Data Packs

面向保险、经纪、融资和 RaaS 的结构化数据。

- Underwriting pack：ODD、任务、利用率、近失误、事故、维护、操作员接管、场地风险。
- Claims reconstruction：事件前后时间线、证据链、维护状态、软件/模型状态、操作记录。
- Warranty reserve：部件故障、维修原因、客户误用、field service cost 和 repeat issue。
- SLA evidence：可用率、计划/非计划停机、MTBF、MTTR、服务例外、service credit。
- Residual value：电池健康、循环、里程、传感器状态、软件支持期、再部署成本和维修历史。

商业模式：

- per-robot monthly SaaS。
- enterprise audit / lender dashboard。
- underwriting API / claims reconstruction tool。
- warranty analytics / service contract module。
- partner-enabled insurance referral 或 coverage workflow，但不无证经营保险业务。

### 6. Cyber Procurement Pack

连接机器人采购安全和 OT 安全。

- Secure-by-design SDLC：threat modeling、SAST/SCA/fuzzing、release gates、signed builds、patch metrics。
- per-robot identity：unique credentials、MFA/RBAC、hardware-backed keys、secure boot where supported。
- signed OTA：staged rollout、rollback、security updates、support period、EOL disclosure。
- SBOM/VEX：release-level SBOM、CVE/KEV monitoring、affected/not affected status、advisory history。
- CVD/VDP：security contact、security.txt、triage SLA、coordinated disclosure。
- audit logs：admin access、robot commands、firmware updates、remote support、policy changes、map/data export、safety-mode changes。
- OT guide：network segmentation、robot VLAN、zones/conduits、least privilege remote access、SIEM export。

安全表述：

- “designed to align with NIST SSDF, NIST IoT guidance, CISA Secure by Design and EU CRA evidence needs.”
- 不说 CRA compliant、NIST certified、hack-proof、guaranteed secure 或 fully compliant。

## Qualcomm Value

RiskLedger 是一个非常适合 Qualcomm 的“硬件信任根 + 边缘证据”叙事：

- Secure Boot / hardware root of trust：证明机器人从授权软件启动。
- QTEE / secure storage / SPU-like capabilities：保护签名密钥、计数器和证据哈希。
- AI Hub：记录模型 ID、版本、runtime target、compiled artifact hash、latency、memory、compute-unit profile 和 numerical validation result。
- Dragonwing / RB / QCS / IQ 平台：多摄像头、LiDAR、IMU、ToF、音频和控制数据在本体侧低延迟采集。
- 5G / Wi-Fi / private network：离线签名、本地排队、恢复网络后同步账本。
- Qualcomm edge 不只是运行模型，而是让模型、固件、传感器和事件证据可被第三方信任。

Demo hooks：

1. Trusted Boot Gate：secure boot / attestation 通过才显示绿色；模拟 debug/tamper 后锁定高风险技能。
2. Model Swap Alarm：AI Hub profile 模型正常；换成未验证模型后 RiskLedger 标记 model drift。
3. Near-Miss Evidence Capsule：人进入限制区，机器人签名事件、保存本地视频、上传 hash 和元数据。
4. Disconnected But Accountable：断网时持续本地签名，联网后按顺序同步。
5. Tamper Demo：篡改一帧 telemetry，证据包 hash verification 失败。
6. Fleet Risk Ledger：比较三台机器人在信任状态、模型状态、安全事件和未关闭证据上的差异。

## Competition Demo

最稳妥的比赛演示是浏览器可交互 replay：

1. 模拟仓库 AMR 任务，显示机器人、工位、人行区和安全 zone。
2. 出现 near-miss：人进入黄区，机器人保护停或降速。
3. RobotShield 冻结事件前后数据窗口。
4. RiskLedger 生成证据包：时间线、视频片段、LiDAR/地图、控制命令、模型哈希、固件版本、维护状态。
5. 点击“校验”，证据链通过；手动篡改一条 telemetry，校验失败。
6. 一键导出给 insurer / integrator / customer safety team 的证据摘要。
7. 事件进入 corrective action：更新 ODD、速度区、测试场景和 SafetyOps gate。

## China / Overseas Positioning

中国版：

- 面向机器人厂商、系统集成商、场景业主、租赁公司和保险/风控伙伴。
- 重点说“事故复盘、运维质保、项目验收、设备租赁、责任边界、数据留痕”。
- 不公开强调“自动理赔”，而强调“安全生产、设备可信、项目验收、可追溯运维”。

海外版：

- 面向 RaaS operator、robotics OEM、insurance broker、equipment lessor、enterprise risk team。
- 重点说 insurability、bankability、claims reconstruction、product liability evidence、Cyber Resilience Act evidence needs。
- 可以和 Koop / Lloyd's / AXA XL / Hartford / Axis 等生态作为外部市场信号，但不声称替代它们。

## Claims To Avoid

- 不声称 guaranteed premium reduction 或 financing approval。
- 不声称 determine legal fault；只说 evidence preservation and attribution support。
- 不声称 OSHA approved、ANSI certified、CRA compliant、NIST certified 或 safety certified。
- 不说 tamper-proof，除非实现足够密码学控制；更稳妥是 tamper-evident。
- 不说机器人比人类绝对更安全；风险取决于场景、维护、控制和部署边界。
- 不把 AI root-cause analysis 当作结论；AI 只能做 advisory，事实证据才是核心。
- 不把 cybersecurity 说成 machinery / functional safety 的替代品。

## Sources

- IFR industrial robot demand：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- A3 robot orders 2025：https://www.automate.org/robotics/news/robot-orders-grow-6-6-in-2025-as-general-industries-drive-broader-automation-adoption
- OSHA robotics：https://www.osha.gov/robotics
- Koop Lloyd's Lab：https://www.lloyds.com/insights/lloyds-lab/programmes-and-initiatives/lloyds-lab-accelerator/alumni/koop-technologies
- Koop underwriting API：https://www.koop.ai/blog/api-underwriting-a-perfect-solution-for-avs-robotics-insurance
- The Hartford autonomous risk：https://www.thehartford.com/insights/technology/evaluating-autonomous-risk
- Axis robotics insurance：https://axisinsurance.ca/commercial-insurance/robotics-insurance/
- AXA XL autonomous vehicle policy：https://axaxl.com/press-releases/axa-xl-launches-single-customisable-policy-for-autonomous-vehicles
- EU Product Liability Directive：https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng
- eCFR 49 CFR Part 563 Event Data Recorders：https://www.ecfr.gov/current/title-49/subtitle-B/chapter-V/part-563
- Federal Register EDR final rule 2024：https://www.federalregister.gov/documents/2024/12/18/2024-29862/event-data-recorders
- ISO 10218-1:2025：https://www.iso.org/standard/73933.html
- ISO 10218-2:2025：https://www.iso.org/standard/73934.html
- ANSI/A3 R15.08：https://www.automate.org/robotics/safety/robot-safety-standard-documents
- OSHA Technical Manual robotics：https://www.osha.gov/otm/section-4-safety-hazards/chapter-4
- NIST SP 800-92 Log Management：https://csrc.nist.gov/pubs/sp/800/92/final
- NIST chain of custody glossary：https://csrc.nist.gov/glossary/term/chain_of_custody
- NIST SSDF SP 800-218：https://csrc.nist.gov/pubs/sp/800/218/final
- NISTIR 8259A IoT cybersecurity baseline：https://csrc.nist.gov/pubs/ir/8259/a/final
- NIST SP 800-82 Rev. 3 OT Security：https://csrc.nist.gov/pubs/sp/800/82/r3/final
- CISA Secure by Design：https://www.cisa.gov/resources-tools/resources/secure-by-design
- CISA SBOM：https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom
- EU Cyber Resilience Act：https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- ISA/IEC 62443：https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
- Qualcomm secure boot：https://www.qualcomm.com/developer/blog/2024/12/secure-boot-as-part-of-platform-security-architecture-modern-system-on-chip
- Qualcomm IoT security：https://www.qualcomm.com/products/features/iot-security
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
