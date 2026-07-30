from typing import List, Dict

class InputData:
    def __init__(self, data: List[Dict[str, str]]):
        self.data = data
        self.preprocessed = False
        self.ingested = False
        self.queries = []
        self.inferred = False
        self.postprocessed = False


class OutputData:
    def __init__(self, result: str):
        self.result = result
