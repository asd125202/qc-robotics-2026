# SurfaceLoop 表面工程证据闭环 Pitch

更新时间：2026-07-06。

## One-Line Company

SurfaceLoop 让每一平方米钢表面都有可验证的施工记忆：

> 把除锈、打磨、喷涂、复检、返工和放行变成可审计工作包。边缘 AI 看到表面风险，机器人/人工完成受控返修，检验员签核 release packet，低置信度和接管片段进入 LeRobot 数据闭环。

## Problem

表面工程不是“刷一层漆”，而是交付前最容易丢证据的质量关口。

- 业主为腐蚀、停航/停线、质保、重涂、脚手架、干坞、索赔和工期延误付费。
- 承包商在前处理或涂装问题发现太晚时损失利润，还很难证明责任边界。
- 检验员依赖照片、DFT、粗糙度、温湿度、纸单和手工抽检。
- 机器人和相机能采集数据，但数据很少变成完整的 closed work package。

## Why Now

- AMPP/NACE IMPACT 常用口径：全球腐蚀年度成本约 2.5 万亿美元，成熟腐蚀控制措施可节约 15%-35%。
- Manufacturing Institute / Deloitte 2024 预测美国制造业到 2033 年可能需要 380 万名新员工，其中 190 万岗位可能空缺。
- HII 与 GrayMatter Robotics 在 2026 年签署 MOU，将 autonomous surface preparation、coating 和 inspection 引入造船。
- HII HYPR 计划把 robotic welding、material movement、autonomous surface treatment 和 autonomous quality checks 放进 2026 proof / 2027 pilot。
- Aerobotix 2026 年获得 120 万美元 Air Force DP2 SBIR，用于 F-35 robotic scuff sanding。
- FANUC / GM / 3M / Inovision 在移动汽车产线上部署 robotic paint repair。
- 中国 2025 年造船完工量占全球 56.1%，新增风电 120GW，汽车 NEV 销售占比在 2026 年 5 月达到 56.9%。
- 中国制造政策强调在线智能检测、质量追溯、AI + manufacturing、具身智能示范线和工业智能体。

## Core Insight

涂层不是产品，放行包才是产品。

Defensible dataset 不是更多锈蚀图片，而是：

`surface before state + prep method + environment + surface profile + coating recipe + DFT + defect decision + inspector disposition + rework result + final release`

## Solution

SurfaceLoop 是表面前处理、涂装 QA 和返工放行的工作包层：

1. Import：导入资产、区域、涂层体系、前处理标准、hold point 和检验计划。
2. Capture：从相机、DFT、粗糙度、温湿度、机器人、手机和检验员批注采集证据。
3. Flag：端侧识别锈蚀、旧涂层残留、漏打磨、针孔、橘皮、膜厚风险和低置信度区域。
4. Rework：对缺陷区域生成返修 patch，机器人或人工在受力/速度/材料边界内处理。
5. Close：生成 before/after、测量、模型版本、人工批准、返工历史和放行包。
6. Learn：低置信度、补拍、返工、复检和人工改判进入 LeRobot/HIL 数据闭环。

## Market Wedge

先从 shipyard / heavy steel coating release work package 切入。

原因：

- 高价值资产。
- 大面积钢结构。
- 强检验、强争议、强证据需求。
- 弱网络和数据敏感，适合 edge-first。
- 已有 HII/GrayMatter/Blastman 等自动化信号。

扩展路径：

ship repair -> newbuild ship blocks -> tanks/terminals -> bridges -> wind towers/blades -> rail/steel fabrication -> auto paint/body -> aerospace MRO.

中国目标客户：

