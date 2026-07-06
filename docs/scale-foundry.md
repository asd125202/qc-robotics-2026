# ScaleFoundry Pitch

更新时间：2026-07-06。该版本按 `docs/pitch-deck-standard.md` 重写，定位为 Dragonwing 机器人从原型到可报价、可生产、可维护 SKU 的产品化层。

## One-Liner

ScaleFoundry 不造机器人，而是把 Dragonwing 机器人从“能跑 demo”铸成“可报价、可生产、可维护 SKU”的产品化流水线：BOM、EVT/DVT/PVT、工厂测试、认证证据、Golden Image、FRU、PCN/PDN 和现场故障反馈全部连成一条产品化图谱。

## 1. Problem

这台机器人今天能动，但客户不敢买 500 台。

机器人团队越来越容易做出 demo，却很难把 demo 变成可复购 SKU。真正卡住量产的不是单个算法，而是：

- 传感器同步、实时控制、散热、电源、线束和机构。
- OTA、安全启动、设备密钥、调试口关闭和 Golden Image。
- DFM/DFA、测试夹具、EOL 测试、Golden Sample 和 PVT 良率。
- FCC/CE/RED/EMC、电池运输、机器人安全、功能安全、说明书和标签。
- BOM、AVL、二供、PCN/PDN、ECO、备件、FRU、RMA 和现场故障闭环。

如果这些没有系统化，demo 会动，但采购、工厂、认证实验室、售后和投资人都不敢把它当产品。

## 2. Current Alternatives Fail

开发板、ODM、集成商、PLM、MES、fleet ops 都只解决半题。

- Devkit：RB3、IQ EVK 和参考设计降低原型门槛，但不会自动生成量产测试、认证包和 FRU 策略。
- ODM / CM：Jabil、Plexus、Sanmina 等强在 NPI 与生产执行，但通常要求客户先定义清楚产品和测试。
- PLM / MES：Arena、Duro、Tulip、Aegis 能管 BOM 和工厂，却不懂 mission success、intervention rate、校准和模型版本。
- Fleet ops：Formant、InOrbit、Foxglove 擅长运维和调试，但现场 failure 不会天然回到 DVT/PVT 和供应商 CAPA。
- Consulting：传统产品化顾问能救一个项目，但很难沉淀跨机器人、跨供应商、跨工厂的产品化数据资产。

ScaleFoundry 的边界：不正面做 PLM、MES、fleet ops 或 CM。它是这些系统之间的机器人语义层。

## 3. Solution

ScaleFoundry 是 Dragonwing 机器人产品化操作系统。

核心流程：

1. Audit：2-4 周生成 SKU 风险图谱，覆盖热、电源、接口、BOM、OTA、安全、认证、制造和服务风险。
2. Gate：把 EVT/DVT/PVT/MP 变成可审计门禁，补上 autonomy、calibration、MTBF 和 serviceability 指标。
3. Package：生成 CM Readiness Pack：BOM、治具、作业指导、EOL 测试、Golden Image、追溯和验收标准。
4. Launch：小批试产、良率爬坡、认证资料、标签说明书、备件包、RMA 和 UptimeOS/RiskLedger 接入。
5. Learn：现场失败、制造缺陷和供应商问题回写 ECO/CAPA、下一版 DVT 和 verified recipe。

客户买到的不是咨询 PPT，而是能交给 ODM、试点客户、认证实验室和售后团队的出货资产。

## 4. Why Now

Physical AI 正在从展台进入工厂，产品化断层会成为产业瓶颈。

- IFR 2025 显示，2024 年全球工业机器人安装约 54.2 万台，中国占全球新装机 54%。
- 专业服务机器人和 RaaS 增长说明机器人正在从 demo 进入真实部署。
- McKinsey 对 humanoid 商业化的判断包括安全、uptime、灵巧/移动能力、成本和供应链约束。
- Qualcomm 2025 年整合 Dragonwing 品牌，2026 年推出 IQ10 Robotics Reference Design，把 compute、sensing、networking、software 和 prototype-to-production 放到一个叙事中。
- AI Hub、Edge Impulse、FoundriesFactory、Ubuntu/Yocto、Dragonwing IQ/RB 平台和模组伙伴已经形成一套可产品化的基础设施。

