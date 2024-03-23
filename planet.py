from human import Human


class Planet:

    def __init__(self, name: str = ''):
        self.__humans = []
        self.__name = name

    def __repr__(self):
        return f'planet(name={self.__name}, humans={self.__humans})'

    def __str__(self):
        return f'Planet {self.__name} has {len(self.__humans)} humans.'

    def add(self, human: Human) -> bool:
        self.__humans.append(human)
        return (human in self.__humans)

    def has(self, human: Human) -> bool:
        return (human in self.__humans)

    def population(self) -> int:
        return len(self.__humans)

    def remove(self, human: Human) -> bool:
        self.__humans.remove(human)
        return (human not in self.__humans)
        
    # Assuming LivingThing is defined with necessary attributes and methods

    class Planet:
        def __init__(self, name: str = ''):
            self.__living_things = []
            self.__name = name

        def add_living_thing(self, living_thing):
            self.__living_things.append(living_thing)

        def remove_living_thing(self, living_thing):
            if living_thing in self.__living_things:
                self.__living_things.remove(living_thing)
                return True
            return False

        def has_living_thing(self, living_thing):
            return living_thing in self.__living_things
