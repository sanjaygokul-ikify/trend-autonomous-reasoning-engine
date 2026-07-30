import unittest
from packages.core import RealTimeAutonomousReasoningEngine
from packages.services import orchestrator

class TestPipeline(unittest.TestCase):
    def test_orchestrator(self) -> None:
        input_data = InputData([{'key': 'value'}])
        engine = RealTimeAutonomousReasoningEngine(input_data)
        orchestrator = orchestrator.Orchestrator(engine)
        orchestrator.run()
        self.assertTrue(input_data.preprocessed)
        self.assertTrue(input_data.ingested)
        self.assertTrue(input_data.inferred)
        self.assertTrue(input_data.postprocessed)