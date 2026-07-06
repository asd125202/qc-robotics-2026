# 骁工 XiaoGong Pitch

更新时间：2026-07-05。人形机器人商业化进展、量产节奏、客户试点、政策补贴、标准和安全要求都在快速变化；真实参赛材料和商业计划应在提交前复核最新公告、客户合同、监管要求和硬件参数。

## Core Thesis

骁工 XiaoGong 是面向真实工序的商用人形平台：

> 不是发布会上的通用人形机器人，而是能被采购、验证、远程协助、持续迭代的具身工作单元。

2025-2026 年的市场信号已经很清楚：人形机器人正在从实验室演示进入工厂、仓储、物流和接待巡检的早期商业化试点；但当前最成熟的落地方式不是“完全自主的通用劳动力”，而是先锁定高频、可度量、可接管、可复盘的工序。

骁工的产品判断：

- 先做任务包，不做泛化承诺。
- 先做 30 天现场建模、90 天试点和 KPI 验收，不直接承诺大规模替人。
- 让每一次低置信度、人工接管和失败恢复都进入 LeRobot 数据闭环。
- 用 Qualcomm 边缘计算把低延迟感知、策略推理、传感器融合、安全边界和本体运行留在机器人本地。

## Five-Thread Research Synthesis

### 1. Global Market Reality

Figure 在 BMW Spartanburg 的公开材料显示，Figure 02 完成了 11 个月产线部署，累计 90,000+ 零件、1,250+ 运行小时，并服务 30,000+ X3 车辆生产。Agility 与 GXO 的 multi-year RaaS 协议、Toyota Canada 和 Mercado Libre 商业协议，也说明物流和制造工位正在成为人形机器人最现实的第一批商业场景。

安全表达：这是从 demo 进入 paid pilot / narrow deployment 的信号，不等于通用自主劳动力已经成熟。

### 2. China Deployment Lane

中国政策明确把人形机器人定位为未来产业和制造业升级方向。工信部 2023 指导意见提出 2025 年初步建立创新体系、整机达到国际先进水平并实现批量生产，2027 年形成安全可靠产业链供应链体系并深度融入实体经济。

中国版骁工需要面向场景试点：汽车/3C 工厂、物流分拣、药房/零售、园区接待巡检、教育科研和数据采集中心。差异化重点不是“又一台本体”，而是本地云/私有化、中文工单、二维码/门禁/支付/企业系统集成、数据合规和本地服务网络。

### 3. Productization Bottleneck

人形机器人真正难的不是单个动作视频，而是同步传感器、确定性控制、功耗热设计、安全证据、OTA、远程诊断、备件、现场维护和持续训练。Qualcomm Dragonwing IQ10 RRD 这类 reference design 的价值在于把 compute、sensor I/O、networking、deterministic control、software stack 和 lifecycle tools 收敛到更清晰的产品边界。

### 4. Technical Architecture

骁工把系统拆成三条闭环：

- Real-time body loop：本地安全、whole-body control、关节/力/速度限制、跌倒风险、急停和运动降级。
- Qualcomm edge autonomy loop：多模态感知、策略推理、ROS 2 skill runtime、任务编排、低置信度检测。
- Cloud learning loop：中国/海外云训练、LeRobot dataset、评估、签名 artifact、灰度发布、失败片段挖掘。

LeRobot 负责 episode、policy、evaluation 和 HIL 数据回流，但不直接越过本体安全层写入电机。

### 5. Creative Business Design

骁工不是卖“机器人像人”，而是卖“人形机器人变成可交付工位”：

- 每个客户先购买任务包：搬箱、分拣、巡检、接待、工具递送、数据采集。
- 每个任务包都有能力账本：成功率、周期、人工接管率、低置信度事件、故障恢复、适用场地和禁用条件。
- 每一次人工协助都被记录成训练数据，进入下一轮私有模型改进。
- 收入来自硬件/OEM margin、WorkOS subscription、任务包、RaaS per shift、试点服务、私有模型改进和市场分成。

## Product Modules

### 1. Task-Bounded Humanoid WorkOS

骁工的核心不是一个聊天型通用机器人，而是可验证的工序操作系统：

- 任务 manifest：输入、输出、传感器、工位、工具、禁区、安全等级、失败处理。
- 能力账本：按任务记录成功率、周期、人工协助、硬件故障、模型版本和数据版本。
- 现场建模：地图、工位、料箱、托盘、门禁、电梯、人员动线和安全区。
- KPI dashboard：任务吞吐、接管率、停机时间、训练收益和扩展建议。

### 2. Human-Assist Learning Loop

骁工默认承认真实世界会失败：

1. 机器人执行任务。
2. 置信度下降或安全边界触发。
3. 本体减速、保持、蹲坐或退回安全姿态。
4. 人类远程或现场接管。
5. 系统记录自主片段、接管片段、恢复片段和结果。
6. episode 进入 LeRobot-compatible dataset。
7. 云端训练和评估后，签名 artifact 灰度回到 Qualcomm edge。

卖点不是“永不需要人”，而是“每一次需要人，都会让下一次更少需要人”。

### 3. Qualcomm Edge Runtime

骁工把 Qualcomm 放在产品必须位置：

- On-device AI：视觉、深度、人体/障碍物、语音/意图、抓取 affordance、低延迟策略推理。
- Sensor fusion：相机、深度、IMU、力/触觉、编码器、LiDAR/ToF 和安全传感器时间同步。
- Deterministic control：PCIe、TSN、EtherCAT/CAN-FD、实时 I/O 和本体控制边界。
- Connectivity：5G / Wi-Fi / private network，让远程协助、fleet telemetry 和云训练闭环可运营。
- Lifecycle：签名 OTA、模型 artifact、AI Hub / QNN / ExecuTorch 路线、profile 和回滚。

