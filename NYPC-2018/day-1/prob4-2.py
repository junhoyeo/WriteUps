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