机会点：Qualcomm 有很多 building blocks，但客户仍需要一条可采购、可认证、可维护、可部署十年的产品路径。

## 5. Product

ScaleFoundry 的核心产品是 `Productization Graph`。

它让每台样机、每个 build、每批工厂件、每次现场故障都能追溯到设计、供应商、测试、软件、模型和服务记录。

核心 artifact：

- `sku-readiness-report.pdf`：热、电源、I/O、传感器、BOM、认证、制造、服务和安全风险图谱。
- `dragonwing-sku-kit.yaml`：QCS6490/QCS5430、IQ8、IQ9、IQ10 的 target、OS、ROS 2、AI Hub/QNN 和连接配置。
- `evt-dvt-pvt-gates.json`：DFMEA、DFA/DFM、验证矩阵、可靠性、预扫、认证样机、PVT 良率和 MP 准入标准。
- `cm-readiness-pack.zip`：EBOM/MBOM/Service BOM、AVL、EOL 测试、治具需求、SOP、Golden Image 和追溯 schema。
- `lifecycle-ledger.json`：SoC 供货期、BOM 版本、OS/kernel、SBOM/CVE、模型版本、认证状态、PCN/PDN 和迁移路径。
- `field-capa-loop.jsonl`：现场 RMA、UptimeOS 事件、RiskLedger 事故、供应商 CAPA、ECO 和下一版 build gate。

建议产品模块：

- Prototype Audit：48 小时到 2-4 周内生成 SKU 风险图谱。
- Dragonwing SKU Kit：面向 AMR、巡检、配送、机械臂/人形上身控制器的参考硬件和软件包。
- Robot NPI Gates：EVT/DVT/PVT/MP，加上 autonomy、safety、calibration、mission success、intervention rate、MTBF 和 serviceability。
- Certification Kit：FCC/CE/IC/UKCA/EMC/安全/网络安全/电池/说明书/标签文档矩阵。
- Lifecycle Ledger：Product Longevity、OS LTS、CVE/SBOM、模型版本、OTA、认证状态、FRU 和迁移路径。
- Closed-loop ECO/CAPA：把现场 failure 回写到设计、供应商、工站、软件版本或模型版本。

## 6. Market And Business Model

最先付钱的人，是已经有原型、客户压力或量产窗口的人。

优先买方：

- 机器人初创：demo 已跑通，但缺 DFM、供应链、测试治具、认证、EVT/DVT/PVT 经验。
- 机器人/设备 OEM：新 SKU 上市、降 BOM、补边缘 AI/ROS 2/安全能力。
- Qualcomm/Dragonwing 生态伙伴：需要把 RB3/IQ/IQ10 参考设计变成生产机器人平台。
- 企业实验室/自动化团队：需要从 POC 进工厂/仓库/园区试点，ROI 要过 CFO。
- 系统集成商：想把一次性项目变成可复制机器人单元或行业套件。
- CM/ODM、测试实验室、认证顾问、模组伙伴：更适合做渠道和联合交付方。

建议价格带：

- 中国 SKU Readiness Audit：`¥10万-30万`。
- 海外 SKU Readiness Audit：`$25k-$75k`。
- 中国 EVT Sprint：`¥60万-200万 + BOM`。
- 海外 EVT Sprint：`$150k-$400k + BOM`。
- 中国 DVT/Pilot：`¥150万-500万 + BOM`。
- 海外 DVT/Pilot：`$300k-$1M + BOM`。
- 中国 PVT/Launch：`¥300万-1200万 + BOM/治具`。
- 海外 PVT/Launch：`$500k-$3M + BOM/fixtures`。
- 持续支持：中国 `¥3万-15万/月`，海外 `$5k-$50k/月`。

