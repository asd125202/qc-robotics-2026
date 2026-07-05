# 能栈 NengStack Pitch

更新时间：2026-07-05。电池安全、充电基础设施、消防、运输、CCC/UN38.3、无线充电和园区电力约束会随国家、行业、化学体系和客户现场变化；真实交付前必须由电气、安全、消防、认证和客户设施团队复核。

## Core Thesis

能栈 NengStack 是机器人补能操作系统：

> 让机器人不断电，让园区不超载。能栈连接机器人、充电桩、换电柜、无线补能点与园区电网，用 Qualcomm 边缘 AI 和 5G 调度，让每台机器人知道何时充、去哪充、充多少。

它不是一个更快的充电桩，而是机器人规模化之后必需的能源协议层、调度层和商业层：

- 机器人 ROI 的关键，不只是单机续航，而是整支车队何时充、在哪里充、是否能稳定自动对接。
- 充电桩、换电柜、无线补能点、电池健康、峰值用电、热安全和任务调度必须在同一套策略里协同。
- 机器人补能影响吞吐、SLA、备件、保险、认证、售后、RaaS 残值和园区电力成本。

一句话：能栈把“能跑多久”升级为“每天能稳定完成多少任务”。

## Five-Thread Research Synthesis

### 1. Fleet Energy Economics

- IFR 报告 2024 年专业服务机器人销售接近 200,000 台，其中交通/物流类 102,900 台。
- AMR/AGV 规模化后，充电基础设施从配件变成独立市场和 uptime 变量。
- opportunity charging 是高利用率车队的现实方向：在装卸、排队、低峰或 staging 时补能，而不是等待长时间离线充满。
- dock 对接成功率、failed handshake、energy delivered、charge time 和 thermal faults 都应该作为运营 KPI。

安全表述：减少充电中断对吞吐的影响，而不是承诺零停机。

### 2. Competitor Practices

行业领先者已经把充电纳入 fleet loop：

- MiR Fleet 评估电量和任务负载，MiR Charge 做自动对接。
- Locus 强调 autonomous opportunity charging 和多形态机器人共享运营。
- OTTO Fleet Manager 根据电量和任务在作业间安排充电。
- AutoStore 通过机器人、电池化学体系、充电窗口和 grid 设计改变系统经济性。
- Geek+ 等仓储 AMR 强调快速 top-up 和部分充电循环。
- WiBotic、Wiferion、Delta、Conductix 等证明无线/导电机会充电是现实选项，但要看 ROI、认证和现场改造。

### 3. Technical Architecture

能栈是能源数据平面：

> BMS telemetry -> battery digital twin -> mission energy scheduler -> dock / charger controller -> site power planner -> RiskLedger / CertForge / RobotLeaseOps / UptimeOS feedback

核心模块：

- Telemetry Ingestion：Linux power_supply、ROS BatteryState、SBS/SMBus、CANopen、BMS、dock sensors、charger APIs。
- Battery Digital Twin：SoC、SoH、cycle count、energy throughput、internal resistance、temperature、certification history。
- Qualcomm Power Budgeter：CPU/GPU/NPU/DSP/ISP/camera/modem 工作负载的 watts、joules/inference、thermal headroom 和 mission reserve。
- Mission Energy Scheduler：任务能耗、回桩 reserve、dock queue、opportunity charging、fleet-level allocation。
- Dock/Charger Controller：contact dock、wireless pad、battery swap、USB-C PD/EPR、小车/开发板、OCPP-style site management。
- Safety Interlocks：no task start、return now、disable fast charge、compute derate、safe shutdown。
- Battery Passport：电池身份、化学体系、容量、SoH、维修、复用、回收和合规证据。

### 4. China Lane

中国版要讲“电池安全 + 充电安全 + 本地运营”：

- CCC 对锂电池/电池包已经相关，但首阶段覆盖便携式电子产品，机器人动力电池要按产品类型判断。
- GB 31241-2022、SJ/T 11852-2022、GB/T 40013-2021、GB/T 41527-2022 是可引用安全信号。
- 机器人电池/无线充电相关标准在推进中，说明市场正在从泛化锂电池走向机器人专用补能规范。
- 中国仓储/园区现场需要充电区、烟温监测、漏电保护、急停、故障断电、损坏电池隔离和书面 SOP。
- 地图、视频、日志、充电数据和运维数据默认中国区本地处理，云端不直接控制安全关键链路。

### 5. Product Design

名称：能栈 NengStack。

定位：

> 机器人正在成群落地。下一个瓶颈不是算法，是补能。

产品层：

- 能源路由：battery-aware task routing and charge-slot reservation。
- 补能中枢：plug-in、wireless、battery-swap、mobile charger 统一管理。
- 边缘 Dock AI：视觉/标记对接、充电桩健康、接触/对准异常检测。
- 电池护照：state-of-health、charge history、mission energy prediction。
- 园区电力协同：峰值限制、负载均衡、储能/光伏/备用电源和需求响应预留。

## Product Modules

### 1. Fleet Energy Scheduler

- 根据 SOC / SOH、任务优先级、charger availability、queue、route cost 和预测需求安排充电。
- 支持 min / target / max SOC，opportunity charging bands，reserve energy 和任务延迟策略。
- 避免多台机器人在高峰同时低电量离线。

### 2. Dock And Charger Mesh

