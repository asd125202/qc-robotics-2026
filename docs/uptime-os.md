# UptimeOS Pitch

更新时间：2026-07-05。售后服务、备件、质保、SLA、远程诊断和数据合规随地区、行业和客户合同变化很大；真实商业报价前必须按目标市场、客户场景和服务伙伴重新核算。

## Core Thesis

UptimeOS 是机器人队列的售后操作系统：

> 机器人已经有运行时操作系统，现在还需要 aftersales operating system：健康护照、预测维护、远程诊断、备件图谱、技师工单、质保证据、RaaS 可用率和二手残值都在同一个服务数据平面里闭环。

它不是又一个调度器，也不是替代 OEM 售后团队。UptimeOS 解决的是商业机器人规模化后最现实的瓶颈：

- 机器人能部署，但不能稳定持续在线。
- 故障诊断分散在 OEM 门户、日志包、微信群、表格、备件 PDF 和现场工程师经验里。
- RaaS 把硬件、折旧、维护、备件和 SLA 风险从客户转移给运营商。
- 中国和海外市场对服务响应、备件、合规交接和客户安全的要求不同。
- Qualcomm 机器人需要把边缘 AI、连接、安全启动、热/功耗/传感数据变成长期服务能力。

一句话：UptimeOS 把机器人从“能交付的设备”变成“能持续运营的资产”。

## Five-Thread Research Synthesis

### 1. Service Economics

商业机器人售后的经济锚点是 downtime、MTTR、MTBF、一次修复率、备件可得性和现场服务效率。

- IFR 报告 2024 年全球工业机器人安装约 542,000 台，运行存量约 4.664M 台。
- 专业服务机器人 2024 年销售接近 200,000 台，RaaS fleet 增长 31%，物流 RaaS 增长 42%。
- Siemens 2024 downtime study 估计全球 500 大工业企业每年因非计划停机损失接近 1.4T 美元。
- 机器人维护横跨软件、电气、机械、控制、传感器、网络和现场环境。

安全表述：不要说“机器人平均每小时停机损失多少”。更稳妥是说机器人在制造、仓储、医疗和服务流程中嵌入关键工序，停机成本必须按客户流程计算。

### 2. Competitive Signals

市场已经出现多个碎片化层：

- Formant / InOrbit / Foxglove：机器人运维、数据、日志、事件和远程介入。
- Locus / MiR / AutoStore / Geek+ / GreyOrange / Vecna：仓储机器人把服务、监控、支持和持续优化打包到运营模型里。
- KUKA / FANUC / ABB：工业 OEM 通过 connected services、predictive maintenance、备份、远程访问和服务协议变现 uptime。

UptimeOS 的机会不是复制单点功能，而是把跨 OEM 资产护照、服务工单、备件、质保、RaaS、RiskLedger 和 CertForge 证据连接起来。

### 3. China Lane

中国不是试点市场，而是规模化存量市场。客户把售后能力当作采购门槛：

- 重点是 7x24 响应、400 / 企微 / 微信小程序报修、本地备件库、远程诊断、现场工程师和服务站。
- AGV/AMR 项目通常要接 WMS/WCS/MES/ERP、PLC、输送线、电梯、门禁、消防联动、充电桩和现场网络。
- 服务机器人售后更零售化：到货安装、回访评价、备用机/快速换件和门店级响应很重要。
- 商业模式应把维保、备件、软件订阅、驻场服务、延保和授权服务商做成可报价 SKU。

### 4. Technical Architecture

最强架构不是 dashboard，而是 service data plane：

> RobotCoreOS edge agent -> telemetry / log bundle / evidence capsule -> service twin -> prediction / ticket / parts / OTA workflow -> RiskLedger / CertForge / LeRobot feedback

关键模块：

