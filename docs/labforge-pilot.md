# LabForgePilot Pitch

更新时间：2026-07-07。

## One-Line Thesis

LabForgePilot 是 RobotMac 平台的主比赛 demo 和第一个可销售楔子：一台桌面级 verified sample-transfer workcell，把 LeRobot 数据采集、ACT/HIL 训练、Qualcomm Dragonwing 边缘证据、条码/视觉核验、LIMS 写回和失败挖掘做成实验台上能购买的产品。

一句话：

> 把“样本从 A 放到 B”这件小事，变成可训练、可审计、可写回、可收费的机器人工作站。

## 01 · Problem

实验室真正昂贵的不是一次拿放，而是样本身份、物理位置和系统记录不同步。

- 中小型研发、QC、CRO、biobank、教学和转化实验室里，样本转移仍靠人手、条码枪、Excel、LIMS/ELN 补录和事后复核。
- 人力短缺和样本量增长同时发生。2025 年 MLO 调研中，71% 的 lab professionals 把 staffing 列为近期规划挑战，66% 提到 funding。
- 数据断裂也很真实。MLO 2025 显示 48% 的受访者仍受 LIS/EHR interoperability 和 data integration 困扰。
- 样本识别错误是实验室错误的重要来源。CDC/LMBP 和 CAP 都把条码/RFID、容器/申请单/位置一致性和核验作为关键实践。
- 失败经验没有沉淀。夹取失败、遮挡、错位、错样和人工接管通常被当场修掉，没有进入训练集。

核心痛点：

1. 样本从哪里来、到哪里去，系统未必实时知道。
2. 错样、漏扫、补录和复核消耗人力，还难以审计。
3. 机器人失败片段没有变成下一版策略的训练资产。
4. 裸机械臂便宜了，但实验室买不到“可培训、可维护、可写回”的完整工作站。

## 02 · Current Alternatives Fail

LabForgePilot 不正面挑战 Hamilton、Tecan、Beckman 或 Opentrons 的液体处理强项。它选择一个更窄、更适合比赛和商业试点的楔子：容器级 sample movement / staging / barcode verification / chain-of-custody / light QC。

- 人工 + LIMS：是事后记录，不是物理闭环。人能修复异常，但修复过程不会自动进入数据飞轮。
- Opentrons Flex：开放、价格透明、适合自动移液；但页面标注非 IVD/GMP，视觉核验、失败学习、LIMS 证据链仍需要用户自己拼。
- Hamilton / Tecan / Beckman：大型液体处理和高通量平台很强，但采购、验证和集成周期重，不是面向低成本 LeRobot 数据闭环的桌面工作站。
- Automata / Biosero / HighRes：实验室编排和跨设备调度成熟，但更适合已经有自动化团队的大客户。
- myCobot / Dobot / xArm / SO-101：证明硬件成本下降，但客户买到的是手臂，不是样本流程、夹具、应用、日志、训练和维护体系。
- 定制 SI：可以交付非标项目，但每个项目重新做夹具、接口、SOP、培训和维护，很难形成可复制商品。

结论：市场缺的不是另一只机械臂，而是能把样本动作、数据、审计和持续学习连起来的轻量产品。

## 03 · Solution

LabForgePilot 是一台桌面 sample-transfer workcell。

核心流程：

```text
LIMS/import worklist
→ scan source sample
→ verify rack/slot/sample identity
→ transfer tube / vial / mock labware
→ scan destination
→ capture QC photo and action trace
→ write back result
→ mine failures into LeRobot/HIL queue
→ retrain and redeploy edge policy
```

第一版只做容器级转移，不先挑战全谱复杂移液：

- tube-to-rack。
- rack-to-rack。
- tube-to-plate staging。
- plate/rack staging。
- barcode/sample verification。
- QC photo capture。
- failure mining。

每次动作绑定：

- sample ID。
- source / destination。
- operator / approver。
- timestamp。
- barcode/OCR/vision result。
- robot trajectory。
- policy version。
- edge profile。
- LIMS/ELN writeback receipt。

## 04 · Why Now

三件事在 2026 年同时成熟。

1. 实验室自动化有真实预算。Fortune Business Insights 估算 lab automation 市场 2025 年约 92 亿美元，2026 年约 100.7 亿美元，到 2034 年约 207.1 亿美元。
2. LeRobot 把桌面机器人学习变成可展示流程。2026-07-06 的 LeRobot v0.6.0 加强了 `lerobot-rollout`、DAgger-style HIL corrections、reward models、depth/language dataset support 和统一 benchmark；ACT 是可靠 baseline，SmolVLA 是语言条件升级。
3. Qualcomm Dragonwing 提供可量化边缘叙事。RB3 Gen 2 / QCS6490 是 2026 年 7 月比赛 MVP 的可信 target，QCS8550 是扩展 profile，IQ10 RRD 是 2026 年 9 月后 roadmap / early access ask。

