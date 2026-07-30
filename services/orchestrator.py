from packages.core import AutonomousReasoningEngine
from packages.utils import logging

class Orchestrator:
    def __init__(self, engine: AutonomousReasoningEngine):
        self.engine = engine
        self.logger = logging.Logger(__name__)

    def run(self) -> None:
        try:
            self.engine.execute()
            self.logger.info('Engine execution completed successfully')
        except Exception as e:
            self.logger.error(f'Error executing engine: {e}')