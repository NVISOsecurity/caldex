class Technique:
    def __init__(self, raw_technique: dict):
        if "attack_id" in raw_technique:
            self.identifier = raw_technique["attack_id"]
        if "name" in raw_technique:
            self.name = raw_technique["name"]
        if "tactic" in raw_technique:
            self.tactic = raw_technique["tactic"]
