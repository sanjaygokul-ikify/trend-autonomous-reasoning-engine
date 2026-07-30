import argparse
from packages.core import RealTimeAutonomousReasoningEngine
from packages.services import orchestrator

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    args = parser.parse_args()
    input_data = InputData([{'key': 'value'}])
    engine = RealTimeAutonomousReasoningEngine(input_data)
    orchestrator = orchestrator.Orchestrator(engine)
    orchestrator.run()