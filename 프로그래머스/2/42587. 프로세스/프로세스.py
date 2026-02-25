from collections import deque

def solution(priorities, location):
    answer = []
    queue = deque((idx, v) for idx, v in enumerate(priorities))

    while queue:
        process = queue.popleft()
        if any(process[1] < q[1] for q in queue):
            queue.append(process)
        else:
            answer.append(process)
    
    cnt = 1
    for a in answer:
        if location == a[0]:
            return cnt
        else:
            cnt += 1