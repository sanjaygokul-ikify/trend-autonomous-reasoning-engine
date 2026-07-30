class AutonomousReasoningEngineError(Exception):
    pass

class PreprocessingError(AutonomousReasoningEngineError):
    pass

class IngestionError(AutonomousReasoningEngineError):
    pass

class QueryError(AutonomousReasoningEngineError):
    pass

class InferenceError(AutonomousReasoningEngineError):
    pass

class PostprocessingError(AutonomousReasoningEngineError):
    pass
