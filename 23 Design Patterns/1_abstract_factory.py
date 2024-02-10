from abc import ABC, abstractmethod


class AbstractFactory(ABC, abstractmethod):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError()

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError()

    @abstractmethod
    def create_table(self):
        raise NotImplementedError()


class Chair:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name


class Sofa:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name


class Table:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair("Victorian Chair")

    def create_sofa(self):
        return Sofa("Victorian Sofa")

    def create_table(self):
        return Table("Victorian Table")


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair("Modern Chair")

    def create_sofa(self):
        return Sofa("Modern Sofa")

    def create_table(self):
        return Table("Modern Table")


class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair("Futuristic Chair")

    def create_sofa(self):
        return Sofa("Futuristic Sofa")

    def create_table(self):
        return Table("Futuristic Table")
