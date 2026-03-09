from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def can_change(a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff == 1
    
    visited = [False] * len(words)
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        current, step = queue.popleft()
        
        if current == target:
            return step
        
        for i in range(len(words)):
            if not visited[i] and can_change(current, words[i]):
                visited[i] = True
                queue.append((words[i], step + 1))
    
    return 0