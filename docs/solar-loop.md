# SolarLoop 光伏收入漏洞闭环层 Pitch

更新时间：2026-07-06。

## One-Line Company

SolarLoop 是光伏 O&M 的 action and evidence layer：

> 把 SCADA、逆变器、无人机热像、清洗机器人、气象和工单信号，变成按可恢复 MWh / RMB 排序的动作、复核证据、质保/保险材料和 LeRobot HIL 数据闭环。

## YC-Style Opening

### Problem

光伏电站不缺告警和图片，缺的是把异常变成已复核的恢复收入。

- 业主/IPP 买的不是巡检报告，而是 PR、可用率、收入、质保证据和少跑冤枉路。
- 资产管理人要把异常转成 dollars-at-risk、恢复计划、贷款/税务权益报告和投后审计材料。
- O&M 承包商要用同一队伍覆盖更多 MW，证明 SLA、减少误派工、把清洗/维修做在最值钱窗口。
- 保险/质保团队需要冰雹、热斑、批次缺陷和组件失效的时间戳、影像、性能、处置和复核证据。

### Why Now

- IEA PVPS Snapshot 2026：2025 年全球 PV 累计容量接近 3TW，全年新增约 698GW。
- 中国 2025 年新增光伏 317GW，年底累计 1.2TW，光伏发电量 1.17 万亿千瓦时，同比增长 40%。
- 截至 2026 年 5 月底，中国太阳能装机约 1.26TW，同比增长 16.3%。
- 136 号文后，2025-06-01 之后新建风光项目进入市场化结算，运维动作要考虑电价和消纳窗口。
- IEA PVPS 估算积灰造成全球平均 4%-7% 发电损失；kWh Analytics 发现美国 PV 站点平均低于 P50 预测 8.6%。
- 中国能源行业数据安全管理办法自 2026-07-01 生效，本地/私有化部署成为能源客户采购优势。

### Core Insight

热像图没有价值，已关闭的收入漏洞才有价值。

Raptor Maps、Zeitview、DJI、Percepto、SCADA、逆变器和清洗机器人都能产生信号。SolarLoop 的位置是：

```text
inspection / SCADA / inverter / robot signals
  -> asset graph + dollars-at-risk + dispatch decision
  -> work order / robot / crew / warranty action
  -> verified closure + evidence packet + HIL data
```

## Product

SolarLoop 是光伏 O&M 的闭环修复智能层。它不替代无人机平台、Raptor Maps、SCADA、逆变器门户、CMMS/EAM 或清洗机器人。它坐在这些系统之间，把碎片化信号变成 prioritized, verified remediation loop。

1. Normalize：把站点、区块、逆变器、串、组件、序列号、图像、告警和工单接成资产图谱。
2. Value：融合辐照、气象、电价、弃光、积灰、清洗日志和热像，计算 dollars-at-risk。
3. Decide：区分可清洗、需维修、需复检、质保/保险证据和低置信度人工审核。
4. Dispatch：把动作推给 Maximo/SAP/Power Factors/现场工具、无人机、清洗机器人或人工队伍。
5. Verify：用复扫、性能恢复、人工签核和证据包关闭异常，并生成质保/保险/M&A 材料。
6. Learn：人工改判、误报、失败清洗、复检结果和机器人接管进入 LeRobot HIL 数据闭环。

## Market Wedge

先切最值钱的场景：大、脏、远、入市、少人、需要证据。

中国两个包装：

- 沙戈荒大基地：灰尘、远距离、少人值守、弱网、清洗优化、调度/消纳窗口、本地化部署。
- 分布式/C&I portfolio：可观可测可调可控、自发自用、VPP/现货参与、多站点 O&M 成本下降。

海外两个包装：

- Utility PV recoverable value audit：针对高积灰、高电价、近期冰雹、反复低 PR 或混合设备站点。
- O&M/robot/drone partner layer：让巡检、清洗和维修伙伴更高效，而不是替代他们。

目标买方：

- Utility PV owners / IPP。
- Asset managers。
- O&M contractors。
- C&I rooftop portfolio operators。
- PV+BESS owners。
- Insurer / warranty teams。
- Robot / drone / cleaning partners。

## Business Model

收入模型：

> paid pilot + annual SaaS per MW/site + edge station + mission orchestration + evidence packet + optional success fee

建议价格：

