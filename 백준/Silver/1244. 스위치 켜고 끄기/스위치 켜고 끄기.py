import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
student_num = int(input())
ans = []

for i in range(student_num):
    gender, num = map(int, input().split())

    # 남->1
    if gender == 1:
        for j in range(n // num):
            if s[num * (j + 1) - 1] == 0:
                s[num * (j + 1) - 1] = 1
            else:
                s[num * (j + 1) - 1] = 0

    # 여->2
    min_num = min(n - num, num - 1)
    if gender == 2:
        for k in range(1, min_num + 1):
            if s[num - 1 - k] == s[num - 1 + k]:
                continue
            else:
                min_num = k - 1
                break
        for z in range(num - 1 - min_num, min_num + num):
            if s[z] == 0:
                s[z] = 1
            else:
                s[z] = 0

for i in range(0, n, 20):
    print(' '.join(map(str, s[i:i+20])))