class Player:
    def __init__(self, name="Player", money=100, result=None):
        self.name = name
        self._money = money
        self._result = result

    def return_result(self):
        return self._result

    def update_result(self, result):
        self._result = result

    def return_money(self):
        return self._money

    def increment_money(self, amount: int):
        self._money += amount
