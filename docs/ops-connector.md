# OpsConnector Pitch

更新时间：2026-07-07。企业系统、机器人 fleet API、WMS/MES/LIMS/SCADA 标准、VDA 5050、Open-RMF、OPC UA、Qualcomm Linux / AI Hub / QNN / QAIRT 和中国/海外数据合规变化较快；正式交付前必须按客户现场版本重新验证。

## One-Line Thesis

> OpsConnector 把企业系统里的业务请求，变成可执行、可审计、可复用、可写回的机器人工作流包。

机器人已经有 fleet manager。企业缺的是 workflow connector：把 WMS/MES/ERP/LIMS/SCADA/CMMS intent 转成 robot work，处理人工审批和异常补偿，用 Qualcomm edge 生成证据，再把结果写回 system of record。

## Required Deck Spine

### 01 · Problem

企业机器人部署失败，通常不是因为机器人不会动，而是因为机器人动作没有变成企业记录。

- WMS / MES / LIMS / SCADA / ERP 需要任务来源、审批、异常、验收、写回和责任边界；机器人系统通常只返回 `mission done`。
- WMS 管订单、库存、波次、库位和报表；机器人需要秒级位置、路径、拥堵、充电、工位容量和异常恢复。
- LIMS / ELN 管样本、协议、结果和 lineage；机器人扫码、交接、称重和样本转移如果不写回系统，就会破坏审计。
- MES / eBR 管材料、人员、设备、批次、质量和偏差；机器人平台通常不会自动生成 eBR、deviation 或 CMMS work order。
- 缺货、条码不符、温度越界、工位满、门禁未放行、机器人阻塞和人工接管，经常掉进微信群、电话、Excel 和手工补录。
- 每换一个 WMS、机器人品牌、仓库流程、样本规则或安全区，项目就重新写接口，无法复制到下一站点。

### 02 · Current Alternatives Fail

现在的方案各有价值，但没有拥有“企业任务 -> 机器人执行 -> 异常处理 -> 审计写回”的闭环。

- SI 项目制：能让一个现场上线，但接口、异常和写回逻辑沉没在项目代码里，下一站点继续卖人天。
- Robot OEM fleet software：Locus、GreyOrange、MiR、Geek+、Hikrobot、Quicktron 等能调度自家场景，但通常优先服务自家车队、WES/WCS/RCS 和任务模型。
- InOrbit / Formant / Orbit：验证了多品牌 robot ops、workflow AI、incident、inspection-to-work-order 需求；OpsConnector 应集成它们，而不是假装替代。
- WMS / MES 扩展：SAP EWM、Manhattan、Blue Yonder、Siemens Opcenter、国产 WMS/MES 能发业务任务，但不应直接承担机器人实时执行、离线控制、OT 网络和 safety interlock。
- iPaaS：MuleSoft、Boomi、Workato 懂 SaaS API，不懂 robot state、mission、safety、latency、on-prem edge、OPC UA、PLC 和离线 authority。
- 标准协议：VDA 5050、MassRobotics、Open-RMF、OPC UA Robotics 是好基础，但它们不覆盖订单语义、样本 lineage、库存写回、人工审批和商业 SLA。

### 03 · Solution

OpsConnector 是企业系统和机器人执行层之间的 workflow contract compiler。

核心原则：workflow-first, adapter-second.

主流程：

1. `Intent`：WMS 补货单、cycle count、MES 工单、LIMS 样本请求、SCADA interlock、CMMS work order、FHIR Task 或人工审批进入统一入口。
2. `Contract`：生成 TaskContract、ObjectMap、ApprovalGate、AdapterProfile、idempotency key、acceptance rule、timeout、rollback 和 trace context。
3. `Dispatch`：按 capability registry 选择 RobotAppLayer、EdgeFleet、VDA 5050、Open-RMF、OPC UA、vendor fleet API 或人工队列。
4. `Execute`：Dragonwing edge gateway 本地执行已授权任务，store-and-forward，断网期间只执行有效 lease 和 local-authority-safe command。
5. `Evidence`：采集条码/RFID、timestamp、robot run id、sensor reading、photo、QNN inference、operator approval、exception、signature。
6. `Writeback`：把完成、失败、库存移动、样本 lineage、CMMS work order、QMS deviation、eBR record 和 audit pack 写回企业系统。

一句话：OpsConnector 把一次性集成沉淀成可售卖、可复用、可测试的 workflow pack。

### 04 · Why Now

机器人进入运营规模后，下一场竞争是把集成服务池产品化。

