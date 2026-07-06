# RobotAppLayer Pitch

更新时间：2026-07-06。

## One-Line Thesis

RobotAppLayer 是 ROS 2 和 LeRobot 之上的机器人应用 ABI：让开发者像发布手机应用一样发布机器人技能，并把签名包、权限、兼容性、仿真评测、Qualcomm edge profile、上架、计费和回滚做成统一流程。

## 01 · Problem

今天写一个机器人应用，仍然像重新做系统集成。

- 应用开发者想写巡检、配送、实验室样品转移、教学课程或现场运维，却先被相机、夹爪、电机、ROS topic、launch file、QoS、driver bring-up 和模型部署拦住。
- 企业客户需要权限、安全边界、审计、数据归属、回滚和责任证明，但机器人应用通常还停留在脚本和项目文件夹阶段。
- 开发者没有可信兼容性、认证、分发、试用、授权、用量计费和收入分成，生态就很难越过一次性项目。

## 02 · Current Alternatives Fail

RobotAppLayer 不应该被描述成“另一个 robot OS”。更强的定位是：中立应用层和分发层。

- ROS 2：必要中间件，提供 topic、service、action、lifecycle、QoS 和 DDS security，但不是 app store、权限系统、计费系统或认证市场。
- Open-RMF / VDA 5050：适合多机调度、设施协调和 AMR/AGV 协议，不负责技能包、模型、权限、上架和收益分成。
- Foxglove / MCAP：强化观测、日志和物理 AI 数据，但不决定应用能否安装、运行、回滚和收费。
- Viam / Intrinsic：最接近机器人开发平台方向，但更偏自有 runtime、企业工作站或工业自动化。
- NVIDIA Isaac / GR00T：强化 GPU-first 仿真、ROS 加速和 foundation model，不是 Qualcomm-native 的技能分发和边缘证据层。
- OEM app stores：UR+、KUKA、FANUC、ABB、PUDU、Unitree 都证明生态方向成立，但多数锁在单一硬件品牌。

## 03 · Solution

RobotAppLayer 定义 `.rap` 应用包和 RobotKit 稳定 API。

`.rap` bundle 包含：

- app id、publisher signature、version、SBOM。
- container image、launch graph、ROS interface map。
- LeRobot policy/model references。
- supported robot profiles、resource budgets、simulation tests。
- safety limits、permission declarations、billing SKU、rollback target。

RobotKit facade 暴露：

- `observe`
- `move`
- `grasp`
- `speak`
- `record`
- `train`
- `profile`
- `install`
- `monitor`
- `rollback`

底层仍然可以映射到 ROS 2 nodes/actions/services、Open-RMF、VDA 5050、MCAP/Foxglove、LeRobot Dataset v3、Qualcomm AI Hub/QNN/ONNX Runtime QNN 和 EdgeFleet。

## 04 · Why Now

机器人正在进入“应用生态”阶段，但还没有通用运行时。

- ROS 2 基础设施已经足够成熟，可以作为应用层映射的底座。
- LeRobot 把数据采集、策略训练、HIL 和低成本机器人带给更大开发者群体。
- Foxglove / MCAP 把物理 AI 数据工作流标准化。
- VDA 5050 v3.0.0、Open-RMF 和 fleet orchestration 让多机器人部署更接近标准化。
- UR+、KUKA、FANUC、ABB、PUDU、Unitree、Hugging Face Reachy Mini 和 OpenMind 等信号表明“机器人应用商店”正在成为用户能理解的形态。
- Qualcomm Dragonwing / RB3 / IQ10 RRD 给了 edge-first 机器人应用一个清晰硬件 target。

## 05 · Product

第一版不要宣称支持所有机器人。先服务 ROS 2 + LeRobot + Qualcomm edge 的可控子集，从低风险应用开始：

- 数据采集和现场失败回流。
- 巡检和远程运维。
- 实验室样品转移。
- 教学和开发者课程。
- 低力矩操作技能。

产品模块：

- RobotApp SDK：Python / TypeScript API。
- Permission Manifest：物理权限、ODD、ROS/DDS 边界、网络和云训练授权。
- Compatibility Registry：robot profile、sensor、effector、ROS distro、LeRobot version、Qualcomm target、runtime、compute budget。
- Certification CI：MCAP replay、Gazebo/Isaac 仿真、HIL、碰撞/接管/成功率门槛、QNN profile、SBOM、rollback test。
- SkillDock Store：公开市场、企业私有商店、OEM 商店、试用、订阅、用量计费和开发者分成。
- EdgeFleet Runtime：签名安装、灰度、遥测、事故包、数据回流、版本回滚和客户现场审计。

## 06 · Product API Objects

- `RobotProfile`：ROS domain、namespace、lifecycle、传感器、夹爪、底盘、机械臂、E-stop、RB3/QCS6490/QCS8550/IQ10 target。
- `TaskContract`：任务阶段、前置条件、成功标准、人工接管、失败标签、MCAP 记录和 LeRobot episode 生成策略。
- `SkillManifest`：app id、publisher、签名、版本、容器、ROS interface map、LeRobot policy、rollback target 和 billing SKU。
- `PermissionPolicy`：允许 camera/map/navigate/grasp；禁止 raw motor、E-stop reset、人体接触和未授权 cloud upload。
- `LeRobotPolicyBinding`：dataset、checkpoint、processors、action Hz、HIL/DAgger 策略和失败样本回流。
- `QualcommEdgeProfile`：QNN context binary、ONNX Runtime QNN、input shape、p95 latency、memory、compute unit 和 AI Hub profile evidence。
- `EvalHook`：MCAP replay、Gazebo/Isaac、hardware-in-loop、扰动测试和 success/intervention/collision gates。
- `AppRelease`：install checks、canary rollout、active/degraded 状态、incident capsule、fleet metrics、entitlement 和 rollback。

