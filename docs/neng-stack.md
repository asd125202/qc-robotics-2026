# 能栈 NengStack Pitch

更新时间：2026-07-06。该版本按 YC / Airbnb 风格 pitch spine 重写：先讲问题，再讲现有方案为什么失败、方案、为什么现在、产品、商业模式、壁垒、为什么 Qualcomm 必须参与、比赛演示和申请支持。

## One-Liner

能栈是机器人车队的能源运营层：

> 把 AMR/AGV/自动叉车的电量、充电、任务、站点功率和电池健康统一调度，让客户用更少备用机器人、更少充电桩、更低峰值功率，完成同样吞吐。

## 1. Problem

机器人规模化之后，瓶颈从“会不会导航”变成“能不能一直干活”。

客户买机器人是为了吞吐、SLA、劳动力替代和 24/7 运营，不是为了管理低电量、充电排队、充电桩故障和电池衰减。随着站点从 5 台机器人走向 50 台、500 台，能源会变成隐藏的 ROI 阀门：

- 低电不是状态，而是未来 30-60 分钟的任务失败风险。
- 多买备用机器人可以掩盖充电停机，但会增加 CapEx、租赁月费、地面拥堵和维护复杂度。
- 多装充电桩会占地、占电路、提高峰值负荷，并带来消防/安全区管理。
- 高温快充、深度放电、错配充电器和异常循环会影响质保、残值、换电计划和事故责任。
- 楼宇 EMS 懂 kW，机器人 FMS 懂任务，但客户需要的是“哪些机器人现在能充，不能让站点超功率”。

## 2. Current Alternatives Fail

现在的系统各管一段，没有一个层负责 robot energy operations。

- OEM fleet manager：MiR、OTTO、Geek+、Hikrobot、HAI 等系统会考虑电量，但能源通常只是任务调度约束，不是跨品牌站点能源产品。
- 充电硬件：导电桩、无线垫、换电柜和移动充电车解决“怎么充”，不解决“谁、何时、以什么功率、为了哪个 SLA 去充”。
- Battery analytics：TWAICE、ACCURE、Voltaiq 等偏 EV/BESS/制造，机器人小电池包的任务上下文和停机成本没有被产品化。
- Building EMS / EV charger management：理解电表、电价和负荷，但不了解 ROS2/VDA5050、地图区域、任务队列和机器人交通。
- RobOps dashboard：InOrbit、Formant 等强在可观测和互操作，但不天然负责电池衰减、charger contention、demand charge 和能源证据。

## 3. Solution

能栈不是充电桩，而是机器人能源运营层。

它接入机器人、充电器、BMS、WMS/WES、站点电表、PV/储能和楼宇 EMS，把电量预测、任务调度、充电预约、电池 SoH、站点功率上限和安全联锁放进同一个优化器。

核心流程：

1. Measure：采集 ROS BatteryState、BMS、dock、charger、Qualcomm edge workload、WMS 任务和站点电力。
2. Forecast：预测每个任务的能耗、回桩 reserve、dock queue、热余量、电池衰减和未来能源缺口。
3. Reserve：为导电桩、无线垫、换电柜、移动充电车和不同功率档预约补能槽。
4. Enforce：NengEdge 在本地执行功率 envelope、充电安全边界和断网时的保守策略。
5. Prove：输出 charger utilization、battery passport、SLA risk、RaaS margin 和合规证据。

## 4. Why Now

2026 年以后，机器人能源会从“附件问题”变成“运营平台问题”。

- IFR 2025 显示，2024 年专业服务机器人销售接近 20 万台，其中运输/物流类约 102,900 台。
- RaaS 把机器人从一次性设备变成月度运营资产，供应商必须对 uptime、维护、电池和能耗负责。
- 仓库、工厂、医院、港口和冷链站点越来越同时运行机器人、AS/RS、EV、HVAC、储能和大量边缘计算，功率容量成为选址和扩容约束。
- EU Battery Regulation 从 2027-02-18 起对特定 EU 市场电池类别引入数字电池护照义务，包括 LMT、EV 和 2 kWh 以上工业电池；机器人 pack 是否适用要按具体 SKU 判断。
- 中国 2026 年国家标准计划已经出现“人形机器人能量管理系统技术要求”等推荐标准项目，说明机器人能源管理正在进入标准化视野，但不能说中国已经有机器人电池护照强制要求。

## 5. Product

先做能源 ROI 副驾驶，再进入闭环能源调度。

第一阶段只读接入，不和 OEM dispatch 正面冲突：

- 连接 robot FMS、chargers、BMS、WMS/WES 和 building meter。
- 输出 required robots、charger ratio、battery risk、charge windows、power ceiling、site expansion plan。
- 让客户知道是否能少买备用机器人、少装桩、降低站点功率风险、延后电池更换。

第二阶段进入闭环：

