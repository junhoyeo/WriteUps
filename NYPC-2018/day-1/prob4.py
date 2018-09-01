from operator import itemgetter
from datetime import datetime, timedelta
score = [10, 8, 6, 5, 4, 3, 2, 1]
T = int(input()) # number of testcases
for t in range(T):
    game_type = input()
    game_player = []
    if game_type == 'item':
        for i in range(8):
            data = input().split()
            data[1] = float(data[1].replace(':', ''))
            game_player.append(data)
        game_player = sorted(game_player, key=itemgetter(1))
        print(game_player[0][0])
    else: # speed
        for i in range(8):
            data = input().split()
            data += data[1].split('.')
            del(data[1])
            data[1] = datetime.strptime(data[1], '%M:%S')
            game_player.append(data)
        game_player = sorted(game_player, key=itemgetter(1))
        for i in range(len(game_player)-1):
            if game_player[i][1] == game_player[i+1][1]:
                if game_player[i+1][2] < game_player[i][2]:
                    game_player[i], game_player[i+1] = game_player[i+1], game_player[i]
        retire = game_player[0][1] + timedelta(seconds=10)
        retire_xx = game_player[0][2]
        blue = 0
        red = 0
        for rank, player in enumerate(game_player):
            # print(player[1], retire)
            if player[1] < retire:
                if player[0] == 'red':
                    red += score[rank]
                    # print('red', score[rank])
                else: # blue
                    blue += score[rank]
                    # print('blue', score[rank])
            if player[1] == retire:
                if player[2] < retire_xx:
                    if player[0] == 'red':
                        red += score[rank]
                        # print('red', score[rank])
                    else: # blue
                        blue += score[rank]
                        # print('blue', score[rank])
            else:
                if player[0] == 'red':
                    red += 0
                else: # blue
                    blue += 0
        # print('red : ', red, 'blue : ', blue)
        if red > blue:
            print('red')
        elif red == blue:
            print(game_player[0][0])
        else: # blue > red
            print('blue')
