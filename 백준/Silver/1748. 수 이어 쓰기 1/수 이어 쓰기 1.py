import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
T = len(str(N))

for i in range(1, T):
    cnt += (9 * 10 ** (i - 1)) * i

cnt += (N - 10 ** (T - 1) + 1) * T

print(cnt)