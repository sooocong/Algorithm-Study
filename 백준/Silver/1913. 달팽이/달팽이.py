import sys
input = sys.stdin.readline

N = int(input())
loc = int(input())
board = [[0] * N for _ in range(N)]
# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x = y = N // 2
num = 1
board[x][y] = num
dir = 0
step = 1
num += 1
while num <= N * N:
    for _ in range(2): # 1 1 2 2 3 3 4 4 ..
        for _ in range(step):
            if num > N * N:
                break
            x += dy[dir]
            y += dx[dir]
            board[x][y] = num
            num += 1
        dir = (dir + 1) % 4
    step += 1

for bo in board:
    print(' '.join(str(b) for b in bo))

for i in range(N):
    for j in range(N):
        if loc == board[i][j]:
            print(i + 1, j + 1)