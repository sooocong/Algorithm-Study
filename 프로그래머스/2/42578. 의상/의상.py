def solution(clothes):
    clothes_dict = {}
    
    for clo in clothes:
        if clo[1] not in clothes_dict:
            clothes_dict[clo[1]] = 1
        else:
            clothes_dict[clo[1]] += 1
            
    ans = 1
    for i, v in clothes_dict.items():
        ans *= (v + 1)
            
    return ans - 1