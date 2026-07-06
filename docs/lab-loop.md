# LabLoop 实验室闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

LabLoop 是面向生命科学、临床检验、药企 QC、CRO/CDMO 和核心实验平台的实验室闭环操作层：

> 把样本、协议、仪器、机器人、原始数据、QC 异常、报告和下一轮实验建议连成可执行、可审计、可学习的闭环。

它不替换 LIMS/ELN，也不卖单个机器人。它做的是 existing lab 之上的 system of action and provenance。

## Problem

实验室已经买了 LIMS、ELN、仪器、排程系统、机器人和 QMS，但实验闭环仍然断裂。

典型痛点：

- 协议意图、样本 lineage、仪器参数、原始文件、分析脚本和结论分散在不同系统。
- 样本错放、漏扫、标签错误、耗材不足、仪器未就绪和操作偏差经常靠人工发现。
- LIMS/ELN 记录 what happened，但不实时知道 bench 上正在发生什么。
- QMS 往往事后处理 deviation，无法在执行中阻断错误并自动附上证据。
- AI 模型缺少可学习的实验数据：目的、动作、状态、结果、异常和人类纠错没有连起来。

## Why Now

- 全球 lab automation、lab robotics、LIMS/ELN 都在增长，但自动化仍高度碎片化。
- Biopharma R&D 成本高、回报压力大，企业需要实验 throughput、可复现性和审计证据，而不是展示型机器人。
- 临床实验室人员紧缺，ASCP 2025 年发布的 2024 vacancy survey 仍显示多类岗位 vacancy 高于疫情前。
- 样本链路错误是真实痛点：大量研究反复指出 pre-analytical errors 是实验室错误的重要来源。
- 中国药监、临床检验质控、医疗数据本地化、科学仪器国产化和 CRO/CDMO 国际化都在推高可追溯数据需求。
- SiLA、OPC UA LADS、Allotrope、AnIML 等标准让仪器互联比过去更可行。
- Qualcomm edge AI 和 LeRobot HIL 让本地视觉核验、机器人执行、人工纠错和云训练回流成为可演示产品。

## Non-Obvious Insight

下一代实验室软件公司不会只是另一个 system of record。

它会成为 system of action and provenance：

> 知道科学家想做什么，仪器实际做了什么，样本/耗材/机器人状态发生了什么，数据是否有效，以及下一步应该做什么。

实验室数据的最小可学习单元不是 raw file，而是：

> protocol intent + sample identity + physical action + instrument run + QC outcome + deviation/correction + next action。

## Solution

LabLoop 由四层组成：

1. LabLoop Bridge：连接 LIMS/ELN/QMS、仪器、机器人、相机、条码/RFID、文件夹和人工确认。
2. Workcell Runtime：在 Qualcomm edge 上核验样本、耗材、rack、plate、instrument readiness 和 robot action。
3. Experiment Graph：建立 protocol-sample-instrument-result-deviation-next action 的可审计图谱。
4. Learning Loop：把人工纠正、机器人失败、低置信度核验和成功 run 转成 LeRobot HIL 数据。

## Product Workflow

1. LIMS 创建 work order：sample IDs、plate map、protocol version、instrument method、acceptance criteria。
2. 操作员加载样本 rack、试剂和耗材；RFID 读 rack/tray，barcode 扫 sample/plate/reagent，camera 验证摆放。
3. Edge reconciles expected vs observed；如果不一致，阻断任务并生成 QMS deviation candidate。
4. Bench robot 执行安全动作：移液 mock liquid、开盖/合盖 mock tube、移动 carrier 或读 plate。
5. 相机验证 postcondition：well occupancy、tube presence、rack slot、label visibility、spill/anomaly。
6. AMR 或人工把 sealed carrier 送到 instrument station，instrument adapter 返回 raw file 和 structured result。
7. 系统把结果写回 ELN/LIMS；如果 QC 异常则更新 QMS deviation，并附带原始证据。
8. 人工纠正一次机器人或核验失败，LabLoop 记录为 LeRobot HIL episode。

## Market Wedge

先打已有仪器和系统、但缺 live execution loop 的实验室。

首批 beachheads：

- Biopharma QC / CMC：方法、样本、仪器、原始数据、QA 和审计压力强。
- CRO/CDMO assay / process development：项目交付、客户审计、样本流转和可复现性直接影响收入。
- 医院临床检验：样本拒收、IQC、EQA、报告互认和 LIS/LIMS 质量证据。
- 大学/科研核心平台：仪器预约、样本流转、平台服务、数据归档和使用计费。
- 检验检测 / CNAS/CMA：样本 chain-of-custody、报告防篡改、设备校准和 false-report 风险。
- AI-first biotech / materials labs：模型需要 lab-grade closed-loop data。

## Business Model

一句话收入模型：按实验流程、workcell、仪器连接和合规验证包收费。

