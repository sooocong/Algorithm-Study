from sys import stdin

N = int(stdin.readline())
queue =[]

for i in range(N):
    a = stdin.readline().split()

    if a[0] == 'push':
        queue.append(a[1])
    if a[0] == 'pop':
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)
    if a[0] == 'size':
        print(len(queue))
    if a[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if a[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    if a[0] == 'back':
        if len(queue) > 0:
            print(queue[len(queue)-1])
        else:
            print(-1)