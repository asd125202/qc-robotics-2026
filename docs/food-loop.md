# FoodLoop 餐饮异常闭环 Pitch

更新时间：2026-07-06。餐饮机器人、食品安全、POS/KDS 接口、服务机器人安全、平台外卖规则和餐饮成本变化很快；正式提交前需要复核客户系统、设备认证、食品安全 SOP 和本地法规。

## 一句话

FoodLoop：让每一单从“做好了”走到“正确交付”。

连锁餐饮用 FoodLoop 把 KDS/POS 票据、托盘/外卖袋、跑菜机器人、回盘清洁、食安证据、浪费重做和人机接管，变成可派单、可验证、可复盘、可训练的餐饮异常闭环。

## Problem

餐厅高峰最贵的不是没有机器人，而是每个异常都靠人盯人。

- KDS 记录“票据完成”，但不证明托盘、外卖袋和桌号正确。
- 错托盘、漏饮料、过敏原漏检、外卖交接不清，会导致退款、差评和复购损失。
- 回盘慢、清洁漏项、温度/持有时间记录不完整，会带来翻台和食安风险。
- 过量备餐、重做、超时废弃和报损很难追溯到具体流程。
- 机器人如果只负责跑路线，就只是搬运“被装上去的东西”。

## Why Now

餐饮进入低毛利、高外卖、高连锁化的效率战。

- 美国餐饮业 2026 年预计销售额 1.55 万亿美元、就业 1580 万人，但 2025 年 45% 经营者未盈利，60% 遇到客流下滑。
- 美国全服务/有限服务餐厅中，95%/94% 认为食材成本是重大挑战，96%/94% 认为人工成本是重大挑战。
- 中国 2025 年餐饮收入 57,982 亿元，同比增长 3.2%；2026 年 1-5 月餐饮收入 23,488 亿元，同比增长 3.1%。
- 中国 2025 年餐饮连锁化率达 25%，美团系统中 2025 年标记停业商户 339 万家，同比增长 9.4%。
- UNEP 估算 2022 年全球 food service 食物浪费约 2.90 亿吨。
- 2025 年 QSR drive-thru 准确率约 87%，漏项、错项、定制项和饮料细节仍是直接利润黑洞。
- 服务机器人已进入商用阶段，IFR 报告 2024 年专业服务机器人销量接近 20 万台。

这些信号说明：餐饮买家现在不是为“炫技机器人”付费，而是为更少错单、浪费、重做、等待、清洁漏项和食安证据缺失付费。

## Core Insight

餐厅不缺会走路的机器人，缺的是把异常关掉的操作系统。

机会不是再造一个机器人服务员，也不是做一个单点厨房视觉模型，而是把：

- ticket：POS/KDS/外卖订单。
- tray/bag：托盘、外卖袋、菜品、封签、过敏原、重量和温度。
- motion：机器人路线、堵路、等待、回盘和清洁。
- proof：交接、桌号、清洁、食安、废弃和主管确认。
- learning：人工接管、低置信度、错单纠正和复发异常。

连接成同一条闭环。

## Solution

FoodLoop 是 existing restaurant 之上的餐饮异常闭环层。

它不替代 POS、KDS、机器人、清洁设备或食安系统，而是连接它们：

1. 识别异常：漏项、错项、过敏原、封签、温度/持有时间、堵路、无人取餐、回盘超时、清洁逾期、重做报废。
2. 判断优先级：按票据时间、客诉风险、食安风险、桌台周转、浪费金额和人力状态排序。
3. 自动派单：分配给出餐口、跑菜员、店长、清洁员、机器人、后厨工位或人工复核。
4. 验证结案：用 QR、重量、视觉、桌号确认、路线状态、清洁照片、温度日志和员工签名形成证据包。
5. 训练迭代：把低置信度、堵路、人机接管、错单纠正和重做归因导出为 LeRobot episode。

## Market Wedge

首发不做全自动餐厅，而做高峰明显、路线固定、托盘/袋子多、人工步数高、异常可定义的场景。

- QSR / fast casual：出餐袋核验、漏项提醒、定制项、第三方司机交接和 drive-thru 准确率。
- 连锁茶饮/咖啡：出杯节拍、封签、外卖交接、原料过期、培训一致性和低成本复制。
- 火锅/自助/宴会：跑菜、回盘、补餐、清洁 proof、盘余浪费和高峰人力调度。
- 酒店/客房送餐：房号、门禁、电梯、托盘回收、客诉证据和夜间低人力配送。
- 高校/医院/园区食堂：菜单稳定、空间封闭、审计强，适合餐盘分拣、取餐柜和室内配送。
- 中央厨房/档口厨房：称重、分装、贴标、追溯、冷链交接、明厨亮灶和出品一致性。

