# SkillCertKit Pitch

更新时间：2026-07-05。

## Core Thesis

如果 SkillDock 要成为机器人技能市场，就不能只上传模型文件。每个技能都必须带上可审查、可复现、可回滚的证据包：

> SkillCertKit = skill manifest + dataset lineage + hardware compatibility + edge benchmark + safety gate + signature + rollback + marketplace review。

它把机器人技能从“开发者打包的策略模型”变成企业客户、系统集成商和 Qualcomm 生态都能信任的可安装产品。

## Why This Matters

机器人技能比普通 App 风险更高。一个策略模型如果拿错相机、跑在错误硬件、越过安全边界或无法回滚，影响的不是界面崩溃，而是真实设备、人员和客户现场。

SkillCertKit 解决的核心问题：

- 买家如何知道某个技能适配自己的机器人硬件？
- 系统集成商如何复用技能模板，而不是每次重新交付？
- 企业客户如何审计数据来源、权限范围、运行指标和失败记录？
- Qualcomm 如何成为机器人技能上架、部署和认证时必须声明的 edge target？

## Certification Pipeline

### 1. Submit Package

开发者提交技能包、训练配置、策略 artifact、运行依赖和目标任务说明。

### 2. Manifest Check

检查 `skill.yaml`，确认输入输出契约、传感器、执行器、权限、安全模式和目标硬件 profile。

### 3. Dataset Lineage

记录 LeRobot-compatible dataset、采集设备、episode 数量、失败样本、版本号和客户数据权限。

### 4. EdgeRuntimeBench

在 Qualcomm edge target 上生成 compile / profile / deploy 证据，至少包含延迟、资源占用、稳定性和部署包版本。

### 5. SafetyOps Gate

检查急停、工作空间边界、速度限制、人工接管、审计日志和 rollback package。

### 6. Marketplace Publish

通过认证后进入 SkillDock，买家看到硬件兼容、适用场景、证据报告、版本历史和支持方式。

### 7. Monitor And Rollback

安装后的运行日志进入 EdgeFleet。失败片段回到 DataFlywheel，版本异常时自动回滚。

## Skill Manifest Example

```yaml
skill_id: labforge.sample-transfer.v1
robot_profile: robotmac.core.pro.qcs8550
policy_type: act
dataset_uri: lerobot://labforge/sample-transfer-v1
permissions:
  sensors: [front_camera, wrist_camera]
  actuators: [arm, gripper]
safety:
  max_speed: low
  workspace: tabletop_cell
deployment:
  target: qualcomm_edge_package
  rollback: required
evidence:
  edge_runtime_bench: required
  safetyops_gate: required
```

## Evidence Pack

每个认证技能包至少包含：

- Manifest：输入、输出、权限、依赖和目标硬件。
- Dataset：来源、版本、episode、失败样本和授权边界。
- Hardware：RobotMac profile、相机、执行器、IO 和 runtime version。
- Runtime：Qualcomm edge benchmark、部署包和资源指标。
- Safety：工作空间、速度、急停、接管和审计记录。
- Rollback：上一稳定版本、回滚条件和恢复流程。

## Commercial Value

SkillCertKit 让 SkillDock 具备商业化基础：

- 企业买家能先看证据，再安装技能。
- 系统集成商能销售可复用、可验收的行业技能模板。
- 开发者能围绕认证标准构建付费技能。
- 平台可以收取认证费、上架费、企业私有技能库费用和支持订阅。
- Qualcomm 成为技能兼容表和边缘部署证据中的默认硬件目标。

## Competition Story

在比赛叙事中，SkillCertKit 负责回答评委可能提出的关键问题：

- 技能市场如何避免变成无法落地的模型仓库？
- 商业客户如何采购和验收机器人能力？
- Qualcomm 处理器如何从 demo 硬件变成生态标准？
- 为什么这个项目能形成长期平台，而不是一次性比赛作品？

## Sources

- ROS Index：https://index.ros.org/
- ROS package manifest documentation：https://docs.ros.org/en/rolling/How-To-Guides/Package-maintainer-guide.html
- LeRobot documentation：https://huggingface.co/docs/lerobot/index
- Qualcomm AI Hub：https://aihub.qualcomm.com/
- Existing project pages：SkillDock、EdgeRuntimeBench、SafetyOps、DataFlywheel、EdgeFleet
