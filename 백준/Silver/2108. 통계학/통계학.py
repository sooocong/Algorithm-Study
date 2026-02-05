import sys
input = sys.stdin.readline

n = int(input())
ans = []
ans_dict = {}

for i in range(n):
    num = int(input())
    ans.append(num)

ans.sort()
mean = int(round(sum(ans) / len(ans), 0))

for a in ans:
    if a not in ans_dict:
        ans_dict[a] = 1
    else:
        ans_dict[a] += 1

max_freq = max(ans_dict.values())
modes = []
for k, v in ans_dict.items():
    if v == max_freq:
        modes.append(k)

modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]

print(mean)
print(ans[len(ans) // 2])
print(mode)
print(max(ans) - min(ans))