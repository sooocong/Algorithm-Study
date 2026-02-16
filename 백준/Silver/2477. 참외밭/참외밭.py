import sys
input = sys.stdin.readline

K = int(input())
cham = []
ch_dict = {}

for i in range(6):
    arrow, length = map(int, input().split())
    cham.append((arrow, length))

for a, l in cham:
    if a not in ch_dict:
        ch_dict[a] = l
    else:
        ch_dict[a] += l

max_w, max_h = 0, 0
for i in range(len(cham)):
    if cham[i][0] == 1 or cham[i][0] == 2:
        max_w = max(max_w, cham[i][1])
    if cham[i][0] == 3 or cham[i][0] == 4:
        max_h = max(max_h, cham[i][1])

small_w, small_h = 0, 0
for i in range(len(cham)):
    if cham[i][1] == max_w:
        small_w = abs(cham[(i - 1) % 6][1] - cham[(i + 1) % 6][1])
    if cham[i][1] == max_h:
        small_h = abs(cham[(i - 1) % 6][1] - cham[(i + 1) % 6][1])

# 참외밭 전체너비
width = ch_dict[1] * ch_dict[4] - small_w * small_h

print(width * K)