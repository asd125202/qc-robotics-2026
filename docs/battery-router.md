# BatteryRouter 电池第一小时路由层 Pitch

更新时间：2026-07-06。

说明：`BatteryRouter` 是本页使用的产品名；`BatteryLoop` 只作为内部概念名。市场上已有 Stena 旗下 BatteryLoop 等同名实体，本项目不代表任何关联、授权或合作。

## One-Line Company

BatteryRouter 是退役电池的第一小时路由层：

> 读取编码、护照/BMS/诊断、外观、热像、物流、所有权、召回和下游报价，把每个 pack/module 路由到复用、维修、梯次利用、拆解、材料回收、隔离或退回，并留下可审计流向证据。

## YC-Style Opening

### Problem

电池回收最危险、也最浪费钱的一步，是第一小时不知道它该去哪。

- 回收商怕错混 NMC/LFP、入厂资料不全、危险品仓储变长、拒收/返运和低价值黑粉污染利润。
- OEM 回收网络要证明每块电池从经销商、维修点、拆解厂到综合利用企业的流向和责任。
- 梯次利用商买错一批不可用或高风险电池，会拖住测试、质保、项目交付和融资模型。
- 保险、拍卖和车队的事故车电池价值不明，处置慢，安全存放天数高，残值无法快速释放。

### Why Now

- IEA 2026：2025 年全球 EV 电池部署约 1.2TWh，同比增长接近 30%。
- IEA 2026：2025 年全球新增电池储能约 108GW，同比增长约 40%。
- 工信部口径：2025 年中国新能源汽车废旧动力电池综合利用量超过 40 万吨，同比增长 32.9%；2030 年退役量预计超过 100 万吨/年。
- 2026-04-01，中国《新能源汽车废旧动力电池回收和综合利用管理暂行办法》生效。
- 2026-07-01，GB 38031-2025 生效，动力电池安全证据的重要性提升。
- 2027-02-18，欧盟电池护照开始覆盖 EV、LMT 和大于 2kWh 的工业电池。

### Core Insight

电池的价值不在“仓库里”，而在下一站匹配得是否正确。

BatteryRouter 不是 SOH 仪表盘，也不是回收厂。它要占据的位置是：

```text
first-life asset owner
  -> routing intelligence + transaction + audit trail
  -> recycler / refurbisher / second-life / disassembly / quarantine / return
```

## Product

BatteryRouter 是 first-life asset owner 和下游去向之间的路由交易层。它读取护照、BMS/telematics、诊断证书、安全状态、化学体系、位置、所有权、质保、损伤和物流约束，再把每块电池路由到合法且最值钱的下一环。

1. Ingest：导入 QR/编码、护照、BMS/车队数据、诊断证书、召回、运输和所有权信息。
2. Inspect：站点本地采集 RGB、热像、外观、标签、重量、mock/真实可用诊断字段和人工备注。
3. Decide：输出 reuse、repair、second-life、disassembly、recycle、quarantine、return-to-owner 等 route。
4. Transact：连接合规综合利用企业、回收商、梯次利用商、维修点、承运商和业主审批。
5. Record：生成 chain-of-custody、数字身份更新、证据哈希、报送字段和下游接收回执。
6. Learn：下游接收、拒收、收益、事故、质保和人工改判回流到 route outcome graph。

## Market Wedge

先卖给回收商和梯次利用商，因为他们每天都在为错路由付钱。OEM 回收网络空间更大，但销售周期长。

第一批买家：

- Battery recyclers / refiners。
- Second-life integrators。
- BESS O&M / decommissioning teams。
- Insurance / auction / fleet salvage triage。
- Micromobility and robotics fleets。

中国目标买方：

- NEV 整车厂 / 进口商。
- 动力电池生产企业。
- 换电运营商。
- 维修网络。
- 报废机动车回收拆解企业。
- 白名单综合利用企业。
- 储能系统集成商和运维商。

中国商业语言：

- `动力电池数字身份证`
- `编码与流向监控`
- `全生命周期溯源`
- `回收服务网点`
- `综合利用企业`
- `梯次利用`
- `异常隔离`
- `合规报送时限`

## Business Model

收入模型：

> paid pilot + annual SaaS + edge workstation + per-pack routing fee + marketplace/value take-rate

建议价格：

- 60-90 天云端试点：25k-60k 美元，覆盖 1 个站点或 1 条网络线路、250-1000 条 pack 记录。
- 90 天运营试点：60k-125k 美元，覆盖 1-3 个站点、集成、路由规则、dashboard、1-2 个边缘工位。
- OEM / 保险 / 拍卖网络试点：150k-250k 美元，覆盖多区域、合规报表、SSO/API 和 5000+ records。
- 年度 SaaS：小运营商 36k-75k 美元/年；回收/梯次/车队 90k-250k；OEM/保险/拍卖网络 250k-750k。
- Edge workstation：软件支持 7.5k-18k 美元/站/年；硬件包 6k-18k 美元。
- EV / 工业 pack 路由费：20-75 美元/件；带诊断和合规包 75-250 美元/件。
- BESS module/container：5-25 美元/module，或 250-1000 美元/container/rack。
- Micromobility / robotics：0.10-0.75 美元/active pack/月，另加 1-5 美元/disposition event。
- Marketplace/value fee：BatteryRouter 撮合下游交易时收取 1%-3%。