- IFR 2025 service robots 报告称 2024 年专业服务机器人销量接近 20 万台，transport/logistics robots 约 10.29 万台，RaaS fleet 增长 31%。
- IFR 2025 industrial robots 报告称中国 2024 年新增工业机器人安装约 29.5 万台，占全球 54%；中国是验证多品牌、快交付、私有化和 SI-led integration 的最大市场。
- AMR / warehouse robotics software 市场报告已经把 WMS/MES/ERP integration 列为增长驱动；买方问题从“机器人会不会动”转向“能否接单、审批、对账和写回”。
- Blue Yonder、InOrbit、Formant、Boston Dynamics Orbit、GreyOrange、Locus、MiR、Tulip、Biosero 等都在从 robot ops 走向 business execution / workflow / writeback，说明品类正在形成。
- VDA 5050 3.0.0、Open-RMF、MassRobotics、OPC UA、ISA-95、CloudEvents、OpenTelemetry、OpenAPI / AsyncAPI、FHIR 等给通用合约层提供标准土壤。
- Qualcomm Dragonwing、Qualcomm Linux 2.0、RB3 / QCS6490、QCS8550、AI Hub、QNN/QAIRT 和 IQ / Dragonwing roadmap 让 on-prem robot workflow gateway 有现实 edge target。

### 05 · Product

第一批产品不是空泛 connector marketplace，而是带 SOP、UI、权限、事件、验收指标、异常处理和写回路径的 workflow pack。

优先 wedges：

1. Warehouse first：WMS-driven cycle count、replenishment、pick-exception sweeps。ROI 清晰、重复性高、低操作风险。
2. Factory second：inspection-to-work-order loop。视觉/热/声学异常 -> MES/CMMS ticket，最适合 Qualcomm edge AI，但 OT integration 更慢。
3. Lab / hospital third：secure specimen / supply courier with chain-of-custody into LIMS/LIS/EHR，故事强但合规和集成负担更高。

产品模块：

- `WMS Bridge Pack`：cycle count、补货、拣选异常、移库、入库、出库、盘点、库存写回、GS1 EPCIS traceability。
- `Factory Inspection Pack`：视觉/热/声学检测、SCADA/OPC 状态、CMMS work order、MES deviation、OEE/downtime evidence。
- `Lab Sample Transfer Pack`：LIMS/Benchling/LabWare 样本、plate map、协议、审批、条码核验、结果和 audit package。
- `SCADA / OPC Pack`：OPC UA、MQTT/Sparkplug、PLC interlock、设备状态、门禁放行、alarm、historian event。
- `Exception Compensation Pack`：缺货、工位满、条码不符、温度越界、机器人阻塞、超时、人工接管、retry/skip/abort。
- `SI Sandbox & Certification Pack`：模拟 WMS/LIMS/MES、robot task simulator、dead-letter queue、回归测试、partner certification。

### 06 · Product API/Evidence

核心对象不是 endpoint，而是可恢复、可审计、可写回的任务合约。

Core objects：

- `WorkflowPack`: vertical、version、systems、adapters、SOP、acceptance tests、pricing、support boundary。
- `TaskContract`: source、idempotency key、business object、robot capability、location、priority、due time、acceptance rule、rollback。
- `EnterpriseObjectMap`: sample、container、shelf、pallet、bin、equipment、personnel、work order、batch、barcode、plate/well、system IDs。
- `ApprovalGate`: requested_by、required_role、approver、decision、reason_code、e-signature、quality hold、SCADA interlock、expires_at。
- `CommandRequest`: lease、TTL、safety policy、local authority、approval status、max offline window、revalidation rule。
- `AdapterProfile`: VDA 5050 order/state、Open-RMF task、MassRobotics telemetry、OPC UA job、Sparkplug、FHIR、REST/gRPC/webhook。
- `ExceptionRaised`: category、severity、retryable、safe_to_retry、source_system、source_code、human_action_required、next_allowed_actions。
- `EvidencePacket`: barcode/RFID、timestamp、run id、command log、sensor reading、photo、QNN inference、operator approval、signature。
- `AuditWriteback`: inventory update、sample lineage、FHIR Task/Specimen/Observation、CMMS work order、QMS deviation、eBR record、export pack。

Event fabric：

- CloudEvents envelope with `tenant_id`, `site_id`, `edge_gateway_id`, `adapter_id`, `workflow_instance_id`, `correlation_id`, `causation_id`, `idempotency_key`, `schema_version`, `actor`, `approval_id`, `offline_window`。
- REST contracts via OpenAPI 3.1.1；async contracts via AsyncAPI 3.x；HTTP errors via RFC 9457 Problem Details。
- Edge pattern：read many, write narrowly。所有写操作都通过 lease、TTL、idempotency key、approval status 和 safety policy。

Qualcomm evidence：

- `device_id`, `model_hash`, `AI_Hub_profile_id`, `ONNX/QNN/QAIRT artifact`, `backend`, `latency`, `memory`, `thermal`, `QNN context binary`, `barcode/image/sensor evidence`, `writeback receipt`。
- AI inference evidence 不能替代业务验收；必须跟 acceptance rule 和 enterprise writeback receipt 绑定。