为什么现在能赢比赛：

- 3 分钟内可以展示一个完整闭环，而不是只展示机械臂动作。
- 失败不再是演示事故，而是 HIL/DAgger 数据飞轮的证据。
- Qualcomm 的价值不是贴 logo，而是本地视觉、低延迟决策、断网运行、AI Hub/QAIRT/QNN profile 和可提交 evidence pack。

## 05 · Product

硬件组成：

- 低成本桌面机械臂或 SO-101 风格 follower arm。
- 可选 leader arm / teleop station。
- front + top/side cameras。
- 条码扫描器或相机条码解码。
- 固定管架、孔板、样品盒、夹具和灯箱。
- Qualcomm Dragonwing-class edge compute。
- 急停、边界、限位、权限和安全状态灯。

软件组成：

- `TubeRackTransfer`：样本管从源管架到目标槽位。
- `PlateStaging`：孔板/样品盒 staging。
- `BarcodeVerify`：worklist 与条码/孔位不匹配时拒绝执行。
- `QCPhoto`：关键动作后拍照留证。
- `FailureMining`：失败片段、人工接管、恢复动作入库。
- `EdgeProfileViewer`：展示 AI Hub/QNN/ONNX Runtime QNN profile。
- `LIMSWriteback`：Benchling/LIMS/mock connector 写回。

明确不承诺：

- 临床诊断。
- GMP/CLIA/IVD 认证。
- 替代高精度液体处理器。
- 未实测的电池续航、端到端 latency 或全 NPU 路径。

合规定位：

- LabForgePilot 是 bench actions 和 LIMS/ELN/LIS/QMS 之间的执行与证据层，不替代系统记录源。
- 美国/EU 药企 QC 口径写成“支持 Part 11 / Annex 11 validation workflows”，不写“validated GMP product”。
- 中国版默认本地私有云 / on-prem / edge gateway，不默认导出原始图像、视频或样本元数据。
- 涉及人类样本、诊断、HGR/基因组或敏感个人信息时，必须进入更高等级数据、伦理、法务和客户验证流程。

## 06 · Product API/Evidence

Product API 的目标是让评委看到：这不是脚本，而是产品接口。

```text
POST /jobs/import
POST /samples/verify
POST /robot/transfer
POST /events/intervention
POST /lims/writeback
GET  /evidence/run/:id
GET  /policies/:id/profile
```

关键对象：

- `Job`：从 LIMS/CSV/API 进入的 worklist，包含 sample、source、destination、priority 和 SOP。
- `SampleVerification`：条码、OCR、视觉槽位、rack pose、operator approval 和 mismatch reason。
- `Episode`：LeRobotDataset v3 episode，包含多相机视频、低维状态/动作、metadata 和 train/eval split。
- `Intervention`：HIL 接管帧、leader-arm 恢复动作、失败类型、恢复是否成功。
- `PolicyCard`：ACT/SmolVLA checkpoint、dataset hash、camera config、训练步数、success@20、interventions/min。
- `EdgeProfile`：device id、model hash、runtime、QNN/CPU/GPU path、latency、memory、fallback status。
- `WritebackReceipt`：LIMS/ELN/QMS 写回 payload、时间戳、结果、异常、签名和 evidence link。

比赛证据页必须展示：

- LeRobotDataset v3 episode preview。
- ACT baseline 前后 success@20。
- HIL/DAgger correction replay。
- Qualcomm AI Hub / QAIRT / QNN 或 ONNX Runtime QNN profile。
- 本地断网运行视频。
- 错样拦截事件。
- LIMS writeback receipt。

Validation-ready package：

- URS。
- functional spec。
- design spec。
- risk assessment。
- data-flow map。
- supplier assessment。
- traceability matrix。
- IQ/OQ/PQ scripts。
- test evidence。
- release notes。
- SBOM / vulnerability report。
- backup / restore evidence。
- disaster recovery procedure。
- change-control template。
- admin SOP templates。

P0 compliance controls：

- RBAC、SSO/SAML/OIDC、MFA option。
- unique users、service-account separation。
- e-signature with meaning/reason。
- trusted time、append-only audit trail、audit-trail review screen。
- exportable audit packet、retention policies、encrypted storage、tenant KMS。
- immutable log option 和 raw-data hash chain。

## 07 · Market & Business Model

