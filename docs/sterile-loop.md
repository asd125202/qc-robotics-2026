# SterileLoop 手术器械异常闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

SterileLoop 帮医院 CSSD/SPD 和手术室在托盘上台前关闭缺件、错件、损坏、周期缺证和外来器械延误：

> Qualcomm 边缘视觉做终检，扫码/RFID 和清洗灭菌记录补证据，人工签核完成放行前确认，LeRobot HIL 把每次纠错变成下一轮训练数据。

它不是基础器械追踪系统，也不是自动临床放行系统。它做的是 surgical tray exception closure。

## YC-Style Opening

手术不该等一把还没找到的钳子。

医院已经有器械追踪、清洗机、灭菌器、HIS/手麻系统和人工清点，但开台前真正让 OR、CSSD、供应链和质控一起着急的问题不是“有没有记录”，而是：

- 谁负责？
- 怎么补救？
- 替代件是否合规？
- 清洗/灭菌周期证据在哪里？
- 护士和技师是否已经确认？
- 能不能上台？

SterileLoop 把这些问题变成一个可以发现、分派、补证、签核和审计的异常对象。

## Problem

医院已经追踪了器械，却仍然会在开台前为一把器械停下来。

- 延误发生在最贵的地方：器械错误常常到开台前才暴露，巡回护士、外科医生、CSSD 和供应商开始打电话、找替代、等补包。
- 视觉任务天然易错：托盘复杂、器械相似、金属反光、班次紧，缺件、错件、损坏候选和污物候选都压在人眼上。
- 追踪不等于关闭：条码/RFID 可以告诉你资产在哪里，但不能自动证明周期证据齐全、替代件合规、护士和技师已经确认。
- 事后报告太晚：事件上报常常不完整且滞后，无法支撑实时分派、根因复盘、召回闭环和跨班次培训。

## Why Now

2026 年的机会不是从零教育医院“要不要数字化 CSSD”。预算、痛点和标准已经存在。真正的新入口，是把视觉终检、周期证据、UDI/RFID、人工签核和边缘 AI 组织成一个能在 90 天内证明 OR 容量回收的产品。

关键证据：

- BMC Surgery 2024 直接观察研究中，562 台手术有 147 台至少出现一个器械错误，占 26.16%。
- 同研究中，有延误数据的器械错误病例平均延误约 10.16 分钟。
- 该研究还估算单院区年度可计费 OR 分钟损失可达 675 万-942 万美元。
- BMC Health Services Research 2026 对美国器械再处理建模，估算每年近 40 亿次器械再处理事件，70%-87% 已灭菌器械在手术中未被使用，缺失器械替换负担中位数约 3.17 亿美元/年。
- Aesculap/Ascendco 2025 benchmark 中，76% 受访者把人为错误列为追踪挑战，51% 提到器械丢失，57.7% 表示库存准备不足会导致手术延误或取消。
- Censis Assembly Copilot、Scalpel AI、RIF Robotics 和 SterileVision 证明视觉终检、AI 托盘验证和机器人辅助开始进入商业和医院创新流程。
- 中国 WS/T 879-2025 CSSD 监测数据标准 2026-06-01 生效，强调采集、存储、共享、追溯和反馈。
- 中国 UDI 扩围、DRG/DIP 2.0 落地、第三方/区域消供中心增长，让 CSSD 从后台流程变成医院运营数据和成本问题。

## Insight

最小商业单元不是托盘，而是“会阻塞手术的异常”。

> 追踪系统回答 where，SterileLoop 回答 closed or not。

医院不会先为“机器人自动临床放行”买单，但会为更少 OR 等待、更少找器械电话、更完整 CSSD 追溯、更快召回、更少重洗返工和更可信审计付费。

## Solution

SterileLoop 是托盘离开 CSSD 前的 30 秒异常关闭层。

它插在现有流程之上，把“这盘看起来有问题”变成“已分派、已纠正、已补证、已签核、可审计”：

