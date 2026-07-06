# WarehouseLoop 仓库异常闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

WarehouseLoop 是面向电商仓、3PL、多客户履约仓、跨境海外仓和制造备件仓的仓库异常闭环平台：

> 把错拣、缺货、卡单、滞留、破损、设备卡停和退货待判，从群聊救火变成可派单、可追踪、可验证、可回写、可复盘、可训练的异常闭环。

它不替代 WMS/WES/AMR，不从“全自动无人仓”开始，也不强卖一整套机器人。第一步是让仓库里每天发生的异常可以被发现、派单、修正、验证、回写和复盘。

## Problem

买方痛点不是“机器人不够聪明”，而是：

> 仓库最贵的不是作业，而是异常没人闭环。

仓库主管每天被异常打断：WMS 只记录状态，群聊只传递情绪，现场人员靠经验补救。结果是订单延迟、重复盘点、跨班扯皮、客户投诉、加班成本和管理层救火。

典型客户：

- 中大型 3PL、多客户履约仓、跨境海外仓。
- DTC 服饰、美妆、消费电子品牌仓。
- 退货中心、换标/贴标/质检工位。
- 已经有 WMS/WES/AMR，但现场异常仍靠微信群、Excel、纸单和主管记忆补洞的 brownfield 仓。

高频痛点：

- 错拣/错库位：SKU 被放到 B-02，WMS 仍显示 A-03。
- 缺货/卡单/漏扫：收货、上架、复核、包装缺少证据链。
- 退货质检：破损、错货、疑似欺诈、可售/不可售判定缺标准证据，返架慢。
- 临时工和旺季：新人不熟流程，异常堆积，主管只能事后追责。
- 机器人项目：AMR 能搬运，AS/RS 能存取，机械臂能抓取，但失败、低置信度、人工接管和 WMS 状态更新没有闭环。

## Why Now

订单碎片化、即时履约、退货增长、用工波动、物流降本和机器人普及，让异常频率和处置成本同时上升。企业不再只买自动化设备，而是需要一套能把异常压下去的运营系统。

关键变化：

- 退货变成 CFO 级问题。NRF 预计 2025 年美国零售退货规模约 8499 亿美元，线上退货率 19.3%。
- 全球仓库自动化市场仍在增长，软件和编排层的重要性上升。
- 美国 Q1 2026 电商销售 3267 亿美元，同比 +9.8%，占零售 16.9%。
- 中国仓储成本压力明确。2025 年社会物流总费用/GDP 降至 13.9%，政策目标到 2027 年约 13.5%。
- 中国电商和跨境规模巨大。2025 年快递业务量 1989.5 亿件，跨境电商进出口约 2.75 万亿元。
- 中国机器人采用已足够高，下一层机会是 WMS/WES/RCS/TMS/摄像头/机器人日志之间的多系统协同。
- LeRobot 和 Qualcomm edge AI 让“失败 -> 接管 -> 训练 -> 端侧部署”有了可演示路径。

## Insight

异常不是单点事件，而是一条未完成的业务链。

真正的问题不在“有没有报警”，而在报警之后：

- 异常由谁负责？
- 多久响应？
- 是否升级？
- 证据是否足够？
- 系统状态是否被回写？
- 有没有根因和防复发动作？

WarehouseLoop 的数据单元不是一张库存表，而是：

> exception + owner + SLA + action + evidence + writeback + review + HIL episode

## Solution

WarehouseLoop 是 existing warehouse 之上的异常闭环操作层。

核心产品：

1. **Capture**：订单、库存、路径、设备、人员状态、固定相机、扫码、RFID、称重和 WMS 对账发现异常。
2. **Classify**：判断影响订单、客户、时效、SLA、退货价值、dock dwell 和 AMR 任务风险。
3. **Dispatch**：把异常变成有负责人、SLA、优先级、目标状态、所需证据和截止时间的任务。
4. **Close**：扫码、照片、视频、RFID、重量变化和机器人状态组成证据包，回写 WMS/WES/TMS。
5. **Learn**：失败、低置信度、人工接管和复发导出为 LeRobot episode。

三类首发工作流：

- 收货 / 上架差异：ASN、到货、扫码、拍照、库位确认和异常索赔。
- 库位错放 / 盘点差异：相机、扫码、RFID、重量和人工复核形成 proof。
- 退货质检 / 可售判定：RMA、照片、条码、破损等级、可售/不可售/复检。

## Product Workflow

