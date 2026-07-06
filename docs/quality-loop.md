# QualityLoop 质检闭环 Pitch

更新时间：2026-07-06。

## One-Line

QualityLoop 是检测之后的质量操作系统：

> AI 视觉发现缺陷，QualityLoop 关闭缺陷，并把每次关闭结果变成下一轮 edge 模型和质量流程的资产。

目标客户不是“想试 AI 的工厂”，而是每周质量会上都在追同一种 NG 的质量总监、制造工程负责人、厂长和数字化工厂负责人。

## Problem

工厂已经有 AOI、相机、MES、QMS、SPC 和人工复判，但质量异常仍然无法闭环。

- 缺陷图像没有稳定关联工单、批次、设备、工艺参数、供应商、模型版本和处置结果。
- 工程师在群聊、截图、Excel 和会议之间追根因，RCA 周期长。
- CAPA 派发后没有复检和效果证据，不知道同类缺陷是否真的下降。
- 供应商质量反馈常靠人工整理证据，扯皮成本高。
- 模型阈值、缺陷 taxonomy、station recipe、训练集、灰度和回滚没有进入审计体系。

一句话：检测系统越多，异常越多；如果没有闭环，工厂得到的是更多报警，而不是更少缺陷。

## Why Now

质量正在从质检工位问题，升级为董事会、监管、出海审厂和智能制造预算问题。

中国版时机：

- 《质量强国建设纲要》把 2025 年制造业质量竞争力指数目标定为 86，制造业产品质量合格率目标定为 94%，并推动质量策划、控制、保证、改进全流程数字化、网络化、智能化。
- 工业设备更新政策要求到 2027 年，工业领域设备投资规模较 2023 年增长 25% 以上，数字化研发设计工具普及率和关键工序数控化率继续提升。
- AI+制造专项行动提出到 2027 年推动 3-5 个通用大模型在制造业深度应用，建设 100 个工业高质量数据集、推广 500 个典型应用场景、选树 1000 家标杆企业。
- 2025 年中国汽车产销分别达 3453.1 万辆和 3440 万辆，新能源汽车新车销量占比突破 50%。
- 2025 年中国汽车召回涉及 684.6 万辆，其中制造原因占召回车辆 36.5%。
- 新版《医疗器械生产质量管理规范》将于 2026-11-01 施行，质量体系覆盖设计开发、生产、质量控制与放行、销售和售后服务。

海外版时机：

- ASQ 把 cost of quality 拆成 prevention、appraisal、internal failure、external failure；报废、返工、保修、退货、召回都是真实质量成本。
- McKinsey 与 Upstream 的汽车质保 AI 材料把根因分析、早期检测和全车覆盖列为降低 warranty / recall 暴露的核心方向。
- NHTSA 2025 年召回数据说明汽车质量问题仍然会公开化、监管化。
- 全球机器视觉、AOI、MES 和 QMS 软件市场都在增长，但中间缺一个轻量闭环层。
- Qualcomm edge AI 让多相机、本地推理、低延迟、弱网运行和敏感数据不出厂更现实。

## Core Insight

检测框不是产品，闭环才是产品。

真正有防御性的质量数据不是“更多缺陷图片”，而是：

> 缺陷图片 + 工站上下文 + 根因候选 + 纠正动作 + 复检结果 + 是否复发。

谁能拥有这条链，谁就拥有制造质量的学习飞轮。

## Solution

QualityLoop 是 vendor-neutral overlay，不替换 Cognex、Keyence、Hikrobot、OPT、AOI 或现有 QMS/MES，而是在它们之上建立质量闭环：

1. EdgeVision Station 捕获 NG、热力图、缺陷码、置信度、模型版本、latency 和 station recipe。
2. Issue Graph 关联 lot、serial、work order、设备、工艺参数、供应商和历史相似缺陷。
3. RCA/CAPA Copilot 生成 5 Why / 鱼骨图候选，要求工程师确认。
4. CAPA workflow 派发给工程、制程、供应商、返工站或机器人复检站。
5. Re-inspection 验证返工或工艺调整是否有效，跟踪 FPY、PPM、返工率和复发率。
6. 低置信度、人工复判、机器人接管和复检失败进入 active learning / LeRobot HIL 队列。
7. MES/QMS/SPC 回写形成可审计证据包。

