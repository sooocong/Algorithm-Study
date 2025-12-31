def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        total = 0
        total += numbers[i]
        for j in range(i + 1, len(numbers)):
            total += numbers[j]
            answer.add(total)
            total = numbers[i]
    
    return sorted(answer)