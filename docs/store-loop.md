# StoreLoop 门店异常闭环 Pitch

更新时间：2026-07-06。零售、即时履约、药店合规、门店视频、POS/ERP/WMS、ESL、边缘 AI 和机器人部署都变化很快；正式提交前需要复核客户系统、地区法规、设备安全和数据合规。

## 一句话

StoreLoop：让每一次门店异常都有闭环。

连锁零售用 StoreLoop 把缺货、错价、陈列偏差、冷柜/临期、即时零售拣货超时、退货待判和药店追溯异常，从门店现场问题变成可派单、可验证、可复盘、可训练的异常闭环。

## Problem

痛的是区域经理、店长和总部运营，不是算法团队。

- 总部看到 BI 和销售报表时已经太晚。
- 区域经理巡店低频、主观、样本少。
- 店长靠群消息和电话救火，没有 owner、SLA、升级链和结案验证。
- 一线员工缺少照片、库存快照、价签 OCR、扫码记录和复扫证明。

门店异常发生在分钟级，管理动作却经常是小时级或天级。

## Why Now

门店容错率正在下降。

- 2025 年中国社会消费品零售总额 50.12 万亿元；便利店和超市仍增长，但零售从扩张进入效率和利润保卫战。
- 2024 年中国即时零售规模 7810 亿元，预计 2026 年突破 1 万亿元；线下门店正在变成本地履约节点。
- IHL 2025 估算全球零售因缺货和过剩库存产生约 1.73 万亿美元库存失真损失。
- NRF 预计 2025 年美国零售退货 8499 亿美元，线上退货率 19.3%。
- 中国药店在 2026 年面临医保个人账户白名单、追溯码全量采集上传、票据和处方合规等更强闭环要求。

同时，门店已有摄像头、电子价签、POS 接口、扫码、边缘算力和低速机器人底盘，第一次让“异常闭环自动化”具备可部署基础。

## Core Insight

门店的问题不是看不见，是没有闭环。

单点 AI 会制造更多告警。真正有价值的是把异常变成：

- 责任明确：谁处理。
- 时限明确：多久处理。
- 证据明确：用什么证明处理过。
- 结果可验证：是否复扫通过。
- 经验可沉淀：失败、误报、复发和人工接管进入 SOP 与训练数据。

## Solution

StoreLoop 是 existing store 之上的异常闭环操作层。

它不替代 POS、ERP、WMS、电子价签、视频监控或店员任务系统，而是连接这些系统，把门店真实状态推进到结案：

1. Detect：边缘摄像头、巡检机器人、员工照片、ESL、POS、库存和 IoT 发现异常。
2. Decide：按销售损失、合规风险、订单 SLA、库存状态和人力可用性排序。
3. Dispatch：生成有 owner、SLA、目标状态、证据要求和升级链的任务。
4. Verify：复扫、拍照、扫码、OCR、POS 快照或人工确认验证完成。
5. Learn：失败、低置信度、人工接管和复发进入异常库与 LeRobot 数据集。

## Market Wedge

首批客户不是所有零售商，而是总部强运营、门店多、SKU 多、即时履约压力大、SOP 强、异常可量化的连锁业态。

- 便利店：高频 SKU、夜间人力少、即时订单多，缺货、错价、临期和冷柜异常可量化。
- 社区超市/生鲜：低毛利、高损耗、高频补货，空面、临期、报损和冷链响应影响利润。
- 连锁药房：药品追溯码、批次、效期、医保白名单、处方交接和近效期处理需要总部审计。
- 即时零售前置门店：线上承诺库存必须等于货架真实状态。
- 会员店/大卖场：货架面积大、人工巡检贵，适合全店视觉或巡检机器人版。
- 美妆、3C、专业零售：促销陈列、锁柜、退货待判和高价值 SKU 需要证据化闭环。

## Business Model

收入来自“异常在同班次被关闭”，不是卖摄像头。

