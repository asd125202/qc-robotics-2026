# SiteLedger 工地实录 Pitch

更新时间：2026-07-06。施工机器人、智能建造政策、地产周期、BIM/CDE 标准、工地安全责任和客户采购节奏变化很快；真实商业材料应在提交前复核最新法规、项目招标、保险条款和设备认证。

## Core Thesis

SiteLedger 工地实录是施工现场的边缘 AI 记忆层：

> 让一台小型工地机器人把每天的放线、实测实量、巡检、进度、风险和人工复核变成可审计数据，再通过 LeRobot 和 Qualcomm edge 形成持续学习闭环。

它不是“机器人自动盖楼”，而是把施工机器人最先商业化的工作流产品化：

- Layout / 放线：把 BIM/CAD/图纸坐标转成现场可执行路线和标记。
- Reality capture / 实况采集：把每日照片、点云、路线、位置和时间统一成项目记忆。
- QA / 实测实量：把偏差、缺陷、遮挡、错位和返工风险变成结构化问题。
- Safety evidence / 安全证据：记录受限区域、通道占用、缺失护栏、材料堆放和人工复核。
- Payment evidence / 进度款证据：为业主、总包和分包生成可追踪的 work-in-place 记录。

一句话：SiteLedger 不替代工长，而是让工地每天留下机器可读、合同可用、训练可复用的现场记忆。

## Five-Thread Research Synthesis

### 1. Global Commercial Proof

施工机器人的成熟方向不是泛化施工，而是窄任务：Dusty、HP SitePrint、Rugged Robotics 的机器人放线；Built Robotics 的太阳能桩基；Canvas / JLG 的墙面处理；Hilti Jaibot 的 BIM 驱动钻孔；Advanced Construction Robotics 的钢筋绑扎；Spot / DroneDeploy / Exyn 的现实捕捉。买家语言不是“autonomy”，而是 rework、schedule、labor、safety exposure、documentation 和 predictable quality。

### 2. China Construction Lane

中国智能建造政策强，但地产周期压制民营商品房需求。中国版 SiteLedger 应优先面向央国企施工单位、公共建筑、机场、轨交、医院、学校、工业园区、城市更新、保障房和智能建造试点城市。最稳的第一楔子是：

> 实测实量 + 巡检 + 放线辅助。

它与政策、现场管理和验收证据直接相关，避免一开始进入重型施工机械和监管责任最复杂的环节。

### 3. Platform Business

商业产品不是卖一台车，而是卖项目级证据流：

- 海外版：layout RaaS、progress + QA subscription、safety evidence add-on、enterprise platform、rental channel。
- 中国版：智能建造示范项目包、机器人服务站、站点 SaaS、本地云/私有化、广联达/企业系统/钉钉/企微接入。
- 试点结构：6-8 周、一个楼层/区域/专业、固定 KPI、项目数据归客户、模型和平台 IP 归厂商。

### 4. Technical Architecture

SiteLedger 是 ground AMR / UGV，不是重型无人施工机械：

- Qualcomm RB3 Gen 2 / QCS6490 / RB6 / IQ10 路线作为边缘 AI 与多传感器主节点。
- 独立 safety MCU 处理急停、制动、watchdog、bumper、motor inhibit 和硬 geofence。
- ROS 2 / Nav2 / robot_localization / RTAB-Map 处理定位、路线、避障和站点地图。
- BIM/CDE 层接入 IFC、openCDE、BCF、图纸、点云、进度计划和工区。
- LeRobot 只负责 episode、teleop/HIL、训练和评估，不直接越过安全层控制电机。

### 5. Creative Product Shape

产品名：SiteLedger / 工地实录。

定位：

> 施工现场不是缺一个机器人，而是缺一层可审计、可复盘、可训练的现场记忆。

最强叙事不是“robot builds”，而是“one patrol becomes site memory; repeated patrols become a jobsite-specific robotics dataset”。

## Product Modules

### 1. SiteFrame

施工坐标和项目模型的可信框架：

- project_id、EPSG、竖向基准、IFC project GUID、RTK control points、BIM/CAD/document version。
- 把 `WGS84 / RTK -> site CRS -> map -> odom -> base_link` 的转换链固化为版本化证据。
- 如果控制点残差过高或图纸版本过期，阻止自主任务，只允许人工遥操作复核。

### 2. Daily Walk Robot

