# 护元 CareOS Pitch

更新时间：2026-07-06。

## Core Thesis

护元 CareOS 是面向居家、社区和机构养老的护理生产力平台：

> 用 Qualcomm 端侧机器人、LeRobot 人机协同训练闭环和云端模型迭代，把巡护、提醒、递送、风险上报、任务核验和人工接管变成可记录、可复盘、可持续升级的照护能力。

它不定位为“机器人护士”，也不承诺替代护工、医疗诊断、用药决策或全自动照护。更稳妥的商业叙事是：

- 让护理员少跑腿、少重复提醒、少漏任务。
- 让机构和社区能把服务过程记录下来。
- 让家属看到经过授权的照护摘要，而不是原始监控视频。
- 让每次失败、人工接管和低置信度场景进入 LeRobot-style 数据集。
- 让 Qualcomm edge 成为养老机器人真正可部署的本体计算底座。

## Pitch Spine

### One-Line Company

护元 CareOS helps eldercare institutions, community care stations, and home-care providers turn fragmented care tasks into safe, auditable, human-supervised robot workflows.

中文一句话：

> 养老机构和社区护理团队用护元 CareOS 把巡护、提醒、递送、风险上报和人工接管交给安全可接管的边缘机器人执行，并把每次失败变成下一版可部署技能。

### Problem

养老行业不是缺一个聊天机器人，而是缺可复制的护理产能：

- 护理员时间被巡房、提醒、找物、递送、记录和家属沟通切碎。
- 机构和社区需要可证明的服务记录，否则很难验收、结算和扩点。
- 家属需要安心和摘要，但老人生活空间不能变成默认上传的监控视频。
- 机器人如果直接承诺“替代护工”会碰到安全、伦理、监管和接受度风险。

### Why Now

- 中国老龄化、养老设施、长护险制度化和“机器人+养老”政策在同一时期形成窗口。
- Qualcomm 端侧 AI、多摄像头、连接、安全启动和低功耗能力让本地感知执行更现实。
- LeRobot/HIL 让真实失败和人工接管可以变成可复用训练资产。
- 海外 ElliQ、Labrador、Moxi、Relay、Nobi、Vayyar、Hero Health 已经验证多个窄场景付费入口。

### Non-Obvious Insight

第一代可商业化养老机器人不是“机器人护士”，而是“护理团队放大器”：先把高频、低风险、可接管、可审计的碎片任务闭环，再用 HIL 数据逐步扩大技能边界。

### Solution

CareOS = Robot Edge + CareOps Console + Skill Cloud + Safety Envelope。

- Robot Edge 执行低速导航、端侧感知、隐私过滤、任务核验和轻物品操作。
- CareOps Console 管护理任务、服务记录、家属摘要、异常升级和角色权限。
- Skill Cloud 把失败、低置信度和接管片段变成 LeRobot episode，再发布到 Qualcomm edge。
- Safety Envelope 限制动作边界：不搬人、不诊断、不独立给药、不默认上传原始视频。

### Business Model

一句话收入模型：按“可验收的照护能力”收费，而不是一次性卖硬件。

- 试点包：3-6 个月、3-10 台机器人、部署培训和验收报告。
- 机构 RaaS：硬件租赁 + CareOS 软件 + 运维 + 数据看板。
- 居家长护包：服务商主导，机器人 + 家属小程序 + 远程看护 + 服务记录。
- OEM SDK：CareOS runtime、Qualcomm edge profile、Skill Cloud 和任务包授权。

### Competition

- ElliQ / Hyodol：陪伴提醒强，物理任务和机构工作流弱。
- Labrador：日常递送方向务实，但缺少机构级任务和训练平台。
- Moxi / Relay / Aethon：机构物流成熟，但主要面向医院和固定路线。
- Nobi / Vayyar / CarePredict：监测明确，但不是可行动机器人。
- CareOS：把感知、动作、接管、证据和训练连接成平台层。