- 软件闭环版：中国 ¥500-2,000/店/月；海外 US$500-1,500/店/月。接 POS/库存、现有摄像头或员工照片、任务流和总部看板。
- AI 重点区域版：中国 ¥2,000-8,000/店/月；海外 US$1,000-5,000/店/月。先做冷柜、端架、高频 SKU、退货区和药房柜台。
- 全店视觉/机器人版：中国 RaaS ¥8,000-25,000/店/月；海外可按 US$3,000-8,000/店/月建模。适合大店、会员店和区域旗舰。
- 企业集成/品牌数据：中国项目费 ¥5万-50万，海外 US$25k-250k。覆盖总部 API、SLA、供应商共担和 CPG 洞察。

试点经济模型按单店计算：

`年收益 = 恢复销售毛利 + 节省工时 + 减少损耗/报损 + 减少价签错误/投诉/罚款 + 退货回架收益 - 年化订阅/硬件/实施成本`

## 60-90 天试点指标

- 重点 SKU 可得率：中国 +1-3pp，海外成熟超市 +2-5pp。
- 高频 SKU 缺货/低货架事件下降 15-30%。
- 重点货架 planogram compliance +5-15pp，或达到 90%+。
- 价签/促销错配下降 50-80%。
- 冷柜异常中位响应时间 <15 分钟，未关闭异常下降 30-60%。
- 退货到可售/报损 dwell time 下降 20-50%。
- 大店每周释放 15-50 小时巡检/找货/价签核查工时；小店 3-15 小时。
- 高优先级任务同班次关闭 ≥85%，重开率 <10%。
- SKU 映射 >95%，库存同步延迟 <15 分钟，接口成功率 >99%。

这些指标应作为试点目标，不作为未经验证的对外承诺。

## GTM

从 20-50 家门店的区域试点进入总部预算。

1. 选择同一区域、同一店型、同一高频异常，设置对照门店和 baseline。
2. 用 4-8 周诊断输出异常损益表：可恢复销售、错价数量、缺货时长、员工巡检节省、库存修正率。
3. 60-90 天验证同班次关闭率、响应时长、复发率、价签差错、OOS 时长、冷柜异常和退货返架。
4. 成功后从一个异常模块扩到多模块，再从区域复制到集团总部和供应商共担。

买方是 COO、门店运营负责人、数字化负责人、商品/供应链和损耗负责人。渠道伙伴包括 POS/ERP/WMS、ESL、视频集成、机器人厂商、药店 SaaS、零售咨询和 Qualcomm edge 生态。

## Competition

StoreLoop 不是和摄像头比清晰度，而是和人工巡店、BI 报表、单点视觉 AI 比闭环。

- 人工巡店灵活但低频、主观、不可规模化。
- CCTV 能留视频，但不理解 SKU、库存、价格、促销和任务闭环。
- BI/ERP 看结果和库存记录强，但不知道货架现场是否真实。
- Simbe/Focal/Vusion/Captana/Trax/Pensa/Brain 等证明 shelf intelligence 需求真实。
- Zebra、Blue Yonder、RELEX、Oracle/SAP、YOOBIC、WorkJam、Reflexis 等负责计划、任务、安全或库存，但缺少“门店真实状态 -> 异常优先级 -> 执行验证 -> 模型训练”的统一层。

## Moat

护城河不是单个模型，而是：

- 门店异常库：缺货、错价、错位、临期、冷柜、退货、药品追溯、拣货超时和漏扫。
- 行业 SOP 映射：不同业态、门店规模、班次、人力和总部规则对应不同 owner、SLA 和证据要求。
- 处理结果反馈：任务是否完成、是否复扫通过、是否复发、是否被店长驳回。
- 连接器：POS、ERP、WMS、OMS、ESL、RFID、药品追溯、企微/钉钉/飞书和门店视频系统。
- 跨店 benchmark：同区域、同品类、同店型异常密度、响应时长和复发模式。
- Edge profiles：QNN/AI Hub profile、模型版本、延迟、内存、fallback 和回滚记录。

## Competition Demo

三分钟桌面 demo：