商业模式：

1. Paid diagnostic：低摩擦入口，2-4 周，输出 BOM、风险、认证路径、NPI 预算。
2. Milestone NRE：EVT/DVT/PVT 分阶段 SOW，每阶段有 acceptance criteria。
3. Launch subscription：量产后按月收质量、BOM、固件、认证、供应商管理支持。
4. Unit economics add-on：高价值机器人可叠加 `$50-$300/台/月` 或 `1%-3% COGS royalty`，可设置上限方便采购批准。
5. Partner marketplace：CM、测试实验室、供应商、认证顾问、返修服务商和模组伙伴分成。

ROI 逻辑：少一次硬件大改版、少一次认证返测、更快 PVT/MP、更低 BOM、更少现场故障。不要承诺固定降本或良率，应该用项目基线验证。

## 7. Competition And Moat

ScaleFoundry 的壁垒不是顾问能力，而是机器人产品化数据和工作流嵌入。

竞争格局：

- 硬件产品化/工程服务：Synapse、Kickr、Dragon Innovation/Avnet、Fictiv、Simplexity。
- 合同制造/EMS/ODM：Jabil、Flex、Plexus、Benchmark、Sanmina、Celestica、Foxconn FII。
- 机器人开发/运行平台：ROS、NVIDIA Isaac、Intrinsic、Viam、Polymath。
- 机器人运维/数据平台：Formant、InOrbit、Foxglove、Boston Dynamics Orbit。
- IoT/嵌入式生命周期：Memfault、Mender、balena、Particle。
- 测试自动化/制造数据：NI TestStand、Keysight PathWave、Instrumental、Arch Systems。
- PLM/QMS/MES：Arena、Duro、Tulip、MasterControl、Siemens Opcenter、Aegis FactoryLogix、SAP DM。

ScaleFoundry 的 wedge：

- Productization Graph：每台机器人绑定 BOM revision、firmware、model、calibration、供应商批次、测试结果、现场事件。
- Robot NPI Gates：EVT/DVT/PVT/MP 之外加入 autonomy、safety、calibration、mission success、intervention rate、MTBF、serviceability。
- CM Readiness Package：自动生成制造包、测试夹具需求、作业指导、验收标准、良率 dashboard、风险清单。
- Closed-loop ECO/CAPA：现场故障和制造缺陷归因到设计、供应商、工站、软件版本或模型版本。
- Supplier/Test Playbooks：机器人专用 DfT、DfR、DfS、burn-in、HIL/SIL、site acceptance、safety case 模板。

长期护城河：

- 跨项目 failure-mode 数据库。
- AMR、机械臂、人形、无人机、field robot 的测试与验收模板库。
- CM/供应商/实验室网络。
- 和 Arena/Duro/Tulip/Aegis/Memfault/Viam/Foxglove/Formant 的集成。
- 单机级 build history、质量记录和现场记录带来的迁移成本。

## 8. Why Qualcomm

Dragonwing 已有拼图，ScaleFoundry 把拼图变成客户能采购、能认证、能部署十年的产品路径。

ScaleFoundry 不复制 AI Hub、Edge Impulse 或 FoundriesFactory，而是把它们编排进量产路径：

- Verified Recipes：RB3 零售视觉、IQ-8275 工业相机、IQ-9075 多路视频/AMR、IQ10 机器人 blueprint。
- Lifecycle Ledger：记录 SoC 供货期、BOM 版本、OS/kernel、SBOM、CVE、模型版本、OTA wave、认证文件、备选模组。
- Benchmark-to-BOM：用 AI Hub/Edge Impulse/QDC 做真实模型 benchmark，把结果转成成本、功耗、热设计、内存、相机数量和 SoC 推荐。
- Certification Kit：把 FCC/CE/IC/UKCA/EMC/安全/网络安全文档和测试计划模板化。
- Migration Contract：围绕性能等级抽象应用，支持 QCS5430 ↔ QCS6490、RB3 ↔ IQ8/IQ9、IQ9 ↔ IQ10 的迁移策略。