1. Inspect：固定相机和 Qualcomm edge 模型识别托盘模板、槽位、器械类别、缺件、错件、多件和低置信度区域。
2. Reconcile：扫码、UDI/DataMatrix、RFID、清洗/灭菌周期、BI/CI、过期时间和人工记录汇成同一个异常包。
3. Route：异常按手术时间、严重度、替代方案和责任人分派给 CSSD、OR、供应链、供应商或质控。
4. Close：人工签核后导出证据包；纠错、接管和低置信度样例进入 LeRobot HIL 训练队列。

## Product

第一版只卖一个清晰产品：

> Edge Inspection Station + Exception Console + Evidence Packet

第一版不判断“无菌”，不自动放行临床托盘。它做辅助终检、证据汇聚、异常分派、人工签核和审计包。

核心 workflow：

1. Load：扫描托盘条码，加载模板、病例时间、医生偏好、外来器械、关键件和版本哈希。
2. See：固定顶视/侧视相机识别槽位、器械类别、缺件、错件、多件、遮挡和低置信度区域。
3. Match：把视觉结果与 UDI/DataMatrix、RFID、清洗批次、灭菌批次、BI/CI 和人工备注对齐。
4. Assign：异常按开台时间、严重度、替代路径和责任人进入 CSSD、OR、供应商或质控队列。
5. Close：技师/护士人工签核，系统输出照片、扫码、周期、模型版本、HIL 片段和关闭时间。

## Market Wedge

先卖给最讨厌“找器械”的人，而不是先卖给全院。

第一批试点不是全院替换，而是一个高风险托盘族、一个手术线或一个外来器械流程，在 90 天内证明延误分钟、重洗返工、缺件老化和审计缺证下降。

优先入口：

- 骨科 / 脊柱：器械多、外来包多、相似件多、手术分钟贵。
- 心外 / 神外：关键件缺失和替代方案确认需要更早、更可信闭环。
- 机器人手术：器械、附件、能量设备和专用托盘复杂，适合模板化视觉终检。
- 外来器械：供应商到货、清洗、灭菌、放行、召回和归还链路跨组织。
- 中国三甲：手术量大、DRG/DIP 压力强，WS/T 879-2025 和 UDI 扩围让 CSSD 数据合规进入预算语言。
- 独立/区域 CSSD：需要证明回收、清洗、灭菌、发放、不合格反馈和跨院召回闭环。

## Business Model

卖点不是“AI 准确率”，而是 90 天内可回收的 OR 容量。

收入模型：

> 90-day paid pilot + site subscription + edge inspection station + integration + optional savings share

建议价格：

- 90 天试点：25k-75k 美元或 20-60 万元，覆盖一个院区、4-8 间 OR 或一个高风险服务线。
- 硬件/集成较重的试点：75k-125k 美元。
- 年度站点订阅：75k-250k 美元/院区量级，按 OR 数、CSSD 站点、托盘量、终检工位和集成模块扩展。
- 硬件包：Qualcomm edge node、相机、扫码/RFID、光源、工位治具和安全桌面机器人。
- VAC 商业包：给 Value Analysis Committee 一页 ROI：延误分钟、取消手术、替换支出、返工和人工节省。

ROI 公式：

`90-day ROI = (avoided OR delay minutes * local OR cost/min + avoided cancellations * cost/cancel + avoided rework trays * reprocess cost + avoided replacement spend + avoided search/overtime labor - pilot cost) / pilot cost`

90 天 KPI：

- 器械相关 OR 延误分钟 / 100 台病例下降 20%+。
- 95%+ 阻塞手术异常当天关闭。
- 95%+ 异常 15 分钟内分派责任人。
- 托盘缺陷率：缺件、错件、损坏、包装/指示物问题下降。
- 缺失器械和替换支出下降。
- 重洗、返工、wet load、held set 和 IUSS 触发事件下降。
- case cart / tray readiness by cutoff 提升。
- 审计包完整率提升到 95%+。

## Go-To-Market

试点设计：

1. 2 周 baseline：记录每 100 台病例的器械异常、缺件、错件、重洗、IUSS、OR 等待、找器械电话和文档完整率。
2. 8-10 周 active pilot：部署一个边缘终检工位，接入托盘模板、扫码/RFID、周期记录和 OR 时间表。
3. 每周 ROI dashboard：用医院本地 OR 分钟成本、取消手术成本、替换支出、返工和人工数据输出 before/after。
4. 结题材料：给 VP Perioperative Services、COO、Director of Surgical Services、CSSD 负责人、OR 护理、院感/质控、IT/security 和 Value Analysis Committee。
5. 扩展路径：赢下一个托盘族后，扩到外来器械、召回、供应商 SLA、院区 CSSD 和区域消供中心。

