from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)
        
    def can_change(a, b):
        diff = 0
        
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff == 1
        
    while q:
        current, step = q.popleft()
        if current == target:
            return step
        
        for i in range(len(words)):
            if not visited[i] and can_change(current, words[i]):
                visited[i] = True
                q.append((words[i], step + 1))
            
    return 0
            