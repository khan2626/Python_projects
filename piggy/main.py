import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

players = input("type number of players (2-4): ")
while True:
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break;
        else:
            print('enter number between 2 - 4')
    else:
        print('enter a valid digit')

players_scores = [0 for _ in range(players)]
max_score = 50
while max(players_scores) < max_score:
    for player_idx in range(players):
        current_score = 0
        print('player number', player_idx + 1, 'turn just started')
        while True:
            answer = input('would you like to roll? (y) to roll: ')
            if answer.lower() != 'y':
                break
            value = roll()
            if value == 1:
                print('you rolled a 1 and you have lost a turn')
                print('your current score is 0')
                current_score = 0
                break
            else:
                current_score += value
                print('you rolled', value)
                print('your current score is:', current_score)
        players_scores[player_idx] += current_score
    print(players_scores)

winner = max(players_scores)
winner_idx = players_scores.index(winner)
print('the winner is player number:', winner_idx + 1)



