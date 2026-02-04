import sys
input = sys.stdin.readline

paper = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())

max_left, max_down = 0, 0
for i in range(n):
    left, down = map(int, input().split())
    max_left = max(left, 0)
    max_down = max(down, 0)

    for d in range(down - 1, down + 9):
        for l in range(left - 1, left + 9):
            paper[d][l] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)