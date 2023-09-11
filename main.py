# Python Cee-Lo game by Ryan Sessions
from dice_rules import compare_results_pvp, get_roll, get_result
from player_ai import Player


def main_game():
    print('--------Cee-Lo, by Ryan Sessions--------')
    # Get player count, make sure it's from 2 to 4
    while True:
        player_count = input("Enter the amount of total players (2-4):\n")
        if player_count.isdigit() and (2 <= int(player_count) <= 4):
            break
        print("Please enter an integer from 2 to 4.")
    player_count = int(player_count)
    # player_count = 2  # Setting default player_count for easier prototyping
    print(f"Total player count: {player_count}")

    # Create a dictionary containing all players and collect their names
    player_dict = dict()
    for i in range(player_count):
        name = input(f"Input name for player {i + 1}:\n")
        player_dict['player_' + str(i + 1)] = Player(name=name)

    # TODO: Work out rolls, roll order, matchups, etc
    print("--------------------------------------")
    # Iterate through all players who don't have a roll result until they all do
    while not all(player_dict[player].return_result() for player in player_dict):
        for player in player_dict:
            if not player_dict[player].return_result():
                roll_list = get_roll()
                print(f"{player_dict[player].name} rolled: {roll_list}")
                result = get_result(roll_list)
                if result:  # If they roll something, add the roll result to player object
                    player_dict[player].update_result(result)
                    print(f"{player_dict[player].name}'s result: {result}")
                else:  # Notify the players about the re-roll
                    print(f"{player_dict[player].name} will need to re-roll.")
            else:
                print(f"{player_dict[player].name}'s result: {player_dict[player].return_result()}")
        print("--------------------------------------")
    for player in player_dict:
        print(f"{player_dict[player].name}'s result: {player_dict[player].return_result()}")

    compare_results_pvp(player_dict)


if __name__ == '__main__':
    main_game()
