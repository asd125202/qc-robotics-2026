from .models import (
    DatasetManifest,
    DemoState,
    DeploymentPackage,
    ModelArtifact,
    RobotProfile,
    SkillPackage,
    TrainingJobSpec,
)


def build_demo_state(cloud: str = "china") -> DemoState:
    if cloud not in {"china", "global"}:
        raise ValueError("cloud must be 'china' or 'global'")

    provider = "aliyun-pai-or-autodl" if cloud == "china" else "runpod-or-lambda"

    robot = RobotProfile(
        robot_id="robotmac-tabletop-arm-01",
        form_factor="tabletop_arm",
        edge_target="qcs8550",
        runtime_profile="act_policy_local_control",
        sensors=["rgb_camera", "wrist_camera", "joint_state"],
        actuators=["six_axis_arm", "parallel_gripper"],
    )

    dataset = DatasetManifest(
        dataset_id="tabletop-pick-v1",
        format="lerobot-compatible",
        episodes=128,
        failure_clips=42,
        storage_uri="lerobot://robotmac/tabletop-pick-v1",
    )

    training_job = TrainingJobSpec(
        job_name="act-grasp-v3",
        provider=provider,
        policy="act",
        dataset_uri=dataset.storage_uri,
        robot_profile=robot.robot_id,
        max_gpu_hours=8,
        preferred_gpu="a100_80g",
    )

    model = ModelArtifact(
        model_id="act-grasp-v2",
        policy="act",
        success_rate=0.86,
        latency_ms=34,
        artifact_uri="artifact://robotmac/act-grasp-v2.qedge",
    )

    deployment = DeploymentPackage(
        package_id="act-grasp-v2-qcs8550",
        model_id=model.model_id,
        target="qcs8550",
        rollback_package_id="act-grasp-v1-qcs8550",
        safety_profile="local_control_with_estop",
    )

    skill = SkillPackage(
        skill_id="desktop-pick-place",
        display_name="桌面抓取",
        model_id=model.model_id,
        compatible_targets=["qcs8550", "qcs6490"],
        status="verified",
    )

    return DemoState(
        cloud=cloud,
        robot=robot,
        dataset=dataset,
        training_job=training_job,
        model=model,
        deployment=deployment,
        skill=skill,
    )
