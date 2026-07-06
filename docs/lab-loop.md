# LabLoop 实验室闭环 Pitch

更新时间：2026-07-06。

## One-Line

LabLoop 是合规样本流转的物理 AI 操作层：

> 让制药、生物技术和诊断实验室，把人工样本处理变成 24/7 可追踪机器人流水线，而不需要重建整个实验室。

更短版本：

> 实验室缺的不是记录系统，是让真实 bench 动作闭环的操作层。

## Problem

实验室不是缺软件，而是缺 loop。

- LIMS 知道样本编号，ELN 知道实验结论，但没人实时知道 bench 上到底发生了什么。
- 科学家和检验人员仍在 SOP、Excel、仪器文件、邮件、手工判断和 QMS 偏差之间搬运上下文。
- 采集、运输、扫码、分拣、开盖、移液、冷藏和交接是 pre-analytical 错误高发环节。
- plate reader、qPCR、液体工作站、冷库、AMR 和文件夹只知道自己的状态。
- deviation 常在错误发生后再追溯，raw evidence、图像、轨迹和人类处置很难拼齐。
- 机械臂能移动样本，但没有协议意图、样本 lineage、QC 结果和 HIL 纠错就无法学习。

## Why Now

AI 能设计实验，湿实验执行却成了瓶颈。

全球版时机：

- Grand View 估算全球 lab automation 市场从 2025 年约 90.5 亿美元增长到 2033 年 183.9 亿美元。
- MarketsandMarkets 估算全球实验室软件 2025 年 63.1 亿美元，2030 年 101.2 亿美元。
- 自动样本存储/取回市场也在高增，驱动因素包括 biobank、pharma R&D、clinical diagnostics、LIMS 集成和样本完整性。
- NIH 等机构正在推动自动化实验、可复现性、metadata 和数字工作流捕获，让实验闭环从研究方向变成基础设施机会。
- ASCP 2024 vacancy survey 显示美国医学实验室岗位空缺仍高于疫情前，很多岗位招聘要 3-12 个月。
- 研究反复指出 pre-analytical errors 是实验室错误的重要来源。
- Deloitte 2025 biopharma QC 调研显示，40% QC labs 仍是 disconnected systems + limited automation；已经做 lab transformation 的受访者报告更少 errors/deviations、更好 compliance 和更短 testing timelines。

中国版时机：

- 《医药工业数智化转型实施方案（2025-2030年）》明确要求研发推广智能制药设备、检测仪器、制药工业软件，打造典型场景和数智药械工厂。
- 同一方案点名“药品质检（QC）实验室管理”：部署自动化仪器、液体工作站、机器人、LIMS，实现检验分析、结果判定、试剂耗材及样品管理自动化，并研究 CSV 指南。
- 生态环境监测机构评审补充要求自 2026 年 1 月 1 日施行，要求信息管理系统覆盖合同、采样、流转、前处理、分析测试、结果计算、审核、签发等流程；仪器数据优先直接采集，修改需确认批准并留痕。
- 临床检验 2025 版质控指标把标本类型/容器/采集量错误率、标本拒收率、室内质控覆盖率、检验总周转时间、报告不正确率、危急值通报率等自动化 KPI 写清楚。
- 北京、深圳、上海具身智能政策都在开放医疗健康、真实场景测试、中试平台和机器人产业支持。

## Core Insight

最快的实验室不是机器人最多，而是反馈回路最短。

真正的瓶颈不是能不能自动移液，而是：

> 每个样本、参数、仪器状态、文件、观察结果和人工纠正，能不能自动变成下一轮实验或 QC 决策的输入。

实验室数据的最小可学习单元不是 raw file，而是：

> protocol intent + sample identity + physical action + instrument run + QC outcome + deviation/correction + next action。

## Solution

LabLoop 是现有实验室之上的物理 AI 执行层。

它不替换 LIMS/ELN/QMS，也不卖孤立机械臂；它把样本、协议、仪器、机器人、相机、条码/RFID、原始文件和人工审批连接成 live execution + observation + learning loop。

1. `Worklist Bridge`：导入 LIMS worklist、ELN protocol、QMS rule 和 instrument method。
2. `Edge Lab Cell`：Qualcomm edge 本地核验 barcode/OCR、tube、cap、well、liquid level 和 anomaly。
3. `Evidence Graph`：Sample、Container、Aliquot、ProtocolVersion、RobotRun、InstrumentReading、QCDecision、HILIntervention、ModelRelease。
4. `Fail-Closed Gates`：发现 swapped tube、低液量、错孔位或手进入区域时阻断动作并请求 human-in-the-loop。
5. `Learning Loop`：HIL 纠错进入区域训练云，经 AI Hub profile 后等待 QA 审批和灰度。
6. `System Writeback`：LIMS/ELN/QMS 接收 run status、QC result、exception notes、signatures 和 evidence packet。

