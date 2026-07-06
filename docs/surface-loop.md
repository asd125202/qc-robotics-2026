# SurfaceLoop 表面工程放行层 Pitch

更新时间：2026-07-06。

## One-Line Company

SurfaceLoop 是船厂、重钢、风电、汽车和航空表面工程的放行证据层：

> 把前处理、环境、膜厚/粗糙度、缺陷、机器人/人工返工、检验员签核和付款/质保证据变成一个可追溯 release packet。

## YC-Style Opening

### Problem

表面工程的失败，通常不是因为没人干活，而是证据在交付前断掉。

- 业主/总包关心停航、停线、干坞延期、质保争议和付款依据。
- 船厂/涂装主管面对多班组、多区域、多设备并行施工，真正拖慢交付的是返工票、复检排队和资料退回。
- 承包商在前处理或涂装问题发现太晚时损失利润，且责任边界很难证明。
- 第三方检验员需要把照片、DFT、profile、温湿度、批次、返工和签名整理成可审计文档。

### Why Now

- AMPP/NACE 常用口径：全球腐蚀年度成本约 2.5 万亿美元。
- 中国 2025 年造船完工量占全球 56.1%，2026 年一季度新接船舶订单全球份额达到 84.9%。
- 中国 2025 年新增风电装机约 120GW，累计风电约 640GW，塔筒、叶片和海上维护带来重复表面检验需求。
- 中国 2025 年工业机器人产量 773,074 台，AI+制造政策要求在线智能检测、质量追溯和工业智能体。
- HII HYPR、GrayMatter、Blastman、VertiDrive、AMBPR、FANUC、FerRobotics 等信号说明表面执行层正在自动化，但放行证据层仍碎片化。

### Core Insight

涂料公司卖材料，机器人公司卖动作；客户真正买的是可付款、可质保、可审计的放行决定。

Defensible dataset 不是更多锈蚀图片，而是：

```text
surface before state
+ prep method
+ environment
+ profile / DFT / batch
+ defect decision
+ rework action
+ inspector disposition
+ owner acceptance
+ final release
```

## Product

SurfaceLoop 是设备中立的 Surface Release Packet Layer。它坐在机器人、巡检、涂装设备、手机和仪器之上，把现场动作变成可关闭的表面工作包。

1. Spec：导入资产、区域、涂层体系、前处理标准、hold point、责任班组和放行条件。
2. Capture：采集照片、视频、DFT/profile、温湿度、批次、机器人轨迹、工具状态和检验员批注。
3. Flag：端侧识别锈蚀、残留旧涂层、漏打磨、针孔、橘皮、膜厚风险和低置信度区域。
4. Route：把问题派给人工、机器人、承包商或第三方复检。
5. Close：绑定返工动作、低力接触、复检照片、测量值和人工接管。
6. Release：生成 before/after、测量、模型版本、签名、返工历史和 owner-ready release packet。
7. Learn：低置信度、返工、复检、人工接管和改判进入 LeRobot/HIL 数据闭环。

## Market Wedge

先从 shipyard / heavy steel coating release work package 切入。

原因：

- 大面积、多班组、强检验、弱网络、数据敏感。
- 一次返工、一天干坞延期或一次资料退回就能证明 ROI。
- 业主、承包商、检验员和项目控制都有同一份 release packet 需求。
- 已有机器人表面处理和纸less QA 信号，客户教育成本下降。

扩展路径：

ship repair -> newbuild ship blocks -> tanks/terminals -> bridges -> wind towers/blades -> rail/steel fabrication -> auto paint/body -> aerospace MRO.

中国目标客户：

- 船厂：CSSC 江南、沪东中华、外高桥、大连、广船国际，COSCO Heavy，招商金陵，扬子江，新纪元，恒力重工。
- 汽车：BYD、SAIC/VW、FAW-Hongqi、Geely/Zeekr、Chery、Changan、GAC Aion、NIO、XPeng、Li Auto、Xiaomi EV。
- 风电：Goldwind、Envision、Mingyang、Sany Renewable、Shanghai Electric、Dongfang Electric、Windey、CRRC Zhuzhou。
- 轨交/航空：CRRC、COMAC/SAMC、AVIC、AECC、MRO 厂。

