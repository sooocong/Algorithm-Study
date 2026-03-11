import sys
input = sys.stdin.readline
from collections import deque

def solution(n, k):
    q = deque()
    q.append((n, 0))
    visited = [False] * 100001
    visited[n] = True

    while q:
        idx, total = q.popleft()

        if idx == k:
            return total

        for nx in [idx-1, idx+1, idx*2]:
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                q.append((nx, total + 1))

n, k = map(int, input().split())
print(solution(n, k))