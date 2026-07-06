# AgriLoop 农务闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

AgriLoop 是面向规模化种植基地、合作社和农业服务商的农务闭环系统：

> 把巡田、处方、派工、机器人/无人机执行、验收、成本、追溯和下一轮训练数据连成一条可验证的工作流。

它不做又一个农业机器人，也不做泛泛的智慧农业大屏。它做的是从 farm work 到 farm proof 的操作系统。

## Problem

农场经理通常知道“应该做什么”，但很难证明“到底做成了什么”。

典型痛点：

- 农事派活靠微信群、纸单和口头交代，漏活、返工和扯皮很常见。
- 无人机、农机、传感器、相机、人工巡田和合规系统各自记录，缺少统一任务语言。
- 农资用量、作业轨迹、工人/设备责任、作物批次和采收结果难以自动核验。
- 合格证、追溯、农残风险、采购商审计和政府项目材料经常临时补。
- 机器人或无人机发现问题之后，仍然缺少派工、执行、验收、成本和学习闭环。

## Why Now

- USDA ERS 预测 2026 年美国农场生产费用约 4777 亿美元，其中现金劳动力费用约 539 亿美元。
- USDA ERS 农业劳动力资料显示 H-2A 认证岗位从 FY2005 的约 4.8 万增长到 FY2024 的约 38.5 万；园艺、果树、温室等作物劳动密度更高。
- GAO 2024 年报告显示 2023 年美国仅约 27% 农场/牧场使用精准农业实践，复杂度和前期成本仍是主要障碍。
- John Deere / Blue River See & Spray、Carbon Robotics、Ecorobotix、DJI/XAG 等证明“看见一株植物并精准执行”已经商业化，但跨品牌闭环仍不足。
- 中国 `全国智慧农业行动计划(2024-2028年)` 要求到 2026 年底智慧农业公共服务能力初步形成，农业生产信息化率超过 30%。
- 中国农业无人机已经成为最成熟的农业机器人入口，政策和农机补贴正在把智能农机、智慧农场、植保和农业机器人推向真实场景。
- Qualcomm edge AI、低功耗连接、相机管线和 LeRobot HIL 让田间离线识别、机器人执行证据和云端训练回流变得更现实。

## Non-Obvious Insight

农场数据的最小商业单元不是“地块”，而是“已闭环的农事任务”。

农户、基地和农服组织不买“数字化”。他们买三件事：

- 少漏活。
- 少扯皮。
- 能卖好价。

所以 AgriLoop 的核心不是 dashboard，而是：

> 发现问题 -> 生成任务 -> 指派人/机 -> 验证结果 -> 结算成本 -> 形成追溯 -> 改善下一次决策。

## Solution

AgriLoop 用手机端、边缘 AI、设备连接和云端训练把农务工作流闭环：

1. 巡田图像、无人机航测、相机、IoT 和人工语音/照片进入 Field Evidence。
2. AI 识别病虫草害、长势异常、缺水、成熟度和作业风险。
3. 系统生成处方、农事任务、责任人、设备、用量、时间窗和验收标准。
4. 工人、无人机、拖拉机、UGV 或机器人执行任务，系统记录轨迹、照片、用量和操作人。
5. 验收结果自动更新库存、人工、成本、合格证、追溯、采购商审计包和下一轮模型训练队列。

## Product Workflow

第一版只做最有付费意愿的闭环，不追求“全自动农场”：

1. 建地块、作物、批次、SOP 和采收/销售目标。
2. 巡田或 drone/rover 扫描，边缘 AI 识别疑似病虫草害和长势异常。
3. 农技员确认处方，生成植保、巡检、采收、灌溉或复查任务。
4. 农服队、工人、无人机或机器人执行，上传轨迹、照片、用量和安全证据。
5. 系统验收作业、结算成本、生成合格证/追溯材料，并把低置信度和人工纠正转成 LeRobot HIL episode。

## Market Wedge

不要先打所有农业，也不要先打大田粮食。

首批 beachheads：

- 高价值果蔬：人工密集、农资风险高、批次追溯和品牌溢价直接。
- 果园/茶园/葡萄园：病虫害巡检、植保、采收、运输和合规记录密集。
- 设施农业/温室：环境可控、作业重复、相机和机器人部署更容易。
- 订单农业基地：采购商需要可审计的作业、投入品、采收和质量记录。
- 农服组织/植保队：按亩服务，需要作业证明、客户结算、设备利用率和培训。
- 县域智慧农业项目：需要智慧农业公共服务、典型场景、监管和示范材料。

## Business Model

一句话收入模型：按闭环农事任务、基地规模和边缘设备收费，而不是只卖机器人硬件。

