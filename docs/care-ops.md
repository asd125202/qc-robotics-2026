# CareOps Pitch

更新时间：2026-07-06。该版本按 YC / Airbnb 风格 pitch spine 重写：先讲医院运营问题，再讲现有方案缺口、解决方案、为什么现在、产品、商业模式、竞争壁垒、为什么 Qualcomm、比赛演示和合规边界。

## One-Liner

CareOps 是院内智运控制面：

> 用 Qualcomm 边缘节点把样本、药品、耗材、机器人、门梯、隐私和审计连成一个非临床物流闭环，让医院证明“什么被送了、谁碰过、是否越权、是否超时、是否可以复盘”。

它不做诊断、不分诊、不给药、不监护患者、不替代医嘱或临床判断。

## 1. Problem

医院最短缺的人力，被消耗在送标本、送药、取耗材和等电梯上。

核心痛点：

- 护士、药师、检验人员每天被非临床跑腿任务打断。
- 标本从病区到检验科的 last mile 最容易出现错码、延迟、交接不清和运输异常。
- 药品、耗材、小设备和 PPE 配送需要锁柜、身份、权限、时间戳和签收。
- 老院区、多楼宇、电梯、门禁、拥挤走廊、夜间路线让机器人部署复杂。
- 走廊视频、患者位置、工牌、屏幕、样本编号和异常片段不能默认上云。
- 医院招采部门需要网络安全、隐私、消毒 SOP、风险评估、验收 KPI 和运维 SLA，不是只看一个 robot demo。

商业表达：

> 医院不是缺一个会移动的机器人，而是缺一套能把院内物流变成可采购、可审计、可持续优化的系统。

## 2. Current Alternatives Fail

现有方案各解决一块，但没有把可采购的院内智运拼成闭环。

- 人工 runner：灵活但不可复制，交接、温控、路线、延迟、错误和责任边界常靠人工记录。
- 气动物流：适合小件高速传输，但覆盖不了大件、锁柜、多点配送、机器人路线和异常复盘。
- 单一机器人厂商：Moxi、TUG、Relay、Pudu、Keenon、MiR 都能执行任务，但客户仍需要跨系统 workflow 和招采证据。
- 实验室自动化：提升 lab 内部效率，但不解决病区到检验科的 last mile、身份签收、电梯门禁和 PHI 边界。
- 通用 RobOps：InOrbit、Formant 擅长 fleet ops，但不天然包含样本链路、LIS/LIMS/FHIR、BAA-ready、消毒 SOP 和医院 procurement packet。

Deck line：

> 机器人负责跑，CareOps 负责让样本、药品、耗材、电梯门禁、隐私和审计形成闭环。

## 3. Solution

CareOps 是院内部署的非临床物流控制面。

部署形态：

- Qualcomm Dragonwing / RB / IQ edge appliance。
- 连接机器人、LIS/LIMS、HIS、药房、SPD、护士站、门梯和 BMS/设施接口。
- 云端只做训练、分析、远程支持和包更新；现场任务、隐私、签收、审计和异常复盘在院内边缘运行。

核心流程：

1. Request：LIS/LIMS、HIS、药房、SPD、护士站或人工台生成非临床物流任务。
2. Verify：条码/RFID、工牌、锁柜、温控、目的地和权限进入 SpecimenChain。
3. Dispatch：按优先级、路线、门梯、电量、区域规则和机器人能力派发任务。
4. Protect：视频、患者位置、工牌和屏幕默认本地处理，导出前完成最小化和脱敏。
5. Replay：交接失败、错码、超时、堵路和人工接管变成审计包和 LeRobot 训练片段。

## 4. Why Now

护理短缺、医院机器人成熟和数据合规压力正在同时逼近。

可用事实：

- AHA 报告显示人工和薪酬约占美国医院成本的 56%。
- NSI 2025 报告中 RN turnover 为 17.6%，每名 bedside RN turnover 成本约 $60,090。
- McKinsey / ANA 估计技术和任务重分配可释放最高约 15% 护士时间。
- AHRQ / PSNet 指出，检验结果影响大量临床决策，pre-analytical 阶段是错误高发区。
- 中国医院物流机器人招采已经出现从单机采购、系统采购到租赁服务的多种形态。
- HIPAA、PIPL、网络安全、医院感染控制和医疗软件边界让“云端裸奔”的机器人方案越来越难进医院。
- Qualcomm Dragonwing / RB / IQ + AI Hub / QNN 可以把本地推理、模型 profile、隐私处理和部署证据打包成 reference workflow。

