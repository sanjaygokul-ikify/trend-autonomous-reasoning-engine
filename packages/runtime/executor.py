from typing import Tuple
from packages.core.engine import RealTimeAutonomousReasoningEngine
from packages.core.types import InputData, OutputData
from packages.core.exceptions import AutonomousReasoningEngineError


class AutonomousReasoningEngineExecutor:
    def __init__(self, input_data: InputData):
        self.engine = RealTimeAutonomousReasoningEngine(input_data)

    def execute(self) -> Tuple[OutputData, None]:
        return self.engine.execute()
