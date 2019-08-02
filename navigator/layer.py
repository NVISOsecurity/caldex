from typing import List

from .domain import Domain
from .gradient import Gradient
from .technique import Technique
from .version import Version
from .legend import Legend


class Layer:
    def __init__(self, name: str, description: str):
        self.name: str = name
        self.version: Version = Version.v2_1
        self.domain: Domain = Domain.Enterprise
        self.description: str = description
        self.techniques: List[Technique] = []
        self.gradient: Gradient = Gradient(100)
        self.legendItems: List[Legend] = [Legend("Successfully mitigated", "#00FF00"), Legend("Failed to mitigate", "#FF0000")]

    def export(self):
        export = {
            "name": self.name,
            "version": self.version.value,
            "domain": self.domain.value,
            "techniques": [technique.export() for technique in self.techniques],
            "gradient": self.gradient.export(),
            "legendItems": [legend.export() for legend in self.legendItems]
        }
        if self.description and len(self.description) > 0:
            export["description"] = self.description
        return export