## Product Workflow

比赛 demo 的核心流程：

1. MES mock 下发工单和 inspection plan。
2. 操作员扫码零件，加载产品、批次、工位和 station recipe。
3. 相机/机器人拍摄 2-3 个角度，Qualcomm edge 本地识别划伤、漏装或错装。
4. UI 显示 mask、热力图、缺陷码、置信度、模型版本和 latency。
5. QualityLoop 生成 evidence packet，并关联历史相似问题、设备和供应商批次。
6. RCA Copilot 给出候选根因，例如夹具偏移、供应商批次、灯光漂移、刀具磨损。
7. 工程师确认后创建 NCR/CAPA，mock MES 标记 HOLD 或 REINSPECT。
8. 安全低速机械臂或固定相机执行二次复检。
9. 复检结果写回 MES/QMS，低置信度和人工接管进入下一轮训练。

示例 evidence packet：

```json
{
  "packet_id": "QL-2026-07-06-0007",
  "part_id": "P-88421",
  "work_order": "WO-1042",
  "defect": {"type": "scratch", "confidence": 0.94, "bbox": [412, 188, 92, 31]},
  "evidence": {"image_hash": "sha256:...", "mask_uri": "local://...", "model": "ql-v12-qnn"},
  "process": {"station": "line-cam-3", "batch": "B-17", "operator_visible": false},
  "actions": ["hold_part", "robot_reinspect", "open_capa"]
}
```

## Market Wedge

首个切入点不是“所有制造业”，而是已有视觉设备、缺陷证据强、返工昂贵、审计压力大、MES/QMS 基础存在但闭环仍靠人的产线。

中国优先顺序：

1. 新能源汽车 Tier-1/Tier-2：电池包/模组密封、焊接、结构件压铸、热管理、电驱零部件。
2. 3C/电子制造：SMT、AOI、X-ray、外观缺陷、装配一致性。
3. 汽车轴承与精密加工件：微划痕、裂纹、烧伤、尺寸偏差。
4. 医疗器械生产企业：新版 GMP 带来批记录、放行、供应商、CAPA、追溯预算。
5. 智能机器人/高端装备装配：3D 视觉检测装配瑕疵、线束/线路排布、运动部件寿命预测。

海外优先顺序：

1. Electronics NPI / EMS：缺陷漂移快、工程复盘密集、图片证据强。
2. Automotive Tier 1：保修、召回、追溯和供应商质量压力强。
3. Industrial equipment：高价值零部件、低产量、多工艺，返工成本高。
4. Battery pilot lines：新工艺迭代快，最需要 recipe、模型和复检闭环。

## Business Model

QualityLoop 按闭环价值收费，不按模型调用收费。定价锚点是经客户确认的年度质量收益：少返工、少报废、少追责、少质量会议、少审计准备时间。保守规则是收取已验证年度收益的 10-25%，目标是试点后 12 个月内回本。

中国：

- Paid pilot：30k-80k 元，6-8 周，1-2 条线或一个供应商/返工 workflow。
- Starter：60k-120k 元/厂/年，单厂最多 3 条线，异常 workflow、证据包和 dashboard。
- Standard：120k-300k 元/厂/年，3-10 条线，供应商质量、返工闭环、CAPA/RCA、追溯接口。
- Enterprise：300k-800k+ 元/厂/年，多线、多厂、私有部署、HIL/机器人 workflow、高级集成。
- 硬件/集成：20k-100k+ 元/站，取决于相机、光源、边缘计算、PLC/MES/QMS scope。

海外：

- Paid pilot：15k-40k 美元，6-8 周。
- Starter：18k-36k 美元/年。
- Standard：36k-90k 美元/年。
- Enterprise：90k-180k 美元/年；多站点 ACV 可达 250k-750k 美元。
- 硬件/集成：8k-60k+ 美元/视觉站。

## Go-To-Market

第一单不卖“全厂 AI”，卖一个质量总监愿意在周会上展示的结果。

