# 研究笔记：LeRobot 与云端机器人训练

## 当前可依赖的 LeRobot 能力

LeRobot 的官方定位是提供真实世界机器人的模型、数据集和工具，并降低进入机器人学习的门槛。它不是单一模型，而是一套面向真实机器人训练和部署的工作流。

关键能力：

- 统一机器人接口：用硬件无关的 `Robot` 类抽象观测、动作和连接。
- 统一数据集格式：LeRobotDataset 使用视频/图像和 Parquet 存储状态/动作，并支持 Hugging Face Hub。
- 真实机器人教程：覆盖数据记录、可视化、训练策略、评估策略。
- 策略模型：ACT、Diffusion、VQ-BeT、SmolVLA、X-VLA、HIL-SERL 等。
- 数据工具：删除、拆分、合并、添加/移除特征、视频转换。

## 适合比赛 demo 的路线

### 最稳路线：ACT + 桌面机械臂

ACT 是 LeRobot 官方推荐的新手起点之一，原因是训练快、算力要求低、对精细操作表现强。适合作为 7 月 20 日前项目书和 8-11 月最终作品的保底路线。

可演示任务：

- 夹取指定物体并放入指定区域。
- 根据视觉状态选择下一步动作。
- 失败后由人类接管，记录恢复动作，再微调策略。

### 更前沿路线：SmolVLA / X-VLA

SmolVLA 是轻量级机器人基础模型，适合在 LeRobot 数据集上微调。X-VLA 的方向是跨机器人形态适配，用少量参数或 prompt 适配不同硬件。它们适合包装为产品的“未来扩展能力”，但比赛落地应先用 ACT 做闭环。

### 产品化路线：云训练闭环

产品流程：

1. 本体采集：机器人本地记录多摄像头视频、状态、动作、时间戳。
2. 数据同步：转为 LeRobotDataset，上传到中国或海外云端存储。
3. 云端训练：根据任务选择 ACT / SmolVLA / X-VLA 模板，启动 GPU job。
4. 自动评估：回放验证集、生成成功率、动作平滑度、延迟指标。
5. 边缘部署：导出模型包，部署到 Qualcomm 设备运行。
6. 人类纠错：HIL 数据继续进入下一轮训练。

## 为什么要做双版本云

中国团队更需要国内网络、合规、付款和售后：阿里云 PAI、腾讯云 GPU、华为 ModelArts、AutoDL 都可以作为候选。海外开发者更重视快速 GPU 实例、全球区域、API/容器体验和按秒计费：Runpod、Lambda、Modal、Paperspace 更适合。

产品不应把自己绑定死在某一家云。正确做法是定义统一的训练 job spec：

```yaml
dataset: lerobot-dataset-uri
policy: act
robot: qcs8550_arm_v1
gpu_profile: single_a100_40g
eval:
  replay_episodes: 20
  metrics:
    - success_rate
    - action_smoothness
    - latency_budget
export:
  target: qualcomm_edge_runtime
```

然后为不同云供应商做 adapter。

## 信息来源

- LeRobot 文档：https://huggingface.co/docs/lerobot/index
- LeRobot GitHub：https://github.com/huggingface/lerobot
- ACT 文档：https://huggingface.co/docs/lerobot/act
- SmolVLA 文档：https://huggingface.co/docs/lerobot/smolvla
- LeRobotDataset v3：https://huggingface.co/docs/lerobot/lerobot-dataset-v3
- 真实机器人教程：https://huggingface.co/docs/lerobot/main/getting_started_real_world_robot
- HIL 数据采集：https://huggingface.co/docs/lerobot/hil_data_collection