中国第一优先是 100-1000 家门店的区域连锁茶饮/咖啡/QSR；第二优先是美团/淘宝闪购生态里的品牌卫星店、外卖专门店和档口厨房；第三优先是高校、医院、产业园、交通枢纽食堂。

## Business Model

定价按站点、机器人、任务量、证据模块和总部管理收费。年费应落在保守已验证节省的 25%-35%，买方目标回本小于 6 个月。

- Starter：中国 ¥399-799/点/月；海外 US$99-199/点/月。适合 QSR、ghost kitchen、小连锁；手机/平板确认 + KDS 旁路 + 异常工单。
- Pro：中国 ¥1,200-2,800/点/月；海外 US$299-699/点/月。适合连锁餐厅、中型食堂；1 个 AI/称重/托盘站 + POS/KDS + 清洁 proof。
- Enterprise：中国 ¥3,000-8,000/点/月；海外 US$900-1,800/点/月。适合酒店自助、大型食堂、food court；多站点、多机器人、总部看板和 API。
- Paid Pilot：中国 ¥8,000-30,000/点；海外 US$1,500-6,000/点。60-90 天基线、试点、ROI 和部署方案。

试点经济模型：

`年收益 = 减少错单/退款 + 减少重做/报废 + 减少备餐浪费 + 缩短回盘/清洁周期 + 降低经理追踪工时 + 食安证据价值 - 年化订阅/硬件/实施成本`

## 60-90 天试点指标

- Baseline：先做 10-14 天被动测量。
- 覆盖率：85%-90%+ 营业日和主要 dayparts 有数据。
- 异常关闭：第 30 天 60%+ 异常同班次关闭；第 90 天 80%+ 异常带 owner、原因、动作和验证。
- 浪费/重做：第 60 天 measured avoidable exception cost 下降 8%-15%；第 90 天下降 15%-25%。
- 经济性：第 90 天 verified savings run-rate 达到月费 2x，或展示明确 3x annual ROI 路径。
- 人员负担：人工确认事件采集 15-30 秒内，店长每班复核 <10 分钟。
- 交付质量：错托盘/漏项拦截、handoff delay、route wait、回盘周期、清洁覆盖、robot uptime 和 HIL intervention reason。

这些是试点目标，不是未经客户验证的公开承诺。

## Competition

FoodLoop 不替代 POS/KDS，也不重新造一台送餐机器人。

- POS/KDS：Toast、Square、Oracle MICROS、NCR Aloha、PAR Brink、QSR Automations 负责票据和厨房屏，但不验证物理交付。
- 订单聚合：Olo、DoorDash、Uber Eats、Deliverect、Otter、Chowly/Checkmate 管订单流，但缺少店内托盘/袋子和交接证据。
- 厨房视觉 AI：Agot AI、PreciTaste、Yum Byte/Dragontail 优化站位、产能和品牌自有系统，偏单点。
- 做餐机器人：Miso、Hyphen、Botinkit、Nala 等适合受限工位，但仍需要交付验证、清洁和异常处理。
- 送餐/回盘机器人：Bear、Pudu、Keenon、Richtech、Relay 负责移动，FoodLoop 决定什么时候该动、为何停、如何结案。
- 食物浪费 AI：Winnow、Leanpath、Orbisk、Kitro、Phood 做称重和统计，FoodLoop 把浪费追溯到错单、超时和重做。

## Moat

护城河来自：

- 餐饮异常库：漏项、错项、封签、过敏原、持有时间、堵路、无人取餐、回盘、清洁和重做归因。
- 连接器：Toast、Square、Oracle/NCR、扫码点餐、美团、抖音、微信、机器人 fleet 和清洁设备。
- 证据标准：Order ID、托盘 ID、重量差、图像 crop、封签、温度、路线状态、员工签名和模型版本。
- HIL 数据：堵路恢复、错托盘纠正、客人未取、低置信度、路线等待和人工接管轨迹。
- 门店 benchmarks：同品牌、同菜单、同班次、同店型的异常密度、关闭率、浪费金额和训练收益。
- Edge profiles：QNN/AI Hub profile、延迟、内存、NPU 命中、fallback、签名部署和回滚记录。

## Competition Demo

三分钟 demo：