## Product Workflow

第一版只闭环一个高频样本流程，不重建整座实验室：

1. 导入 LIMS worklist、样本 ID、plate map、protocol version 和 acceptance criteria。
2. 操作员加载样本 rack、试剂、tip box 和 plate。
3. Qualcomm edge camera + barcode/RFID + 传感器核验 expected vs observed。
4. 系统发现 swapped tube、低液量、错孔位、未关盖或手进入 robot zone 时阻断任务。
5. 操作员纠正或 teleoperate rescue，LabLoop 记录 LeRobot HIL episode。
6. robot 执行 mock pipetting / tube transfer / plate move / instrument loading。
7. mock instrument 返回 result 和 raw file，系统绑定 metadata。
8. 结果、QC flag、exception note、签名和 evidence packet 写回 LIMS/ELN/QMS。

## Market Wedge

先打有监管压力、有系统基础、但缺 live execution loop 的实验室。

中国优先顺序：

1. 药企 / 生物药 / CDMO 的 QC 实验室。卖点是 GxP、CSV、数据完整性、LIMS/QMS 集成和放行检验提效。
2. 第三方医学检验 ICL、区域检验中心、医院检验科非标流程。避开成熟 TLA 主线，切样本分拣、复检调度、异常样本闭环和报告审核辅助。
3. 生态环境、食品、疾控等检验检测实验室。2026 新规让信息管理系统、防篡改、全流程追溯从可选变刚需。
4. 高校/科研院所/园区中试平台。适合比赛 demo 和政策项目落地。

海外优先顺序：

1. Biopharma QC / CMC。
2. CRO/CDMO assay / process development。
3. Clinical diagnostics 的 sample handling 和 chain-of-custody。
4. AI-first biotech / materials lab 的 plate-based assay optimization。
5. Core facilities。

## Business Model

LabLoop 是 workflow infrastructure，不是诊断产品。定价锚点是减少人工核对、降低样本链路异常、缩短 audit retrieval、提升 throughput 和形成 AI-ready data。

中国：

- Paid pilot：5-18 万元，8-12 周，1 个 central lab、1 个样本类、1 个 LIMS/LIS/QMS 集成。
- Department SaaS：6k-20k 元/月，另加每个 shipment / custody event 的超额费用。
- Network SaaS：3-12 万元/月 + 10-50 万元实施费。
- Regulated/private deployment：8-30 万元/月 + 15-80 万元 setup，面向数据本地化、验证包和自定义集成。

海外：

- Paid pilot：8k-35k 美元，8-12 周。
- Team SaaS：1k-4k 美元/月。
- Network SaaS：6k-25k 美元/月 + 25k-100k 美元实施费。
- Enterprise regulated：30k-120k 美元/月 + 75k-300k 美元 setup。

Pilot KPI：

- in-scope volume 的 LabLoop 建单率 >90%。
- digital custody completeness >95%。
- pickup / transfer / delivery timestamp completeness >95%。
- late / missing / custody exceptions 下降 10-30%。
- manual dispatch / reconciliation hours 下降 20-40%。
- audit packet retrieval time <5 分钟。
- 温控日志完整率 >95%，如果纳入 scope。

## Go-To-Market

不卖“大平台”，先让一个流程从 protocol 到 clean dataset。

- 第一试点：一个样本链路、一个仪器类别、一个 robot/manual action、一个 QC/QMS 输出。
- 3 个 design partners：药企 QC/CRO/CDMO、医学检验/ICL、检验检测/核心平台各一个。
- 交付方式：创始团队进入实验室做 concierge onboarding，把手工支持产品化成 adapter、protocol template 和 validation playbook。
- 扩张路径：样本流转 -> plate workflow -> workcell -> 实验室站点 -> 多站点模型治理。
- 渠道伙伴：LIMS/ELN 实施商、自动化集成商、仪器厂商、CRO/CDMO、Qualcomm 生态硬件伙伴。

## Competition

