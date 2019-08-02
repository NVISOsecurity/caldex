from .technique import Technique


class Ability:
    def __init__(self, raw_ability: dict):
        if "id" in raw_ability:
            self.identifier = raw_ability["id"]
        if "ability_id" in raw_ability:
            self.uuid = raw_ability["ability_id"]
        if "technique" in raw_ability:
            self.technique = Technique(raw_ability["technique"])
        if "platform" in raw_ability:
            self.platform = raw_ability["platform"]
