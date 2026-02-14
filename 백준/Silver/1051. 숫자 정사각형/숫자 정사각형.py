import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input().strip())

size = min(N, M)
for size in range(min(N,M), 0, -1):
    for i in range(N - size + 1):
        for j in range(M - size + 1):
            if board[i][j] == board[i][j + size - 1] == board[i + size - 1][j] == board[i + size - 1][j + size - 1]:
                print(size ** 2)
                sys.exit()