# StoreLoop 店务闭环 Pitch

更新时间：2026-07-06。零售机器人部署、门店系统接口、隐私监管、药品追溯、POS/ERP/WMS 数据结构和机器人安全认证变化很快；真实商业材料应在提交前复核客户系统、区域法规和设备认证。

## Core Thesis

StoreLoop 店务闭环是面向门店运营的 Qualcomm 边缘机器人与 LeRobot 数据飞轮：

> 不是“会逛商店的机器人”，而是门店里的边缘运营闭环。每一次巷道巡检都把货架真实状态变成三个输出：店员任务、受限机器人动作和可训练 episode。

零售机器人已经商业化，但最成熟的不是通用店员机器人，而是窄任务：

- shelf intelligence：缺货、错位、价格、促销、陈列和 planogram。
- cleaning proof：清洁机器人、路线覆盖、proof-of-work。
- store patrol：货架巡检、地面异常、门店任务。
- bounded replenishment：便利店/药房/饮料柜/小件补货等受限场景。
- pharmacy/retail capsule：订单、拣选、追溯码、打包、取货柜和人工异常处理。

StoreLoop 的产品判断：

- POS/WMS 库存不等于货架真实状态。
- 机器人只检测问题还不够，价值来自“发现 -> 派单 -> 修复/协助 -> 复查 -> 学习”。
- 人类店员不该被替代，而应该获得更准确的任务优先级和机器人协助。
- Qualcomm edge 负责本地视觉、OCR/barcode、导航、安全、隐私和低延迟动作；LeRobot 负责 HIL 数据和训练闭环。

## Five-Thread Research Synthesis

### 1. Global Market

Simbe Tally 是最强货架智能参考，公开材料覆盖 on-shelf availability、价格/促销准确性、商品位置、planogram、补货和履约。Brain Corp/BrainOS 在清洁与 inventory scan 组合上有规模化部署，Badger/Marty 证明门店巡检机器人可以从地面异常扩展到货架检测，Pudu 在清洁/配送/服务机器人上规模化，Telexistence 在 FamilyMart 冷柜饮料补货上证明 last-10-meter replenishment 可以在受限场景成立。

安全表达：零售机器人商业化已经真实存在，但大多是窄任务和人机协作，不是全店无人化。

### 2. China Retail And Pharmacy

中国版最强信号不是“通用人形店员”，而是闭环药房/便利店 workflow。Galbot G1 在北京海淀持牌药房运营的公开报道，给了药品订单接收、拣选、打包、补货、库存、追溯码、近效期提醒和药监追溯平台接入等 benchmark。

中国版 StoreLoop 要把消费者侧 WeChat mini-program、会员、支付、取货通知，与员工侧企微/钉钉/飞书异常提醒分开设计。药房场景必须支持药品追溯码、批次、有效期、处方/药师审核交接和本地数据边界。

### 3. Technical Architecture

StoreLoop 采用三平面架构：

- Robot edge plane：Qualcomm edge 运行 ROS 2、感知、安全过滤、OCR/barcode、导航、受限动作和本地 policy inference。
- Store services plane：门店本地服务器保存地图、planogram、库存缓存、POS/WMS/ERP adapter、任务派发、视频脱敏和操作台。
- Cloud training plane：中国/海外两套数据平面，LeRobot dataset、标注、训练、评估、模型注册和 OTA 灰度。

### 4. Business Model

卖零售执行平台，不卖一台机器人：

- Shelf Core：缺货、价格、促销、陈列和 planogram。
- Execution Pro：补货任务、BOPIS、门店任务、POS/ERP/ESL 接入。
- Clean + Proof：清洁机器人 proof-of-work 与货架/地面巡检合并。
- Brand Insights：把货架执行数据变成 CPG / retail media 的付费洞察。
- Enterprise Fleet：多门店 RaaS、SLA、服务备机、API、安全审查和区域部署。

### 5. Product Design

名称：RobotMac StoreLoop / 店务闭环。

一句话：

> Shelf truth -> human-safe action -> training data -> edge deployment.

产品不与 Simbe/Brain/Pudu 正面做“又一个扫描机器人”，而是把 shelf truth 与受限动作、店员任务、LeRobot 数据和 Qualcomm edge 部署闭环连接起来。

## Product Modules

### 1. Shelf Truth Engine

货架真实状态引擎：

