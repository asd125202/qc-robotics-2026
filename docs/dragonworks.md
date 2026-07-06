# DragonWorks Pitch

更新时间：2026-07-06。本页按照 YC / Airbnb 风格整理：先讲问题和为什么现在，再讲解决方案、证据包、市场、竞争、壁垒、Qualcomm 请求、演示和 claim boundaries。

## One-Line Pitch

DragonWorks 是 Qualcomm-first robotics workbench / control plane：把 Dragonwing 设备、TeleopStudio 数据、LeRobot dataset、TrainRouter 双云训练、AI Hub / QNN edge evidence、SkillCertKit 门禁、SkillDock 发布、EdgeFleet 运行证据和比赛提交材料放到同一条可复现产品流水线里。

## Problem

机器人团队现在不是缺单点工具，而是缺一条可信流水线。

今天的状态：

- 设备接入、传感器数据、teleop episode、训练 job、模型版本、边缘 profile、技能包、fleet 日志和提交视频分散在不同工具里；
- demo 能跑，但团队说不清这次成功来自哪份数据、哪个训练 job、哪个 runtime、哪个板卡 profile；
- Qualcomm edge 往往在最后部署阶段才被考虑，错过了从数据采集到训练约束的全链路价值；
- 比赛提交材料常常手工拼装，难以证明“可复现”和“商业化”。

## Why Now

Qualcomm 已经拥有关键工具碎片，现在需要一条开发者旅程：

- Dragonwing Robotics Hub：开发者样例与机器人项目展示。
- AI Hub Workbench：模型转换、compile、profile、inference 和 deployment。
- QNN / QAIRT / ONNX Runtime QNN：边缘 runtime 路径。
- Device Cloud / Profiler：真实设备或远程设备运行证据。
- RB3 / QCS6490 / QCS8550 / IQ-8275 / IQ10 RRD：从开发套件到生产参考设计的硬件路径。
- LeRobot / TeleopStudio / CloudTwin / TrainRouter：真实机器人 episode 到 cloud training 的路径。

NVIDIA 已经把 Isaac / Jetson 讲成了 GPU-first robotics path。DragonWorks 的机会是把 Qualcomm 讲成 edge-first robot skill release path。

## Insight

下一代机器人开发平台不是“机器人 IDE”，而是 evidence layer。

真正有价值的是把：

> “这个机器人 demo 跑了一次”

变成：

> “这个技能在什么设备、什么数据、什么训练 job、什么 Qualcomm runtime、什么安全边界下可以复现、发布、回滚。”

## Solution

DragonWorks 不替代 ROS、LeRobot、AI Hub、Foxglove、Formant 或 Viam。它站在这些工具之上，把完整 release graph 组织成产品界面。

核心模块：

- DeviceDock：Dragonwing / RB3 / QCS / IQ target registry，记录 board、SoC、OS、runtime、camera、actuator、firmware、health。
- Dataset Ledger：LeRobot-compatible dataset、episode hash、failure clips、operator/site/device、rights、region。
- TrainRouter Console：China / Overseas lane、GPU provider、budget guard、eval gate、Qualcomm target profile。
- Edge Evidence：AI Hub / QNN / QAIRT / ONNX Runtime QNN artifacts，latency、memory、thermal、power、fallback。
- Skill Gate：SkillCertKit allow/deny result、SBOM/VEX、signature、safety boundary、rollback。
- Skill Release：SkillDock card、pricing/support、staged rollout、previous-known-good。
- Fleet Feedback：EdgeFleet logs、failure event、manual takeover、rollback、new training episode。
- Submission Builder：evidence table、screenshots/links、BOM、code steps、3-minute storyboard。

## Evidence Packet

DragonWorks 的核心产品屏幕应该是 evidence packet，而不只是 dashboard。

建议 artifacts：

- `device-registry.json`
- `dataset_manifest.json`
- `split_manifest.json`
- `job_contract.v1.yaml`
- `cloud_job_record.json`
- `eval_report.json`
- `qualcomm_export_manifest.json`
- `edge-profile.qualcomm.json`
- `skill.yaml`
- `policy-decision.json`
- `install-audit-log.jsonl`
- `release-record.json`
- `submission-demo-builder.json`

这些 artifact 已经在 TrainRouter、SkillCertKit、SkillDock、EdgeFleet 等页面中分别出现。DragonWorks 的价值是把它们聚合成一条完整项目状态。

## Market

第一批用户：

- Qualcomm / Arduino / Hackster-style 开发者；
- 机器人比赛团队；
- 高校和实验室；
- 系统集成商；
- 机器人 OEM；
- RaaS / fleet operators；
- 企业创新团队。

免费入口吸引开发者，付费来自团队协作和证据工作流：

- Developer：免费项目模板、submission builder、demo storyboard。
- Team：按 seat、设备数、数据存储、训练 job、profile credits、release history 收费。
- Enterprise：私有部署、SSO/RBAC、审计、regional data lanes、SkillCertKit evidence、EdgeFleet hooks。
- Ecosystem：reference skills、SI/OEM templates、SkillDock 上架、validation services、training credits。

## Competition