1. Mock POS/KDS 创建订单 T12-047：主餐、饮料、过敏原标记、桌号 12。
2. KDS 标记 ready 后，FoodLoop edge gate 不允许派车，先做托盘验证。
3. Qualcomm edge 用相机 + 重量/load cells + QR/RFID 检测出饮料缺失，KDS 变红，生成异常证据包。
4. 员工补齐饮料，验证通过，AMR 低速送到桌号。
5. 桌面 QR 或员工平板确认送达，机器人切换回盘，把假脏托盘送回洗碗区。
6. 清洁站扫码 sanitizer/wipe checklist，空托盘传感器和短视频生成清洁 proof。
7. 人为制造堵路，人工接管恢复；系统保存 LeRobot HIL episode。
8. Dashboard 展示 order event、robot task、food-safety event、exception evidence、AI Hub/QNN profile 和下一次部署门禁。

安全约束：

- 使用封闭假餐，无热液体，无开放烹饪。
- 低速、限定路线、围挡、物理急停、无线 deadman、现场安全员。
- ML 不能直接越过安全 supervisor；动作被限制在允许区域和允许速度。
- 不做人脸识别、顾客画像或员工监控叙事。
- 不声称食品安全认证，只展示可审计辅助记录。

## Why Qualcomm

餐厅高峰是 Qualcomm edge AI 的真实压力测试：

- Edge Vision：托盘、菜品/容器、QR、封签、桌号、湿滑地面、障碍和清洁站都在本地识别。
- AI Runtime：AI Hub、QNN、QAIRT、ONNX Runtime QNN EP 和量化 profile 让模型上线可验证。
- Robotics Stack：ROS 2、Nav2、Open-RMF、多机器人调度、keepout/speed zones 和接管记录可在 edge 上整合。
- Privacy / Offline：顾客和员工画面边缘脱敏；断网时仍可核验、派单、缓存证据和安全停靠。
- Hardware Path：RB3 Gen 2/QCS6490 做比赛原型，RB5/RB6/IQ10 RRD 形成多摄像头和生产路线。

Qualcomm 的战略价值：把“机器人开发板”升级成“餐饮服务机器人参考架构”，把低延迟感知、连接、隐私、模型部署和 fleet lifecycle 放到同一个可复制样板里。

## Claims To Avoid

- 不说全自动餐厅、替代服务员或替代厨师。
- 不承诺固定 ROI、固定节省 FTE、固定吞吐提升。
- 不声称 NSF/UL/HACCP/FDA/CE 等认证，除非具体硬件已认证。
- 不承诺开放式烹饪或危险热源自主操作。
- 不做人脸识别、顾客画像或监控优先叙事。
- 不说 99% 菜品识别、零误报、无需员工行为改变。
- 不声称实时从零训练或 Qualcomm/LeRobot 官方认证。

## Sources

- NRA 2026 State of Restaurant Industry：https://restaurant.org/research-and-media/research/research-reports/state-of-the-industry/
- Restaurant margins：https://restaurant.org/issues-and-advocacy/policy-agenda/tax-policy/
- China Catering 2025：https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html
- China Catering 2026 YTD：https://www.stats.gov.cn/sj/zxfb/202606/t20260616_1963949.html
- UNEP Food Waste Index 2024：https://www.unep.org/resources/publication/food-waste-index-report-2024
- Champions 12.3 restaurant food waste：https://champions123.org/publication/business-case-reducing-food-loss-and-waste-restaurants
- ReFED restaurants and foodservice：https://refed.org/stakeholders/restaurants-and-foodservice/
- QSR Drive-Thru Report：https://www.qsrmagazine.com/story/the-2025-qsr-drive-thru-report/
- Order accuracy study summary：https://www.restaurantdive.com/news/study-diners-are-dependent-on-food-delivery-but-are-sensitive-to-order-inaccuracies/623372/
- IFR service robots：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Keenon / Xinhua：https://www.news.cn/20250528/bd49185b0c8740dcb8a4eed8cffe3276/c.html
- Bear Servi Plus：https://www.bearrobotics.ai/servi-plus
- Pudu BellaBot：https://www.pudurobotics.com/en/products/bellabot
- Chipotle Hyphen：https://newsroom.chipotle.com/2024-09-16-CHIPOTLE-DEBUTS-AUTOCADO-AND-THE-AUGMENTED-MAKELINE-BY-HYPHEN-IN-RESTAURANTS
- Botinkit：https://botinkit.ai/
- Square Orders API：https://developer.squareup.com/docs/orders-api/what-it-does
- Toast order webhooks：https://doc.toasttab.com/doc/devguide/devOrdersWebhookRef.html
- FDA Food Code 2022：https://www.fda.gov/food/fda-food-code/food-code-2022
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm QNN SDK：https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- Nav2 Collision Monitor：https://docs.nav2.org/configuration/packages/collision_monitor/configuring-collision-monitor-node.html
- Open-RMF：https://openrmf.readthedocs.io/
- LeRobot HIL：https://huggingface.co/docs/lerobot/en/hil_data_collection
