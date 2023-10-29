import random

def roll():
    min_number = 0
    max_number = 7

    roll = random.randint(min_number, max_number)

    return roll


while True:
    players = input("Please enter how many players will be playing. ( 2 - 5 ) ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 5:
            break
        else:
            print("There should be between 2 - 5 players.")
    else:
        print("Wrong input.")

max_score = 60
players_score = [0 for i in range(players)]


while max(players_score) < max_score:
    for players_idx in range(players):
        print("Player" , players_idx + 1, "turn now")
        curent_score = 0

        while True:
            should_roll = input("Do you want to roll? (y)")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled 1. Turn end")
                curent_score = 0
                break
            else:
                curent_score += value
                print("You rolled", value)

            print("Your current score is ", curent_score)

        players_score[players_idx] += curent_score
        print("Your total scored are: ", players_score[players_idx])

max_score = max(players_score)
winning_idx = players_idx.index(max_score)
print("Player number", winning_idx + 1, " is thewinner with the score of:", max_score)