- Buyer：质量总监、制造工程负责人、厂长、数字化工厂负责人、MES/QMS owner。
- Land：一个每周质量会上都会出现的高频缺陷族。
- Pilot：6-8 周，一条线、一个缺陷族、一个 MES/QMS 回写接口。
- KPI：检测到遏制周期下降 25-50%；>95% flagged units 链接图片、批次、序列号、工站、时间、处置；CAPA overdue 下降 25-40%；trace drill 时间下降 50-80%；复发率可追踪。
- Expand：单缺陷族 -> 多缺陷族 -> 多检测站 -> 工厂模板 -> 集团供应商质量网络。
- Channel：机器视觉集成商、MES/QMS 实施商、自动化集成商、Qualcomm 生态硬件伙伴。

## Competition

| 层级 | 代表玩家 | 强项 | QualityLoop 切口 |
|---|---|---|---|
| 视觉/AOI 硬件 | Cognex、Keyence、Omron、Koh Young、Camtek、Saki、TRI、ViTrox、Hikrobot、OPT | 线速检测、测量、PLC 集成、2D/3D AOI | 他们卖“眼睛”；QualityLoop 卖“异常闭环” |
| AI 视觉平台 | Landing AI、Elementary、Instrumental、Overview.ai、Averroes、Siemens Inspekto、Lumafield | 少样本训练、异常检测、视觉数据 | 多数止步于 defect detection；QualityLoop 接 RCA/CAPA/验证 |
| MES/QMS/eQMS | Siemens、SAP、Rockwell Plex、Dassault、Hexagon ETQ、MasterControl、Veeva、Sparta TrackWise | 合规流程、CAPA、审计、企业 workflow | 大系统重、表单化；QualityLoop 做线边实时 evidence layer |
| 机器人/自动化 | ABB、FANUC、KUKA、Yaskawa、Universal Robots、Omron、Siemens | 执行动作、自动上下料、机器人单元 | QualityLoop 决定何时动、为何动、如何验证 |

## Moat

- 缺陷 taxonomy：跨产品、产线、设备、供应商和客户统一质量语言。
- Station recipe：相机、光源、机器人姿态、模型版本、阈值和工艺规则一起版本化。
- MES/QMS/PLC/SPC adapter：接口越多，切换成本越高。
- 闭环质量记忆：缺陷 -> 根因 -> CAPA -> 复检 -> 复发结果持续积累。
- 人工复判和 HIL 数据：真实工厂里“为什么判断为 OK/NG”的稀缺数据。
- 模型治理：灰度、回滚、model card、training data hash、审计包。
- 工作流嵌入：周质量会、CAPA 审核、供应商反馈和 NPI ramp 模板成为组织习惯。

## Architecture

### EdgeVision Station

- Qualcomm board + camera / light / trigger。
- Qualcomm IM SDK / GStreamer / ISP / video pipeline。
- QNN / ONNX Runtime QNN EP / TFLite。
- GenICam、OPC UA Vision、工业相机、光源 recipe、trigger、strobe、曝光。

### QualityCore

- `DefectObservation`
- `QualityEvent`
- `CAPA`
- `TraceEvent`
- `ModelRelease`
- MES/QMS/SPC/ERP/PLC adapter
- Issue Graph、RCA Copilot、CAPA workflow、审计包、模型注册和回滚。

### Robot Re-Inspection

- ROS 2 + MoveIt 2 做多角度复检。
- 安全由机器人控制器、安全 PLC、光栅、急停和站内互锁负责。
- LeRobot HIL 记录人工接管、复检动作和失败恢复。

### Regional Learning Loop

- 中国数据留在中国租户或客户私有云。
- 海外只接收被批准的脱敏 evidence packet、指标、model card 或合成样本。
- Label Studio / CVAT 标注。
- AI Hub profile / quantize / compile。
- 灰度发布到边缘站，保留 rollback pointer。

## Demo Safety

比赛阶段只做安全桌面演示：

- 只使用塑料样件，不用锋利工具和真实高速输送线。
- 机器人低速低力矩，固定姿态，带亚克力隔离、实体急停、软件 deadman。
- 人手进入 cell、相机丢失、网络故障、低置信度时停止动作。
- 不声称安全认证，不声称可直接部署真实产线。

