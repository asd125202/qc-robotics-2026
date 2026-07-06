# FoodLoop 餐务闭环 Pitch

更新时间：2026-07-06。餐饮机器人、食品安全要求、POS/KDS 接口、服务机器人认证、地方监管和餐饮经营成本变化很快；真实商业材料应在提交前复核客户系统、设备认证、食品安全 SOP 和当地法规。

## Core Thesis

FoodLoop 餐务闭环是面向餐饮运营的 Qualcomm 边缘机器人与 LeRobot 数据飞轮：

> 不是“另一个机器人服务员”，而是把 KDS/POS 订单、安全托盘交接、机器人配送/回收、异常接管、清洁证据和训练数据连成一条可运营闭环。

餐饮机器人已经真实部署，但成熟场景不是“全自动餐厅”：

- 前厅：送餐、回收、引导、排队区配送和宴会/自助餐厅巡回。
- 后厨：受限菜单的炒制、炸制、饮品、装配线、洗碗/回收、清洁日志。
- 酒店/园区：房间/会议/机场/办公楼最后 30 米配送。
- 运营系统：POS/KDS、扫码点餐、Meituan/Douyin/WeChat、任务调度、SLA、维护和 ROI。

FoodLoop 的产品判断：

- 餐饮买家不买“炫技机器人”，而买更少瓶颈、更稳交付和可衡量的高峰效率。
- 机器人不能只跑路线，必须和 KDS/POS、托盘验证、清洁证据、异常处理和服务工单连接。
- LeRobot 的价值在于把错托盘、堵路、抓取失败和人工恢复变成可训练 episode。
- Qualcomm 的价值在于本地感知、低延迟导航、隐私过滤、连接、边缘部署 profile 和安全降级。

## Five-Thread Research Synthesis

### 1. Global Market

餐饮机器人商业化已经跨过“新奇展示”阶段，但主要是窄任务工具。Bear、Pudu、Keenon 等送餐/回收机器人是最成熟类别；Richtech、Cafe X、Nala、Miso/Flippy、Botinkit、Sweetgreen/Spyce、Hyphen 等证明厨房和饮品自动化在受限菜单、受限工位中可行；Picnic 的关闭也提醒我们，单点厨房机器人如果没有强运营闭环和服务经济性，很容易失败。

安全表达：餐饮机器人已经是运营工具，但赢家是可靠、可服务、可度量的窄系统，不是泛化机器人厨师。

### 2. China F&B Lane

中国餐饮规模巨大但价格竞争激烈，连锁化提升让标准化自动化更有机会。Pudu 和 Keenon 证明送餐、回收、酒店配送和清洁机器人在中国及海外都有规模化；Botinkit 代表标准化智能厨房；Meituan 已经把 AI agent、机器人、商户、位置和配送场景连接到具体订单工作流。

中国版 FoodLoop 应优先面向：

- 火锅/宴会/自助餐：跑菜、回盘、清洁 proof。
- QSR / 标准化炒锅站：数字菜谱、出餐节拍、异常日志。
- 酒店/机场/办公园区：最后 30 米配送、门/梯/柜/房号集成。
- 连锁总部：门店对比、远程健康、峰值吞吐、培训周期和服务商网络。

### 3. Technical Architecture

FoodLoop 的技术栈：

- Qualcomm edge runtime：ROS 2、Nav2、Open-RMF、MoveIt、相机/托盘/重量/二维码/温度传感器、签名模型和本地任务状态机。
- POS/KDS connector：Square、Toast、Oracle/NCR、Meituan RMS、Douyin、WeChat 等订单事件规范化。
- Food safety service：HACCP-style checkpoint、TCS timer、温度日志、过期/废弃/过敏原约束和清洁记录。
- LeRobot HIL：自动段、人工接管段、恢复段和结果标签进入 LeRobotDataset v3。
- Cloud training：同一 schema 分中国/海外数据平面，训练、评估、AI Hub profile、灰度和回滚。

### 4. Business Model

餐饮机器人 GTM 要卖 ROI，不卖机器人：

- Runner Starter：送餐/回盘 AMR、地图、基础 dashboard。
- Service Pro：POS/KDS、托盘 ID、桌号/柜号、清洁 proof、服务分析。
- Kitchen Assist：炸锅/装配/炒锅/饮品/洗碗站的受限工位自动化。
- Multi-Site Fleet：连锁总部、区域门店、SLA、服务备机和季度 ROI。
- Distributor SKU：给设备经销商/服务商的安装、维护、备件和软件分成。