- Edge Health Agent：ROS diagnostics、CAN/EtherCAT、BMS、热区、NPU/GPU/CPU、校准漂移。
- Remote Diagnostics：低带宽健康探针、日志 tail、topic snapshot、审批式远程动作。
- Predictive Maintenance：健康分、异常检测、RUL、原因码和服务计划。
- FRU / Spares Graph：BOM 到可更换件、兼容性、库存、替代件和提前备件。
- Technician Mobile：QR 扫码、离线 checklist、照片、备件消耗、客户签收。
- OTA Orchestrator：签名发布、canary、A/B 回滚、SafetyOps gate 和 CertForge 证据。
- Log Bundle Builder：MCAP / rosbag slice、metrics、视频脱敏、manifest hash 和 custody log。

### 5. Product Positioning

最强名称：UptimeOS。

定位语：

> Every robot needs a service record, a health score, and an uptime contract.

网站主线：

1. 机器人从 demo 进入租赁、仓库、医院、工厂、餐饮、园区和校园。
2. 商业瓶颈从“能不能部署”转向“能不能持续在线”。
3. UptimeOS 把健康护照、预测维护、远程诊断、备件图谱、技师派单、质保证据和 RaaS 可用率做成一个服务操作系统。
4. Qualcomm 让诊断和异常检测尽量在边缘发生，云端负责服务编排、证据和学习闭环。

## Product Modules

### 1. Robot Health Passport

- Robot id、serial、customer、site、SKU、Qualcomm SoC、OS image、QNN/QAIRT version。
- 电池循环、SoH、运行小时、里程、温度、传感器校准、固件、模型、维修历史。
- 质保、SLA、服务等级、授权服务商和数据出境/驻留策略。

### 2. Edge Diagnostic Agent

- 采集 ROS 2 diagnostics、ros2_control、CAN、EtherCAT、BMS、温度、风扇、NPU/GPU/CPU、网络、定位、充电和安全状态。
- 离线缓存、低带宽摘要、本地脱敏和异常优先上报。
- 默认只做诊断与证据采集，不插入安全关键控制链。

### 3. Incident Packet

每个故障自动生成支持工单所需证据：

- 任务上下文、地图位置、最近命令、健康信号、错误码、日志片段、视频/MCAP ref。
- 疑似原因、置信度、建议检查步骤、需要备件和升级路径。
- RiskLedger hash / custody log，避免售后争议。

### 4. Spares And FRU Graph

- ScaleFoundry 输出 BOM / AVL / FRU 映射。
- 按 robot serial 判断兼容备件、库存、替代件、交期、质保状态。
- 电池、驱动轮、脚轮、激光雷达、深度相机、急停、防撞条、控制板、通信模组、线束、关节、电机和减速器优先建模。

### 5. Technician Mobile Workflow

- QR 扫码识别机器人和合同。
- 离线 checklist、远程专家协助、照片/视频、备件消耗、客户签收和回访。
- 自动计算 SLA clock、first-time-fix、MTTR、重复故障和服务成本。

### 6. RaaS Uptime Ledger

- 连接 RobotLeaseOps：月付机器人必须有可用率、服务响应、维护履约、残值和违约损失数据。
- 连接 CertForge：OTA、维修、替换、说明书和合规资料变化进入证据包。
- 连接 LeRobot：失败片段进入数据飞轮，训练和回归测试后再回到 Qualcomm edge。

## Competition Demo

比赛演示可以做成一条完整售后闭环：

1. 机器人 AMR + 小机械臂进入客户现场，UptimeOS 显示健康护照。
2. 电机电流和温度出现异常，Qualcomm edge agent 本地检测到趋势。
3. 系统生成 incident packet：任务、位置、日志、MCAP、热状态、BMS、模型版本和疑似部件。
4. Spares Graph 推荐驱动轮/减速器 FRU，检查本地备件库和授权服务商可用性。
5. 自动创建工单：技师扫码、离线 checklist、拍照、消耗备件、客户签收。
6. 维修后健康分恢复，RiskLedger 更新证据，RobotLeaseOps 更新 SLA，CertForge 记录变更，LeRobot 标记失败 episode。
7. Dashboard 展示 MTTR、first-time-fix、服务毛利、备件周转和续约风险。

## China / Overseas Positioning

中国版：