## 5. Product

先做 sealed specimen transport，再扩展到药房、耗材和设备补给。

第一阶段 wedge：

- 使用 sealed mock specimen tubes 和二维码/条码。
- 从护士站/病区/急诊/手术室到检验科。
- 不处理开放样本、锐器、Category A infectious substances 或真实临床结果。
- 目标是 traceability、handoff、route SLA 和 exception closure，不声称保证临床检测结果。

核心模块：

- CareOps Edge：本地任务引擎、机器人 adapter、隐私视觉、事件账本和 sync agent。
- Integration Gateway：FHIR R4 / HL7 v2 / vendor API / LIS/LIMS / HIS / pharmacy / SPD adapters。
- SpecimenChain：条码/RFID、锁柜、工牌/PIN、温控、时间戳、签收和 hash-linked custody events。
- SiteGraph + AccessBridge：楼层、门禁、电梯、restricted zones、服务电梯队列和设施 ack。
- Robot Adapter Runtime：VDA 5050、Open-RMF / ROS 2、vendor REST/gRPC、observe-only。
- PrivacyVision：本地人脸、工牌、腕带、屏幕和非任务标签脱敏，原始视频短期留院内。
- Incident Replay：MCAP/JSON 复盘包，包含任务状态、机器人轨迹、交接、设施事件、视频片段和模型版本。
- LeRobot Flywheel：只导出获批的非临床、脱敏 HIL episodes，例如堵路、错码、交接失败、电梯等待和锁柜定位。

### Reference Architecture

```text
CareOps edge appliance on hospital LAN
  ├─ api-gateway
  ├─ nurse-station console
  ├─ integration-gateway
  ├─ task-engine
  ├─ specimen-chain ledger
  ├─ site-graph
  ├─ access-bridge
  ├─ robot-adapter-runtime
  ├─ privacy-vision
  ├─ incident-replay
  ├─ rbac-audit
  ├─ model-registry
  └─ sync-agent
```

Data plane:

- Postgres for task state and custody ledger.
- Append-only event log.
- Local object store for replay media and redacted exports.
- MQTT / NATS / ROS 2 / vendor API for local integration.
- Cloud optional; never required for live hospital logistics.

### Core Schemas

```json
{
  "CareOpsTask": {
    "task_id": "co_task_123",
    "kind": "specimen_transport|pharmacy_lockbox|supply_replenish",
    "priority": "routine|urgent|stat",
    "source_refs": {
      "fhir_task": "Task/abc",
      "service_request": "ServiceRequest/lab1"
    },
    "objects": [
      {
        "id": "SP-2026-001",
        "id_type": "barcode|rfid",
        "sealed": true
      }
    ],
    "pickup": "Location/ward-5a-nurse-station",
    "dropoff": "Location/core-lab-intake",
    "custody_required": true,
    "due_by": "2026-07-06T10:15:00Z"
  }
}
```

```json
{
  "CustodyEvent": {
    "event_id": "urn:uuid:...",
    "task_id": "co_task_123",
    "object_id": "SP-2026-001",
    "event_type": "commission|pickup|handoff|exception|receive",
    "actor": "badge_hash:...",
    "read_point": "ward-5a-locker-02",
    "biz_location": "core-lab-intake",
    "sensor": {
      "temp_c": 4.8,
      "locker_slot": "A3"
    },
    "media_ref": "redacted://clip/...",
    "prev_hash": "sha256:...",
    "signature": "ed25519:..."
  }
}
```

```json
{
  "IncidentReplay": {
    "incident_id": "inc_barcode_mismatch_01",
    "kind": "barcode_mismatch|elevator_timeout|path_blocked|handoff_failed|temp_excursion",
    "task_id": "co_task_123",
    "timeline_uri": "mcap://careops/inc_barcode_mismatch_01",
    "redaction_status": "passed",
    "exportable_to_lerobot": true,
    "model_versions": {
      "redactor": "qnn-face-redact-v3",
      "barcode": "qnn-barcode-v2"
    }
  }
}
```

