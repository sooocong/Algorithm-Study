from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    t = int(input())

    for _ in range(t):
        m, n, k = map(int, input().split())
        rect = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        for _ in range(k):
            x, y = map(int, input().split())
            rect[y][x] = 1

        ans = 0
        for i in range(n):
            for j in range(m):
                if rect[i][j] == 1 and not visited[i][j]:
                    ans += 1
                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True

                    while queue:
                        x, y = queue.popleft()

                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            if 0 <= nx < n and 0 <= ny < m and rect[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))


        print(ans)

bfs()