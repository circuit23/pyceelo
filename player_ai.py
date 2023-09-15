class Player:
    def __init__(self, name="Player", money=100, result=None, result_lf=None, banker=False):
        self.name = name
        self._money = money
        self.result = result
        self.result_lf = result_lf
        self.banker = banker
        # TODO: consider moving the 'banker' info to the round itself, getting passed/changed at the end

    def return_money(self):
        return self._money

    def increment_money(self, amount: int):
        self._money += amount
