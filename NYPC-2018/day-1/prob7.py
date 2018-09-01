n = int(input())

login = []
logout = []
for i in range(n):
    data = input().split()
    login.append(data[0])
    logout.append(data[1])
logged_in = []
tmp_range = []
tmp_hot = []
cache = None
for hour in range(0, 24):
    for minute in range(60):
        # time_now = f'{hour:02}:{minute:02}'
        time_now = '{hour:02d}:{minute:02d}'.format(hour=hour, minute=minute)
        for i in range(n):
            if login[i] == time_now:
                logged_in.append(i)
                # print(login[i] + ' : ' + str(i) + '번 유저 로그인')
                # print(logged_in)
            if logout[i] == time_now:
                logged_in.remove(i)
                # print(logout[i] + ' : ' + str(i) + '번 유저 로그아웃')
                # print(logged_in)
        if cache != len(logged_in):
            tmp_hot.append(len(logged_in))
            tmp_range.append(time_now)
        cache = len(logged_in)
# print(tmp_hot, tmp_range)
idx = tmp_hot.index(max(tmp_hot))
print(tmp_hot[idx])
print(tmp_range[idx], tmp_range[idx+1])
