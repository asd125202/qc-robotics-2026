# RiskLedger Pitch

更新时间：2026-07-06。该版本按 `docs/pitch-deck-standard.md` 重写，定位为 Physical AI EDR / robot claims exchange，而不是普通机器人运维平台。

## One-Liner

机器人行业不缺保险产品，缺的是保险、融资、质保和 SLA 都能相信的机器事实层。RiskLedger 在 Dragonwing 机器人本体侧封存事故前后证据，用签名、哈希链、隐私脱敏和可回放时间线，把每台机器人变成可承保、可融资、可复盘的商业资产。

## 1. Problem

机器人不是买不起，是出事后没人敢相信谁的数据。

商业机器人进入仓库、医院、酒店、园区和人机混行空间以后，一次事故会同时牵涉：

- 硬件故障、传感器状态、制动和急停。
- AI 模型、QNN runtime、策略版本、地图版本和 OTA。
- 现场环境、人员闯入、网络异常和操作员接管。
- OEM、系统集成商、维护商、客户、租赁方、保险方和融资方。

没有可信证据，保险公司难定价，融资方难尽调，OEM 难判断质保责任，客户难证明 SLA，法务和 EHS 团队只能靠截图、群聊和事后口供。

## 2. Current Alternatives Fail

今天的工具能看见机器人，却不能把事故变成第三方可信证据。

- Fleet ops：Formant、InOrbit、Viam 等适合监控、告警、远程诊断和调度，但不是 claims exchange。
- ROS bag / MCAP：能回放数据，但默认缺少保全、签名、隐私脱敏、custody log、分享权限和事故报告格式。
- CCTV：只能看到表象，看不到模型 hash、控制命令、QNN runtime、急停状态、地图版本和传感器健康。
- CMMS / EAM：ServiceNow、Maximo、Dynamics 可以处理工单，但需要一个机器人证据包作为输入。
- OEM cloud：适合单厂商设备管理，但客户现场常是多品牌、多集成商、多业务系统。
- Blockchain：如果边缘端采集不可信，只是给不可信日志盖时间戳。

RiskLedger 的产品边界必须清晰：不做 fleet command center，不替代 CMMS，不抢 OEM cloud。它只做跨 OEM、跨队列、客户可控、外部机构能读取的 Physical AI EDR。

## 3. Solution

RiskLedger 是机器人事故的 EDR、黑匣子和 claims exchange。

核心流程：

1. Trigger：急停、近碰、人员闯入、安全区越界、QNN failure、人工接管、租赁越界或证书异常触发事件。
2. Capture：冻结 `T-60s` 到 `T+180s` 环形缓冲，采集视频、LiDAR、IMU、ROS 2、CAN、EtherCAT、日志和控制链。
3. Seal：生成 manifest、Merkle root、COSE signature、timestamp、privacy class 和 custody event。
4. Replay：把原始日志变成可读时间线：先发生什么、系统怎么判断、谁接管、是否超出 ODD。
5. Export：输出保险理赔包、质保争议包、SLA credit、EHS 审计包、融资尽调和 CertForge 证据。

RiskLedger 不直接判定法律责任。它保全可复核事实，支持 root-cause review、保险理赔、质保判断、SLA 争议和安全案例更新。

## 4. Why Now

Physical AI 正在进入保险、责任、融资和合规结算层。

- IFR 2025 显示，2024 年全球工业机器人新增安装约 54.2 万台，运行存量约 466.4 万台。
- 2024 年专业服务机器人销售接近 20 万台，RaaS fleet 增长 31%。
- 自动驾驶和汽车 EDR 已经证明，事故前后窗口记录是责任和理赔基础设施。
- EU AI Act 对高风险 AI 系统有生命周期日志要求，但并不意味着所有机器人都是高风险 AI。
- EU Product Liability Directive 更明确地把软件/AI 纳入产品责任框架。
- EU Cyber Resilience Act、Machinery Regulation、中国数据出境规则、客户 IT/OT 审计，都在推动机器人生命周期证据成为采购门槛。

安全表述：商业机器人目前没有通用“黑盒强制要求”。RiskLedger 的机会来自合规、保险、融资、质保和诉讼压力形成的事实需求。

## 5. Product

RiskLedger 卖的不是“录像”，而是一条可采信的责任链。

核心 artifact：

