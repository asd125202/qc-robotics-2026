# AgriLoop 农务闭环 Pitch

更新时间：2026-07-06。

## One-Line

AgriLoop 是高价值作物的闭环 AI 作业层：

> Farmers do not need another dashboard. They need an autonomous loop that sees, acts, and proves ROI every pass.

中文表达：

> 农场缺的不是大屏，是能看见、行动并证明 ROI 的闭环。

AgriLoop 面向设施蔬菜、果园和农业社会化服务组织，用 Qualcomm edge AI + LeRobot HIL 把巡田、诊断、处方、无人机/地面机器人/人工执行、验收、追溯和下一轮模型训练连成一条可验证作业链。

## Problem

农场经理通常知道“应该做什么”，但很难证明“谁做了、做没做成、值不值钱”。

- 无人机、传感器、农机和手机都能产生数据，但发现问题和处理问题之间断裂。
- 农事派活靠微信群、纸单和口头交代，漏活、返工和扯皮常见。
- 季节工难招，设施蔬菜、果园、茶园、采摘、喷药、搬运和复查越来越难排班。
- 无人机、农机、机器人、传感器和农场软件没有统一任务语言。
- 农资用量、作业轨迹、工人/设备责任、采收批次和采购商审计难以自动核验。
- 农场买了机器人和软件后，仍然很难证明节省了多少工、少用了多少药、哪一批次质量变好。

## Why Now

农业机器人从“能不能动”，进入“能不能闭环赚钱”。

全球版时机：

- 全球农业机器人市场已进入高速扩张期，多家机构估算 2025 年约 150 亿美元以上，到 2030/2031 年约 400 亿美元以上。
- IFR 统计 2024 年农业服务机器人销量约 19,500 台，真实部署仍处早期；RaaS 机器人 fleet 增长说明按服务付费正在降低采用门槛。
- 精准喷洒正在验证 ROI：John Deere See & Spray 2025 年覆盖 500 万英亩，减少约 3100 万加仑非残留除草剂混合液。
- 植株级 AI 是主战场：Ecorobotix ARA 已售 1,000 台，Carbon、Verdant、Niqo、Solinftec 等都在推进精准除草、点喷和 robot fleet。
- 现有机器人常太贵、太重、太依赖单一作物或大农场；Monarch、Naio 等案例说明硬件 CAPEX、售后和田间可靠性是核心风险。

中国版时机：

- 2025 中央一号文件支持智慧农业，拓展人工智能、数据、低空等技术应用场景，推动国产先进适用农机装备研发应用。
- 2026 中央一号文件进一步把无人机、物联网、机器人写入农业科技创新场景，强调高端智能、丘陵山区适用农机装备。
- 《全国智慧农业行动计划（2024-2028年）》要求到 2026 年底农业生产信息化率超过 30%，到 2028 年底超过 32%。
- 农业农村部智慧农业指导意见明确设施种植要集成作物生长监测、环境调控、水肥管理和作业机器人。
- 2026 年农业农村部征集“人工智能+农业”典型场景，重点包括智慧种植、病虫害预测、供应链智能调度、溯源和市场预测。
- 大疆农业 2025 年年度报告称截至 2024 年底，全球约有 40 万架 DJI 农业无人机投入使用，农业无人机是最成熟的农业机器人入口之一。
- Qualcomm Dragonwing IQ10 RRD 支持高算力、多相机和传感融合，适合弱网、低延迟、端侧视觉推理的田间场景。

## Core Insight

农场数据的最小商业单元不是“地块”，而是“已闭环的农事任务”。

农户、基地和农服组织不买数字化。他们买三件事：

- 少漏活。
- 少扯皮。
- 能结算、能卖好价、能证明 ROI。

所以 AgriLoop 的核心不是 dashboard，而是：

> 发现问题 -> 生成任务 -> 指派人/机 -> 安全执行 -> 验证结果 -> 结算成本 -> 形成追溯 -> 改善下一次模型和 SOP。

## Solution

AgriLoop 是高价值作物的闭环 AI 作业层，不替代 DJI、XAG、Deere、FJD 或现有农场软件，而是在它们之上建立跨品牌作业闭环。

