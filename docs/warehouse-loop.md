# WarehouseLoop 仓务异常闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

WarehouseLoop 是给 3PL、品牌仓、跨境海外仓和退货中心的仓务异常闭环平台：

> 发现错货、漏扫、破损、库位不一致，派人或机器人纠偏，拍照/扫码验证，并自动回写 WMS；每一次接管都变成 LeRobot 训练数据。

它不替代 WMS，不从“全自动仓库”开始，也不强卖一整套机器人。第一步是让仓库里每天发生的异常可以被发现、派单、修正、验证、回写和学习。

## Problem

买方痛点不是“机器人不够聪明”，而是：

> WMS 说库存正常，货架现场已经错了。

典型客户：

- 中小 3PL、多客户履约仓、跨境海外仓。
- DTC 服饰、美妆、消费电子品牌仓。
- 退货中心、换标/贴标/质检工位。
- 已经有 WMS/WES/AMR，但现场异常仍靠微信群、Excel、纸单和主管记忆补洞的 brownfield 仓。

高频痛点：

- 错库位：SKU 被放到 B-02，WMS 仍显示 A-03。
- 漏扫/少件：收货、上架、复核、包装缺少证据链。
- 退货质检：破损、错货、疑似欺诈、可售/不可售判定缺标准证据。
- 临时工和旺季：新人不熟流程，异常堆积，主管只能事后追责。
- 机器人项目：AMR 能搬运，AS/RS 能存取，机械臂能抓取，但失败、低置信度、人工接管和 WMS 状态更新没有闭环。

## Why Now

仓库自动化预算在上升，但客户不想先承担全仓重建风险。异常闭环是更轻、更快、更能付费的入口。

关键变化：

- 退货变成 CFO 级问题。NRF 预计 2025 年美国零售退货规模约 8499 亿美元，线上退货率 19.3%。
- 物流用工仍紧。Descartes 调查显示 76% supply chain / logistics operations 正在经历劳动力短缺。
- 供应链技术预算打开。MHI/Deloitte 2025 报告称供应链领导者正在增加数字化、自动化和机器人投资。
- 中国仓储成本压力明确。2025 年社会物流总费用与 GDP 比率仍在 13.9% 附近，政策目标到 2027 年降到约 13.5%。
- 中国电商和跨境规模巨大。2025 年快递业务量约 1990 亿件，跨境电商进出口约 2.84 万亿元。
- 机器人商业化正在从 demo 走向运营。Locus、Brightpick、Ambi、Dexterity、GXO/Agility、Geek+、海柔、快仓等证明仓库愿意为真实产能付费。
- LeRobot 和 Qualcomm edge AI 让“失败 -> 接管 -> 训练 -> 端侧部署”有了可演示路径。

## Insight

仓库自动化的第一桶金不是无人仓，而是异常闭环。

WMS/WES 知道“应该发生什么”；AMR/ASRS/机械臂负责“移动或执行一部分动作”；真正缺的是：

- 现场是否真的发生了？
- 异常由谁负责？
- 纠偏是否有照片、扫码、RFID、重量或视频证据？
- 系统状态是否被回写？
- 低置信度和人工接管是否成为下一轮机器人技能数据？

WarehouseLoop 的数据单元不是一张库存表，而是：

> exception + task + action + evidence + writeback + HIL episode

## Solution

WarehouseLoop 是 existing warehouse 之上的异常操作层。

核心产品：

1. **Exception Capture**：固定相机、手持扫码、RFID、称重台、AMR、机械臂、手机拍照和 WMS 对账发现异常。
2. **Task Dispatch**：把异常变成有负责人、SLA、优先级、目标库位、所需证据和截止时间的任务。
3. **Human/Robot Correction**：仓员、主管、AMR、机械臂或远程协助完成纠偏。
4. **Proof & Writeback**：扫码、照片、视频、RFID、重量变化和机器人状态组成证据包，回写 WMS/WES/ERP。
5. **LeRobot Learning Loop**：失败、低置信度和人工接管导出为 LeRobot episode，云端训练后部署到 Qualcomm edge。

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

> pilot fee + robot/workcell monthly fee + cloud training subscription + per-closed-exception success fee

建议价格：

- 付费试点：中国 8-12 周，20-60 万元；海外 30k-80k 美元集成/部署费。
- 工位订阅：中国按工作站、摄像头节点、任务量和 WMS 集成收费；海外 8k-15k 美元 / 月 / 工位。
- 云训练订阅：中国版使用阿里云/华为/腾讯区域内训练；海外版使用 AWS/GCP/Azure。
- 成功费：按 corrected item、closed exception、return processed、pick/orderline 成功数加价。
- OEM/集成商授权：异常闭环 SDK、Qualcomm profile、LeRobot 数据导出、WMS 连接器和任务模板。

试点 KPI：

- 错货/错库位修正时间。
- 退货返架周期。
- 每件触点数。
- 人工接管率。
- WMS 回写延迟。
- 异常关闭率。
- 训练后同类任务成功率。

## Go-To-Market

第一步不是“让仓库无人化”，而是拿到一个客户愿意付费的异常流程。

路径：

