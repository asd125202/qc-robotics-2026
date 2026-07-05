# Vertical Market Playbooks

更新时间：2026-07-05。

## Why This Matters

评委需要看到商业潜力不是一句“可以卖给企业”。本项目应展示同一个机器人产品底座如何被包装成多个垂直市场产品：

- 同一套 RobotMac Core 硬件 SKU。
- 同一套 LeRobot CloudTwin 训练闭环。
- 同一套 SkillDock 技能包机制。
- 同一套 EdgeFleet 运维逻辑。
- 不同市场使用不同机器人形态、技能模板、销售包和评价指标。

## Five Playbooks

### 1. FactoryPilot

目标客户：小型工厂、产线系统集成商、质检团队。

机器人形态：

- 移动巡检车。
- 固定工位机械臂。
- 可选视觉质检相机条。

首批技能：

- 产线异常拍照。
- 指针/仪表/状态灯巡检。
- 简单抓取和放置。
- 失败片段回流训练。

商业包装：

- Core Pro 或 Core Industrial。
- EdgeFleet 企业运维。
- 私有数据集和质检模板。
- 年度维护和模型更新。

评分价值：

- 商业潜力强。
- Qualcomm edge AI 的低延迟和本地隐私价值清楚。
- 适合展示“云训练、本地执行”的安全边界。

### 2. LogisticsMove

目标客户：仓储、园区、实验室内部物流。

机器人形态：

- AMR / 小型移动底盘。
- 可选载物舱或轻量机械臂。

首批技能：

- 路线巡航。
- 目标跟随。
- 货物到站检测。
- 异常阻挡记录。

商业包装：

- Core Lite / Core Pro。
- EdgeFleet 队列运维。
- CloudTwin 训练路径优化。
- SkillDock 安装“巡航/跟随/异常记录”技能包。

评分价值：

- 演示可控。
- 能扩展到多机队列。
- 适合讲 RaaS / fleet operations。

### 3. LabForge

目标客户：高校实验室、生物/材料/硬件实验室、自动化研发团队。

机器人形态：

- 桌面机械臂。
- 相机/称重/扫码/小型夹具。

首批技能：

- 样品转移。
- 扫码记录。
- 固定流程示教复现。
- 失败接管和动作修正。

商业包装：

- Core Pro。
- LeRobot CloudTwin 训练包。
- EduForge 课程或企业实验室模板。
- 数据集和实验 SOP 管理。

评分价值：

- 与 ACT 模仿学习高度匹配。
- 适合比赛第一 demo。
- 可用桌面环境控制风险。

### 4. CampusService

目标客户：高校、园区、酒店、展馆、医院非关键服务场景。

机器人形态：

- 小型服务机器人。
- 移动底盘 + 语音/屏幕/货架。

首批技能：

- 迎宾和引导。
- 简单配送。
- 目标跟随。
- 异常上报。

商业包装：

- Core Pro。
- CloudTwin 训练本地场景动作。
- EdgeFleet 管理多台机器人。
- SkillDock 安装不同服务技能。

评分价值：

- 用户容易理解。
- 可突出 Qualcomm 多媒体、连接和低功耗价值。
- 注意避免把安全关键控制放到云端。

### 5. EduForge

目标客户：高校、训练营、开发者社区、比赛团队。

机器人形态：

- 教学机械臂。
- 小车。
- 传感器和 edge AI kit。

首批技能：

- 数据采集。
- ACT 训练。
- 边缘部署。
- 网站路演。

商业包装：

- Core Lite / Core Pro。
- 中文课程。
- 云训练额度。
- 比赛模板和认证。

评分价值：

- 能解释开发者生态价值。
- 对 Qualcomm 长期开发者心智有意义。
- 适合初赛传播和复赛训练。

## Recommended Competition Focus

初赛主线建议：

- 主产品：RobotMac Core + LeRobot CloudTwin。
- 主 demo：LabForge 桌面机械臂。
- 商业扩展：FactoryPilot + LogisticsMove + EduForge。

原因：

- LabForge 最容易把 LeRobot / ACT / edge deployment 讲清楚。
- FactoryPilot 和 LogisticsMove 最容易证明商业价值。
- EduForge 最容易证明 Qualcomm 开发者生态价值。

## Sources

- IFR World Robotics：https://ifr.org/worldrobotics/
- IFR service robots growth：https://ifr.org/news/service-robots-see-global-growth-boom
- IFR China robotics strategy：https://ifr.org/ifr-press-releases/news/china-makes-ai-powered-robots-core-of-national-strategy
- AgileX Robotics：https://global.agilex.ai/
- AgileX ROS2 education kit：https://global.agilex.ai/blogs/news/the-world-s-first-ros2-mobile-robot-navigation-open-source-education-kit-released
- Unitree Robotics：https://www.unitree.com/
