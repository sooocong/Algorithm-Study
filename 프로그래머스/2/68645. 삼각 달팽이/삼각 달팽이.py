def solution(n):
    arr = [[0] * n for _ in range(n)]
    
    # 시작 위치
    x, y = -1, 0
    # 채울 숫자
    num = 1
    
    for i in range(n):        
        for _ in range(n - i):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            
            arr[x][y] = num
            num += 1
    
    answer = []
    for row in arr:
        for val in row:
            if val != 0:
                answer.append(val)
    
    return answer