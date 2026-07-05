# Source

Application source code lives here.

Current prototype modules:

- `robot_platform/models.py`: provider-neutral dataclasses for robot profiles, datasets, training jobs, models, deployment packages, and skills.
- `robot_platform/demo_state.py`: simulated state used to align the website prototype with future APIs.
- `robot_platform/cloud_adapters/`: cloud training adapter interface and mock adapter.

Example:

```bash
PYTHONPATH=src python3 -m robot_platform export-state --cloud china
PYTHONPATH=src python3 -m robot_platform submit-mock-job --cloud global
```
