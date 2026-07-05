# CareOps Pitch

更新时间：2026-07-05。

## Core Thesis

CareOps 是面向医院与实验室的非临床机器人工作流平台：

> 用 Qualcomm 边缘机器人连接样本、药房、耗材、电梯门禁、LIMS/HIS 与审计系统，让院内取送交接变成隐私优先、可追溯、可持续学习的运营流程。

它不做诊断、不替代医嘱、不执行给药、不声称医疗器械批准。第一阶段只做高频、可验证、可采购的运营任务：

- 样本取送与分拣。
- 药房和耗材配送。
- PPE、设备、床旁物资补给。
- 夜间低人力覆盖。
- 清洁/消毒流程辅助和 proof-of-work。
- 老年照护场景中的物品递送和提醒类支持。

## Why This Matters

医院的机器人价值不在于炫技，而在于把重复搬运交给机器人，把医护时间还给患者。

关键痛点：

- 医护人员被非临床取送任务打断。
- 样本、药品和耗材在院内流转时需要条码、权限、温控、交接和审计。
- 电梯、门禁、禁行区、夜间路线和拥挤走廊让部署复杂。
- 医疗数据属于敏感数据，云端训练不能默认收集 PHI 或原始视频。
- 采购部门需要 HIPAA/PIPL/GDPR-oriented controls、网络安全、消毒 SOP、风险评估和运维 SLA。

CareOps 的策略是先做院内运营，不碰诊疗承诺。

## Product Modules

### 1. EdgeRobot Core

基于 Qualcomm edge 的院内机器人核心。

- 本地多摄像头感知、避障、路径执行、任务缓存和断网降级。
- 走廊、人群、电梯厅、护士站和实验室入口的现场感知在边缘完成。
- 原始视频和 PHI 不默认进入云端训练。

### 2. FlowOps Scheduler

院内任务调度引擎。

- 对接 LIMS / LIS / HIS / pharmacy / inventory / CMMS / FHIR mock API。
- 支持 STAT priority、夜班队列、定时巡回、ETA、异常处理和人工接管。
- 与 FleetConductor 共享电梯、门禁、楼层和充电资源。

### 3. AccessBridge

电梯、门禁和楼层规则接入层。

- 通过院方授权接口请求电梯、自动门、门禁和禁行区通行。
- 所有通行都进入审计日志，不直接绕过医院设施控制。
- 支持地理围栏、慢行区、人机混行区和维护模式。

### 4. SpecimenChain

样本链路模块。

- 条码/RFID、锁柜、电子签收、温控、时间戳、交接人、取件点和目的地。
- 支持 sealed mock specimen demo，不处理开放样本、锐器、Category A infectious substances 或临床结果。
- 目标是 traceability 和 chain-of-custody，不声称保证检测结果或样本完整性。

### 5. MedSupply Secure Relay

药房、耗材和小设备安全配送。

- 锁柜、多站点配送、工牌/PIN/RFID 授权开柜和电子签收。
- 支持耗材、PPE、小设备、一般药房配送流程。
- 不做给药动作，不替代药师、护士或医嘱系统。

### 6. PrivacyAudit DataFlywheel

隐私优先的数据飞轮。

- 本地脱敏、人脸/屏幕模糊、最小化采集、可配置保留和删除。
- 结构化审计事件：谁下单、谁取件、谁交接、何时到达、是否超温、是否异常。
- 非临床任务的示教、路线、排队、交接和异常片段进入 LeRobot-compatible dataset。

## Competition Demo

最稳妥 demo：

1. 使用 sealed mock specimen tubes 和二维码/条码标签。
2. 护士或操作员扫码，把样本放入锁柜。
3. CareOps 生成 LIMS/FHIR-style 任务、温控记录和 chain-of-custody 时间线。
4. 机器人从病区模拟点移动到检验科模拟点。
5. 到达后扫码交接，系统回写状态。
6. 一次条码错误或路径阻塞进入异常流程。
7. 采集的非临床取送 episode 进入 LeRobot/DataFlywheel，用于训练更稳定的交接动作和任务路线。

这能展示商业闭环，同时避开医疗器械、诊断和真实样本处理风险。

## Why Qualcomm Should Care

CareOps 让 Qualcomm 进入高价值、强合规、需要边缘智能的医疗运营场景：

- 医院需要本地推理和隐私边界，不能把原始视频和 PHI 默认送到云端。
- 多摄像头、连接、低功耗和本地 AI 是院内移动机器人刚需。
- RB / QCS / IQ / Dragonwing 可以成为医院机器人 OEM 的标准边缘底座。
- AI Hub 和 LeRobot 工作流可以把非临床支持任务持续优化，而不触碰诊疗承诺。
- 中国版强调智慧医院、数据不出院、院内物流、养老服务和 “机器人+” 应用；海外版强调 HIPAA/GDPR-oriented controls、护理人力短缺、RaaS 试点和采购证据包。

## Claims To Avoid

- 不声称 FDA/NMPA/CE medical-device approval。
- 不声称诊断、治疗、分诊、患者监护、跌倒检测或临床决策支持。
- 不声称替代护士、药师或检验人员。
- 不声称 HIPAA compliant robot；只说支持 HIPAA-oriented safeguards 或 BAA-ready deployment。
- 不声称 sterile、prevents infection、reduces HAIs，除非有临床验证。
- 不声称训练数据已经 de-identified，除非完成 HIPAA Safe Harbor 或 Expert Determination。

## Sources

- AHA workforce shortage market scan：https://www.aha.org/aha-center-health-innovation-market-scan/2024-09-10-5-health-care-workforce-shortage-takeaways-2028
- HRSA workforce projections：https://bhw.hrsa.gov/data-research/projecting-health-workforce-supply-demand
- Aethon hospital robots：https://aethon.com/hospital-robots-healthcare/
- Relay hospital delivery robots：https://relayrobotics.com/relay-delivery-robots-for-hospitals
- Diligent Robotics Moxi：https://www.diligentrobots.com/moxi
- Swisslog lab specimen transport：https://www.swisslog-healthcare.com/en-us/medication-management/transport/lab-specimen-transport
- HIPAA Security Rule：https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html
- FDA administrative-support software guidance：https://www.fda.gov/medical-devices/digital-health-center-excellence/step-2-software-function-intended-administrative-support-health-care-facility
- CLIA specimen integrity：https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-493/subpart-K
- OSHA bloodborne pathogens：https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030
- FHIR Specimen：https://build.fhir.org/specimen.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
