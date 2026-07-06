# InfraLoop 设施巡检闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

InfraLoop 是面向数据中心、私有变电站、BESS、泵站、工业园区、能源设施 O&M 团队的关键设施巡检闭环平台：

> 把机器人、无人机、固定摄像头和人工巡检看到的现场变化，变成当天可处理的工单、复检证据和资产级历史记忆。

它不替代 Maximo / SAP / CMMS。它卖的是现场事实层：发现异常、生成任务、验证修复、沉淀资产历史，并把失败片段送入 LeRobot HIL 与 Qualcomm edge 模型迭代。

## Problem

关键设施客户不是缺机器人，而是缺“现场事实进入维修闭环”：

- 现场照片、热成像、声音、气体、仪表读数和人工备注散落在承包商 PDF、微信群、巡检表和文件夹里。
- CMMS / EAM 存工单和资产，但往往没有同一资产的 before/after 证据、热图、位置、置信度和复检状态。
- 机器人、无人机和固定摄像头能采集数据，但采集完之后很少直接进入工单、维修、复检和下一次路线优化。
- 停机、二次确认、漏检、错误优先级、保险/合规证据不足，才是真正付费痛点。

买方包括：

- 数据中心设施负责人：关心 UPS、冷机、发电机、BESS、配电室、热漂移和客户 SLA。
- 工业园区 / 私有变电站 O&M：关心资产台账、巡检覆盖、异常处理和承包商管理。
- 电厂 / IPP O&M：关心少人值守、例行巡检、设备可靠性和停机风险。
- 水务 / 泵站 / 冷链辅助设施：关心泵阀、漏水、仪表、振动、温湿度和维修证据。
- 保险、合规、审计和客户成功团队：关心可追溯证据，而不是又一个机器人后台。

## Why Now

时机来自四个方向同时出现：

- IEA《Energy and AI》预计全球数据中心用电 2030 年约 945 TWh，较 2024 年翻倍以上。数据中心和电力设施的现场可靠性会变成更大的经济问题。
- Uptime 2026 outage analysis 显示，57% 受访者的最近一次重大故障成本超过 10 万美元，约五分之一超过 100 万美元。停机风险足够大，足以支持高价值运维工具。
- MaintainX 2026 报告显示，50% 维护团队把低于 40% 的时间花在计划性工作上，39% 受访者称过去一年非计划停机成本增加。
- NFPA 70B 2023 从推荐实践转为标准，强化了电气维护、记录和可执行维护程序的重要性。不同司法辖区的采用方式不同，但“记录化、计划化、可证明”的方向明确。
- 机器人巡检商业化进入大额订单：Gecko Robotics 2025 年达到 12.5 亿美元估值；NAES 与 Gecko 宣布超过 1 亿美元的能源设施合作；Energy Robotics 披露已完成 100 万次以上巡检；Qualcomm Ventures 投资 ANYbotics。
- 中国能源数字化智能化政策、配电网高质量发展行动方案、能源 AI 高价值场景政策，都在推动电力设备状态评价、缺陷诊断、少人值守和智能运维。

## Insight

赢的不是最会走路的机器人，而是最短的异常闭环。

过去的巡检平台常把“机器人到了哪里、拍了什么”当产品核心。InfraLoop 的判断是：

> 设施负责人付费买的不是巡检轨迹，而是更快的异常确认、更明确的责任、更少的二次出车、更完整的修复证据和可复用的资产历史。

产品需要把每个资产变成 daily heartbeat：

- 正常。
- 需要复核。
- 已创建工单。
- 维修中。
- 已复检。
- 下次路线或模型需要改进。

## Solution

InfraLoop 是关键设施的现场事实层：

1. 从资产清单、风险等级、历史异常和巡检点生成路线。
2. 用机器人、无人机、固定摄像头、手持设备和人工巡检采集现场事实。
3. 在 Qualcomm edge 上做热、视觉、仪表、声音、气体和路线异常初筛。
4. 将异常卡片转成有资产 ID、位置、严重度、证据、复核按钮和 SLA 的工单。
5. 写入 Maximo / SAP / ServiceNow / 国产 CMMS / mock API。
6. 技术员处理后，机器人或固定摄像头复检，形成 before/after 证据。
7. 堵路、坏视角、低置信度、人工接管和失败片段进入 LeRobot HIL 数据集。
8. 中国版在阿里云 / 华为云 / 腾讯云 / AutoDL / 私有云训练；海外版在 Runpod / Lambda / Modal / Paperspace / AWS / Azure 训练。
9. 模型经 AI Hub / QNN / QAIRT profile 后回到 Qualcomm edge。

