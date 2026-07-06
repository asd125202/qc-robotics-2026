# QualityLoop 质检闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

QualityLoop 是制造业的 AI 质检闭环系统：

> 把每一次 NG 从“发现缺陷”推进到“定位根因、派发纠正动作、验证不再复发”。

它不是再做一个 AOI 算法，也不是替代 Cognex/Keyence/Hikrobot 这类视觉系统。它是检测之后的质量操作系统。

## Problem

工厂不只是漏检，而是缺陷图片、工站数据、MES/QMS、工程复盘和 CAPA 分散，导致问题反复出现。

典型痛点：

- 视觉系统发现 NG，但缺陷和工单、批次、设备、工艺参数、供应商数据没有连起来。
- 返工、报废、保修、投诉、退货、召回都是真实财务损失。
- 工程师用 Excel、微信群、截图和会议追根因，RCA 周期长。
- CAPA 派发后没有可靠验证，不知道复发率是否下降。
- 模型升级、阈值调整和质检规则没有稳定版本治理。

## Why Now

- ASQ 把 COPQ 定义为报废、返工、保修、投诉、退货、召回等失败成本；2025 年报告页面指出只有 31% 受访者完全理解质量成本对财务表现的影响。
- McKinsey 2026 年称全球汽车保修相关成本 2024 年约 580 亿美元，约占行业销售 2.2%。
- NHTSA 2025 年年度召回报告显示，美国全年 997 起召回、受影响规模 3127 万。
- Deloitte 2025 年制造业调查显示，大型制造商正在加码 smart manufacturing、vision systems、MES 和 QMS。
- Qualcomm edge AI 让多相机、本地推理、低延迟质检和敏感工厂数据不出厂更现实。
- LeRobot/HIL 让机器人复检路径、返工动作和人工接管可转成训练数据。

## Non-Obvious Insight

检测框不是产品，闭环才是产品。

真正有防御性的质量数据不是“更多缺陷图片”，而是：

> 缺陷图片 + 工站/批次/设备/人员/物料 + 根因判断 + 纠正动作 + 复发结果。

QualityLoop 的价值不止在于看见坏件，而在于让同一个坏件不再发生。

## Solution

QualityLoop 把 AI 视觉、工程复盘和质量流程接成闭环：

1. 边缘视觉检测站捕获 NG、热力图、缺陷码和置信度。
2. Issue Graph 自动聚合同类缺陷、批次、工站、设备、供应商和历史案例。
3. RCA Copilot 生成 5 Why / 鱼骨图候选，并要求工程师确认。
4. CAPA workflow 派发给工程、制程、供应商或返工站。
5. Re-inspection 验证返工后是否通过，跟踪 FPY、PPM、返工率和复发率。
6. 低置信度、人工覆判和机器人复检接管进入主动学习 / LeRobot HIL 队列。

## Market Wedge

先打“高混低量、返工昂贵、图片证据强”的产线，不讲所有制造业。

首批 beachheads：

- 电子装配 / EMS / 3C：连接器、摄像头模组、FPC/PCB/SMT、显示外观。
- EV battery：极片、电芯、焊接、模组/PACK、追溯和供应商质量。
- Automotive Tier 1：焊接、压铸、涂装、EOL、扭矩/装配验证。
- NPI / 试产线：新缺陷多、模型漂移快、工程复盘密集。

中国版：

- 定位为质检闭环、质量追溯、根因分析、CAPA 协同。
- 默认 on-prem / private cloud / edge inference。
- 连接既有 Hikrobot、OPT、Luster、Aqrose、SmartMore、Jutze、Keyence、Cognex、Omron、Basler 等检测资产。
- 买方是质量总监、制造工程、自动化/IE、数字化工厂、MES/QMS owner、厂长。

海外版：

- 面向 automotive、electronics/EMS、industrial equipment、battery 和高价值 NPI。
- 不替换 QMS/MES，也不替换相机系统；做缺陷证据湖、RCA/CAPA 和 edge model governance。

## Business Model

一句话收入模型：按“闭环的质量问题族”和检测站收费，而不是按模型调用收费。

- 付费 pilot：6-8 周，单线单缺陷族，15k-50k 美元。
- 生产版：每个检测站 1k-3k 美元/月 + 实施费。
- 工厂版：100k-300k 美元/厂/年，含 MES/QMS 集成、审计包、模型治理和私有部署。
- 成功费：对 scrap/rework/warranty 节省可选按验证金额分成。
- 中国版：按工站、产线、缺陷族、接口和私有化部署计费。

## Go-To-Market

先卖给有明确质量损失、已有相机/AOI、且愿意把 RCA/CAPA 数字化的工厂。