- C&I 组合 90 天试点：18k-45k 美元，覆盖 5-25MW 或 5-50 个站点，巡检/清洗 pass-through。
- Utility PV 90 天试点：55k-125k 美元，覆盖 50-150MW 站点；含边缘站时另加 10k-35k。
- PV+BESS 90 天试点：75k-160k 美元，含 PV loss model 与储能可用性/SOH workflow。
- 年度 Utility SaaS：50-500MW 450-900 美元/MW/年；500MW-2GW 250-550；2GW 以上 150-350；站点最低 10k-18k 美元/年。
- 年度 C&I SaaS：大于 250kW 屋顶 1.5k-4k 美元/site-year，或 1k-2.5k 美元/MW-year。
- BESS add-on：800-2000 美元/MWac-year + 6-15 美元/MWh-year，最低 15k/site-year。
- Edge station：Edge Lite 4.5k-9k setup + 2k-4.8k/year；Edge Pro 15k-35k installed 或 650-1400 美元/月。
- Drone/thermal mission：自带数据 analytics 25-100 美元/MW；turnkey mission 150-500 美元/MW + 10%-20% coordination margin。
- Robot/cleaning mission：SolarLoop orchestration/proof fee 75-225 美元/MW/mission 或 0.04-0.12 美元/panel。
- Warranty/insurance evidence：1.5k-7.5k 美元/claim packet，重大站点事件 5k-25k 美元。

ROI 公式：

```text
Annual gross value =
  recovered energy
+ avoided outage loss
+ cleaning optimization
+ avoided truck rolls
+ warranty / insurance recovery
+ BESS value

recovered energy =
  MWdc * annual MWh/MWdc * realized $/MWh * yield uplift %

ROI =
  (annual gross value - SolarLoop annual cost)
  / SolarLoop annual cost
```

示例：

100MWdc 站点，年发电 180,000MWh，实现电价 35 美元/MWh，年收入约 630 万美元；每恢复 1% 发电量约 6.3 万美元。若 SolarLoop 捕捉 30% 的异常损失、减少一部分无效清洗和巡检，一个 95k-130k 美元/年的合同可解释。

## 90-Day KPIs

- Day 30：90%+ tag mapping，资产层级对齐，数据延迟低于 30 分钟，建立 PR/积灰/可用率 baseline。
- Day 60：识别 2k-6k 美元/MW/年 annualized yield-at-risk，或证明站点已经接近最优。
- Day 90：高优先级告警 verified precision 75%+，false positives <25%。
- Actionability：60%+ 建议进入工单或任务。
- Value：已实现和已承诺年化价值达到首年 ARR 的 2x，或 90 天价值覆盖试点费。
- Ops：inspection/triage time 下降 30%-50%；积灰明显站点清洗成本或无效清洗下降 10%-25%。
- Evidence：80%+ eligible defects/events 生成 warranty/insurance packet。
- Reliability：edge uptime 95%+，无超过 24 小时未处理数据缺口。

## Competition

SolarLoop 不应声称自己是第一套 AI solar inspection、solar digital twin、autonomous inspection system、cleaning robot 或 SCADA replacement。

- Solar inspection analytics：Raptor Maps、Zeitview/Heliolytics、DroneDeploy、Sitemark、Above、SenseHawk。
- Drone autonomy：Percepto、DJI Dock/FlightHub、Skydio Dock、FlytBase。
- Cleaning robots：Ecoppia、Sunpure、Aegeus、Airtouch。
- SCADA / inverter / O&M platforms：Power Factors、AlsoEnergy/PowerTrack、GreenPowerMonitor/DNV、Huawei FusionSolar、Sungrow iSolarCloud、SMA、SolarEdge。
- CMMS / EAM：IBM Maximo Renewables、SAP EAM、IFS Ultimo、60Hertz。
- Insurance / warranty analytics：kWh Analytics、Energetic Capital、Omnidian。

Credible layer:

> SolarLoop owns the action and evidence layer for solar O&M: prioritized remediation, dispatch, verification, and evidence packets across existing systems.

## Moat

- Closure graph：异常、根因、动作、恢复 MWh、证据、签核和索赔结果形成资产级图谱。
- Workflow lock-in：接入 SCADA、CMMS、无人机、机器人、质保和保险系统后，替换成本上升。
- HIL data flywheel：人工纠正、误报、清洗失败、机器人接管和复检结果都回流成 LeRobot 数据集。
- China/global dual lane：中国本地数据面和海外云训练共享 job contract，但满足能源数据安全和客户采购差异。
- Partner coverage：O&M、无人机、清洗机器人、保险和质保伙伴越多，动作与证据网络越强。

## Architecture

现场弱网、粉尘、高温和大面积资产决定了推理不能完全依赖云。SolarLoop 把低延迟视觉、热像、传感器融合和任务安全留在 Qualcomm edge，把跨站点训练、报告和模型迭代放在云端或本地私有云。

Runtime:

- Edge capture：RGB、热像、固定相机、无人机数据、PV telemetry、气象和机器人状态。
- QNN candidates：组件检测、热斑/积灰分割、可清洗/不可清洗分类、小型传感器融合模型。
- ROS 2 loop：inspection、cleaning、verification 用 action 表达，安全状态、相机流和工单事件可追踪。
- CloudTwin：训练 PyTorch 模型、导出 ONNX/QNN artifact、管理数据集、评估和跨站点回放。

