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


def score_reset(player_dict):
    for player in player_dict:
        player_dict[player].result, player_dict[player].result_lf = None, None


def game_round_pvp(player_dict):
    score_reset(player_dict)
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
    # Compare results
    wins = [(k, player_dict[k].result[1]) for k in player_dict.keys() if player_dict[k].result[0] == "W"]
    trips = [(k, player_dict[k].result[1]) for k in player_dict.keys() if player_dict[k].result[0] == "T"]
    points = [(k, player_dict[k].result[1]) for k in player_dict.keys() if player_dict[k].result[0] == "P"]
    # losers = [(k, player_dict[k].result[1]) for k in player_dict.keys() if player_dict[k].result[0] == "L"]
    for bracket_list in [wins, trips, points]:
        if bracket_list:
            if len(bracket_list) == 1:
                return bracket_list[0][0]
            else:
                top_rank = 0
                winners_list = []
                for item in sorted(bracket_list, key=lambda item: item[1], reverse=True):
                    if top_rank == int(item[1]):
                        winners_list.append(item[0])  # add to winners_list due to same rank
                    elif top_rank < int(item[1]):
                        top_rank = int(item[1])
                        winners_list = [item[0]]  # begin new winners_list with new top rank
                if len(winners_list) > 1:
                    print("Roll-off!")
                    for winner in winners_list:
                        print(f"{player_dict[winner].name} ({player_dict[winner].result_lf})")
                        if not winner == winners_list[-1]:
                            print('tied with')
                    game_round_pvp({k: player_dict[k] for k in winners_list})
                return winners_list[0]
        else:
            continue
