# FieldOps Pitch

更新时间：2026-07-05。

## Core Thesis

FieldOps 野巡是面向户外巡检、农田、能源场站和基础设施的边缘机器人平台：

> 把 Qualcomm 端侧 AI、耐候机器人套件、任务级传感器舱、弱网/离线连接策略和 LeRobot 数据飞轮整合成一套可商用的现场作业底座，让客户先购买可验收任务，再逐步扩展机器人队。

它不是“万能户外机器人”，而是一套可复制的现场作业产品线：

- 在明确 ODD 内执行高频、危险、重复的巡检。
- 用本地感知和任务缓存保证断网不失控。
- 用远程接管解决复杂地形、异常设备和低置信度判断。
- 用证据包交付结果，而不是只交付视频流。
- 把人工接管、失败恢复、低置信度片段转成 LeRobot-compatible 训练数据。

## Why This Matters

户外机器人商业化的真实需求不是“机器人很酷”，而是：

- 远程资产太多：光伏、风电、管线、变电站、农田、矿区和园区分散。
- 人工巡检成本高、风险高、频次不足，且记录质量不稳定。
- 弱网、泥水、粉尘、强光、坡度、碎石、雨雾和季节变化让通用机器人方案容易失效。
- 客户采购需要报告、工单、GIS/CMMS/SCADA/EAM 对接和可追溯证据。
- 农业、能源和基础设施买家越来越接受按任务、按站点、按面积或按资产收费的 RaaS / inspection-as-a-service。

市场上已有 ANYbotics、Gecko Robotics、Percepto、DJI Agriculture、Carbon Robotics、Built Robotics、Farm-ng 等强玩家。FieldOps 的差异不是声称没有竞品，而是把“现场边缘智能 + 证据工作流 + 数据训练飞轮 + 双云部署”打包成 Qualcomm-first 的可交付平台。

## Product Modules

### 1. FieldBrain

Qualcomm edge AI 现场大脑。

- 本地视觉检测、异常初筛、SLAM/定位、任务缓存和安全降级。
- 断网时继续执行限定任务，恢复网络后同步证据和日志。
- RB3 Gen 2 / QCS6490 适合 demo 和开发者套件，RB6 适合 5G-heavy 巡检机器人，IQ9 / IQ10 适合高端多传感器生产路线。
- IQ10 可以作为 2026 年 9 月后高端路线图叙事；不把它写成当前量产主硬件。

### 2. RuggedBase

机器人本体适配层。

- 轮式、履带、四足、无人机和专用爬行/巡检本体共享任务接口、时间戳、数据格式和远程接管策略。
- FieldOps 不声称开发板天然耐候，而是把外壳、电源、热设计、连接器、线束、维护 SOP 和测试证据产品化。
- 对外以任务 ODD 表述能力：地形、坡度、雨水、粉尘、温度、光照、可见度、网络和人机混行边界。

### 3. SensorPod

任务级传感器舱。

- RGB、热成像、多光谱、LiDAR、声学、气体、土壤/作物传感器。
- 统一时间同步、标定、传感器健康检查和证据元数据。
- 以场景卖 payload：光伏热斑、电力表计/温升、农田长势/杂草、管线/园区巡检。

### 4. MissionMap

现场任务规划器。

- 导入 GIS、卫星图、资产清单、巡检点、禁行区、返航点和人工接管规则。
- 把“巡一圈”拆成可验收任务：路线、传感器、证据格式、报告字段、异常等级和工单写回。
- 光伏按 MW / 区块，农业按亩/公顷，电力按站点/设备，管线按公里，矿区按班次或区域计费。

### 5. ResilientLink

户外弱网连接策略。

- 专网 5G/LTE、公网 4G/5G、Wi-Fi、卫星兜底和离线缓存。
- 弱网优先级：安全心跳、控制指令、告警摘要、缩略图、轨迹、证据片段，最后才是原始日志。
- WebRTC 用于低延迟远程接管，但控制权受本体安全层约束；高延迟或丢包超阈值时降级为低速或半自主接管。
- 卫星只作为低频摘要、位置、告警和应急指令补充，不承诺稳定高清视频遥操作。

