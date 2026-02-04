import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
yose = deque(range(1, n + 1))
ans = []

while yose:
    yose.rotate(-(k - 1))   # 앞에서 k-1번 뒤로 보냄
    ans.append(yose.popleft())  # k번째 제거

res = ', '.join(map(str, ans))
print(f"<{res}>")