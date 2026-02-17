import sys
input = sys.stdin.readline

def mark(board, x):
    for r in range(5):
        for c in range(5):
            if board[r][c] == x:
                board[r][c] = 0
                return

def check_bingo(board):
    bingo = 0

    # 가로
    for r in range(5):
        if sum(board[r]) == 0:
            bingo += 1

    # 세로
    for c in range(5):
        s = 0
        for r in range(5):
            s += board[r][c]
        if s == 0:
            bingo += 1

    # 대각선 \
    if sum(board[i][i] for i in range(5)) == 0:
        bingo += 1

    # 대각선 /
    if sum(board[i][4 - i] for i in range(5)) == 0:
        bingo += 1

    return bingo

board = [list(map(int, input().split())) for _ in range(5)]
calls = []
for _ in range(5):
    calls.extend(map(int, input().split()))

cnt = 0
for x in calls:
    cnt += 1
    mark(board, x)
    if check_bingo(board) >= 3:
        print(cnt)
        break