| 层级 | 代表玩家 | 强项 | LabLoop 切口 |
|---|---|---|---|
| LIMS/ELN | Benchling, LabWare, Thermo SampleManager, Dotmatics | system of record | LabLoop 管实时 bench action、核验和证据包 |
| 科学数据云 | TetraScience, Scitara, ZONTAL | 数据标准化、AI-ready data | LabLoop 把数据连接到任务、样本、机器人和 QMS |
| 自动化调度 | Automata, Biosero, Green Button Go | workcell 自动化和调度 | LabLoop 做跨 manual、robot 和 outsourced steps 的证据层 |
| 机器人/仪器 | Opentrons, Hamilton, Beckman, Tecan, Roche, Abbott, Mindray | 液体处理、临床流水线、仪器渠道 | LabLoop 管 sample lineage、QC provenance 和 HIL 数据 |
| 云实验室 | Emerald Cloud Lab, Strateos | 远程闭环自动实验室 | LabLoop 升级客户自己的物理实验室 |
| 国内玩家 | 镁伽科技、华大智造、晶泰、英矽智能、迈瑞、安图 | 智慧实验室、DBTL、自建闭环、IVD 自动化 | LabLoop 做轻量合规闭环和 Qualcomm edge 样板 |

## Moat

- Adapter library：LIMS/ELN/QMS、仪器、机器人、条码/RFID、文件格式、SiLA、OPC UA LADS。
- Semantic layer：Sample、Container、Aliquot、ProtocolVersion、InstrumentReading、QCDecision。
- Execution graph：protocol intent、physical action、instrument run、raw file、deviation 和 next action。
- Compliance flow：ALCOA+、audit trail、电子签名、CSV/CSA、变更控制和 release evidence。
- Edge footprint：本地运行、数据本地化、弱网可用、视觉核验和 fail-closed safety gate。
- HIL dataset：机器人救援轨迹、人工处置、核验失败和成功 run 组成可训练 episode。

## Architecture

### LabLoop Control Plane

- LIMS / ELN / QMS connectors。
- Protocol lock、worklist、review、signatures、RBAC、tenant policy。
- REST、FHIR、vendor APIs。

### Regional Event + Evidence Store

- Append-only logs、hashes、raw-data policy、chain-of-custody。
- Region-pinned storage，pseudonymized sample IDs at the edge。
- No patient linkage outside LIMS unless explicitly required and approved。

### Edge Lab Cell on Qualcomm

- Qualcomm RB3/RB6/IQ or Dragonwing QCS6490-class device。
- QNN / ONNX Runtime / QAIRT models。
- barcode/OCR、tube presence、cap state、well occupancy、liquid-level estimate、anomaly detection。
- Signed model/runtime manifest。

### Robots + Instruments

- robot arm、pipette、scanner、balance、plate reader。
- SiLA 2、OPC UA LADS、serial、vendor SDK、CSV/PDF watcher。

### Regional Training Plane

- LeRobot datasets、validation、model registry、QA approval。
- AI Hub compile/profile。
- Deployment scope、rollback model、signed release packet。

## Demo

比赛 demo：12 个条码 mock 样本，从 LIMS 工单走到 inspection-ready evidence。

1. LIMS mock 创建 worklist，ELN mock 锁定 protocol。
2. 操作员摆放 12 个 mock sample、reagent、tip box 和 plate。
3. Qualcomm edge camera 检测 barcode/OCR、tube presence、cap state、well occupancy 和液量。
4. 故意注入 fault：swapped tube、unreadable barcode、low volume、wrong well 或手进入 robot zone。
5. LabLoop pauses，记录 exception，请求 HIL correction。
6. 操作者 teleoperate 纠正；rescue trajectory 保存为 LeRobot/HIL 训练数据。
7. robot 执行 sample transfer / mock pipetting / plate move。
8. mock instrument 返回 QC result，LIMS/ELN/QMS 接收 run status、exception notes、signatures 和 evidence packet。

## Safety / Data / Regulatory

- Physical safety independent of AI：guarded cell、E-stops、light curtain/scanner、speed/force limits、zone states、manual loading lockout、hardware interlocks。
- AI 不能 override E-stop、门禁、biosafety、hazard controls 或人类审批。
- Demo 只使用安全 mock sample，不处理真实生物危害、挥发性化学品、尖锐物、加热/高压设备。
- Region-pinned storage、pseudonymized sample IDs、raw video retention limits、encryption、RBAC、signed model artifacts、trusted time、immutable audit logs。
- 设计上支持 21 CFR Part 11、EU Annex 11、FDA CSA、ALCOA+ 和 data integrity 思路，但不声称 demo 已验证 production GMP。
- 中国场景默认考虑 PIPL、数据安全法、网络安全法、人类遗传资源和本地化数据平面。

## Why Qualcomm

LabLoop 是 Qualcomm 在 regulated physical AI 场景里的高价值样板：

