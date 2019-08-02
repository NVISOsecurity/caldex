from typing import List


class Gradient:
    def __init__(self, upper: int):
        self.colors: List[str] = ["#00FF00", "#FF0000"]
        self.minValue: int = 0
        self.maxValue: int = upper

    def export(self):
        return {
            "colors": self.colors,
            "minValue": self.minValue,
            "maxValue": self.maxValue
        }