### 4. China / Overseas Versions

中国版：

- 强调制造业升级、地方政策、人形机器人数据中心、试点采购和本地服务。
- 支持私有云/本地云、国产 GPU 训练候选、本地日志、中文工单、企业微信/钉钉/飞书、WMS/MES/ERP 对接。
- 首批场景：汽车/3C 产线物流、仓储分拣、药房/零售补货、园区巡检接待、教育科研与数据采集。

海外版：

- 强调 RaaS、labor shortage、warehouse/factory safety、insurable deployment、fleet uptime 和 task ROI。
- 对接 GXO/Agility、Figure/BMW、Apptronik/Mercedes/Jabil 等市场叙事。
- 首批场景：物流 tote handling、汽车零部件加载、warehouse sequencing、facility inspection 和 data collection service。

### 5. Competition Demo

比赛不需要真的造完整人形本体。骁工可以把完整商业逻辑压缩成一个可信 demo：

1. 浏览器中展示工厂/物流工位：托盘、料箱、质检点、巡检路线和人工协助台。
2. 用桌面机械臂或移动底盘模拟“骁工任务包”的一部分，例如识别料箱、抓取/递送、异常标记。
3. 本体侧运行 Qualcomm edge inference 和安全状态机。
4. 人为制造低置信度标签、遮挡或位置偏差。
5. 系统触发人类接管，记录 episode。
6. Dashboard 显示 LeRobot 数据集、训练 job、评估、签名部署包和能力账本变化。

评委看到的是完整产品逻辑：任务 -> 安全 -> 接管 -> 数据 -> 训练 -> 部署 -> 商业 KPI。

## Why Qualcomm Should Support It

骁工把 Qualcomm 的价值从“这块板子可以跑模型”提升为“人形机器人商业化平台的边缘标准件”：

- 人形机器人需要高带宽多传感器、本地推理、低功耗、连接、安全和长期供货，正好对应 Dragonwing 的组合优势。
- IQ10 RRD 这种 full-stack reference design 可以成为人形机器人从 prototype 到 production 的缺省底座。
- Qualcomm 可以通过骁工建立开发者生态：LeRobot 数据、AI Hub profile、QNN/ExecuTorch、ROS 2 runtime、任务包市场和系统集成伙伴。
- 对中国比赛尤其重要：如果 Qualcomm 能把人形机器人从“本体竞赛”提升为“商业部署底座”，就能在政策、教育、创业和企业试点之间形成生态入口。

一句话：

> 人形机器人越接近商业化，越需要 Qualcomm 这样的边缘平台把感知、控制、连接、安全和生命周期管理变成可复制产品。

## Claims To Avoid

- 不说“完全替代人工”。
- 不说“家庭通用劳务已经成熟”。
- 不说“无需遥操作或人工协助”。
- 不把所有 demo 视频当作生产部署证据。
- 不承诺固定 ROI、固定成功率或零事故。
- 不把 LeRobot 说成直接控制电机的安全系统；安全关键控制必须在本体侧。

## Sources

- Figure / BMW production deployment：https://www.figure.ai/news/production-at-bmw
- BMW Group Figure 03 project：https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg
- Agility / GXO RaaS agreement：https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics
- Agility 100k totes：https://www.agilityrobotics.com/content/digit-moves-over-100k-totes
- Agility Toyota Canada：https://www.agilityrobotics.com/content/agility-robotics-announces-commercial-agreement-with-toyota-motor-manufacturing-canada
- Boston Dynamics Atlas：https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/
- Apptronik Series A：https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a
- Jabil / Apptronik Apollo：https://investors.jabil.com/news/news-details/2025/Apptronik-and-Jabil-Collaborate-to-Scale-Production-of-Apollo-Humanoid-Robots-and-Deploy-in-Manufacturing-Operations/default.aspx
- Unitree G1：https://www.unitree.com/g1/
- 1X NEO：https://www.1x.tech/discover/neo-home-robot
- NVIDIA GR00T：https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks
- Qualcomm IQ10 RRD：https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- Qualcomm AI Hub：https://aihub.qualcomm.com/get-started
- Qualcomm RB3 Gen 2：https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit
- ROS 2 real-time background：https://design.ros2.org/articles/realtime_background.html
- ROS 2 lifecycle：https://design.ros2.org/articles/node_lifecycle.html
- ros2_control hardware interfaces：https://control.ros.org/rolling/doc/ros2_control/hardware_interface/doc/hardware_interface_types_userdoc.html
- MoveIt 2：https://moveit.picknik.ai/
- LeRobot hardware integration：https://huggingface.co/docs/lerobot/en/integrate_hardware
- LeRobot HIL data collection：https://huggingface.co/docs/lerobot/hil_data_collection
- LeRobot inference：https://huggingface.co/docs/lerobot/main/inference
- LeRobot dataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- DROID dataset：https://droid-dataset.github.io/
- Open X-Embodiment：https://robotics-transformer-x.github.io/
- MIIT humanoid robot guidance / Xinhua：https://www.xinhuanet.com/tech/20231103/e4d37192a8de419d9c2bc24b9d87dcdb/c.html
- Shenzhen robotics policy：https://stic.sz.gov.cn/xxgk/tzgg/content/post_12052515.html
- UBTECH Walker S2：https://www.ubtrobot.com/cn/humanoid/products/walker-s2
- AgiBot：https://www.agibot.com/article/231/detail/31.html