- 船厂：CSSC 江南、沪东中华、外高桥、大连、广船国际，COSCO Heavy，招商金陵，扬子江，新纪元，恒力重工。
- 汽车：BYD、SAIC/VW、FAW-Hongqi、Geely/Zeekr、Chery、Changan、GAC Aion、NIO、XPeng、Li Auto、Xiaomi EV。
- 风电：Goldwind、Envision、Mingyang、Sany Renewable、Shanghai Electric、Dongfang Electric、Windey、CRRC Zhuzhou。
- 轨交/航空：CRRC、COMAC/SAMC、AVIC、AECC、MRO 厂。

## Business Model

收入模型：

> paid pilot + site subscription + edge nodes + integrations + optional verified-savings fee

建议价格：

- 试点：5-15 万美元/站点/工作流，或中国 30-100 万元。
- 生产订阅：5k-25k 美元/site/月，按资产、用户、工作包、证据存储和模型服务分层。
- 边缘节点：1k-3k 美元/节点/月。
- 集成：MES/CMMS/EAM/Ship OS/QMS 实施费。
- 成功费：按返工减少、放行加速或争议减少分享 verified savings。

ROI 公式：

```text
Rework cost =
  sanding_hours * loaded_rate
+ paint_touchup_hours * loaded_rate
+ QA_reinspection_hours * loaded_rate
+ consumables + paint/materials + waste disposal
+ constraint_delay_days * cost_per_constraint_day
+ scrap_probability * part_or_area_replacement_cost

Pilot ROI =
  (verified_savings - pilot_fee - buyer_internal_cost)
  / (pilot_fee + buyer_internal_cost)
```

90 天 KPI：

- 从“表面完成”到“检验放行”的平均时间下降 20%-35%。
- 每 100 平米 / aircraft zone / blade / ship section 返工小时下降 20%-35%。
- 至少避免 1 个 constraint day。
- 关键缺陷 recall >=90%，误报不增加净 QA 时间。
- 95%+ NCR/返工票带 before/after、测量值、区域、处置、复检和检验员签核。

## Competition

- GrayMatter / Blastman / VertiDrive / AMBPR / KUKA / Durr：强在机器人执行。
- Gecko Robotics / Square Robot / Apellix / Voliro：强在资产巡检。
- Cognex / Keyence / Hikrobot / Basler / MVTec：强在机器视觉工具。
- Maximo / SAP / ServiceNow / MES / CMMS / Ship OS：强在系统记录。

SurfaceLoop 的差异：关闭表面工作包，跨前处理、涂装、返工、检验和放行。

## Moat

- Surface evidence graph：资产、区域、前处理状态、涂层配方、测量值、缺陷、处置和放行。
- Domain dataset：before/after、低置信度、人工纠错、机器人轨迹、DFT/profile、返工结果。
- Workflow lock-in：业主、承包商、检验员和项目控制共用同一个 release packet。
- Integrations：MES、CMMS、EAM、Ship OS、document control、coating specs、QA forms。
- Edge profiles：Qualcomm-optimized models、离线缓存、弱网同步、回滚和安全边界。

## Architecture

比赛 demo 使用安全桌面 coupon，不接触真实喷涂、溶剂、金属粉尘或高能打磨。

### Sensors

- Front RGB camera。
- Wrist RGB camera。
- Optional depth / structured-light height map。
- Wrist F/T or fixture load cell。
- Tool RPM/current。
- Vibration/IMU。
- Coupon QR ID。
- Fixture clamp switch。
- E-stop。

### ROS 2 Topics

- `/camera/front/image_rect`
- `/camera/wrist/image_rect`
- `/surface/height_map`
- `/surface/defect_mask`
- `/surface/rework_plan`
- `/tool/ft_raw`
- `/tool/ft_filtered`
- `/tool/rpm_state`
- `/tool/current`
- `/force_ctrl/target`
- `/hil/intervention`
- `/episode/event`
- `/qnn/perf`

### Edge AI

Runs well on Qualcomm edge / QNN:

- Defect detector / segmenter。
- Coverage / risk flagger。
- Contact-state classifier from F/T, current, vibration。
- Quality pass/fail classifier on before/after crops。
- AI Hub compile/profile/package evidence。