## 07 · Market & Business Model

买方不是普通终端消费者，而是 robot OEM、系统集成商、企业开发团队、教育/研究机构和应用开发者。

中国版：

- OEM bundle。
- SI 私有部署。
- 教育/比赛套件。
- 低 take-rate 技能市场。
- 云训练和边缘部署用量。

海外版：

- 企业控制平面。
- 认证 marketplace。
- 私有商店、SSO、审计和合规。
- 支持 SLA。
- certified partner app 和集成包。

定价假设：

- 免费 SDK、模拟器适配、样例应用和公开 listing。
- Team / Pro：每开发者每月 49-149 美元，包含私有应用、CI 验证、日志、权限和仿真任务。
- Production runtime：每台活跃机器人每月 50-250 美元，包含部署、遥测、权限、回滚和审计。
- Enterprise site license：每站点每年 25k-150k 美元，包含私有市场、SSO、合规、on-prem/private cloud、WMS/MES 集成和 SLA。
- Marketplace take rate：付费应用/技能 15%-30%，工业场景可以降低 take rate 并增加认证费。
- Certification fees：标准应用 1k-5k 美元，高安全/高合规应用 10k+ 美元。

## 08 · Competition & Moat

壁垒不是“封装 ROS”。壁垒是可信应用生态的复利。

- App ABI：比 topic 更稳定的 RobotKit 能力接口。
- Permission taxonomy：物理动作、数据、网络、云训练和人工接管形成可审计权限图。
- Compatibility matrix：机器人型号、传感器、执行器、ROS distro、LeRobot policy 和 Qualcomm target 的兼容证据。
- Certification corpus：仿真、HIL、MCAP replay、事故回放和安全门禁积累失败模式。
- Marketplace gravity：开发者、SI、OEM、企业客户和教育用户共享安装、试用、授权和分成流程。
- Qualcomm evidence：AI Hub/QNN profile、低功耗边缘运行、连接、安全启动和 device attestation 成为上架门槛。

## 09 · Why Qualcomm

Qualcomm 的机会不是只把开发板卖给机器人开发者，而是成为机器人应用默认 target。

RobotAppLayer 可以把 Qualcomm 放进每个 app release：

- `target_profile`: `rb3-gen2`, `qcs6490`, `qcs8550`, `iq10-rrd`
- `runtime`: `qnn_context_binary`, `onnxruntime-qnn`, `tflite`, `qairt`
- `evidence`: AI Hub compile/profile/inference metrics, latency, memory, compute-unit use
- `secure_install`: signed skill bundle, permissions, rollback, device attestation
- `marketplace`: Dragonwing-ready skill cards

近期目标用 RB3 Gen 2 / QCS6490 做比赛和早期验证。IQ10 RRD 作为 forward profile，不把 2026 年 7 月的 demo 绑定在尚未大规模可得的未来硬件上。

## 10 · Demo & Ask

7 分钟 demo：

1. `robotapp init lab-transfer --target rb3-gen2` 生成 `.rap`、RobotProfile、权限和 TaskContract。
2. 展示应用代码调用 `observe / grasp / record`，而不是直接操纵 raw motor topic。
3. 运行 LabForge 样品转移任务并生成 MCAP + LeRobot Dataset v3 episode。
4. 模拟失败和人工接管，把失败片段送回训练。
5. 导出策略，通过 AI Hub / QNN / ONNX Runtime QNN 生成 edge evidence。
6. SkillCertKit 通过后进入 SkillDock skill card。
7. EdgeFleet 灰度安装；异常时生成 incident capsule 并回滚。

向高通要：

- 6-8 周联合验证 sprint。
- RB3 Gen 2 / QCS6490 硬件 target。
- AI Hub / QNN / QAIRT office hours。
- Robotics Hub 发布指导。
- IQ10 RRD roadmap 指导。
- 5-10 个 OEM/SI/开发者访谈。

## Sources

- ROS 2 Actions：https://design.ros2.org/articles/actions.html
- ROS 2 Lifecycle：https://design.ros2.org/articles/node_lifecycle.html
- ROS 2 DDS Security：https://design.ros2.org/articles/ros2_dds_security.html
- Open-RMF：https://www.open-rmf.org/
- VDA 5050：https://www.vda.de/en/topics/automotive-industry/vda-5050
- MCAP：https://mcap.dev/
- Foxglove：https://foxglove.dev/
- Viam：https://docs.viam.com/what-is-viam/
- Intrinsic Flowstate：https://www.intrinsic.ai/flowstate
- NVIDIA Isaac ROS：https://developer.nvidia.com/isaac/ros
- LeRobot：https://huggingface.co/docs/lerobot/en/index
- LeRobot Dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- Qualcomm AI Hub：https://workbench.aihub.qualcomm.com/docs/
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- Dragonwing IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Universal Robots UR+：https://www.universal-robots.com/marketplace/
- PUDU Open Platform：https://open.pudutech.com/en