1. `EdgeScout`：Qualcomm edge 本地识别杂草、病斑、长势、缺水、成熟度、障碍物和作业 proof。
2. `Task Engine`：农技员确认处方，系统分配人、无人机、地面机器人、农机和验收标准。
3. `Safe Action`：机器人只在 geofence、限速、避障、天气和人工批准约束内执行。
4. `WorkProof`：GPS、图像、轨迹、用量、操作人、农资批次、安全间隔和 before/after 形成证据包。
5. `FarmOps Writeback`：写回库存、成本、追溯、采购商审计、农服结算和政府项目材料。
6. `Learning Loop`：低置信度、人工接管、复查失败进入 LeRobot HIL、区域云训练、AI Hub profile 和端侧灰度。

## Product Workflow

第一版只做最有付费意愿的闭环，不追求全自动农场：

1. 导入地块边界、作物计划、SOP、限制区、作业窗口、采收目标和采购商要求。
2. 无人机、固定相机、手机或 UGV 识别杂草、病斑、缺水和成熟度。
3. 系统生成处方和任务，农技员批准人机资源、用量和安全约束。
4. 无人机、农机、地面机器人或人工执行，机器人低置信度时请求接管。
5. WorkProof 写回库存、成本、追溯、采购商审计和下一轮训练队列。

## Market Wedge

不要先打所有农业，也不要先打重型大田农机。先打高价值、劳动密集、道路相对标准化、作业 proof 值钱的 specialty crops。

中国优先顺序：

1. 设施番茄、草莓、彩椒、黄瓜基地。环境可控、轨道/道路标准化、单品价值高、采摘和巡检高频。
2. 猕猴桃、柑橘、苹果等果园。巡检、点喷、采收辅助和搬运可分阶段闭环。
3. 浙江未来农场、数字农业工厂、智慧农业引领区。政策需要可展示、可复制的典型场景。
4. 农业社会化服务组织。机器人可按亩、按棚、按季收费，降低小农户 CAPEX。

海外优先顺序：

1. Greenhouse / nursery：环境可控，视觉和机器人部署更容易。
2. Vineyard / orchard：高价值、人工密集，spot treatment 和 harvest-assist ROI 清晰。
3. Specialty crop growers：有劳动力、除草剂、食品安全和批次追溯压力。
4. Labor contractor / service provider：按任务和设备小时付费，更适合 RaaS。

第二增长线：

- 规格外果蔬和农业剩余物的边缘分级、撮合与追踪，延展为循环农业 proof。
- 这条线不作为比赛主叙事，避免和公开同名 AgriLoop 循环农业项目混淆。

## Business Model

AgriLoop 按闭环作业和设备利用率收费，而不是一次性卖机器人。

中国：

- Paid pilot：50k-150k 元，6-8 周，一个作物、一个作业闭环、一个基地或农服队。
- Base software：60k-200k 元/基地/年，包含作业闭环、WorkProof、库存/成本、追溯和 dashboard。
- Edge kit：相机、传感器、离线同步盒、Qualcomm edge gateway、无人机/机器人 adapter 单独计费。
- RaaS / 农服：按棚、按亩、按任务或按设备小时收费，绑定作业 proof 和结算。
- County / enterprise：300k-1.5m 元/年，用于县域示范、龙头企业、多基地、多设备和政府项目材料。

海外：

- Paid pilot：15k-50k 美元，6-8 周。
- Site subscription：24k-90k 美元/年，按作物、基地、设备数和 workflow 计费。
- Enterprise / multi-site：100k-300k 美元/年。
- RaaS revenue share：按 acre、mission、robot-hour 或 verified savings 抽成。

Pilot KPIs：

- 作业记录完整率 >95%。
- 任务关闭周期下降 25-40%。
- 人工复查时间下降 20-30%。
- 低置信度/人工接管事件 100% 留痕。
- 农资用量、作业面积、作业人/设备、before/after 可追踪。
- 30 天内替代纸质记录和微信群验收，90 天内接入一个机器人/无人机执行点。

## Go-To-Market

先替代微信群验收，再接入机器人自动化。

