from typing import List

from .domain import Domain
from .gradient import Gradient
from .technique import Technique
from .version import Version


class Layer:
    def __init__(self, name: str, description: str):
        self.name: str = name
        self.version: Version = Version.v2_1
        self.domain: Domain = Domain.Enterprise
        self.description: str = description
        self.techniques: List[Technique] = []
        self.gradient: Gradient = Gradient(100)

    def export(self):
        export = {
            "name": self.name,
            "version": self.version.value,
            "domain": self.domain.value,
            "techniques": [technique.export() for technique in self.techniques],
            "gradient": self.gradient.export()
        }
        if self.description and len(self.description) > 0:
            export["description"] = self.description
        return export
