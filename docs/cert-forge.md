# CertForge Pitch

更新时间：2026-07-05。法规、标准、认证路径和实验室要求会随产品类别、目标市场和版本变化；真实交付前必须由合规负责人、实验室、认证机构和法律顾问按具体 SKU 复核。

## Core Thesis

CertForge 是面向 Qualcomm 机器人产品的合规证据工厂：

> 从原型到量产，把每一次模型、固件、ROS 节点、传感器标定、基准测试、SBOM、风险决策和供应商声明，自动锻造成可审计的认证准备证据包。

它不是认证机构，也不承诺机器人“自动通过 CE / FCC / UL / CCC”。它解决的是商业化过程中更常见、更昂贵的问题：

- 初创团队不知道哪些标准、法规和测试路径真正适用。
- 认证准备经常发生在量产前夜，导致硬件返工、说明书返工、标签返工、软件更新流程返工。
- 模型、固件、BOM、无线模组、电池、传感器和安全策略变更后，没有统一的合规影响分析。
- 企业客户、集成商、实验室、投资人和 Qualcomm 生态伙伴需要看到结构化证据，而不是零散文件夹。

一句话：CertForge 不替你“发证”，而是让机器人产品从第一天就按可审计证据来研发。

## Five-Thread Research Synthesis

### 1. Product Compliance Roadmap

最稳妥的产品定位是 scope-first roadmap：

- 产品分类：工业机器人、协作机器人、AMR/AGV、服务机器人、家庭/消费机器人、医疗/实验室辅助设备、户外/农业机器人。
- 市场路径：EU CE / Machinery、EMC、RED、Battery、RoHS；US FCC、NRTL/UL、CPSC/FDA where applicable；China CCC catalogue、SRRC、GB / GB/T 标准。
- 技术文件：风险评估、EHSR checklist、DoC、标签、说明书、测试报告、BOM、无线模块资料、电池运输文件。
- 变更控制：BOM、无线、外壳、电源、散热、固件、模型、OTA、传感器和安全参数变化后自动触发 impact review。

### 2. Functional Safety Evidence

机器人安全不是一个证书，而是一套持续维护的 safety case：

- ISO 12100 风险评估。
- ISO 13849 / IEC 62061 安全相关控制系统证据。
- ISO 10218-1/-2:2025 工业机器人与集成单元证据。
- ISO 3691-4:2023 AMR / AGV 相关证据。
- ANSI/A3 R15.08 工业移动机器人和系统集成证据。
- ISO 13482 个人护理/服务机器人路径。

CertForge 不复印标准正文，只维护 applicability matrix、hazard-to-evidence graph、测试任务、责任人、版本和证据索引。

### 3. Cybersecurity And Software Compliance

联网机器人是软件产品、OT 资产和边缘 AI 设备：

- SBOM / VEX：版本级组件清单、漏洞状态和影响说明。
- NIST SSDF：安全开发、release gate、构建完整性、漏洞修复流程。
- CVD / PSIRT：漏洞披露、响应 SLA、security.txt、客户公告。
- OTA evidence：签名发布、灰度、回滚、支持期、EOL 和补丁历史。
- EU CRA readiness：2024-12-10 生效；2026-09-11 起漏洞和事件报告义务开始适用；2027-12-11 主要义务开始适用。

稳妥表述是“designed to support EU CRA readiness”和“aligned to NIST SSDF evidence needs”，而不是声称自动合规或认证。

### 4. China / Overseas Lanes

中国版重点是“适用范围先判定”：

- CCC 只覆盖官方目录内的产品和部件，机器人整机常常通过电源适配器、电池、家电/儿童产品、车辆、无线模块、爆炸性环境设备等触发。
- SRRC / CMIIT 用于无线电发射设备型号核准。
- GB / GB/T evidence map：工业机器人安全、协作机器人、服务机器人、机械电气安全、EMC、安全相关控制系统。
- 中文说明书、标签、产品铭牌、供应商声明和实验室资料需要单独管理。

海外版重点是 EU / US launch dossier：

- EU：Machinery Directive / Machinery Regulation transition、EMC、RED、RoHS、Battery、GPSR、CRA、AI Act where applicable。
- US：FCC equipment authorization、NRTL planning、UL robotics safety path、OSHA workplace expectations、CPSC/FDA where applicable。

### 5. Product Design

最有商业张力的产品不是“合规咨询平台”，而是“Qualcomm-powered robots 的 compliance evidence factory”：

- ScaleFoundry 输出硬件 SKU、BOM、EVT/DVT/PVT 记录。
- EdgeRuntimeBench 输出 Qualcomm edge profile、模型哈希、延迟、温度、功耗和回滚证据。
- SafetyOps 输出 release gate、权限、运行策略和异常日志。
- RiskLedger 输出现场事故、near-miss、维护和证据保管链。
- CertForge 把这些证据映射到市场准入、认证准备、采购问卷和审计包。

## Product Modules

### 1. Standards Graph

- 产品分类问卷。
- 地区和行业选择。
- 适用法规 / 标准 / 测试路径候选。
- 不适用理由和 reviewer sign-off。
- 标准变更 watchlist。