### 5. Product Design

名称：FoodLoop 餐务闭环。

一句话：

> Ticket -> tray -> table -> exception -> training loop.

产品不是替代服务员，而是把餐厅里最重复、最耗步数、最容易在高峰出错的工作连接到边缘机器人和数据闭环。

## Product Modules

### 1. KDS / POS Task Bridge

把订单系统变成机器人任务：

- 接收订单、桌号、取餐柜、外卖取餐号、房间号、门店区域和 promised time。
- 支持重复 webhook、取消、改单、缺货和 KDS 手动覆盖。
- 生成 RobotTask：出餐、送餐、回盘、清洁、补料、洗碗、取货柜、房间配送。
- 中国版接入微信扫码点餐、Meituan/Dianping、Douyin 本地生活、Alipay/WeChat Pay 和门店 RMS/POS。

### 2. Tray Verification

送餐机器人要知道自己拿的是什么：

- QR/条码/桌号/托盘 ID。
- 相机识别菜品/容器/缺件。
- 重量传感器或托盘槽位检测。
- 过敏原、温度、持有时间、封签和是否需要人工确认。
- 错托盘、缺菜、超时和未锁托盘时不派车。

### 3. Dining-Floor AMR

前厅机器人只做安全、低速、可接管工作：

- Nav2 路线、Open-RMF 调度、桌区/通道/厨房口/回盘点/清洁区语义地图。
- 动态避障、堵路等待、人工接管、慢行区和临时 wet-floor zone。
- 支持送餐、回盘、桌边停靠、取餐架、宴会巡回和酒店最后 30 米配送。

### 4. Kitchen Assist Cells

后厨自动化必须被限定在工位里：

- 炸锅/烤炉/炒锅：计时、温度、篮筐/锅具、烟雾/异常、硬 interlock。
- 装配线：碗/堡/饮品/配菜、视觉+称重验证。
- 洗碗/回收：脏/净分离、托盘/杯/餐具识别、消毒/温度日志。
- LeRobot policy 只控制受限动作，安全 PLC/MCU 永远有最高优先级。

### 5. Service Evidence Ledger

最终交付是运营证据：

- 订单：ticket time、promise time、出餐、送达、回盘、异常。
- 机器人：路线、等待、接管、堵路、低电、清洁、维护。
- 食安：温度、TCS timer、过敏原、封签、清洁、废弃/重做。
- ROI：步数减少、峰值 ticket time、table turn、回盘周转、清洁覆盖、停机和服务工单。
- 训练：失败原因、人工恢复、低置信度、模型版本和部署门禁。

## China / Overseas Versions

中国版：

- 主张：`餐务闭环：机器人不是表演，而是连锁门店标准化工具`。
- 优先场景：火锅、宴会、自助餐、酒店、机场、园区食堂、医院食堂、QSR、标准化炒锅站。
- 本地系统：WeChat Mini Program、Meituan/Dianping、Douyin POI/团购/点餐、Alipay/WeChat Pay、门店 RMS/POS、中文工单。
- 商业打法：低摩擦、低 CAPEX、经销商/服务商渠道、月租/买断+软件、本地云/私有化。

海外版：

- 主张：`Restaurant ops robot platform: service assurance, not robot novelty`。
- 优先客户：QSR、casual dining、hotel、cafeteria/campus、cloud kitchen、facility service、equipment distributor。
- 首批包：Runner Starter、Service Pro、Kitchen Assist、Multi-Site Fleet、Distributor SKU。
- 商业打法：RaaS/SLA、POS/KDS integration、保险/安全/隐私、安装维护、备机和 ROI dashboard。

## Competition Demo

三分钟 demo 可以这样做：

1. Mock KDS/POS 生成订单：桌号、菜品、过敏原、预计出餐时间。
2. 桌面机械臂或操作员把 sealed bowl 放到托盘；相机/QR/重量验证 tray。
3. AMR 从厨房口到桌号/取餐架，遇到 blocked aisle 或 wet-floor zone 时本地避障或等待。
4. 制造异常：缺少配菜、错托盘、路线被挡、托盘识别失败或客人未取。
5. 人工接管并完成恢复，系统保存 HIL episode。
6. Dashboard 显示 OrderEvent、RobotTask、FoodSafetyEvent、LeRobot dataset、Qualcomm edge profile 和 proof-of-service。
7. 复盘页输出：ticket time、handoff delay、intervention reason、training data version 和 next deployment gate。