## Competition

竞品证明预算存在；SterileLoop 选择更窄、更可演示的异常关闭切口。

- Censis / STERIS SPM / Aesculap Ascendco：SPD 流程、资产追踪、周期记录和报表强；SterileLoop 聚焦终检异常是否关闭。
- ReadySet：外来器械、供应商和 bill-only 协同强；SterileLoop 把外来包接到托盘终检和周期证据。
- Scalpel AI / SterileVision / RIF Robotics：AI 托盘验证、视觉缺陷检查和机器人装盘方向强；SterileLoop 的差异是 OR/CSSD/VAC 共同认可的关闭证据和 ROI。
- 新华医疗 / 老肯 / 安特速 / 第三方 CSSD：设备和消供服务强；SterileLoop 做跨系统异常关闭层。
- 医院物流机器人：运输强；SterileLoop 做托盘 QA、签核和异常数据。

定位：

> AI visual QA layer that plugs into Censis/SPM/ReadySet and closes exceptions before the tray reaches the OR.

## Moat

壁垒不是看懂一张托盘照片，而是知道每类异常如何被关闭。

会积累的资产：

- Exception Graph：托盘模板、器械身份、病例时间、医生偏好、外来包、周期记录、替代路径和 OR 时间。
- Evidence Dataset：视觉帧、扫码/RFID、设备周期、人工纠错、机器人指引、替代件和签核结果。
- Standards Connectors：WS 310、T/WSJD 39、WS/T 879、UDI、FHIR Device、HIS、手麻、HRP 和院感接口。
- Edge Profiles：反光金属器械、多相机、弱网、本地隐私、QNN/QAIRT 和 HIL 数据。
- ROI Benchmarks：按服务线、托盘族、异常类型、责任队列和关闭时间形成运营基准。

## Architecture

### Edge Capture

- Fixed overhead RGB / RGB-D camera。
- Optional side or macro camera。
- Polarized / diffuse lighting for reflective instruments。
- Darkfield/ring lighting for etched Direct Part Marks。
- Handheld 2D barcode/DataMatrix scanner。
- Optional UHF RFID mat, treated as supplemental proof。
- Tray barcode and mock UDI labels。
- Washer/sterilizer gateway over REST/MQTT/CSV demo feed。

### Edge Runtime

- RB3 Gen 2 / QCS6490 / Dragonwing。
- `camera_node`。
- `tray_pose_node`。
- `instrument_detector_qnn`。
- `identifier_decoder`。
- `count_fusion_node`。
- `washer_gateway_node`。
- `exception_engine`。
- `robot_pointer_node`。
- `audit_packet_api`。

### Data Objects

- `tray_instance`
- `manifest_version`
- `expected_item`
- `observed_item`
- `identifier_scan`
- `process_cycle`
- `exception`
- `closure_action`
- `operator_signoff`
- `evidence_packet`

### Training Loop

- Human corrections and recovery actions become HIL episodes。
- China raw data stays in hospital/on-prem/China cloud。
- Overseas raw data stays in overseas cloud。
- PyTorch/ONNX -> AI Hub profile/quantize/validate -> QNN/QAIRT artifact -> edge redeploy。

## Competition Demo

3 分钟 demo 只证明一件事：异常能被发现、分派、补证、人工关闭。

1. 操作员扫描 mock 托盘条码，加载 Ortho Minor Tray 模板。
2. overhead camera 检测托盘和器械，edge UI 显示 expected vs observed。
3. 演示者移走一个 forceps、加入一个错误 clamp、遮住一个 DataMatrix。
4. edge inference 打开 missing forceps / unexpected clamp / unreadable mark 异常。
5. 机械臂用塑料指针慢速指向异常槽位，不接触临床器械。
6. 人工通过 LeRobot leader/gamepad 暂停、接管、纠正并恢复。
7. 操作员扫描替代器械条码，RFID mat 作为补充证据确认存在。
8. 模拟 washer/sterilizer gateway 发送 cycle pass / cycle missing 两种状态。
9. 技师人工关闭；系统导出照片、扫码、周期引用、HIL 片段、模型版本、设备 ID、签核和关闭时间证据包。