### 6. EvidenceFlywheel

证据与训练飞轮。

- 本地滚动记录 MCAP / ROS bag 片段，按任务、事件、传感器和权限选择性上传。
- 人工接管、低置信度、近失误、路线失败和特殊地形生成高价值训练样本。
- MCAP / episode 转为 LeRobot Dataset v3：多相机视频、状态/动作、标定、任务文本、固件/模型版本和环境标签。
- 云端训练后通过 Qualcomm AI Hub / QNN / ONNX / TFLite 等路径做优化、profile、签名、灰度发布和回滚。

## China Version

中国版主张：

> FieldOps 野巡：面向智慧农业、新能源场站、矿山安全和电力巡检的边缘智能无人巡检平台。

采购语言要强调：

- 示范场景：智慧农业、AI+农业、新能源运维、矿山安全和园区巡检。
- 可复制推广：县域农场、国企场站、能源基地、工业园区和系统集成伙伴。
- 国产化交付：本地数据边界、本地运维、本地云 GPU 训练路径。
- 结果交付：报表、工单、巡检证据、异常复核和安全管理。

优先客户：

- 农业农村部门、地方智慧农业示范园、国有农场和大型农企。
- 光伏/风电场站业主、能源央国企、O&M 承包商。
- 电网、工业园区、矿山集团和安全生产团队。
- 本体厂商、传感器厂商和地方系统集成商。

收入模型：

- 试点包：机器人 + 传感器舱 + 任务地图 + 报告模板 + 数据回流。
- 项目制：多机器人队列、平台私有化、系统集成和年度运维。
- 示范场景申报包：面向地方项目的材料、验收指标、看板和现场视频证据。

## Overseas Version

海外版主张：

> Autonomous field intelligence for remote assets.

采购语言要强调：

- Fewer truck rolls, safer inspections, faster issue detection, lower downtime, auditable records.
- Utilities, solar/wind operators, farms, mines and infrastructure teams buy verified condition data, not generic robot novelty.
- RaaS / inspection-as-a-service can lower upfront adoption barrier.

优先客户：

- Utility vegetation / wildfire / storm-readiness teams.
- Solar IPP、asset manager、O&M provider。
- Wind farm operator 和 blade/tower inspection provider。
- 大型农场、果园、葡萄园、合作社和精准农业服务商。
- Mining HSE / operations teams。
- 保险、基础设施风险和资产管理团队作为二级数据买家。

收入模型：

- 按 acre / MW / turbine / line-mile / km / mine-shift 收费。
- 硬件租赁 + 软件订阅 + inspection report credits。
- 传感器舱升级、analytics API、企业支持和数据保留服务。

## Competition Demo

最稳妥 demo 可以做成“户外现场数字孪生 + 小车/桌面验证”的组合：

1. 在网页中展示光伏/农田/变电站任务地图、传感器舱和弱网状态。
2. 小车或模拟机器人执行一段巡检路线，识别热斑/杂草/表计/障碍中的一个 mock 异常。
3. 人工远程接管一次绕障，生成 intervention episode。
4. 系统输出 evidence package：位置、时间、图片/热图、传感器、置信度、工单状态。
5. 异常片段进入 LeRobot/DataFlywheel，展示训练任务和 Qualcomm edge deployment gate。
6. 切换网络状态：在线、弱网、离线缓存、恢复同步，展示“弱网不断巡，无网不失控”。

## Why Qualcomm Should Care

FieldOps 让 Qualcomm 的价值从“机器人开发板”扩展成“户外商用机器人底座”：

- 多摄像头、多传感器和边缘 AI 是户外巡检的硬需求。
- 低功耗、本地推理和热设计决定机器人能否长时间跑在现场。
- 5G / Wi-Fi / NTN / 私有网络叙事让 Qualcomm 在弱网和远程资产场景中有清晰位置。
- AI Hub 与边缘优化路径可以把云训练模型转成可验证的本体部署包。
- IQ10 RRD 的 production robot 架构故事与 FieldOps 的长期路线高度一致：compute、sensing、networking、ROS 2、MLOps、DevOps 和 fleet lifecycle。

## Safety And Compliance Posture

