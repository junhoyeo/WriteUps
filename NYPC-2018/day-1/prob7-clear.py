n = int(input())

login = []
logout = []
for i in range(n):
    data = input().split()
    tmp1 = data[0].split(':')
    login.append(int(tmp1[0])*60 + int(tmp1[1]))
    tmp2 = data[1].split(':')
    logout.append(int(tmp2[0])*60 + int(tmp2[1]))
logged_in = []
tmp_range = []
tmp_hot = []
cache = None
for time_now in range(1440):
    for i in range(n):
        if login[i] == time_now:
            logged_in.append(i)
        if logout[i] == time_now:
            logged_in.remove(i)
    length = len(logged_in)
    if cache != length:
        tmp_hot.append(length)
        tmp_range.append(time_now)
    cache = length
idx = tmp_hot.index(max(tmp_hot))
print(tmp_hot[idx])
start = tmp_range[idx]
end = tmp_range[idx+1]
print('{:02d}:{:02d} {:02d}:{:02d}'.format(int(start/60), int(start%60), int(end/60), int(end%60)))
