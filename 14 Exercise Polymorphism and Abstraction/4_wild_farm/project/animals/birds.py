from project.animals.animal import Bird


class Owl(Bird):
    FOOD_TO_EAT = ["Meat"]
    WEIGHT_INCREMENT = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    FOOD_TO_EAT = ["Meat", "Vegetable", "Seed", "Fruit"]
    WEIGHT_INCREMENT = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
