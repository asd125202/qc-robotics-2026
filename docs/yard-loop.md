# YardLoop 港场异常闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

YardLoop 是面向港口、内陆港、集装箱堆场、铁路联运场和大型货主堆场的边缘视觉异常闭环平台：

> 把箱号、封签、损坏、底盘车、箱位和放行状态从现场事实变成可处理、可举证、可回写的操作闭环。

它不替代 TOS/YMS，也不卖“全自动码头”。它是现有港场系统之上的异常生命周期层：现场看见问题，系统生成任务，人工或机器人补证据，处理完成后回写。

## Problem

港场不是没有系统，而是现场异常没有闭环：

- TOS/YMS 记录计划、预约和箱位，但现场的箱号、封签、损坏、底盘车、查验 hold 和放行状态会偏离计划。
- 闸口 OCR、堆场摄像头、吊机、拖车、小车和人工巡检都能产生数据，但异常往往停留在截图、邮件、电话、对讲机和 Excel。
- D&D 费用、damage claim、chassis roadability、release proof 和客户投诉需要证据链，而不是单张照片。
- 港场自动化项目重，TOS 替换风险高；更短的商业路径是先把高频异常流程闭环。

买方痛点：

- 码头运营团队：闸口拥堵、低置信度 OCR、错位、rehandle 和放行延迟。
- 船公司 / 承运商：D&D 争议、箱损责任、放行证明和客户投诉。
- chassis pool / 车队：底盘车 roadability、维修责任和照片证据。
- 内陆港 / 铁水联运场：铁路、卡车、仓库和码头系统交接复杂，责任更容易断裂。
- 大型货主 / 3PL 堆场：自有堆场也会产生滞留、错箱、损坏和查验延迟。

## Why Now

时机来自四个变化：

- FMC 披露，9 家海运承运人在 2020-04 至 2025-03 收取约 154 亿美元 detention / demurrage 费用；监管也强化了相关账单规则。费用争议需要更好的现场证据。
- 行业资料中常见 detention / demurrage 为 75-300 美元 / container / day。一个异常箱子每天都在变贵。
- UNCTAD 长期指出全球贸易量大部分通过海运，红海、巴拿马运河、港口拥堵和区域波动会把港场异常放大到供应链。
- GAO 对港口自动化的研究显示，闸口、堆场、岸桥和水平运输自动化正在成为美国大型集装箱港口的重要议题。自动化越多，越需要统一异常语言。
- 中国上海、宁波舟山、深圳、青岛、天津等港口长期推进智慧港口、自动化码头和 5G 港口；大型港口已有系统，机会在跨系统现场事实层。
- 多摄像头 OCR、低照度视觉、私有 5G、端侧推理和区域云训练成熟，使“小步快跑”的异常闭环比过去可行。

## Insight

港场自动化的第一桶金不是无人码头，而是异常闭环。

YardLoop 的非显而易见判断：

> 港口客户不一定愿意先重建 TOS、吊机或水平运输，但愿意为更短的异常处理、更清楚的费用责任和更可信的放行证明付钱。

从一个 gate lane 和一个 yard block 开始，就可以跑通：

- 现场事实采集。
- 异常判定。
- 人工复核。
- 任务分派。
- 证据包生成。
- TOS/YMS 回写。
- HIL 数据沉淀。

## Solution

YardLoop 是港场现场事实到 TOS/YMS 的异常操作层：

1. 接入闸口 OCR、堆场杆位相机、车载相机、小车/AMR、RTK/UWB、RFID、人工手机照片。
2. 端侧识别箱号、封签、箱损、底盘车状态、箱位和低置信度事件。
3. 对比 TOS/YMS 的预约、计划箱位、hold、release、inspection status 和历史照片。
4. 生成 exception case：类型、责任人、SLA、证据要求、复核按钮和回写目标。
5. 调度人工、巡检小车或固定摄像头补证据。
6. 形成 proof pack：进出闸照片、damage/seal/chassis card、时间戳、复核记录、处理动作。
7. 异常关闭后回写 TOS/YMS。
8. OCR 失败、遮挡、雨夜、坏角度和人工纠正进入 LeRobot HIL。
9. 中国版在阿里云 / 华为云 / 腾讯云 / AutoDL / 私有云训练；海外版在 Runpod / Lambda / Modal / Paperspace / AWS / Azure 训练。
10. 模型经 AI Hub / QNN / QAIRT / ONNX Runtime QNN EP profile 后回到 Qualcomm edge。

## Product Workflow

1. 导入 yard map、TOS/YMS API、gate lane、yard block、container list、appointment、hold/release status。
2. 闸口相机识别箱号、车牌、底盘车、封签和箱体照片。
3. 低置信度 OCR 或封签异常生成 case。
4. YardLoop 对比计划箱位和实际箱位，发现错位或未放行。
5. 巡检小车或固定摄像头补拍 damage / seal / chassis proof。
6. 人工复核并选择处理动作：放行、查验、维修、补证、拒收、重新定位。
7. 系统自动生成 dispute packet 或 release proof。
8. 状态回写 TOS/YMS，并通知客户 portal 或内部调度。
9. 坏角度、遮挡、雨夜、误识别和人工纠正导出为 LeRobot episode。
10. 区域云训练后生成 edge model artifact，部署到 gate/yard edge nodes。

