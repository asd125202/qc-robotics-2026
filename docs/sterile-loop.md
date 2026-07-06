# SterileLoop 手术器械异常闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

SterileLoop 是给医院 CSSD/SPD、手术室和器械管理团队的托盘异常闭环系统：

> 用 Qualcomm 边缘视觉、扫码/RFID、清洗灭菌周期证据、人工确认和 LeRobot HIL，把缺件、错件、损坏、过期包、清洗/灭菌异常、外来器械延误和审计缺证在手术室付出分钟成本前关闭。

它不是基础器械追踪系统，也不是自动临床放行系统。它做的是 surgical tray exception closure。

## Problem

手术室不只需要知道托盘在哪里，更需要知道异常有没有在切皮前解决。

- 缺件、错件、破损、外来器械迟到、灭菌周期缺证、过期包和召回常常在 OR 前暴露。
- 人工视觉任务压力高：器械相似、反光强、托盘复杂、班次紧。
- 清洗批次、灭菌批次、BI/CI、UDI、责任人、替代件和最终使用记录不总是在一个异常包里。
- 事后事件上报低估风险，且无法支撑实时改进。

## Why Now

- BMC Surgery 2024 直接观察研究中，562 台手术里 147 台至少出现一个器械错误，占 26.16%。
- 同研究中，有延误数据的器械错误病例平均延误约 10.16 分钟。
- 手术室分钟成本/可计费分钟常用区间从约 46 美元/分钟到 153 美元/分钟。
- Aesculap/Ascendco 2025 benchmark 显示人误、器械丢失和库存准备缺口仍然是 SPD/OR 领导层痛点。
- Censis Assembly Copilot 证明计算机视觉终检已进入医院流程。
- 中国 WS/T 879-2025 CSSD 监测数据标准 2026-06-01 生效，强调采集、存储、共享、追溯和反馈。

## Insight

最小经营单元不是托盘，而是阻塞手术准备的异常。

> 医院不会先为“机器人自动放行器械”买单，但会为更少 OR 等待、更少找器械电话、更完整 CSSD 追溯、更快召回、更少重洗返工和更可信审计付费。

## Solution

SterileLoop 是手术器械工厂的闭环 QA 层。

1. 扫描托盘条码，加载模板、病例时间、医生偏好、外来器械和关键件清单。
2. 固定相机识别槽位、器械类别、缺件、错件、多件、低置信度和明显损坏候选。
3. 合并 UDI/扫码、RFID、清洗批次、灭菌批次、BI/CI、过期时间和人工备注。
4. 异常按手术时间、严重度、替代方案和责任人路由到 CSSD、OR、供应商或质控。
5. 人工签核后生成异常关闭包。
6. 低置信度、人工纠错、机器人指引和替代决策进入 LeRobot HIL。
7. 模型经 AI Hub / QNN / QAIRT profile 后部署到 Qualcomm edge。

## Product Workflow

状态对象：

- `tray_instance`
- `expected_item`
- `observation`
- `identifier_scan`
- `process_cycle`
- `exception`
- `closure_action`
- `evidence_packet`

第一版闭环：

1. Scan tray。
2. Inspect tray。
3. Open exception。
4. Assign owner。
5. Guide correction。
6. Fuse proof。
7. Human approve。
8. Export audit packet。
9. Feed HIL dataset。

## Market Wedge

第一批场景：

- 骨科 / 脊柱：器械多、外来包多、相似件多、手术分钟贵。
- 心外 / 神外：关键件缺失和替代方案确认需要更早、更可信闭环。
- 机器人手术：器械、附件、能量设备和专用托盘复杂。
- 外来器械：供应商到货、清洗、灭菌、放行、召回和归还链路跨组织。
- 中国三甲：手术量大，CSSD 标准化和智慧医院建设给本地部署留下预算入口。
- 独立 CSSD：需要证明回收、清洗、灭菌、发放和不合格反馈闭环。

## Business Model

收入模型：

> 90-day paid pilot + site subscription + edge inspection station + optional savings share

建议价格：

- 90 天试点：25k-75k 美元或 20-60 万元，覆盖一个手术线、一个 CSSD 站点或一个高风险托盘族。
- 站点订阅：按 OR 数、CSSD 站点、托盘量、视觉终检工位和集成模块收费。
- 硬件包：Qualcomm edge node、相机、扫码/RFID、光源和安全桌面机器人。
- 价值分成：对经验证的 OR 分钟节省、缺件追回、返工减少和审计人工压缩收取可选分成。

试点价值公式：

`Value = reduced instrument-delay minutes * OR cost/min + averted cancellations + reduced rework cycles + recovered missing instruments + audit/admin hours avoided + overtime avoided`

90 天 KPI：

- 器械/托盘异常每 100 台下降 20-30%。
- 相关延误分钟下降 20%+。
- 95%+ 阻塞手术异常当天关闭。
- 95%+ 异常 15 分钟内分配责任人/root cause。
- 文档完整率提升到 95%+。
- 超过 7 天缺件老化下降 50%。
- 重洗、返工、IUSS 触发事件下降 15-25%。

## Competition

SterileLoop 不替代已有系统：

