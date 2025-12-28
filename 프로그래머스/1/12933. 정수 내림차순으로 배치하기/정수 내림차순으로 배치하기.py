def solution(n):
    ls = sorted(str(n), reverse=True)
    
    answer = int("".join(ls))
    
    return answer