from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    visited = set()
    visited.add(x)

    while queue:
        v, cnt = queue.popleft()
        if v == y:
            return cnt

        for nv in (v + n, v * 2, v * 3):
            if nv <= y and nv not in visited:
                visited.add(nv)
                queue.append((nv, cnt + 1))

    return -1