Runs outside QNN:

- F/T filtering。
- Force/admittance control。
- Watchdogs, geofence, tool interlock。
- ROS 2 graph and MCAP recording。
- Patch generation and safety supervisor。

Cloud:

- LeRobot training/fine-tuning。
- HIL dataset curation。
- Evaluation replay。
- Larger VLA/LLM experiments。
- Dashboard analytics。

## Competition Demo

3 分钟 demo：

1. Edge camera detects simulated dust nib / scratch / missed sanding area on a safe coupon。
2. System opens surface NCR with defect mask and work-package context。
3. System generates bounded rework patch: target force, speed, dwell, and tool mode。
4. Robot uses low-force felt/foam pad; force spike or mask drift pauses motion。
5. Human performs HIL correction if needed。
6. System rescans, compares before/after, and inspector approves on tablet。
7. Release packet is generated and the HIL episode is saved to LeRobotDataset。

## Why Qualcomm

- Surface work occurs in harsh, weak-network, data-sensitive industrial sites。
- Multi-camera and sensor ingestion benefit from local edge processing。
- Defect segmentation and quality scoring can be compiled/profiled through AI Hub / QNN / QAIRT。
- Factory/shipyard/auto data should not default to raw public-cloud upload。
- LeRobot HIL corrections create training data; profiled artifacts return to Qualcomm edge。
- China private deployment and overseas cloud training can share the same job contract。

## Claims To Avoid

- 不说零腐蚀。
- 不说零返工。
- 不说替代检验员。
- 不说自动认证。
- 不说全自动喷涂/打磨可覆盖任意场景。
- 不说生产汽车/飞机漆面返修已完成。
- 不说云端在安全控制环内。
- 不说任意 PyTorch 模型可直接跑 QNN。

## Sources

- AMPP corrosion campaign: https://www.ampp.org/blogs/webmasternaceorg/2025/04/22/global-campaign-urges-action-on-corrosion-crisis
- AMPP surface prep standards: https://blogs.ampp.org/protectperform/surface-prep-standards-a-quick-summary
- Manufacturing Institute / Deloitte workforce: https://themanufacturinginstitute.org/manufacturers-need-as-many-as-3-8-million-new-employees-by-2033/
- IFR World Robotics 2025: https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- HII GrayMatter MOU: https://hii.com/news/hii-teams-with-graymatter-robotics-to-integrate-physical-ai-into-manned-and-unmanned-shipbuilding
- HII HYPR: https://hii.com/news/hii-launches-hypr-program-with-path-robotics-and-graymatter-robotics-to-accelerate-production-at-scale
- Aerobotix F-35 sanding: https://aerobotix.net/aerobotix-secures-1-2m-air-force-dp2-sbir-contract-for-robotic-scuff-sanding-on-f-35-aircraft/
- FANUC GM paint repair: https://www.fanucamerica.com/case-studies/first-ever-robotic-paint-repair-solution-on-a-moving-automotive-line
- FerRobotics SEAT/Cupra paint repair: https://www.ferrobotics.com/en/references/case-studies/seat-cupra-robotic-paint-repair-sanding-polishing/
- China shipbuilding 2025: https://news.cn/fortune/20260224/421f9de6ac8548c8a9112099698c43cb/c.html
- China wind 2025: https://www.nea.gov.cn/20260212/742b8c6a078347b0b39de676c05c5d58/c.html
- CAC auto data rules: https://www.cac.gov.cn/2021-08/20/c_1631049984897667.htm
- LeRobot HIL: https://huggingface.co/docs/lerobot/en/hil_data_collection
- LeRobotDataset v3: https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Qualcomm AI Hub: https://workbench.aihub.qualcomm.com/docs/
- QNN / QAIRT: https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/general_introduction.html
- Qualcomm RB3 Gen 2: https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
