from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        return 'woof'


class Cat(Animal):
    def make_sound(self) -> str:
        return 'meow'


class Turtle(Animal):
    def make_sound(self) -> str:
        return 'strange sound'


class Chicken(Animal):
    def make_sound(self) -> str:
        return 'cluck'


class Pig(Animal):
    def make_sound(self) -> str:
        return 'oink'


def animal_sound(animals: List[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Turtle(), Chicken(), Pig()]
animal_sound(animals)