- `robot-evidence-event.json`：event_id、robot_id、fleet_id、site_id、trigger、severity、capture_window、lease_id、operator_id_hash、policy_version、privacy_class。
- `event.mcap`：ROS 2 topic、sensor fusion、planning、control、safety state、pose、velocity、fault code。
- `qnn/runtime.json`：AI Hub job、model hash、QNN context hash、runtime version、latency、target SoC。
- `policy/decision_log.jsonl`：策略决策、人工审批、风险模式变化、权限和拒绝原因。
- `evidence-bundle-manifest.cbor`：file hashes、Merkle root、secure boot state、OTA version、retention class、legal hold。
- `signature.cose` / `timestamp.tsr` / `ledger_receipt.json`：签名、时间戳和透明日志收据。
- `redaction-manifest.json`：人脸、工牌、地图、客户工艺信息和音视频片段的脱敏规则与 reviewer hash。
- `claim-pack.pdf`：事故时间线、责任因子、维护状态、质保边界、SLA 例外和导出记录。

建议 API：

- `POST /v1/robot-events`
- `POST /v1/evidence-bundles:init`
- `PUT /v1/evidence-bundles/{id}/parts/{part}`
- `POST /v1/evidence-bundles/{id}:seal`
- `GET /v1/evidence-bundles/{id}:verify`
- `POST /v1/custody-events`
- `POST /v1/redactions`
- `GET /v1/replay/{bundle_id}`

和其他模块关系：

- UptimeOS：事故后自动打开 incident，更新 health passport 和 service workflow。
- RobotLeaseOps：事故后进入 evidence hold，必要时禁止 redeploy，直到 sealed receipt 生成。
- CertForge：导出标准映射 evidence pack，进入安全案例、合规包和版本变更记录。
- LeRobot / TrainRouter：把失败片段转成 failure mining 和训练评估数据。

## 6. Market And Business Model

第一批买家不是“所有机器人用户”，而是已经在承担事故、维修、理赔、残值和责任归属成本的人。

买方优先级：

1. RaaS / 租赁运营商：高频流转、跨场景使用，设备损坏、第三者责任和数据安全风险集中在运营方。
2. 保险公司 / 经纪 / MGA：机器人风险数据少，难精准定价，需要动态费率、承保准入和理赔取证。
3. 融资租赁 / 设备金融：关心抵押物位置、使用强度、维护状态、残值和道德风险。
4. OEM 质保 / 售后：需要区分产品缺陷、客户误用、超工况使用和 no-fault-found。
5. 企业 EHS / 合规团队：上线机器人前后需要事故复盘、审计留痕和安全闭环。
6. 系统集成商：把证据系统打包进 FAT/SAT、风险评估、验收和维护移交。

建议定价：

- 中国低风险室内配送/清洁：`100-300 元/台/月`。
- 中国人形、AMR、工业移动机器人：`300-800 元/台/月`。
- 中国事故取证报告：`3000-20000 元/次`。
- 中国保险/租赁平台试点：`10万-50万元/3-6个月`。
- 海外基础证据账本：`$25-75 / robot / month`。
- 海外高风险视频/AI 事故分析：`$100-250 / robot / month`。
- 海外事故取证报告：`$300-1500 / incident`。
- 海外保险/企业试点：`$25k-$150k / 3-6 months`。

ROI 公式示例：

- RaaS / 租赁运营商：少赔的维修费 + 少赔的第三者责任 + 追回责任方赔偿 + 保险可得性提升 + 停机争议减少 - RiskLedger 成本。
- 保险公司：损失率下降 + 反欺诈节省 + 理赔处理成本下降 + 风险选择改善 - 数据/集成成本。
- 融资租赁：残值提升 + 灭失/逾期损失下降 + 保险可得性提升 + 处置效率提升 - 监控成本。
- OEM 质保：识别误用索赔 + no-fault-found 减少 + 供应商追偿 + 质保准备金优化 - SDK/数据接入成本。

安全表述：不承诺保费必降、融资必批或责任自动判定，只承诺建立可验证事实层。

## 7. Competition And Moat

公开市场里还没有一个清晰主导者专门做“机器人事故证据交换与责任账本”。现有工具要么偏运维，要么偏开发数据，要么偏 IT/OT 风险，要么锁在 OEM 云里。

RiskLedger 的 wedge：

- Robot EDR schema：定义机器人事故前后窗口，覆盖感知、控制、QNN、策略、地图、人工接管、安全状态和维护状态。
- Evidence packet：自动截取事故前后多模态数据，生成可验证、可脱敏、可分享的证据包。
- Chain of custody：hash、签名、时间戳、WORM/object lock、访问审计、导出记录和 redaction。
- Claims / warranty / safety export：面向保险、OEM、SI、客户 EHS、法务、融资和监管流程。
- Connector-first：接 Formant、InOrbit、Viam、Foxglove、Roboto、ServiceNow、Maximo、Jira、Zendesk 和 OEM cloud。
- Risk data flywheel：每个事故、near-miss、维修、补丁、接管和质保结果都会改善下一版风险评分。

一句话边界：