- SaaS：按亩、基地、账号、活跃作业人员或作物模板收费。
- 设备网关：边缘相机、传感器、无人机/机器人 adapter、离线同步盒子。
- 合规包：合格证、追溯、采购商审计、FSMA / GLOBALG.A.P. / 中国农产品质量记录。
- 农服网络：按作业量、亩次、设备利用率和结算流水抽成。
- 企业/政府版：县域智慧农业、龙头企业、合作社联盟和大型基地私有化部署。

## Go-To-Market

先承诺“30 天把纸质农事记录和微信群验收替换掉”，再扩展到机器人/无人机调度。

- 中国切入：一个县一个作物模板，先做 3 个样板基地，再通过合作社、农服队、农资经销商和县域项目复制。
- 海外切入：面向果蔬出口商、packing house、农场集团、labor contractor 和食品安全审计顾问，主张 audit-ready in 30 days。
- 第一试点：一个作物、一个高频农事、一个农服团队、一个合规/追溯输出。
- 扩张路径：作业记录 -> 植保闭环 -> 采收/质量闭环 -> 多设备调度 -> 采购商/政府/保险数据接口。
- 渠道伙伴：农机经销商、无人机服务队、农资商、农技服务商、食品安全审计机构、Qualcomm 生态硬件伙伴。

## Competition

- DJI / XAG：无人机、喷洒、播撒、航测和硬件生态强，但跨品牌农务闭环有限。
- John Deere / CNH / AGCO / Kubota：农机和自动驾驶强，但机器和品牌边界明显。
- Blue River / Carbon / Ecorobotix / Verdant：精准除草和点喷强，但多作物多设备闭环窄。
- Taranis / Pix4D / Sentera / CropX：巡田、影像和农学洞察强，但执行和验收闭环弱。
- FieldView / PTx Trimble / Cropwise / AGRIVI：农场管理和精准农业强，但前线任务 proof 不够深。
- 慧云 / 爱科农 / FJD / 中联智慧农业：国内智慧农业和设备平台强，但 AgriLoop 做中立的任务闭环、证据和学习层。

AgriLoop 的位置：

> 跨品牌农务闭环层：把巡田洞察、处方、作业、验收、结算、追溯和训练数据连起来。

## Moat

- 农事任务本体：作物、地块、病虫草害、投入品、机具、人员、时间窗、验收标准。
- 已验证事件图谱：每张照片、GPS 点、机具轨迹、农资批次、人工动作和采收结果关联到成本、质量和利润。
- 作物 SOP 数据：越多闭环任务，越懂不同作物、区域、季节和设备的真实效果。
- 设备与渠道集成：无人机、农机、相机、传感器、ERP、追溯、采购商和政府平台 adapter。
- 合规信任：采购商、农服组织、基地和县域项目一旦使用同一套证据链，切换成本上升。
- LeRobot HIL 数据：机器人/无人机执行失败、人工纠正和复检动作回流为下一版技能。

## Architecture

### AgriCore

- `FieldBlock`、`CropBatch`、`FarmTask`、`InputBatch`、`WorkProof`、`HarvestLot`、`AuditPack`。
- 作物 SOP、任务引擎、责任人、时间窗、验收标准、成本核算、合格证/追溯输出。

### EdgeScout

- Qualcomm edge 摄像头/机器人/无人机网关。
- 本地病虫草害识别、长势异常、成熟度评分、PPE/作业 proof、低置信度标记。
- 弱网可用，先本地记录，再同步云端。

### FarmOps Console

- 作业派单、设备调度、农服队结算、库存扣减、作物批次、采购商审计包。
- 中国版默认中国本地数据平面；海外版按 FSMA、GLOBALG.A.P. 和采购商要求输出记录。

### Learning Loop

- 低置信度识别、人工纠正、机器人接管、复查失败进入主动学习。
- LeRobotDataset 记录相机、状态、动作、时间戳、控制模式和 intervention flag。
- 云端训练后经 Qualcomm AI Hub / QNN / ONNX Runtime QNN EP profile，再灰度回 edge station。

## Data Objects

- `FieldBlock`: 地块边界、作物、品种、责任人、灌溉/设施条件。
- `CropBatch`: 播种/定植、投入品、作业历史、采收批次、销售/采购商。
- `PlantFinding`: 病虫草害、长势、成熟度、缺水、位置、置信度、图像证据。
- `FarmTask`: 类型、处方、用量、执行人/设备、时间窗、验收标准、状态。
- `WorkProof`: GPS、轨迹、照片、视频、机具 telemetry、人工签名、用量和 before/after。
- `InputBatch`: 农资名称、批号、库存、领用、地块、任务和安全间隔。
- `AuditPack`: 合格证、追溯码、采购商审计、政府项目、农残/投入品记录。
- `LeRobotEpisode`: task text、observation、action、timestamp、control mode、intervention flag。

