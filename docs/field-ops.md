# FieldOps Pitch

更新时间：2026-07-06。该版本按 YC / Airbnb 风格 pitch spine 重写：从光伏/新能源场站 O&M 的可量化痛点切入，再讲现有方案缺口、产品、商业模式、竞争壁垒、Qualcomm 价值、比赛演示和合规边界。

## One-Liner

FieldOps 野巡是远程资产的任务、证据和训练闭环：

> 从光伏/新能源 O&M 切入，把无人机、UGV、四足、传感器舱、弱网策略、工单系统和 LeRobot 数据飞轮连成一个 Qualcomm edge workflow，让客户买“可验收的异常关闭”，不是买一台野外机器人。

## 1. Problem

新能源场站不是缺照片，而是缺“异常是否被关闭”的证据。

光伏、BESS、变电站和风场越来越分散，站点少人值守，网络不稳定，现场环境复杂。无人机和机器人能采集图像，但运营团队真正需要的是收入损失被发现、工单被派发、维修/清洗被验证、模型持续变准。

核心痛点：

- 热斑、遮挡、积灰、支架异常、逆变器状态会影响发电和质保。
- 偏远站点人工复查成本高，重复 truck roll 会吞掉巡检 ROI。
- 弱网和离线是常态，不能把安全、证据和任务完成度押在云端。
- 坡度、泥水、粉尘、强光、夜间、人车混行和危险区必须进入 ODD。
- 原始视频不是资产；闭环异常才是资产：位置、资产、传感器、人工判断、机器人动作、维修结果和最终验证。

一句话：

> 客户不是买一台野外机器人，而是买少人值守场站里每一个收入漏洞的发现、派工、复核和证据。

## 2. Current Alternatives Fail

采集层已经很强，但“发现到关闭”仍然断在中间。

- Drone capture：DJI、Skydio、Percepto、DroneDeploy 等覆盖快，但更擅长发现，不擅长地面复核、清洗/维修证明和弱网自主闭环。
- Robot hardware：Spot、ANYmal、Unitree、轮式/履带 UGV 都能进入现场，但客户买的是可验收任务，不是机身参数。
- Solar/wind analytics：Raptor Maps、Zeitview 等能生成缺陷图和资产视图，但现场仍要派人、派机器人、验证修复和沉淀数据。
- CMMS / EAM：工单系统记录流程，但不理解机器人 ODD、传感器证据、弱网同步和模型发布门禁。
- Generic RobOps：Formant、InOrbit、Viam、Foxglove 横向能力强，但缺少新能源资产、GIS、ODD、弱网、传感器舱、CMMS/EAM/SCADA 语义。

Deck line：

> Capture is solved; closure is not.

## 3. Solution

FieldOps 是 site-controlled ODD 内的 supervised outdoor mission/evidence OS。

第一阶段只承诺：

- 光伏区块、BESS、升压站、围栏、服务道路和能源园区。
- 站点授权私有区域，不进入公共道路或无授权 BVLOS 场景。
- 人在环监督、远程接管和 ODD 限制，而不是 fully autonomous everywhere。

核心流程：

1. Plan：导入 GeoJSON、资产清单、禁行区、ODD、传感器计划和验收模板。
2. Inspect：无人机、UGV、四足和人工 crew 共享 MissionSpec 与 Evidence API。
3. Close：把热斑、积灰、遮挡、设备异常和低置信度片段转成工单和复核任务。
4. Prove：交付位置、时间、RGB/thermal、MCAP、模型版本、人工 verdict 和签名。
5. Learn：接管、近失误和复核结果进入 LeRobot episode，再经 AI Hub/QNN 门禁回到边缘。

## 4. Why Now

光伏规模、机器人硬件和数据合规压力第一次把“闭环证据”推到预算中心。

关键信号：

- IEA PVPS Snapshot 2026 显示全球 PV 累计规模接近 3TW，2025 年新增约 698GW。
- 中国国家能源局数据：2026-05 光伏装机已超过 1.26TW。
- IEA PVPS soiling work 指出积灰损失具有实质影响，需要监测和清洗优化。
- 美国公用事业植被管理是数十亿美元级预算，说明 remote asset risk 有真实资金池。
- 无人机、四足、UGV、dock、edge AI 和云训练已经成熟，但客户仍缺闭环 evidence contract。
- FAA/CAAC/BVLOS、关键基础设施限制、EU Data Act、China data residency、Cyber Resilience Act 等要求让“只上传原始数据”的方案越来越难卖。