### 07 · Market & Business Model

目标客户不是“还没买机器人”的客户，而是已经买机器人、已有企业系统、但每个现场仍靠 SI 胶水的仓库、实验室、工厂和园区。

China distribution：

- `OpsConnector CN`：local-first，不是 global SKU 加几个开关。
- On-prem / edge gateway inside warehouse/factory；optional China control plane；China tenant/logs/secrets/KMS；PIPL/data-export controls；ICP/App filing metadata for hosted services。
- 优先适配 Geek+、Hikrobot、Hai Robotics、Quicktron、SEER/Standard Robots/ForwardX style WES/WCS/RCS；VDA 5050 是 optional，不是 baseline。
- 企业系统优先 Yonyou、Kingdee、Digiwin、SAP China、Oracle China、本地 WMS/OMS/TMS/MES、project-specific WCS。
- 内建 e-fapiao / procurement pack：VAT special/general invoice metadata、red-letter invoice、PO/GRN/invoice matching、supplier master、company tax ID。
- 渠道：robot OEM、warehouse automation SI、ERP/MES implementer、本地云/服务伙伴；中文 SI toolkit、handover docs、partner certification。

Global distribution：

- `OpsConnector Global`：standards-first, cloud-first, edge connector for plants。
- Multi-region SaaS + edge gateway；private cloud/on-prem for regulated customers。
- Standards: VDA 5050、MassRobotics AMR、OPC UA、MQTT/Sparkplug、REST/webhooks、Open-RMF、ISA-95、GS1 EPCIS、FHIR/HL7 for healthcare/lab。
- Enterprise adapters: SAP EWM、Manhattan Active WM、Blue Yonder、Körber、Infor、Oracle WMS Cloud、Siemens Opcenter、LabWare、Coupa、ServiceNow、SAP Ariba。
- Regional e-invoicing / compliance packs：EU ViDA/Peppol、GDPR/SCC、EU Data Act、SOC 2 / ISO 27001 posture。

Pricing:

- 90-day paid pilot：$25k-60k overseas；RMB 100k-300k China。
- Production site subscription：$60k-180k / year overseas；RMB 300k-1.2M / year China。
- Edge gateway：$12k-36k / site / year；China RMB 50k-200k / site / year。
- Connector pack：$10k-30k / year；workflow pack：$15k-50k / year。
- Enterprise / on-prem / compliance package：$150k-500k+ / year。
- Early target：3 lighthouse customers, 2 robot OEM connector partners, 5 certified SI partners.

### 08 · Competition & Moat

竞争来自 SI、robot OEM fleet software、robot ops platforms、enterprise iPaaS 和 enterprise system extensions。

Positioning:

- Integrate with InOrbit / Formant / Orbit / MiR / Open-RMF / VDA 5050 rather than replacing them。
- Connect them to Tulip / Ignition / MaintainX / Biosero / SAP / Oracle / Manhattan / Siemens / LabWare / local China WMS/MES。
- White space: standards move robot orders and status; OT/lab platforms manage human workflows and records; robot vendors expose APIs. OpsConnector owns cross-system choreography, approval gates, exception handling, and audit-grade writeback.

Moat:

- Connector library：WMS/MES/LIMS/ERP/SCADA/QMS/robot brand 的已验证 adapter 越多，下一次交付越快。
- Workflow templates：订单到机器人、样本到记录、工单到 eBR、异常到 QMS、库存到 ERP 的模板不断复用。
- Exception corpus：vendor error、normalized error、approval decision、retry outcome、writeback receipt 形成部署知识。
- Edge runtime：on-prem gateway 处理离线缓存、低延迟、幂等、dead-letter queue、OT/IT 网络分区和本地签名。
- Audit corpus：每个现场积累异常、审批、写回、失败原因、验收证据和 Qualcomm edge benchmark。
- Certified SI network：sandbox、partner portal、connector SDK、培训和收入分成让 SI 愿意沉淀资产。
- Data graph：`enterprise object -> robot capability -> Qualcomm edge profile -> exception -> audit writeback -> ROI evidence`。

### 09 · Why Qualcomm

OpsConnector 让 Dragonwing 从机器人推理芯片，升级为企业现场可信执行和证据节点。

Qualcomm value:

