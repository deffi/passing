from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Optional
from passing import Club

if TYPE_CHECKING:
    from passing import Throw


@dataclass()
class Hand:
    juggler: "Juggler"
    name: str
    clubs: List[Club] = field(default_factory=list)

    def __str__(self):
        clubs_text = ", ".join(f"{club.id_}" for club in self.clubs)
        return f"{self.name} [{clubs_text}]"


class Juggler:
    name: str

    def __init__(self, name):
        self.name = name
        self.left = Hand(self, "left")
        self.right = Hand(self, "right")

    def __str__(self) -> str:
        return f"{self.name}: {self.left}, {self.right}"

    def start(self) -> "Throw":
        raise NotImplementedError

    def catch(self, throw: "Throw") -> "Throw":
        raise NotImplementedError
