from sys import stdin
from collections import deque

N = int(stdin.readline())
deq = deque()

for i in range(N):
    a = stdin.readline().split()

    if a[0] == 'push_front':
        deq.appendleft(a[1])
    if a[0] == 'push_back':
        deq.append(a[1])
    if a[0] == 'pop_front':
        if len(deq) > 0:
            print(deq.popleft())
        else:
            print(-1)
    if a[0] == 'pop_back':
        if len(deq) > 0:
            print(deq.pop())
        else:
            print(-1)
    if a[0] == 'size':
        print(len(deq))
    if a[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    if a[0] == 'front':
        if len(deq) > 0:
            print(deq[0])
        else:
            print(-1)
    if a[0] == 'back':
        if len(deq) > 0:
            print(deq[len(deq)-1])
        else:
            print(-1)