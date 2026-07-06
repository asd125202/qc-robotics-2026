# CleanLoop 商业清洁闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

CleanLoop 是面向物业、保洁承包商、机场/商场/医院非临床区/园区/仓库运营团队的商业清洁运营塔台：

> 把人流、污染点、保洁员、清洁机器人、人工接管和清洁证据连成一条可调度、可验收、会改进的服务闭环。

它不卖“另一台洗地机器人”。它卖给设施负责人和保洁服务商的是：少漏扫、少投诉、少夜间盯人、能向客户/财务交付 proof-of-service。

## Problem

商业清洁最大痛点不是“没有机器拖地”，而是现场发生了什么没人看得见：

- 哪里脏？
- 谁去清？
- 什么时候清完？
- 漏掉哪里？
- 机器人卡住、缺水、低电、绕不开人群时谁接管？
- 客户投诉、合同验收、SLA 争议时有没有证据？

买方痛点：

- BSC 保洁承包商：排班难、流动率高、夜间监督弱、客户续约需要证据。
- IFM / 物业集团：多站点、多品牌设备、多外包团队，服务质量难统一。
- 商场/机场/地铁：高人流、突发污染、湿滑风险、公众投诉压力强。
- 医院非临床区/校园/园区：低噪、避人、隐私和审计要求更高。
- 仓库/制造场地：大面积硬地面、夜班、叉车/AMR 通道、SLA 和安全风险。

## Why Now

行业已经从“要不要机器人”进入“怎么把机器人纳入运营”。

关键变化：

- 美国 BLS 预计 2024-2034 年 janitors/building cleaners 每年约 351,300 个岗位空缺。
- 2026 年美国 janitorial services market 预计约 1120 亿美元，工资占收入比例高，清洁服务商利润率有限。
- Brain Corp 公开披露清洁机器人累计 23M+ 自主运行小时、300B+ 平方英尺覆盖。
- Tennant 2025 年售出第 10,000 台机器人洗地机，并与 Brain Corp 延长合作推动机器人业务。
- Pudu、Gausium、ECOVACS Commercial、SoftBank Robotics、LionsBot、Kärcher 等在 2026 年继续推新品和海外部署。
- 中国“机器人+”政策明确提到商用/社区服务机器人；GB/T 46495-2025《商用清洁机器人》将于 2026-05-01 实施。
- 中国地铁、物业、医院、园区已经出现规模化案例，例如 ECOVACS 在苏州地铁、Gausium 在招商积余 100+ 项目中的部署。

## Insight

清洁机器人不是产品终点，清洁证据才是客户愿意续费的产品。

CleanLoop 的非显而易见判断：

> 清洁从固定路线，变成按真实使用量触发的服务。

过去：按班次和路线打卡。
现在：按人流、污染、投诉、风险、SLA 和机器人状态动态派单。
未来：每个堵路、漏扫、缺水、人工接管和复检都会让下一班次更准。

## Solution

CleanLoop 是商业清洁的人机运营闭环。

产品模块：

1. **Clean Priority Map**：接入楼层图、SLA、班次、人流/投诉/传感器、机器人地图，生成清洁优先级热力图。
2. **Robot/Human Dispatch**：机器人做地面覆盖，保洁员处理边角、卫生间、垃圾、污渍、补水、异常和客户投诉。
3. **Proof Pack**：路线覆盖、时间戳、照片/短视频、耗材、异常、人工签核、跳过区域和复检记录自动生成客户报告。
4. **Ops Finance**：把覆盖面积、机器人小时、人工接管、投诉、返工、节省班次和 SLA 绑定到月度 ROI。
5. **LeRobot HIL**：堵路、湿滑牌、线缆、玻璃、拥挤、电梯等待、漏扫等失败片段进入训练队列。

## Product Workflow

