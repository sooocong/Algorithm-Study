def solution(progresses, speeds):
    
    for i in range(len(progresses)):
        mod = (100 - progresses[i]) % speeds[i]
        progresses[i] = (100 - progresses[i]) // speeds[i]
        if mod != 0:
            progresses[i] += 1
            
    result = []
    answer = 1
    max_num = 0
    for i in range(len(progresses) - 1):
        max_num = max(max_num, progresses[i])
        if progresses[i] < progresses[i + 1] and max_num < progresses[i + 1]:
            result.append(answer)
            answer = 1
        else:
            answer += 1
            
    if len(progresses) != sum(result):
        result.append(len(progresses) - sum(result))
    
    return result