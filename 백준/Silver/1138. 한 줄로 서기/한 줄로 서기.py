import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = [0 for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(len(stack)):
        if stack[j] == 0:
            cnt += 1
        if cnt == a[i] + 1:
            stack[j] = i + 1
            break

print(' '.join(str(stack[i]) for i in range(len(stack))))