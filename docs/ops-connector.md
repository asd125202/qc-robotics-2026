# OpsConnector Pitch

更新时间：2026-07-06。企业系统、标准、厂商 API 和高通平台发布节奏变化较快，真实交付前必须按客户现场的 WMS / MES / LIMS / ERP / SCADA / robot fleet 版本重新验证。

## One-Line Thesis

OpsConnector 是企业系统和机器人执行层之间的工作流合约层：把 WMS/MES/ERP/LIMS/SCADA/人工审批里的业务请求，编译成可验证、可追踪、可审计的 Robot Task Contract，再分发给 RobotAppLayer、EdgeFleet、Open-RMF、VDA 5050、MassRobotics、OPC UA 或厂商 fleet API。

一句话：

> OpsConnector 把机器人动作变成企业记录。

## 01 · Problem

企业机器人部署失败，不是因为机器人不会动，而是因为它进不了企业流程。

- WMS 管订单、库存、波次、库位和报表；机器人需要秒级位置、路径、拥堵、充电、工位容量和异常恢复。
- LIMS/ELN 管样本、协议、结果和 lineage；机器人移液、扫码、交接、称重和样本转移如果不写回系统，就会破坏审计。
- MES/eBR 管材料、人员、设备、批次、质量和偏差记录；机器人平台通常只返回 mission done。
- 缺货、条码不符、温度越界、工位满、门禁未放行、机器人阻塞和人工接管，经常掉进微信群、电话和 Excel。
- 每换一个 WMS、机器人品牌、仓库流程、样本规则或安全区，项目就重新写接口。

## 02 · Current Alternatives Fail

现有方案都解决了一部分，但没有拥有“企业任务到机器人执行再到系统写回”的闭环。

- SI 项目制：能让一个现场上线，但接口、异常处理和回写逻辑常常沉没在项目代码里。
- 机器人 OEM 软件：交付快，但通常服务自家车队和任务模型，容易形成单一厂商锁定。
- WMS / MES 扩展：能发业务任务，但不应承担机器人实时控制、离线执行、地图、路径、PLC interlock 和 OT 安全。
- iPaaS：MuleSoft、Boomi、Workato 懂 SaaS API 和数据流，但不懂 robot state、mission、safety、latency、on-prem edge 和 OT 网络。
- 标准协议：VDA 5050、MassRobotics、Open-RMF、OPC UA Robotics 是好基础，但不覆盖订单语义、样本 lineage、库存写回和商业 SLA。
- Ops dashboards：Formant、InOrbit、Foxglove 等验证了可观测性和运维需求；企业仍需要任务合约、审批、异常补偿和系统记录写回。

## 03 · Solution

OpsConnector 的核心不是“接一个 API”，而是定义一份企业能验收、机器人能执行、系统能写回的任务合约。

主流程：

1. `Intent`：订单、工单、样本请求、FHIR Task、SCADA interlock、QMS 偏差或人工审批进入统一入口。
2. `Contract`：任务 ID、对象、位置、设备需求、审批、验收规则、超时、回滚、审计目标和 trace context。
3. `Dispatch`：按能力注册表选择 RobotAppLayer、VDA 5050、Open-RMF、OPC UA、厂商 API 或人工队列。
4. `Evidence`：采集条码、时间戳、robot run id、传感器、图片、模型版本、异常、接管和签名事件。
5. `Writeback`：把完成、失败、库存移动、样本状态、批记录、QMS 偏差和审计包写回企业系统。

## 04 · Why Now

机器人规模已经上来，下一场竞争是把一次性集成变成可复用软件。

- IFR 报告 2024 年全球工业机器人安装约 54.2 万台，在役约 466.4 万台。
- 中国占 2024 年全球工业机器人安装量 54%，在役超过 200 万台，适合验证多品牌、快交付、私有云版本。
- 多个市场报告把机器人/工业系统集成服务池估在数百亿美元。不要把它作为精确 TAM，而要作为服务池信号：客户一直在为“接进流程”付费。
- VDA 5050 v3.0.0、Open-RMF、MassRobotics、OPC UA Robotics、CloudEvents、OpenTelemetry 等让通用合约层更可行。
- Qualcomm Dragonwing / RB3 / QCS8550 / IQ10 RRD 给 on-prem robot gateway 提供了更清晰的 edge target。