## Business Model

定位：不是表单软件，而是 constraint-day insurance 和 defensible release packet。

建议价格：

- 90 天试点：海外 7.5k-15k 美元/项目工作包；中国 5-10 万元。覆盖模板、5-10 用户、现场 onboarding 和 ROI 报告。
- 年度项目订阅：18k-36k 美元/站点或项目团队/年，外加 75-150 美元/现场用户/月；业主/检验员查看免费。
- 企业业主版：50k-150k 美元/年，覆盖多团队、SSO、审计、数据留存、owner reporting 和系统集成。
- 边缘证据节点：按节点租赁或一次性硬件加软件维护，负责多相机接入、弱网缓存、模型 profile 和证据同步。

ROI 公式：

```text
ROI =
  (admin labor saved
 + rework avoided
 + constraint days avoided
 + faster release / invoice value
 + dispute and audit cost avoided
 - SurfaceLoop cost)
 / SurfaceLoop cost
```

90 天 KPI：

- release packet 编制时间下降 30%-50%。
- 资料退回/缺字段率下降 50%，missing required fields <2%。
- required hold points captured digitally = 100%。
- inspection to reviewed report <24h。
- out-of-spec DFT/profile 或表面缺陷在下一道涂层前被发现。
- zero schedule delays caused by missing QA documentation。

## Competition

SurfaceLoop 不应声称自己是第一个表面机器人或检测系统。

- GrayMatter / Blastman / VertiDrive / AMBPR / KUKA / Durr / FANUC / FerRobotics：强在机器人执行。
- Gecko Robotics / Square Robot / Apellix / Voliro：强在资产巡检。
- Cognex / Keyence / Hikrobot / Basler / MVTec：强在机器视觉工具。
- Maximo / SAP / ServiceNow / MES / CMMS / Ship OS：强在系统记录。

SurfaceLoop 的差异：跨设备、跨班组、跨检验点关闭表面工作包。它不是执行器或巡检器，而是 release packet layer。

## Moat

- Surface evidence graph：before/after、DFT/profile、环境、缺陷、返工动作、复检和签核连成可查询图谱。
- Domain dataset：低置信度、人工纠错、机器人轨迹、测量值、返工结果和最终放行结果绑定在同一 surface zone。
- Workflow lock-in：业主、承包商、检验员、项目控制和质保团队共用同一个 release packet 格式。
- Equipment neutrality：可接机器人、爬壁车、无人机、手机、膜厚仪、粗糙度仪和既有 MES/CMMS。
- Edge deployment know-how：Qualcomm 模型 profile、离线缓存、弱网同步、回滚和数据不出厂变成部署资产。

## Architecture

比赛 demo 使用安全桌面 coupon，不做真实喷涂、溶剂、金属粉尘或高能打磨。DFT/profile 字段默认模拟，只有接入校准仪器时才作为真实测量。

### Field Stack

- 双 RGB 相机，可选 depth/thermal。
- Spring-loaded probe + 1-axis load cell / HX711，或 wrist F/T。
- Coupon QR ID、fixture clamp switch、E-stop。
- ROS 2 负责低层 motion、joint state、image、force topic 和安全 supervisor。
- LeRobotDataset v3 保存多相机视频、state/action、force、intervention、label 和模型版本。

### AI Stack

- 云端/GPU：训练和 fine-tune perception model / evidence classifier / HIL policy。
- Qualcomm edge：部署 compact defect segmentation、quality scoring、contact-state classifier。
- AI Hub / QNN：对目标 SoC compile/profile，使用 ONNX Runtime QNN 或 AI Hub 生成的 profile artifacts。
- 安全边界：AI 只给缺陷、建议和证据；速度/力上限、tool interlock、E-stop、人工签核在确定性系统和人类流程中。

## Competition Demo

