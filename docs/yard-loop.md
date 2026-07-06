# YardLoop 港场异常闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

YardLoop 是港场 TOS 之上的 AI 异常关闭操作层：

> 港口已有摄像头和 TOS，YardLoop 关闭仍靠对讲机、截图和 Excel 流转的异常。

它面向码头、内陆港、铁路联运场、港外堆场和 chassis pool，把 TOS、闸口 OCR、预约、查验、箱号、封签、箱损、底盘车、司机和现场视频连成一条可分派、可复核、可举证、可回写、可训练的异常闭环。

YardLoop 不替代 TOS/YMS，也不卖“全自动码头”。它是现有系统之上的 exception control plane。

## Problem

港场不是缺系统，而是异常卡在系统之间。

TOS 记录计划，摄像头看到现场，司机在电话和微信里改计划，调度靠对讲机救火。每一个没有闭环的异常都会变成排队、滞箱费、截关风险、设备空等、damage claim 和客户投诉。

具体痛点：

- TOS/YMS 知道“应该发生什么”，但箱号、箱位、封签、查验、放行和底盘车状态常在现场偏离。
- OCR、LPR、摄像头和司机 App 能发现问题，但低置信度、错箱、缺封签和箱损仍靠人工追。
- D&D、箱损、roadability、release proof 和客户争议需要证据链，不是一张截图。
- 全自动码头重、慢、敏感；human-in-the-loop 的异常闭环更容易先落地。

## Why Now

吞吐增长、船期波动、D&D 争议和 smart port 投资同时放大异常成本。

关键变化：

- 全球集装箱港口吞吐量 2024 年约 9.13 亿 TEU。
- 中国 2025 年港口集装箱吞吐量约 3.54 亿 TEU，同比增长 6.8%。
- 2025 年全球约 850 个相关集装箱码头中，仅 76 个有运营中的自动化能力，说明大多数场站需要 retrofit layer，而不是一次性全自动改造。
- Tideworks/Port Technology 调研显示，许多 terminal professionals 仍在面对数据准确性、内部系统集成、外部数据共享、实时可视性和人工数据流程问题。
- FMC 和相关规则把 demurrage / detention 账单证据推向前台。
- 中国智慧港口政策到 2027 年强调数字化基础设施、智能感知网络、5G/F5G/北斗、AI、区块链、数字孪生、全流程和闭环。
- 铁水联运、内陆港、海关便利化和单一窗口让跨系统交接更多，异常面也更多。

港口买方不是第一次数字化。变化在于：越来越多设备已经能看见现场，但大部分港场还没有把异常关闭。

## Core Insight

港场真正值钱的数据，不是 ETA 或视频流，而是异常如何被解决。

识别是入口，关闭才是产品：

> event -> exception -> owner -> SLA -> evidence -> action -> TOS writeback -> audit -> HIL improvement

谁先沉淀异常类型、责任人、SOP、影响金额、动作结果和复核证据，谁就能训练出港场运营的行动模型。

## Solution

YardLoop 是 TOS、OCR、闸口、堆场和司机协同之上的 exception control plane。

产品模块：

1. **Event Fusion**：接入 TOS、OCR/LPR、预约、查验、hold/release、GPS/AIS、视频和司机协同数据。
2. **Exception Engine**：识别 OCR mismatch、seal missing、damage、appointment miss、hold conflict、container not found、chassis issue。
3. **Action Orchestrator**：分派调度、闸口、场桥、司机、客户或巡检小车，按 SLA 跟踪关闭。
4. **Evidence Ledger**：冻结图片/短视频、模型版本、人工决策、hash、TOS 写回和争议证据包。
5. **TOS/YMS Writeback**：人工批准后写入 Gate Hold、Inspection Required、Evidence URI、Suggested Yard Task、release proof。
6. **Learning Loop**：OCR glare、bad angle、missing seal、雨夜、遮挡和人工纠正进入 LeRobot/HIL 数据队列。

## Product Workflow

第一版先做 Gate Exception Control Tower：

1. 闸口相机读到箱号。
2. ISO 6346 / BIC check digit 或 TOS expected-vs-actual 触发异常。
3. 系统建议 `SOFT_HOLD`，生成 owner、SLA、证据要求和人工审核按钮。
4. 小车/AGV 或人工补拍 door-side code、seal、damage 和 chassis proof。
5. 人工批准后，回写 TOS/YMS：Gate Hold、Inspection Required、Evidence URI、Suggested Yard Task。
6. 系统生成 evidence pack：图片、短视频、OCR box、confidence、lane ID、timestamp、appointment、model version、operator decision、ledger hash。
7. operator 标注 root cause，例如 OCR glare + missing seal。
8. 片段导出为 LeRobot episode，进入区域云训练和 Qualcomm edge profile 队列。

## Market Wedge

