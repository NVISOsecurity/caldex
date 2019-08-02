from .ability import Ability


class Adversary:
    def __init__(self, raw_adversary: dict):
        if "name" in raw_adversary:
            self.name = raw_adversary["name"]
        if "description" in raw_adversary:
            self.description = raw_adversary["description"]
        if "phases" in raw_adversary:
            raw_phases = raw_adversary["phases"]
            self.phases: dict = {}
            for i, raw_phase in raw_phases.items():
                self.phases[i] = []
                for raw_ability in raw_phase:
                    self.phases[i].append(Ability(raw_ability))