## Product Workflow

1. 导入 asset list、inspection points、risk level、route、restricted zone、slow zone 和复检要求。
2. 调度机器人、无人机、固定摄像头或人工巡检任务。
3. 采集 RGB、热成像、声学、气体、2D/3D LiDAR、仪表 OCR、人工照片和技术员备注。
4. Edge model 将当前资产状态与历史基线和上一次巡检结果对比。
5. 生成 anomaly card：位置、资产 ID、截图、热图、置信度、严重度、人工复核按钮。
6. 一键创建 Maximo / SAP / CMMS work request。
7. 技术员修复并记录处理动作。
8. 机器人或固定摄像头复检，验证状态并回写工单。
9. blocked route、bad viewpoint、failed meter read、teleop recovery 进入 LeRobot HIL。
10. 区域云训练后导出 QNN/QAIRT artifact，部署到 edge fleet。

## Market Wedge

首批切入：

- 数据中心：电气室、UPS、发电机、冷机、BESS、热通道、DCIM/CMMS 连接。
- 私有变电站 / 工业园区：资产台账清晰、停机成本高、巡检频次稳定。
- 电厂 / IPP O&M：有成熟运维预算和少人值守压力。
- 水务 / 泵站：泵阀、仪表、漏水、振动、异响和远程站点。
- 冷链 / 仓储辅助设施：温控设备、配电、机房和能耗异常。

中国版：

- 国网 / 南网生态、发电集团、IDC、工业园区、轨交、隧道、水务、石化。
- 不从“替换既有机器人”开始，而从统一平台、资产历史、私有部署和现有设备集成切入。
- 重点强调数据安全、视频最小化、私有云、国产云适配和本地系统集成。

海外版：

- 区域数据中心、colocation、IPP、工业设施、BESS、utility contractor、facility O&M。
- 通过电气/红外巡检承包商、CMMS/EAM 集成商、机器人 OEM 和 O&M 服务商进入。

## Business Model

收入模型：

> paid pilot + site SaaS + EAM/CMMS integration + edge node + cloud training + evidence reports

建议价格：

- 海外付费试点：25k-75k 美元 / site，6-8 周，验证一条高价值巡检路线。
- 中国付费试点：20-80 万元 / 站点，包含私有部署、边缘节点、mock CMMS 或现有系统连接。
- Site SaaS：3k-15k 美元 / site / month，按资产数量、路线数量、摄像头/机器人数量和报告层级收费。
- 中国站点 license：按站点、资产包、巡检路线、私有云、数据安全包、系统接口和实施服务收费。
- 硬件/机器人/承包商可做 pass-through 或联合方案，不做第一收入核心。

试点 KPI：

- anomaly-to-work-order time。
- time-to-verified-fix。
- critical anomalies found。
- contractor re-visit reduced。
- proof latency。
- planned work ratio。
- asset history completeness。
- inspection coverage。
- human review rate。
- edge FPS / latency / NPU load。

## Go-To-Market

第一阶段：

1. 找一个有明确资产台账和停机成本的站点。
2. 选择 20-50 个巡检点和一条高价值路线。
3. 部署小型巡检机器人 / 固定相机 / 手持设备 + mock CMMS。
4. 用 6-8 周证明异常发现、工单创建、维修复检和证据报告。
5. 向设施负责人、运维主管、风险/保险和财务同时展示价值。

第二阶段：

- 扩到全站关键路线。
- 加入更多传感器和机器人/无人机品牌。
- 与 Maximo / SAP / ServiceNow / 国产 CMMS / DCIM / BMS 对接。
- 通过 O&M 服务商、红外巡检承包商、CMMS 集成商和机器人 OEM 渠道复制。

