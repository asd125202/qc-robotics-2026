from ..models import TrainingJobSpec
from .base import CloudTrainingAdapter


class MockCloudAdapter(CloudTrainingAdapter):
    def __init__(self, cloud: str) -> None:
        self.cloud = cloud

    def submit_training_job(self, job: TrainingJobSpec) -> dict:
        provider_prefix = "cn" if self.cloud == "china" else "global"
        return {
            "job_name": job.job_name,
            "provider": job.provider,
            "status": "submitted",
            "dashboard_url": f"mock://{provider_prefix}/{job.job_name}",
            "max_gpu_hours": job.max_gpu_hours,
            "preferred_gpu": job.preferred_gpu,
        }
