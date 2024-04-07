input = __import__('sys').stdin.readline

N = int(input())
bar = []

for i in range(N):
    a = list(input().split())

    if a[0] == 'push':
        bar.append(a[1])
    if a[0] == 'pop':
        if len(bar) == 0:
            print(-1)
        else:
            print(bar.pop())
    if a[0] == 'size':
        print(len(bar))
    if a[0] == 'empty':
        if len(bar) == 0:
            print(1)
        else:
            print(0)
    if a[0] == 'top':
        if len(bar) == 0 :
            print(-1)
        else:
            print(bar[-1])