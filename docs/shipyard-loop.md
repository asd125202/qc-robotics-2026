# ShipyardLoop 船厂生产证据闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

ShipyardLoop 是面向船厂、船修厂和海工制造基地的生产证据闭环：

> 把分段、焊缝、打磨、涂装、质检、返工和进度风险从对讲机与纸单，变成可验证、可追溯、可回写的 work package。

它不替代 PLM/CAD/ERP/MES，也不声称“全自动船厂”。它做的是现场事实层：机器人、人、传感器、工长、质检和计划系统之间的闭环。

## Problem

船厂不缺计划，缺现场真相：

- 分段到了没有？
- 焊缝做完了吗？
- 打磨覆盖够不够？
- 涂装是否在窗口内？
- 材料是否卡住？
- Inspector 有没有释放下一道工序？
- 哪个 NCR 正在阻塞排程？

答案常常散落在对讲机、照片、Excel、纸单、报工系统和老师傅脑子里。

痛点：

- 计划显示完成，现场可能仍在等材料、返工、检验或前序工序释放。
- 焊接参数、seam 图像、热图、打磨覆盖、涂装环境、DFT、NCR、inspector review 不在同一个证据包。
- 焊接/打磨/喷涂/扫描机器人能做单点自动化，但产出很少自然回到 work package、QA 和排程。
- 返工发现越晚，影响越大：交付、船级社、客户验收、试航和保修阶段代价都更高。

## Why Now

四个变化同时出现：

- 中国造船进入 backlog-driven delivery race。2026 Q1 中国手持订单量 322.30m DWT，同比增长 43.6%，新订单同比增长 195.2%，绿色船舶订单占比高。
- 美国船厂也有交付压力。GAO 报告显示，45 艘在建美国海军战斗舰中 37 艘截至 2024-09 延期。
- 焊接是核心成本池。NDIA/ETI 报告指出焊接约占造船工时的 25-28%，并明确提到 in-process weld monitoring 和 real-time QA data 的需求。
- 船厂正在购买机器人。HII/Path、HII/GrayMatter、HD Hyundai、Novarc、Navantia、中国 COOEC/GSI 等信号说明焊接、打磨、表面处理、涂装和 QA 自动化正在商业化。
- 数据和 AI 进入预算。美国海军 Ship OS / AI shipbuilding 投资、中国“AI + Manufacturing”、MIIT shipbuilding digital-transformation center 都表明船厂 AI 不再只是实验室话题。
- 边缘 AI、相机、私有 5G、ROS 2、LeRobot HIL、QNN/QAIRT 让现场 evidence loop 可用更轻的方式启动。

## Insight

数字船厂过去主要解决设计数据，下一步要闭环计划和现场之间的最后 100 米。

ShipyardLoop 的非显而易见判断：

> 船厂不会先为“全自动船厂”买单，但会为更快释放工序、更少返工、更完整 QA 证据和更可信的每日进度付钱。

因此第一版不是大而全的 shipyard OS，而是一个可验证的 work package evidence loop。

## Solution

ShipyardLoop 是船厂 work package 的现场证据层。

1. 导入工包、分段、焊缝、WPS/工艺、检验点、材料状态和排程。
2. 用边缘相机、HDR/weld camera、thermal、LiDAR/depth、工具电流/力、DFT/env probes、手机扫码和工长确认采集现场事实。
3. 模型识别 seam、打磨覆盖、表面缺陷、涂层覆盖、等待检验、安全区域和低置信度事件。
4. 生成 production evidence packet：before/after、路径、传感器帧、工具数据、人工复核、模型版本和处理建议。
5. NCR、返工、等待检验、材料缺失、前序阻塞和安全/许可异常进入任务队列。
6. 工长/质检确认处理动作。
7. 状态回写 MES/ERP/Ship OS/P6/报表。
8. 人工接管、低置信度、坏视角和返工结果进入 LeRobot HIL。
9. 中国版在阿里云/华为/腾讯/AutoDL/私有云训练；海外版在 Runpod/Lambda/Modal/Paperspace/AWS/Azure 训练。
10. 模型经 AI Hub / QNN / QAIRT / ONNX Runtime QNN EP profile 后回到 Qualcomm edge。

## Product Workflow

1. 导入 P6 / ERP / MES / Excel work package。
2. 给分段、焊缝、管段、电缆、涂层区域绑定 QR、视觉标识或 CAD 坐标。
3. 边缘相机、LiDAR、热图、工具遥测和手机补证采集现场证据。
4. 系统对比 as-planned vs as-built。
5. 低置信度、缺陷、返工、材料缺失、等待检验触发异常 case。
6. 工长/质检确认或修正。
7. 系统更新工包状态：planned、in_progress、blocked、rework、ready_for_inspection、released。
8. 状态和 QA packet 回写 MES/ERP/Ship OS。
9. 人工修正进入 LeRobotDataset v3。
10. 区域云训练后导出 QNN/QAIRT artifact 到 edge。

## Market Wedge

第一版不从全厂替换开始，先切高变化、高返工、高协同工序：