先打闸口异常控制塔，再扩到堆场、铁路、查验、chassis 和客户堆场。

第一 wedge：

- OCR mismatch。
- missing booking。
- hold/release mismatch。
- appointment miss。
- unpaid demurrage。
- container not found。
- seal / damage flag。
- chassis / roadability issue。

中国版：

- 场景：上海、宁波舟山、深圳、青岛、天津、广州、厦门等智慧港口，内陆港，铁水联运场，查验堆场，chassis pool。
- 竞合：不替换 ZPMC、招商国科、Westwell、主线科技、飞步等系统和设备；做异常识别、分派、处置、复核、留痕的一体化闭环。
- 政策语言：智能感知、一张图、全流程、智能调度、闭环式防控、单一窗口、一次委托、一单到底、一箱到底。
- 数据策略：视频、车牌、客户货物和场站运营数据默认不上境外云；本地云或私有云训练。

海外版：

- 场景：中小码头、rail intermodal yard、inland depot、chassis pool、drayage yard、大型进口商堆场。
- 生态：Kaleris/Navis、Tideworks、Camco、CERTUS、Visy、Kalmar、project44、FourKites、Terminal Industries。
- 进入方式：private terminal operators 和 depot/chassis operators 比公共港口 RFP 更快。

## Business Model

YardLoop 定价高于通用 workflow，低于替换 TOS 或 smart gate。

建议模型：

- **Paid Pilot**：海外 15k-50k 美元，8-12 周；中国 30万-100万元，先接一条 lane / 一个 workflow。
- **Platform ARR**：50k-150k 美元 / site / year + 0.05-0.15 美元 / gate-yard transaction。
- **AI Evidence Add-on**：0.08-0.25 美元 / imaged container，或 20k-80k 美元 / lane / year。
- **Implementation**：25k-150k 美元一次性，按 TOS/OCR/PCS/EDI 集成复杂度收费。
- **Large Terminal ACV**：1.5M+ annual transactions 可到 400k-700k 美元 ARR。
- **Hardware**：摄像头、edge box、小车和传感器可合作或 pass-through，不做核心毛利来源。

ROI 逻辑：

- 500k annual transactions，若 5% exceptions，即 25k trouble tickets / year。
- 25k exceptions x 10 min x $65/hr loaded cost，可形成约 $271k manual handling baseline。
- 若减少 40%，直接人工节省约 $108k。
- 若每个异常减少 15 min truck wait，25k x 15 min x $75/hr 是约 $469k ecosystem value。
- 防止 500 avoidable container-days，可形成 $55k-$138k D&D customer value，具体取决于 dry/reefer/chassis。
- Damage evidence 和 audit trail 可减少 claim/admin 成本。

生产门槛：

- TOS writeback success >99%。
- 不增加 truck turn time。
- exception MTTR 降 30-50%。
- manual touches per exception 降 30-50%。
- audit/evidence package 5 分钟内可取。

## Go-To-Market

8-12 周试点：

1. Weeks 1-2：映射 exception taxonomy、TOS/OCR feed、baseline KPI 和安全/权限边界。
2. Weeks 3-6：shadow mode，不写回；分类异常、测量 leakage、生成证据包。
3. Weeks 7-10：live assist：一个 lane、一个 shift、一个异常队列，人工批准后写回。
4. Weeks 11-12：ROI readout、production security/integration plan、扩展范围。

核心 KPI：

- Exception rate。
- Mean/P90 exception resolution time。
- Truck turn time。
- Gate transaction time。
- % exceptions resolved before trouble window。
- Manual touches per exception。
- TOS/OCR data correction rate。
- Rehandles / container not found。
- Dwell time for exception containers。
- Avoided D&D days。
- Disputed invoice value。
- Damage claim cycle time。
- API latency / uptime / audit completeness。

## Competition

YardLoop 不替代现有系统，而是拥有 exception lifecycle。

- Kaleris / Navis：TOS 主系统强；YardLoop 做现场异常、低置信度事件、证据包和回写。
- Tideworks / TBA / INFORM / RBS：运营计划和执行系统强；YardLoop 补视觉异常、人工复核和跨系统证据层。
- Camco / CERTUS / Visy / ABB：闸口、吊机、堆场 OCR 强；YardLoop 把 bad reads 变成可关闭任务。
- Kalmar / ZPMC / ABB / terminal automation：设备和自动化强；YardLoop 做跨设备事件图和 HIL 数据层。
- project44 / FourKites / Portcast / visibility platforms：可视化和运输决策强；YardLoop 聚焦码头现场的责任、证据和写回。
- Terminal Industries：计算机视觉切入 drayage/yard；YardLoop 聚焦 TOS/YMS 写回、exception workflow 和 LeRobot edge training。
- 中国智慧港生态：大型港口自研和集成能力强；YardLoop 以私有化、边缘视觉、事件图和跨系统异常闭环切入。

