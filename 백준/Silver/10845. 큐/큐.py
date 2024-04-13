import sys
from collections import deque

n = int(input())
q = deque()

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push":
        q.append(a[1])
    if a[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            x = q.popleft()
            print(x)
    if a[0] == "size":
        print(len(q))
    if a[0] == "empty":
        if len(q) == 0 :
            print(1)
        else:
            print(0)
    if a[0] =="front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    if a[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            x = q.pop()
            print(x)
            q.append(x)