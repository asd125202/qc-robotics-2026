# CertForge Pitch

更新时间：2026-07-06。CertForge 不是认证机构、测试实验室或法律顾问；它不承诺自动获得 CE / FCC / UL / CCC / SRRC / NRTL / AI Act / CRA 结论。真实项目必须由合规负责人、实验室、认证机构和律师按具体 SKU、目标市场、用途和版本复核。

## One-Liner

CertForge 是 Dragonwing 机器人合规 CI/CD：

> 不是写合规，是铸证据。它把每一次代码、模型、SBOM、ROS/MCAP、HIL/真机测试、QNN profile、风险评估和供应商证明，自动编成可审计技术文件证据链。

## 1. Problem

机器人公司不是被“要不要合规”卡住，而是被“证据在哪里、版本为什么可信、变更影响是什么”卡住。

- 机器人不是 App。模型、固件、无线、电池、传感器、外壳、速度限制、说明书和供应商变化后，原有安全、网络、无线、电气和市场准入判断都可能失效。
- 证据散落在 Git、Jira、Confluence、实验室 PDF、仿真报告、ROS bag、SBOM 工具、供应商邮件和现场运维系统。
- 实验室、顾问和客户安全团队通常在量产前夜看到一个快照，很难追回每次设计决策、风险接受、测试覆盖和真实运行记录。
- Qualcomm 的安全启动、AI profile、功耗、连接和生命周期优势，如果没有证据格式，很难进入企业采购、融资尽调和上市材料。

## 2. Current Alternatives Fail

- 实验室 / 认证顾问：能解释路径和做测试，但通常太晚介入，无法自动追踪工程变更影响。
- PLM / ALM：能管理需求、物料和流程，却不天然理解 ROS/MCAP、QNN profile、模型回归、现场事件和机器学习版本。
- SBOM / SAST：能覆盖软件供应链，不能覆盖机械危险源、功能安全、无线、电池和运行场景风险。
- 仿真平台：能生成大量数据，但如果没有条款、危险源、控制措施、签核人和 release 关系，数据不会自动变成审计证据。
- 通用合规自动化：Saphira AI、Normal、Ketryx 等证明市场正在形成。CertForge 的差异化必须是机器人 evidence graph + Dragonwing release integration + field evidence。

## 3. Solution

CertForge 连接 Dragonwing 研发栈、Git/CI、SBOM、AI Hub / QNN、ROS2/MCAP、ScaleFoundry、UptimeOS、RiskLedger、SafetyOps、仿真、HIL、真机测试和供应商文档，维护一张可审计图谱：

```text
regulatory clause -> hazard -> safety/control measure -> test -> artifact -> signer -> release
```

核心流程：

1. Classify：选择机器人类型、用途、目标市场、无线、电池、电源、环境、用户和应用边界。
2. Map：生成适用法规、标准、测试路径、不适用理由和 reviewer sign-off。
3. Collect：从 release、BOM、SBOM、QNN profile、ROS/MCAP、HIL、仿真和真机测试收集证据。
4. Gate：每次模型、固件、供应商、无线、电池、外壳、风险策略和说明书变化触发 impact review。
5. Export：输出 EU、US、中国、客户采购、保险尽调和实验室沟通所需的 evidence dossier。

## 4. Why Now

2026-2028 是 Physical AI 从 demo 走向监管证据的窗口期。

- EU RED 网络安全要求已从 2025-08-01 开始适用于相关无线设备。
- EU CRA 漏洞和严重事件报告义务从 2026-09-11 开始，主要义务从 2027-12-11 开始。
- EU Machinery Regulation 从 2027-01-20 开始适用。
- AI Act 让高风险 AI 的文档、日志、治理和质量管理要求逐步进入实体产品，但不能声称所有机器人都是同一类高风险 AI。
- ISO 10218-1/-2:2025 更新，AMR、协作机器人和移动机器人安全证据继续细化。
- Qualcomm Dragonwing 和 AI Hub / QNN 把边缘 AI 推向量产机器人，正需要一个把芯片能力转成商业准入能力的证据层。