- Energy Graph：统一建模机器人、电池、dock、charger、任务、地图区域、站点功率和电价。
- NengEdge：站点控制器，负责离线 scheduler、dock mesh broker、power envelope 和本地安全观察。
- Battery Passport Lite：电池 ID、化学体系、容量、SoH、循环、温度事件、维修、复用和 EU passport-ready 字段。
- Site Power Planner：把 OCPP、Modbus、OPC UA、OpenADR、PV/储能、楼宇 EMS 和 robot charge budget 接起来。
- Qualcomm Edge Agent：采集 NPU/GPU/CPU load、QNN model hash、latency、thermal throttling、joules/inference 和 autonomy confidence。

### Reference Architecture

```text
Robots / batteries / docks / meters / PV / ESS / building BMS
        ↓
NengEdge site controller
- offline scheduler
- dock mesh broker
- power envelope enforcement
- ROS2 / VDA5050 / OCPP / Modbus / OPC UA / OpenADR adapters
- local safety observer, not safety authority
        ↓
NengCloud control plane
- fleet energy twin
- battery passport ledger
- optimizer
- telemetry lake
- APIs, webhooks, audit, RBAC
        ↓
UptimeOS / RiskLedger / ScaleFoundry / LeRobot / Qualcomm AI Hub
```

### Core Schemas

```json
{
  "RobotState": {
    "robot_id": "amr-042",
    "mode": "executing|idle|queued|charging|fault|estop",
    "task_id": "task-884",
    "battery_id": "bat-lfp-0007",
    "soc_pct": 42.8,
    "soh_pct": 91.4,
    "energy_rate_w": -620,
    "reserve_soc_pct": 18
  },
  "Dock": {
    "dock_id": "dock-fast-03",
    "capabilities": ["contact_48v", "ocpp_2_0_1", "auto_alignment"],
    "max_kw": 15,
    "state": "available|reserved|occupied|faulted",
    "allowed_kw": 8.5
  },
  "BatteryPassport": {
    "battery_id": "bat-lfp-0007",
    "chemistry": "LFP",
    "rated_kwh": 3.2,
    "usage": {"cycles": 812, "negative_events": 1, "last_soh_pct": 91.4}
  },
  "PowerEnvelope": {
    "site_id": "fulfillment-a",
    "max_import_kw": 420,
    "robot_charge_budget_kw": 96,
    "source": "ems|openadr|operator|tariff"
  }
}
```

## 6. Market And Business Model

卖给停机时真正亏钱的人，而不是卖“省电”。

核心预算来自：

- VP Ops / warehouse automation lead：吞吐、SLA、人工、峰值波次。
- Site GM / supply-chain VP：机器人投资回报和扩容。
- Facilities / energy manager：电路容量、峰值功率、demand charge、改造风险。
- Maintenance manager：电池、充电桩、故障、备件和质保。
- Robot OEM / RaaS provider：机器人月费、残值、换电、电池质保和服务毛利。

海外定价：

- Energy audit + deployment simulation：$10k-$50k / site。
- SaaS orchestration：$20-$80 / robot / month + $50-$150 / charger / month。
- Large site：$2k-$15k / site / month。
- OEM / RaaS embedded：$5-$25 / robot / month + value share on avoided robots, chargers, battery replacement, or warranty reserve。

中国定价：

- 更适合随项目交付，而不是先卖独立 SaaS。
- 规划、仿真、调试和验收包：人民币 5万-30万 / site。
- 轻量软件：人民币 20-100 / robot / month。
- OEM / SI 打包：与机器人 OEM、系统集成商、充电桩伙伴和本地运维云一起报价。

ROI 表述：

- 不是“电费省很多”，而是“一台备用机器人、一个多余充电桩、一次站点电力改造、一次错误电池更换，可能就能支付小站点订阅”。
- 不承诺固定百分比提升；先建立 baseline，再用 charger utilization、low-SOC task failure、queue time、peak kW、battery replacement window 和 SLA risk 量化。

## 7. Competition And Moat

市场被切成五块：

- AMR / OEM fleet managers：Geek+、Hikrobot、HAI、Quicktron、MiR、OTTO、OMRON、KUKA。
- Vendor-neutral robot ops：InOrbit、Formant、SVT、Meili、Open-RMF。
- Charging hardware：HAI Charger、Geek+/Quicktron dock、WiBotic、Wiferion、Delta MOOVair、Rocsys。
- Battery analytics / passport：TWAICE、ACCURE、Voltaiq、Elysia、Minespider、AVL。
- Building EMS / EV charging：AMPECO、Driivz、Virta、ChargePoint/EV Connect、BrainBox AI、GridPoint、Enertiv。

能栈壁垒：

- Cross-brand energy graph：robot、pack、dock、charger、site feeder、task SLA 和电价在同一张图里。
- Mission-aware charging scheduler：按任务 SLA、交通、充电排队、SOC reserve、SoH 和 site power 约束优化。
- Battery responsibility data：把热事件、错配充电、深度放电、快充循环和换电历史接到质保、残值和保险。
- Edge-first deployment：仓库、医院、工厂和港口断网或数据不能出域时，NengEdge 仍能保守执行安全和功率边界。
- WMS/WES stickiness：一旦接入真实任务队列和充电桩网络，能栈会形成运营黏性。