不建议一开始直接硬闯大型受监管公共电网采购，除非通过既有 O&M 或集成商通道进入。

## Competition

InfraLoop 不替代机器人、无人机、CMMS 或数字孪生，而是做异常生命周期层。

- ANYbotics / Boston Dynamics Spot / Unitree B2 / DEEP Robotics：移动机器人强；InfraLoop 做跨设备异常、工单、复检和训练闭环。
- Energy Robotics / Korial：巡检平台强；InfraLoop 聚焦资产级现场事实到 EAM/CMMS 的闭环。
- Percepto / Skydio / DJI Enterprise：无人机和监管场景强；InfraLoop 连接空中证据与地面维修。
- Gecko Robotics：专用检测和基础设施 AI 强；InfraLoop 从日常 O&M 闭环切入，避免过重专用检测硬件。
- Flyability / Asylon / ExRobotics / Taurob / ULC：特定机器人和场景强；InfraLoop 做工单和资产历史层。
- IBM Maximo / SAP EAM / ServiceNow：企业系统主账本强；InfraLoop 提供现场事实、异常卡片和复检证据。
- 中国电力巡检生态：亿嘉和、申昊、国网/南网相关体系、云深处、优艾智合、大疆、宇树等已有设备；InfraLoop 可做统一事实层和训练闭环。

## Moat

壁垒不是某台机器人，而是：

> asset-level memory + EAM connectors + risk taxonomy + verified repair evidence + edge training profile

会积累的资产：

- 每个资产的正常基线、热图历史、声音历史、仪表读数、维修记录和复检证据。
- Maximo / SAP / ServiceNow / 国产 CMMS connector、字段映射、状态同步和报告模板。
- 数据中心、BESS、变电站、泵站、电厂、冷链、轨交等行业 severity taxonomy。
- blocked route、bad viewpoint、failed read、teleop recovery 的 LeRobot HIL 数据集。
- Qualcomm edge profile、QNN/QAIRT artifact、rollback recipe 和设备级 benchmark。
- 私有部署、视频最小化、区域云训练和数据合规 playbook。

## Architecture

### Facility Map + Asset Graph

- 导入 CAD / floor plan / drone map / robot map / asset list。
- 每个巡检点绑定 asset_id、sensor_needed、risk_level、route、last_result 和 verification_rule。
- 用 RMF / facility semantics 表达门、电梯、闸机、禁行区和慢行区。

### Edge Runtime

- ROS 2 topics、Nav2 waypoint patrol、camera/thermal/audio/gas/LiDAR topics。
- 安全控制和导航留在本地 deterministic stack。
- 学习策略只建议 recovery action、viewpoint 或 task priority，不直接绕过安全控制。

### Anomaly Engine

- 与历史基线对比，而不是承诺“预测所有故障”。
- 输出 anomaly_type、severity、confidence、asset_id、evidence_uri、review_required。
- 低置信度事件默认进人工复核。

### CMMS / EAM Bridge

- anomaly event -> work request。
- 字段：asset ID、location、evidence、severity、suggested action、review status、verification rule。
- 工单状态同步回 InfraLoop：open、assigned、in_progress、fixed_pending_verify、verified、reopened。

### Training Loop

- 统一 contract：dataset_uri、policy、sensor_schema、target_board、eval_suite、export_runtime=qnn/qairt。
- 中国训练：阿里云 PAI、华为 ModelArts、腾讯 TI-ONE、AutoDL 或私有 GPU。
- 海外训练：Runpod、Lambda、Modal、Paperspace、AWS、Azure。
- 训练产物经 AI Hub / QNN / QAIRT profile 后部署到 RB3 / RB6 / QCS8550 / Dragonwing 路线。

## Competition Demo

3 分钟 demo：

1. 打开设施地图，显示 restricted zone、slow zone、door/gate mock、20-50 个巡检点。
2. 派发一条巡检路线，机器人开始 waypoint patrol。
3. 在泵/开关柜处检测到相对历史基线的热异常。
4. Dashboard 生成 anomaly card：last vs current、thermal map、location、confidence、human review。
5. 一键创建 mock Maximo / SAP / CMMS 工单。
6. 技术员标记处理，机器人复检并回写 verified。
7. 堵路或坏视角片段进入 LeRobot HIL export。
8. 展示 edge metrics：FPS、latency、NPU/CPU load、local/cloud mode、QNN/QAIRT artifact。

