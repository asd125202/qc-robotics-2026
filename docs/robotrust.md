# RoboTrust Pitch

更新时间：2026-07-05。

## Core Thesis

机器人商业化的关键问题不只是“能不能训练”，而是企业是否敢让机器人采集真实世界数据、是否敢把数据送到云端训练、是否能解释数据权属和模型使用边界。

RoboTrust 是一层具身数据可信云：

1. Qualcomm edge robot 在本体侧先完成采集、脱敏、签名、加密和缓存。
2. 数据进入 LeRobot-compatible Trust Vault，同时附带数据护照。
3. Policy Gateway 根据客户、地区、敏感等级和合同，把训练任务路由到中国云、海外云、客户 VPC 或私有云。
4. 训练过程留下 dataset card、model card、job receipt、SBOM/VEX、访问日志和部署审批证据。
5. 合格策略回到 Qualcomm edge runtime，现场失败继续回流，但原始敏感轨迹不默认跨境、不默认进入共享大模型训练。

一句话：数据不出域，模型可进化；共享智能，不共享原始数据。

## Why This Matters Now

### China

- 机器人相机、语音、位置、轨迹和工厂运行数据不能简单当成“机器数据”。在可识别个人、工业生产和重要数据场景下，PIPL、DSL、CSL、网络数据安全管理条例和工业数据分类规则都会影响采集、存储、出境和训练。
- 2024 年数据出境规则降低了部分门槛，但没有消除跨境评估、标准合同、认证和重要数据边界。
- 中国版机器人训练平台需要区域数据面、国产云/私有云/BYOC 选项、导出审批、敏感数据计数和可审计证据。

### EU / Overseas

- EU Data Act 已进入执行期，连接产品的用户数据访问、导出和第三方共享将影响机器人 telemetry 与训练数据平台。
- GDPR 仍然约束视频、音频、位置、badge ID、脸部、步态、工作场景日志等数据。
- AI Act、Cyber Resilience Act 和 Machinery Regulation 会推动模型追溯、日志、安全更新、漏洞报告、远程监督和安全状态证明。
- 海外企业买家会要求 SOC 2、ISO 27001、NIST CSF/SSDF、SBOM、VEX、SLSA、日志留存、SSO、RBAC、SIEM export 和供应商安全问卷。

### Robotics Market

- LeRobot、DROID、Open X-Embodiment、Physical Intelligence、Skild AI、Figure、Covariant 和 NVIDIA Isaac GR00T 都说明机器人智能正在转向数据规模、跨形态数据、仿真/合成数据和 fleet learning。
- 但开源机器人数据集的商业许可不一致。比如 Apache-2.0、CC BY、CC BY-NC-SA、研究用途数据和客户私有数据不能混用。
- 因此平台必须把每段 episode 的来源、授权、用途、区域、到期、删除和派生模型权利记录下来。

## Product Modules

### 1. Edge Trust Agent

部署在 Qualcomm 本体侧的采集代理。

- 多相机、关节状态、动作、语音指令和任务结果采集。
- 本体侧 face / license plate / screen / badge / location redaction。
- episode timestamp、device identity、hash、signature、encryption。
- 断网缓存、带宽感知上传和失败片段优先级。

### 2. LeRobot Trust Vault

LeRobot-compatible 数据工厂和可信存储层。

- Parquet / video shard / metadata / data card。
- episode 质检、切分、合并、导出和版本管理。
- 数据分类：PI、sensitive PI、industrial data、important-data candidate、open dataset、synthetic。
- 数据保留、删除、冻结和 legal hold。

### 3. Dataset Passport

把数据从文件变成可签约资产。

- owner、site、operator、collector、robot SKU、task、sensor、license、region。
- 允许用途：private model only、shared improvement、synthetic derivative、benchmark only、marketplace revenue share。
- 禁用场景、到期删除、撤回、收益分配和审计哈希。
- 对 NC/SA/未知许可数据自动拦截商业训练任务。

### 4. Dual-Region Training Mesh

按地区和合同路由训练任务。

