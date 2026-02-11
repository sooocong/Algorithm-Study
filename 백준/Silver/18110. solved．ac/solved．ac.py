import sys
input = sys.stdin.readline

n = int(input())
op = []

if n == 0:
    print(0)

else:
    for i in range(n):
        opinion = int(input())
        op.append(opinion)

    m = int(n * 0.15 + 0.5)
    op.sort()
    ans = 0
    
    if m != 0:
        sum_op = sum(op[m:-m])
        print(int(sum_op / (len(op) - m * 2) + 0.5))
    else:
        print(int(sum(op) / (len(op)) + 0.5))