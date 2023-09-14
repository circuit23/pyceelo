from random import randint


def get_roll(amount=3):
    return [randint(1, 6) for _ in range(amount)]


def get_result(roll_list):
    roll_list.sort()
    roll_1, roll_2, roll_3 = roll_list

    if (roll_1, roll_2, roll_3) == (4, 5, 6):
        return "W9", "WIN: 4-5-6 straight kill"
    elif all(roll == roll_list[0] for roll in roll_list):
        return f"T{roll_1}", f"TRIPS: {roll_1}"
    elif roll_1 == roll_2:
        return f"P{roll_3}", f"POINT: {roll_3}"
    elif roll_2 == roll_3:
        return f"P{roll_1}", f"POINT: {roll_1}"
    elif (roll_1, roll_2, roll_3) == (1, 2, 3):
        return "L0", "LOSE: 1-2-3 straight lose"
    else:
        return None


def get_game_mode():
    game_mode = None
    while not game_mode:
        game_mode_choice = input("Should one of the players act as a [b]ank, or is this [w]inner take all (b/w)? ")
        if game_mode_choice == 'b' or game_mode_choice == 'B':
            game_mode = 'BANK'
        elif game_mode_choice == 'w' or game_mode_choice == 'W':
            game_mode = 'PvP'
        print("Please enter either 'b' or 'w'.")

    return game_mode


def get_wagers(player_list):
    wager = None
    while not wager:
        player_wager = input(f"How much monies should each player bet? 1 to "
                             f"{min([player_list[player].return_money() for player in player_list])}: ")
        if (player_wager.isdigit() and
                (1 <= int(player_wager) <= min([player_list[player].return_money() for player in player_list]))):
            wager = int(player_wager)
            break
        else:
            print(f"Please enter an integer from 1 to "
                  f"{min([player_list[player].return_money() for player in player_list])}.")
            wager = None
    total_pot = wager * len(player_list)
    for player in player_list:
        player_list[player].increment_money(-1 * wager)

    return wager, total_pot


def roll_all_players(player_dict):
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


def score_reset(player_dict):
    for player in player_dict:
        player_dict[player].result, player_dict[player].result_lf = None, None


def get_winners(bracket_list):
    sorted_list = sorted(bracket_list, key=lambda item: item[1], reverse=True)
    top_rank = 0
    winners_list = []

    for player in sorted_list:
        player_rank = int(player[1])

        if player_rank > top_rank:
            top_rank = player_rank
            winners_list = [player[0]]  # begin new winners_list with new top rank

        elif player_rank == top_rank:
            winners_list.append(player[0])

        else:
            # No need to evaluate lower ranked players
            break

    return winners_list


def print_winner(player_dict, winner, wager, total_pot, game_mode):
    if game_mode == 'PvP':
        player_dict[winner].increment_money(total_pot)
        return f"{player_dict[winner].name} nets {total_pot - wager} monies with {player_dict[winner].result_lf}!"
    elif game_mode == 'BANK':
        pass
    else:
        pass


def game_round_pvp(player_dict, roll_off=False, wager=0, total_pot=0):
    if not roll_off:
        # Get the wager, subtract from everyone's totals
        wager, total_pot = get_wagers(player_dict)
        print(f"Each player bets {wager}, for a total of {total_pot}.")

    # Reset scores, then roll up all the players' dice
    score_reset(player_dict)
    roll_all_players(player_dict)

    # Separate into brackets and compare results
    wins = [(k, player_dict[k].result[1]) for k in player_dict.keys() if player_dict[k].result[0] == "W"]
    trips = [(k, player_dict[k].result[1]) for k in player_dict.keys() if player_dict[k].result[0] == "T"]
    points = [(k, player_dict[k].result[1]) for k in player_dict.keys() if player_dict[k].result[0] == "P"]
    losers = [(k, player_dict[k].result[1]) for k in player_dict.keys() if player_dict[k].result[0] == "L"]

    if losers and len(losers) == len(player_dict):
        return "There was no winner this round... you are all losers!"

    for bracket_list in [wins, trips, points]:
        # Continue to the next iteration if the list is empty.
        if not bracket_list:
            continue

        # If there is only one element in the list, return the first element of the contained tuple.
        if len(bracket_list) == 1:
            round_winner = bracket_list[0][0]
            return print_winner(player_dict=player_dict, winner=round_winner, wager=wager, total_pot=total_pot,
                                game_mode='PvP')

        # In case there are multiple elements in the list.
        bracket_winners = get_winners(bracket_list)

        # If there's only one winner, return it.
        if len(bracket_winners) == 1:
            round_winner = bracket_list[0][0]
            return print_winner(player_dict=player_dict, winner=round_winner, wager=wager, total_pot=total_pot,
                                game_mode='PvP')

        # Handle multiple winners.
        print("Roll-off!")
        for winner in bracket_winners:
            print(f"{player_dict[winner].name} ({player_dict[winner].result_lf})")
            if not winner == bracket_winners[-1]:
                print('tied with')

        roll_off_dict = {player: player_dict[player] for player in bracket_winners}
        roll_off_winner = game_round_pvp(roll_off_dict, roll_off=True, wager=wager, total_pot=total_pot)
        if roll_off_winner:
            return roll_off_winner


def game_round_bank(active_players):
    pass