## Market Wedge

第一市场不是“所有港口”，而是能在 6-8 周内证明异常价值的高频流程：

- 集装箱码头：gate OCR low confidence、damage/seal proof、release hold。
- 内陆港 / 铁水联运：系统交接多，责任链长。
- chassis pool：底盘车 roadability、维修任务和照片证据。
- 大型货主 / 3PL 堆场：自有堆场也有 D&D、错箱、查验和 damage claim。
- 冷链港场：reefer plug、setpoint、门封和温控证明。

中国版：

- 上海、宁波舟山、青岛、天津、深圳、广州、厦门等港口和内陆港。
- 不替换既有智慧港系统，先做 edge exception layer、私有部署、TOS/YMS connector 和数据本地化。
- 视频、车牌、货物、客户数据默认不上境外云；模型训练在中国本地云或私有云。

海外版：

- 中小码头、内陆港、rail intermodal yard、chassis pool、drayage yard、大型进口商堆场。
- 通过 TOS/YMS 集成商、港口自动化 SI、闸口 OCR 厂商、chassis 维护服务商和保险/理赔伙伴进入。

## Business Model

收入模型：

> paid pilot + site subscription + lane/block modules + scan/exception volume + proof/dispute reporting

建议价格：

- 海外付费试点：30k-90k 美元，6-8 周，1 个 gate lane + 1 个 yard block。
- 中国付费试点：30-100 万元，包含私有部署、edge node、mock/真实 TOS 接口和异常 SOP。
- 站点订阅：8k-25k 美元 / yard / month，按 lane、block、摄像头、小车、connector、报告层级收费。
- 按量加价：per scan、per closed exception、per damage proof、per chassis inspection、per dispute packet。
- 硬件/摄像头/小车可打包，也可接入现有设备。

试点 KPI：

- gate cycle time。
- OCR exception rate。
- low-confidence review time。
- D&D exception resolution time。
- damage claim cycle time。
- chassis roadability issue closure。
- release latency。
- yard rehandle。
- proof packet completeness。
- edge latency / FPS / NPU utilization。

## Go-To-Market

第一阶段：

1. 找一个愿意做 6-8 周试点的中小港场、内陆港、chassis pool 或大型货主堆场。
2. 选一个 gate lane 和一个 yard block。
3. 接入摄像头、小车或手机补证，先跑 mock TOS，再接真实 API。
4. 聚焦 2-3 个异常：低置信度 OCR、damage/seal proof、release hold。
5. 用费用争议减少、处理时间缩短和 proof 完整率验收。

第二阶段：

- 扩到更多 gate lanes、yard blocks、reefer lanes、chassis shop、rail interchange。
- 接入更多固定摄像头、小车、车载相机和 OCR 点位。
- 与 TOS/YMS、客户 portal、TMS/WMS、保险/理赔系统集成。
- 做多站点 container-event graph。

## Competition

YardLoop 不替代现有系统，而是补上异常生命周期层：

- Kaleris / Navis：TOS 主系统强；YardLoop 做现场事实、低置信度事件、证据包和回写。
- Tideworks / TBA / INFORM / RBS：运营计划和执行系统强；YardLoop 补视觉异常和人工复核层。
- Camco / OCR 厂商：闸口和吊机 OCR 强；YardLoop 把 OCR 失败、箱损、封签和底盘车异常变成任务。
- Kalmar / ZPMC / ABB / terminal automation：设备和自动化强；YardLoop 做跨设备事件图和 HIL 训练数据。
- Terminal Industries：计算机视觉切入 drayage/yard；YardLoop 聚焦 TOS/YMS 写回、exception workflow 和 LeRobot edge training。
- 中国智慧港生态：大型港口自研和集成能力强；YardLoop 以私有化、边缘视觉、事件图和跨系统异常闭环切入。

## Moat

壁垒不是某个 OCR 模型，而是：

> container-event graph + TOS/YMS connector + proof workflow + HIL data + edge deployment profile

会积累的资产：

- 每个箱子的事件时间线：gate、yard、rail、hold、release、damage、seal、chassis、proof。
- TOS/YMS connector 和字段映射。
- D&D、damage claim、chassis roadability、release proof 的证据模板。
- 雨夜、污损箱号、反光、遮挡、低角度、箱损和人工纠正的视觉数据集。
- gate、yard block、reefer、rail、chassis pool 的 SOP 模板。
- Qualcomm edge profile、离线缓存、弱网回写、模型回滚和部署 recipe。

## Architecture

### Edge Capture

- Gate OCR cameras、yard pole cameras、vehicle-mounted cameras、AMR/small rover、RTK/UWB、RFID、QR/barcode、mobile app。
- 端侧输出 container_id、confidence、seal_state、damage_state、chassis_state、slot、event_time、camera_pose。

