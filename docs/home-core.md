# HomeCore Pitch

更新时间：2026-07-05。

## Core Thesis

HomeCore 是家用机器人的技能内核：

> 像安装 App 一样安装机器人技能；用家庭示教和 LeRobot 训练；通过评估、权限和安全边界后，在 Qualcomm edge 本体侧本地执行。

它不是“万能家务管家”，也不是医疗设备或照护者替代品。它把家庭机器人能力拆成小而可信的技能：

- Table Reset：收拾轻量杯子、纸巾、零食盒和托盘。
- Toy Bin：把安全玩具和软物体放回指定区域。
- Entry Check：检查门口、灯光、包裹和家庭设备状态。
- Fetch Assist：在已映射房间内递送轻量日用品。
- Family Co-Care：提醒、日常摘要和远程家人支持。
- Smart Home：和灯、空气净化器、扫地机器人等设备联动。

一句话：不是承诺机器人什么都会，而是让每个家庭技能可安装、可示教、可评估、可本地执行、可持续更新。

## Why This Matters

消费机器人已经规模化，但大部分还停留在窄任务：

- IFR 报告 2024 年消费服务机器人销售接近 20M 台，家庭清洁、割草和 domestic-task 机器人是最大类别。
- 家庭照护需求长期存在。WHO 预测全球 60 岁以上人口从 2020 年约 1B 增至 2030 年约 1.4B。
- AARP / NAC 报告 2025 年美国 caregivers 约 63M，比 2015 年增加近 50%。
- 中国 2025 年末 60 岁及以上人口约 323.38M，占 23.0%；65 岁及以上约 223.65M，占 15.9%。
- 家庭场景的真正缺口不是“人形机器人炫技”，而是低风险、可复用、可订阅的日常支持技能。

市场启发：

- Matic 强调本地处理家中地图、音频和视频，证明 privacy-first 是家庭机器人核心卖点。
- SwitchBot K20+ Pro 证明移动智能家居平台路线比万能人形更接近短期市场。
- 1X NEO 和 Figure/Physical Intelligence 证明家庭操作有想象力，但仍需远程支持、人类校正和边界表述。
- Weave Isaac 从洗衣/折叠等 chore-specific manipulation 切入，说明先做任务垂直能力更可信。
- ElliQ / Intuition Robotics 和 Labrador Systems 说明 elder support 可以从陪伴、提醒、物品递送和家人连接切入。

## Product Modules

### 1. HomeCore Skill Library

家用技能商店。

- 每个技能有 capability contract：支持物体、适用区域、风险边界、传感器、执行器、权限和版本。
- 技能有状态：ready、beta、needs teaching、blocked、retired。
- 家庭技能不默认共享给其他家庭，训练数据和模型更新受用户授权控制。

### 2. Privacy-First Edge Runtime

家庭视频、音频和地图默认本地处理。

- 本地 wake word、ASR/TTS、物体识别、人物/宠物避让、语义地图和任务规划。
- local-only mode：摄像头、麦克风、上传、远程支持和训练开关可见。
- 家庭事件摘要可授权给家人，但不默认开启“持续监控”。
- 训练片段优先脱敏、裁剪和事件化，不上传完整全屋视频。

### 3. Teach-to-Skill Studio

示教到技能的闭环。

1. 用户安装技能。
2. 操作员或远程专家示教 10-20 条轨迹。
3. 数据进入 LeRobot-compatible dataset。
4. 中国云或海外云训练和评估。
5. 通过 SkillCertKit / SafetyOps 门禁。
6. 优化为 Qualcomm edge deployment package。
7. 本体执行，失败和纠正片段回流。

### 4. Family Co-Care Layer

家人协同，而不是照护替代。

- 日常提醒、房间 check-in、物品递送、设备状态、智能家居联动。
- Adult child / caregiver 可以看授权摘要：“今天是否按时互动、是否完成例行提醒、是否需要协助”。
- 不诊断跌倒、中风、痴呆、抑郁或其他医疗问题。
- 不宣称 emergency response；最多是用户确认后的求助建议或服务派单入口。

### 5. Smart Home Bridge

智能家居联动。

