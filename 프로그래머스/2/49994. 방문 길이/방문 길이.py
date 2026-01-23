def solution(dirs):
    x, y = 0, 0
    visited = set()
    
    # 방향별 이동
    move = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    
    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy
        
        # 좌표 범위 벗어나면 무시
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        
        # 길 저장 (방향 무시)
        road = tuple(sorted([(x, y), (nx, ny)]))
        visited.add(road)
        
        # 현재 위치 갱신
        x, y = nx, ny
    
    return len(visited)