- 400 / 企微 / 微信小程序入口。
- 区域备件中心、授权服务商、重点城市 24-48 小时到场。
- 中文故障码、中文工单、中文说明书、国标电源、SRRC / CCC / CR / EMC 资料交接。
- WMS/MES/PLC/电梯/门禁/消防接口模板，服务商培训认证。

海外版：

- OEM / RaaS / enterprise operator support portal。
- ServiceNow / Jira / Zendesk / Dynamics adapter。
- SOC2 / ISO 27001-ready evidence posture, OT segmentation, audit log, RBAC, JIT remote access。
- spare-parts depot、RMA、warranty reserve、residual value、insurability and bankability data。

## Qualcomm Value

UptimeOS 让 Qualcomm 从“机器人上车前的计算平台”延伸到“机器人全生命周期服务智能”：

- Edge AI：在本体侧做异常检测、视频/日志压缩、热/电池/电机健康判断。
- Connectivity：Wi-Fi、5G、专网、离线缓存和恢复同步支撑远程诊断。
- Security：安全启动、设备身份、签名 OTA、RBAC 和审计日志支撑客户信任。
- AI Hub / QNN：模型版本、runtime profile、latency、功耗和回滚证据进入健康护照。
- Product longevity：长期供货、BOM、PCN/PDN、备件和安全更新变成采购与续约证据。

一句话：

> Qualcomm 不只负责机器人“跑起来”，还可以通过 UptimeOS 参与机器人“活得久、修得快、续得上”的商业价值。

## Claims To Avoid

- 不承诺所有客户都能达到固定 uptime。
- 不承诺自动替代 OEM 或实验室质保判断。
- 不说 AI 自动判断法律责任；只能做故障建议和证据整理。
- 不直接控制安全关键链路；远程动作必须有 RBAC、审批、审计和 SafetyOps gate。
- 不声称跨所有品牌无缝兼容；先说 Qualcomm-powered / RobotCoreOS-first，再开放 adapter。

## Sources

- IFR industrial robots 2025：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots 2025：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Siemens downtime study 2024：https://assets.new.siemens.com/siemens/assets/api/uuid:1b43afb5-2d07-47f7-9eb7-893fe7d0bc59/TCOD-2024_original.pdf
- KUKA service：https://www.kuka.com/en-us/services/service_robots-and-machines/robot-service-maintenance-servicing
- Motoman spare parts：https://www.motoman.com/en-us/service-training/spare-parts
- BCG field service：https://www.bcg.com/publications/2025/the-next-frontier-of-field-service
- IBM first-time fix rate：https://www.ibm.com/think/topics/first-time-fix-rate
- Formant：https://formant.io/
- InOrbit：https://www.inorbit.ai/
- Foxglove：https://foxglove.dev/
- Locus RaaS：https://locusrobotics.com/why-locus/robots-as-a-service
- MiR Fleet Enterprise：https://mobile-industrial-robots.com/products/software/mir-fleet
- FANUC ZDT：https://www.fanuc.eu/eu-en/accessory/software/zdt-zero-down-time
- ABB Connected Services：https://www.abb.com/global/en/areas/robotics/services/data-driven-services/connected-services
- Geek+ after-sales signal：https://www.zhineng518.com/page119?article_id=3646&brd=1
- Hikrobot after-sales：https://www.hikrobotics.com/cn/mobilerobot/service/aftersale/site/
- Estun service network：https://www.estun.com/oemservice/
- AUBO South China service center：https://www.aubo-robotics.cn/news-info/134
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Qualcomm industrial AI and private 5G：https://www.qualcomm.com/news/releases/2026/03/qualcomm-brings-onpremises-industrial-ai-and-connectivity-to-a-s
- Qualcomm Edge AI overview：https://www.qualcomm.com/developer/blog/2025/05/qualcomm-iot-edge-ai-overview-embedded-world-2025
- ROS diagnostics：https://github.com/ros/diagnostics
- MCAP：https://mcap.dev/
- Mender OTA：https://mender.io/engineers/how-mender-works
- Uptane OTA：https://uptane.org/docs/latest/standard/uptane-standard
