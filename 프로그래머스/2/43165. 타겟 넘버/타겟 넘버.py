def solution(numbers, target):
    n = len(numbers)
    
    def dfs(idx, total):
        if n == idx:
            if total == target:
                return 1
            else:
                return 0
        return dfs(idx+1, total + numbers[idx]) + dfs(idx+1, total - numbers[idx])
        
    return dfs(0, 0)