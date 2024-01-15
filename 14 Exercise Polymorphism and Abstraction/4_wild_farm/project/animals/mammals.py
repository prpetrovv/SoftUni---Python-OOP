from project.animals.animal import Mammal


class Mouse(Mammal):
    FOOD_TO_EAT = ["Vegetable", "Fruit"]
    WEIGHT_INCREMENT = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    FOOD_TO_EAT = ["Meat"]
    WEIGHT_INCREMENT = 0.45

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    FOOD_TO_EAT = ["Meat", "Vegetable"]
    WEIGHT_INCREMENT = 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    FOOD_TO_EAT = ["Meat"]
    WEIGHT_INCREMENT = 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"