- 充电桩不是附件，而是被监控和调度的 fleet endpoint。
- 记录 dock success rate、failed handshake、alignment error、contact resistance、wireless efficiency、thermal fault 和 service state。
- 支持导电对接、无线垫、换电柜、移动充电车和小型开发板 USB-C PD 场景。

### 3. Battery Passport

- 电池 QR / ID、化学体系、容量、电压、认证、UN38.3、安装日期、循环数、SoH、温度异常、维修、复用和回收。
- 连接 RobotLeaseOps 的残值、折旧、质保 reserve 和 RaaS 计费。
- 连接 CertForge 的 battery / transport / fire-safety evidence。

### 4. Qualcomm Power Budgeter

- 记录 AI inference 的 FPS、latency、watts、joules/inference、thermal delta。
- 在 mission reserve 不足或温度过高时切换 compute profile、降低 FPS、延迟非关键模型或回桩。
- 让 EdgeRuntimeBench 的边缘运行证据进入真实运营策略。

### 5. Site Power Planner

- 规划 dock count、charger kW、panel limit、peak concurrency、peak kW cap 和 load policy。
- 做“10 台机器人 + 3 个补能点”的试点仿真。
- 输出 charger utilization、queue time、peak load、battery replacement risk 和 uptime impact。

## Competition Demo

比赛可以做一个浏览器能量调度演示：

1. 混合车队进入工厂/医院/仓储园区：AMR、机械臂工位、服务机器人和巡检车。
2. 现场同时出现 rush order 与 peak power cap。
3. 不启用能栈：机器人排队、一个任务低电失败、园区负载超限。
4. 启用能栈：系统预约充电槽，把一台机器人安排到无线 opportunity charging，一台去换电，一台延后充电，一台快速补能。
5. 打开机器人卡片：显示电池护照、任务能耗预测、Qualcomm edge workload、dock protocol 和热状态。
6. 输出 simulated KPI：queue time、charger utilization、peak kW、SLA risk、battery replacement window 和 RaaS margin。

## China / Overseas Positioning

中国版：

- 重点讲安全充电区、消防、漏保、急停、损坏电池隔离、UN38.3、机器人电池标准、国内云/私有化。
- 支持导电、无线、换电和本地 fleet dispatch。
- 用中文工单和 UptimeOS 连接电池更换、充电桩维护、备件和服务商。

海外版：

- 重点讲 robot energy OS、OCPP-style charger management、battery passport、EU Battery Regulation、UL battery safety、energy savings share、demand response readiness。
- 连接企业能源管理、设施团队、RaaS 财务和 fleet reliability。

## Qualcomm Value

能栈让 Qualcomm 从“机器人计算大脑”扩展到“机器人能源基础设施大脑”：

- Edge AI：本地 docking perception、充电异常检测、热/电池健康预测。
- Low-power compute：同一个任务在不同 compute profile 下的能耗、热和任务剩余时间可比较。
- Connectivity：5G / Wi-Fi / private network 连接机器人、桩、换电柜和站点控制台。
- Security：机器人、电池、dock 和 charger 都有身份、签名 OTA、审计和证据。
- AI Hub / EdgeRuntimeBench：模型部署不只看 latency，也看 joules/inference 和 mission reserve。

一句话：

> Qualcomm 不只是让机器人更聪明，还能让机器人更会用电。

## Claims To Avoid

- 不说 100% uptime、零停机、固定提升百分比。
- 不说无线充电一定优于导电充电或换电。
- 不把 EV 充电监管直接套到机器人，只作为相邻基础设施信号。
- 不声称所有机器人电池都已 CCC 覆盖；按具体产品分类判断。
- 不承诺 battery life extension，除非有 pilot 数据。

## Sources

- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Interact Analysis mobile robots：https://interactanalysis.com/mobile-robots-market-outpaces-fixed-automation/
- AMR docking market：https://www.futuremarketinsights.com/reports/amr-docking-and-charging-stations-market
- Opportunity charging：https://onepointech.com/opportunity-charging-agv-amr/
- MiR Charge 48V：https://mobile-industrial-robots.com/products/applications/mir-charge-48v
- Locus Origin：https://locusrobotics.com/locusone/fleet/locus-origin-collaborative-robot
- OTTO Fleet Manager：https://ottomotors.com/fleet-manager/
- AutoStore R5 Pro：https://www.autostoresystem.com/news/autostore-launches-new-r5-pro-robot
- Geek+ P-Series：https://www.geekplus.com/hubfs/P-series.pdf?hsLang=en
- WiBotic：https://www.wibotic.com/
- Wiferion：https://www.wiferion.com/en/applications/wireless-power-of-amr-makes-autonomous-mobile-robots-even-more-productive/
- OCPP：https://openchargealliance.org/protocols/open-charge-point-protocol/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Linux power supply class：https://docs.kernel.org/power/power_supply_class.html
- ROS BatteryState：https://github.com/ros2/common_interfaces/blob/rolling/sensor_msgs/msg/BatteryState.msg
- EU Battery Regulation：https://eur-lex.europa.eu/eli/reg/2023/1542/oj/eng
- UL battery safety：https://www.ul.com/services/battery-safety-testing
- GB 31241 notice：https://www.cqc.com.cn/www/col68/559866.html
- SJ/T 11852-2022：https://std.samr.gov.cn/hb/search/stdHBDetailed?id=19BAAB466C76DB66E06397BE0A0AC0DE
