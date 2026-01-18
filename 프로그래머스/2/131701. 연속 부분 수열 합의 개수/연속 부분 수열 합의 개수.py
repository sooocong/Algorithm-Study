def solution(elements):
    ans = set()
    ele = elements * 2
    
    for i in range(len(elements)):
        for j in range(len(elements)):
            if sum(ele[i : i + j + 1]) not in ans:
                ans.add(sum(ele[i : i + j + 1]))
    
    return len(ans)