## 5. Product

先卖可验收巡检结果，再扩展机器人队列。

### Product Modules

- FieldBrain：Qualcomm edge kit，本地运行视觉、热斑初筛、任务缓存、弱网同步和 QNN policy。
- SensorPod：RGB、thermal、LiDAR、acoustic、gas、multispectral 的 manifest、校准、时间同步和健康检查。
- MissionMap：GeoJSON route、资产 ID、禁行区、ODD、安全边界、证据模板和工单字段。
- ResilientLink：local safety、heartbeat、alert summary、thumbnail、track、MCAP 的优先级同步。
- TeleopFallback：只有在 ODD、延迟、丢包、电量、速度、人车边界和 supervisor 条件满足时开放。
- EvidenceFlywheel：每个异常生成 evidence package；每次接管、近失误、低置信度片段成为 LeRobot 候选数据。
- TrainRouter：一个 LeRobot job contract，映射到中国云/私有云和海外 GPU provider 两条算力通道。
- SimEval：用 MCAP + digital twin 做发布前回放评测，检查 route completion、recall、false positive、p95 latency、energy、lost-link 和 rollback。

### Reference Architecture

```text
FieldOps edge stack
  ├─ fieldbrain-runtime
  ├─ mission-map
  ├─ sensorpod-registry
  ├─ resilient-link
  ├─ robot-drone-adapter-runtime
  ├─ safety-envelope
  ├─ evidence-package-api
  ├─ teleop-fallback
  ├─ mcap-recorder
  ├─ train-router
  ├─ sim-eval
  ├─ edge-policy-registry
  └─ cmms-eam-scada-sync
```

### Core Schemas

```json
{
  "MissionSpec": {
    "mission_id": "solar_block_a_hotspot_scan",
    "site_id": "acme-solar-80mw",
    "route_geojson": "s3://missions/route.geojson",
    "asset_ids": ["pv-row-17", "inverter-02", "bess-container-03"],
    "sensor_plan": ["rgb", "thermal", "gnss", "imu"],
    "od_profile": "solar_service_road_daylight_dry",
    "link_policy": "fieldops_weaknet_v1",
    "offline_policy": "cache_alerts_stop_at_boundary",
    "safety_envelope_id": "se_solar_daylight_v1",
    "evidence_template_id": "pv_hotspot_v2"
  }
}
```

```json
{
  "EvidencePackage": {
    "evidence_id": "ev_hotspot_001",
    "mission_id": "solar_block_a_hotspot_scan",
    "asset_id": "pv-row-17-module-044",
    "geometry": {"type": "Point", "coordinates": [113.93, 22.54]},
    "assets": {
      "rgb": "object://rgb/ev_hotspot_001.jpg",
      "thermal": "object://thermal/ev_hotspot_001.tiff",
      "mcap": "object://mcap/ev_hotspot_001.mcap"
    },
    "model_id": "pv-hotspot-qnn-v3",
    "qnn_profile_id": "profile_9075_20260706",
    "confidence": 0.82,
    "operator_verdict": "work_order_required",
    "cmms_ticket": "WO-9381",
    "signature": "ed25519:..."
  }
}
```

```json
{
  "EdgePolicyManifest": {
    "policy_id": "pv-hotspot-qnn-v3",
    "dataset_hash": "sha256:...",
    "eval_report": "object://eval/pv-hotspot-qnn-v3.json",
    "onnx_uri": "object://models/pv-hotspot-v3.onnx",
    "qnn_dlc_uri": "object://models/pv-hotspot-v3.dlc",
    "qnn_context_binary_uri": "object://models/pv-hotspot-v3.ctx",
    "target_device": "rb3|rb6|iq10|iq-9075",
    "latency_p95_ms": 38,
    "rollback_policy_id": "pv-hotspot-qnn-v2"
  }
}
```

## 6. Market And Business Model