## Moat

壁垒是：

> port exception graph + closed-loop outcome data + TOS connectors + evidence ledger + edge deployment profile

会积累的资产：

- Exception graph：container、gate、yard、rail、hold、release、damage、seal、chassis、owner、close reason。
- Evidence ledger：图片/视频、OCR box、model version、operator decision、hash、WORM object、audit trail。
- Connectors：TOS/YMS、PCS、EDI、gate OCR、appointment、customs、chassis maintenance、portal。
- Vision dataset：雨夜、反光、污损箱号、遮挡、低角度、中文/英文标识、seal 和人工纠正。
- Ops playbook：gate、yard block、reefer、rail interchange、chassis pool、查验堆场和客户堆场 SOP。
- Edge profiles：AI Hub / QNN / QAIRT profile、离线缓存、弱网回写、signed model 和 rollback recipe。

## Architecture

### Edge Ingest

- Gate/Yard cameras。
- AGV / mobile robot camera。
- ONVIF / RTSP。
- RFID、RTK/UWB、driver app、manual photo。

### Qualcomm Edge Nodes

- RB3 Gen 2 做 gate lane demo。
- RB5 / IQ9 / Dragonwing IQ10 做 mobile robot 和多摄像头 yard edge。
- OCR、ALPR、seal、damage、safety-zone、container-tracking models。
- ONNX Runtime QNN / Qualcomm AI Hub optimized deployments。

### Fusion + Exception Engine

- ISO 6346 / BIC check digit validation。
- Expected-vs-actual match against TOS/YMS。
- Confidence gating。
- Multi-camera consensus。
- Low confidence 默认进入 review，而不是自动关闭。

### Evidence Ledger

- snapshots / video clips / model outputs / context hashes。
- append-only Merkle log。
- WORM object store。
- 每个事件保留 model version、device ID、timestamp source、operator decision。

### Action Orchestrator

- gate hold / release。
- inspection task。
- AGV / robot dispatch。
- TOS/YMS status writeback。
- operator approval。
- idempotent、versioned、reversible integration。

### Learning Loop

- corrected events and robot interventions -> LeRobotDataset。
- retrain / fine-tune。
- profile / compile for Qualcomm edge。
- staged OTA rollout。

## Competition Demo

3 分钟 demo：

1. Live yard twin 显示 3 条 lane、12 个箱模、TOS/YMS work orders 和正常 operations dashboard。
2. Truck 进入 lane A。闸口读到 `MSCU 663987 1`，TOS 期望 `MSCU 663987 6`。
3. YardLoop 高亮 OCR boxes、ISO 6346 check-digit failure 和 TOS mismatch；edge device 显示 cloud disconnected，证明本地推理。
4. 系统冻结 10 秒 clip、front/side snapshots、OCR confidence、lane ID、timestamp、TOS appointment 和 model version。
5. 生成 evidence envelope，显示 ledger hash。
6. Gate status 改为 `SOFT_HOLD`；dispatcher 看到 “wrong box or OCR conflict”。
7. Operator 选择 send mobile inspection；小车进入 geofenced inspection zone，补拍 door-side code 和 seal image。
8. YardLoop 确认 side code 与 gate-side OCR 不一致，并检测 seal missing / seal mismatch。
9. 人工批准后，回写 mock TOS/YMS：Gate Hold、Inspection Required、Exception Evidence URI、Suggested Yard Task。
10. Operator 标注 root cause：gate OCR glare + missing seal；系统生成 LeRobot episode 和 Qualcomm profile 队列。

安全控制：

- Demo 小车在 geofenced corridor 内运行，有 speed caps、E-stop、person detection、manual takeover。
- YardLoop 提议动作；TOS/YMS 执行被批准的状态变化。
- 网络中断时 edge node 保持本地推理，降级为 hold/manual inspect。
- 不承诺 100% OCR 准确率；低置信度必须进入人工复核。

## Why Qualcomm

YardLoop 是 Qualcomm edge AI + industrial logistics 的港口样板：

- 港场是物理世界 AI，不是纯 SaaS dashboard。
- 多摄像头：闸口、堆场杆位、车载、小车和吊具摄像头在现场融合。
- 低延迟：箱号、车牌、封签、箱损、人员闯入和低置信度事件优先本地判断。
- 弱网和私有数据：港场视频、车牌、客户货物和运营数据默认不全量上云。
- 私有网络：5G / Wi-Fi 6E、store-and-forward、站内边缘节点协同。
- 硬件路径：RB3 Gen 2 做桌面 demo；RB5 / IQ9 / Dragonwing IQ10 做 mobile + multi-camera production。
- 模型路径：AI Hub、QNN、QAIRT、ONNX Runtime QNN EP 让模型可 profile、可回滚、可区域部署。