## 05 · Product

第一批产品不做空泛 connector marketplace，而是带 SOP、UI、权限、事件、验收指标、异常处理和写回路径的 workflow pack。

- `WMS Bridge Pack`：订单、波次、拣选、补货、移库、入库、出库、盘点、异常和库存写回。
- `Lab Sample Transfer Pack`：LIMS/Benchling 样本、plate map、协议、审批、条码核验、结果和 audit package。
- `MES / eBR Pack`：工单、批次、设备、物料、操作员、quality hold、deviation 和 electronic batch record 写回。
- `SCADA / OPC Pack`：OPC UA、Sparkplug、PLC interlock、设备状态、门禁放行、alarm 和 historian event。
- `Exception Pack`：缺货、工位满、条码不符、温度越界、机器人阻塞、超时、人工接管、retry/skip/abort。
- `SI Sandbox`：模拟 WMS/LIMS/MES、测试 robot task、dead-letter queue、回归测试和认证培训。

## 06 · Product API Objects

- `TaskContract`：source、idempotency key、business object、robot capability、location、priority、due time、acceptance rule、rollback。
- `EnterpriseObjectMap`：样本、容器、货架、托盘、库位、设备、人员、工单、批次、条码、plate/well 和企业系统 ID 映射。
- `ApprovalGate`：operator、reviewer、role、e-signature、quality hold、SCADA interlock、override reason 和 release token。
- `AdapterProfile`：VDA 5050 order/state、Open-RMF task、MassRobotics telemetry、OPC UA job、Sparkplug、REST/gRPC。
- `EvidenceLedger`：barcode/RFID、timestamp、run id、command log、sensor reading、photo、QNN inference、exception 和 signature。
- `AuditWriteback`：Job Response、inventory update、sample lineage、FHIR Task/Specimen、QMS deviation、eBR record 和 export pack。

## 07 · Market & Business Model

把一次性 SI 人天，产品化成年度订阅、连接器包和工作流包。

中国版：

- 快接入、低改造、多品牌、私有化。
- 包装成样板间 PoC、OEM/SI white-label、私有云、国产系统适配、固定范围交付和 25%-40% 渠道毛利。
- 参考定价：PoC/样板间 10万-30万人民币；单工厂私有化订阅 30万-120万人民币/年；边缘网关 5万-20万人民币/站点/年；连接器包 5万-20万人民币/年；工作流包 8万-30万人民币/年。

海外版：

- 标准合规、on-prem、审计和年度合同。
- 强调 SAP/Manhattan/Blue Yonder 集成、IT/OT 网络隔离、网络安全、审计、SSO、数据驻留和采购安全的年度订阅。
- 参考定价：90 天 pilot 25k-60k 美元；生产站点年费 60k-180k 美元；edge gateway 12k-36k 美元/站点/年；connector pack 10k-30k 美元/年；workflow pack 15k-50k 美元/年；enterprise/on-prem/compliance 150k-500k+ 美元/年。

早期目标：

- 3 个灯塔客户。
- 2 个机器人 OEM connector partner。
- 5 个认证 SI。
- 每个 pilot 都沉淀 1 个 reusable connector pack 和 1 个 reusable workflow pack。

## 08 · Competition & Moat

壁垒不是某一个连接器，而是不断扩大的机器人工作流地图。

竞争/参照：

- InOrbit：最接近 robot orchestration / business execution system。
- Viam / Wandelbots / Intrinsic：robotics platform 和开发平台。
- Formant / Foxglove：robot ops、teleop、data、observability。
- MuleSoft / Boomi / Workato：企业 iPaaS 类比。
- SI 和 robot OEM：最大渠道，也可能是竞争者。

壁垒：

- Connector library。
- Workflow templates。
- On-prem edge runtime。
- Audit corpus。
- Certified SI network。
- Compliance/private-cloud readiness。
- Qualcomm edge evidence。

## 09 · Why Qualcomm

