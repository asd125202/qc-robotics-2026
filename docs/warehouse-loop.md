# WarehouseLoop 仓务闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

WarehouseLoop 是给 3PL、品牌仓和跨境电商仓的 AI 仓务闭环平台：

> 发现仓内异常，派单纠偏，拍照/扫码验证完成，并回写 WMS。

它不是替代 WMS，也不是再卖一套 AMR 车队。它是现场事实到系统记录之间的闭环层。

## Problem

仓库不缺系统，缺“现场事实到系统记录”的闭环。

典型问题：

- SKU 放错库位，但 WMS 还显示正常。
- 扫码漏扫、错扫、少件、多件、串货，最后变成赔付和加班。
- 退货质检在纸单、Excel、微信群和主管记忆里流转。
- 损坏包裹、错货、疑似欺诈、不可售商品没有统一证据。
- WMS、AMR、人工、相机、扫码枪之间没有统一异常闭环。

## Why Now

- 电商和跨境电商继续拉高 SKU、订单和退货复杂度。
- 2025 年美国零售退货预计 8499 亿美元，线上退货率 19.3%。
- 中国 2025 年快递业务量约 1989.5 亿件，跨境电商进出口约 2.84 万亿元。
- 仓库自动化预算增加，但 brownfield 仓库不能都重建成全自动仓。
- AMR、ACR、AS/RS、机械臂和固定相机都在部署，真正缺的是跨设备异常闭环。
- Qualcomm edge AI 让现场低延迟感知和隐私更可行，LeRobot 让失败与接管能进入训练闭环。

## Non-Obvious Insight

仓库 AI 的第一桶金不是“全自动仓库”，而是“异常闭环”。

WMS 记录的是应然状态，WarehouseLoop 捕捉和修正实然状态。每个错放、破损、漏扫、低置信度抓取、退货质检和人工接管，都应该变成可追责、可验证、可回写、可训练的数据资产。

## Solution

WarehouseLoop 从三个高痛工作流切入：

1. 收货 / 上架差异：ASN、到货、扫码、拍照、库位确认和异常索赔。
2. 库位错放 / 盘点差异：相机、扫码、RFID、重量和人工复核形成 proof。
3. 退货质检 / 可售判定：RMA、照片、条码、破损等级、可售/不可售/复检。

工作流：

- 现场设备发现异常：手机、固定相机、AMR、机械臂、扫码枪、RFID、称重台。
- LoopCore 生成 ExceptionCase。
- 系统派给仓员、主管或机器人。
- 操作员扫码/拍照/视频验证。
- WarehouseLoop 回写 WMS/WES/ERP。
- 失败、接管和低置信度动作进入 LeRobot dataset。

## Market Wedge

第一客户不是所有仓库，而是：

- 中小 3PL 和品牌仓。
- 高 SKU、高退货、高临时工比例的服饰、美妆、消费电子仓。
- 跨境电商海外仓、保税仓和退货中心。
- 已经有 WMS，但现场执行和异常闭环混乱的 brownfield 仓。

中国版重点：

- 跨境退货分级、贴标、换标、破损包裹、错货和海外仓库存纠偏。
- 与 WMS/WES/RCS、AMR/ACR 厂商、自动化 EPC 和跨境服务商合作。
- 数据本地化、私有部署、中文工单、企微/钉钉/飞书和本地运维。

海外版重点：

- 中小 3PL、DTC 品牌仓、服饰/鞋履/电子产品退货中心。
- 先卖 30-45 天单流程试点，再扩到多仓。
- 不重建仓库，不替换 WMS，先把异常闭环做成 ROI。

## Business Model

一句话收入模型：按“闭环的仓务异常流程”收费，而不是靠硬件毛利。

