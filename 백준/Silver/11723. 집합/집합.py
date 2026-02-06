import sys
input = sys.stdin.readline

m = int(input())
S = set()
for i in range(m):
    num = input().split()

    if num[0] == 'add':
        S.add(int(num[1]))
    elif num[0] == 'remove':
        if int(num[1]) in S:
            S.remove(int(num[1]))
    elif num[0] == 'check':
        if int(num[1]) in S:
            print(1)
        else:
            print(0)
    elif num[0] == 'toggle':
        if int(num[1]) in S:
            S.remove(int(num[1]))
        else:
            S.add(int(num[1]))
    elif num[0] == 'all':
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif num[0] == 'empty':
        S = set()