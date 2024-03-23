class Animal:
    MAX_ENERGY = 100
    MIN_ENERGY = 0
    REPRODUCE_ENERGY = 1
    MOVE_ENERGY = 10

    def __init__(self, name: str, age: int = 0, energy: int = MAX_ENERGY) -> None:
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self) -> str:
        return f'animal(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and has an energy of {self.energy}.'

    def eat(self, amount) -> int:
        potential_energy = self.energy + amount

        if potential_energy >= Animal.MAX_ENERGY:
            self.energy = Animal.MAX_ENERGY
            return potential_energy - Animal.MAX_ENERGY
        else:
            self.energy = potential_energy
            return 0

    def grow(self) -> None:
        self.age += 1

    def move(self, distance: int) -> bool:
        potential_energy = self.energy - distance

        if potential_energy >= Animal.MOVE_ENERGY:
            self.energy = potential_energy
            return True
        else:
            return False

    def reproduce(self) -> bool:
        if self.energy >= Animal.REPRODUCE_ENERGY + Animal.MIN_ENERGY:
            self.energy -= Animal.REPRODUCE_ENERGY
            return True
        else:
            return False
