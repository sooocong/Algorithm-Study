from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(l, sx, sy, ex, ey):
    visited = [[0] * l for _ in range(l)]
    q = deque([(sx, sy)])
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()

        if x == ex and y == ey:
            return visited[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

t = int(input())
for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    print(bfs(l, sx, sy, ex, ey))