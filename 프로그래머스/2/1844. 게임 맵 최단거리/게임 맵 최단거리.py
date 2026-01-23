from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 방향: 우, 좌, 하, 상
    direction = [(0,1), (0,-1), (1,0), (-1,0)]
    
    # BFS 큐 초기화 (시작점)
    q = deque()
    q.append((0, 0))
    
    # 시작점 방문 처리 (거리 = 1)
    # maps[0][0]은 원래 1이지만, "방문했다"는 의미로 그대로 사용
    # 이후 방문한 칸은 2, 3, 4 ... 로 바뀜
    
    while q:
        x, y = q.popleft()
        
        # 도착 지점이면 바로 반환 (BFS라서 최단)
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            
            # 맵 범위 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 아직 방문 안 한 길(1)만 이동
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    
    return -1