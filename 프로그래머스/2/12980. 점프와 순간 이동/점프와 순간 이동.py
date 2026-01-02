def solution(n):
    ans = 0
    # 뒤로 가는 걸로 생각하기
    # 홀수면 1 빼고(1만큼 점프), 짝수면 2로 나누기
    
    while n != 0:
        if n % 2 != 0:
            n -= 1
            ans += 1
        else:
            n //= 2
    
    return ans