- 付费试点：中国 20-50 万元；海外 50k-150k 美元，8 周闭环一个高频流程。
- 站点授权：中国企业/医院/药企 100-300 万元/站点/年；海外 150k-500k 美元/站点/年。
- Connector packs：LIMS/ELN/QMS、instrument class、SiLA/LADS、file watcher、barcode/RFID、robot adapter。
- Edge kit：Qualcomm workcell gateway、camera、barcode/RFID、local evidence store 和部署服务。
- Validation pack：GxP/CSV/CSA、审计 trail、访问控制、变更控制、model release evidence。

## Go-To-Market

先承诺“不替换 LIMS/ELN，不改仪器，8 周把一个高频实验流程变成 AI-ready 闭环”。

- 中国切入：药企 QC/CMC、CRO/CDMO、医院临床检验、检验检测机构和高校核心平台。
- 海外切入：AI-first biotech、high-throughput assay、formulation、analytical development 和 core facilities。
- 第一试点：一个样本链路、一个仪器类别、一个机器人/人工动作、一个 QMS/QC 输出。
- 扩张路径：流程 -> 仪器类别 -> workcell -> 实验室站点 -> 多站点数据/模型治理。
- 渠道伙伴：仪器厂商、自动化集成商、LIMS/ELN 实施商、CRO/CDMO、Qualcomm 生态硬件伙伴。

## Competition

- Benchling / Dotmatics / LabWare / Thermo SampleManager：system of record 强，但不主要管理实时 bench action。
- TetraScience / Scitara / ZONTAL：科学数据云和标准化强，但更像 data pipe，不闭环执行任务。
- Opentrons / Automata / Biosero / Hamilton / Beckman：workcell 自动化强，但通常是 station island。
- Emerald Cloud Lab / Strateos：云实验室闭环强，但更多是外包/自有设施，不升级客户现有实验室。
- Roche / Abbott / Siemens / Mindray clinical automation：临床流水线强，但 LabLoop 更通用、跨系统、跨科研/QC/平台场景。
- Veeva / MasterControl / TrackWise：QMS 强，但 LabLoop 能从执行异常自动生成 deviation 和证据。

LabLoop 的位置：

> Vendor-neutral lab operations loop：把 request/protocol、sample/material readiness、schedule、human/robot/instrument execution、data capture、QC/QMS exception、report/next action 连成一条实时闭环。

## Moat

- Connector library：国内外 LIMS/ELN/QMS、仪器、机器人、条码/RFID、文件格式和 API adapter。
- Instrument semantic layer：method、sample、run、raw file、QC flag、deviation 和 report 的统一对象模型。
- Protocol-action-result graph：目的、动作、状态、结果和纠正行为组成可学习数据。
- Audit/compliance workflows：data integrity、audit trail、电子签名、CSV/CSA、变更控制和 model release evidence。
- Edge deployment in regulated labs：本地运行、数据本地化、弱网可用、视觉核验和安全门控。
- Workflow-specific AI agents：每个流程的 QC、异常、next action 和 HIL 数据越来越强。

## Architecture

### Edge Workcell Gateway

- Qualcomm RB3 Gen 2 / RB6 作为 workcell edge。
- 接入 camera、barcode、RFID、balance/temperature/door state、bench robot、AMR、instrument adapter。
- 本地完成 identity check、rack pose、label visibility、cap state、plate/well state、spill/anomaly 和 fail-closed gating。

### LabLoop Cloud

- Workflow authoring、LIMS/ELN/QMS connectors、fleet scheduling、analytics、LeRobot datasets、GPU training、model registry 和 deployment approval。
- 中国版默认本地/私有云，医疗和 HGR 相关数据留在中国合规数据平面。

### Instrument Layer

- 优先 SiLA 2、OPC UA LADS、Allotrope、AnIML。
- 现实中支持 CSV/PDF watcher、instrument folder、serial/API、RPA、vendor SDK 和人工确认。

### Learning Loop

- LeRobot 只用于受控技能：rack alignment、sample carrier handoff、mock pipetting、tube handling、instrument loading。
- 人工接管、核验失败和成功 run 进入 LeRobotDataset。
- AI Hub profile 后把 vision / anomaly / robot policy 灰度回 edge workcell。

## Data Objects

- `WorkOrder`: LIMS request、protocol、sample set、plate map、acceptance criteria。
- `PhysicalAsset`: sample、rack、tray、plate、reagent、tip box、barcode/RFID、lot、expiry、location。
- `Observation`: camera detection、barcode scan、RFID read、weight、temperature、door state。
- `TaskPlan`: robot/instrument/AMR steps、preconditions、postconditions、approval gates。
- `ActionEvent`: robot command、start/end、controller、result、error code、human override。
- `InstrumentRun`: method version、device ID、raw data URI、parsed result、QC flags。
- `TraceEvent`: what、where、when、why、disposition、chain-of-custody。
- `DeviationEvent`: mismatch、failed verification、blocked step、operator disposition。
- `TrainingEpisode`: LeRobot episode、videos、state/action tensors、intervention spans、outcome label。
- `ModelRelease`: dataset hash、training config、eval metrics、AI Hub/QAIRT artifact、approval status。

