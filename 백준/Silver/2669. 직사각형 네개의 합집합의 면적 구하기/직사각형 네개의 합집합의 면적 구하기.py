import sys
input = sys.stdin.readline

rects = []
max_x, max_y = 0, 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    rects.append((x1, y1, x2, y2))
    max_x = max(x2, max_x)
    max_y = max(y2, max_y)

board = [[0 for _ in range(max_x)] for _ in range(max_y)]

for k in range(len(rects)):
    for i in range(max_y - rects[k][3], max_y - rects[k][1]):
        for j in range(rects[k][0], rects[k][2]):
            board[i][j] = 1

cnt = 0
for bo in board:
    for b in bo:
        if b == 1:
            cnt += 1
print(cnt)