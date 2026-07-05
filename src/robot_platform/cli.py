import argparse
import json

from .demo_state import build_demo_state
from .cloud_adapters.mock import MockCloudAdapter


def main() -> int:
    parser = argparse.ArgumentParser(description="Robot platform prototype utilities")
    subparsers = parser.add_subparsers(dest="command", required=True)

    export_state = subparsers.add_parser("export-state", help="Print the simulated dashboard state as JSON")
    export_state.add_argument("--cloud", choices=["china", "global"], default="china")

    submit_job = subparsers.add_parser("submit-mock-job", help="Create a mock cloud training job")
    submit_job.add_argument("--cloud", choices=["china", "global"], default="china")

    args = parser.parse_args()

    state = build_demo_state(args.cloud)

    if args.command == "export-state":
        print(json.dumps(state.to_dict(), ensure_ascii=False, indent=2))
        return 0

    if args.command == "submit-mock-job":
        adapter = MockCloudAdapter(args.cloud)
        result = adapter.submit_training_job(state.training_job)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    return 1
