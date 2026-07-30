import unittest
from packages.core import AutonomousReasoningEngine

class TestRuntime(unittest.TestCase):
    def test_engine_execution(self) -> None:
        input_data = InputData([{'key': 'value'}])
        engine = RealTimeAutonomousReasoningEngine(input_data)
        output, error = engine.execute()
        self.assertIsNotNone(output)
        self.assertIsNone(error)