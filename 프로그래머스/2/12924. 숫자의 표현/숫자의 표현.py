def solution(n):
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(i, n + 1):
            cnt += j
            if cnt == n:
                ans += 1
                break
            elif cnt > n:
                break
            
    return ans