演示不要假装从零实时训练，而是展示已经预计算 artifact 如何通过评估和部署门禁。

## Why Qualcomm Should Care

餐饮场景能把 Qualcomm 的边缘价值讲得很具体：

- 现场弱网也要继续送餐、回盘、清洁和记录。
- 多摄像头、托盘/菜品识别、二维码、语音、避障和地面异常都需要本地推理。
- 低延迟导航和动作仲裁决定能否安全穿过高峰餐厅。
- 机器人相机不能默认把顾客视频上传云端，隐私过滤应在边缘完成。
- AI Hub / QNN / ONNX / TFLite profile 可以成为每次模型上线的性能证据。
- IQ10 RRD 适合生产路线，RB3/RB5/RB6 等适合比赛和开发者路线。

一句话：

> Qualcomm 不只是让送餐机器人会走路，而是让餐厅每一次出餐、异常、回盘和清洁都进入可学习、可审计、可部署的餐务闭环。

## Claims To Avoid

- 不说全自动餐厅、替代服务员、替代厨师。
- 不承诺固定 ROI、固定节省 FTE、固定吞吐提升。
- 不声称 NSF/UL/HACCP/FDA/CE 等认证，除非具体硬件已认证。
- 不做开放式烹饪或危险热源自主操作承诺。
- 不做 face recognition、顾客画像或监控优先叙事。
- 不声称实时从零训练或 Qualcomm/LeRobot 官方认证。

## Sources

- National Restaurant Association 2026：https://restaurant.org/research-and-media/media/press-releases/persistent-cost-increases-and-enduring-demand-will-shape-the-restaurant-industry-in-2026/
- Pudu Robotics funding：https://www.pudurobotics.com/en/news/pudu-robotics-raises-150-million-exceeds-1-5-billion-valuation
- Pudu BellaBot Pro：https://www.pudurobotics.com/en/products/bellabotpro
- Pudu Open Platform：https://open.pudutech.com/en
- Keenon / Xinhua：https://www.news.cn/20250528/bd49185b0c8740dcb8a4eed8cffe3276/c.html
- Bear Robotics：https://www.bearrobotics.ai/
- Richtech 10-K：https://www.sec.gov/Archives/edgar/data/1963685/000121390025003458/ea0226831-10k_richtech.htm
- Richtech Walmart locations：https://www.globenewswire.com/news-release/2024/10/17/2964874/0/en/richtech-robotics-expands-agreement-with-ghost-kitchens-to-manage-20-additional-walmart-located-restaurants-growing-its-restaurant-operations-model.html
- Sweetgreen / Spyce sale：https://www.businesswire.com/news/home/20251106759339/en/Sweetgreen-Announces-Strategic-Sale-of-Spyce-to-Wonder
- Chipotle Hyphen：https://newsroom.chipotle.com/2024-09-16-CHIPOTLE-DEBUTS-AUTOCADO-AND-THE-AUGMENTED-MAKELINE-BY-HYPHEN-IN-RESTAURANTS
- Miso SEC deployment count：https://www.sec.gov/Archives/edgar/data/1710670/000110465926001520/tm262179d1_partiiandiii.htm
- Armstrong dishwashing robots：https://www.newswire.com/news/armstrong-raises-12m-to-bring-general-purpose-robots-to-kitchens-22659296
- Botinkit：https://botinkit.ai/
- Nala Wingman：https://nalarobotics.com/the-wingman.html
- Cafe X：https://www.cafexapp.com/locations
- Picnic shutdown：https://www.nrn.com/restaurant-technology/pizza-robot-company-picnic-shuts-down
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- China catering 2025：https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html
- Meituan robot delivery：https://www.meituan.com/news/NN260227211002715
- Meituan RMS：https://rms.meituan.com/
- Douyin catering solution：https://developer.open-douyin.com/docs/resource/zh-CN/local-life/solution/catering
- Qualcomm IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm Robotics ROS：https://www.qualcomm.com/developer/project/robotics-ros
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- Nav2：https://docs.nav2.org/
- Open-RMF：https://openrmf.readthedocs.io/
- MoveIt 2：https://moveit.picknik.ai/
- Square Orders API：https://developer.squareup.com/docs/orders-api/what-it-does
- Toast order webhooks：https://doc.toasttab.com/doc/devguide/devOrdersWebhookRef.html
- FDA Food Code 2022：https://www.fda.gov/food/fda-food-code/food-code-2022
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