Qualcomm 可以把 YardLoop 做成 edge AI + industrial logistics 的标杆 reference workflow。

## Ask

比赛阶段需要：

- RB3 Gen 2 / RB5 / Vision Kit 或 Dragonwing dev kit。
- mock TOS/YMS API。
- 20-50 个箱模或真实匿名照片样本。
- 闸口照片、异常状态机、复核规则。
- 一个小车 / AGV / 桌面移动平台。
- 2 个港口、内陆港、堆场、chassis pool、TOS/YMS 集成商或港口自动化 SI 试点引荐。

90 天目标：

> 跑通一个 Qualcomm-powered gate exception closure demo，把核心异常处理时长降低 30%，集卡周转改善 15% 作为试点目标。

## Claims To Avoid

- 不说替代 TOS/YMS。
- 不说建设全自动码头。
- 不说 100% OCR 准确率。
- 不承诺消除所有 D&D 费用。
- 不承诺适用于所有港口安全规则。
- 不默认上传港场原始视频、车牌或客户货物数据到境外云。
- 不声称获得港口、承运商、海关或 Qualcomm 官方认证，除非真实取得。

## Sources

- World Bank TEU data：https://data.worldbank.org/indicator/IS.SHP.GOOD.TU
- UNCTAD Review of Maritime Transport 2025 chapter 1：https://unctad.org/system/files/official-document/rmt2025ch1_en.pdf
- UNCTAD Review of Maritime Transport 2025 chapter 4：https://unctad.org/system/files/official-document/rmt2025ch4_en.pdf
- Container terminal automation：https://porteconomicsmanagement.org/pemp/contents/part6/terminal-automation/fully-semi-automated-container-terminals-total-hectares/
- World Bank CPPI 2024：https://www.worldbank.org/en/topic/transport/publication/cppi-2024
- Schedule reliability：https://safety4sea.com/sea-intelligence-global-schedule-reliability-rises-to-64-7-in-may/
- Drewry cancelled sailings tracker：https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/cancelled-sailings-tracker
- FMC detention and demurrage：https://www.fmc.gov/detention-and-demurrage/
- FMC billing rule：https://www.federalregister.gov/documents/2024/02/26/2024-02926/demurrage-and-detention-billing-requirements
- China TEU source：https://news.cctv.com/2026/01/30/ARTIN61RWbydYeeeXJAcEX1t260130.shtml
- Shanghai Port TEU：https://www.news.cn/fortune/20260107/cfb63b2935e84960bfd4d28883e5c253/c.html
- Ningbo-Zhoushan TEU：https://local.cctv.com/2026/01/05/ARTIOeFxGf2BBZm1FA5hRk0A260105.shtml
- China smart port policy：https://xxgk.mot.gov.cn/jigou/syj/202312/t20231204_3961959.html
- Rail-water intermodal：https://www.mot.gov.cn/xinwen/jiaotongyaowen/202605/t20260525_4206185.html
- Customs facilitation：https://sw.gz.gov.cn/gkmlpt/content/10/10647/post_10647493.html
- Smart port-of-entry guidance：https://www.hlj.gov.cn/hljzqc/c100116/202409/c00_31774510.shtml
- Tideworks survey：https://tideworks.com/new-tideworks-survey-reveals-need-for-practical-data-accuracy-and-connectivity-at-marine-terminals/
- Kaleris TOS：https://kaleris.com/solutions/terminal-operating-system/container-terminals/
- Tideworks：https://tideworks.com/
- Camco：https://camco.be/container-terminals/
- CERTUS：https://certusautomation.com/
- Visy：https://visy.fi/industries/ports-and-terminals/
- Kalmar One：https://www.kalmarglobal.com/automation/kalmar-one-automation-system/
- Terminal Industries：https://terminal-industries.com/
- Seaboard GOS RFP：https://www.seaboardmarine.com/notices/request-for-proposals-container-terminal-gate-operating-system/
- Crowley Gate OCR RFP：https://www.crowley.com/crowley-procurement/
- TRB gate productivity data：https://onlinepubs.trb.org/onlinepubs/webinars/111117.pdf
- BIC check digit：https://www.bic-code.org/check-digit-calculator/
- DCSA Track & Trace：https://dcsa.org/standards/track-and-trace
- ONVIF Profile S：https://www.onvif.org/profiles/profile-s/
- Merkle logs：https://www.rfc-editor.org/info/rfc6962/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB5：https://www.qualcomm.com/developer/hardware/robotics-rb5-development-kit
- Qualcomm IQ9 ecosystem：https://www.qualcomm.com/developer/blog/2026/06/developers-guide-to-qualcomms-iot-ecosystem
- Qualcomm IQ10 robotics reference design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobot HIL-SERL：https://huggingface.co/docs/lerobot/en/hilserl