- 付费试点：30-45 天，单仓单流程，5k-15k 美元。
- 生产版：1.5k-5k 美元 / 仓 / 月起，按工作流、摄像头节点、闭环任务量加价。
- 企业版：25k-75k 美元 / 仓 / 年，含集成、SLA、审计报表和私有部署。
- 中国版：8-12 周试点，按工作站、摄像头节点、闭环任务量和 WMS 集成收费。
- OEM/集成商：边缘视觉/异常闭环 SDK、Qualcomm profile、LeRobot 数据导出和任务模板授权。

## Competition

现有玩家证明仓库机器人真实有市场，但它们大多没有解决跨系统异常闭环：

- Locus / 6 River / GreyOrange：AMR pick assist 强，但不负责库存真相和退货闭环。
- AutoStore / Exotec / Ocado：goods-to-person 和 AS/RS 强，部署重，仍需要上下游异常处理。
- Symbotic / Amazon Robotics：mega-DC 自动化强，但不适合大多数 brownfield 中小仓。
- Covariant / Nimble / RightHand / Plus One：机械臂能力强，但 SKU、破损、退货和异常仍需闭环。
- Geek+ / Hai Robotics / Quicktron / Cainiao：国内 AMR/ACR 竞争成熟，WarehouseLoop 应做插件式异常闭环层。
- Dexory / Gather AI：更偏 physical AI / digital twin；WarehouseLoop 更轻、更贴近“任务派发 + proof + WMS 回写”。

## Moat

护城河不是通用视觉模型，而是“异常-动作-结果”数据集：

- SKU、库位、容器、责任人、照片证据、WMS 修正、SLA、返工结果。
- 退货等级、破损标签、欺诈风险、复检结果、可售/不可售去向。
- 人工接管、低置信度抓取、错误识别和安全停机片段。
- WMS/WES/ERP/RCS 连接器、行业 SOP 模板和客户运营报表。

## Architecture

### LoopCore

云端或本地服务：

- WMS/ERP/WES/RCS 连接器。
- ExceptionCase、WarehouseTask、VerificationEvidence、ReturnAssessment。
- 任务规划、审计日志、SLA、报表、模型注册和回滚。
- CSV/API/mock WMS 起步，后续接 Oracle、Manhattan、Blue Yonder、SAP、金蝶、用友、聚水潭等。

### LoopRMF

机器人和现场资源编排：

- Open-RMF 任务队列、交通、门、充电、fleet adapter。
- 把 WarehouseTask 转成 AMR API、ROS 2 Nav2、MoveIt 2 Task Constructor 或工站动作。
- 支持混合厂商，不要求替换已有 AMR/ACR。

### LoopEdge

Qualcomm 端侧运行层：

- RB3 Gen 2 / IQ-9075 / IQ10 级别 edge device。
- 固定相机、手持扫码、RFID、称重、工位机械臂、AMR 相机。
- QNN / TFLite / ONNX Runtime、AI Hub profile、离线推理和弱网缓存。
- 本地识别条码、SKU、包装破损、错位、缺件、多件和动作失败。

## Data Objects

- `WarehouseTask`: type, priority, WMS ref, source, destination, expected items, deadline.
- `ExceptionCase`: mismatch type, confidence, owner, SLA, status, evidence refs.
- `ItemIdentity`: SKU, GTIN, SSCC, lot, serial, barcode, RFID reads.
- `VerificationEvidence`: photo/video, barcode, RFID, weight delta, vision result, pass/fail.
- `ReturnAssessment`: RMA, item, grade, defect tags, disposition, human override.
- `RobotJob`: AMR route, MoveIt stages, battery, status, recovery count.
- `DatasetEpisode`: videos, state/action, labels, outcome, privacy flags.
- `ModelRelease`: target SoC, runtime, quantization, metrics, signature, rollback id.

## Demo

比赛 demo 不需要真实仓库。一个迷你货架、几个 SKU、一个破损纸箱、一个二维码退货单即可：

1. Mock WMS 显示 SKU A 应在 A-03。
2. 固定相机或手机发现 SKU A 被放在 B-02，置信度 0.82。
3. WarehouseLoop 自动生成异常纠偏任务。
4. 操作员扫码并拍照，把 SKU 放回 A-03。
5. 系统回写 WMS，状态从 `异常` 变成 `已修正`。
6. 第二个场景演示退货破损，低置信度交给人工复核。
7. 人工接管片段导出为 LeRobot episode，生成 Qualcomm edge profile。

