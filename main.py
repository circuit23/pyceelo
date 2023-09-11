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
        print("Re-roll.")
        return None


class Player:
    def __init__(self, name="Player", money=100, current_points=0):
        self.name = name
        self.money = money
        self.current_points = current_points

    def return_current_points(self):
        print(self.current_points)


def main_game():
    print('-----Cee-Lo, by Ryan Sessions-----')
    # input("Press any key to play.")
    print("baby's 1st roll")
    result = None
    while not result:
        roll_list = get_roll()
        print(f'roll list : {roll_list}')
        result = get_result(roll_list)
    print(f'result - {result}')


if __name__ == '__main__':
    main_game()