## Why Qualcomm

这是 Qualcomm 能进入医院真实运营闭环的边缘 AI 样板。

- 医院不希望托盘图像、手术计划、人员行为和设备周期默认上公网云。
- 反光器械和多相机终检需要本地低延迟推理。
- CSSD 工作站需要弱网可用、审计日志和设备身份。
- AI Hub / QNN / QAIRT 让比赛 demo 能展示模型 profile、部署、运行和回滚链路。
- 商业上连接智慧医院、CSSD、器械供应、院内机器人、区域消供和医疗 IoT。

## Ask

比赛阶段需要一个可信、保守、可演示的 CSSD 托盘异常闭环样板。

需要：

- RB3 Gen 2 / RB6 / Dragonwing dev kit。
- 固定相机、偏振/漫射光源、扫码枪、RFID mat、桌面机械臂。
- 泡沫/塑料/退役器械、托盘模板、条码/UDI mock 标签、清洗/灭菌周期模拟器。
- 匿名托盘模板、器械清单、异常类型、替代规则、周期字段和审计字段样例。
- AI Hub / QNN profile 支持。
- 2-3 位 CSSD、OR 护理、院感/质控顾问。

## Claims To Avoid

- 不说 SterileLoop 证明无菌。
- 不说自动临床放行手术托盘。
- 不替代 CSSD 技师或 OR 护士清点。
- 不承诺视觉唯一识别每把真实器械。
- 不检测微生物、所有污染、锋利度或微观损伤。
- 不声称 FDA/AAMI/医院生产就绪。
- 不声称 RFID/DataMatrix 永远可读。
- 不声称可接所有清洗机、灭菌器、EHR 和器械系统。

## Sources

- BMC Surgery instrument errors：https://link.springer.com/article/10.1186/s12893-024-02407-1
- BMC HSR reprocessing cost：https://link.springer.com/article/10.1186/s12913-026-14663-3
- Surgical instrument tracking market：https://www.marketsandmarkets.com/Market-Reports/surgical-instrument-tracking-system-market-211153029.html
- Aesculap / Ascendco benchmark：https://www.aesculapusa.com/content/dam/aesculap-us/us/website/aesculap-inc/healthcareprofessionals/surgical-asset-management-solutions/2025%20Surgical%20Asset%20Management%20Industry%20Benchmark%20Report%20Aesculap%20Ascendco%20Health%20UPDATE.pdf
- Censis CensiTrac：https://censis.com/products/censitrac/
- Censis Assembly Copilot：https://censis.com/products/censis-copilot
- Fortive Censis overview：https://fortive.com/censis
- STERIS SPM：https://www.steris.com/healthcare/products/spm
- ReadySet Vizient：https://readysetsurgical.com/resources/readyset-vizient/
- ReadySet Epic Connection Hub：https://www.businesswire.com/news/home/20250528617815/en/ReadySet-Surgical-Now-Available-in-Epic-Connection-Hub
- Scalpel AI：https://www.scalpel.ai/
- RIF Robotics / Wellstar：https://catalyst.wellstar.org/casestudies/rif-robotics/
- Robotic tray assembly research：https://arxiv.org/html/2602.01679v1
- WS/T 879-2025：https://www.nhc.gov.cn/fzs/c100048/202512/42af605da1384e038617405834641909/files/WST%20879%E2%80%942025.pdf
- T/WSJD 39-2023：https://www.qiluhospital.com/uploadfile/2023/0303/20230303174258890.pdf
- China UDI policy：https://udi.nmpa.gov.cn/toDetail.html?CatalogId=2&infoId=80
- FDA UDI basics：https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/udi-basics
- eCFR 21 CFR 801.45 direct marking：https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-801/subpart-B/section-801.45
- CDC sterilizing practices：https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/sterilizing-practices.html
- FHIR Device：https://build.fhir.org/device.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/general_introduction.html
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
