import sys
input = sys.stdin.readline

croa = ['c=', "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0

s_input = input()
i = 0
while i + 1 < len(s_input):
    if s_input[i:i + 2] in croa:
        cnt += 1
        i += 2
    elif s_input[i:i + 3] in croa:
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1

print(cnt)