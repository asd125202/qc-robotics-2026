# 护元 CareOS 照护异常闭环 Pitch

更新时间：2026-07-06。养老政策、长护险、护理机构支付、隐私合规、机器人安全和医疗软件边界变化很快；正式提交前需要复核客户流程、监管红线、设备认证和数据合规。

## 一句话

护元 CareOS：把远方子女的担心，变成可执行的照护。

它面向居家、社区、机构、长护险服务商和护理团队，把日常节律、温和提醒、非急救异常、机器人递送、人机接管、家属摘要和服务证据，变成可派单、可验证、可复盘、可训练的照护异常闭环。

## Problem

养老的痛点不是缺一个聊天机器人，而是没人知道“现在该谁做什么”。

- 父母不想被摄像头监控，也不想过早离开熟悉的家。
- 子女每天在猜：没接电话是在睡觉、忘了提醒，还是需要人去看一眼。
- 护理员进门前常常不知道过去 12 小时发生了什么。
- 机构需要夜间巡视、提醒、服务记录、家属沟通和质控留痕。
- 长护险、家庭养老床位和社区服务需要过程证据和结算材料。

现有方案碎片化：手表要戴、按钮要按、音箱太被动、摄像头太冒犯、人工护理太贵且不足。

## Why Now

老龄化、护理缺口、政策支付和 edge AI 在同一窗口叠加。

- WHO 预计全球 60+ 人口从 2020 年约 10 亿增至 2030 年 14 亿、2050 年 21 亿；80+ 到 2050 年约 4.26 亿。
- WHO 估计到 2030 年全球卫生工作者短缺 1100 万。
- BLS 预计美国 home health and personal care aides 2024-2034 增长 17%，每年约 765,800 个岗位空缺。
- AARP/NAC 2025 报告称美国 6300 万成人是照护者，约 1/4 成人。
- 2025 年末中国 60 岁及以上人口 3.2338 亿，占总人口 23.0%。
- 2024 年末中国各类养老机构和设施 40.6 万个，养老床位 799.3 万张。
- 中国长护险正在从试点走向全国建制，2025 年底试点地区 92 个、覆盖 3.08 亿参保人。

真正的创业窗口来自：家庭照护能力变薄、机构人力不足、长护险制度化、智能养老机器人试点和端侧机器人能力同时成熟。

## Core Insight

家庭不会为“机器人”付费，他们为“我知道下一步该谁做”付费。

CareOS 不是跌倒报警器、陪聊玩具或机器人护士，而是照护异常闭环系统：

`发现异常 -> 判断严重度 -> 找到责任人 -> 远程确认/机器人辅助 -> 升级家属/护理员/机构 -> 自动文档 -> 形成支付与风控证据`

## Solution

CareOS 在老人同意的边界内学习日常基线，先用温和提醒处理低风险任务，再按风险和权限升级给家人、护理员、机构或服务商。机器人只在安全边界内执行递送、提醒、巡护和低风险辅助。

1. 发现异常：未回应、药盒未确认、夜间多次起身、长时间静止、离床/离房、通道障碍、服务逾期。
2. 判断优先级：按风险等级、护理计划、时间窗口、家属偏好、机构 SOP 和服务商 SLA 排序。
3. 自动派单：分配给老人本人、家属、邻居、护理员、机构值班人员、服务商或远程接管员。
4. 验证结案：用确认按钮、语音回应、位置摘要、机器人状态、护理员记录和签名证据关闭任务。
5. 训练迭代：把低置信度、人工接管、误报/漏报复盘和机器人动作失败导出为 LeRobot episode。

## Product Workflow

- Care Circle：老人、子女、护理员、邻居、机构和医生联系人各自拥有不同权限和通知规则。
- Baseline：端侧学习起居、活动、门磁、药盒、睡眠和厨房节律，只保存必要元数据。
- Assist：温和提醒吃饭、喝水、预约、药盒确认、起夜柔光和轻物品递送。
- Escalate：疑似跌倒、无回应、长时间静止或异常开门，先询问本人，再通知照护圈。
- Close：确认、接管、上门、复核和下一步安排进入护理日志与训练数据。

## Market Wedge

先从高焦虑、高支付意愿、高闭环需求的照护入口切入：

