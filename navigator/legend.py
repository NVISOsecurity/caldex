class Legend:
    def __init__(self, label: str, color: str):
        self.label: str = label
        self.color: str = color

    def export(self):
        return {
            "label": self.label,
            "color": self.color
        }