## Demo

比赛 demo 应该展示实验闭环，而不是只展示机械臂移动：

1. LIMS mock 创建一个 plate reader / qPCR / ELISA-style work order。
2. 操作员摆放 sample rack、mock reagent、tip box 和 plate。
3. Qualcomm edge camera + barcode/RFID 核验 expected vs observed。
4. 故意放错一个 tube 或缺一个 reagent，系统阻断任务并生成 deviation candidate。
5. 操作员纠正后，bench robot 执行 mock pipetting / tube transfer。
6. 相机验证 plate/well postcondition，mock instrument 返回 result 和 raw file。
7. 系统写回 ELN/LIMS，生成 QC evidence 和 audit trail。
8. 人工接管一次机器人对位，LabLoop 保存 LeRobot HIL episode 并显示下一轮训练队列。

## Why Qualcomm

LabLoop 是 Qualcomm 在 regulated physical AI 场景里的高价值样板：

- 实验室需要本地视觉、低延迟核验、设备网关、机器人控制和安全门控。
- 医疗、药企和 HGR 相关数据不能默认上公有云；edge inference 和本地缓存很关键。
- Qualcomm RB3/RB6、IM SDK、AI Hub、QNN/QAIRT、ONNX Runtime QNN EP 可支持 workcell vision、anomaly detection、机器人状态监控和 model release evidence。
- Edge Impulse/Arduino/developer ecosystem 能降低仪器/传感器/edge model 开发门槛。
- LeRobot HIL 让人工纠错和机器人动作变成可持续训练数据。

## Claims To Avoid

- 不说已经满足 GxP、21 CFR Part 11、CNAS/CMA、NMPA 或 QMS 合规，除非逐项验证。
- 不说完全自主科学发现。
- 不说能接入所有仪器、所有 robot、所有 LIMS/ELN。
- 不说 AI 可以绕过 E-stop、门禁、biosafety、hazard 和人类审批。
- 不说 dev kit 默认具备生产安全和网络安全配置。
- 不说机器人能处理真实生物危害、挥发性化学品、尖锐物、加热/高压设备，demo 只用安全 mock sample。

## Ask

比赛阶段最需要 Qualcomm 支持三件事：

1. RB3/RB6 edge hardware + AI Hub profile：用于 lab workcell vision、identity check、anomaly detection 和本地推理。
2. 3 个仪器/机器人 OEM 或集成商连接：优先 sample tracking、plate reader/qPCR、liquid handling、AMR。
3. 3 个样板实验室：药企 QC/CRO/CDMO、医院检验或高校核心平台，验证 8 周 closed-loop workflow。

## Sources

- Grand View lab automation market：https://www.grandviewresearch.com/industry-analysis/lab-automation-market
- Fortune lab robotics market：https://www.fortunebusinessinsights.com/laboratory-robotics-market-117407
- Deloitte pharma R&D productivity：https://www.deloitte.com/us/en/industries/life-sciences-health-care/perspectives/navigating-the-glp-boom.html
- ASCP vacancy survey summary：https://www.aabb.org/news-resources/news/article/2025/10/08/ascp-publishes-results-of-2024-vacancy-survey
- ASCP AI adoption barriers：https://criticalvalues.org/news/all/2026/01/27/ascp-2024-vacancy-survey-report-highlights-policy-priorities-to-address-laboratory-workforce-shortages-through-credentialing--advocacy--and-education-expansion
- Scientific Reports pre-analytical errors：https://www.nature.com/articles/s41598-026-38458-y
- Clinical Chemistry pre-analytical errors：https://profiles.wustl.edu/en/publications/pre-analytical-phase-errors-constitute-the-vast-majority-of-error/
- FDA CSA guidance：https://www.fda.gov/regulatory-information/search-fda-guidance-documents/computer-software-assurance-production-and-quality-management-system-software
- FDA Part 11 guidance：https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application
- NMPA reform policy：https://english.nmpa.gov.cn/2025-03/25/c_1080969.htm
- NHC 2025 medical quality goals：https://www.nhc.gov.cn/wjw/c100378/202503/62073c6fc3064f7f9d971f0b1b9c7dd5/files/1743410147292_68704.pdf
- China drug record/data rules：https://www.ccfdie.org/cn/yjxx/yphzp/webinfo/2020/07/1592159028811276.htm
- WuXi 2025 results：https://www.wuxiapptec.com/news/wuxi-news/ukp6jpdhyncifp8ovk4kv1z6
- SiLA standards：https://sila-standard.com/standards/
- OPC UA LADS：https://reference.opcfoundation.org/specs/OPC-30500-1/full
- Allotrope：https://www.allotrope.org/product-overview
- Opentrons Python API：https://docs.opentrons.com/python-api/
- Open-RMF：https://openrmf.readthedocs.io/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
