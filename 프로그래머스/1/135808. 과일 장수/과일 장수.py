def solution(k, m, score):
    answer = 0
    score.sort()
    box = len(score) // m

    for i in range(1, box + 1):        
        answer += (m * score[len(score) - m * i])
        
    return answer
    