def solution(food):
    answer = []
    
    for i in range(len(food) - 1):
        for j in range(food[i + 1] // 2):
            answer.append(i + 1)
    
    return ''.join(map(str, answer)) + '0' + ''.join(map(str, sorted(answer, reverse=True)))