import sys
input = sys.stdin.readline

n = int(input())
dungchi = []
answer = []

for i in range(n):
    x, y = map(int, input().split())
    dungchi.append([x, y])

for i in range(n):
    cnt = 0
    for j in range(n):
        if dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
            cnt += 1
    answer.append(cnt + 1)

print(' '.join(str(a) for a in answer))