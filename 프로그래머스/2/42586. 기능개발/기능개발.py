from collections import deque

def solution(progresses, speeds):
    q = deque()
    
    for p, s in zip(progresses, speeds):
        q.append((100 - p + s - 1) // s)
    
    result = []
    while q:
        day = q.popleft()
        cnt = 1
        
        while q and q[0] <= day:
            q.popleft()
            cnt += 1
        
        result.append(cnt)
    
    return result