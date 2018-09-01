from datetime import date, datetime, timedelta
import itertools

def perdelta(start, end, delta):
    # https://stackoverflow.com/questions/40815648/get-all-the-times-in-between-two-datetime-in-list
    curr = start
    while curr <= end:
        yield curr
        curr += delta

n = int(input())
time_range = []

for i in range(n):
    data = input().split()
    start = datetime.strptime(data[0], '%H:%M')
    end = datetime.strptime(data[1], '%H:%M')
    # print(start, end)

    times = []
    for result in perdelta(start , end, timedelta(seconds=1)):
        times.append(result.strftime('%H:%M'))
    time_range.append(times)
    
result = []
count = []
for i in range(len(time_range)):
    for j in range(len(time_range)):
        tmp = list(set(time_range[i]).intersection(time_range[j]))
        tmp.sort()
        if len(tmp) < 2:
            continue
        data = [tmp[0], tmp[-1:][0]]
        if data in result:
            count[result.index(data)] += 1
        else:
            result.append(data)
            count.append(1)
max_count = max(count)
print(max_count)
# idx = [i for i, j in enumerate(count) if j==max_count]
# for i in idx:
    # print(result[i][0], result[i][1])
idx = count.index(max_count)
print(result[idx][0], result[idx][1])
