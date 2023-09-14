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


def get_wagers(player_list, game_mode):
    if game_mode == 'PvP':
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

        print(f"Each player bets {wager}, for a total of {total_pot}.")
        return wager, total_pot
    elif game_mode == 'BANK':
        # TODO: implement bank wagers
        pass


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
    player = player_dict[winner]
    if game_mode == 'PvP':
        player.increment_money(total_pot)
        return f"{player.name} nets {total_pot - wager} monies with {player.result_lf}!"
    elif game_mode == 'BANK':
        print('Bank mode is not currently supported.')
    else:
        print('Invalid game mode.')


def determine_winner(bracket_list, player_dict, wager, total_pot):
    if len(bracket_list) == 1:
        round_winner = bracket_list[0][0]
    else:
        bracket_winners = get_winners(bracket_list)
        if len(bracket_winners) == 1:
            round_winner = bracket_list[0][0]
        else:
            print("Roll-off!")
            for winner in bracket_winners:
                player = player_dict[winner]
                print(
                    f"{player.name} ({player.result_lf}){' tied with' if not winner == bracket_winners[-1] else ''}")
            roll_off_dict = {player: player_dict[player] for player in bracket_winners}
            return game_round_pvp(player_dict=roll_off_dict, roll_off=True, wager=wager, total_pot=total_pot)
    return print_winner(player_dict=player_dict, winner=round_winner, wager=wager, total_pot=total_pot,
                        game_mode='PvP')


def game_round_pvp(player_dict, roll_off=False, wager=0, total_pot=0):
    if not roll_off:
        # Get the wager, subtract from everyone's totals
        wager, total_pot = get_wagers(player_dict, game_mode='PvP')

    # Reset scores, then roll up all the players' dice
    score_reset(player_dict)
    roll_all_players(player_dict)

    # Separate into brackets and compare results
    result_types = ['W', 'T', 'P', 'L']
    brackets = [[(k, player_dict[k].result[1]) for k in player_dict.keys() if player_dict[k].result[0] == res_type] for
                res_type in result_types]

    loser_bracket = brackets[-1]
    if loser_bracket and len(loser_bracket) == len(player_dict):
        return "There was no winner this round... you are all losers!"

    for bracket_list in brackets[:-1]:
        if bracket_list:
            return determine_winner(bracket_list, player_dict, wager, total_pot)


def game_round_bank(active_players):
    pass
