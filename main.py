# Python Cee-Lo game by Ryan Sessions
from game_mechanics import game_round_pvp, score_reset
from player_ai import Player


def main_game():
    print('--------Cee-Lo, by Ryan Sessions--------')
    # Set up game (mode, players, etc.)
    # Get player count, make sure it's from 2 to 4
    while True:
        player_count = input("Enter the amount of total players (2-4): ")
        player_dict = dict()
        if player_count == '':
            print('TEST MODE!!')
            player_count = 4
            for i, foo in enumerate(['Wendy', 'Ryan', 'Crystal', 'Brian']):
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

    # main game round loop
    while True:
        round_winner = game_round_pvp(player_dict)
        print(f"{player_dict[round_winner].name} wins the round with {player_dict[round_winner].result_lf}!")
        input("Press any key to begin next round.")
        # Do money math
        # print('math')


if __name__ == '__main__':
    main_game()
