# OpsConnector Pitch

更新时间：2026-07-05。企业系统、标准和厂商 API 变化较快，真实交付前必须按客户现场的 WMS / MES / LIMS / ERP / SCADA 版本重新验证。

## Core Thesis

RobotMac 如果要真正进入工厂、仓库和实验室，就不能只会“执行一个机器人任务”。企业购买机器人之后，真正难的是把机器人接入已有业务流程：

> OpsConnector = enterprise work order + connector adapters + edge gateway + robot task contract + event writeback + audit trail + security policy。

它把 RobotMac 从机器人产品，变成能接入客户 WMS、MES、ERP、LIMS、ELN、PLC/SCADA、operator approval 和 incident workflow 的企业系统节点。

## Why This Matters

并行研究得到的结论很一致：机器人硬件不是最大价值池，集成才是商业化瓶颈。

- MIT Sloan 的机器人采用研究指出，集成到生产流程往往是主要障碍，成本可能达到机器人本体的数倍。
- 系统集成服务是一个巨大市场，企业愿意为缩短项目周期和降低失败概率付费。
- Viam、Formant、InOrbit、Intrinsic、Foxglove 等平台验证了机器人客户需要 API、OTA、teleop、incident、数据、日志和 workflow。
- 仓储机器人通常不是直接接 ERP，而是通过 WMS / WES / WCS / RCS / fleet software 完成任务下发、执行和确认。
- 实验室自动化正在形成 LIMS / ELN 负责科学意图和记录，机器人 workcell 负责物理执行，中间层负责 protocol、events、results 和 lineage 的模式。

OpsConnector 的目标不是替代所有企业系统，而是把 RobotMac 变成这些系统能理解、能审计、能验收的执行端。

## Research Synthesis

### 1. Standards Layer

- ISA-95 / IEC 62264 是企业业务系统和制造执行系统之间的语义锚点。
- OPC UA Robotics 适合把机器人资产、状态和 condition monitoring 暴露给 MES / SCADA / maintenance 系统。
- OPC UA for ISA-95 Job Control 适合把 job order、job response、queued / executing / completed 状态映射到机器人任务。
- MQTT + Sparkplug 适合轻量边缘 telemetry、状态发现和 unreliable network 下的事件传输。
- VDA 5050 / MassRobotics / Open-RMF 更适合作为 AMR / 多机器人 / facility orchestration 的 southbound adapter。

### 2. Warehouse Layer

仓库机器人通常遵循：

```text
ERP / WMS
  -> WES / WCS / RCS / fleet software
  -> robot missions
  -> task confirmations / exceptions
  -> WMS inventory / order state update
```

OpsConnector 应该提供 canonical warehouse task model：orders、waves、picks、putaway、replenishment、transport、inventory adjustments、confirmations、exceptions 和 cancellations。

### 3. Lab Layer

实验室自动化通常遵循：

```text
LIMS / ELN request
  -> protocol / run plan
  -> deck and sample verification
  -> robot execution
  -> event and error capture
  -> result artifact upload
  -> sample lineage and status writeback
```

OpsConnector 应该先定义 `LabRun` contract，再接 Opentrons、Automata LINQ、Benchling、Synthace、HighRes、Biosero 或 legacy CSV worklist。

### 4. Platform Layer

Viam / Formant / InOrbit / Foxglove / Intrinsic / Wandelbots / MoveIt Pro 说明市场已经很拥挤。OpsConnector 不应该再做一个 dashboard，而应该做：

- Connector templates。
- Workflow contracts。
- Edge buffering。
- Human approval。
- Exception handling。
- Audit / compliance log。
- Robot skill and business-system action binding。

### 5. Buyer Economics

企业采购关注的是 TCO、停机风险、IT/OT 安全、项目周期、内部改变成本和持续维护。OpsConnector 因此可以成为付费产品：

- Connector Pack：WMS / MES / LIMS / ERP / SCADA。
- SI Accelerator：给系统集成商的模板、测试 sandbox 和认证。
- Enterprise Security Pack：SSO、RBAC、TLS、certificate、audit、network segmentation、offline mode。
- Workflow Pack：带 SOP、UI、acceptance metrics、operator handoff 和 result writeback 的垂直行业包。

