import sys
input = sys.stdin.readline

n, k = map(int, input().split())

deleted = [False] * (n + 1)
cnt = 0

for p in range(2, n + 1):
    if deleted[p]:
        continue

    for x in range(p, n + 1, p):
        if not deleted[x]:
            deleted[x] = True
            cnt += 1
            if cnt == k:
                print(x)
                sys.exit(0)