## 6. Market And Business Model

卖给医院的不是机器人，是更少跑腿、更快交接和更完整的招采证据。

第一批客户：

- 大型综合医院 / 三甲：多楼宇、多科室、高检验量、老院区改造、夜间低人力。
- 医学中心 / 检验量高的医院实验室：重视 specimen TAT、错码、交接和异常追溯。
- 药学部 / PIVAS / 中心药房：重视安全配送、锁柜、授权签收和中断减少。
- SPD / 后勤 / 运营院长：重视跨科室耗材、PPE、设备补给和路线 SLA。
- 医院 SI / SPD operator / robot OEM：需要把一次性交付变成可复用方案。

海外版：

- 90 天 pilot：2-3 台机器人 + CareOps edge + LIMS/pharmacy mock integration，$30k-$75k。
- Site integration：$25k-$100k。
- Secure delivery robot operations：$3k-$8k / robot / month。
- 付费理由：护士时间、药房配送时长、specimen TAT、异常关闭时间、chain-of-custody、BAA-ready evidence。

中国版：

- 试点到招采：三甲/大型院区、检验科、SPD、信息中心和后勤联合推动。
- 轻量样本机器人人民币 198k-298k。
- 安全药品/温控机器人人民币 350k-500k。
- 试点包人民币 0.6M-1.5M。
- 年维保 8%-12%。
- 强调数据不出院、院内部署、等保、国产云/院内私有训练、本地 robot/SI/SPD 伙伴和招采材料。

## 7. Competition And Moat

竞争很多，但不能按“谁的机器人更好”来打。

竞争地图：

- Hospital delivery robots：Diligent Robotics Moxi、Aethon TUG / Zena RX、Relay Robotics、Pudu、Keenon、MiR。
- Healthcare transport incumbents：Swisslog Healthcare pneumatic tube / transport automation。
- Lab automation：Thermo Fisher、Biosero、Omron 等 lab AMR and automation workflow。
- Horizontal RobOps：InOrbit、Formant。
- China hospital logistics robots：钛米、赛特、普渡、擎朗、诺亚、易普森等。
- Hospital IT / LIS / SPD / SI：东软、卫宁、创业慧康、东华、上药 SPD、国药、九州通等。

CareOps 的壁垒：

- Workflow memory：每条病区到检验科、药房到护士站、SPD 到科室的路线、权限、异常和交接模式会变成站点资产。
- Evidence packet：BAA-ready、PIPL/等保、消毒 SOP、SBOM、patch SLA、数据流图、风险评估和验收 KPI 服务招采。
- Hospital adapters：FHIR / HL7 v2、LIS/LIMS、药房、SPD、BMS、电梯门禁和 robot adapter 逐步复用。
- Privacy data flywheel：只把批准的脱敏事件、模拟数据和非临床片段进入训练，形成中国和海外两条数据边界。
- Qualcomm profile library：不同 RB / Dragonwing / IQ target 的本地视觉、QNN profile、网络、功耗和断网行为形成 deployment profile。

## 8. Why Qualcomm

Qualcomm 的机会，是成为医院机器人可被信任的边缘底座。

CareOps 对 Qualcomm 的价值：

- 把 Dragonwing / RB / IQ 从机器人开发板叙事升级成 hospital edge workflow reference。
- 多摄像头、NPU/GPU/DSP、低功耗、Wi-Fi/private 5G、设备身份和断网降级正好对应医院现场要求。
- AI Hub / QNN compile-profile-run 结果可以进入上线门禁：redaction FPS、barcode/OCR latency、memory、power、rollback。
- Qualcomm 可以连接机器人 OEM、医院 SI、SPD、LIS/LIMS、药房系统和设施系统，而不是只进入单机 BOM。
- 中国版强调院内部署、数据不出院和国产云/私有训练；海外版强调 BAA-ready、FHIR/LIS/pharmacy integration 和 RaaS pilot。

需要 Qualcomm 支持：