1. Mock/real WMS 下发“SKU A 应在 A-03”的库存或退货任务。
2. Edge camera / scanner / RFID 发现 SKU A 在 B-02，或退货箱破损、条码不匹配。
3. WarehouseLoop 创建 ExceptionCase，标注异常类型、置信度、责任人、SLA 和所需证据。
4. 系统派单给仓员、主管、AMR、机械臂或远程协助。
5. 人或机器人纠偏：移动 SKU、复核退货、贴标、分拣、装入正确 tote/bin。
6. 扫码、拍照、视频、RFID 或重量变化验证完成。
7. WMS/WES/ERP 状态从 `异常` 变成 `已修正`，证据包进入审计记录。
8. 人工接管、失败动作和低置信度片段导出为 LeRobot dataset。
9. 中国版在阿里云 PAI / 华为 ModelArts / 腾讯 GPU 云训练；海外版在 AWS SageMaker / Google Vertex AI / Azure ML 训练。
10. 训练结果经 AI Hub / QNN / ONNX Runtime QNN profile 后回到 Qualcomm edge device。

## Market Wedge

第一客户不是所有仓库，而是：

- 中小 3PL 和多客户履约仓：多客户、多 SLA、多系统、多临时工，最需要中立闭环层。
- DTC 品牌仓：服饰、美妆、消费电子 SKU 多、退货多，返工和库存准确率敏感。
- 跨境海外仓：退货分级、换标、破损、疑似欺诈和库存纠偏是高价值场景。
- 自动化集成商：AMR/ACR/WMS/WES 项目里，异常闭环是可复制插件。
- 制造业仓储/线边配送：MES order、kitting、QR/RFID 验证和失败接管可以复用同一闭环。

中国版重点：

- 跨境电商、仓配一体、海外仓、保税仓、制造业仓储。
- 本地云、本地数据、私有部署、企微/钉钉/飞书任务通知。
- 和 Geek+、海柔、快仓、海康机器人、立镖、劢微、未来机器人、系统集成商做生态连接。

海外版重点：

- 3PL、DTC returns center、high-SKU e-commerce、apparel/beauty/electronics。
- 从一个退货/putwall/receiving station 切入，避免超大客户长周期全仓改造。
- 和 WMS/WES、AMR、RaaS、系统集成商合作，而不是正面替代。

## Business Model

收入模型：

> 试点费 + 仓年费 + 模块费 + 系统集成费 + 按订单行/闭环异常的用量费

建议价格：

- 60-90 天试点：中国 ¥8万-30万/仓；海外 US$25k-100k/仓。
- 仓年费：中国 ¥20万-80万/仓/年，大仓/多模块 ¥80万-200万/仓/年；海外 US$60k-250k/仓/年，企业版 US$250k-600k/仓/年。
- 用量/模块：中国 ¥0.03-0.20/订单行，或 ¥1-5/闭环异常；海外 US$0.01-0.08/line，或 US$0.25-2/closed exception。
- 集成/硬件：WMS/WES 集成、码头/托盘视觉、RFID/扫码/称重、AMR/RCS 连接器单独收费。
- 成果费：大客户可加 10%-20% verified savings success fee。

试点 KPI：

- 库存准确率和 SKU-location 差异。
- 错拣/错数量/错批次。
- 异常从触发到责任人接受、处理、回写的 median/P90 dwell。
- dock dwell / dock-to-stock。
- 退货 receive-to-disposition。
- 可见破损/少件/标签异常自动建单率。
- AMR intervention rate。
- WMS/WES 回写延迟、失败率和人工 override 审计。

## Go-To-Market

第一步不是“让仓库无人化”，而是拿到一个客户愿意付费的异常流程。

路径：

1. 找 2-3 家 design partner：3PL、跨境退货中心、服饰/美妆品牌仓。
2. 选择一个高频流程：退货质检、收货差异、错库位纠偏、putwall 复核。
3. 60-90 天部署一个轻集成闭环：相机/扫码/RFID/称重 + mock or real WMS + 人工/机器人任务。
4. 用客户数据证明 KPI：更快关闭异常、更少返工、更短返架、更低主管追踪时间。
5. 扩展到同仓更多流程：receiving -> putaway -> return grading -> replenishment -> kitting。
6. 再复制到多仓、多客户、多机器人 fleet。

渠道：

- WMS/WES/RMS 厂商：把 WarehouseLoop 作为现场 proof 和机器人训练层。
- AMR/ACR/机械臂厂商：为其失败/异常提供任务和数据闭环。
- 系统集成商：负责现场部署，WarehouseLoop 保留软件、数据和云训练订阅收入。
- Qualcomm 生态：以 RB3/RB6/Dragonwing 作为 edge reference design。

## Competition

竞争不是“谁有机器人”，而是谁能把异常闭环成数据资产。