DragonWorks 不能声称“全栈替代”：

- NVIDIA Isaac / Omniverse / GR00T：GPU-first simulation、synthetic data、physical AI stack。
- Intrinsic Flowstate：工业 workcell、behavior trees、skills 和 sim-to-real。
- Viam：robot app/runtime/fleet platform。
- Foxglove：robotics data observability 和 MCAP workflow。
- Formant：enterprise fleet monitoring / teleop / incident management。
- ROS / Gazebo / Nav2 / MoveIt：机器人基础设施。
- LeRobot：open robot learning datasets、policies、training tools。
- Qualcomm Robotics Hub / AI Hub：官方工具碎片。

DragonWorks 的准确定位：

> Qualcomm-first robotics developer workbench for turning real robot episodes into validated edge skills.

## Moat

短期壁垒：

- Qualcomm target templates。
- Dragonwing / RB3 / QCS / IQ profile library。
- TrainRouter + CloudTwin + SkillCertKit + SkillDock 的端到端模板。

中期壁垒：

- release evidence graph。
- 每个 episode、training job、profile、skill gate、install、failure、rollback 都成为可查询关系。
- competition/submission builder 降低开发者参与门槛。

长期壁垒：

- ecosystem distribution。
- Robotics Hub reference projects、SkillDock skills、SI/OEM templates、education kits、training credits、validation services 互相强化。

## Qualcomm Ask

请求 Qualcomm 支持 6-8 周 “DragonWorks Dragonwing Validation Sprint”：

1. Hardware：RB3 Gen 2 / QCS6490 target，QCS8550-class kit，IQ10 RRD guidance。
2. Tooling：AI Hub organization quota、Device Cloud access、QNN / QAIRT workflow support、Profiler guidance、Qualcomm Linux / BSP review。
3. Engineering office hours：每周 review 2-3 个 reference skills，重点是 fixed-shape models、quantization、unsupported ops、NPU fallback、QNN / ONNX Runtime artifacts。
4. Public output：3 个 Dragonwing Robotics Hub workflows：
   - LeRobot episode -> cloud train -> AI Hub profile -> QNN artifact -> Dragonwing deploy；
   - vision grasping；
   - AMR / inspection。
5. Ecosystem support：引荐 module vendors、education partners、system integrators、Robotics Hub / Project Hub reviewers。
6. Claim language：比赛阶段使用 `Dragonwing-profiled` 或 `Qualcomm-edge-ready candidate`，不称 official Qualcomm certification。

## Demo Plan

7 分钟演示：

1. Create project：选择 tabletop manipulator、QCS / QCS8550 / IQ target、camera、actuator、runtime、task template。
2. Register device：显示 health、runtime、camera/actuator profile、installed model/skill。
3. Import data：显示 LeRobot-compatible dataset、hashes、failure clips、region/privacy。
4. Submit TrainRouter job：选择 China / Overseas lane、GPU provider、budget guard、eval gate。
5. Show eval：fixed split、success rate、failure tags、replay clips、release verdict。
6. Export Qualcomm package：AI Hub / QNN / QAIRT / ONNX Runtime QNN status、profile metrics、rollback package。
7. SkillCertKit：不兼容 profile 被阻止；兼容 Qualcomm target 被允许。
8. SkillDock：生成 skill card，展示 lineage、edge profile、SBOM/signature、safety boundary、pricing/support。
9. EdgeFleet：staged rollout、live status/logs、failure event、rollback to previous-known-good。
10. Submission Builder：导出 evidence table、screenshots、links、BOM、代码步骤和三分钟答辩 storyboard。

## Claim Boundaries

可以声称：

- Qualcomm-first workbench concept。
- LeRobot-compatible workflow。
- AI Hub-ready / QNN-ready evidence path。
- ROS 2 adapter / workflow layer。
- skill packaging and release evidence concept。
- pilot/developer workbench。
- integrates with MCAP/Foxglove-style data workflows。

不能声称：

- official Qualcomm product。
- Qualcomm certification / endorsement。
- replaces ROS / LeRobot / Isaac / Viam / Foxglove / Formant。
- production-ready fleet platform。
- all models compile to QNN without changes。
- measured hardware metrics unless generated from real device or Device Cloud。

## Sources

- Qualcomm Dragonwing Robotics Hub：https://www.qualcomm.com/developer/blog/2026/03/what-qualcomm-dragonwing-robotics-hub-means-for-developers
- Qualcomm AI Hub Workbench：https://workbench.aihub.qualcomm.com/docs/
- AI Hub compile examples：https://workbench.aihub.qualcomm.com/docs/hub/compile_examples.html
- ONNX Runtime QNN：https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3
- NVIDIA Isaac ROS：https://developer.nvidia.com/isaac/ros
- Intrinsic Flowstate：https://www.intrinsic.ai/flowstate
- Viam：https://docs.viam.com/what-is-viam/
- Foxglove Data Management：https://foxglove.dev/product/data-management
- Formant Fleet Management：https://docs.formant.io/docs/getting-started-fleet-management
- ROS：https://www.ros.org/
- IFR 2025 industrial robots：https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