ROI 公式：

```text
Annual ROI =
  (Annual Gross Benefit - Annual BatteryRouter Cost)
  / Annual BatteryRouter Cost

Annual Gross Benefit =
  logistics savings
+ disposition uplift
+ avoided misrouting/rework
+ avoided storage/quarantine cost
+ labor/reporting savings
+ avoided incident/compliance exposure
+ warranty/claims savings
```

90 天 KPI：

- Days 0-30：导入 80%+ 相关记录，定义 chemistry/damage/SoH/region 路由规则，部署首个边缘工位。
- Days 31-60：90%+ 入仓扫描合规，85%-95% 与操作员复核一致，route recommendation acceptance >60%，chain-of-custody 完整率 >95%。
- Days 61-90：试点线路物流成本下降 8%-15%，隔离/返工下降 15%-25%，处置时间下降 30%-50%。
- 回收商指标：更高 gross margin per ton/pack，更少 rejected loads，更好的 NMC/LFP segregation。
- 梯次利用指标：accepted usable kWh 提升 10%-20%，每个 pack 测试小时下降 25%-50%。
- 保险/拍卖指标：48-72 小时内给出处置，sale uplift 2%-5%，unsafe storage days 下降 25%+。

## Competition

BatteryRouter 不应声称自己是电池护照、SOH 认证、回收厂、保险公司或二次利用集成商。

- Battery analytics / SOH：ACCURE、TWAICE、Elysia、Zitara、Voltaiq。
- Battery health / resale：Autotrader、AVILOO、Recurrent、Geotab、ReJoule。
- Passport / traceability：Circulor、Minespider、Global Battery Alliance。
- Second-life integrators：B2U、Moment Energy、Connected Energy、Element Energy、Smartville。
- Recyclers / materials：Redwood、Cirba、Li-Cycle/Glencore、Ascend Elements、Fortum。
- Automated disassembly：R3 Robotics、Comau、ORNL-style research automation。
- Thermal / safety monitoring：Honeywell Li-ion Tamer、Dukosi、BMS/off-gas/fire systems。

Credible layer:

> BatteryRouter owns routing intelligence and transaction workflow between first-life asset owners and downstream destinations.

## Moat

- Route outcome graph：来源、检测、建议、审批、去向、价格、接收和真实后续结果绑定在同一资产上。
- Partner coverage：合规综合利用企业、回收商、梯次商、承运商、诊断设备和保险/拍卖平台越多越强。
- Compliance workflow：编码、数字身份证、流向报送、报表时限、角色审计和区域数据驻留形成流程壁垒。
- Rare event HIL：接触不良、标签误读、热像偏移、罕见 pack 和人工改判进入 LeRobot 数据闭环。
- Edge profiles：RGB/thermal/telemetry 模型的 AI Hub/QNN profile、哈希、延迟和回滚记录。

## Architecture

比赛 demo 是无电芯、无高压的桌面 HIL 模拟工位。电压、阻抗、热风险和 SOH/SOC 都是 synthetic 或场景表；如果没有校准仪器和合规流程，不声称测量真实电池健康或安全。

### Physical Mock

- 3D 打印/泡棉 dummy pack。
- QR label。
- 装饰端子，不连接真实电池。
- USB/5V current-limited electronics。
- Synthetic voltage / impedance / temperature scenario table。
- RGB camera。
- Thermal camera 或 synthetic heatmap。
- Low-force robot arm / servo gate。
- E-stop。

### ROS 2 Graph

- `rgb_camera_node`
- `thermal_camera_node`
- `qr_decode_node`
- `synthetic_battery_node`
- `fusion_inference_node`
- `hil_review_node`
- `sorter_controller_node`
- `lerobot_recorder_node`

Topics:

- `/camera/rgb/image_raw`
- `/camera/thermal/image_raw`
- `/pack/qr`
- `/pack/sim_electrical`
- `/policy/triage`
- `/operator/correction`
- `/sorter/command`

### Model

- RGB encoder：MobileNet/EfficientNet-style。
- Thermal encoder：tiny CNN 或 shared image encoder。
- Telemetry/QR encoder：MLP。
- Fusion head：route class、confidence、needs-human-review。
- Cloud/GPU：PyTorch training from LeRobotDataset。
- Qualcomm edge：ONNX / AI Hub profile / QNN or ONNX Runtime QNN deployment。

### Dataset

LeRobotDataset v3 字段：

