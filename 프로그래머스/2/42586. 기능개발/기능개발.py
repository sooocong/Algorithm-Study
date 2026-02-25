def solution(progresses, speeds):
    answer = []
    remain_stack = []
    for i in range(len(progresses)):
        t = 100 - progresses[i]
        if t % speeds[i] == 0:
            remain_stack.append(t // speeds[i])
        else:
            remain_stack.append(t // speeds[i] + 1)
    
    max_num = remain_stack[0]
    cnt = 1
    for remain in remain_stack[1:]:
        if max_num >= remain:
            cnt += 1
        else:
            answer.append(cnt)
            max_num = remain
            cnt = 1
    answer.append(cnt)
    
    return answer