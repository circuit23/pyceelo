class Player:
    def __init__(self, name="Player", money=100, result=None, result_lf=None):
        self.name = name
        self._money = money
        self.result = result
        self.result_lf = result_lf

    def return_money(self):
        return self._money

    def increment_money(self, amount: int):
        self._money += amount
