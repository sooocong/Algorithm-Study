def solution(n):
    fibo = [0, 1]
    
    if n == 1:
        return 0
    elif n == 2:
        return 1
        
    for i in range(2, n + 1):
        fibo.append(fibo[i - 2] + fibo[i - 1])
        
    ans = fibo[n]
    return ans % 1234567