### Ask

比赛阶段的 ask：

- 用 Qualcomm 开发板完成安全边界 demo。
- 形成养老机器人 reference task pack：送水、提醒、巡护、二维码核验、异常上报、人工接管。
- 输出 LeRobot HIL 数据样例和 Qualcomm edge artifact profile。

## Why This Matters

养老机器人不是“3 亿老人都买一台机器人”的消费电子故事。更真实的机会在失能、半失能、高龄独居、养老机构、社区照护站、长护险服务商和护理连锁。

五线程研究得到的核心信号：

- WHO 指出全球 60 岁及以上人口从 2020 年约 10 亿，将到 2030 年约 14 亿、2050 年约 21 亿。
- 中国国家统计局 2025 年末数据：60 岁及以上人口 3.2338 亿，占 23.0%；65 岁及以上 2.2365 亿，占 15.9%。
- 民政部 2024 年统计公报：全国养老机构和设施 40.6 万个，养老床位 799.3 万张。
- 长期护理保险正在制度化，政策鼓励居家和社区护理，并研究探索智能化服务和支持性辅具纳入支付。
- 海外市场已验证三个付费方向：医院/机构物流、居家陪伴提醒、跌倒/活动监测和药物提醒。
- 家庭物理辅助仍处早期，Labrador、Hello Robot、Kinova 等说明“递送和受限操作”比“全能照护”更可信。

## Product Definition

护元 CareOS 包含四层：

### 1. 护元 Edge

Qualcomm 端侧机器人核心。

- 居家/试点版：RB3 Gen 2 级别，适合多传感、低功耗、Linux/Ubuntu、Wi-Fi 6E、相机和本地 AI。
- 机构/高配版：IQ-9075 / IQ10 级别，适合多摄像头、更多 TOPS、5G/Wi-Fi、AMR 和 fleet 场景。
- 本地完成导航避障、隐私过滤、姿态/风险识别、条码/OCR、任务核验、断网缓存和安全停机。
- 生产版必须处理 secure boot、签名 OTA、debug 关闭、密钥注入和 SBOM/VEX。

### 2. CareOps Console

护理任务和服务证据系统。

- 任务：巡房、送水、取物、送餐、药盒提醒、康复陪练提醒、异常上报、家属摘要。
- 角色：护理员、护士长、机构运营、社区站、家属、远程接管员。
- 数据：任务时间、地点、完成状态、确认人、异常、接管、隐私等级、训练授权。
- 对接：FHIR Task-style workflow、机构系统、长护险服务记录、企微/钉钉/飞书、家属小程序。

### 3. Skill Cloud

LeRobot 训练和模型发布层。

- 收集低风险照护任务的多模态 episode。
- 标注成功、失败、低置信度、人工接管和安全拦截。
- 云端训练后生成 Qualcomm edge artifact。
- 灰度到单台/单机构，验证后再扩展，支持回滚。

### 4. Safety Envelope

安全边界和合规证据包。

- 不搬人、不抱人、不做医疗给药、不独立处置急救。
- 轻物品、低速、受限工作空间、软夹爪、急停、力/速度限制。
- Nav2 keepout zones、bathroom/bedroom privacy zones、stairs/kitchen risk zones。
- 默认上传结构化事件，不默认上传原始视频。
- 人在回路内，远程接管始终低于本地安全监督。

## China Version

中国版应讲“政策试点 + 养老服务运营 + 国产化边缘 AI”。

目标客户：

- 民政/工信/医保相关试点牵头方。
- 连锁养老机构、康复机构、护理院。
- 社区养老服务中心、街道综合养老服务平台。
- 长护险定点服务机构、家政护理连锁、物业养老服务商。
- 机器人 OEM 和集成商。

第一批场景：