## 8. Why Qualcomm

Qualcomm 可以从机器人“大脑”，延伸到机器人能源基础设施“大脑”。

能栈给 Dragonwing 一个新的高价值边缘 AI 工作负载：实时预测哪些机器人会缺电、哪些电池在加速衰减、哪个站点会超功率、怎样调度才能保住 SLA。

Qualcomm 价值：

- Dock AI：相机/标记对接、无线/导电对准、异常检测和充电桩健康。
- Power budget：按 mission reserve 切换 CPU/GPU/NPU profile，记录 joules/inference。
- Connectivity：机器人、桩、换电柜、BMS、WMS 和站点控制台通过专网/5G/Wi-Fi 同步。
- Trust：电池、dock、charger、机器人都有身份、签名 OTA 和审计证据。
- Ecosystem attach：Qualcomm 可以发布 robot energy operations reference architecture，帮助 OEM 从开发板走向量产。

需要 Qualcomm 支持：

- Dragonwing/RB3/RB5/RB6 技术支持和 QIRP SDK 集成指导。
- 2-3 个 AMR OEM / 系统集成商介绍。
- 1 个仓储、制造或医院后勤设计伙伴试点。
- AI Hub / QNN 证据接口，把模型和能源 profile 同时进入 NengStack。

## 9. Competition Demo

8 分钟 demo：同一批任务，打开能栈后看吞吐、排队和峰值怎么变化。

演示数据：

- 1 个 fulfillment site。
- 24 台 AMR。
- 8 个 dock。
- 36 个 swappable 3.2 kWh LFP packs。
- 500 个 warehouse tasks。
- 250 kW rooftop PV、500 kWh stationary ESS。
- 600 kW normal site cap，420 kW demand-response cap。
- 1 个 dock fault，1 段高峰波次。

演示流程：

1. Baseline：无能栈，低电机器人集中回桩，充电排队，dock fault 被晚发现，站点功率冲高。
2. Read-only copilot：只读接入 FMS/WMS/BMS/电表，输出缺口预测、需要的桩比、备用机器人风险和电池退役窗口。
3. Closed loop：启用预约、机会充电、延迟非关键任务、power envelope 和保守安全边界。
4. Evidence：导出 `battery-passport-lite.json`、`charge-session-ledger.csv`、`site-power-report.pdf` 和 RaaS margin view。

## Claims To Avoid

- 不承诺 100% uptime、零停机或固定提升百分比。
- 不说“所有机器人电池都需要 EU 电池护照”；只说特定 EU 市场电池类别从 2027-02-18 起适用，具体按 SKU 判断。
- 不说 ISO 3691-4 覆盖机器人电池/充电器设计；它不覆盖 power-source requirements。
- 不说 UL 3100 认证整个车队站点；产品安全和站点电气安装是不同范围。
- 不说中国已经强制机器人电池护照；中国更适合表述为机器人能量管理标准正在推进。
- 不说无线充电天然优于导电充电或换电；能栈支持多种补能方式。
- 不说云端可以覆盖安全关键链路；安全联锁必须本地、可审计、人工授权。

## Sources

- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- LogisticsIQ AGV/AMR market：https://www.thelogisticsiq.com/research/automated-guided-vehicles-agv-market
- MiR250 specifications：https://mobile-industrial-robots.com/products/robots/mir250/specifications
- Locus Origin：https://locusrobotics.com/locusone/fleet/locus-origin-collaborative-robot
- Wiferion opportunity charging：https://www.wiferion.com/en/opportunity-charging-industry-standard-power-supply-agvs-amr/
- Open Charge Alliance OCPP：https://openchargealliance.org/protocols/open-charge-point-protocol/
- OpenADR：https://www.openadr.org/
- EU Battery Regulation：https://eur-lex.europa.eu/eli/reg/2023/1542/oj/eng
- ISO 3691-4:2023：https://www.iso.org/standard/83545.html
- ANSI/RIA R15.08 overview：https://www.automate.org/robotics/industry-insights/mobile-robot-standard-r15-08-1-2020-what-you-need-to-know
- UL 3100 overview：https://ulse.org/insight/ul-standards-engagement-robotics-introducing-standard-safety-automated-mobile-platforms-amps/
- OSHA battery charging requirements：https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.178
- PHMSA lithium battery test summaries：https://www.phmsa.dot.gov/training/hazmat/new-un-requirement-test-summaries
- DOE managed charging：https://www.energy.gov/cmei/femp/managed-ev-charging-federal-fleets
- Qualcomm Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- ROS BatteryState：https://github.com/ros2/common_interfaces/blob/rolling/sensor_msgs/msg/BatteryState.msg
- Linux power supply class：https://docs.kernel.org/power/power_supply_class.html
- InOrbit interoperability：https://www.inorbit.ai/interoperability
- Formant fleet observability：https://docs.formant.io/docs/fleet-observability
- WiBotic：https://www.wibotic.com/