- Matter-compatible where supported。
- 灯光、空气净化器、扫地机器人、传感器、门铃、提醒设备等进入技能上下文。
- 不宣称 Matter 解决机器人问题；它只解决部分设备互操作，机器人仍需感知、语境和安全层。

### 6. Home ODD And Safety Boundaries

家庭机器人只在定义边界内工作：

- 室内、干燥、平整地面、已映射区域。
- 低速、低力、可见急停、app 停止、权限确认。
- 不走楼梯、湿浴室、阳台、车库、户外路线或未验证区域。
- 不处理刀具、热液体、火源、炉灶、碎玻璃、强腐蚀清洁剂、药物发放。
- 不承诺儿童、宠物或老人无人看护安全。

## Technical Architecture

### Edge

- RB3 Gen 2 / QCS6490 可作为 MVP：本地视觉、语音、地图、低速移动和小技能 demo。
- IQ-8275 / IQ-9075 作为更高多模态、多摄像头、本地 VLM/LLM 和复杂策略路线。
- 摄像头、深度/ToF、麦克风阵列、IMU、wheel/arm encoder、力/碰撞传感器。
- ROS 2 / Nav2-style navigation / MoveIt-style manipulation / safety supervisor / motor MCU。
- 本体保留安全层，学习策略只提出技能或 waypoint，不直接绕过碰撞、速度、关节和力限制。

### Cloud

- 授权示教片段进入 LeRobot。
- 云端负责训练、评估、压缩、量化、签名和模型 registry。
- AI Hub / Neural Processing SDK / QNN 路线用于优化、profile 和目标设备部署。
- 技能更新采用签名、灰度、回滚和家庭授权。

### Privacy

- Local-first inference。
- Visible camera/mic/upload indicators。
- 家庭成员权限分层。
- 保留、删除、导出和远程支持审计。
- 不把“本地处理”说成自动满足 GDPR/PIPL/HIPAA。

## China Version

中国版主张：

> HomeCore：陪伴 + 安全 + 居家养老中枢。

目标客户：

- 城市成人子女：父母独居或分居，希望有日常安全摘要，不想装满屋摄像头。
- 社区养老站 / 物业 / 运营商：需要可规模化的提醒、巡查、服务派单和家庭设备联动。
- 智能家居平台和家电厂商：需要家庭机器人技能内核，连接已有 IoT 设备。
- 养老机构和居家养老床位项目：需要非医疗、低风险、可审计的辅助系统。

收入模型：

- RMB 1,999-4,999 硬件或租赁 + RMB 29-99/月家庭服务。
- 与电信运营商、智能家居品牌、物业和社区养老站做 B2B2C。
- 传感器、安装、家庭设备联动和服务派单的附加收入。

## Overseas Version

海外版主张：

> Privacy-preserving home robot skills for caregiver relief and independent living.

目标客户：

- 工作中的成年子女 caregiver。
- 独立生活老人。
- home-care agency、senior living group、Area Agency on Aging、payer / Medicaid waiver pilots。
- 智能家居平台、家电/OEM 和机器人创业团队。

收入模型：

- $299-699 upfront + $30-80/month subscription。
- 低首付 lease + support / replacement / skill update。
- B2B2C per-member-per-month。
- 智能家居 bundle 和安装服务。
- White-label HomeCore for appliance/router/smart-speaker/robot OEM。

## Competition Demo

最稳妥 demo：

1. 家庭桌面场景：杯子、纸巾、零食盒、玩具盒。
2. HomeCore app 展示 `Table Reset - Beta`。
3. 展示技能 contract：支持杯子、纸巾、零食盒；不处理刀具、热液体、碎玻璃或无人看护。
4. 机器人本地识别安全物品并低速移动到托盘。
5. 出现不确定物体，机器人暂停并请求帮助。
6. 人工在 app / teleop 中纠正，片段进入 LeRobot dataset。
7. 页面展示训练、评估、边缘部署和技能 v1.1。
8. 切换 local-only privacy mode，展示无网情况下语音/感知仍可本地工作。

## Why Qualcomm Should Care

HomeCore 把 Qualcomm 放到家庭机器人增长入口：