- 远程子女家庭：术后恢复、行动不便、轻度记忆下降、夜间风险高和子女异地。
- Home-care agencies：no-contact、迟到、漏记、未确认、家属沟通和班次交接闭环。
- Senior living / memory care：wellness check、夜间离床、漏服药提醒、家属询问和人工巡查排序。
- 中国社区养老：街道养老站、家庭养老床位、居家上门服务和补贴核销。
- 长护险服务商：失能评估、护理项目目录、服务证据、结算材料和质量监管。
- 医养/康复机构：出院后康复、慢病随访、康复提醒、护理机器人接入和家属摘要。

## Business Model

按可闭环照护异常收费，不按机器人硬件一次性收费。

- 机构 / Senior Living：中国 ¥20-60/人/月 core，¥60-150 pro；海外 US$8-20 core，US$20-45 pro。
- 护理院 / 高 acuity：中国 ¥60-150/人/月，¥150-280 高阶；海外 US$15-95/人/月。
- 居家服务机构：中国 ¥10-30/活跃客户/月，¥30-80 带家属门户；海外 US$5-30/客户/月。
- 出院 / 康复 episode：中国 ¥80-300/30天，¥300-800 带临床/RPM 伙伴；海外 US$25-175。
- 家庭订阅：家庭 app、监测、concierge 月费；参考 medical alert / family care subscription 价格带。
- OEM SDK：Qualcomm/ODM/OEM reference design + CareOS runtime + Skill Cloud + edge profile 授权。

Pilot fees：中国 ¥30k-100k/机构点位，海外 US$5k-25k/点位，周期 8-12 周。医院/出院 episode 试点按 cohort 定价。

## Pilot KPIs

早期只承诺工作流指标，不承诺医疗结果。

- 通用：异常确认时间、关闭时间、SLA 内关闭率、未分配异常、重复/噪声告警、每个 closed exception 的员工分钟数、审计完整率、家属升级和 adverse-event review 完成率。
- Senior living：75%-85% exceptions closed within SLA；unresolved wellness checks 下降 15%-25%；家属咨询量下降 10%-20%。
- Nursing homes：care-task audit completeness 90%-95%；missed med/repositioning/rounding exceptions 在窗口结束前升级。
- Home-care agencies：迟到/漏访异常下降 15%-25%；call-off fill time 下降 10%-20%；护理记录 24h 内完成率提升 10 个百分点。
- Hospital discharge/home rehab：48 小时内 med pickup/med-rec confirmation 80%+；7 天内首个 follow-up 确认；康复 adherence 提升 10-15 个百分点。
- Family care：daily check-in adherence 65%-80%；urgent family acknowledgement <15 分钟；caregiver task completion 提升 15%。

## Competition

现有产品证明需求，但多数停在单点事件。

- 跌倒/远程监测：SafelyYou、Vayyar、Nobi、CarePredict、Apple Watch、Medical Guardian 强在发现事件，弱在跨设备确认、分派、复核和服务证据。
- 药物提醒：Hero、MedMinder、Spencer 强在提醒，弱在和起居、活动、护理任务统一排序。
- 陪伴机器人：ElliQ、PARO、Lovot 强在陪伴，弱在物理照护任务和机构 workflow。
- 机构软件/EHR：PointClickCare、MatrixCare、WellSky、AlayaCare 是 system of record，不是实时执行层。
- 配送/辅助机器人：Moxi、Aethon、Relay、Labrador、Pudu 可减轻跑腿，但缺少 eldercare exception OS。
- CareOS：把发现、确认、分派、机器人辅助、家属摘要、服务证据和 HIL 训练串起来。

## Moat

- 信任界面：老人愿意长期放在家里，子女能理解摘要，护理员不觉得被监控。
- 隐私边缘计算：默认输出事件、轮廓、时间线和置信度，不把生活空间变成云端摄像头。
- 照护图谱：谁该知道什么、何时升级、谁确认、如何交接，随家庭和机构长期使用变准。
- 多模态基线：视觉、语音、门磁、药盒、活动、环境和机器人状态融合，比单设备更稳。
- 服务证据：任务、异常、确认、接管、上门、家属查看和服务商结算材料可审计。
- Edge profiles：QNN/AI Hub profile、签名 OTA、回滚、模型版本、延迟和安全拦截记录。

## Demo

三分钟 demo：