## Why Qualcomm

WarehouseLoop 是 Qualcomm edge AI 在工业现场的闭环应用样板：

- 仓库现场需要低延迟视觉、弱网运行、本地隐私和多摄像头边缘推理。
- AMR、固定相机站、退货工位和机械臂都需要低功耗、本地可维护的边缘计算。
- AI Hub / QNN / TFLite / ONNX Runtime 可把训练模型变成可验证 edge artifact。
- Qualcomm 不只是“跑模型”，而是让仓库异常闭环在现场可靠运行。

## Claims To Avoid

- 不说替代 WMS。
- 不说完全无人仓、lights-out warehouse 或零错误。
- 不说一天接入所有系统。
- 不说中国仓储机器人无人竞争；中国已经非常拥挤。
- 不说通用机器人已经能处理所有 SKU、软包、破损和退货。
- 不说 Qualcomm 官方合作/认证，除非真实签约。
- 不说固定 ROI；试点指标必须由现场数据验证。

## Sources

- MHI/Deloitte supply chain report：https://www.mhi.org/media/news/48246
- NRF returns 2025：https://nrf.com/research/2025-retail-returns-landscape
- U.S. Census ecommerce Q1 2026：https://www.census.gov/retail/ecommerce.html
- IFR service robots 2025：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- 国家邮政局 2026 Jan-May：https://www.mot.gov.cn/shuju/tongjishuju/youzheng/202606/t20260624_4208155.html
- 新华网 2025 快递业务：https://www.news.cn/politics/20260122/d5b9076f70cb4cc5a6f7958bc2b6f3ad/c.html
- 国家统计局 2026 Jan-May online retail：https://www.stats.gov.cn/sj/zxfb/202606/t20260616_1963949.html
- 中国跨境电商数据：https://english.www.gov.cn/news/202606/16/content_WS685033abc6d0868f4e8eeabc.html
- 物流降本增效行动方案：https://www.mee.gov.cn/zcwj/zyygwj/202411/t20241128_1097450.shtml
- Geek+ investor relations：https://ir.geekplus.com/zh-cn/investor-relations
- Hai Robotics prospectus：https://www1.hkexnews.hk/app/sehk/2026/108202/documents/sehk26021300409_c.pdf
- Quicktron：https://www.quicktron.com/zh_CN/about-us
- Locus Robotics 7B picks：https://locusrobotics.com/blog/seven-billion-picks-warehouse
- AutoStore Q1 2026：https://www.autostoresystem.com/investors
- Symbotic filings：https://www.sec.gov/Archives/edgar/data/1837240/000183724025000113/sym-20250927.htm
- Amazon robotics：https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model
- Nimble Series C：https://nimble.ai/news/nimble-closes-106-million-series-c-funding-round-at-1b-valuation-scales-fully-autonomous-fulfillment-with-fedex
- Plus One Robotics：https://www.plusonerobotics.com/
- Pickle Robot：https://www.picklerobot.com/news/series-b-press-release
- Blue Yonder Optoro：https://blueyonder.com/media/2025/blue-yonder-acquires-optoro
- Dexory：https://www.dexory.com/en-us
- Gather AI：https://gather.ai/
- Oracle WMS Cloud APIs：https://docs.oracle.com/en/cloud/saas/warehouse-management/25d/owmre/
- Open-RMF：https://www.open-rmf.org/
- ROS 2 Jazzy：https://docs.ros.org/en/jazzy/
- Nav2：https://docs.nav2.org/
- MoveIt Task Constructor：https://moveit.picknik.ai/main/doc/concepts/moveit_task_constructor/moveit_task_constructor.html
- GS1 Application Identifiers：https://www.gs1.org/standards/barcodes/application-identifiers
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
