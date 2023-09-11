# This is a Python Cee-Lo game
# by Ryan Sessions
from random import randint


def get_rolls(amount=3):
    roll_list = []
    for _ in range(amount):
        roll_list.append(randint(1, 6))
    return roll_list


def get_result(roll_list):
    if sorted(roll_list) == [4, 5, 6] or roll_list[0] == roll_list[1] == roll_list[2]:
        return "WIN"
    elif sorted(roll_list) == [1, 2, 3]:
        return "LOSE"
    elif roll_list[0] == roll_list[1]:
        return roll_list[2]
    elif roll_list[0] == roll_list[2]:
        return roll_list[1]
    elif roll_list[1] == roll_list[2]:
        return roll_list[0]
    else:
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
    input("Press any key to play.")
    print("baby's 1st roll")
    result = None
    while not result:
        roll_list = get_rolls()
        print(f'roll list : {roll_list}')
        result = get_result(roll_list)
    print(f'result : {result}')


if __name__ == '__main__':
    main_game()