一台可服务化交付的小型工地机器人：

- 多相机、IMU、wheel odometry、RTK/GNSS、2D/3D LiDAR 或雷达。
- 支持室内 GPS-denied 与室外 RTK 场景切换。
- 每天按工区巡检路线执行进度拍摄、材料堆放、通道占用、护栏/洞口、放线点和实测实量任务。
- 断网时本地运行、本地缓存；网络恢复后同步证据和低优先级日志。

### 3. BIM / CDE Evidence Layer

把机器人看到的现场接回工程管理系统：

- IFC：连接 BIM 元素、专业、楼层、空间、计划位置和容差。
- BCF：每个问题变成 issue topic，带照片、位置、模型元素、严重程度和负责人。
- CDE：同步图纸、模型、点云、日巡报告和项目文档版本。
- PDF/CAD fallback：承认很多项目 BIM 不干净，支持图纸图片、CAD 和手工控制点对齐。

### 4. LeRobot BuildLoop

把现场复核变成训练资产：

1. 机器人巡检并提出进度、偏差或风险标记。
2. 现场工程师确认、驳回或修正。
3. 系统记录机器人观测、动作、位置、图纸版本、人工复核和结果。
4. episode 进入 LeRobot-compatible dataset。
5. 云端训练/评估后，模型通过 Qualcomm AI Hub / QNN / TFLite / ONNX Runtime 路线部署回边缘端。

### 5. Project Ledger

最终交付不是视频流，而是项目证据账本：

- 每日实录：位置、照片、路线、时间、工区、模型版本和检测结果。
- 进度证据：work-in-place、完成率、待复核、争议项和支付支持材料。
- 质量证据：偏差、缺陷、返工风险、NCR、闭环状态和责任分包。
- 安全证据：受限区域、通道占用、护栏/洞口、材料堆放和人工复核状态。
- 训练证据：接管片段、低置信度、误报、漏报、模型版本和发布门禁。

## China / Overseas Versions

中国版：

- 名称可用 `工地实录 SiteLedger` 或 `建造闭环 BuildLoop`。
- 首批客户：中建系统、上海建工、中铁/铁建、中交、中冶、机场/轨交/医院/学校/产业园业主、地方智能建造试点城市。
- 第一场景：实测实量、进度巡检、智能建造示范、放线辅助、质量安全巡查和数字档案。
- 默认本地云/私有化、数据不跨境、中文工单、钉钉/企微/飞书、广联达/BIM/成本系统接口。
- 不正面硬拼成熟抹灰、喷涂、地坪等施工本体，先做它们周围的地图、验收、调度和证据层。

海外版：

- 名称可用 `SiteLedger`。
- 首批客户：general contractors、trade contractors、owners、survey/layout crews、safety teams、rental companies。
- 第一场景：layout verification、progress capture、QA/punch、payment evidence、safety observations。
- 对接 Procore、Autodesk Construction Cloud、Oracle Primavera、DroneDeploy/Doxel/BCF/IFC 工作流。
- 以 6-8 周试点、robot-day、site/month、sq ft / point / issue pricing 进入。

## Competition Demo

比赛 demo 可以用小车和模拟工地完成：

1. 在网页中导入一张楼层图或轻量 IFC mock，标出通道、洞口、材料区、施工区和机器人路线。
2. 小型机器人或模拟器执行 daily walk，识别梯子、锥桶、材料堆、通道阻塞、错位标记或缺失检查点。
3. 触发一次低置信度事件：机器人暂停，请求人工复核。
4. 工程师在 dashboard 上确认或修正，系统生成 BCF-style issue 和 SiteLedger daily entry。
5. episode 被保存为 LeRobot 数据样本，展示训练 job、边缘 profile、签名 artifact 和灰度部署。
6. 切换“断网 / RTK 丢失 / 图纸过期 / dust camera”故障，展示本体安全降级和人工接管。

这个 demo 的强点是：三分钟内讲清“现场 -> 证据 -> 复核 -> 数据 -> 训练 -> Qualcomm edge 部署”。

## Why Qualcomm Should Care

施工现场是 Qualcomm 边缘 AI 的高价值场景：