- 中国打法：一个县一个作物模板，样板基地 -> 合作社/农服队 -> 农资经销商 -> 县域项目。
- 海外打法：Audit-ready crop-care loop，卖给温室集团、果园、葡萄园、packing house 和 labor contractor。
- 第一试点：一个作物、一个高频农事、一个农服团队、一个追溯或采购商输出。
- 扩张路径：作业记录 -> 巡检/植保闭环 -> 采收/搬运闭环 -> 多设备调度 -> 采购商/政府/保险接口。
- 渠道伙伴：农机经销商、无人机服务队、农资商、农技服务商、食品安全审计机构、Qualcomm 生态硬件伙伴。

## Competition

| 层级 | 代表玩家 | 强项 | AgriLoop 切口 |
|---|---|---|---|
| 大 OEM | John Deere / Blue River, Kubota / Agtonomy, CNH, AGCO | 整机、渠道、农机自动驾驶 | 重、贵、封闭；AgriLoop 更轻、更中立，面向混合车队和农服队 |
| 无人机 | DJI Agriculture, XAG | 植保、播撒、航测、硬件生态 | 把航测和作业接入任务、验收、结算和 HIL 训练 |
| 精准处理 | Carbon Robotics, Ecorobotix, Verdant, Niqo, Solinftec | 精准除草、点喷、robot fleet | AgriLoop 做多作物、多设备、多任务 proof layer |
| 农场软件 | FieldView, Trimble, Cropwise, AGRIVI | 农场管理、精准农业、处方图 | AgriLoop 更靠近一线执行、机器人工单和作业 proof |
| 国内玩家 | 大疆、极飞、丰疆、乔戈里、慧云、爱科农 | 设备、农机自动驾驶、采摘机器人、智慧农业平台 | AgriLoop 做跨设备执行证据和模型回流 |

## Moat

- 农事任务本体：作物、地块、病虫草害、投入品、机具、人员、时间窗、验收标准。
- 已验证事件图谱：图像、GPS、轨迹、农资批次、人工动作、采收结果连接到成本和利润。
- 作物 SOP 数据：不同区域、季节、品种、设备和农服队的真实执行效果。
- 设备集成：无人机、农机、机器人、相机、传感器、追溯和采购商系统 adapter。
- HIL 数据：人工纠正、机器人接管、行间漂移和复查失败持续变成可训练技能。
- 信任网络：基地、农服组织、采购商和县域项目使用同一套证据链，切换成本上升。

## Architecture

### Field Layer

- Drones / UGV / robots / fixed cameras / soil and weather sensors / implement telemetry。
- ROS 2、MAVLink、MQTT、LoRaWAN、ISOBUS read-only adapter。

### Edge Autonomy

- Qualcomm edge AI node。
- 本地感知推理、本地地图、geofence、障碍物/安全监控。
- LeRobot policy client / HIL bridge。
- Evidence packet builder。
- Offline-first cache。

### Regional Cloud

- Ingestion broker、object store/lakehouse、labeling/replay、training。
- Model registry、evaluation gates、Qualcomm optimization / validation、signed OTA。
- 中国数据留在中国租户；海外按客户和地区隔离。

### FarmOps Layer

- FMIS connectors、ADAPT/ISOXML-style export、Deere/Trimble/Climate-style APIs。
- Dashboards、agronomist review、work orders、prescription maps、completed-operation logs。

## Demo

比赛 demo 应展示“发现作物压力 -> 安全处理 -> 证明结果 -> 训练回流”：

1. 桌面温室或作物行间场景，放置真实盆栽、假杂草、病斑卡、缺水标记和地块二维码。
2. Qualcomm edge 设备连接相机或小车，离线识别疑似病虫草害、杂草、缺水或成熟度异常。
3. Dashboard 生成农事任务：目标位置、处方、执行设备、验收标准和安全提示。
4. 操作者批准后，小车/机械臂在 geofence、限速、避障和急停条件下执行安全动作。
5. 安全动作只使用水/染色水、LED 标记、移动到复查点或虚拟喷洒，不使用真实农药。
6. 系统生成 WorkProof、扣减 mock 库存、更新成本和追溯材料。
7. 操作者故意纠正一次漏检，AgriLoop 记录为 LeRobot HIL episode，并显示下一轮训练队列。

## Safety / Data

