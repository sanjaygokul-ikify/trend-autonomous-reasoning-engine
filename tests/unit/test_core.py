import unittest
from packages.core import InputData, RealTimeAutonomousReasoningEngine

class TestCore(unittest.TestCase):
    def test_input_data(self) -> None:
        input_data = InputData([{'key': 'value'}])
        self.assertFalse(input_data.preprocessed)
        self.assertFalse(input_data.ingested)

    def test_engine(self) -> None:
        input_data = InputData([{'key': 'value'}])
        engine = RealTimeAutonomousReasoningEngine(input_data)
        engine.execute()
        self.assertTrue(input_data.preprocessed)
        self.assertTrue(input_data.ingested)