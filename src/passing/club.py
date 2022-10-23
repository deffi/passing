from dataclasses import dataclass


@dataclass(frozen=True)
class Club:
    id_: str
    label: str
    color: str


no_club = Club("", "", "")