- Locus / Geek+ / AMR/RaaS：人机协作和货到人强；WarehouseLoop 负责异常、proof、WMS 回写和训练回流。
- AutoStore / Symbotic / Exotec：AS/RS 和 mega-DC 自动化强；WarehouseLoop 面向 brownfield 3PL、退货和上下游异常。
- Corvus / Dexory / Gather AI：库存扫描和数字孪生强；WarehouseLoop 进一步把异常变成任务、纠偏、proof 和 HIL 数据。
- Hai / Quicktron / Hikrobot：国内 AMR/ACR 生态成熟；WarehouseLoop 做多系统异常和训练插件。
- WMS/WES/QMS：system of record 强；WarehouseLoop 是 system of action, evidence and learning。
- 群聊/人工：短期灵活但无法沉淀 SLA、根因、证据、跨班责任和复发预防。

## Moat

核心护城河不是通用视觉模型，而是：

> exception-owner-SLA-action-evidence-writeback-review-training graph

会积累的资产：

- 异常图谱：错拣、缺货、卡单、库存差异、dock dwell、AMR 卡停和退货争议的根因链。
- 证据标准：SKU、库位、tote/bin、条码、RFID、照片、重量、视频、模型版本和 WMS 状态。
- HIL 数据：人工接管、低置信度、错误识别、AMR 卡停、复核驳回和恢复策略。
- 连接器：WMS/WES/ERP/RMS/RCS/TMS、AMR、RFID、扫码、称重和工位系统。
- SOP benchmarks：客户 SOP、SLA、责任分派、审计证据、退货规则和 KPI benchmark。
- Qualcomm edge model profiles、deployment recipes、fallback layer 和 rollback records。
- 中国/海外两套云训练和数据边界 playbook。

## Architecture

### LoopCore

- WMS/ERP/WES/RMS/RCS 连接器。
- ExceptionCase、WarehouseTask、VerificationEvidence、ReturnAssessment。
- 任务规划、SLA、审计日志、报表、模型注册和回滚。
- CSV/API/mock WMS 起步，后续接 Oracle、Manhattan、Blue Yonder、SAP、金蝶、用友、聚水潭等。

### LoopEdge

- Qualcomm RB3 Gen 2 / RB6 / Dragonwing IQ10-class edge device。
- 固定相机、腕部相机、手持扫码、RFID、称重、AMR、机械臂。
- 本地识别条码、SKU、库位、包装破损、缺件、多件、错放和动作失败。
- 弱网缓存、本地审计 buffer、离线执行门控。

### LoopRMF

- ROS 2 / Nav2 / MoveIt 2 / ros2_control / Open-RMF。
- 把 WarehouseTask 转成 AMR route、robot arm stages、fleet task、door/charger traffic。
- 支持混合厂商，不要求替换已有 AMR/ACR。

### Learning & Cloud Split

- LeRobotDataset v3 记录多相机视频、状态、动作、任务、episode 边界和结果。
- HIL loop：deploy -> intervene -> record -> fine-tune -> redeploy。
- 中国训练：阿里云 PAI、华为 ModelArts、腾讯 GPU 云；原始视频和订单数据留在中国。
- 海外训练：AWS SageMaker、Google Vertex AI、Azure ML。
- Qualcomm 部署：AI Hub profile、QNN/QAIRT、ONNX Runtime QNN EP、edge artifact signature 和 rollback。

## Competition Demo

比赛 demo 用 2-3 层小货架、6-9 个库位、3 个 mini pallet/tote、SKU 盒子、QR/AprilTag、固定 edge camera、可选扫码枪/RFID/称重台和低速 rover 即可。

3 分钟故事：

1. Mock WMS 显示 `SKU-A` 应在 `A-03`。
2. 现场货架故意把 `SKU-A` 放在 `B-02`。
3. Qualcomm edge camera 识别库位 AprilTag + SKU QR，生成红色异常卡。
4. 系统派单给仓员、低速 AMR 或小机械臂纠偏。
5. 扫码/拍照验证，WMS 从 `exception_open` 变成 `closed_verified`。
6. 第二个退货箱破损/条码不匹配，低置信度触发人工复核。
7. 人工接管片段导出为 LeRobot episode。
8. 页面展示云训练任务、AI Hub edge profile 和下一轮模型队列。

## Why Qualcomm

WarehouseLoop 让 Qualcomm 在仓库 physical AI 中不是装饰，而是必要基础：