## Demo

比赛 demo 应该展示“发现问题之后的闭环”，而不是只展示识别框：

1. 桌面小农场或温室行间场景，放置真实盆栽、假杂草、病斑卡、缺水标记和地块二维码。
2. Qualcomm edge 设备连接相机或小车，离线识别疑似病虫草害/杂草/长势异常。
3. Dashboard 生成农事任务：目标位置、处方、执行设备、验收标准和安全提示。
4. 人工批准后，小车/机械臂执行安全动作：放置标记、喷清水、移动到复查点或拍摄 after image。
5. 系统自动生成 WorkProof、扣减 mock 库存、更新成本和追溯材料。
6. 操作者故意纠正一次漏检，AgriLoop 记录为 LeRobot HIL episode，并显示下一轮训练队列。

## Why Qualcomm

AgriLoop 是 Qualcomm edge AI 在农业场景的强样板：

- 农场网络不稳定，巡田和验收必须能在边缘本地运行。
- 农业机器人需要低功耗、多摄像头、GNSS/IMU/无线连接、弱网同步和本地安全监督。
- Qualcomm edge 设备可以作为农场相机、无人机/机器人网关、农服队作业盒子和训练数据采集端。
- AI Hub、QNN、ONNX Runtime QNN EP 和 IM SDK 可形成模型编译、profile、部署和回滚证据。
- LeRobot HIL 让人工纠正、机器人接管和复查动作变成可复用训练数据。

## Claims To Avoid

- 不说全自动农场。
- 不说保证增产或保证农药减少。
- 不说适配所有作物、所有天气、所有地块和所有农机。
- 不说可无监督喷洒农药或替代农技师决策。
- 不说已经满足 FSMA、GLOBALG.A.P.、中国农产品质量或无人机监管要求，除非逐项验证。
- 不说所有 LeRobot/VLA 模型都能跑在 Qualcomm NPU；只能说通过 profile 的模型部署到端侧。
- 不说 Qualcomm 官方合作/认证，除非真实签约。

## Ask

比赛阶段最需要 Qualcomm 支持三件事：

1. 开发板和 edge AI profile：用于田间/温室识别、离线 proof、功耗和弱网同步证据。
2. 农业样板连接：2 个中国样板基地或农服队，1 个海外果蔬/温室 pilot 数据场景。
3. 生态联合展示：把 AgriLoop 做成 Qualcomm edge AI + LeRobot HIL 的农业参考应用。

## Sources

- OECD-FAO Agricultural Outlook 2026-2035：https://www.oecd.org/en/publications/2026/06/oecd-fao-agricultural-outlook-2026-2035_5610f218.html
- USDA ERS farm sector income forecast：https://www.ers.usda.gov/topics/farm-economy/farm-sector-income-finances/farm-sector-income-forecast
- USDA ERS farm labor：https://www.ers.usda.gov/topics/farm-economy/farm-labor
- GAO precision agriculture：https://www.gao.gov/products/gao-24-105962
- Arkansas See & Spray research：https://aaes.uada.edu/news/see-and-spray-research/
- John Deere autonomous 9RX：https://www.deere.com/en-us/john-deere-news/autonomous-9rx
- IFR service robots 2025：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- MarketsandMarkets agricultural robots：https://www.marketsandmarkets.com/Market-Reports/agricultural-robot-market-173601759.html
- 全国智慧农业行动计划：https://www.moa.gov.cn/govpublic/SCYJJXXS/202410/t20241025_6465041.htm
- 农机购置与应用补贴：https://njhs.moa.gov.cn/tzggjzcjd/202406/t20240604_6456671.htm
- 农业无人机市场信号：https://jhs.moa.gov.cn/jjyx/202601/t20260122_6480954.htm
- 农业机器人典型场景征集：https://njhs.moa.gov.cn/tzggjzcjd/202606/t20260616_6485036.htm
- 无人驾驶航空器飞行管理暂行条例：https://www.caac.gov.cn/XXGK/XXGK/FLFG/202401/t20240115_222642.html
- FDA FSMA traceability rule：https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods
- GLOBALG.A.P. IFA fruit and vegetables：https://www.globalgap.org/what-we-offer/solutions/ifa-fruit-and-vegetables/
- Qualcomm RB3 Gen 2 development kit：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- ROS 2 control：https://control.ros.org/rolling/doc/ros2_control/hardware_interface/doc/hardware_interface_types_userdoc.html
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