- 实验室需要本地视觉、低延迟核验、设备网关、机器人控制和安全门控。
- 医疗、药企、HGR 和实验数据不能默认上公有云；edge inference 和本地缓存很关键。
- Qualcomm RB3/RB6/IQ、IM SDK、AI Hub、QNN/QAIRT、ONNX Runtime QNN EP 可支持 workcell vision、anomaly detection、机器人状态监控和 model release evidence。
- Qualcomm AI Hub / Workbench 可做模型转换、量化、profile 和设备侧验证。
- LeRobot HIL 让人工纠错和机器人动作变成可持续训练数据。

## Claims To Avoid

- 不说 FDA approved、NMPA approved 或 medical device software。
- 不说 improves diagnosis、improves patient outcomes 或 clinical decision support。
- 不说 blanket HIPAA / CLIA / CAP / GxP validated / Part 11 compliant。
- 不说 guarantees sample integrity、prevents all lost samples 或 eliminates rejection。
- 不说能接入所有仪器、所有 robot、所有 LIMS/ELN。
- 不说机器人能处理真实生物危害、挥发性化学品、尖锐物、加热/高压设备。
- 不说 dev kit 默认具备生产安全和网络安全配置。
- 不说 Qualcomm 官方合作/认证，除非真实签约。

安全表述：

- supports audit-ready chain-of-custody records。
- reduces manual reconciliation。
- alerts teams to custody, delay, QC, and temperature exceptions。
- measures logistics-related pre-analytical risk。
- designed for validation workflows; not validated production GMP in the demo.

## Ask

比赛阶段最需要 Qualcomm 支持三件事：

1. Edge hardware + AI profile：RB3/RB6/IQ，lab workcell vision、identity check、anomaly detection、本地推理 profile。
2. OEM/integration partner：sample tracking、plate reader/qPCR、liquid handling、AMR、SiLA/OPC UA LADS。
3. 3 个样板实验室：药企 QC/CRO/CDMO、医院检验、检验检测或高校核心平台。

## Sources

- Grand View lab automation market：https://www.grandviewresearch.com/industry-analysis/lab-automation-market
- MarketsandMarkets lab informatics：https://www.marketsandmarkets.com/Market-Reports/lab-informatic-market-203037633.html
- Grand View automated sample storage：https://www.grandviewresearch.com/industry-analysis/automated-sample-storage-systems-market-report
- NIH automated experimentation：https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/66
- ASCP workforce：https://criticalvalues.org/news/all/2026/01/27/ascp-2024-vacancy-survey-report-highlights-policy-priorities-to-address-laboratory-workforce-shortages-through-credentialing--advocacy--and-education-expansion
- Pre-analytical errors：https://profiles.wustl.edu/en/publications/pre-analytical-phase-errors-constitute-the-vast-majority-of-error/
- Deloitte QC lab modernization：https://www.deloitte.com/us/en/insights/industry/health-care/biopharma-lab-modernization-digital-transformation-qc-lab-future.html
- 医药工业数智化转型：https://www.ccfdie.org/cn/yjxx/yphzp/webinfo/2025/05/1744575796851275.htm
- 生态环境监测 LIMS：https://www.mee.gov.cn/xxgk2018/xxgk/xxgk10/202512/t20251223_1138494.html
- 临床检验质控指标：https://www.nhc.gov.cn/yzygj/c100068/202509/56aedbf79f6e476f89657d61e466f95a/files/2.%E4%B8%B4%E5%BA%8A%E6%A3%80%E9%AA%8C%E4%B8%93%E4%B8%9A%E5%8C%BB%E7%96%97%E8%B4%A8%E9%87%8F%E6%8E%A7%E5%88%B6%E6%8C%87%E6%A0%87%EF%BC%882025%E5%B9%B4%E7%89%88%EF%BC%89.pdf
- 镁伽科技：https://www.stcn.com/article/detail/2264818.html
- 华大智造 ZLIMS：https://www.mgi-tech.com/lab-management-system.html
- LabClaw：https://insilico.com/news_sc/rgga92ofe1-labclaw
- Automata：https://automata.tech/company-news/automata-raises-45m-series-c-funding
- Biosero：https://biosero.com/products/green-button-go-scheduler/
- SiLA：https://sila-standard.com/standards/
- OPC UA LADS：https://reference.opcfoundation.org/specs/OPC-30500-1/full
- Allotrope：https://www.allotrope.org/
- 21 CFR Part 11：https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11
- FDA CSA：https://www.fda.gov/regulatory-information/search-fda-guidance-documents/computer-software-assurance-production-and-quality-management-system-software
- Qualcomm IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