按 MW、站点、工单和证据收费，而不是按机器人炫技收费。

第一批客户：

- Head of Solar O&M / 新能源场站运维负责人。
- IPP asset manager / regional operations lead。
- O&M contractor GM。
- Utility innovation team / 集控中心负责人。
- Energy SI / drone service provider / cleaning robot vendor。
- Gatekeepers：HSE、OT/IT security、SCADA/CMMS owner、procurement、data office。

ROI formula:

```text
recovered MWh
+ avoided truck rolls
+ optimized cleaning
+ faster repair
+ warranty / insurance recovery
- FieldOps cost
```

Pilot success metric:

- 90 天证明 `2x annualized value / first-year ARR`。
- `30%-50% inspection triage time reduction`。
- 至少一个从发现到验证关闭的缺陷闭环。

### China Version

中国版 headline：

> 先卖可验收巡检结果，再扩展机器人队列。

商业模式：

- 30-90 天光伏/新能源 pilot：人民币 100k-500k，覆盖 1-3 个站点或一个 plant block。
- 年度：人民币 200k-1M / site-year，或人民币 3k-12k / MW-year。
- 大型央国企/园区项目：人民币 1M-5M+。
- 本地 robot/drone partner 作为 pass-through 或联合交付。

采购包：

- 本地部署。
- 中文报告模板。
- 数据边界和跨境 off-by-default 说明。
- 操作员培训。
- PMS/SCADA/GIS/EAM integration plan。
- 验收指标：coverage rate、defect recall、report latency、manual recheck rate。

优先渠道：

- 光伏/风电/储能 O&M 承包商。
- 国家电网 / 南方电网省公司和合格供应商体系。
- 能源央国企、地方能源集团、工业园区。
- DJI / XAG / GDU / Deep Robotics / Shenhao / Yijiahe / Youibot 等本地生态伙伴。

### Overseas Version

海外版 headline：

> Autonomous field intelligence for remote assets.

商业模式：

- 50-150MW pilot：$50k-$125k。
- Annual evidence layer：$250-$900 / MW-year，site minimum $10k-$25k。
- Mission fees benchmark：solar thermal mission $150-$500 / MW，utility line inspection $300-$2,000 / mile。
- 扩展口径：MW、turbine、line-mile、acre、mine-shift。

优先客户：

- Solar IPP、asset manager、O&M provider。
- Utility vegetation / wildfire / storm readiness teams。
- Wind farm operator 和 blade/tower inspection provider。
- Specialty crop / orchard / greenhouse service provider。
- Mining HSE / operations teams as later high-ACV expansion。

## 7. Competition And Moat

竞争不是没有机器人，而是闭环缺少统一 workflow。

竞争地图：

- Quadrupeds / UGV：ANYbotics、Boston Dynamics、Unitree、Deep Robotics。
- Drone ops：DJI Dock、Skydio Dock、Percepto、FlytBase、DroneDeploy。
- Solar/wind analytics：Raptor Maps、Zeitview、Aerones。
- Agriculture robots：AgXeed、Burro、Carbon Robotics、Verdant、DJI Agriculture、farm-ng。
- Horizontal robot ops：Formant、InOrbit、Viam、Foxglove。
- Critical infrastructure data：Gecko Robotics。
- Mining autonomy：Komatsu、Sandvik、Emesent and OEM-specific systems。

FieldOps 的壁垒：

- Closed exceptions：热斑、遮挡、清洗、维修、复核和质保证据带有最终 outcome，比原始视频更有价值。
- ODD library：不同站点的坡度、天气、可见度、人车边界、弱网和 lost-link 行为形成可复用 deployment profile。
- Adapter compound：机器人、无人机、CMMS、SCADA、GIS、EAM、传感器舱和云训练 provider 越接越快。
- Evidence contract：位置、资产、传感器、人工 verdict、ticket、signature、model version 和 replay data 对接采购/保险/质保。
- Qualcomm edge proof：QNN profile、latency、memory、thermal、power、rollback 和 replay eval 变成边缘上线门禁。

## 8. Why Qualcomm

户外机器人需要边缘 AI、连接、功耗和部署证据一起成立。

Qualcomm value:

