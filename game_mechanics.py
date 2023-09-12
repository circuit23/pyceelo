from random import randint


def get_roll(amount=3):
    return [randint(1, 6) for _ in range(amount)]


def get_result(roll_list):
    roll_list.sort()
    roll_1, roll_2, roll_3 = roll_list

    if (roll_1, roll_2, roll_3) == (4, 5, 6):
        print("WIN: 4-5-6 straight kill")
        return "WW", "WIN: 4-5-6 straight kill"
    elif all(item == roll_list[0] for item in roll_list):
        print(f"TRIPS: {roll_1}")
        return f"T{roll_1}", f"TRIPS: {roll_1}"
    elif roll_1 == roll_2:
        print(f"POINT: {roll_3}")
        return f"P{roll_3}", f"POINT: {roll_3}"
    elif roll_2 == roll_3:
        print(f"POINT: {roll_1}")
        return f"P{roll_1}", f"POINT: {roll_1}"
    elif (roll_1, roll_2, roll_3) == (1, 2, 3):
        print("LOSE: 1-2-3 straight lose")
        return "LL", "LOSE: 1-2-3 straight lose"
    else:
        return None


def compare_results_pvp(player_dict):
    wins = {k: v for k, v in player_dict.items() if player_dict[k].result == "WW"}
    trips = {k: v for k, v in player_dict.items() if player_dict[k].result[0] == "T"}
    points = {k: v for k, v in player_dict.items() if player_dict[k].result[0] == "P"}
    losers = {k: v for k, v in player_dict.items() if player_dict[k].result == "LL"}
    for tier_list in [wins, trips, points, losers]:
        if tier_list:
            if len(tier_list) == 1:
                print([f"{player_dict[player].name} wins with the result '{player_dict[player].result_lf}'" for player
                       in tier_list])
            else:
                # TODO: Run through levels of trips and points, then return the winner.  Else: roll-off!
                print("Roll-off!")
                for item in dict(sorted(tier_list.items(), key=lambda item: item[1].result, reverse=True)):
                    print(f"{tier_list[item].name}: {tier_list[item].result_lf}")
            break
        else:
            continue