- 夜间巡护和异常呼叫。
- 水杯、毛巾、餐盘、轻物品递送。
- 药盒/康复/饮水提醒，但不做给药决策。
- 房间、走廊、活动室的风险点巡查。
- 护理站跑腿和家属授权摘要。
- 居家床位和社区站的服务记录。

商业包装：

- 试点包：3-6 个月，3-10 台机器人，含场景调研、部署、培训、运维和数据报告。
- 机构 RaaS：硬件租赁 + CareOS 软件 + 运维 + 数据看板。
- 居家长护包：机器人 + 家属小程序 + 远程看护 + 服务商接管。
- OEM 授权：CareOS SDK、Qualcomm edge profile、Skill Cloud、标准任务包。

## Overseas Version

海外版应讲 workforce support、aging in place、senior living、privacy-preserving edge AI 和 RaaS。

目标客户：

- senior living / assisted living 连锁。
- home-care agencies。
- long-term services payers。
- AgeTech 渠道和医疗设备分销商。
- 养老服务机器人 OEM。

海外信号：

- ElliQ 证明陪伴和提醒有真实需求，但它不是物理照护平台。
- Labrador 证明“移动桌/货架 + 日常物品递送”是务实家庭入口。
- Moxi、Relay、Aethon 证明机构内固定路线物流可以商业化，但不能直接代表居家照护。
- Nobi、Vayyar、CarePredict 证明跌倒/活动监测是付费入口，但不是完全防跌倒。
- Hero Health 证明药物提醒和药盒管理有支付意愿，但最终用药责任仍在用户和护理者。

## Architecture

### Runtime Nodes

- `sensor_ingest`: camera, depth, radar/wearable optional, mic optional, robot state.
- `privacy_perception`: local face/screen blur, pose-only event, raw buffer policy.
- `fall_risk`: unusual posture, immobility, gait change, blocked path; alerting only.
- `med_task_verify`: barcode / GS1 DataMatrix / time-window / resident confirmation.
- `nav2_adapter`: maps, keepout zones, preferred lanes, collision monitor.
- `manip_action_shield`: light-object policy constraints, speed/force/workspace limits.
- `teleop_gateway`: dead-man switch, local safety override, intervention capture.
- `local_event_store`: encrypted event log, offline cache, upload queue.
- `policy_executor`: signed model release, confidence gate, rollback pointer.
- `fleet_rmf_adapter`: doors, elevators, hallways, charging docks in institutions.

### Data Objects

- `RobotState`: robot id, battery, thermal, pose, map, safety state.
- `ObservationFrame`: derived pose, occupancy, object detections, fall score, privacy tier.
- `CareTask`: resident pseudonym, location, schedule, required checks, status, audit trail.
- `MedicationCheck`: barcode, lot/expiry, resident/time match, confirmation actor, status.
- `ManipulationAction`: proposed action, shield result, executed or blocked reason.
- `TeleopIntervention`: reason, takeover time, recovery actions, trainable flag.
- `LeRobotEpisode`: task label, observation/action streams, success/failure, privacy policy.
- `SafetyEvent`: severity, trigger, local action, notifications, resolution.
- `ModelRelease`: dataset versions, evaluation metrics, Qualcomm target, rollout ring.

## Competition Demo

Demo 不需要真实老人、真实药品或医疗流程。最稳妥版本：

1. 在模拟养老房间里标记卧室、卫生间、厨房、楼梯和护理站。
2. 机器人执行送水/毛巾任务，使用 Nav2 keepout zone 和碰撞监控低速运行。
3. 机器人扫描托盘/药盒二维码，只做提醒和核验，不做给药。
4. 机器人发现“坐姿异常 / 无回应 / 通道障碍”这类模拟事件，先本地停机并请求护理员。
5. 页面显示只上传结构化事件和骨架/位置摘要，原始视频默认留在本地。
6. 操作员接管一次失败的取物动作，生成 LeRobot HIL episode。
7. 云端训练后输出 Qualcomm edge artifact，并展示灰度部署和回滚策略。

## Pilot KPIs

