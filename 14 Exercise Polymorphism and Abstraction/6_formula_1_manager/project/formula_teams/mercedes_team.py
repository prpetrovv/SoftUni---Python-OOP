from abc import abstractmethod

from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    @staticmethod
    def get_team_data():
        expenses_per_race = 200000
        sponsors = {"Oracle": {1: 1000000, 3: 500000},
                    "Honda": {5: 100000, 7: 50000}}
        return expenses_per_race, sponsors
