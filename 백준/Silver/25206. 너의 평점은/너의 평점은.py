import sys
input = sys.stdin.readline

score, sum_score = 0, 0

for i in range(20):
    a, b, c = input().split()
    b = float(b)
    sum_score += b

    if c == 'A+':
        score += b * 4.5
    elif c == 'A0':
        score += b * 4.0
    elif c == 'B+':
        score += b * 3.5
    elif c == 'B0':
        score += b * 3.0
    elif c == 'C+':
        score += b * 2.5
    elif c == 'C0':
        score += b * 2.0
    elif c == 'D+':
        score += b * 1.5
    elif c == 'D0':
        score += b * 1.0
    elif c == 'F':
        score += 0
    elif c == 'P':
        sum_score -= b
print(score / sum_score)