- 多相机、depth/ToF、货架边缘定位、商品检测/分割、OCR 价签、barcode/QR/GS1 Digital Link。
- 输出缺货、错位、价格不一致、促销标签异常、陈列偏差、低库存、货架遮挡和无法识别。
- 对相似包装、反光包装、冷柜门、挂钩商品、堆头和季节陈列保持人工复核。

### 2. Store Task Loop

把检测结果转成门店任务：

- 检测到空面 -> 查询 POS/WMS/ERP -> 判断是否后仓有货 -> 生成补货任务。
- 检测到错价 -> 查 POS/ESL -> 生成价格复核任务。
- 检测到促销陈列不一致 -> 生成 merchandising task。
- 机器人无法确定 -> 生成人工复核 task，而不是直接写入库存。
- 任务完成后复扫，形成 proof-of-closure。

### 3. Bounded Action Runtime

StoreLoop 不承诺全 SKU 自动补货，而是做受限动作：

- 指示灯/投影：指给店员要处理的位置。
- 小件取放：轻量 demo SKU、药盒、饮料/瓶装商品、标准托盘。
- shelf facing assist：把小件对齐或前移到可见面。
- tote handoff：从后仓/取货柜/打包台递交给店员。
- 药房订单：扫码、追溯码、批次、有效期、打包和药师审核交接。

### 4. LeRobot Store Dataset

每次异常都可以变成训练样本：

- ShelfObservation：图片、深度、机器人位姿、货架层、OCR、barcode、检测框和置信度。
- ReplenishmentTask：源位置、目标货架、SKU、数量、优先级、deadline。
- ManipulationEpisode：相机、动作、夹爪状态、成功/失败、人工接管和恢复。
- PrivacyManifest：人脸/身体脱敏、保留周期、区域、导出权限。
- ModelArtifact：数据版本、训练区域、quantization profile、Qualcomm target、回滚版本。

### 5. Retail Integrations

门店不是孤岛：

- POS / WMS / ERP：商品主数据、库存、价格、促销、会员和订单。
- ESL / price label：价签和促销验证。
- BOPIS / pickup：线上下单、门店拣货、缺货替代和取货柜。
- EPCIS / GS1：商品追溯和库存事件。
- 中国版：WeChat mini-program、企微、钉钉、飞书、本地 POS、药品追溯、Meituan/Ele.me。

## China / Overseas Versions

中国版：

- 主张：`门店边缘 AI 店务闭环`。
- 第一场景：药房小店、便利店、商超高频货架、即时零售前置仓和商场清洁/巡检。
- 消费者侧：微信小程序下单、会员、优惠券、支付、取货通知。
- 员工侧：企微/钉钉/飞书异常任务、药师/店长审核、低库存、近效期提醒、卡货/卡机通知。
- 数据侧：本地云/私有云、PIPL、门店 LAN fallback、药品一物一码、批次和有效期。

海外版：

- 主张：`Retail execution platform for shelf truth and trainable store actions`。
- 第一客户：grocery、warehouse club、pharmacy、convenience、CPG、facility service。
- 首批包：Shelf Core、Execution Pro、Clean + Proof、Brand Insights、Enterprise Fleet。
- 以 RaaS、8-12 周 pilot、control stores、UL/安全准备、privacy-forward 和 API integration 进入。

## Competition Demo

三分钟 demo 可以用 mock store shelf 完成：

1. Qualcomm target 启动，显示本地相机、机器人状态、manual stop。
2. 机器人扫描货架，检测空面、错位 SKU、价签/QR 不匹配或低库存。
3. Dashboard 生成补货/复核任务，并显示 POS/WMS 缓存查询。
4. 机器人执行受限动作：指示灯定位、移动一个轻量 demo 商品，或把商品从 tote 递给店员。
5. 制造边界情况：遮挡、反光、抓取失败、planogram 过期或人流阻挡。
6. 人工接管，系统记录 LeRobot episode。
7. 展示 dataset version、训练 job、Qualcomm edge profile、签名 artifact 和灰度部署。
8. 复扫货架，关闭任务，输出 proof-of-closure。

这个 demo 避免假装“实时从零训练”，而是展示已经预训练/预计算 artifact 的发布门禁。

## Why Qualcomm Should Care

门店运营是 Qualcomm 边缘 AI 的高密度场景：

