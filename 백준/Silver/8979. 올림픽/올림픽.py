import sys
input = sys.stdin.readline

N, K = map(int, input().split())
olimpic = []
for _ in range(N):
    name, g, s, b = input().split()
    name, g, s, b = map(int, (name, g, s, b))
    olimpic.append((name, g, s, b))

olimpic.sort(key=lambda x: (x[1], x[2], x[3]), reverse = True)

res = 1
for i in range(len(olimpic)):
    if olimpic[i][0] == K:
        print(res)
    elif i >= 1:
        if olimpic[i][1:] != olimpic[i - 1][1:]:
            res += 1