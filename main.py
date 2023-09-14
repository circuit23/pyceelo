#!/usr/bin/env python3

# Python Cee-Lo game by Ryan Sessions
from game_mechanics import game_round_pvp, get_wagers
from player_ai import Player


def main_game():
    print('--------Cee-Lo, by Ryan Sessions--------')
    # Set up game (mode, players, etc.)
    while True:
        # Get player count, make sure it's from 2 to 4
        player_count = input("Enter the amount of total players (2-4): ")
        player_list = dict()
        if player_count == '':
            print('TEST MODE!!')
            for i, foo in enumerate(['Wendy', 'Ryan', 'Crystal', 'Brian']):
                player_list['player' + str(i + 1)] = Player(name=foo)
            break
        elif player_count.isdigit() and (2 <= int(player_count) <= 4):
            player_count = int(player_count)
            print(f"Total player count: {player_count}")

            # Create a dictionary containing all players and collect their names
            for i in range(player_count):
                name = input(f"Input name for player {i + 1}: ")
                player_list['player_' + str(i + 1)] = Player(name=name)
            break
        print("Please enter an integer from 2 to 4.")

    round_index = 0
    # main game round loop
    while True:
        round_index += 1
        print(f"--*Round {round_index}*--")
        for player in player_list:
            print(f"{player_list[player].name}: {player_list[player].return_money()}")
        # Only allow players with more than 0 monies to play
        active_players = {k: v for k, v in player_list.items() if v.return_money() > 0}
        if len(active_players) == 1:  # Found a winner, so announce that and exit the game
            game_winner = active_players.popitem()
            print(f"{game_winner[1].name} won the game by taking everyone else's monies!")
            input("Press any key to end the game.")
            exit(0)
        # Get the wager, subtract from everyone's totals
        wager, total_pot = get_wagers(active_players)
        print(f"Each player bets {wager}, for a total of {total_pot}.")
        round_winner = game_round_pvp(active_players)
        if round_winner:
            print(f"{player_list[round_winner].name} nets {total_pot - wager} monies with "
                  f"{player_list[round_winner].result_lf}!")
            player_list[round_winner].increment_money(total_pot)
        else:
            print("There was no winner this round... you are all losers!")
        input("Press any key to begin next round.")


if __name__ == '__main__':
    main_game()