- RB3 Gen 2 / Dragonwing IQ10 / IQ-9075 硬件访问或 technical profile。
- AI Hub / QNN 技术指导，把 privacy redaction、barcode/OCR、obstacle/handoff anomaly profile 写入 demo evidence。
- 机器人 OEM、医院 SI 或医疗生态伙伴 introduction。
- 允许作为 Qualcomm edge healthcare robotics reference workflow 继续打磨。

## 9. Competition Demo

8 分钟 demo：一个 STAT mock specimen，从护士站到检验科，途中电梯超时。

Demo site：`Acme Medical Center`

- Locations：`ward-5a-nurse-station`、`service-elevator-a`、`core-lab-intake`、`pharmacy-window`、`spd-room`。
- Robots：1 台 secure delivery AMR，1 个 simulator，1 个 FleetConductor-style site graph。
- Objects：sealed mock specimen tube、mock medication package、PPE bin。
- Interfaces：FHIR-style Task / Specimen mock、barcode scanner、badge mock、locker state、elevator ack mock。
- Incidents：elevator timeout、barcode mismatch、path blocked、handoff failed。

演示流程：

1. Nurse station dashboard 显示 STAT mock specimen to core lab。
2. 操作员扫码 sealed mock tube + staff badge，锁柜关闭，生成 CareOpsTask 和第一条 CustodyEvent。
3. SiteGraph 预约走廊、服务电梯和检验科门；机器人 adapter 接收任务。
4. 本地视频 overlay 显示人脸、工牌和屏幕脱敏，不上传 raw hallway video。
5. 注入 elevator timeout 或 barcode mismatch；CareOps 暂停、告警、生成 IncidentReplay。
6. 人工接管完成交接，FHIR-style Task 变为 completed，最终 CustodyEvent 签名。
7. 导出 redacted LeRobot episode：observations、pose/action、intervention marker、outcome label、no raw PHI。
8. Qualcomm evidence screen：target hardware、AI Hub/QNN profile、latency/memory/power、model manifest、rollback package。

## Compliance And Procurement Evidence

Pitch 中要展示的材料：

- BAA-ready control matrix：PHI flows、subcontractors、retention、breach process。
- Data map：what stays on robot、hospital server、cloud、training set。
- No raw video by default：院内短期 ring buffer + 脱敏导出 + 审批流程。
- Cleaning SOP：disinfectant compatibility、contact time、wheels/cabinet/payload bay、spill response。
- Safety case：risk assessment、speed zones、geofences、E-stop、manual takeover、near-miss logs。
- Specimen evidence：barcode/RFID、lock state、temperature if used、handoff signatures、exception timeline。
- Cyber packet：SBOM、signed OTA、vulnerability policy、patch SLA、pen-test summary、network ports。
- AI packet：model/version registry、evaluation set、failure taxonomy、human override log、drift monitoring。
- China packet：PIPL data classification、local deployment、cross-border off by default、等保/医院网络安全配合。
- Pilot governance：hospital IPC、lab director、privacy/security、facilities、nursing/pharmacy signoff。

## Claims To Avoid

- 不说 “HIPAA compliant robot”、“PIPL compliant”、“fully de-identified” 或 “PHI never touched”。
- 不说 FDA/NMPA cleared、not regulated by FDA/NMPA、medical device approved。
- 不说诊断、分诊、患者监护、跌倒检测、病情预测或 clinical decision support。
- 不说 prevents infection、reduces HAIs、sterile 或 hospital-grade disinfection，除非有验证。
- 不说 CLIA compliant robot、guarantees specimen integrity 或处理 Category A / open specimens。
- 不说替代护士、药师、检验人员或 courier。
- 不说 autonomous drug administration、dispenses medication 或 verifies medication correctness。
- 不说 secure/unhackable/zero-risk、SOC 2/ISO 27001 certified，除非真的完成。
- 不说中国数据可以训练全球模型，除非跨境路径、同意和数据分级已解决。

## Sources