OpsConnector 让 Dragonwing 从机器人推理芯片，升级为企业现场可信执行节点。

Qualcomm-native 架构：

1. `Dragonwing Edge Node`：RB3 Gen 2 / QCS6490 作为开发和轻量网关基线；QCS8550 作为高性能 edge AI box / 多摄像头网关；IQ10 RRD 作为高级 AMR / humanoid / 工业机器人参考目标。
2. `Qualcomm Linux / Ubuntu Runtime`：基于 Qualcomm Linux 或 Ubuntu on Qualcomm IoT，承接 container、OTA、security hardening、real-time 和 local services。
3. `OpsConnector Local Execution Core`：workflow engine、policy engine、capability registry、local queue/cache、idempotent task runner。
4. `Protocol Gateway`：southbound ROS2/DDS、OPC UA、MQTT Sparkplug、Modbus、EtherCAT、CAN-FD、REST/gRPC、vendor SDK；northbound SAP、MES、WMS、SCADA、Kafka、AMQP、REST/webhook、MQTT。
5. `AI Evidence Layer`：AI Hub / QAIRT / QNN 把模型版本、profile、latency、输入摘要、置信度、任务 ID 和设备身份写入 evidence packet。

谨慎表述：

- RB3 Gen 2 / QCS6490 是近期比赛 demo 的现实基线。
- QCS8550 是高性能 on-prem robot operations box profile。
- IQ10 RRD 作为 2026 年后的 Qualcomm robotics roadmap / early-access reference，不写成 2026-07-06 已量产可买。

## 10 · Demo & Ask

7 分钟 demo：

1. 模拟 WMS 补货单或 LIMS 样本转移请求，带货位/样本/条码/审批/验收条件。
2. OpsConnector 生成 TaskContract、ObjectMap、ApprovalGate、AdapterProfile 和 idempotency key。
3. Dragonwing edge gateway 断网仍能执行已授权任务，调用 RobotAppLayer 或 VDA 5050/Open-RMF adapter。
4. 条码不符、工位满或温度越界触发人工审批，不写成功结果，只写 deviation 和 incident。
5. 任务完成后把库存移动、样本 lineage、QNN evidence、operator、版本和 audit pack 写回系统。

向高通要：

- RB3 Gen 2 Vision/Core Kit。
- QCS8550 合作渠道。
- IQ10 RRD early access 或 roadmap 指导。
- AI Hub / QNN / QAIRT office hours。
- Qualcomm Linux / Ubuntu / ROS2 指导。
- secure boot、device identity、OTA 推荐路径。

比赛交付物：

- 一个可运行 Dragonwing edge workflow demo。
- 两个 connector/workflow pack 原型。
- 一个企业审计证据包。
- 一个 SI sandbox。
- 中国/海外两套商业包装和报价模型。

## Sources

- ISA-95：https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard
- OPC UA Robotics：https://reference.opcfoundation.org/specs/OPC-40010-1/
- OPC UA ISA-95 Job Control：https://reference.opcfoundation.org/specs/OPC-10031-4/1
- Sparkplug：https://sparkplug.eclipse.org/specification/
- VDA 5050：https://www.vda.de/en/topics/automotive-industry/vda-5050
- MassRobotics AMR Interop：https://github.com/MassRobotics-AMR/AMR_Interop_Standard
- Open-RMF：https://www.open-rmf.org/
- CloudEvents：https://www.cncf.io/projects/cloudevents/
- OpenTelemetry：https://opentelemetry.io/docs/
- NIST SP 800-82：https://csrc.nist.gov/pubs/sp/800/82/r3/final
- ISA/IEC 62443：https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
- Benchling Developer Platform：https://docs.benchling.com/docs/developer-platform-overview
- Opentrons Python API：https://docs.opentrons.com/python-api/
- FHIR Task：https://hl7.org/fhir/task.html
- 21 CFR Part 11：https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11
- IFR robot demand：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- Viam pricing：https://www.viam.com/pricing
- InOrbit BES：https://www.inorbit.ai/bes
- Foxglove pricing：https://foxglove.dev/pricing
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