1. 导入楼层图、服务合同、SLA、禁行区、班次、机器人/人工资源和客户报告模板。
2. 人流、投诉、相机/传感器、工单或固定巡检触发清洁需求。
3. CleanLoop 生成 Clean Priority Map，把入口、卫生间、货架通道、餐饮区、事故点排优先级。
4. 系统派机器人做大面积地面覆盖，派保洁员处理细节、垃圾、补给和异常。
5. Qualcomm edge 设备在现场识别障碍、污渍、湿滑牌、人群、漏扫和低置信度事件。
6. 机器人卡住、缺水、低电、遇到人群或无法覆盖时，自动生成接管任务。
7. 保洁员补做细节并上传 before/after、签核或照片证据。
8. 系统生成覆盖热力图、跳过区域、异常原因、人工接管率、SLA proof 和客户报告。
9. 失败和人工接管片段进入 LeRobot dataset；中国版在本地云训练，海外版在 AWS/GCP/Azure 训练。
10. 模型经 AI Hub / QNN / QAIRT / ONNX Runtime QNN profile 后回到 Qualcomm edge。

## Market Wedge

第一客户不是普通办公楼，而是能直接捕捉价值的大面积硬地面场景：

- 机场、地铁、火车站、商场：高人流、公开投诉、湿滑风险和高频清洁。
- 仓库、制造园区、3PL：大面积硬地面、夜班、叉车/AMR 通道和安全审计。
- 医院非临床区：低噪、避人、可追溯清洁记录。
- 高校/园区/总部：多楼、多班次、多外包团队和统一服务标准。
- BSC/IFM 承包商：用机器人证据包赢固定价格合同和续约。

中国版：

- 物业集团、地铁/机场、商场、医院、园区、学校、制造园区。
- 对接高仙、科沃斯商用、普渡、霞智、汤恩等设备生态。
- 本地数据、本地云、私有部署、PIPL、视频默认不上云、脸/人形模糊。

海外版：

- BSC/IFM、机场/体育场、大学、仓库、医院非临床区、大型零售。
- 对接 Brain/Tennant、Pudu、Gausium、Avidbots、LionsBot、Kärcher、SoftBank Robotics。
- 先从一个站点、一个 night-shift floor-care route、一个 proof pack 切入。

## Business Model

收入模型：

> paid pilot + site SaaS + robot ops subscription + proof/ROI reporting + optional all-in RaaS

建议价格：

- 付费试点：海外 10k-25k 美元；中国 10-40 万元，8-12 周。
- Site SaaS：1.5k-3k 美元 / site / month，覆盖地图、工单、证据、报告和集成。
- Robot Ops：1k-3k 美元 / robot / month，客户已有或租赁机器人时收运营层费用。
- All-in RaaS：把机器人、维护、软件、报告和训练打包，价格锚定少一个重复地面清洁 FTE。
- 中国租赁版：按站点、机器人、清洁面积、任务量和报告模板收费，支持 1288 元/月/台级别低门槛设备租赁生态。

试点 KPI：

- coverage rate。
- skipped area。
- intervention rate。
- proof latency。
- complaint rate。
- robot hours。
- labor redeployment。
- SLA pass rate。
- monthly proof pack used in customer/finance review。

## Go-To-Market

第一阶段：

1. 找一个 50k+ sq ft、每周 5 晚重复清洁的大面积硬地面场地。
2. 部署一条机器人地面清洁路线 + 一个保洁员异常队列 + 一个主管证据 dashboard。
3. 用 8-12 周数据证明 coverage、接管率、投诉、返工和服务证据。
4. 将报告直接给设施负责人、财务或客户合同经理，而不是只给机器人运营员。

第二阶段：

- 复制到同一建筑的卫生间、入口、餐饮区、仓库通道、地下停车场。
- 扩展到多楼、多站点和多品牌机器人。
- 与 CMMS / IFM suite / ServiceNow / Maximo / Eptura / 保洁排班软件集成。
- 与机器人 OEM 和 BSC/IFM 服务商合作，把 CleanLoop 作为合同 proof layer。

## Competition

CleanLoop 不替代清洁机器人厂商，也不替代保洁软件。它把它们连接成运营闭环。

- Brain / Tennant：单机成熟、渠道强、部署规模大；CleanLoop 做跨品牌任务、证据和客户报告层。
- Pudu / Gausium / ECOVACS：产品线和中国/海外部署强；CleanLoop 统一多品牌 fleet 和人机交接。
- Avidbots / LionsBot / Kärcher：工业和传统清洁设备渠道强；CleanLoop 让客户看到 facility-level ROI。
- SoftBank Robotics / Whiz：RaaS 和服务体系强；CleanLoop 做设施级 priority map 和 proof pack。
- Mero / Swept / Optii / TEAM：保洁运营软件强；CleanLoop 原生连接机器人、edge perception 和 HIL training。
- ServiceNow / Maximo / Eptura：设施工单和资产管理强；CleanLoop 做清洁执行层和证据层。