### Exception Engine

- 对比 TOS/YMS：appointment、planned_slot、hold/release、inspection_state、last_seen、customer。
- 生成 exception case：type、severity、owner、SLA、evidence_required、review_status、writeback_target。

### Robot / Patrol Layer

- ROS 2 + Nav2 waypoint patrol。
- Yard geofence、slow zone、human override、manual review。
- 安全控制本地执行，学习策略只建议补拍角度、巡检点和复核优先级。

### TOS/YMS Bridge

- Case -> TOS/YMS status update。
- 同步 release proof、damage proof、slot correction、chassis issue、hold close reason。
- 支持 mock API、CSV、message queue、existing integration partner。

### Training Loop

- LeRobot HIL records：image、camera pose、event fields、human correction、task outcome。
- 统一 contract：dataset_uri、sensor_schema、policy、target_board、eval_suite、export_runtime=qnn/qairt。
- 中国训练：阿里云 PAI、华为 ModelArts、腾讯 TI-ONE、AutoDL、私有 GPU。
- 海外训练：Runpod、Lambda、Modal、Paperspace、AWS、Azure。
- AI Hub / QNN / QAIRT profile 后部署到 RB3 / RB6 / QCS8550 / Dragonwing edge nodes。

## Competition Demo

3 分钟 demo：

1. 桌面堆场地图上有 gate lane、yard block、hold area 和 release lane。
2. 摄像头扫描一个箱模，OCR 低置信度并触发 exception。
3. 小车巡检发现该箱在错误 block，同时检测到 damage/seal 异常。
4. Dashboard 生成 case：箱号、位置、照片、confidence、责任人、SLA、复核按钮。
5. 人工确认后，系统补拍一个角度并生成 proof pack。
6. 一键回写 mock TOS/YMS：status = verified release 或 hold closed。
7. 坏角度/OCR 失败片段导出 LeRobot episode。
8. 展示中国/海外云训练队列和 QNN/QAIRT edge artifact。

演示重点：

> 不是机器人在堆场跑了一圈，而是一个箱子的异常从“看见”变成“可放行、可举证、可回写、可训练”。

## Why Qualcomm

YardLoop 是 Qualcomm edge AI 的强适配场景：

- 多摄像头：闸口、杆位、车载、小车、吊具摄像头同时产生数据。
- 低延迟：箱号、封签、箱损和底盘车状态需要现场判断。
- 弱网可用：港场网络和系统连接不稳定时，edge node 要缓存事件并安全回写。
- 私有数据：视频、车牌、客户货物、场站运营数据默认不应全量上云。
- 硬件路径：RB3 Gen 2 做桌面 demo；RB6 / QCS8550 / Dragonwing IQ 系列做多摄像头生产路线。
- 软件路径：AI Hub、QNN、QAIRT、ONNX Runtime QNN EP 支撑可 profile、可部署、可回滚 artifact。
- 生态路径：港场是机器人、小车、摄像头、私有网络和企业系统共同落地的高价值场景。

## Ask

比赛阶段需要：

- RB3 Gen 2 / RB6 / Vision Kit 或 Dragonwing dev kit。
- 一个 mock TOS/YMS API。
- 20-50 个箱模或真实匿名箱体照片样本。
- 一个 gate lane / yard block 的流程图。
- 一个内陆港、堆场、chassis pool、TOS/YMS 集成商或港口自动化 SI 作为设计伙伴。
- AI Hub / QNN profile 支持。

## Claims To Avoid

- 不说替代 TOS/YMS。
- 不说建设全自动码头。
- 不说 100% OCR 准确率。
- 不承诺消除所有 D&D 费用。
- 不承诺适用于所有港口安全规则。
- 不默认上传港场原始视频、车牌或客户货物数据到境外云。
- 不声称获得港口、承运商、海关或 Qualcomm 官方认证，除非真实取得。

## Sources

- FMC detention and demurrage：https://www.fmc.gov/detention-and-demurrage/
- FMC demurrage and detention billing requirements：https://www.federalregister.gov/documents/2024/02/26/2024-02926/demurrage-and-detention-billing-requirements
- D&D fee explainer：https://terminal-industries.com/all-resources/detention-and-demurrage-key-shipping-fees-explained-clearly
- UNCTAD maritime transport：https://www.unognewsroom.org/teleprompter/en/2840/unctad-press-conference-review-of-maritime-transport-24-september-2025/8512
- GAO port automation report：https://www.gao.gov/assets/d24106498.pdf
- Kaleris TOS：https://kaleris.com/solutions/terminal-operating-system/
- Tideworks TOS：https://tideworks.com/
- Camco solutions：https://camco.be/solutions/
- Kalmar automation：https://www.kalmarglobal.com/automation/
- Terminal Industries：https://terminal-industries.com/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/QNN_general_overview.html
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- Nav2：https://docs.nav2.org/
- Open-RMF：https://www.open-rmf.org/
