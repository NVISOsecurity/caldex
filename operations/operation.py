from .action import Action
from .adversary import Adversary


class Operation:
    def __init__(self, raw_result: dict):
        if "adversary" in raw_result:
            self.adversary: Adversary = Adversary(raw_result["adversary"])
        if "chain" in raw_result:
            raw_actions = raw_result["chain"]
            self.chain = []
            for raw_action in raw_actions:
                self.chain.append(Action(raw_action))
