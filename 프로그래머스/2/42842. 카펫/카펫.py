def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for h in range(3, total // 2):
        if total % h == 0:
            w = total // h
            if (w - 2) * (h - 2) == yellow and 2 * (w - 1) + 2 * (h - 1) == brown:
                answer.append(w)
                answer.append(h)
                return answer