## Product Modules

### 1. Northbound Connectors

连接企业意图和记录：

- WMS / WES / WCS：订单、波次、拣选、搬运、库存和异常。
- MES / MOM：工单、工序、设备、产线状态和质量记录。
- LIMS / ELN：样品、协议、实验请求、结果、批次和 lineage。
- ERP：采购、库存、客户订单、项目成本和财务归档。

### 2. Robot Task Contract

把企业任务映射为机器人可执行合约：

- Task type。
- Input object / sample / location。
- Target location / station。
- Priority / due time。
- Required skill。
- Human approval rule。
- Safety boundary。
- Success and failure writeback。

### 3. Southbound Adapters

连接机器人执行层：

- RobotMac skill runtime。
- EdgeFleet。
- Open-RMF。
- VDA 5050。
- MassRobotics AMR Interop。
- Existing vendor fleet managers。

### 4. Edge Gateway

现场 edge gateway 负责：

- 本地缓存和断网继续运行。
- 低延迟任务下发。
- OT / IT 网络分区。
- Idempotent task execution。
- Retry / dead-letter queue。
- Audit event signing。

### 5. Security And Governance

企业集成必须默认包含：

- Device identity。
- TLS / certificates。
- RBAC / SSO。
- MQTT broker ACL。
- OPC UA role mapping。
- Schema validation。
- Integration health monitoring。
- Audit logs and export。

## Competition Demo

初赛可以展示 mock workflow：

1. 一个 WMS / LIMS task 被创建。
2. OpsConnector 把它转换成 RobotMac task contract。
3. RobotAppLayer 调用 observe / move / grasp / record。
4. RobotCoreOS 在本体执行并记录事件。
5. EdgeFleet 展示状态，SafetyOps 记录权限和异常。
6. OpsConnector 把 success / exception / result artifact 写回企业系统。

这比单纯机械臂 demo 更强，因为它回答了企业客户最关心的问题：机器人如何进入我的流程？

## Why Qualcomm Should Care

OpsConnector 让 Qualcomm edge 不只是机器人推理设备，而是企业 IT/OT 流程里的可信执行节点：

- 业务任务在云或企业系统创建。
- 本体执行在 Qualcomm edge。
- 现场可靠性由 RobotCoreOS / EdgeFleet 保障。
- 运行证据进入企业 audit trail。
- 新任务数据回到 CloudTwin / TrainRouter。

这让 Qualcomm 进入的不只是单台机器人，而是客户业务系统和系统集成商交付链路。

## Sources

- OPC UA Robotics：https://reference.opcfoundation.org/specs/OPC-40010-1
- OPC UA ISA-95 Job Control：https://reference.opcfoundation.org/specs/OPC-10031-4
- ISA-95 standard：https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard
- MQTT 5.0 specification：https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
- Sparkplug 3.0 specification：https://sparkplug.eclipse.org/specification/version/3.0/documents/sparkplug-specification-3.0.0.pdf
- VDA 5050：https://www.vda.de/vda-5050
- MassRobotics AMR Interoperability：https://github.com/MassRobotics-AMR/AMR_Interop_Standard
- Open-RMF：https://www.open-rmf.org/
- Viam fleet management：https://www.viam.com/platform/fleet-management
- Formant integrations：https://docs.formant.io/en_US/docs/integrations-overview
- InOrbit orchestration：https://www.inorbit.ai/orchestration
- Foxglove fleet docs：https://docs.foxglove.dev/docs/fleet
- Opentrons HTTP API：https://docs.opentrons.com/http/api_reference.html
- Automata LINQ docs：https://docs.automata.tech/
- Benchling automation：https://www.benchling.com/automation
- MIT Sloan robot integration：https://mitsloan.mit.edu/ideas-made-to-matter/how-smaller-firms-can-harness-potential-collaborative-robots
- NIST SP 800-82：https://csrc.nist.gov/pubs/sp/800/82/r3/final