这些指标用于试点验收，不应写成既有成绩：

- 安全：严重安全事件 0；隐私事件 0；急停和人工接管全记录。
- 稳定：机器人在线率 >=95%；关键任务日志完整率 >=98%。
- 使用：机构场景 >=10 个有效任务/台/日；居家场景 >=5 个有效互动或辅助任务/日。
- 效率：护理员非核心跑腿、提醒、找物时间下降 10-20%，或每班节省 30-60 分钟，需现场实测。
- 接受度：护理员满意度 >=80%；老人拒用率 <15%；家属 NPS >30。
- 学习闭环：每个试点沉淀标准化任务数据集、失败案例库和下一版技能包。

## Why Qualcomm Should Care

护元 CareOS 是 Qualcomm 值得支持的场景，因为养老机器人天然需要：

- 多摄像头、多传感、低功耗、长生命周期。
- 弱网和断网下的本地推理、导航和任务缓存。
- 隐私优先的端侧 AI，不默认把生活空间视频上传云端。
- ROS 2、Nav2、Open-RMF、LeRobot 和 Qualcomm AI Hub 之间的真实部署链路。
- 可复制的参考设计：居家版、机构版、OEM SDK、Skill Cloud、试点 benchmark。

这比单纯炫技人形更适合讲“可靠、隐私、低延迟、人机协作和商业闭环”。

## Claims To Avoid

- 不说“替代护工/护士/医生”。
- 不说“全自动护理”“7x24 无人照护”“老人无需子女照护”。
- 不说“可治疗孤独、抑郁、失智”。
- 不说“完全防跌倒”或“保证安全”。
- 不说“自动给药、医疗诊断、急救处置”。
- 不说“长护险已经报销机器人硬件”；只能说政策正在研究探索智能化服务和支持性辅具。
- 不说“Qualcomm 官方背书/战略合作”，除非真实签约。
- 不说“LeRobot 已具备通用护理能力”；只能说用于数据标准化、训练和迭代。

## Sources

- WHO ageing and health：https://www.who.int/news-room/fact-sheets/detail/ageing-and-health
- BLS home health and personal care aides：https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm
- 国家统计局 2025 年统计公报：https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html
- 新华网 2024 年养老服务体系数据：https://www.xinhuanet.com/politics/20250725/5b74e57bc39e47099190cb8308655b21/c.html
- 国办银发经济文件解读：https://www.ndrc.gov.cn/xwdt/spfg/mtjj/202401/t20240117_1363422.html
- 长期护理保险制度文件：https://www.news.cn/politics/zywj/20260325/71e216ae767b487491ba1d9dbf9cf57d/c.html
- “机器人+”应用行动实施方案：https://news.cctv.com/2023/01/20/ARTI2DLvC4ty6iotNG0vLLsj230120.shtml
- NYSOFA ElliQ：https://aging.ny.gov/elliq-proactive-care-companion-initiative
- Labrador Systems：https://labradorsystems.com/products/
- Diligent Robotics Moxi：https://www.diligentrobots.com/moxi
- Relay Robotics hospitals：https://relayrobotics.com/relay-delivery-robots-for-hospitals
- Nobi smart lamps：https://www.nobi.life/en
- Vayyar Care：https://vayyar.com/care/
- Hero Health：https://herohealth.com/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm IQ-9075：https://www.qualcomm.com/internet-of-things/products/iq9-series/iq-9075
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- LeRobot HIL data collection：https://huggingface.co/docs/lerobot/en/hil_data_collection
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- ROS 2 lifecycle：https://design.ros2.org/articles/node_lifecycle.html
- Nav2 collision monitor：https://docs.nav2.org/tutorials/docs/using_collision_monitor.html
- Open-RMF：https://www.open-rmf.org/
- FHIR Task：https://build.fhir.org/task.html
- HHS de-identification：https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html
- ISO 13482：https://www.iso.org/standard/53820.html