## 5. Product

### Evidence Graph

版本化追踪每个 release 的风险、控制措施、测试、签核、缺口和导出材料。

### Robot Run Recorder

把 ROS2/MCAP、仿真、HIL、真机测试和现场事件转换成场景覆盖、安全证据和回归结果。

### Cyber + AI Pack

SBOM、VEX、漏洞报告、模型卡、数据 lineage、QNN profile、量化误差、性能边界、鲁棒性和人工监督证据。

### Technical File Export

Machinery、CRA、AI Act、RED、FCC、NRTL planning、ISO 10218、ISO 3691-4、ANSI/RIA R15.08、中国 CCC 目录判定、SRRC、客户审计包和 gap tickets。

### Evidence Schema

```json
{
  "evidence_id": "ev_qnn_profile_2026_07_06",
  "kind": "model_qnn_evidence",
  "product": "dragonwing-amr-iq10",
  "subject": "pick_place_policy_v17",
  "standard_refs": ["ISO 10218-1:2025", "EU CRA"],
  "requirement_refs": ["safe_stop_fallback", "software_supply_chain"],
  "producer": "aihub-qnn-pipeline",
  "hashes": ["sha256:..."],
  "attachments": ["qnn_profile.json", "regression_report.html"],
  "signature": "sigstore-bundle",
  "status": "review_required"
}
```

## 6. Business Model

首批买家：准备量产、准备企业采购或准备融资尽调的机器人 OEM / startup。

第二批买家：RaaS operator、系统集成商、实验室、园区、保险/融资数据用户和 Qualcomm 生态伙伴。

海外定价：

- Readiness Sprint：$8k-$25k，4-6 周梳理路径和 gap。
- Certification Run：$30k-$100k NRE / robot / market。
- Continuous Assurance：$24k-$120k / year by product line / market / evidence count。
- Fleet add-on：$500-$2k / site / month 或 $25-$150 / robot / month。
- Lab/channel white-label：$75k-$250k / year + usage。

中国定价：

- 预合规包：人民币 2万-5万。
- 认证资料 / 送检项目包：人民币 8万-25万。
- 年订阅：人民币 3万-20万 / 产品线。
- 实验室、园区、集成商白标：人民币 20万-80万 / 年。

核心 ROI：缩短上市准备周期、减少测试失败和返工、提高企业采购与保险审查通过概率、把 Qualcomm 评估板转化为可销售机器人 SKU。

## 7. Competition & Moat

相邻竞争者：

- Saphira AI：机器人 / 硬件安全认证自动化，最接近。
- Normal：YC S25，硬件认证自动化。
- Ketryx：受监管软件 traceability 和文档自动化。
- Vanta / Drata / Secureframe / Hyperproof：企业 GRC。
- Assent / Sphera / Compliance & Risks / Enhesa：产品合规和材料合规。
- CycloneDX / SPDX / Dependency-Track / Anchore / Black Duck：SBOM / VEX / software supply chain。
- UL / TUV / Intertek / SGS / CSA：实验室和认证服务，不是被替代对象。

CertForge 壁垒：

- Robot-specific evidence graph：危险源、控制措施、测试、现场事件、模型版本和 release 连接在一起。
- Dragonwing-native release integration：AI Hub / QNN、secure boot、edge benchmark、OTA、device identity 内建。
- Field evidence loop：UptimeOS、RiskLedger、SafetyOps、ScaleFoundry 的运行、事故、维修和变更记录持续回写。
- Channel format：实验室、ODM、集成商和生态伙伴可以复用同一预审包。

## 8. Why Qualcomm

Qualcomm 的价值不止是算力，而是机器人商业化底座。