> RiskLedger 是机器人事故的 EDR + 黑匣子 + claims exchange，不是另一个 robot fleet dashboard。

## 8. Why Qualcomm

可信证据必须从边缘硬件开始，而不是事故后补表格。

Dragonwing IQ10 RRD 把异构计算、AI 加速、多相机、LiDAR、ToF、IMU、EtherCAT、CAN-FD、TSN、网络和机器人软件栈放进同一参考设计。RiskLedger 把这些能力转换成商业信任：证明某台机器人在某个模型/QNN/策略版本下，基于哪些传感器输入和控制链路做出了什么动作。

Qualcomm 价值：

- Secure edge：安全启动、设备身份、签名和本地证据密钥，让日志从源头具备可信起点。
- Sensor fusion：相机、LiDAR、IMU、CAN、EtherCAT 和安全状态在本体侧同步封存。
- QNN proof：AI Hub job、QNN context hash、runtime version 和 latency 进入模型证据链。
- Offline trust：断网时本地签名排队，恢复 Wi-Fi/5G/专网后按 custody chain 同步。
- Ecosystem attach：RiskLedger 能把 Qualcomm 生态从“机器人运行”延伸到“机器人承保、融资、质保和合规”。

需要 Qualcomm 支持：

- RB3 / IQ9 / IQ10 证据 profile：定义安全启动、传感器、QNN、系统版本、功耗和网络状态如何进入事件证据包。
- AI Hub / QNN artifact ID：让比赛 demo 的模型不是“跑过”，而是能在事故回放里证明实际部署版本。
- 生态验证场景：联合 OEM、RaaS、保险/MGA 和融资方做 90 天证据试点。

## 9. Competition Demo

8 分钟演示：把一次 near-miss 变成保险、质保、SLA 和训练都能使用的证据包。

演示脚本：

1. RobotLeaseOps 创建租赁任务，UptimeOS 显示机器人在线，RiskLedger agent 处于 armed 状态。
2. 人员进入安全区，触发 `near_miss.human_zone_intrusion`。
3. Evidence Agent 冻结 `T-60s` 到 `T+180s` 缓冲，打包 MCAP、视频、QNN runtime、policy decision log、SBOM/MLBOM。
4. 生成 Merkle root、COSE signature、RFC3161 timestamp 和 RiskLedger receipt。
5. RiskLedger 展示时间线：感知帧、policy decision、规划轨迹、速度/刹车曲线、急停状态和 redacted replay。
6. UptimeOS 自动开 incident，RobotLeaseOps 加 legal hold，CertForge 一键生成标准映射 evidence pack。
7. Tamper demo：改动一帧视频或一行日志，`GET /verify` 返回 hash mismatch。
8. 导出 claim pack、warranty pack、SLA exception 和 LeRobot failure episode。

## Claims To Avoid

- 不说“全球首个机器人黑匣子”。
- 不说“不可篡改”，说 tamper-evident / 可发现篡改。
- 不承诺保费必降、融资必批、质保准备金必降。
- 不暗示所有机器人都受 EU AI Act 高风险日志义务约束。
- 不说 RiskLedger 能判定法律责任；它提供证据和责任因子。
- 不声称 Qualcomm 官方合作、认证或内置，除非已经拿到授权。
- 不说 CRA compliant、NIST certified、safety certified 或 hack-proof。

## Sources

- IFR industrial robot demand 2025：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots 2025：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- NHTSA Event Data Recorder：https://www.nhtsa.gov/research-data/event-data-recorder
- 49 CFR Part 563：https://www.ecfr.gov/current/title-49/subtitle-B/chapter-V/part-563
- EU AI Act Article 12：https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12
- EU Cyber Resilience Act：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- EU Product Liability Directive：https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng
- China cross-border data rules：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Dragonwing RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub compile examples：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- MCAP：https://mcap.dev/
- ROS 2 DDS Security：https://design.ros2.org/articles/ros2_dds_security.html
- OpenTelemetry Semantic Conventions：https://opentelemetry.io/docs/concepts/semantic-conventions/
- COSE RFC 9052：https://datatracker.ietf.org/doc/rfc9052/
- RFC 3161 timestamp：https://www.ietf.org/rfc/rfc3161.txt
- RFC 9162 transparency log：https://datatracker.ietf.org/doc/html/rfc9162
- C2PA Specification：https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html
- Formant Fleet Observability：https://docs.formant.io/docs/fleet-observability
- Viam Fleet Management：https://www.viam.com/platform/fleet-management
- Cambridge Mobile Telematics Claims Exchange：https://www.cmtelematics.com/news/cambridge-mobile-telematics-announces-enhanced-driver-experiences-crash-capabilities-and-developer-tools/