- 仓库现场需要低延迟、多摄像头、弱网可运行的边缘感知。
- 条码/RFID/相机/AMR/机械臂/安全门控需要稳定本地 gateway。
- 客户的 SKU、订单、视频和退货数据不能都上传到公共云。
- RB3 Gen 2 适合比赛原型；RB6/Dragonwing IQ10 适合生产级仓储移动机器人和 workcell。
- AI Hub / QNN / QAIRT / ONNX Runtime QNN EP 让云训练模型变成可验证、可回滚的 edge artifact。
- LeRobot HIL 把人工接管转成下一版技能，Qualcomm edge 让技能在现场可靠执行。

## Ask

比赛阶段的明确请求：

- Qualcomm RB3 Gen 2 或 RB6 级别开发板 + Vision Kit。
- 一个 mock WMS/API 样例和 5-10 个真实仓务异常流程样本。
- 3 个潜在试点场景：3PL 退货中心、跨境海外仓、品牌履约仓。
- 1-2 个 AMR/机械臂/扫码/RFID 生态伙伴用于 demo。
- AI Hub / QNN profile 支持，用于展示“云训模型到 edge deployment”的完整证据链。

## Claims To Avoid

- 不说替代 WMS/WES。
- 不说完全无人仓、lights-out、零错误、0 人力。
- 不说机器人自主解决所有异常。
- 不说一天接入所有系统；更可信的是轻集成、先接关键数据源。
- 不说通用机器人能处理所有 SKU、软包、破损和退货。
- 不说 Qualcomm 官方合作/认证，除非真实签约。
- 不承诺固定 ROI；只承诺试点验证指标。

## Sources

- NRF 2025 retail returns：https://nrf.com/research/2025-retail-returns-landscape
- Warehouse automation market：https://www.mordorintelligence.com/industry-reports/warehouse-automation-market
- Interact Analysis warehouse automation：https://interactanalysis.com/warehouse-automation-order-intake-up-by-7/
- MHI/Deloitte 2026：https://www.businesswire.com/news/home/20260415926416/en/New-MHI-and-Deloitte-Report-Finds-AI-is-Biggest-Disruptor-of-Supply-Chains-Over-the-Next-Decade
- US Census e-commerce Q1 2026：https://www.census.gov/retail/mrts/www/data/pdf/ec_current.pdf
- BTS warehouse labor：https://www.bts.gov/newsroom/may-2026-us-transportation-sector-unemployment-36-falls-below-may-2025-level-44
- Locus AMR scale：https://locusrobotics.com/blog/seven-billion-picks-warehouse
- Symbotic FY26 Q2：https://ir.symbotic.com/news-releases/news-release-details/symbotic-reports-second-quarter-fiscal-year-2026-results
- Corvus GNC case：https://www.corvus-robotics.com/case-study-gnc
- Dexory：https://www.dexory.com/en-us
- NDRC logistics cost：https://www.ndrc.gov.cn/fggz/202602/t20260209_1403645.html
- Logistics cost action plan：https://www.mee.gov.cn/zcwj/zyygwj/202411/t20241128_1097450.shtml
- 2025 express parcels：https://www.mot.gov.cn/shuju/tongjishuju/youzheng/202601/t20260130_4199355.html
- China online retail 2025：https://www.stats.gov.cn/sj/zxfb/202601/t20260119_1962323.html
- 2025 cross-border ecommerce：https://jingji.cctv.com/2026/03/18/ARTI7pCFc4m1r2a7w3mJH2u5260318.shtml
- Geek+ HKEX listing：https://www.geekplus.com/zh-cn/resources/news/geekplus-lists-on-hkex-main-board-pioneering-the-global-smart-logistics-transformation-with-robotics
- Hai Robotics：https://www.hairobotics.com/news/hai-robotics-2025-year-end-recap-year-we-climbed-higher
- Quicktron profile：https://www.quicktron.com/zh_CN/about-us
- Oracle WMS REST APIs：https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faips/wm-rest-apis.html
- Manhattan automation APIs：https://developer.manh.com/docs/reference/app/mawm/automation-and-robotics/
- GS1 EPCIS 2.0：https://www.gs1.org/standards/epcis
- Open-RMF：https://www.open-rmf.org/
- ROS 2 control：https://control.ros.org/rolling/doc/ros2_control/controller_manager/doc/userdoc.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / AI Engine Direct：https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- Alibaba Cloud PAI：https://www.alibabacloud.com/help/zh/pai/product-overview/what-is-machine-learning-platform-for-ai/
- Huawei ModelArts：https://www.huaweicloud.com/product/modelarts.html
- Tencent GPU cloud：https://cloud.tencent.com/product/gpu
- AWS SageMaker training：https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html
- Google Cloud custom training：https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/configure-compute
- Azure Machine Learning：https://learn.microsoft.com/en-us/azure/machine-learning/