- Autonomous actuation 必须具备 geofence、任务批准、有效定位、避障、命令 freshness 和急停。
- ML 不拥有最终安全功能；停止、限速、锁定、watchdog 由独立安全控制负责。
- 真实农机控制总线只读接入，除非使用仿真或认证集成。
- 无人机操作遵循当地监管；比赛环境不做未经批准的飞行演示。
- 原始农场图像、边界、产量和机具日志属于敏感数据。
- 默认区域存储和区域训练，不跨农场使用可识别数据，除非明确 opt-in。
- 证据包保留 hash 和引用，避免暴露不必要的原始数据。

## Why Qualcomm

AgriLoop 是 Qualcomm edge AI 在农业场景的强样板：

- 农场网络不稳定，巡田、验收和机器人安全判断必须能在边缘本地运行。
- 农业机器人需要低功耗、多摄像头、GNSS/IMU、无线连接、弱网同步和本地安全监督。
- Qualcomm RB3/RB6/IQ 设备可以成为农场相机、无人机/机器人网关、农服队作业盒子和训练数据采集端。
- AI Hub、QNN、ONNX Runtime QNN EP 和 IM SDK 可形成模型编译、profile、部署和回滚证据。
- LeRobot HIL 让人工纠正、机器人接管和复查动作变成可复用训练数据。
- 对 Qualcomm 来说，AgriLoop 不只是农业 demo，而是“弱网、多传感、低功耗、长尾设备”的边缘 AI 参考设计。

## Claims To Avoid

- 不说全自动农场。
- 不说保证增产、保证节药或保证成本下降。
- 不说适配所有作物、所有天气、所有地块和所有农机。
- 不说可无监督喷洒农药或替代农技师决策。
- 不说已经满足 FSMA、GLOBALG.A.P.、中国农产品质量或无人机监管要求，除非逐项验证。
- 不说所有 LeRobot/VLA 模型都能跑在 Qualcomm NPU；只能说通过 profile 的模型部署到端侧。
- 不说 Qualcomm 官方合作/认证，除非真实签约。
- 循环农业延展不说 zero waste、carbon negative、feed-grade、food-grade、organic-certified 或 permanent carbon removal，除非独立验证。

## Ask

比赛阶段最需要 Qualcomm 支持三件事：

1. 开发板和 edge AI profile：用于多相机田间识别、离线 proof、功耗、弱网同步、QNN/ONNX artifact 和端侧 latency。
2. 农业样板连接：2 个中国设施农业或农服队样板，1 个海外温室/果园/葡萄园数据场景。
3. 生态联合展示：把 AgriLoop 做成 Qualcomm edge AI + LeRobot HIL + 农业机器人/无人机伙伴的商业化参考应用。

## Sources

- Mordor agricultural robots：https://www.mordorintelligence.com/industry-reports/agricultural-robots-market
- MarketsandMarkets agricultural robots：https://www.marketsandmarkets.com/Market-Reports/agricultural-robot-market-173601759.html
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- USDA ERS farm labor：https://www.ers.usda.gov/topics/farm-economy/farm-labor
- GAO precision agriculture：https://www.gao.gov/products/gao-24-105962
- John Deere See & Spray 2025：https://globalagtechinitiative.com/in-field-technologies/robotics-automation/john-deere-customers-use-see-spray-technology-across-five-million-acres-in-2025/
- Ecorobotix ARA：https://press.ecorobotix.com/449690-ecorobotix-reaches-milestone-1000-ara-ultra-high-precision-sprayers-sold-worldwide
- 全国智慧农业行动计划：https://www.moa.gov.cn/govpublic/SCYJJXXS/202410/t20241025_6465041.htm
- 农业农村部智慧农业指导意见：https://www.moa.gov.cn/govpublic/SCYJJXXS/202410/t20241025_6465040.htm
- “人工智能+农业”典型应用场景通知：https://scs.moa.gov.cn/tzggscxx/202604/t20260420_6483383.htm
- 2025 年农民工监测调查报告：https://www.stats.gov.cn/sj/zxfb/202604/t20260430_1963472.html
- DJI 农业白皮书发布：https://www.dji.com/media-center/announcements/dji-agricultural-annual-report-2025
- Qualcomm IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- 无人驾驶航空器监管：https://www.caac.gov.cn/XXGK/XXGK/FLFG/202401/t20240115_222642.html