- 多摄像头、多传感器、本地视觉和 SLAM 需求天然强。
- 工地网络不稳定，机器人不能依赖云端实时控制。
- 低功耗和热管理决定 robot-day economics。
- 5G / Wi-Fi / private network 支持现场数据同步、远程复核和多机器人 fleet。
- AI Hub / QNN / TFLite / ONNX Runtime profile 可以把模型部署证据转为客户信任。
- IQ10 RRD 的 full-stack robotics reference design 与施工机器人从 prototype 到 production 的路线高度匹配。

一句话：

> Qualcomm 不只是让工地机器人跑起来，而是让工地机器人把现场记忆变成可验证的商业数据。

## Claims To Avoid

- 不说“自动盖楼”“无人施工现场”“替代安全员/工长”。
- 不承诺事故减少、TRIR 改善、固定工期缩短或固定 ROI。
- 不声称支持所有 BIM/CDE/施工系统；真实项目需要 adapter 和现场 commissioning。
- 不让 LeRobot 策略直接控制安全关键运动。
- 不把 PPE/hazard 检测作为安全执法，只作为人工复核和证据辅助。
- 不做重型设备自动驾驶承诺，除非有明确认证和现场安全设计。

## Sources

- Dusty Robotics：https://www.dustyrobotics.com/
- Dusty field study：https://link.springer.com/article/10.1007/s41693-025-00163-z
- HP SitePrint：https://www.hp.com/us-en/printers/site-print/layout-robot.html
- HP SitePrint case studies：https://www.hp.com/us-en/printers/site-print/layout-robot/case-studies.html
- Rugged Robotics / The Robot Report：https://www.therobotreport.com/rugged-robotics-raises-9-4m-to-automate-construction-layout/
- Built Robotics solar piling：https://www.builtrobotics.com/solutions/solar-piling
- Blattner / Built Robotics：https://www.blattnercompany.com/news/blattner-and-built-robotics-announce-contract-to-improve-safety-in-solar-construction
- Canvas / Universal Robots：https://www.universal-robots.com/case-stories/canvas/
- JLG Canvas acquisition：https://www.jlg.com/en/press-releases/jlg-advances-job-site-of-the-future-vision-through-canvas-acquisition
- Hilti Jaibot：https://www.hilti.com/content/hilti/W1/US/en/business/business/trends/jaibot.html
- Advanced Construction Robotics TyBOT：https://www.constructionrobots.com/news/rebar-tying-robot-now-available-for-direct-purchase-as-robotics-firm-gains-industry-acceptance
- Boston Dynamics construction：https://bostondynamics.com/industry/construction/
- DroneDeploy Turner：https://www.dronedeploy.com/blog/turner-construction
- PCL / DroneDeploy：https://www.pcl.com/us/en/newsroom/press-releases/pcl-construction-and-dronedeploy-expand-partnership-to-standardize-reality-capture-across-1000-active-projects.html
- ABC 2026 workforce：https://www.abc.org/News-Media/News-Releases/abc-construction-industry-must-attract-349000-workers-in-2026-despite-macroeconomic-headwinds
- AGC workforce shortage：https://www.agc.org/news/2025/08/28/construction-workforce-shortages-are-leading-cause-project-delays-immigration-enforcement-affects
- Autodesk rework：https://www.autodesk.com/blogs/construction/reduce-construction-rework/
- BLS fatal occupational injuries：https://www.bls.gov/news.release/pdf/cfoi.pdf
- CPWR Focus Four：https://www.cpwr.com/research/data-center/the-construction-chart-book/interactive-7th/injuries-illnesses-health/focus-four/
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub：https://aihub.qualcomm.com/get-started
- ROS 2 Jazzy：https://docs.ros.org/en/jazzy/
- Nav2 keepout filter：https://docs.nav2.org/tutorials/docs/navigation2_with_keepout_filter.html
- MCAP ROS 2：https://mcap.dev/guides/getting-started/ros-2
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- buildingSMART IFC：https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/
- buildingSMART BCF API：https://github.com/buildingSMART/BCF-API
- buildingSMART openCDE API：https://github.com/buildingSMART/OpenCDE-API
- 中国智能建造政策：https://www.mee.gov.cn/xxgk2018/xxgk/xxgk10/202007/t20200729_791792.html
- 24 个智能建造试点城市：https://app.www.gov.cn/govdata/gov/202211/10/494092/article.html
- 中国房地产开发投资 2026-05：https://www.stats.gov.cn/sj/zxfb/202606/t20260616_1963950.html
- BrightMaster / Bozhilin：https://en.bm-robot.com/about.html