市场不是“所有实验室自动化”，而是可快速采购、可快速试点的 sample-transfer / custody workcell。

第一批买家：

1. 高校、职业院校、机器人/生物工程交叉课程：买 5-20 台教学和比赛套件。
2. Biotech R&D、CRO、core facility、biobank：买 1-3 台 pilot kit 做 sample receiving / staging / QC photo。
3. Pharma/biopharma QC 前处理：先做 research/non-GxP 或 pre-validation workflow，证明 deviations、audit time 和 hands-on minutes 下降。
4. 食品、环境、材料、电池和化妆品小型 QC：重复转移、扫码、拍照、记录和异常闭环。
5. SI/OEM 渠道：把 LabForgePilot 当成可复制 demo cell 和 RobotAppLayer 应用入口。

中国版：

- Edu/Starter Kit：¥29,800-49,800。
- Lab Pilot Kit：¥68,000-98,000。
- Fleet Kit 5-pack：¥298,000-498,000。
- Software：¥599-1,999/机器人/月。
- Training credits：¥500-800/小时，或 ¥10,000 包。
- Support：硬件价 15%-20%/年。

中国版采购/部署：

- 中文 UI、中文验证包、VAT 发票、本地支持 SLA。
- 国产机器人、相机、扫描器和夹具 BOM option。
- 企微/钉钉/飞书通知。
- 本地 LIMS/QMS/ERP adapter。
- 数据默认留在大陆；训练数据带 non-sensitive、personal information、sensitive PI、HGR/genomic、important-data-candidate 标签。

海外版：

- Pilot Kit：$9,900-$14,900。
- Fleet Kit 5-pack：$39,000-$69,000。
- Software：$199-$499/robot/month。
- Training：$150-$250/hour。
- Support：$2,000-$8,000/year。

海外版采购/部署：

- SaaS / VPC / on-prem。
- regional residency。
- DPA/SCC support for EU。
- HIPAA BAA option for qualified customers。
- SOC 2 / ISO 27001 roadmap。
- English validation pack。
- Benchling / LabWare / Thermo / Dotmatics-style connector。

90 天 design-partner KPI：

- hands-on minutes saved per run。
- samples/hour。
- wrong-sample blocks。
- turnaround time。
- rerun/deviation rate。
- audit-prep time。
- interventions per episode。
- HIL 后 success@20 提升。

## 08 · Competition & Moat

不要说“我们比所有液体处理平台都强”。更准确的竞争图：

- Manual tech：灵活，但不可学习、不可规模化、不可实时审计。
- LIMS/ELN：记录真相，但不移动样本。
- Opentrons/Hamilton/Tecan/Beckman：液体处理强，但 sample custody、失败学习和低成本边缘数据闭环不是第一卖点。
- Lab orchestrators：编排成熟，但部署重，通常服务已有自动化基础的大客户。
- Robot arms：便宜，但没有应用层、证据层、连接器和支持体系。
- SI：能做项目，但难以形成产品 flywheel。

Moat：

- Labware templates：管架、孔板、样品盒、夹具、灯箱和相机标定模板。
- Failure/recovery dataset：每个错夹、掉落、遮挡、错位和人工接管都进入训练队列。
- LIMS/SOP semantics：样本、任务、操作者、孔位、异常、图像证据和写回 receipt 绑定。
- Edge evidence：AI Hub/QNN profile、model hash、device id、latency、fallback、runtime version。
- App ecosystem：`TubeRackTransfer`、`BarcodeVerify`、`QCPhoto`、`FailureMining` 变成 RobotAppLayer / SkillDock 应用。
- Channel loop：学校、SI、OEM、科研平台和 QC 实验室共同沉淀课程、模板和维护手册。

## 09 · Why Qualcomm

LabForgePilot 是 Qualcomm 应该支持的 Physical AI 样板：真实世界、隐私敏感、需要低延迟、可离线运行、能从 prototype 走向 production。

比赛 MVP：

- RB3 Gen 2 / QCS6490：可信 demo anchor，支持 Qualcomm Linux、GStreamer、robotics algorithms、相机和 12 dense TOPS 级别边缘 AI 路线。
- AI Hub Workbench + QAIRT/QNN：把 PyTorch/ONNX/TFLite 模型优化、profile 到真实设备或 proxy，输出 runtime、latency、memory 和 compute-unit evidence。
- ONNX Runtime QNN：作为部署路径之一，而不是唯一承诺。
- 本地 CPU/CV 条码解码 + ROI OCR/vision：条码不夸成 NPU magic，视觉模型和 OCR 走 edge profile。

扩展路线：

