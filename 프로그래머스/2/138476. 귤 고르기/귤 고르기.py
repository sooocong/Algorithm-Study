def solution(k, tangerine):
    answer = 0
    d = {}
    
    for t in tangerine:
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
            
    d = sorted(d.items(), key = lambda x: x[1], reverse = True)
    
    for i in d:
        k -= i[1]
        answer += 1
        if k <= 0:
            break
    
    return answer