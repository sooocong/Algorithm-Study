def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(total // 2 - 1, 0, -1):
        if total % i == 0:
            if yellow == (i - 2) * (total // i - 2) :
                return [i, total // i]