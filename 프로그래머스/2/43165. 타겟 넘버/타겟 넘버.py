from itertools import product

def solution(numbers, target):
    a = [-1, 1]
    case_list = []
    
    for case in product(a, repeat = len(numbers)):
        case_list.append(list(case))

    ans = 0
    for i in range(2 ** len(numbers)):
        cnt = 0
        for j in range(len(numbers)):
            cnt += numbers[j] * case_list[i][j]
        if cnt == target:
            ans += 1
        
    return ans