演示重点：

> 不是机器人巡了一圈，而是设施当天完成了一次可审计的自动交班。

## Why Qualcomm

InfraLoop 是 Qualcomm 在关键设施 O&M 里的强适配场景：

- 多传感器：RGB、热成像、声学、气体、LiDAR、仪表 OCR。
- 低延迟：异常识别、避障、低置信度判断和复检不能完全依赖云。
- 弱网可靠：站点内网络波动时仍要安全执行和缓存证据。
- 私有数据：关键设施视频、资产图和告警证据不适合默认全量上云。
- 硬件路径：RB3 Gen 2 做比赛原型，RB6 / QCS8550 / Dragonwing IQ 系列走生产路线。
- 软件路径：AI Hub、QNN、QAIRT、Qualcomm Robotics ROS / QIRP 支撑可 profile、可部署、可回滚 artifact。
- 战略信号：Qualcomm Ventures 对 ANYbotics 的投资说明工业巡检机器人是 Qualcomm 生态已经关注的现实市场。

## Ask

比赛阶段需要：

- RB3 Gen 2 / RB6 / Vision Kit 或 Dragonwing dev kit。
- 一个 mock Maximo / SAP / CMMS API。
- 一个设施地图、20-50 个巡检点、两周匿名读数或合成基线。
- 一个数据中心、私有变电站、工业园区、泵站或 O&M 设计伙伴。
- AI Hub / QNN profile 支持。
- 一个安全、非防爆、非高压实操环境的 demo 场景。

## Claims To Avoid

- 不说完全替代人工巡检。
- 不说零停机。
- 不说预测所有故障。
- 不说任何机器人都即插即用。
- 不说已经通过防爆、ATEX、Ex 或电力行业认证。
- 不说 EPA、NFPA、国网/南网或 Qualcomm 官方认证，除非真实取得。
- 不在第一版演示危险高压、易燃易爆或需要特种资质的现场。

## Sources

- IEA Energy and AI executive summary：https://www.iea.org/reports/energy-and-ai/executive-summary
- Uptime annual outage analysis 2026：https://intelligence.uptimeinstitute.com/resource/annual-outage-analysis-2026
- MaintainX State of Industrial Maintenance 2026：https://www.getmaintainx.com/state-of-industrial-maintenance-report
- NFPA 70B reliability and safety：https://www.nfpa.org/news-blogs-and-articles/blogs/2023/03/08/nfpa-70b-is-a-critical-tool-for-reliability-and-safety
- Gecko Robotics unicorn status：https://www.geckorobotics.com/news/gecko-reaches-unicorn-status
- NAES / Gecko $100M deal：https://www.naes.com/naes-and-gecko-announce-100m-deal-deploying-ai-and-robotics-to-transform-the-american-power-grid/
- Energy Robotics Series A / 1M inspections：https://www.climateinvestment.com/news/energy-robotics-secures-13-5-million-series-a-to-scale-critical-infrastructure-inspections-with-ai-robotics
- Qualcomm Ventures ANYbotics：https://www.qualcommventures.com/insights/blog/portfolio-watch-investing-in-anybotics-a-leader-in-ai-powered-industrial-inspections/
- Percepto EPA alternative test method：https://percepto.co/autonomous-ogi-drones-now-alternative-test-method-for-epa-subpart-ooooa-oooob/
- 国家能源局能源数字化智能化意见：https://zfxxgk.nea.gov.cn/2023-03/28/c_1310707122.htm
- 国家能源局配电网高质量发展行动方案：https://zfxxgk.nea.gov.cn/2024-08/02/c_1310784260.htm
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/QNN_general_overview.html
- Qualcomm Robotics ROS：https://www.qualcomm.com/developer/project/robotics-ros
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- Nav2：https://docs.nav2.org/
- Open-RMF：https://www.open-rmf.org/
- IBM Maximo：https://www.ibm.com/products/maximo
- SAP EAM：https://www.sap.com/products/scm/asset-management-eam.html