- 多相机和视频 pipeline：货架、价签、条码、深度、手臂末端相机。
- 本地推理：OCR、barcode、SKU 识别、导航、人群避让和隐私脱敏。
- 低延迟动作：小件抓取、指示、避障和人工接管。
- 连接：Wi-Fi / 5G / private network，门店本地 cache 和云端 fleet 同步。
- AI Hub / QNN / TFLite / ONNX Runtime：模型 profile、量化、回归验证、部署和回滚。
- 隐私边界：默认边缘脱敏，上传任务元数据和授权片段。

一句话：

> Qualcomm 不只是让门店机器人看见货架，而是让货架真实状态进入可执行、可训练、可验证的门店闭环。

## Claims To Avoid

- 不说完全自动补货所有 SKU。
- 不说替代店员。
- 不承诺固定库存准确率、ROI 或销售提升。
- 不说无需门店系统集成。
- 不做 face recognition、顾客画像、动态定价或监控优先叙事。
- 不声称实时从零训练或 Qualcomm/LeRobot 官方认证。
- 不把药房机器人描述成自动处方/临床建议系统；药师审核必须保留。

## Sources

- Simbe Tally 4.0：https://www.simberobotics.com/about/newsroom/simbe-unveils-tally-4-0-the-next-generation-of-autonomous-retail-robot-powering-store-intelligence-via-physical-ai
- Simbe / B&R Stores：https://www.prnewswire.com/news-releases/br-stores-introduces-simbes-tally-inventory-robot-in-stores-across-nebraska-302794610.html
- Simbe / Coresight 2026：https://www.simberobotics.com/the-state-of-in-store-retailing-2026-coresight-research-x-simbe-robotics
- Simbe 10 years：https://www.simberobotics.com/about/newsroom/simbe-marks-10-years-of-tally-the-robot
- Brain Corp Sam's Club：https://corporate.walmart.com/about/samsclub/news/2022/10/20/sams-club-finalizes-national-deployment-of-inventory-scan-brain-corp-becomes-the-worlds-largest-supplier-of-robotic-inventory-scanners
- Brain Corp ShelfOptix：https://www.prnewswire.com/news-releases/brain-corp-and-driveline-launch-shelfoptix-the-first-fully-managed-robot-powered-shelf-intelligence-service-302568903.html
- Badger / Stop & Shop：https://www.badger-technologies.com/news/press-releases/stop-and-shop-upgrade-marty-the-robot.html
- Pudu / Denner：https://www.prnewswire.com/news-releases/pudu-robotics-and-robobee-forge-strategic-partnership-with-denner-for-major-robotic-cleaning-deployment-across-swiss-stores-302795108.html
- Pudu retail：https://www.pudurobotics.com/en/solutions/retail
- Telexistence FamilyMart：https://tx-inc.com/en/blog/2022/08/10/11712/
- Galbot pharmacy / CGTN：https://news.cgtn.com/news/2026-03-13/China-s-first-pharmacy-robot-goes-into-service-in-Beijing-1LtZ7juLcZ2/p.html
- Galbot pharmacy / Stdaily：https://www.stdaily.com/web/gdxw/2026-03/17/content_486741.html
- Pudu Open Platform：https://open.pudutech.com/en
- OrionStar cases：https://en.orionstar.com/SuccessfulCases.html
- Keenon / Xinhua：https://www.news.cn/20250528/bd49185b0c8740dcb8a4eed8cffe3276/c.html
- Gausium cases：https://www.gs-robot.com/case-studies/
- IHL inventory distortion：https://www.ihlservices.com/news/analyst-corner/2025/09/retail-inventory-crisis-persists-despite-172-billion-in-improvements/
- Qualcomm RB5：https://www.qualcomm.com/developer/hardware/robotics-rb5-development-kit
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- Qualcomm SNPE：https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- LeRobot IL robots：https://huggingface.co/docs/lerobot/en/il_robots
- OpenCV Barcode：https://docs.opencv.org/4.x/d6/d25/tutorial_barcode_detect_and_decode.html
- GS1 GTIN：https://www.gs1.org/standards/id-keys/gtin
- GS1 EPCIS：https://www.gs1.org/standards/epcis
- Nav2 collision monitor：https://docs.nav2.org/configuration/packages/configuring-collision-monitor.html
- MoveIt 2：https://moveit.picknik.ai/
- ROS 2 access control：https://design.ros2.org/articles/ros2_access_control_policies.html
- CAC data export assessment：https://www.cac.gov.cn/2022-07/07/c_1658811536396503.htm
