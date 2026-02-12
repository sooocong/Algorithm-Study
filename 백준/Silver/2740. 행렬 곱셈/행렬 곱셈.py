import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())

B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

C = [[0]*K for _ in range(N)]

for i in range(N):
    for k in range(K):
        s = 0
        for j in range(M):
            s += A[i][j] * B[j][k]
        C[i][k] = s

for row in C:
    print(*row)