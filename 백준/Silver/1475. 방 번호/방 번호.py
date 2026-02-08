import sys
input = sys.stdin.readline

room_dict = {}
N = int(input())

N = str(N)
for n in N:
    if n not in room_dict:
        room_dict[n] = 1
    else:
        room_dict[n] += 1

max_v = 0
cnt = 0
for i, v in room_dict.items():
    if i == '6' or i == '9':
        cnt += v
    else:
        if v > max_v:
            max_v = v

if cnt > max_v:
    print((cnt + 1 ) // 2)
else:
    print(max_v)