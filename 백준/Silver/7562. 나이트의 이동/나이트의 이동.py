from collections import deque
import sys
input = sys.stdin.readline

def solution(t):

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    def bfs(l, sx, sy, ex, ey):
        q = deque()
        q.append((sx, sy))

        visited = [[0] * l for _ in range(l)]
        visited[sx][sy] = 1

        while q:
            x, y = q.popleft()
            if x == ex and y == ey:
                return visited[x][y] - 1

            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    answer = []

    for _ in range(t):
        l = int(input())
        sx, sy = map(int, input().split())
        ex, ey = map(int, input().split())
        answer.append(bfs(l, sx, sy, ex, ey))

    return answer

t = int(input())
result = solution(t)
for r in result:
    print(r)