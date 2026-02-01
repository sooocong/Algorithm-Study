import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for i in range(n):
    s = input()
    s_dict = {}
    is_group = True

    for j in range(len(s)):
        if s[j] not in s_dict:
            s_dict[s[j]] = 1
        else:
            if s[j - 1] != s[j]:
                is_group = False

    if is_group:
        answer += 1

print(answer)