- AHA fast facts：https://www.aha.org/statistics/fast-facts-us-hospitals
- AHA 2025 cost of caring report：https://www.aha.org/guides-and-reports/2026-03-09-2025-cost-caring-report
- NSI nurse retention report：https://www.nsinursingsolutions.com/documents/library/nsi_national_health_care_retention_report.pdf
- Becker's summary of McKinsey nursing workload：https://www.beckershospitalreview.com/quality/nursing/6-ways-to-optimize-nurse-workload/
- AHRQ specimen errors：https://psnet.ahrq.gov/web-mm/pre-analytical-pitfalls-missing-and-mislabeled-specimens
- Diligent Moxi：https://www.diligentrobots.com/moxi
- Serve Robotics / Diligent transaction：https://ir.serverobotics.com/news-releases/news-release-details/serve-robotics-acquire-diligent-robotics-expanding-physical-ai
- Aethon T3：https://aethon.com/t3/
- Aethon Zena RX：https://aethon.com/zena-rx/
- Aethon ReadyElevator：https://aethon.com/readyelevator/
- Relay hospitals：https://relayrobotics.com/relay-delivery-robots-for-hospitals
- Swisslog specimen transport：https://www.swisslog-healthcare.com/en-us/medication-management/transport/lab-specimen-transport
- Pudu healthcare：https://www.pudurobotics.com/en/solutions/health-care
- Keenon：https://www.keenon.com/en
- MiR hospitals：https://mobile-industrial-robots.com/industries/hospitals
- InOrbit orchestration：https://www.inorbit.ai/orchestration
- Formant fleet management：https://docs.formant.io/docs/getting-started-fleet-management
- HHS HIPAA Security Rule：https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html
- HHS BAA cloud guidance：https://www.hhs.gov/hipaa/for-professionals/faq/2075/may-a-hipaa-covered-entity-or-business-associate-use-cloud-service-to-store-or-process-ephi/index.html
- HHS minimum necessary：https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/minimum-necessary-requirement/index.html
- HHS de-identification：https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html
- NIST SP 800-66r2：https://csrc.nist.gov/pubs/sp/800/66/r2/final
- FDA administrative-support software：https://www.fda.gov/medical-devices/digital-health-center-excellence/step-2-software-function-intended-administrative-support-health-care-facility
- CDC CLIA overview：https://www.cdc.gov/clia/php/about/index.html
- CLIA specimen handling：https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-493/subpart-K/subject-group-ECFR5f8f0b6639946fd/section-493.1242
- OSHA bloodborne pathogens：https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030
- CMS infection prevention：https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-482/subpart-C/section-482.42
- CDC environmental infection control：https://www.cdc.gov/infection-control/hcp/environmental-control/index.html
- HHS HPH cybersecurity goals：https://hhscyber.hhs.gov/cybersecurity-performance-goals.html
- NIST CSF 2.0：https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
- NIST SSDF：https://csrc.nist.gov/pubs/sp/800/218/final
- NIST AI RMF：https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
- FHIR Specimen：https://build.fhir.org/specimen.html
- FHIR Task：https://build.fhir.org/task.html
- FHIR ServiceRequest：https://build.fhir.org/servicerequest.html
- FHIR AuditEvent：https://build.fhir.org/auditevent.html
- GS1 EPCIS：https://ref.gs1.org/standards/epcis/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- PIPL：https://en.spp.gov.cn/2021-12/29/c_948419.htm
- CAC 2024 data export provisions：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- NHC population health information guidance：https://www.nhc.gov.cn/zwgk/jdjd/201405/9992e411fff04a95b03caeda31794c7d.shtml
- Government procurement law：https://www.gjxfj.gov.cn/gjxfj/xxgk/fgwj/flfg/webinfo/2016/03/1460585589877143.htm
- MOF Order 87：https://www.mof.gov.cn/gp/xxgkml/tfs/201707/t20170718_2652766.htm
- AutoDL：https://www.autodl.com/
- Alibaba PAI-DLC：https://www.aliyun.com/activity/bigdata/pai-dlc
- Tencent GPU：https://cloud.tencent.com/product/gpu
- Huawei ModelArts：https://www.huaweicloud.com/product/modelarts.html
- RunPod pricing：https://www.runpod.io/pricing
- Lambda pricing：https://lambda.ai/pricing
- Modal pricing：https://modal.com/pricing
- CoreWeave pricing：https://www.coreweave.com/pricing
