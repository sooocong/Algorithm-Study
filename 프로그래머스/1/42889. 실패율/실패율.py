def solution(N, stages):
    lose = [] # 실패율
    answer = []
    
    for i in range(1, N + 1):
        total, loc = 0, 0
        for s in stages:
            if s >= i:
                total += 1
            if s == i:
                loc += 1
        if total == 0:
            lose.append(0)
        else:
            lose.append(loc / total)
    
    lose = [(i+1, j) for i, j in enumerate(lose)]
    lose.sort(key=lambda x:x[1], reverse = True)
            
        
    return [i for i, j in lose]