## Competition Demo

低压桌面工位证明异常闭环，不冒充现场电站认证。

Demo 使用两套物理分离资产：

1. 5-12V mini PV panel + LED lamp + fuse/PTC + current-limited load + INA219/INA226 V/I sensing。
2. Acrylic/glass dummy panel with printed cells, removable shading cards, soiling film/powder, and capped 5/12V heater pads。

3 分钟演示：

1. 0:00：展示低压、限流、保险、无并网、无高压串、无真实 destructive hotspot。
2. 0:45：添加遮挡和积灰；系统识别 shade 与 soiling，机器人跳过 shade，只处理可清洁 soiling。
3. 1:30：开启 capped heater；系统标记 synthetic hotspot，派人工检查，不让机器人“修热斑”。
4. 2:00：机器人干式软刷清洁，人工 HIL 微调一次路径，记录 correction。
5. 2:40：导出 evidence packet 和 LeRobotDataset episode，展示 AI Hub/QNN edge profile 路径。

Safe claims:

- Competition-safe, low-voltage desktop demonstration。
- Synthetic thermal anomalies, not destructive real PV hot spots。
- Detects demo conditions: clean, soiling, shading, synthetic hotspot。
- Robot closes cleanable soiling exceptions; flags non-cleaning exceptions for human inspection。
- Uses LeRobotDataset-compatible multimodal robot episodes。
- Demonstrates Qualcomm AI Hub/QNN profiling and inference path。

Claims to avoid:

- 不说防止 PV 火灾。
- 不说修复热斑。
- 不说 IEC-compliant inspection。
- 不说已在 utility-scale farms 现场验证。
- 不说 autonomous repair for shading/hotspots。
- 不说 Qualcomm-certified product 或 guaranteed NPU performance。
- 不说 waterless cleaning restores X% output，除非在自有台架实测。

## Why Qualcomm

- SolarLoop 是 Dragonwing 工业边缘 AI 的高可信样板：价值可量化，现场必须本地推理。
- 光伏 O&M 天然具备多传感器、户外机器人、弱网、本地数据面、长期资产运营和可量化 ROI。
- Qualcomm 可以展示从云端训练到边缘 profile、从传感融合到机器人动作、从中国本地部署到海外云训练的完整路径。
- QCS6490/QCS8550/RB3 类节点适合作为相机、传感器、ROS 2、HIL 和 evidence packet 的现场枢纽。

## Sources

- IEA PVPS Snapshot 2026: https://iea-pvps.org/snapshot-reports/snapshot-2026/
- NEA China PV 2025: https://www.nea.gov.cn/20260212/742b8c6a078347b0b39de676c05c5d58/c.html
- NEA China May 2026: https://www.nea.gov.cn/20260625/24f752fd199c4632b7dc7762462585de/c.html
- NDRC / NEA Document 136: https://www.ndrc.gov.cn/xxgk/zcfb/tz/202502/t20250209_1396066.html
- IEA PVPS soiling: https://iea-pvps.org/fact-sheets/fs-soiling-losses/
- Raptor Maps 193GW analysis: https://www.ourenergypolicy.org/resources/benchmarking-solars-performance-gap-insights-from-193gw-of-analysis/
- NEA AI + Energy: https://www.nea.gov.cn/20260508/4dae97ca01d348e4871bb8654be34b3a/c.html
- Energy Data Security Measures: https://www.nea.gov.cn/20251212/f8ee9d3f829641cb9cc4f1e9405e794a/c.html
- SEIA Solar Market Insight: https://www.seia.org/research-resources/us-solar-market-insight/
- LBNL utility PV OpEx: https://emp.lbl.gov/publications/benchmarking-utility-scale-pv
- LBNL utility solar 2024: https://emp.lbl.gov/publications/utility-scale-solar-2024-edition
- Raptor Maps / DJI: https://enterprise.dji.com/ecosystem/raptor-maps
- Zeitview Heliolytics: https://www.zeitview.com/news/zeitview-acquires-heliolytics-becoming-the-market-leader-in-solar-aerial-inspections
- DroneDeploy renewables: https://www.dronedeploy.com/solutions/renewable-energy
- Percepto solar: https://percepto.co/solar-energy/
- Ecoppia: https://www.ecoppia.com/
- Sunpure: https://www.sunpuretech.com/
- Power Factors: https://www.powerfactors.com/
- IBM Maximo Renewables: https://www.ibm.com/products/maximo/renewables
- IEC TS 62446-3: https://webstore.iec.ch/en/publication/28628
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot HIL: https://huggingface.co/docs/lerobot/hil_data_collection
- Qualcomm AI Hub: https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN EP: https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