1. 护理员在 dashboard 设置药盒、水和餐食提醒；药物是 placebo prop。
2. 机器人在本地发出 scheduled reminder，用户用机器人/平板确认，提醒可 snooze。
3. 机器人用 ROS 2/Nav2 低速从客厅到厨房 waypoint，避开 geofenced no-go zones。
4. 机器人带封闭水瓶或餐卡在托盘中完成低风险 handoff，HIL 操作员可用手柄接管。
5. 演员未回应并在椅边暂停，系统标记“needs check-in / fall-risk pattern”，不说“fall detected”。
6. 机器人后退并询问是否需要帮助，无回应则向 caregiver dashboard 发送最小必要 evidence packet。
7. dashboard 展示 timestamp、reminder state、robot pose/path、anomaly reason、model version、HIL marker、user response 和 signed audit hash；原始视频默认本地保留，不上传。

安全约束：

- 不诊断、不急救派单、不配药、不发药、不提供临床建议。
- 提醒话术是“照护计划中的提醒”，不是“必须服用某药”。
- 只用封闭水瓶、餐卡或毛巾，不用热液体、玻璃、刀具或真实药品。
- 低速、预建图、无楼梯、隐私区禁入、物理急停、无线 deadman、现场操作员。
- 任何阻力、低置信度、接管触发都导致停止或后退。

## Why Qualcomm

CareOS 是 Qualcomm “Physical AI in the home” 的高价值样板。

- Always-on Edge AI：姿态、活动、物体、条码、语音、异常节律和隐私过滤优先在本地完成。
- Robotics Runtime：ROS 2、Nav2、Open-RMF、低速导航、HIL 接管和安全门控需要稳定 edge。
- AI Hub / QNN：模型 profile、量化、性能证据、设备目标、签名部署和回滚可以成为试点评估材料。
- Privacy by Design：不默认上传原始家庭视频，只上传 consented event evidence 和去标识化 HIL correction。
- OEM Reference：RB3/RB5/IQ10 路线 + CareOS SDK 可成为养老机器人和 home-care hardware 的默认照护层。

## Claims To Avoid

- 不说防止跌倒、检测所有紧急事件或保证安全。
- 不说诊断恶化、治疗孤独/抑郁/失智。
- 不说替代护工、护士、医生或子女。
- 不说自动给药、临床建议、急救处置。
- 不说 FDA cleared、HIPAA/GDPR/PIPL compliant、可报销，除非真实完成。
- 不说长护险已经报销机器人硬件；只能说服务费用和智能化服务存在政策探索空间。
- 不说 Qualcomm 官方背书或 LeRobot 已具备通用护理能力。

## Sources

- WHO ageing and health：https://www.who.int/news-room/fact-sheets/detail/ageing-and-health
- WHO health workforce：https://www.who.int/health-topics/health-workforce
- BLS home health and personal care aides：https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm
- PHI direct care workers 2025：https://www.phinational.org/resource/direct-care-workers-in-the-united-states-key-facts-2025/
- AARP caregiving 2025：https://www.aarp.org/pri/topics/ltss/family-caregiving/caregiving-in-the-us-2025/
- CDC falls：https://www.cdc.gov/falls/data-research/index.html
- CareScout cost of care：https://www.carescout.com/cost-of-care
- China NBS 2025：https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html
- China aging report 2024：https://www.cncaprc.gov.cn/u/cms/www/202507/24154203fka1.pdf
- People Daily caregiver gap：https://paper.people.com.cn/rmrb/pc/content/202505/09/content_30071988.html
- China eldercare reform：https://www.news.cn/politics/zywj/20250107/d38c451b3d7f4eb1aec8ce0b4e9a4e23/c.html
- China LTCI：https://www.nhsa.gov.cn/art/2026/3/26/art_104_20039.html
- ElliQ：https://aging.ny.gov/elliq-proactive-care-companion-initiative
- Vayyar Care：https://vayyar.com/care/
- Nobi：https://www.nobi.life/en
- Hero Health：https://herohealth.com/
- Moxi：https://www.diligentrobots.com/moxi
- Labrador：https://labradorsystems.com/products/
- Qualcomm RB5：https://www.qualcomm.com/developer/hardware/robotics-rb5-development-kit
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm QNN SDK：https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai
- Nav2 collision monitor：https://docs.nav2.org/configuration/packages/collision_monitor/configuring-collision-monitor-node.html
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- ISO 13482：https://www.iso.org/standard/53820.html
- FDA low-risk wellness guidance：https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices
