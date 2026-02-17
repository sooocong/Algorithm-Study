import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = list(map(int, input().split()))
leg_stack = deque([0 for _ in range(w)])

leg = 0 # 다리 위 무게
time = 0 # 최단시간
while truck or leg > 0:
    out = leg_stack.popleft()
    leg -= out

    if truck and leg + truck[0] <= l:
        x = truck.pop(0)
        leg_stack.append(x)
        leg += x
    else:
        leg_stack.append(0)
    time += 1

print(time)