from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class RobotProfile:
    robot_id: str
    form_factor: str
    edge_target: str
    runtime_profile: str
    sensors: list[str]
    actuators: list[str]


@dataclass(frozen=True)
class DatasetManifest:
    dataset_id: str
    format: str
    episodes: int
    failure_clips: int
    storage_uri: str


@dataclass(frozen=True)
class TrainingJobSpec:
    job_name: str
    provider: str
    policy: str
    dataset_uri: str
    robot_profile: str
    max_gpu_hours: int
    preferred_gpu: str


@dataclass(frozen=True)
class ModelArtifact:
    model_id: str
    policy: str
    success_rate: float
    latency_ms: int
    artifact_uri: str


@dataclass(frozen=True)
class DeploymentPackage:
    package_id: str
    model_id: str
    target: str
    rollback_package_id: str
    safety_profile: str


@dataclass(frozen=True)
class SkillPackage:
    skill_id: str
    display_name: str
    model_id: str
    compatible_targets: list[str]
    status: str


@dataclass(frozen=True)
class DemoState:
    cloud: str
    robot: RobotProfile
    dataset: DatasetManifest
    training_job: TrainingJobSpec
    model: ModelArtifact
    deployment: DeploymentPackage
    skill: SkillPackage

    def to_dict(self) -> dict:
        return asdict(self)