Qualcomm 获益：

- 提高 Dragonwing 从评估板到量产的转化率。
- 让 Product Longevity Program 变成企业生命周期方案，而不是网页供货日期。
- 拉动 Qualcomm AI Hub、Edge Impulse、Foundries.io、Ubuntu/Yocto、QDC 的使用量。
- 带动 companion chips、Wi-Fi/BT、5G/RedCap、PMIC、模组伙伴和 ODM 生态。
- 降低客户在 bring-up、camera、thermal、OTA、certification 上卡死的概率。

## 9. Competition Demo

比赛演示：从一个会动的原型，生成一份可交给 ODM 的生产包。

演示脚本：

1. 上传原型配置：选择 Dragonwing target、相机/LiDAR/IMU/CAN/EtherCAT、电池、通信、ROS 2、AI Hub 模型和目标市场。
2. 生成 SKU 风险图谱：热、电源、实时、接口、OTA、BOM、认证、DFM/DFA、FRU 和供应链风险。
3. 打开 EVT/DVT/PVT 门禁：验证矩阵、环境/寿命、EMC pre-scan、认证样机、PVT 良率和 MP 准入。
4. 展示 CM readiness：EBOM/MBOM/Service BOM、AVL、EOL 测试、治具需求、SOP、Golden Image 和追溯 schema。
5. 导出 Production Pack：CM handoff、certification readiness、lifecycle ledger、FRU/spares 和 UptimeOS/RiskLedger 接入。
6. 现场闭环：模拟一条 RMA 或 RiskLedger incident，自动触发 CAPA、ECO 和下一版 DVT gate。

一句话：

> Qualcomm provides the reference design; ScaleFoundry turns it into your robot product.

## Claims To Avoid

- 不声称 Qualcomm 官方合作伙伴/认证方案，除非已签约。
- 不说几周量产所有机器人。
- 不说替代客户硬件团队、CM、PLM 或 MES。
- 不包装成通用具身智能算法公司。
- 不直接说比 NVIDIA 更强或更便宜；说面向 Dragonwing 的产品化路径。
- 不承诺安全认证、量产良率、固定降本比例或固定上市时间。
- 不宣传“通过军标”或“通过认证”，除非说明测试方法、严酷度、范围和报告。

## Sources

- IFR industrial robots 2025：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR service robots 2025：https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom
- Qualcomm Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm IQ-9075：https://www.qualcomm.com/internet-of-things/products/iq9-series/iq-9075
- Qualcomm Product Longevity Program：https://www.qualcomm.com/internet-of-things/products/product-longevity-program
- FoundriesFactory：https://www.qualcomm.com/developer/software/foundriesfactory
- Ubuntu on Qualcomm IoT Platforms：https://www.qualcomm.com/developer/software/ubuntu-on-qualcomm-iot-platforms
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Edge Impulse Qualcomm：https://www.edgeimpulse.com/qualcomm
- Formlabs EVT/DVT/PVT：https://formlabs.com/uk/blog/validation-testing-product-development-poc-evt-dvt-pvt-mp/
- AIAG PPAP：https://www.aiag.org/training-and-resources/manuals/details/PPAP-4
- ISO robotics standards：https://www.iso.org/sectors/engineering/robotics
- 47 CFR Part 15：https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15
- OSHA NRTL：https://www.osha.gov/nationally-recognized-testing-laboratory-program
- GS1 Traceability Standard：https://www.gs1.org/standards/gs1-global-traceability-standard/current-standard
- Memfault：https://memfault.com/
- Mender：https://mender.io/
- Duro PLM：https://durolabs.co/
- Tulip：https://tulip.co/
- Plexus NPI：https://www.plexus.com/solutions/new-product-introduction/
- Benchmark robotics and mechatronics：https://www.bench.com/mechatronics-and-robotics
- Fictiv：https://www.fictiv.com/