## Moat

壁垒不是某一台机器人，而是：

> site semantic map + cleaning demand + human-robot execution + proof pack + HIL data

会积累的资产：

- 每栋楼的高风险区、堵点、投诉点、湿滑点、清洁频率和人工接管历史。
- 机器人路线、覆盖足迹、跳过区域、耗材、缺水/低电/堵塞原因。
- before/after evidence、客户报告模板、SLA 争议记录和合同续约证据。
- 多品牌机器人 adapters、CMMS/BMS/elevator/door/保洁软件连接器。
- 隐私策略、视频最小化、模糊化、保留周期和本地部署 playbook。
- LeRobot HIL 清洁恢复数据集和 Qualcomm edge profiles。

## Architecture

### CleanLoop Scheduler

- 接 work-order app / CMMS / IFM suite / 保洁排班软件。
- 生成 CleanTask、ExceptionTask、ProofPack、SLAReport。
- 支持 ServiceNow、Maximo、Eptura、CSV/API/mock CMMS 起步。

### Facility Map Layer

- 导入 CAD / floor plan / robot map。
- 区分 traffic lane、cleaning zone、no-go zone、elevator、door、charging、water station。
- 用 Open-RMF Traffic Editor 管理共享设施语义。

### Robot Edge

- RGB/depth camera、2D/3D LiDAR、IMU、wheel odometry、cleaning base。
- ROS 2 / Nav2 / SLAM / opennav_coverage。
- Qualcomm RB3 Gen 2 原型；RB6 / Dragonwing IQ10 作为多摄像头和生产级路径。

### Privacy-First Perception

- 人/障碍/污渍/湿滑牌/线缆/漏扫在端侧识别。
- 默认上传事件、mask、heatmap、count、coverage，不上传原始视频。
- 人脸/人体模糊，医院/地铁/园区支持本地数据平面。

### Learning Loop

- 记录 camera/LiDAR/costmap/pose/zone/work-order/action/human correction。
- Nav2/RMF 仍是安全和导航权威；学习策略只建议 recovery action、zone strategy 或 task priority。
- 中国训练：阿里云 PAI-DLC、腾讯 TI-ONE、华为 ModelArts 或私有云。
- 海外训练：AWS SageMaker、Google managed training、Azure ML、NVIDIA DGX Cloud。
- 区域训练产物经 AI Hub/QNN/QAIRT profile 后 OTA 到 edge fleet。

## Competition Demo

3 分钟 demo：

1. 晚高峰后，商场入口热力图变红，生成 `clean_lobby` 任务。
2. 清洁机器人执行地面覆盖，dashboard 显示覆盖轨迹和剩余区域。
3. 货架/通道被障碍物挡住，机器人请求人工接管。
4. 保洁员处理污渍并上传 before/after 证据。
5. 系统生成 proof pack：覆盖面积、跳过区域、异常原因、人工接管、时间戳和 SLA 结论。
6. 接管片段导出为 LeRobot episode，展示下一轮训练队列和 Qualcomm edge profile。

演示重点：

> 不是机器人跑一圈，而是主管少看 20 个群消息，只看一个异常队列和一份证据报告。

## Why Qualcomm

CleanLoop 是 Qualcomm 在公共空间 edge AI 里的高频商业场景：

- 商业清洁发生在公共空间，视频和传感器数据不适合全量上云。
- 现场需要低延迟障碍、污渍、湿滑牌、人群和漏扫识别。
- 弱网、电梯/门禁、夜间运行和多楼层覆盖要求本地可靠执行。
- RB3 Gen 2 适合比赛原型，RB6/Dragonwing IQ10 适合多摄像头、多传感器、5G/private-network 的生产路线。
- AI Hub / QNN / QAIRT 把云训练模型变成可部署、可 profile、可回滚的 edge artifact。
- LeRobot HIL 把保洁员接管和场地异常变成下一轮机器人恢复能力。

## Ask

比赛阶段需要：

