from dataclasses import dataclass

from passing import Hand, Club


@dataclass()
class Throw:
    club: Club
    target: Hand
    time: int

    def __str__(self):
        return f"{self.club.id_} -> {self.target.juggler.name}.{self.target.name}"
