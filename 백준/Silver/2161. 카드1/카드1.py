import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
trash = []

li = deque()
for i in range(n):
    li.append(i + 1)

while len(li) > 1:
    trash.append(li.popleft())
    li.append(li.popleft())

trash.append(li[0])
print(' '.join(str(tr) for tr in trash))