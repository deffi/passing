from dataclasses import dataclass
from typing import Optional, Mapping, List

from passing import Juggler, Throw, Club


class ColorPassingJuggler(Juggler):
    def __init__(self, name: str, straight_color: str, cross_color: str, left_clubs: List[Club], right_clubs: List[Club]):
        super().__init__(name)
        self.straight_color = straight_color
        self.cross_color = cross_color
        self._partner: Optional[Juggler] = None
        self.left.clubs = left_clubs
        self.right.clubs = right_clubs

        self._t = 0


    @property
    def partner(self) -> Optional[Juggler]:
        return self._partner

    @partner.setter
    def partner(self, partner: Juggler):
        self._partner = partner

        self._straight_target = {id(self.left): self.partner.right, id(self.right): self.partner.left}
        self._cross_target = {id(self.left): self.partner.left, id(self.right): self.partner.right}
        self._self_target = {id(self.left): self.right, id(self.right): self.left}

        self._color_target = {
            self.straight_color: self._straight_target,
            self.cross_color: self._cross_target,
        }

    def start(self) -> Throw:
        assert len(self.left.clubs) == 1
        assert len(self.right.clubs) == 2

        self._t = 0
        club = self.right.clubs.pop()
        return Throw(club, self._color_target[club.color][id(self.right)], 1)

    def catch(self, throw: Throw) -> Throw:
        assert throw.target in [self.left, self.right]
        assert len(throw.target.clubs) == 1

        self._t = self._t + 1
        club = throw.target.clubs.pop()
        throw.target.clubs.append(throw.club)

        if self._t % 4 == 0:
            target = self._color_target[club.color][id(throw.target)]
        else:
            target = self._self_target[id(throw.target)]

        return Throw(club, target, 1)




def main():
    a1 = Club("a1", "A", "red")
    a2 = Club("a2", "A", "red")
    a3 = Club("a3", "A", "red")
    b1 = Club("b1", "B", "green")
    b2 = Club("b2", "B", "green")
    b3 = Club("b3", "B", "green")

    alice = ColorPassingJuggler("Alice", "red", "green", [a2], [a3, a1])
    bob = ColorPassingJuggler("Bob", "red", "green", [b2], [b3, b1])
    alice.partner = bob
    bob.partner = alice
    jugglers = [alice, bob]

    throws = []
    print(alice, "-", bob, " / ", ", ".join(str(throw) for throw in throws))
    throws = [juggler.start() for juggler in jugglers]

    for i in range (60):
        print(i, alice, "-", bob, " / ", ", ".join(str(throw) for throw in throws))
        throws = [throw.target.juggler.catch(throw) for throw in throws]





if __name__ == "__main__":
    main()
