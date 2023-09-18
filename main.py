#!/usr/bin/env python3

# Python Cee-Lo game by Ryan Sessions
from game_mechanics import (
    game_round_pvp,
    get_game_mode,
    game_round_bank,
    determine_play_order,
)
from player_ai import Player


def main_game():
    print("--------Cee-Lo, by Ryan Sessions--------")
    # Set up game (mode, players, etc.)
    while True:
        # Get player count, make sure it's from 2 to 4
        player_count = input("Enter the amount of total players (2-4): ")
        player_list = dict()
        if player_count == "":
            print("TEST MODE!!")
            for i, foo in enumerate(["Wendy", "Ryan", "Crystal", "Brian"]):
                player_list["player" + str(i + 1)] = Player(name=foo)
            break
        elif player_count.isdigit() and (2 <= int(player_count) <= 4):
            player_count = int(player_count)
            print(f"Total player count: {player_count}")

            # Create a dictionary containing all players and collect their names
            for i in range(player_count):
                name = input(f"Input name for player {i + 1}: ")
                player_list["player" + str(i + 1)] = Player(name=name)
            break
        print("Please enter an integer from 2 to 4.")

    game_mode = get_game_mode()
    round_index = 0
    # main game round loop
    while True:
        # Only allow players with more than 0 monies to play
        active_players = {k: v for k, v in player_list.items() if v.return_money() > 0}
        if (
            len(active_players) == 1
        ):  # Found a winner, so announce that and exit the game
            game_winner = active_players.popitem()
            print(
                f"{game_winner[1].name} won the game by taking everyone else's monies!"
            )
            input("Press any key to end the game.")
            exit(0)
        # Begin round
        round_index += 1
        print(f"--*Round {round_index}*--")
        print(f"Game mode: {'Bank' if game_mode == 'BANK' else 'PvP/Winner take all'}")
        for player in player_list:
            print(f"{player_list[player].name}: {player_list[player].return_money()}")

        # Pass to the appropriate game handler depending on game_mode
        if game_mode == "PvP":
            if round_index == 1:
                play_order = determine_play_order(player_list, game_mode="PvP")
                input("Randomly determining order of play. Press Enter to continue.")
            result = game_round_pvp(active_players, play_order=play_order)
            print(result)
        elif game_mode == "BANK":
            # TODO: implement bank round loop
            play_order = determine_play_order(player_list, game_mode="BANK")
            result = game_round_bank(active_players)
            print(result)
        input("Press any key to begin next round.")


if __name__ == "__main__":
    main_game()