- 船修 / 改装 / retrofit：现场变化多、计划频繁变化、返工和客户验收压力高。
- 分段装配：block 到位、焊缝完成、尺寸偏差、等待检验和下一道工序释放。
- 焊接 QA：in-process weld monitoring、WPS 证据、参数、图像、inspector review。
- 打磨 / 表面处理 / 涂装：sanding、grinding、blasting、coating、DFT、返工窗口。
- 海工模块：FPSO、FLNG、平台导管架、TKY 节点、厚板和复杂重焊缝。

中国版：

- CSSC、COOEC/CNOOC、CIMC Raffles、杨子江、新时代、广船、江南、沪东、招商、南通/泰州/广州/上海/青岛/大连等集群。
- 私有云/本地化部署默认，工业数据分级、重要数据识别、模型训练区域隔离。
- 通过 MIIT shipbuilding digital-transformation center、CCS、Marintec China、船厂 SI 和机器人集成商进入。

海外版：

- 船修厂、工作船/驳船 yard、海工制造、二级供应商、Naval repair yards。
- 通过 NSRP、NDIA、AWS/CWI、AMPP/NACE、MES/PLM SI、焊接/涂装机器人厂商进入。

## Business Model

收入模型：

> paid pilot + annual yard subscription + edge node + integration + optional verified-savings success fee

建议价格：

- 90 天海外试点：75k-150k 美元，一个 yard / work package / trade，25-75 用户，轻量集成和 ROI 报告。
- 中国试点：50-150 万元，一个分段/工序/项目包，私有部署 + edge node + mock/真实接口。
- 年度订阅：250k-600k 美元 / yard 起，企业级多项目、多系统集成 750k-1.5M+。
- 成功费：可选 5-8% verified savings，上限封顶，订阅作为底价。

KPI：

- rework labor hours。
- first-pass inspection yield。
- NCR / defect cycle time。
- weld package traceability completeness。
- coating DFT pass rate。
- recoat-window compliance。
- inspection release time。
- work package evidence completeness。
- schedule risk reduction。

## Go-To-Market

第一阶段：

1. 找一个船修/改装/海工/工作船 yard 或二级供应商。
2. 选择一个工序：weld QA、surface prep、coating QA、block release。
3. 跑 30 天 baseline，90 天 paid pilot。
4. 用 rework、NCR、inspection release、evidence completeness 量化 ROI。
5. 从一个项目扩到一个车间，再扩到多工序和全厂。

第二阶段：

- 接机器人供应商：Path、GrayMatter、HD Hyundai Robotics、Novarc、Kranendonk、Inrotech、国内焊接/涂装机器人。
- 接企业系统：P6、MES、ERP、PLM、document control、NCR、Ship OS。
- 建行业模板：船修、分段、涂装、焊接 QA、海工模块、船级社记录包。

## Competition

ShipyardLoop 不替代设计主干、排程系统、机器人或 inspector。

- Path Robotics / GrayMatter：robot execution 强；ShipyardLoop 连接 robot evidence、QA、返工和排程。
- HD Hyundai Robotics / Novarc / Persona / Fincantieri humanoid programs：智能焊接和未来机器人强；ShipyardLoop 做跨品牌证据层。
- Palantir Ship OS / FarView / Tulip / BigBear.ai / C3 AI：数据平台和运营可视化强；ShipyardLoop 从现场边缘采集可信工序事实。
- Siemens / Dassault / AVEVA / Cadmatic / SSI / Hexagon：设计、PLM、工程数据强；ShipyardLoop 补 as-built、现场 QA packet 和 HIL 数据。
- 中国 CSSC/COOEC/GSI 自研体系：场景和内部资源强；ShipyardLoop 做私有化、边缘模型、机器人孤岛连接和轻量试点。

## Moat

壁垒不是一个视觉模型，而是：

> work-package graph + production evidence dataset + shipyard integration playbook + edge profile

会积累的资产：

- 分段、焊缝、涂层、管系、电缆、材料、班组、检验点和排程依赖的 work graph。
- seam、bead、grind coverage、coating、DFT、thermal、LiDAR、tool telemetry 和 human correction 数据集。
- P6、ERP、MES、PLM、Ship OS、文档控制、NCR、WPS、inspector disposition connectors。
- 中国/海外数据平面、工业数据分级、私有云训练、sanitized calibration 和审计流程。
- 船修、分段、涂装、海工模块、焊接 QA、返工和放行 SOP。
- Qualcomm AI Hub / QNN / QAIRT edge profile、弱网缓存和 rollback recipe。

## Architecture

### Edge Capture

- RGB/global-shutter/HDR camera。
- weld camera / NIR/HDR camera。
- thermal camera。
- LiDAR/depth/stereo。
- laser line scanner。
- force/current/tool telemetry。
- DFT/env probes。
- phone/tablet scan and supervisor review。

### ROS 2 Evidence Bus

- /tf、/joint_states、/tool_pose、/rgb、/weld_cam、/thermal、/points、/tool_telemetry。
- rosbag2/MCAP 记录和回放。
- LeRobotDataset v3 导出。