- China lane：Alibaba Cloud PAI、Tencent Cloud、Huawei Cloud、AutoDL、客户私有云。
- Overseas lane：Lambda、RunPod、CoreWeave、AWS、NVIDIA DGX Cloud、客户 VPC。
- 原始敏感数据默认留在本域；跨域只流动授权模型、指标、脱敏样本、adapter 或合成数据。
- 成本、GPU SKU、训练日志、checkpoint、eval result 和部署包统一记录。

### 5. Evidence Room

企业采购、法务、安全和审计可查看的证据室。

- model card、dataset card、training job receipt、lineage graph、export approval。
- SOC 2 / ISO 27001 roadmap、DPA、subprocessor、incident response、VDP、RTO/RPO。
- SBOM、VEX、signed artifact、SLSA provenance、secure OTA evidence。
- NIST CSF / SSDF / 800-53 / CAIQ / vendor security questionnaire mapping。

### 6. Qualcomm Deployment Gate

训练结果不是直接上机器人，而是经过部署门禁。

- 检查 edge target、模型输入输出契约、数据授权、区域限制、回滚包和运行指标。
- 只把合格 policy export 到 Qualcomm edge runtime。
- 机器人端保留 command audit、model version、fallback state 和 rollback route。

## Website Storyline

1. **Hero**：RoboTrust 具身数信云。让机器人训练数据敢采、敢训、敢采购。
2. **Trust Chain**：从 Qualcomm edge 到 LeRobot Trust Vault，再到中国/海外训练云和部署门禁。
3. **Regional Data Planes**：中国数据在中国云训练，海外数据在海外云训练，原始敏感轨迹不默认跨境。
4. **Dataset Passport**：每一段示教都有权属、同意、许可范围、地域限制和派生模型边界。
5. **Enterprise Approval**：把安全问卷、数据出境、SBOM/VEX、日志、DPA、供应商证据做成采购包。
6. **Qualcomm Value**：Qualcomm 不只是推理芯片，而是可信采集端、边缘隐私边界、部署门禁和长期运营入口。

## Commercial Value

RoboTrust 可以单独销售，也可以作为 DataFlywheel、DualCloudOps、EdgeFleet、SafetyOps 和 PilotContractKit 的企业版升级包。

- 对企业客户：降低数据、法务、安全和 IT 审批成本。
- 对系统集成商：提供可复用的试点证据包和数据合同模板。
- 对机器人公司：让训练数据资产可授权、可复用、可融资。
- 对 Qualcomm：让机器人数据采集、训练、部署和安全治理都围绕 Qualcomm edge target 建立默认工作流。

## Claims To Avoid

- 不声称 fully compliant、免审、无需备案、China-approved、CE-ready 或 SOC 2 compliant。
- 不声称机器人视频自动匿名、自动非个人信息或无再识别风险。
- 不默认把客户数据用于共享大模型训练。
- 不承诺完全删除已经进入派生模型的影响，只承诺可审计的停止使用、删除、冻结和后续训练排除流程。
- 不把“数据在本地存储”等同于 GDPR、PIPL、Data Act 或 CRA 合规。

## Sources

- CAC 网络数据安全管理条例：https://www.cac.gov.cn/2024-09/30/c_1729384452307680.htm
- PIPL：https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm
- 促进和规范数据跨境流动规定：https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm
- EU Data Act：https://digital-strategy.ec.europa.eu/en/policies/data-act
- EU AI Act：https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU Cyber Resilience Act：https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- EU Machinery Regulation：https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Open X-Embodiment：https://robotics-transformer-x.github.io/
- NVIDIA Isaac GR00T：https://developer.nvidia.com/isaac/gr00t
- NIST Cybersecurity Framework 2.0：https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- NIST SSDF SP 800-218：https://csrc.nist.gov/pubs/sp/800/218/final
- CISA SBOM：https://www.cisa.gov/sbom
- CISA VEX minimum requirements：https://www.cisa.gov/resources-tools/resources/minimum-requirements-vulnerability-exploitability-exchange-vex
- Qualcomm AI Hub：https://aihub.qualcomm.com/