- RB3 Gen 2 / RB6 + Vision Kit 或等价 Qualcomm edge dev kit。
- 一个清洁机器人 OEM、BSC/IFM 服务商或物业/园区试点伙伴。
- 一个真实楼层图和 2 周匿名清洁运营数据。
- 一个 mock CMMS / work-order API。
- AI Hub / QNN profile 支持，用于展示从区域云训练到 edge deployment 的完整证据链。

## Claims To Avoid

- 不说全自动替代保洁员。
- 不说无需人工干预。
- 不说适用于所有建筑。
- 不承诺固定 ROI 或固定节省比例。
- 不承诺消毒/杀菌/医疗级清洁，除非有认证和测试。
- 不上传公共空间原始视频作为默认方案。
- 不声称 Qualcomm 官方合作/认证，除非真实签约。

## Sources

- BLS janitors outlook：https://www.bls.gov/ooh/building-and-grounds-cleaning/janitors-and-building-cleaners.htm
- CMM / IBISWorld janitorial economics：https://cmmonline.com/news/u-s-janitorial-services-market-projected-to-grow-nearly-2-in-2026
- ISSA robotics mainstream：https://www.issa.com/articles/going-mainstream/
- Brain Corp floor care：https://www.braincorp.com/floor-care
- BrainOS Clean 2.0：https://www.braincorp.com/resources/brain-corp-launches-brainos-r-clean-2-0-with-selfpath-tm-ai-advancing-adaptive-autonomy-for-tennant-company-floor-cleaning-robots
- Brain Corp scale：https://www.braincorp.com/resources/brain-corps-autonomous-robot-fleet-hits-250-billion-square-feet-milestone-leads-global-surge-in-robotic-automation
- Tennant 10,000 robotic scrubbers：https://investors.tennantco.com/news/news-details/2025/Tennant-Company-Sells-10000th-Robotic-Scrubber-Underscoring-Global-Demand-for-Cleaning-Automation/default.aspx
- Tennant / Brain 2026：https://investors.tennantco.com/news/news-details/2026/Tennant-Company-and-Brain-Corp-Agree-to-Accelerate-Robotic-Cleaning-Innovation-Advancing-Tennants-Transformation-into-a-Robotics-and-Technology-Leader/default.aspx
- Pudu / Denner：https://www.prnewswire.com/news-releases/pudu-robotics-and-robobee-forge-strategic-partnership-with-denner-for-major-robotic-cleaning-deployment-across-swiss-stores-302795108.html
- Pudu cleaning growth：https://www.intercleanshow.com/products-and-services/pudu-robotics/news/70-of-total-revenue-how-pudu-s-commercial-cleaning-robots-became-the-core-growth-engine
- Gausium roadmap：https://gausium.com/2026/02/25/future-of-commercial-cleaning-robots/
- Gausium Interclean：https://gausium.com/news/gausium-introduces-two-new-outdoor-sweepers-and-industrys-largest-cleaning-robot-lineup-at-interclean-amsterdam-2026/
- ECOVACS Commercial：https://www.ecovacsgroup.com/service/commercial-robot
- ECOVACS Suzhou Metro：https://www.ecovacsb2b.com/news/detail?id=67
- Gausium / 招商积余：https://www.gs-robot.com/case/招商积余100项目上岗高仙商用清洁机器人智慧清/
- Pudu China：https://www.pudutech.com/zh-CN
- GB/T 46495-2025：https://std.samr.gov.cn/gb/search/gbDetailed?id=17AC6A11BB1CD005E06397BE0A0AC8FC
- PIPL：https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm
- CAC data export rules：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- Open-RMF：https://www.open-rmf.org/
- Nav2 coverage：https://docs.nav2.org/configuration/packages/configuring-coverage-server.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT：https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/QNN_general_overview.html
- Qualcomm Robotics ROS：https://www.qualcomm.com/developer/project/robotics-ros
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Alibaba PAI-DLC：https://www.alibabacloud.com/help/en/pai/what-is-dlc
- Tencent TI-ONE：https://www.tencentcloud.com/document/product/1141
- Huawei ModelArts：https://support.huaweicloud.com/intl/en-us/usermanual-standard-modelarts/develop-modelarts-0001.html
- AWS SageMaker：https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html
- Azure ML：https://learn.microsoft.com/en-us/azure/machine-learning/how-to-train-distributed-gpu
