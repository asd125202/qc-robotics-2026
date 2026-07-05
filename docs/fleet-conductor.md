# FleetConductor Pitch

更新时间：2026-07-05。

## Core Thesis

机器人越多，现场越像一个小机场：不同厂商、不同地图、不同调度器、不同充电桩和不同异常处理流程，最后变成抢路、抢梯、抢桩、任务断链和人工电话协调。

FleetConductor 是机器人塔台：

> 用 Qualcomm 边缘硬件在现场运行一座本地机器人指挥室，把多品牌机器人、地图交通、门梯充电、WMS/MES 任务、安全事件和 LeRobot 数据飞轮接成一个设施级操作系统。

它不是替代所有厂商 fleet manager，而是连接它们：

- MassRobotics-style telemetry 用于共享状态和可视化。
- VDA 5050 用于 AGV/AMR 与 master control 之间的订单、状态、地图和能力协商。
- Open-RMF-style adapters 用于多车队、门、电梯、充电、交通和共享资源调度。
- Vendor REST / MQTT / OPC-UA / ROS 2 adapters 用于实际项目落地。

## Why This Matters

客户买机器人不是为了多一个 dashboard，而是为了让现场流程更稳：

- WMS/MES/ERP 的订单要变成机器人任务。
- 机器人需要共享走廊、门、电梯、装卸点、禁区和充电位。
- 云断开时，现场仍要能派单、避堵、充电和处置异常。
- 安全事件、急停、堵塞、低电、任务超时和人工接管要可追溯。
- 成功任务、失败片段和绕行轨迹要进入 DataFlywheel，反哺下一轮训练和策略验证。

这正是 Qualcomm 边缘硬件可以放大的价值：云端负责训练和分析，现场边缘负责实时协同与连续运行。

## Product Modules

### 1. Edge Tower Runtime

部署在工厂、仓库、医院或实验室现场的边缘塔台。

- 本地运行任务队列、交通调度、地图服务、fleet registry、incident manager 和 event log。
- 云端断开时保持 store-and-forward：继续调度、继续记录，恢复后再同步。
- 云不在实时控制闭环里，避免每次任务和交通决策依赖公网往返。

### 2. Adapter Hub

把“不同语言”的机器人和设施系统转成统一语义层。

- VDA 5050 v3/v2 MQTT / JSON adapter。
- Open-RMF fleet adapter、door/lift/charger adapter。
- MassRobotics-style status feed。
- Vendor REST / WebSocket / MQTT / ROS 2 / Nav2 bridge。
- OPC-UA / BACnet / BMS / WMS / MES / ERP connector。

### 3. Live Facility Map

地图不是背景图，而是可执行的交通合同。

- 多楼层地图、车道、会车点、禁行区、门、电梯、装卸点、充电区和等待点。
- 支持 vendor-map reference、coordinate transform、map versioning 和 floor/lift topology。
- 把走廊、电梯、门、充电桩和装卸位变成可预约、可冲突检测的资源。

### 4. Task Orchestrator

把企业系统里的任务拆成机器人可执行流程。

- 从 WMS/MES/ERP/LIMS/HIS 接入订单、工单、样本、物料、清洁和配送任务。
- 按机器人能力、位置、电量、payload、优先级、SLA、区域权限和交通成本分配任务。
- 保留人工审批、暂停、重派、降级和 fallback route。

### 5. Incident Command

异常不是弹窗，是处置流程。

- 低电、堵塞、传感器遮挡、急停、任务超时、门梯失败、网络异常进入事件时间线。
- 自动触发重路由、隔离、等待、人工接管、视频快照和复盘包。
- 定位为运营安全和可追溯层，不替代机器人本体安全控制器或现场风险评估。

### 6. LeRobot DataFlywheel

每一次绕行都是下一版模型的数据。

- 成功轨迹、失败轨迹、人工接管、异常视频、状态日志和地图上下文打包成训练样本。
- 进入 LeRobot-compatible dataset、仿真回放、策略评估和 Qualcomm edge deployment gate。
- DataFlywheel 让现场运行和云端训练形成闭环，而不是只做监控看板。

## Competition Demo

比赛可以用模拟设施和真实桌面机器人组合展示：

1. 一个网页/本地 dashboard 展示多楼层地图、两台 AMR、一台机械臂、一个电梯和一个充电桩。
2. WMS mock order 进入 Task Orchestrator，系统选择机器人并安排路线。
3. 电梯冲突或低电事件出现，FleetConductor 重新排队、改道或插入充电任务。
4. 网络云端断开，Edge Tower Runtime 继续执行并记录事件。
5. 异常片段导出为 LeRobot/DataFlywheel 样本，展示“现场运行数据反哺训练”。

## Why Qualcomm Should Care

Qualcomm 不能只在单台机器人上展示 AI 推理，还应该成为现场机器人协同的边缘节点：

- 多摄像头和视频能力支持异常快照、远程接管和现场可视化。
- Wi-Fi / private 5G / connectivity 支持现场多机器人网络。
- NPU/GPU/DSP 支持本地异常检测、地图语义和视频摘要。
- RB / QCS / IQ / Dragonwing 硬件可以成为 factory edge tower appliance。
- AI Hub 和云训练工作流把现场数据回灌到模型优化和边缘部署。

FleetConductor 让 Qualcomm 从“单机 edge AI”扩展到“设施级机器人操作系统”的位置。

## Claims To Avoid

- 不声称开箱支持所有机器人；真实项目需要 adapter、地图对齐、厂商 API 权限和现场 commissioning。
- 不声称 MassRobotics、VDA 5050 或 Open-RMF 能单独解决全部互操作问题。
- 不声称 guaranteed collision-free、安全认证、无人监管或零停机。
- 不直接控制消防、电梯或门禁系统；应通过授权 BMS/PLC/设施接口接收事件和发起请求。
- 不把 Wi-Fi/5G 描述成安全关键控制链路，除非有站点设计、QoS 和安全认证证据。

## Sources

- VDA 5050：https://www.vda.de/en/topics/automotive-industry/vda-5050
- VDA 5050 GitHub：https://github.com/VDA5050/VDA5050
- Open-RMF：https://www.open-rmf.org/
- Open-RMF docs：https://openrmf.readthedocs.io/en/latest/
- Open-RMF fleet adapter tutorial：https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html
- MassRobotics AMR Interoperability：https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/
- MassRobotics AMR GitHub：https://github.com/MassRobotics-AMR/AMR_Interop_Standard
- Qualcomm Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- NIST SP 800-82 Rev. 3：https://csrc.nist.gov/pubs/sp/800/82/r3/final
- ISO 3691-4：https://www.iso.org/standard/83545.html
