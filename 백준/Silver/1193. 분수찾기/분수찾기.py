import sys
input = sys.stdin.readline

x = int(input())

k = 1
while k * (k + 1) // 2 < x:
    k += 1

pos = x - (k * (k - 1) // 2)

if k % 2 == 0:
    numerator = pos
    denominator = k - pos + 1
else:
    numerator = k - pos + 1
    denominator = pos

print(f"{numerator}/{denominator}")