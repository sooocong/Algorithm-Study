def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for number in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + number)
            tmp.append(parent - number)
        leaves = tmp
        
    for leaf in leaves:
        if target == leaf:
            answer += 1

    return answer

# def solution(numbers, target):
#     count = 0
    
#     def dfs(idx, total):
#         nonlocal count # dfs 안에서 solution 함수의 count 변수를 수정할 수 있게 해야함
        
#         if idx == len(numbers):
#             if target == total:
#                 count += 1
        
#             return
        
#         dfs(idx + 1, total + numbers[idx])
#         dfs(idx + 1, total - numbers[idx])
    
    
#     # dfs(0, 0)
    
#     return count