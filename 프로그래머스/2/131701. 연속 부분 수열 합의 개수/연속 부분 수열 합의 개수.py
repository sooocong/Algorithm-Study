def solution(elements):
    nums = elements * 2 #원형처리
    result = set()
    
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            result.add(sum(nums[j : j + i]))

    return len(result)