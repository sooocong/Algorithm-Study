def solution(s):
    answer = []
    last_pos = {}

    for i in range(len(s)):
        if s[i] not in last_pos:
            answer.append(-1)
        else:
            answer.append(i - last_pos[s[i]])
        
        last_pos[s[i]] = i

    return answer