### 2. Evidence Vault

- Release manifest。
- BOM / AVL / PCN / PDN。
- Firmware / OS / ROS package / model hashes。
- SBOM / VEX / vulnerability status。
- Benchmarks and validation reports。
- Labels, manuals, warnings, DoC drafts。
- Supplier declarations and wireless module certificates。

### 3. Safety Case Studio

- Hazard analysis。
- Risk reduction measures。
- Safety functions and performance targets。
- Test cases and validation evidence。
- Residual risk acceptance。
- Link to SafetyOps runtime gates and RiskLedger incidents。

### 4. Launch Dossier Exporter

按市场和产品类型输出可交给内部合规负责人、实验室、客户安全团队或投资人的 evidence index：

- EU technical file index。
- US FCC / NRTL readiness package。
- China CCC / SRRC / GB applicability package。
- Cyber procurement pack。
- Battery and logistics package。
- Change-impact report。

### 5. Compliance Gate In CI

每次 release 都运行合规 gate：

- BOM changed?
- radio module changed?
- battery / charger changed?
- enclosure / thermal changed?
- safety parameter changed?
- AI model changed?
- OTA / vulnerability status changed?
- manuals and labels still match?

低风险变更只更新证据索引；高风险变更进入 reviewer queue 或实验室任务。

## Competition Demo

比赛可以展示一个“机器人从 release 到 launch dossier”的浏览器流程：

1. 选择产品模板：室内 AMR、桌面机械臂、家庭服务机器人、户外巡检车。
2. 导入 ScaleFoundry release manifest：BOM、无线模组、电池、外壳、传感器、QCS / IQ 平台。
3. 导入 EdgeRuntimeBench：AI Hub profile、QNN artifact、模型哈希、延迟、功耗、温度。
4. 导入 SafetyOps：技能权限、速度区、急停、保护停、release gate。
5. Standards Graph 自动生成 EU / US / China 适用路径和不适用理由。
6. Gap view 显示缺失证据：说明书、标签、SBOM/VEX、UN 38.3、电源适配器、FCC modular grant、risk assessment review。
7. 上传一份测试报告或 ROS bag 后，gap 关闭并写入 evidence vault。
8. 一键导出 EU technical-file index、US readiness pack、China scope package 和 customer procurement pack。

## Qualcomm Value

CertForge 对 Qualcomm 的战略价值在于把“芯片能力”变成“商业准入能力”：

- Secure boot / hardware root of trust：作为证据链起点。
- AI Hub / QNN：模型 profile、compiled artifact、target device 和 benchmark 进入可复核 release record。
- Dragonwing / QCS / IQ platforms：传感、连接、多媒体和边缘 AI 证据按平台复用。
- Product longevity：长期供货、BOM 生命周期和安全更新支持期成为客户采购证据。
- Partner ecosystem：开发板、模组、ODM、实验室、集成商和云训练伙伴围绕同一证据格式协作。

一句话：

> Qualcomm 不只是让机器人跑得动；CertForge 让 Qualcomm 机器人更容易进入采购、实验室、量产和全球市场。

## Claims To Avoid

- 不说 CertForge certifies robots。
- 不说 pre-certified radio module makes the whole robot compliant。
- 不说 CE certified；更稳妥是 CE marked after manufacturer conformity assessment。
- 不说 guaranteed FCC / UL / CCC approval。
- 不说 legal advice。
- 不说 NIST certified、CRA compliant、hack-proof、safe by default。
- 不把 AI 生成的判断当作最终结论；AI 只能生成 draft / checklist / gap suggestion，签核要由人完成。

## Sources

- EU Machinery Regulation overview：https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/machinery_en
- EU Cyber Resilience Act：https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EU Radio Equipment Directive：https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red_en
- EU Battery Regulation：https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L:2023:191:FULL
- FCC equipment authorization：https://www.fcc.gov/general/equipment-authorization
- OSHA NRTL program：https://www.osha.gov/nationally-recognized-testing-laboratory-program
- UL robotics safety：https://www.ul.com/services/robotic-safety-security-and-performance
- ISO 12100：https://www.iso.org/standard/51528.html
- ISO 13849-1：https://www.iso.org/standard/73481.html
- ISO 10218-1:2025：https://www.iso.org/standard/73933.html
- ISO 10218-2:2025：https://www.iso.org/standard/73934.html
- ISO 3691-4:2023：https://www.iso.org/standard/82739.html
- ANSI/A3 R15.08：https://www.automate.org/robotics/safety/robot-safety-standard-documents
- NIST SSDF SP 800-218：https://csrc.nist.gov/pubs/sp/800/218/final
- CISA SBOM：https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom
- OASIS CSAF / VEX：https://oasis-open.github.io/csaf-documentation/
- ISO/IEC 29147 vulnerability disclosure：https://www.iso.org/standard/72311.html
- CNCA official site：https://www.cnca.gov.cn/
- MIIT official site：https://www.miit.gov.cn/
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Qualcomm IoT security：https://www.qualcomm.com/products/features/iot-security
- Qualcomm product longevity：https://www.qualcomm.com/internet-of-things/products/product-longevity-program