- Local perception：热斑、遮挡、表计、障碍、人员和低置信度事件在本体侧初筛。
- Connectivity：专网、公网、Wi-Fi、NTN/卫星补充和 store-and-forward 支撑偏远资产。
- Low power / thermal：长时间现场运行必须看 latency、memory、power 和 thermal，而不是只讲 TOPS。
- AI Hub / QNN：ONNX 到 QNN DLC/context/profile，记录 p95 latency、memory、target runtime 和 rollback。
- Roadmap：RB3/QCS6490 用于 demo，RB6 用于 5G-heavy field SKU，IQ10 RRD 进入生产级路线。
- Ecosystem：无人机、四足、UGV、传感器、能源 SI、O&M service partner 和 GPU provider 围绕 Qualcomm edge 连接。

需要 Qualcomm 支持：

- RB3 Gen 2 / RB6 / Dragonwing IQ10 / IQ-9075 hardware 或 profile。
- AI Hub / QNN 指导，把 thermal/RGB defect detector、redaction、obstacle classifier 和 teleop recovery model 做成 evidence gate。
- 传感器 partner、机器人 partner 和新能源/工业客户 introduction。
- 允许作为 Qualcomm edge field robotics reference workflow 继续打磨。

## 9. Competition Demo

8 分钟演示：一个光伏区块，弱网中发现热斑，人工接管复核并生成训练样本。

Demo setup:

- 浏览器 MissionMap。
- 小车或仿真 rover。
- Mini solar field：3 条路线、2 个 no-go zone、若干 panel asset IDs。
- RGB / thermal mock images。
- Network state toggle：online、weak、offline、recovered。
- Teleop assist button。
- LeRobot export + AI Hub/QNN release gate screen。

Demo flow:

1. Buyer pain：remote solar/substation inspections create truck rolls, missing evidence, unsafe manual checks。
2. Field kit：FieldBrain + SensorPod mock，展示 RB3/RB6/IQ10 roadmap、thermal/RGB pod、battery、GNSS/RTK、E-stop。
3. MissionMap：加载 route、asset IDs、ODD card、SafetyEnvelope 和 evidence template。
4. Weak link：机器人执行任务，切换 network state，UI 只保留 heartbeat、cached thumbnails、alert summary，本地安全仍生效。
5. Evidence：检测 mock hotspot 或遮挡，生成 map point、thermal image、confidence、MCAP clip、CMMS ticket。
6. Teleop recovery：低置信度障碍触发 teleop fallback，人工低速接管，事件标注 `autonomy_mode=teleop_assist`。
7. LeRobot：转换 intervention clip 为 LeRobot episode，提交 TrainRouter，显示 China/global provider selector、budget cap、logs。
8. AI Hub/QNN：ONNX -> QNN DLC/context/profile，展示 p95 latency、target hardware、rollback package、simulation regression pass。

## Compliance And Safety Posture

Safe deck position:

> FieldOps is not making robots legal everywhere. It helps customers define the operating domain, approval path, safety case, audit trail, cyber posture, and data residency for each field deployment.

Rules:

- Ground robots on private sites：site-controlled machinery, not free-roaming autonomy。
- Public roads/sidewalks：do not claim blanket legality。
- Drones：US Part 107 / waivers; BVLOS is not broadly legal by default。
- China drones：real-name registration, classification, operator rules and operation identification matter。
- Energy/utility：critical infrastructure UAS restrictions, owner authorization, Remote ID/no-fly screening。
- Electric grid cyber：if touching utility networks, expect NERC CIP/vendor risk scrutiny。
- Agriculture：scouting is easier than spraying; pesticide application requires FAA/EPA/state rules and label compliance。
- Mining：start above-ground or certified non-explosive zones; underground coal/mining needs certified hardware and site safety approvals。
- Rail/road：automated inspection may supplement, not automatically replace mandated inspections。
- Data：video, LiDAR, geolocation, license plates, faces, worker behavior, and critical-site imagery may be sensitive data.
- China data：support local deployment and data-residency controls; do not default to overseas GPU training.

## Claims To Avoid

