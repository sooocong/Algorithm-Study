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
same = 0
for i in range(len(olimpic)):
    if i == 0:
        if olimpic[i][0] == K:
            print(1)
            break
    else:
        if olimpic[i][0] == K:
            if olimpic[i][1:] != olimpic[i - 1][1:]:
                res += 1
                print(res + same)
                break
            else:
                print(res)
                break
        else:
            if olimpic[i][1:] != olimpic[i - 1][1:]:
                res += 1
            if olimpic[i][1:] == olimpic[i - 1][1:]:
                same += 1