FieldOps 的表述应采用“证据包”和“目标测试”，避免无依据的认证承诺：

- IP65/IP67 只能用于明确测试过的外壳、舱体或连接器，不把整机随意称为 waterproof。
- MIL-STD-810H 是定制化环境测试方法，不等于“军工级认证”。
- 农业自主机械应参考 ISO 18497、ISO 25119、ISO 12100、ISO 13849-1、ISO 13850 等安全设计和验证框架。
- GNSS/RTK 只能在有改正数、良好天空视野和完整性检查时给出高精度定位，不承诺“厘米级 everywhere”。
- ODD 必须明确天气、地形、速度、人机混行、网络、夜间、坡度、障碍和遥操作边界。
- 安全关键控制不依赖公网、云 GPU 或 Cloudflare；本体保留急停、限速、失联策略、返航/驻停和安全制动。

## Claims To Avoid

- 不声称 fully autonomous anywhere / all-weather / all-terrain。
- 不声称无人值守、零事故、零停机或替代所有人工巡检。
- 不声称获得 ATEX/IECEx、UL、CE、BVLOS 或行业安全认证，除非具体硬件已完成认证。
- 不声称卫星链路可稳定承担高清视频遥操作。
- 不声称农业 ROI 对所有作物、所有地区成立。
- 不声称 TOPS 等于真实吞吐；需要用目标模型的 FPS、延迟、功耗和热行为说话。

## Sources

- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Qualcomm IQ10 Series：https://www.qualcomm.com/internet-of-things/products/iq10-series
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm IQ-9075：https://www.qualcomm.com/internet-of-things/products/iq9-series/iq-9075
- Qualcomm QCS6490：https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot HIL data collection：https://huggingface.co/docs/lerobot/hil_data_collection
- ROS 2 QoS：https://design.ros2.org/articles/qos.html
- MCAP ROS 2 guide：https://mcap.dev/guides/getting-started/ros-2
- WebRTC：https://www.w3.org/TR/webrtc/
- 3GPP Non-Public Networks：https://www.3gpp.org/technologies/npn
- 3GPP NTN overview：https://www.3gpp.org/technologies/ntn-overview
- IEC IP ratings：https://www.iec.ch/ip-ratings
- ISO 18497-1 autonomous agricultural machinery：https://www.iso.org/standard/82684.html
- ISO 18497-4 verification and validation：https://www.iso.org/standard/82688.html
- ISO 12100 risk assessment：https://www.iso.org/standard/51528.html
- ISO 13849-1 safety-related control systems：https://www.iso.org/standard/73481.html
- MIL-STD-810H DLA entry：https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35978
- FCC equipment authorization：https://www.fcc.gov/general/equipment-authorization-procedures
- EU Radio Equipment Directive：https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red_en
- PHMSA UN 38.3 summaries：https://www.phmsa.dot.gov/training/hazmat/new-un-requirement-test-summaries
- EU ATEX equipment directive：https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/equipment-potentially-explosive-atmospheres-atex_en
- National Grid Spot case study：https://bostondynamics.com/case-studies/spot-becomes-part-of-the-team-at-national-grid/
- ANYmal X：https://www.anybotics.com/robotics/anymal-x/
- Gecko Robotics Cantilever：https://www.geckorobotics.com/cantilever
- Percepto：https://percepto.co/
- DJI photovoltaic inspection：https://enterprise.dji.com/inspection/photovoltaic-power-plant
- DJI Agriculture：https://ag.dji.com/
- DJI Agriculture annual report 2025：https://www.dji.com/media-center/announcements/dji-agricultural-annual-report-2025
- Carbon Robotics：https://carbonrobotics.com/
- John Deere See & Spray：https://www.deere.ca/en/news/all-news/see-spray-herbicide-savings/
- FAA Part 107 waivers：https://www.faa.gov/uas/commercial_operators/part_107_waivers
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- FERC vegetation management：https://www.ferc.gov/transmission-line-vegetation-management
- GAO precision agriculture technologies：https://www.gao.gov/products/gao-24-105962
- NIOSH mine automation：https://www.cdc.gov/niosh/mining/partnerships/automation.html
