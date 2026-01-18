def solution(n,a,b):
    ans = 1
    
    while 1:
        if b - a == 1 and b % 2 == 0:
            break
        if a - b == 1 and a % 2 == 0:
            break
        a = (a + 1) // 2
        b = (b + 1) // 2
        ans += 1
        
    return ans