- Secure boot / hardware root of trust：证据链可信起点。
- AI Hub / QNN：模型 profile、compiled artifact、target device、latency、memory、temperature 和 regression record。
- Dragonwing platforms：连接、视觉、多媒体、边缘 AI、功耗和生命周期数据进入 launch dossier。
- Product longevity：长期供货、BOM 生命周期和安全更新支持期成为客户采购证据。
- Partner ecosystem：开发板、模组、ODM、实验室、集成商和云训练伙伴围绕同一证据格式协作。

一句话：

> Qualcomm 不只是让机器人跑得动；CertForge 让 Qualcomm 机器人更容易进入采购、实验室、量产和全球市场。

## 9. Demo & Ask

比赛演示：一个 Dragonwing AMR 从 release 到三地上市证据包。

1. 选择 `dragonwing-amr-iq10`，导入 ScaleFoundry digital twin、UptimeOS fleet asset、SBOM 和 QNN profile。
2. 选择 EU + US + China、warehouse AMR、collaborative manipulator、edge AI，生成 standards list 和 requirements matrix。
3. 导入 ROS2/MCAP、HIL 报告、QNN profile、SBOM/VEX，dashboard 显示覆盖、缺口和责任人。
4. 展示 model/QNN evidence：模型 hash、量化误差、latency、device profile、ODD limits、fallback。
5. 展示 safety case graph：top claim、风险控制措施、测试和残余风险签核。
6. 注入变更：新模型版本或 OpenSSL CVE，CertForge 输出 impacted requirements、rerun tests、VEX status 和 dossier delta。
7. 导出 `EU_Machinery_Technical_File.zip`、`CRA_Cybersecurity_File.zip`、`Safety_Case.html`、`machine_readable_dossier.jsonld`。

申请方向：用 Qualcomm Dragonwing 作为机器人商业化底座，把合规证据、云训练、边缘部署和现场运行连接成一个可交付产品，而不是比赛结束就消失的 demo。

## Claims To Avoid

- 不说 CertForge certifies robots。
- 不说 pre-certified module makes whole robot compliant。
- 不说 guaranteed CE / FCC / UL / CCC / SRRC approval。
- 不说 legal advice。
- 不说 NIST certified、CRA compliant、hack-proof、safe by default。
- 不说所有机器人都属于 AI Act high-risk。
- 不把 AI 生成的判断当作最终结论；AI 只能生成 draft / checklist / gap suggestion，签核要由人完成。
- 不复制 ISO 标准正文，只维护客户授权范围内的 mapping、evidence index 和 gap。

## Sources

- Qualcomm Dragonwing IQ10 Robotics Reference Design：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub docs：https://workbench.aihub.qualcomm.com/docs/
- EU Machinery Regulation：https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng
- EU Cyber Resilience Act：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- EU CRA manufacturers：https://digital-strategy.ec.europa.eu/en/policies/cra-manufacturers
- EU AI Act：https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- EU Radio Equipment Directive：https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red_en
- FCC Part 15：https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15
- OSHA NRTL program：https://www.osha.gov/nationally-recognized-testing-laboratory-program
- UL consumer and commercial robots：https://www.ul.com/services/consumer-and-commercial-robots
- ISO 10218-1:2025：https://www.iso.org/standard/73933.html
- ISO 10218-2:2025：https://www.iso.org/standard/73934.html
- ISO 3691-4：https://www.iso.org/standard/70660.html
- ANSI / A3 robot safety standards：https://www.automate.org/robotics/safety/robot-safety-standard-documents
- NIST SSDF SP 800-218：https://csrc.nist.gov/pubs/sp/800/218/final
- CISA SBOM：https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom
- CycloneDX VEX：https://cyclonedx.org/capabilities/vex/
- SPDX specifications：https://spdx.dev/use/specifications/
- MCAP：https://mcap.dev/
- Saphira AI：https://www.saphira.ai/
- Normal / YC：https://www.ycombinator.com/companies/normal
- Ketryx：https://www.ketryx.com/