- 第一买方：质量总监、制造工程负责人、厂长、数字化工厂负责人。
- 第一场景：一条线、一个高频缺陷族、一个 NG 到 CAPA 的闭环。
- 试点承诺：6-8 周内证明 RCA 周期缩短、CAPA 关闭证据变完整、复发率可追踪。
- 扩张路径：单缺陷族 -> 多缺陷族 -> 多检测站 -> 工厂模板 -> 集团供应商质量模板。
- 渠道伙伴：MES/QMS 实施商、机器视觉集成商、自动化集成商、Qualcomm 生态硬件伙伴。
- 中国版切入：3C/EMS、动力电池、汽车零部件、深圳/长三角/珠三角智能制造示范线。
- 海外版切入：electronics NPI、automotive Tier 1、industrial equipment、battery pilot lines。

## Competition

- Cognex / Keyence / Omron / Hikrobot：强在机器视觉硬件、相机、光源、控制器和检测算法。
- Landing AI / Robovision / Elementary：强在模型训练和视觉平台。
- Instrumental：强在复杂电子 NPI 和质量洞察。
- Siemens / Zebra / Basler / MVTec：强在工业平台和视觉工具链。
- Luster / Aqrose / SmartMore / Jutze：国内检测和 AOI 生态强。
- QMS/MES：强在记录和流程，但不一定拥有图像、模型、工站上下文和 re-inspection 数据。

QualityLoop 的位置：

> 检测之后的质量操作系统：把多厂商检测结果、MES/QMS/SPC、RCA、CAPA、复检和模型治理连成一条闭环。

## Moat

- 缺陷本体：跨产品、产线、设备和供应商统一缺陷 taxonomy。
- 闭环数据：缺陷 -> 根因 -> CAPA -> 复检 -> 复发结果。
- 工站上下文：批次、设备、工艺参数、人员、供应商和检验计划。
- 集成壁垒：MES/QMS/PLC/SPC/OPC UA Vision/SAP/Odoo/本地系统 adapter。
- 模型治理：station recipe、阈值、模型版本、回滚、主动学习和审计。
- 客户工作流嵌入：质量例会、CAPA 审核、供应商反馈和 NPI ramp 模板。

## Architecture

### QualityCore

- DefectObservation、QualityEvent、CAPA、ModelRelease、TraceEvent。
- MES/QMS/SPC/ERP/PLC adapter。
- Issue Graph、RCA Copilot、CAPA workflow、审计包、模型注册和回滚。

### EdgeVision Station

- Qualcomm IM SDK / GStreamer 摄像头、ISP、视频和 AI pipeline。
- QNN / ONNX Runtime QNN EP / TFLite 推理。
- GenICam 工业相机、光源 recipe、trigger、strobe、曝光和 overtrigger 检查。
- OPC UA Vision 输出 station state、inspection result、measurement、robot guidance。

### Robot Re-Inspection

- ROS 2 + MoveIt 2 规划复检路径和多角度拍摄。
- 安全由机器人控制器、安全 PLC、光栅、急停和站内互锁负责。
- LeRobot HIL 记录人工接管、复检动作和失败恢复。

### Learning Loop

- 低置信度、人工覆判、新缺陷和复发问题进入 active learning queue。
- CVAT / Label Studio 标注。
- 云端或私有云训练，AI Hub 编译 profile，再灰度到 edge station。
- station recipe、taxonomy、threshold 和 model artifact 一起版本化。

## Data Objects

- `ProductUnit`: serial, lot, SKU, routing step, work order.
- `InspectionPlan`: characteristics, tolerances, required views, sampling rule.
- `StationRecipe`: camera params, lighting params, robot poses, model version, thresholds.
- `CaptureEvent`: timestamp, pose ID, trigger source, exposure, gain, image hash.
- `InferenceResult`: model version, runtime, latency, boxes/masks/anomaly score.
- `DefectObservation`: taxonomy code, location, severity, confidence, disposition.
- `QualityEvent`: nonconformance, CAPA link, owner, status, root cause.
- `TraceEvent`: unit, activity, station, operator, artifact, timestamp.
- `ModelRelease`: training data hash, metrics, QNN/ONNX artifact, rollback pointer.

## Demo

比赛 demo 应该让“检测框之后的价值”可见：

1. MES mock 下发工单和 inspection plan。
2. 操作员扫码零件，加载 station recipe。
3. 相机/机器人拍摄 3 个角度，Qualcomm edge 本地识别表面划伤。
4. UI 展示热力图、缺陷码、置信度和历史相似案例。
5. QualityLoop 生成 nonconformance 和 CAPA 任务。
6. 操作员执行 mock rework，复检通过。
7. 系统回写 MES/QMS，并把低置信度样本加入 active learning / LeRobot HIL。
8. 对比竞品视角：别人停在 bbox，QualityLoop 继续走到 RCA、CAPA、复发验证。

