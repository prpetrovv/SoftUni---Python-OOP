from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @staticmethod
    @abstractmethod
    def get_team_data():
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        expenses_per_race, sponsors = self.get_team_data()
        revenue = 0
        for positions in sponsors.values():
            for position, reward in positions.items():
                if race_pos <= position:
                    revenue += reward
                    break
        revenue -= expenses_per_race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
