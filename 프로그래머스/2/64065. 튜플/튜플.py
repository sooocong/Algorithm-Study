def solution(s):
    s_list = s[2:-2]
    result = s_list.split("},{")
    result = [list(map(int, r.split(","))) for r in result]
    result.sort(key=len)
    answer = []
    
    for res in result:
        for r in res:
            if r not in answer:
                answer.append(r)
    
    
    return answer