### Supervisor

- seam detection。
- bead anomaly candidate。
- grind coverage。
- coating coverage。
- safety zone。
- action proposal。
- human approval。
- QA packet generation。

### Training Loop

- HIL corrections + recovery trajectories -> dataset。
- China-yard raw data stays in China cloud/private cloud。
- Overseas-yard raw data stays in overseas cloud。
- PyTorch/ONNX -> AI Hub compile/profile -> QNN/QAIRT package -> signed registry -> edge redeploy。

## Competition Demo

3 分钟 demo：

1. mock hull panel 有 seam、rust marks、grind zone、coating target。
2. robot/camera scan panel；edge model 检测 seam、表面缺陷和安全路径。
3. cobot 走冷焊 marker 或低风险打磨覆盖路径。
4. model 标出一个风险区域；operator 用 gamepad 修正，LeRobot 记录接管。
5. 系统生成 QA packet：before/after、thermal frame、3D map、tool path、intervention log、model version、QNN/QAIRT build ID。
6. mock MES/Ship OS 状态更新为 ready_for_inspection 或 released。
7. 展示 China/global training queue 和 edge profile。

演示重点：

> 不是机器人会焊船，而是船厂每天终于能知道每个工包真实完成到哪一步。

## Why Qualcomm

ShipyardLoop 是 Qualcomm 重工业 edge AI 的高适配样板：

- 多传感器：RGB/HDR、thermal、depth/LiDAR、tool telemetry、DFT/env probes。
- 低延迟：seam、coverage、safety zone 和 low-confidence event 需要现场判断。
- 弱网和私有数据：船厂 CAD、工艺、视频、质量记录和防务/海工信息不能默认上公网云。
- 硬件路径：RB3 Gen 2 Vision Kit / QCS6490 做 demo；RB6 / QCS8550 / Dragonwing IQ 系列做生产路线。
- 软件路径：AI Hub、QNN、QAIRT、ONNX Runtime QNN EP、Qualcomm Robotics ROS 支撑可 profile、可部署、可回滚 artifact。
- 商业路径：把 Qualcomm edge AI 从普通工厂延伸到船厂、海工、重型制造和工业私有网络。

## Ask

比赛阶段需要：

- RB3 Gen 2 Vision Kit / RB6 / Dragonwing dev kit。
- mock MES / Ship OS / ERP API。
- mock hull panel、10-30 个工包样例、焊缝/涂层照片和热图样例。
- 一个船修厂、海工制造、船厂 SI、焊接/涂装机器人厂商或船级社顾问。
- AI Hub / QNN profile 支持。
- 安全 demo 边界：不做真实电弧焊、真实喷涂或高风险打磨。

## Claims To Avoid

- 不说解决造船危机。
- 不说替代工人、工长、焊工、质检或 NDT。
- 不说全自动船厂。
- 不承诺 100% 自动识别进度或 100% weld acceptance。
- 不声称已通过 Navy、船级社、军工或安全认证。
- 不把 QNN/QAIRT 描述成 safety-certified control system。
- 不承诺中国/海外数据无障碍流动。

## Sources

- China shipbuilding Q1 2026：https://gxt.fujian.gov.cn/zwgk/xw/hydt/xydt/202606/t20260603_7156246.htm
- GAO shipbuilding delays：https://files.gao.gov/reports/GAO-25-106286/index.html
- CBO 2026 testimony：https://www.cbo.gov/publication/62375
- NDIA robotic welding report：https://www.emergingtechnologiesinstitute.org/-/media/ndia-eti/reports/robotics/accelerating-robotic-welding-solutions-report.pdf
- AWS welding workforce：https://weldingworkforcedata.com/
- HII HYPR：https://hii.com/news/hii-launches-hypr-program-with-path-robotics-and-graymatter-robotics-to-accelerate-production-at-scale
- HII / GrayMatter：https://hii.com/news/hii-teams-with-graymatter-robotics-to-integrate-physical-ai-into-manned-and-unmanned-shipbuilding
- HII / Path Robotics：https://hii.com/news/hii-teams-with-path-robotics-to-integrate-physical-ai-into-manned-and-unmanned-shipbuilding
- U.S. Navy Ship OS：https://www.navy.mil/Press-Office/Press-Releases/display-pressreleases/Article/4355823/navy-invests-448-million-in-ai-and-autonomy-to-accelerate-shipbuilding/
- Global shipbuilding orderbook：https://www.marinelog.com/news/global-shipbuilding-order-book-hits-a-17-year-high/
- CANSI shipbuilding 2025：https://www.cansi.org.cn/cms/document/19815.html
- AI + Manufacturing policy：https://www.nda.gov.cn/sjj/zwgk/zcfb/0112/20260107214358696030895_pc.html
- MIIT shipbuilding digital transformation center：https://www.miit-eidc.org.cn/art/2025/12/15/art_1618_11914.html
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/QNN_general_overview.html
- Qualcomm Robotics ROS：https://www.qualcomm.com/developer/project/robotics-ros
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- rosbag2：https://github.com/ros2/rosbag2