- 不说 legal everywhere、approved by regulators、certified compliant，除非绑定具体证书、地区和用例。
- 不说 fully autonomous with no human oversight。
- 不说 all-weather、all-terrain、fully autonomous anywhere。
- 不说 BVLOS-ready without approval/waiver path。
- 不说 replaces mandated inspections。
- 不说 no personal data collected，如果相机、LiDAR、GPS、车牌、人脸或 worker activity 会被采集。
- 不说 data can be freely transferred globally。
- 不说 unhackable、military-grade、air-gapped、zero risk。
- 不把 satellite link 描述成稳定高清视频遥操作链路。
- 不把 TOPS 当真实吞吐；要用目标模型 FPS、latency、power、thermal 和 replay eval 说话。

## Sources

- IEA PVPS Snapshot 2026：https://iea-pvps.org/snapshot-reports/snapshot-2026/
- China NEA solar statistics：https://www.nea.gov.cn/20260625/24f752fd199c4632b7dc7762462585de/c.html
- IEA PVPS soiling losses：https://iea-pvps.org/fact-sheets/fs-soiling-losses/
- EIA outage duration：https://www.eia.gov/todayinenergy/detail.php?id=66744
- Public Power vegetation management：https://www.publicpower.org/periodical/article/cost-not-cutting-trees
- USDA farm labor：https://www.ers.usda.gov/topics/farm-economy/farm-labor
- DJI solar inspection：https://enterprise.dji.com/inspection/photovoltaic-power-plant
- DJI Dock 3：https://enterprise.dji.com/dock-3
- Skydio Dock：https://www.skydio.com/dock
- Percepto AIM：https://percepto.co/aim/
- DroneDeploy robotics：https://dronedeploy.com/product/robotics
- Raptor Maps：https://raptormaps.com/
- Zeitview：https://www.zeitview.com/
- Gecko Robotics Cantilever：https://www.geckorobotics.com/cantilever
- ANYmal X：https://www.anybotics.com/robotics/anymal-x/
- Boston Dynamics Orbit：https://bostondynamics.com/products/orbit/
- Unitree B2：https://www.unitree.com/cn/b2/
- AgXeed：https://www.agxeed.com/
- Burro：https://burro.ai/
- Carbon Robotics：https://carbonrobotics.com/
- Formant：https://formant.io/
- InOrbit：https://www.inorbit.ai/overview
- Viam fleet management：https://www.viam.com/platform/fleet-management
- Foxglove：https://foxglove.dev/
- FAA commercial UAS：https://www.faa.gov/uas/commercial_operators
- FAA Part 107 waivers：https://www.faa.gov/uas/commercial_operators/part_107_waivers
- FAA critical infrastructure UAS：https://www.faa.gov/uas/critical_infrastructure
- ISO 3691-4：https://www.iso.org/standard/83545.html
- ANSI/RIA safety resources：https://www.automate.org/robotics/safety/robot-safety-resources
- EU Machinery Regulation：https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery
- EU Data Act：https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained
- CISA UAS cybersecurity：https://www.cisa.gov/topics/physical-security/be-air-aware/uas-cybersecurity
- NERC CIP：https://www.nerc.com/standards/reliability-standards/cip
- FTC location data enforcement：https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-takes-action-against-gravy-analytics-venntel-unlawfully-selling-location-data
- CAAC drone rules：https://www.caac.gov.cn/English/News/202403/t20240305_223119.html
- CAC cross-border data provisions：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- Alibaba PAI Lingjun：https://www.aliyun.com/product/bigdata/learn/pailingjun
- Tencent TI：https://cloud.tencent.com/product/ti
- Huawei ModelArts：https://www.huaweicloud.com/product/modelarts.html
- RunPod pricing：https://www.runpod.io/pricing
- Lambda pricing：https://lambda.ai/pricing
- CoreWeave GPU compute：https://www.coreweave.com/products/gpu-compute
- ROS 2 QoS：https://design.ros2.org/articles/qos.html
- MCAP ROS 2 guide：https://mcap.dev/guides/getting-started/ros-2
- GeoJSON RFC 7946：https://www.rfc-editor.org/rfc/rfc7946
- WebRTC：https://webrtc.org/
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot HIL data collection：https://huggingface.co/docs/lerobot/hil_data_collection
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Qualcomm Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