- QCS8550：更强多相机、多模型和 on-prem robot operations box。
- IQ-9075 / IQ9：工业高端 bridge。
- IQ10 RRD：roadmap / early access ask；不写成 2026-07 已集成量产硬件。

给 Qualcomm 的价值：

- 展示 Dragonwing 不只是开发板，而是机器人产品 SKU 的核心。
- 展示 AI Hub/QNN profile 不是 benchmark 截图，而是 release gate 和商业 evidence。
- 给比赛一个可拍、可测、可销售、可复用的 edge AI demo。

## 10 · Demo & Ask

3 分钟视频：

1. 0:00-0:20：人工实验台、条码枪、Excel/LIMS 补录、错样风险。
2. 0:20-0:45：LabForgePilot workcell 和工作流：import job、scan、verify、transfer、writeback。
3. 0:45-1:10：teleop 采集 LeRobotDataset v3 episode，样本、孔位、视频和动作绑定。
4. 1:10-1:35：ACT baseline autonomous rollout。
5. 1:35-1:55：故意放入错误样本，BarcodeVerify 拒绝执行并生成事件。
6. 1:55-2:20：故意制造偏移，人类 HIL 接管恢复，系统记录 correction。
7. 2:20-2:40：Qualcomm edge profile、本地断网运行、latency/power measured-by-us 占位。
8. 2:40-3:00：LIMS writeback receipt、失败入训练队列、付费 pilot ask。

7 分钟现场 demo：

1. 输入新 worklist。
2. 扫描错误样本并拒绝。
3. 扫描正确样本并执行转移。
4. 人为移动目标位或样本，展示暂停/重定位/接管。
5. 打开 evidence packet：episode、intervention、policy card、edge profile、writeback receipt。
6. 展示 pricing 和 90 天 design partner KPI。

Fallback：

- Green：真实 ACT/HIL 闭环跑通。
- Yellow：学习感知 + 规划器 + 运动原语，保留 LeRobot 数据和 Qualcomm profile。
- Red：仿真策略 + 真实台面感知 + 一个安全物理子任务。
- 最低可交付：端侧识别、任务规划、动作日志、一个物理动作成功，不能退化成纯视频或纯网页。

Ask：

- RB3 Gen 2 Vision/Core Kit。
- QCS8550 profile target。
- IQ10 RRD roadmap review。
- AI Hub/QNN office hours。
- 允许提交 Qualcomm profiling artifacts。
- 2 个实验室/教育/SI pilot intro。
- 90 天内跑 3 个 paid design-partner workcells，证明零错配、可审计写回、干预率下降。

## Sources

- Competition page：https://qc-robotics-dev.aidlux.com/2026/
- LeRobot release v0.6.0：https://github.com/huggingface/lerobot/releases
- LeRobot v0.6.0 blog：https://huggingface.co/blog/lerobot-release-v060
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot ACT：https://huggingface.co/docs/lerobot/en/act
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
- LeRobot SO-101：https://huggingface.co/docs/lerobot/en/so101
- SmolVLA：https://huggingface.co/docs/lerobot/en/smolvla
- Lab automation market：https://www.fortunebusinessinsights.com/laboratory-automation-market-111623
- Liquid handling systems market：https://www.fortunebusinessinsights.com/liquid-handling-system-market-111701
- MLO 2025 state of the industry：https://www.mlo-online.com/information-technology/analytics/article/55263674/us-medical-labs-embrace-digital-transformation-amid-staffing-cost-and-data-challenges-key-insights-from-the-2025-mlo-state-of-the-industry-soi-survey
- Deloitte QC lab modernization：https://www.deloitte.com/us/en/insights/industry/health-care/biopharma-lab-modernization-digital-transformation-qc-lab-future.html
- CDC barcode best practices：https://www.cdc.gov/labbestpractices/pdfs/cdc_barcodingsummary.pdf
- CAP specimen handling guide：https://documentsuat.cap.org/documents/practical-guide-specimen-handling.pdf
- Opentrons Flex：https://opentrons.com/products/opentrons-flex-robot
- Automata LINQ：https://www.automata.tech/linq
- Biosero GBG：https://biosero.com/products/green-button-go-orchestrator/
- HighRes Cellario：https://www.highres.com/lab-orchestration
- Benchling LIMS：https://www.benchling.com/lims-software
- 21 CFR Part 11：https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11
- Qualcomm Dragonwing：https://www.qualcomm.com/news/onq/2025/02/unveiling-the-qualcomm-dragonwing-brand-portfolio
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm QCS6490：https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490
- Qualcomm QCS8550：https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN：https://github.com/onnxruntime/onnxruntime-qnn
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