3 分钟演示：

1. Place coupon under robot. Show zone map and surface work package。
2. Edge camera detects simulated dust nib / scratch / thin coating / missed sanding area。
3. Probe touches ridge/patch at low force. Load-cell trace + mock DFT/profile attach to evidence card。
4. Intentionally trigger drift or missed ridge. Human pauses, teleoperates correction, resumes。
5. Show LeRobotDataset episode: MP4 frames + Parquet state/action/force/labels。
6. Run compact model on Qualcomm edge while disconnected from cloud。
7. Generate pass/fail/needs-review release packet and close the surface NCR。

## Why Qualcomm

- 表面工程发生在弱网、粉尘、噪声和数据敏感的现场，原始视频不应默认上传公有云。
- 多相机和传感器 ingestion 适合本地边缘处理。
- 缺陷分割、quality scoring、evidence classifier 可以通过 AI Hub / QNN / QAIRT 编译和 profile。
- RB3 Gen 2 / QCS6490 级边缘节点可作为相机、传感器、ROS 2 和证据包的现场枢纽。
- 中国私有部署和海外云 GPU 训练可以共享同一 job contract，默认数据不出厂。
- 这是 Qualcomm robotics ecosystem 可展示的商业化参考应用：不是 demo toy，而是工业工作流。

## Claims To Avoid

- 不说零腐蚀。
- 不说零返工。
- 不说替代检验员。
- 不说自动认证或 ASTM/AMPP/IMO compliance 已完成。
- 不说 camera-only 可以真实测量 DFT/profile。
- 不说全自动喷涂/打磨可覆盖任意场景。
- 不说生产汽车/飞机漆面返修已完成。
- 不说云端在安全控制环内。
- 不说任意 PyTorch/VLA 模型可直接跑 QNN。

## Sources

- AMPP corrosion cost: https://www.ampp.org/blogs/webmasternaceorg/2023/04/14/ampp-recognizes-world-corrosion-awareness-day-impa
- Graco surface prep standards: https://www.graco.com/gb/en/contractor/solutions/articles/surface-prep-standards-explained-sspc-nace-iso-8501.html
- AMPP coating inspector program: https://www.ampp.org/education/education-resources/courses-by-program/coating-inspector-program/cip-1
- IMO PSPC: https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/MSCResolutions/MSC.215%2882%29.pdf
- China shipbuilding 2025: https://news.cctv.com/2026/02/01/ARTIPRaqs8PSuxG3vQVoILPF260201.shtml
- China shipbuilding Q1 2026: https://www.news.cn/20260509/94566f90a53d411682a1eeecf1b2a5d0/c.html
- China wind 2025: https://www.nea.gov.cn/20260212/742b8c6a078347b0b39de676c05c5d58/c.html
- China robots 2025: https://www.stats.gov.cn/sj/zxfb/202601/t20260119_1962329.html
- GrayMatter surface robotics: https://graymatter-robotics.com/solutions/
- HII HYPR: https://www.hii.com/news/hii-launches-hypr-program-with-path-robotics-and-graymatter-robotics-to-accelerate-production-at-scale
- Blastman shipbuilding: https://www.blastman.com/references/ship-building.html
- VertiDrive abrasive blasting: https://www.vertidrive.com/abrasive-blasting/
- Damen AMBPR robots: https://www.damen.com/services/shiprepair/projects/dsdu-takes-delivery-of-five-ambpr-robots
- FANUC paint repair: https://www.fanucamerica.com/case-studies/first-ever-robotic-paint-repair-solution-on-a-moving-automotive-line
- FerRobotics ACF-K: https://www.ferrobotics.com/en/services/products/active-contact-flange-kit/
- NSRP paperless paint QA: https://www.nsrp.org/wp-content/uploads/2018/05/2016-428-Implementation-Robust-Paperless-Paint-Final-Report.pdf
- LeRobot HIL: https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Qualcomm AI Hub: https://workbench.aihub.qualcomm.com/docs/
- Qualcomm RB3 Gen 2: https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
