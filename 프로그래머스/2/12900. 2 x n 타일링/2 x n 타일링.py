def solution(n):
    ans = []
    
    for i in range(n):
        if i <= 2:
            ans.append(i + 1)
        else:
            ans.append((ans[i - 1] + ans[i - 2]) % 1000000007)
        
    return ans[-1]