- `observation.images.rgb`
- `observation.images.thermal`
- `observation.state`: QR scenario ID, synthetic voltage, synthetic impedance, synthetic temp, station pose, previous decision。
- `action`: `reuse_bin`, `recycle_bin`, `quarantine_bin`, `manual_review`。
- `timestamp`
- HIL correction flag。
- route outcome label。
- evidence packet hash。

## Competition Demo

3 分钟演示：

1. Safety framing：展示 dummy pack、无电芯、无高压、synthetic telemetry。
2. Intake：扫描 QR、RGB、热像/热图，读取 synthetic voltage/impedance 和场景 passport。
3. Edge inference：Qualcomm edge 上运行 compact fusion model，输出 route、confidence 和 reason code。
4. Physical routing：低力机械臂或 servo gate 把 dummy pack 送到 reuse/recycle/quarantine/manual review bin。
5. HIL correction：故意插入接触偏差或热像偏移，人工覆盖 reuse 为 quarantine。
6. Dataset loop：展示 LeRobotDataset episode，包含图像、热像、telemetry、action 和 operator correction。
7. Evidence export：输出身份、图像、读数、模型版本、人工审批、去向和下游接收字段。

## Why Qualcomm

- 电池入仓路由需要本地视觉、热像、多传感融合、弱网运行和数据不出域。
- AI Hub / QNN 适合 compact RGB/thermal/telemetry fusion model，不需要把 VLA/ACT 作为核心 claim。
- RB3 Gen 2 / QCS6490 级边缘节点可以作为相机、传感器、ROS 2、HIL 和证据包的现场枢纽。
- 中国部署走本地私有云和数据不出厂，海外部署可用云 GPU 训练，同一 job contract 共享。
- Qualcomm 可以把 BatteryRouter 变成 physical AI 在高合规工业场景的参考应用。

## Claims To Avoid

- 不说认证二次利用电池。
- 不说测量真实 SOC/SOH/RUL。
- 不说预测或防止热失控。
- 不说真实锂电池安全处理。
- 不说已满足 EU Battery Passport。
- 不说可自动化真实电池拆解。
- 不说整个机器人栈跑在 QNN。
- 不说与 Stena/BatteryLoop 或任何同名实体有关联。
- 不说 BatteryRouter 是保险公司、回收厂或 SOH 证书机构。

## Sources

- IEA EV batteries 2026: https://www.iea.org/reports/global-ev-outlook-2026/electric-vehicle-batteries
- IEA battery storage 2026: https://www.iea.org/reports/global-energy-review-2026/technology-battery-storage
- EU Batteries Regulation: https://environment.ec.europa.eu/topics/waste-and-recycling/batteries_en
- Battery Pass guidance: https://thebatterypass.eu/wp-content/uploads/q-a_content-guidance.pdf
- China NEV 2025: https://www.news.cn/fortune/20260114/cbbd861081c349d8ae238167ca418fa3/c.html
- MIIT retired battery volume: https://gxt.fujian.gov.cn/jdhy/zcjd/qtzcwjjd/202601/t20260119_7082068.htm
- Order No.73 text: https://xinwen.bjd.com.cn/content/s6969a669e4b0cd719e9c3522.html
- NDRC policy reading: https://www.ndrc.gov.cn/fggz/hjyzy/zyzhlyhxhjj/202603/t20260317_1404213.html
- GB 38031-2025: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=3AB693FAFF5D9716DF61D6FD2187A
- China auto data rules: https://www.cac.gov.cn/2021-08/20/c_1631049984897667.htm
- ACCURE battery analytics: https://www.accure.net/news/accure-battery-intelligence-predictive-analytics-tech-to-increase-battery-safety-and-performance-of-energy-storage-projects
- TWAICE Doosan: https://www.twaice.com/newsroom/doosan-twaice
- Autotrader battery health: https://press.autotrader.com/2025-01-20-EV-Battery-Health-Scores-Now-Available-on-Autotrader-Listings
- Circulor battery passport: https://circulor.com/articles/worlds-first-battery-passport
- Waymo B2U second life: https://waymo.com/blog/2026/06/b2u-partnership
- Moment Energy Series B: https://www.momentenergy.com/news/series-b
- R3 Robotics funding: https://www.eiturbanmobility.eu/r3-robotics-secures-e20m-to-scale-automated-disassembly-for-electric-vehicle-systems/
- Honeywell Li-ion Tamer: https://www.honeywell.com/content/honcorp/us/en/news/press-releases/2025/07/honeywell-makes-strategic-tuck-in-acquisition-of-li-ion-tamer
- PHMSA lithium batteries: https://phmsa.dot.gov/lithiumbatteries
- EPA used lithium-ion batteries: https://www.epa.gov/recycle/used-lithium-ion-batteries
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- ROS 2 interfaces/actions: https://docs.ros.org/en/jazzy/Concepts/Basic/Interfaces-Topics-Services-Actions.html
- Qualcomm AI Hub: https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN EP: https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
