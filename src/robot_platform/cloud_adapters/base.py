from abc import ABC, abstractmethod
from typing import Protocol

from ..models import TrainingJobSpec


class TrainingJobResult(Protocol):
    job_name: str
    provider: str
    status: str
    dashboard_url: str


class CloudTrainingAdapter(ABC):
    @abstractmethod
    def submit_training_job(self, job: TrainingJobSpec) -> dict:
        """Submit a training job and return a provider-neutral result."""