- Qualcomm 2026 investor messaging emphasizes non-handset growth, IoT, industrial/networking/robotics and Physical AI. OpsConnector directly turns robotics edge compute into enterprise workflow attach.
- RB3 Gen 2 / QCS6490 is the realistic competition gateway baseline：robotics、AI vision、edge AI、sensor I/O、Linux/Android、AI Hub support。
- QCS8550 is the high-performance on-prem robot operations box profile：multi-camera、inspection AI、edge inference、gateway workloads。
- IQ / Dragonwing robotics reference designs should be presented as roadmap / early-access production-forward profiles, not “already generally available” in July 2026.
- Qualcomm Linux 2.0 strengthens the story: unified software stack, real-time capability, OTA and security for industrial edge deployments.
- AI Hub / QNN / QAIRT evidence becomes business evidence: model version、profile、latency、input summary、confidence、task ID、device identity and writeback receipt in one packet.

Narrative:

`Enterprise task -> Dragonwing edge gateway -> robot adapter -> local AI verification -> audit writeback -> ROI dashboard`

This is stronger than “Qualcomm runs a model”: it makes Qualcomm the trusted edge node between enterprise systems and robot work.

### 10 · Demo & Ask

7-minute demo：one robot, two vertical configs.

1. Warehouse mode：WMS cycle-count / replenishment task enters OpsConnector with bin、SKU、barcode、acceptance rule。
2. OpsConnector generates TaskContract、ObjectMap、ApprovalGate、AdapterProfile、idempotency key and CloudEvents trace。
3. Dragonwing edge gateway executes locally via RobotAppLayer / VDA 5050 / Open-RMF adapter；network loss does not break authorized local task。
4. Robot scans bin/location with on-device vision；detects mismatch；does not write false success。
5. ExceptionRaised triggers human approval；approval decision and reason code become audit record。
6. Writeback updates inventory exception / CMMS work order / sample lineage with QualcommEdgeProfile and EvidencePacket。
7. ROI panel shows labor minutes saved、exceptions closed、system updates、audit trail、edge latency、rollback readiness。

Ask to Qualcomm:

- RB3 Gen 2 Vision/Core Kit for gateway demo.
- QCS8550 partner/channel guidance for high-performance edge profile.
- IQ / Dragonwing roadmap or early-access feedback.
- AI Hub / QNN / QAIRT office hours.
- Qualcomm Linux / ROS 2 / GStreamer / security / OTA guidance.
- Secure boot, device identity, and OTA recommended path.
- 5-10 robot OEM / SI / warehouse/lab/factory developer introductions.

Claim boundary:

- 不声称 Qualcomm 官方合作、认证或量产承诺；只说 Qualcomm-first validation candidate。
- 不说 OpsConnector 替代 WMS/MES/LIMS/SCADA/robot fleet manager；它是 workflow contract and evidence layer。

## Sources

- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- InOrbit BES：https://www.inorbit.ai/bes
- InOrbit warehouse automation：https://www.inorbit.ai/warehouseautomation
- Formant：https://formant.io/
- Formant intervention requests：https://docs.formant.io/docs/intervention-requests
- Boston Dynamics Orbit：https://bostondynamics.com/products/orbit/
- Open-RMF：https://www.open-rmf.org/
- VDA 5050 releases：https://github.com/VDA5050/VDA5050/releases
- MassRobotics AMR：https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/
- MiR VDA 5050：https://mobile-industrial-robots.com/news-center/mir-supports-interoperability-with-vda5050
- ISA-95：https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard
- B2MML：https://mesa.org/topics-resources/b2mml/
- OPC UA reference：https://reference.opcfoundation.org/
- MQTT 5：https://www.oasis-open.org/standard/mqtt-v5-0-os/
- Sparkplug：https://sparkplug.eclipse.org/specification/version/3.0/
- GS1 EPCIS / CBV：https://ref.gs1.org/guidelines/epcis-cbv/
- CloudEvents：https://cloudevents.io/
- OpenAPI：https://swagger.io/specification/
- AsyncAPI：https://github.com/asyncapi/spec/releases
- RFC 9457：https://www.rfc-editor.org/info/rfc9457/
- HL7 FHIR R4：https://blog.hl7.org/hl7-publishes-fhir-release-4
- NIST SP 800-82：https://csrc.nist.gov/pubs/sp/800/82/r3/final
- China e-fapiao：https://english.www.gov.cn/news/202411/25/content_WS6743b13ac6d0868f4e8ed5e1.html
- EU ViDA：https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en
- EU Data Act：https://digital-strategy.ec.europa.eu/en/policies/data-act
- Qualcomm strategy：https://www.qualcomm.com/news/releases/2026/06/qualcomm-accelerates-diversification-with-comprehensive-strategy
- Qualcomm Linux 2.0：https://www.qualcomm.com/developer/blog/2026/06/qualcomm-linux-2-now-available
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm AI Hub explained：https://www.qualcomm.com/developer/blog/2025/11/qualcomm-ai-hub-explained-workbench-models-apps
- Qualcomm ONNX Runtime Plugin EP：https://www.qualcomm.com/developer/blog/2026/05/qualcomm-launches-the-first-onnx-runtime-plugin-execution-provider
- RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
