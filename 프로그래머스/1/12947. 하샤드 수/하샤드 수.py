def solution(x):
    a = len(str(x))
    answer = 0
    
    for i in range(a):
        answer += int(str(x)[i])
    
    if x % answer == 0:
        return True
    else:
        return False