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
    elif roll_1 == roll_2:
        return f"POINT: {roll_3}"
    elif roll_2 == roll_3:
        return f"POINT: {roll_1}"
    elif (roll_1, roll_2, roll_3) == (1, 2, 3):
        return "LOSE: 1-2-3 straight lose"
    else:
        return None


def compare_results_pvp(player_dict):
    # TODO: actually rank everything to find a (or some) winner(s)
    wins = [player for player in player_dict if player_dict[player].return_result() == "WIN: 4-5-6 straight kill"]
    if wins:
        print([f"{player}: {player_dict[player].return_result()}" for player in wins])
    trips = [player for player in player_dict if player_dict[player].return_result()[:6] == "TRIPS:"]
    if trips:
        print([f"{player}: {player_dict[player].return_result()}" for player in trips])
    points = [player for player in player_dict if player_dict[player].return_result()[:6] == "POINT:"]
    if points:
        print([f"{player}: {player_dict[player].return_result()}" for player in points])
    losers = [player for player in player_dict if player_dict[player].return_result()[:5] == "LOSE:"]
    if losers:
        print([f"{player}: {player_dict[player].return_result()}" for player in losers])
