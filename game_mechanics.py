from random import randint


def get_roll(amount=3):
    return [randint(1, 6) for _ in range(amount)]


def get_result(roll_list):
    roll_list.sort()
    roll_1, roll_2, roll_3 = roll_list

    if (roll_1, roll_2, roll_3) == (4, 5, 6):
        return "WW", "WIN: 4-5-6 straight kill"
    elif all(item == roll_list[0] for item in roll_list):
        return f"T{roll_1}", f"TRIPS: {roll_1}"
    elif roll_1 == roll_2:
        return f"P{roll_3}", f"POINT: {roll_3}"
    elif roll_2 == roll_3:
        return f"P{roll_1}", f"POINT: {roll_1}"
    elif (roll_1, roll_2, roll_3) == (1, 2, 3):
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
                for player in tier_list:
                    print(f"{player_dict[player].name} wins with the result '{player_dict[player].result_lf}'!")
            else:
                # TODO: Run through levels of trips and points, then return the winner.  Else: roll-off!
                # something like:
                # for item in dict(sorted(tier_list.items(), key=lambda item: item[1].result, reverse=True)):
                    # compare item0 to item1, etc
                top_rank = 0
                for item in sorted(tier_list.items(), key=lambda item: item[1].result, reverse=True):
                    if top_rank < int(item[1].result[1]):
                        top_rank = int(item[1].result[1])
                        print(f"{item[1].name} wins with the result '{item[1].result_lf}'!")
                    elif top_rank == item[1].result[1]:
                        print("Roll-off!")
                        pass  # TODO: add these ties to a list for roll-off
                    else:  # top_rank is greater, so discard non-winning entries
                        break
            break
        else:
            continue