## Why Qualcomm

QualityLoop 是 Qualcomm 工业 edge AI 的参考应用，因为工厂质量场景天然适合端侧计算：

- 缺陷图、产品图纸、供应商批次、工艺参数敏感，不能默认上传公有云。
- 产线需要低延迟、多相机、光源同步、弱网运行和本地可维护。
- Qualcomm RB3/RB6/IQ 设备可以成为 AI 质检站、机器人复检站和现场质量网关。
- AI Hub、QNN、ONNX Runtime QNN EP 可以给比赛作品带来端侧性能证据。
- LeRobot + Qualcomm edge 让机器人复检路径、人工接管和异常恢复变成可迭代技能。
- 对 Qualcomm 来说，这不是一个 demo app，而是从“开发板”进入“工业质量闭环入口”的生态样板。

## Claims To Avoid

- 不说零缺陷、零漏检、100% 准确率。
- 不说替代所有质检员。
- 不说任意产线几天内上线。
- 不说自动找到真实根因；只能说“候选根因 + 工程师确认”。
- 不说无需 MES/QMS/现场数据。
- 不说替代 Cognex/Keyence/Hikrobot；定位为集成和闭环层。
- 不说 Qualcomm 官方合作/认证，除非真实签约。
- 不说医疗、汽车、半导体合规已满足，除非逐项验证。

## Ask

比赛阶段最需要 Qualcomm 支持三件事：

1. 开发板和 edge AI profile：多相机质检、QNN/ONNX artifact、延迟、功耗、模型灰度和回滚证据。
2. 工业伙伴连接：1-2 个制造业 demo 数据或试点工位，验证 NG -> RCA/CAPA -> 复检闭环。
3. 生态联合展示：把 QualityLoop 作为 Qualcomm edge AI + LeRobot HIL 的工业参考应用。

## Sources

- ASQ Cost of Quality：https://asq.org/quality-resources/cost-of-quality
- McKinsey / Upstream warranty AI：https://upstream.auto/resources/can-ml-and-ai-cut-vehicle-warranty-and-recall-costs/
- NHTSA recalls：https://www.nhtsa.gov/recalls/vehicle-safety-recalls-week
- Deloitte smart manufacturing 2025：https://www.deloitte.com/us/en/about/press-room/deloitte-2025-smart-manufacturing-survey.html
- IFR industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- MarketsandMarkets machine vision：https://www.marketsandmarkets.com/Market-Reports/industrial-machine-vision-market-234246734.html
- Mordor automated optical inspection：https://www.mordorintelligence.com/industry-reports/automated-optical-inspection-equipment-market
- Mordor MES：https://www.mordorintelligence.com/industry-reports/manufacturing-execution-systems-market
- 国家发改委《质量强国建设纲要》：https://www.ndrc.gov.cn/fggz/cyfz/zcyfz/202302/t20230217_1348911.html
- 工业设备更新政策：https://www.nea.gov.cn/2024-04/12/c_1310770982.htm
- 新华网汽车产销：https://www.news.cn/fortune/20260114/cbbd861081c349d8ae238167ca418fa3/c.html
- 中国汽车召回：https://news.cctv.com/2026/03/19/ARTInDBwwVnfUPIP9ZNUP82J260319.shtml
- 医疗器械 GMP：https://www.ccfdie.org/cn/jyjlqx/webinfo/2025/11/1759929271175159.htm
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Qualcomm RB6：https://www.qualcomm.com/internet-of-things/products/robotics-rb6-platform
- Qualcomm IM SDK：https://www.qualcomm.com/developer/software/qualcomm-intelligent-multimedia-sdk
- Qualcomm AI Hub compile：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- ONNX Runtime QNN EP：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- OPC UA Vision：https://opcfoundation.org/markets-collaboration/machine-vision/
- ISA-95：https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard
- LeRobot HIL：https://huggingface.co/docs/lerobot/hil_data_collection
- OSHA Robotics Safety：https://www.osha.gov/otm/section-4-safety-hazards/chapter-4