## Why Qualcomm

QualityLoop 是 Qualcomm 工业边缘 AI 的参考应用：

- 工厂不想把所有缺陷图、产品图纸和工艺数据上传公有云。
- 产线质检需要低延迟、多相机、光源同步、弱网可用和本地可维护。
- Qualcomm IM SDK、AI Hub、QNN、ONNX Runtime QNN EP 可以把模型落到 edge station。
- Dragonwing / RB / IQ 设备可以成为 AI 质检站、机器人复检站和现场质量网关。
- LeRobot + Qualcomm edge 让机器人复检路径和人工接管变成可迭代技能。

## Claims To Avoid

- 不说零缺陷、零漏检、100% 准确率。
- 不说替代所有质检员。
- 不说任意产线几天内上线。
- 不说自动找到真实根因；只能说提出候选根因并让工程师确认。
- 不说无需 MES/QMS/现场数据。
- 不说替代 Cognex/Keyence/Hikrobot；定位为集成和闭环层。
- 不说 Qualcomm 官方合作/认证，除非真实签约。
- 不说医疗、汽车、半导体合规已满足，除非逐项验证。

## Ask

比赛阶段最需要 Qualcomm 支持三件事：

1. 开发板和 edge AI profile：用于多相机质检、QNN/ONNX artifact、延迟和功耗证据。
2. 工业伙伴连接：找 1-2 个制造业 demo 数据或试点工位，验证 NG -> RCA/CAPA -> 复检闭环。
3. 生态联合展示：把 QualityLoop 作为 Qualcomm edge AI + LeRobot HIL 的工业参考应用。

## Sources

- ASQ Cost of Quality：https://asq.org/quality-resources/cost-of-quality
- McKinsey warranty AI：https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/when-warranty-costs-rival-r-and-d-spend-remaking-vehicle-quality-with-ai
- NHTSA 2025 recalls：https://www.nhtsa.gov/sites/nhtsa.gov/files/2026-03/2025-annual-recalls-report.pdf
- Deloitte smart manufacturing 2025：https://www.deloitte.com/us/en/insights/industry/manufacturing/2025-smart-manufacturing-survey.html
- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- MarketsandMarkets machine vision：https://www.marketsandmarkets.com/Market-Reports/industrial-machine-vision-market-234246734.html
- Knowledge Sourcing AI quality inspection：https://www.knowledge-sourcing.com/report/ai-quality-inspection-market
- 工信部智能制造指导：https://gxt.fujian.gov.cn/jdhy/zxzcfg/gjzcfg/202506/t20250611_6923864.htm
- 深圳 AI+制造计划（新华网转载）：https://www.news.cn/sci-tech/20260302/c9d0eb0e334345919c4d905c94c2cb53/c.html
- CMVU machine vision report summary：https://www.lusterinc.com/%E6%9C%80%E6%96%B0%E5%8F%91%E5%B8%83-%E3%80%8A2024%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89%E5%B8%82%E5%9C%BA%E6%8A%A5%E5%91%8A%E3%80%8B%E8%A7%A3%E8%AF%BB/
- Hikrobot lithium vision：https://www.hikrobotics.com/cn/machinevision/application/list/?id=10
- Aqrose：https://cn.aqrose.com/
- OPT annual report：https://www.optmv.com/Upload/File/202604/b1017ba56d8544ec91339d3714aed6e2.pdf
- Cognex Q1 2026：https://www.prnewswire.com/news-releases/cognex-reports-first-quarter-2026-results-302764643.html
- Keyence VS-G：https://www.keyence.com/products/vision/vision-sys/vs-g/
- Instrumental：https://instrumental.com/
- Elementary：https://www.elementaryml.com/
- Siemens Visual Inspection Cockpit：https://docs.industrial-operations-x.siemens.cloud/r/en-us/1.1.0/visual-inspection-cockpit-and-engineering-tool/introduction/about-visual-inspection-cockpit-and-engineering-tool
- Qualcomm IM SDK：https://www.qualcomm.com/developer/software/qualcomm-intelligent-multimedia-sdk
- Qualcomm AI Hub compile：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- GenICam SFNC：https://www.emva.org/wp-content/uploads/GenICam_SFNC_v2_7.pdf
- OPC UA Vision：https://opcfoundation.org/markets-collaboration/machine-vision/
- ISA-95：https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard
- MVTec AD：https://www.mvtec.com/research-teaching/datasets/mvtec-ad
- Label Studio active learning：https://docs.humansignal.com/guide/active_learning
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