- 家庭隐私要求本地 AI，不适合默认云端裸跑。
- 多摄像头、语音、视觉、低功耗和连接是家庭机器人基础。
- 家庭机器人需要长期更新、技能部署、回滚和本体安全边界。
- RB3/QCS6490 能做教育/MVP；IQ-8275/IQ-9075 能做更高端本地多模态；IQ10 可作为未来生产路线。
- AI Hub、LeRobot、SkillCertKit、SafetyOps 和 RobotAppLayer 可形成完整家庭技能生态。

一句话：

> HomeCore turns Qualcomm edge robots into privacy-first, teachable home skill devices.

## Claims To Avoid

- 不声称 fully autonomous household labor is solved。
- 不声称替代 caregiver、nurse、doctor、emergency responder。
- 不声称诊断跌倒、中风、痴呆、抑郁或其他医疗状态。
- 不声称 HIPAA / FDA / FCC / UL / ISO certified，除非实际完成认证。
- 不声称 child-safe、pet-safe、elder-safe 或 guaranteed safety。
- 不声称云训练、远程专家或相机流默认 privacy-preserving；必须有 opt-in、权限、脱敏和审计。
- 不把 Matter 或 smart-home API 描述成机器人能力本身。
- 不承诺 stairs、bathroom wet floor、cooking surface、open flame、medicine dispensing、door locking/unlocking safety function。

## Sources

- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- WHO ageing：https://www.who.int/news-room/fact-sheets/detail/ageing-and-health
- AARP / NAC caregiving 2025：https://www.aarp.org/pri/topics/ltss/family-caregiving/caregiving-in-the-us-2025/
- NYSOFA ElliQ 2026 update：https://aging.ny.gov/system/files/documents/2026/02/nysofa-elliq-project-update-2026.pdf
- 1X NEO：https://www.1x.tech/neo
- Weave Isaac 1：https://www.weaverobotics.com/isaac-1
- Weave Isaac 0：https://www.weaverobotics.com/isaac-0
- Matic privacy：https://maticrobots.com/blog/why-matic-is-the-most-private-and-secure-robot-vacuum
- SwitchBot K20+ Pro：https://us.switch-bot.com/products/switchbot-multitasking-household-robot-k20-pro
- China population 2025：https://www.stats.gov.cn/english/PressRelease/202602/t20260228_1962661.html
- China silver economy guideline：https://english.www.gov.cn/policies/latestreleases/202401/16/content_WS65a5b709c6d0868f4e8e31cc.html
- China elderly care reform guideline：https://english.www.gov.cn/policies/latestreleases/202501/07/content_WS677d340ac6d0868f4e8ee95d.html
- Xiaomi 2025 annual report：https://ir.mi.com/system/files-encrypted/nasdaq_kms/assets/2026/04/28/5-29-08/Xiaomi%202025%20AR_EN.pdf
- CareScout cost of care：https://www.carescout.com/cost-of-care
- ElliQ membership：https://elliq.com/products/membership
- Qualcomm QCS6490：https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm IQ-8275：https://www.qualcomm.com/internet-of-things/products/iq8-series/iq-8275
- Qualcomm Neural Processing SDK：https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai
- Qualcomm Matter guide：https://www.qualcomm.com/developer/blog/2026/02/designing-smart-home-devices-with-matter-developer-guide
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Matter：https://csa-iot.org/all-solutions/matter/
- LeRobot docs：https://huggingface.co/docs/lerobot/en/index
- LeRobot real-world getting started：https://huggingface.co/docs/lerobot/main/en/getting_started_real_world_robot
- LeRobot HIL data collection：https://huggingface.co/docs/lerobot/hil_data_collection
- ISO 13482：https://www.iso.org/standard/53820.html
- ANSI/CAN/UL 3300：https://webstore.ansi.org/standards/ul/ansiul33002024
- CPSC IoT connected products：https://www.cpsc.gov/Regulations-Laws--Standards/Voluntary-Standards/Internet-of-Things-IoT-Connected-Products
- NIST consumer IoT cybersecurity：https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-iot-program/consumer-iot-cybersecurity
- FDA general wellness guidance：https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices
- WCAG 2.2：https://www.w3.org/TR/WCAG22/
