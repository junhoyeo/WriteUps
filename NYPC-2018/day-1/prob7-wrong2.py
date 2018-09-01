n = int(input())

login = []
logout = []
for i in range(n):
    data = input().split()
    login.append(data[0])
    logout.append(data[1])
# print(login)
# print(logout)
user_num = 0
user_hot = 0
start_time = ''
end_time = ''
for hour in range(0, 24):
    for minute in range(60):
        time_now = f'{hour:02}:{minute:02}'
        counter = user_num == user_hot
        if time_now=='09:59': print(counter)
        for i in range(n):
            if login[i] == time_now:
                user_num += 1
                print(login[i] + ' : ' + str(i) + '번 유저 로그인')
                print(user_num, user_hot)
                # print(user_num)
            if logout[i] == time_now:
                user_num -= 1
                print(logout[i] + ' : ' + str(i) + '번 유저 로그아웃')
                print(user_num, user_hot)   
                # print(user_num)
        if (user_num != user_hot) and counter:
            end_time = time_now
            print('!')
        if user_num is not 0: print(user_num, user_hot)
        if user_num > user_hot:
            user_hot = user_num
            start_time = time_now
print(user_hot)
print(start_time, end_time)
