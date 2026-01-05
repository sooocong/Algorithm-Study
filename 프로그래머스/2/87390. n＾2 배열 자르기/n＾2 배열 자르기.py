def solution(n, left, right):
    # 각 배열의 원소는 각 행, 열의 max + 1
    answer = []
    
    for k in range(left, right + 1):
        answer.append(max(k // n, k % n) + 1)
        
    return answer