- Censis / STERIS SPM / Aesculap Ascendco：追踪和流程强；SterileLoop 关闭阻塞手术的异常。
- ReadySet：外来器械和供应商协同强；SterileLoop 连接外来器械到 CSSD/OR 证据闭环。
- 新华医疗 / 老肯 / 安特速 / 第三方 CSSD：设备和服务强；SterileLoop 做跨系统异常关闭层。
- 医院物流机器人：运输强；SterileLoop 做托盘 QA、签核和异常数据。

## Moat

壁垒不是一张托盘照片，而是：

> tray exception graph + evidence dataset + standards connectors + edge profiles

会积累的资产：

- 托盘模板、器械、病例、医生偏好、外来包、清洗/灭菌周期和 OR 时间图谱。
- 视觉帧、扫码/RFID、设备周期、人工纠错、替代件和签核结果数据集。
- WS 310、T/WSJD 39、WS/T 879、UDI、FHIR Device、HIS/手麻/HRP 接口。
- 反光金属器械、多相机、弱网、本地隐私、QNN/QAIRT 和 HIL 数据。

## Architecture

### Edge Capture

- Fixed overhead RGB / RGB-D camera。
- Optional side camera。
- Polarized lighting and matte tray liner。
- Handheld 2D barcode/DataMatrix scanner。
- Optional UHF RFID mat。
- Tray barcode and mock UDI labels。
- Washer/sterilizer gateway over MQTT/REST/OPC-UA-style messages。

### Edge Runtime

- RB3 Gen 2 / QCS6490 / Dragonwing。
- `camera_node`。
- `tray_pose_node`。
- `instrument_detector_qnn`。
- `count_fusion_node`。
- `washer_gateway_node`。
- `exception_engine`。
- `robot_task_node`。
- `audit_api`。

### Training Loop

- HIL corrections and recovery actions。
- China raw data stays in hospital/on-prem/China cloud。
- Overseas raw data stays in overseas cloud。
- PyTorch/ONNX/TFLite -> AI Hub profile -> QNN/QAIRT package -> edge redeploy。

## Competition Demo

3 分钟 demo：

1. 操作员扫描 mock 托盘条码，加载 Ortho Minor Tray 模板。
2. overhead camera 检测托盘和器械，edge UI 显示 8/8 present。
3. 演示者移走一个 forceps，并加入一个错误 clamp。
4. edge inference 打开 missing forceps / unexpected clamp 异常。
5. 机械臂慢速指向缺失槽位或把错件移入异常盒。
6. 人工通过 LeRobot leader/gamepad 暂停、接管、纠正并恢复。
7. 操作员扫描替代器械条码，RFID mat 确认存在。
8. 模拟 washer/sterilizer gateway 发送 cycle pass。
9. 技师人工关闭；系统导出前后照片、扫码、周期、HIL 片段、模型版本和签核证据。

## Why Qualcomm

SterileLoop 是 Qualcomm 医疗边缘 AI 样板：

- 托盘图像、病例关联、人员记录和设备周期不能默认上公网云。
- 反光器械和多相机终检需要本地低延迟推理。
- CSSD 工作站需要弱网可用、审计日志和设备身份。
- AI Hub / QNN / QAIRT 让比赛 demo 能展示模型 profile、部署、运行和回滚链路。
- 商业上连接智慧医院、CSSD、器械供应、院内机器人和医疗 IoT。

## Ask

比赛阶段需要：

- RB3 Gen 2 / RB6 / Dragonwing dev kit。
- 固定相机、偏振光源、扫码枪、RFID mat、桌面机械臂。
- 泡沫/塑料器械、托盘模板、条码/UDI mock 标签、清洗/灭菌周期模拟器。
- 匿名托盘模板、器械清单、异常类型、替代规则、周期字段和审计字段样例。
- AI Hub / QNN profile 支持。

## Claims To Avoid

- 不说 SterileLoop 证明无菌。
- 不说自动放行手术托盘。
- 不替代 CSSD 技师或 OR 护士清点。
- 不承诺视觉唯一识别每把真实器械。
- 不检测微生物、污物残留、锋利度或微观损伤。
- 不声称 FDA/AAMI/医院生产就绪。
- 不声称可接所有清洗机、灭菌器、EHR 和器械系统。

## Sources

- BMC Surgery instrument errors：https://link.springer.com/article/10.1186/s12893-024-02407-1
- BMC HSR reprocessing cost：https://link.springer.com/article/10.1186/s12913-026-14663-3
- Aesculap / Ascendco benchmark：https://www.aesculapusa.com/content/dam/aesculap-us/us/website/aesculap-inc/healthcareprofessionals/surgical-asset-management-solutions/2025%20Surgical%20Asset%20Management%20Industry%20Benchmark%20Report%20Aesculap%20Ascendco%20Health%20UPDATE.pdf
- Censis Assembly Copilot：https://www.marketscale.com/industries/healthcare/censis-assembly-copilot-final-check-sterile-processing
- Robotic tray assembly research：https://arxiv.org/html/2602.01679v1
- WS/T 879-2025：https://www.nhc.gov.cn/fzs/c100048/202512/42af605da1384e038617405834641909/files/WST%20879%E2%80%942025.pdf
- T/WSJD 39-2023：https://www.qiluhospital.com/uploadfile/2023/0303/20230303174258890.pdf
- FDA UDI basics：https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/udi-basics
- FHIR Device：https://build.fhir.org/device.html
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/general_introduction.html
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
