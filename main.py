# Python Cee-Lo game by Ryan Sessions
from game_mechanics import compare_results_pvp, get_roll, get_result
from player_ai import Player


def main_game():
    print('--------Cee-Lo, by Ryan Sessions--------')
    # Get player count, make sure it's from 2 to 4
    while True:
        player_count = input("Enter the amount of total players (2-4): ")
        player_dict = dict()
        if player_count == '':
            print('TEST MODE!!')
            player_count = 4
            for i, foo in enumerate(['Wendy', 'Ryan', 'Crystal', 'Micah']):
                player_dict['player' + str(i + 1)] = Player(name=foo)
            break
        elif player_count.isdigit() and (2 <= int(player_count) <= 4):
            player_count = int(player_count)
            # player_count = 2  # Setting default player_count for easier prototyping
            print(f"Total player count: {player_count}")

            # Create a dictionary containing all players and collect their names
            for i in range(player_count):
                name = input(f"Input name for player {i + 1}: ")
                player_dict['player_' + str(i + 1)] = Player(name=name)
            break
        print("Please enter an integer from 2 to 4.")

    # main game loop
    print("--------------------------------------")
    # Iterate through all players who don't have a roll result until they all do
    while not all(player_dict[player].result for player in player_dict):
        for player in player_dict:
            if not player_dict[player].result:
                roll_list = get_roll()
                print(f"{player_dict[player].name} rolled: {roll_list}")
                result = get_result(roll_list)
                if result:  # If they roll something, add the roll result to player object
                    player_dict[player].result, player_dict[player].result_lf = result[0], result[1]
                    print(f"{player_dict[player].name}'s result: {result[1]}")
                else:  # Notify the players about the re-roll
                    print(f"{player_dict[player].name} will need to re-roll.")
            else:
                print(f"{player_dict[player].name}'s result: {player_dict[player].result_lf}")
        print("--------------------------------------")
    # Return results
    for player in player_dict:
        print(f"{player_dict[player].name}'s result: {player_dict[player].result_lf}")

    compare_results_pvp(player_dict)
    # Do money math


if __name__ == '__main__':
    main_game()
