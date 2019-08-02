class Technique:
    def __init__(self, identifier: str, tactic: str):
        self.techniqueID: str = identifier
        self.tactic: str = tactic
        self.score: int = 0

    def export(self):
        return {
            "techniqueID": self.techniqueID,
            "tactic": self.tactic,
            "score": self.score
        }