1. 找 2-3 家 design partner：3PL、跨境退货中心、服饰/美妆品牌仓。
2. 选择一个高频流程：退货质检、收货差异、错库位纠偏、putwall 复核。
3. 8-12 周部署一个 workcell：相机/扫码/RFID/称重 + mock or real WMS + 人工/机器人任务。
4. 用客户数据证明 KPI：更快关闭异常、更少返工、更短返架、更低主管追责时间。
5. 扩展到同仓更多流程：receiving -> putaway -> return grading -> replenishment -> kitting。
6. 再复制到多仓、多客户、多机器人 fleet。

渠道：

- WMS/WES/RMS 厂商：把 WarehouseLoop 作为现场 proof 和机器人训练层。
- AMR/ACR/机械臂厂商：为其失败/异常提供任务和数据闭环。
- 系统集成商：负责现场部署，WarehouseLoop 保留软件、数据和云训练订阅收入。
- Qualcomm 生态：以 RB3/RB6/Dragonwing 作为 edge reference design。

## Competition

竞争不是“谁有机器人”，而是谁能把异常闭环成数据资产。

- Locus / 6 River / Robust.AI：人机协作和 AMR pick assist 强；WarehouseLoop 负责异常、proof、WMS 回写和训练回流。
- Brightpick / Nimble / Ambi / Dexterity：机器人动作和自动化履约强；WarehouseLoop 从更轻的异常工位切入。
- AutoStore / Exotec / Ocado：goods-to-person 和 AS/RS 强；WarehouseLoop 补上下游异常和退货闭环。
- Symbotic / Amazon Robotics：mega-DC 自动化强；WarehouseLoop 面向 brownfield 3PL/品牌仓的渐进式闭环。
- Geek+ / Hai Robotics / Quicktron / Hikrobot：国内 AMR/ACR 成熟；WarehouseLoop 做插件式异常和训练层。
- Dexory / Gather AI：数字孪生和库存扫描强；WarehouseLoop 进一步把异常变成任务、纠偏、proof 和 HIL 数据。
- WMS/WES/QMS：system of record 强；WarehouseLoop 是 system of action and evidence。

## Moat

核心护城河不是通用视觉模型，而是：

> exception-action-evidence-writeback-training graph

会积累的资产：

- SKU、库位、tote/bin、条码、RFID、照片、重量、视频和 WMS 状态。
- 退货等级、破损标签、欺诈风险、复检结果、可售/不可售去向。
- 人工接管、低置信度抓取、错误识别、安全停机和恢复策略。
- WMS/WES/ERP/RMS/RCS 连接器。
- 客户 SOP、SLA、责任分派、审计证据和 KPI benchmark。
- Qualcomm edge model profiles、deployment recipes、rollback records。
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

比赛 demo 用一个小货架、三个 SKU、一个退货箱、一个扫码器、一个相机和一台小机械臂/AMR 即可。

3 分钟故事：

1. Mock WMS 显示 SKU A 应在 A-03。
2. 现场货架故意把 SKU A 放在 B-02。
3. Qualcomm edge camera 发现库位不一致，生成异常卡。
4. 系统派单给仓员或小机械臂纠偏。
5. 扫码/拍照验证，WMS 从红色异常变绿色已修正。
6. 第二个退货箱破损，低置信度触发人工复核。
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

- 不说替代 WMS。
- 不说完全无人仓、lights-out、零错误、0 人力。
- 不说一天接入所有系统。
- 不说中国仓储机器人无人竞争。
- 不说通用机器人能处理所有 SKU、软包、破损和退货。
- 不说 Qualcomm 官方合作/认证，除非真实签约。
- 不承诺固定 ROI；只承诺试点验证指标。

## Sources

- NRF 2025 retail returns：https://nrf.com/research/2025-retail-returns-landscape
- Descartes labor shortage：https://www.descartes.com/resources/news/descartes-study-reveals-76-supply-chain-and-logistics-operations-are-experiencing
- MHI/Deloitte supply chain tech investment：https://www.mhi.org/content/2/2285545/new-mhi-and-deloitte-report-focuses-on-orchestrating-end-to-end-digital-supply-chain-solutions
- Warehouse picking economics：https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.97.pdf
- Locus AMR scale：https://locusrobotics.com/blog/seven-billion-picks-warehouse
- Brightpick RaaS / fulfillment：https://brightpick.ai/brightpick-unlocks-lights-out-fulfillment/
- GXO / Agility RaaS：https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics
- GXO / Dexterity pilot：https://gxo.com/news_article/gxo-pilots-ai-enhanced-robotics-in-warehouse/
- NDRC logistics cost：https://www.ndrc.gov.cn/fggz/202602/t20260209_1403645.html
- Logistics cost action plan：https://www.mee.gov.cn/zcwj/zyygwj/202411/t20241128_1097450.shtml
- 2025 express parcels：https://www.news.cn/fortune/20260107/c0945bd4d0094139be638cf1dfd86e21/c.html
- 2025 cross-border ecommerce：https://www.stdaily.com/web/gdxw/2026-06/23/content_535756.html
- Geek+ HKEX listing：https://www.geekplus.com/zh-cn/resources/news/geekplus-lists-on-hkex-main-board-pioneering-the-global-smart-logistics-transformation-with-robotics
- Quicktron profile：https://www.quicktron.com/zh_CN/about-us
- GLP RaaS：https://www.glp.com.cn/information/555.html
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
