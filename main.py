# This is a Python Cee-Lo game
# by Ryan Sessions
from random import randint


def get_roll(amount=3):
    return [randint(1, 6) for _ in range(amount)]


def get_result(roll_list):
    roll_list.sort()
    roll_1, roll_2, roll_3 = roll_list

    if (roll_1, roll_2, roll_3) == (4, 5, 6):
        return "WIN: 4-5-6 straight kill"
    elif all(item == roll_list[0] for item in roll_list):
        return f"TRIPS: {roll_1}"
    elif (roll_1, roll_2, roll_3) == (1, 2, 3):
        return "LOSE: 1-2-3 straight lose"
    elif roll_1 == roll_2:
        return f"POINT: {roll_3}"
    elif roll_2 == roll_3:
        return f"POINT: {roll_1}"
    else:
        # print("Re-roll.")
        return None


class Player:
    def __init__(self, name="Player", money=100, points=0):
        self.name = name
        self._money = money
        self._points = points

    def return_points(self):
        return self._points

    def increment_points(self, amount):
        self._points += amount

    def reset_points(self):
        self._points = 0

    def return_money(self):
        return self._money

    def increment_money(self, amount: int):
        self._money += amount


def main_game():
    print('-----Cee-Lo, by Ryan Sessions-----')
    # Get player count, make sure it's from 2 to 4
    while True:
        player_count = input("Enter the amount of total players (2-4):\n")
        if player_count.isdigit() and (2 <= int(player_count) <= 4):
            break
        print("Please enter an integer from 2 to 4.")
    # player_count = 2  # Setting default player_count for easier prototyping
    player_count = int(player_count)
    print(f"Total player count: {player_count}")

    # Create a dictionary containing all players and collect their names
    players = dict()
    for i in range(player_count):
        name = input(f"Input name for player {i + 1}:\n")
        players['player_' + str(i + 1)] = Player(name=name)

    # TODO: Start working out rolls, roll order, matchups, etc
    print("baby's 1st roll")
    result = None
    while not result:
        roll_list = get_roll()
        print(f'Baby rolled: {roll_list}')
        result = get_result(roll_list)
    print(f'result - {result}')


if __name__ == '__main__':
    main_game()