1. 启动设备，展示本地相机、dashboard、物理急停、软件急停和断网可运行。
2. 低速扫描车或固定相机扫描两层货架，AprilTag 定位货架格，QR/OCR 读取价签。
3. 系统发现四类异常：空面但后仓有 12 件、SKU 错位、纸价签 OCR 6.90 与 POS 7.50 不一致、反光遮挡低置信度。
4. 生成补货、价签复核、错位整理和人工确认任务；10 分钟未处理升级店长。
5. 遮挡/反光触发 human-in-the-loop，只记录复核任务，不直接写库存或价格。
6. 复扫通过后工单 closed，证据包展示模型版本、库存快照、处理人、复扫图片和 AI Hub/QNN profile。
7. 失败、低置信度和接管片段进入 LeRobot dataset。

安全约束：

- 桌面封闭场景，车速建议 ≤0.2 m/s。
- 云端只做训练、遥测和看板，不参与急停、避障、实时控制。
- 不做人脸识别、顾客画像、动态定价。
- 机器人不能直接写 POS/库存/价格，所有业务变更由人确认。
- Nav2 Collision Monitor 只能作为软件保护层，不能替代硬件安全。

## Why Qualcomm

门店是高密度、多摄像头、强隐私、弱网络容错的边缘 AI 场景。

Qualcomm 的价值不是装饰，而是让门店 AI 从“能跑”变成“能规模化跑”：

- Edge Vision：SKU、空面、价签、促销牌、QR、AprilTag、冷柜和退货区都需要现场判断。
- AI Runtime：AI Hub、QNN、ONNX Runtime QNN EP 和量化 profile 把云训练模型变成可度量 edge artifact。
- Local Privacy：默认不做人脸识别和顾客画像；上传前只保留必要 crop、证据元数据和脱敏片段。
- Offline First：断网时仍能扫描、生成本地任务、缓存证据包，联网后同步总部。
- Hardware Path：QCS6490/RB3 Gen 2 做比赛原型，QCS8550/RB6/Dragonwing 路线支持更高阶迁移。

## Claims To Avoid

- 不说“全球首个门店异常闭环系统”。
- 不说准确率 99%、零误报、无需人工干预。
- 不承诺部署后固定营收提升或损耗下降，除非来自真实试点。
- 不说适用于所有门店、所有异常、所有行业。
- 不说无需集成即可完整闭环。
- 不说替代店长或店员。
- 不说 Qualcomm 官方推荐、认证或合作，除非有书面依据。
- 不把核心卖点写成“视觉大模型识别门店行为”；核心卖点是异常闭环带来可衡量运营改善。

## Sources

- China Retail 2025：https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html
- China Retail 2026 YTD：https://www.stats.gov.cn/sj/zxfb/202606/t20260616_1963954.html
- Instant Retail：https://www.news.cn/20251126/0acf69e715b1432d8eb6e48d0822f918/c.html
- AI + Consumption：https://app.xinhuanet.com/news/article.html?articleId=2026061881b7f34785a74704882e80c4e72beec1
- IHL Inventory Distortion：https://www.ihlservices.com/news/analyst-corner/2025/09/retail-inventory-crisis-persists-despite-172-billion-in-improvements/
- NRF Returns 2025：https://nrf.com/research/2025-retail-returns-landscape
- NRF Shrink：https://nrf.com/media-center/press-releases/shrink-accounted-over-112-billion-industry-losses-2022-according-nrf
- Deloitte Retail Outlook：https://www.deloitte.com/us/en/insights/industry/retail-distribution/retail-distribution-industry-outlook.html
- Simbe Tally 4.0：https://www.simberobotics.com/about/newsroom/simbe-unveils-tally-4-0-the-next-generation-of-autonomous-retail-robot-powering-store-intelligence-via-physical-ai
- Focal Systems：https://focal.systems/
- Vusion Captana：https://www.vusion.com/na/products/captana/
- Trax / FORM：https://www.form.com/newsroom/form-and-trax-merge/
- Brain ShelfOptix：https://www.braincorp.com/scanning-as-a-service
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub Profile：https://workbench.aihub.qualcomm.com/docs/hub/profile_examples.html
- Qualcomm QNN SDK：https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- AprilTag：https://april.eecs.umich.edu/software/apriltag
- Nav2 Collision Monitor：https://docs.nav2.org/configuration/packages/collision_monitor/configuring-collision-monitor-node.html
