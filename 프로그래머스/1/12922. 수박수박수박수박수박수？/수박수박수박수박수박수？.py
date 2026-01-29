def solution(n):
    answer = []
    
    for i in range(n // 2):
        answer.append('수박')
    if n % 2 != 0:
        answer.append('수')
    
    return ''.join(answer)