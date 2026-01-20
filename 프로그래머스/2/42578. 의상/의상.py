def solution(clothes):
    clothes_dict = {}
    ans = 1
    for clo in clothes:
        if clo[1] not in clothes_dict:
            clothes_dict[clo[1]] = 1
        else:
            clothes_dict[clo[1]] += 1
            
    clothes_dict = list(clothes_dict.values())
    
    for i in range(len(clothes_dict)):
        ans *= (clothes_dict[i] + 1)
        
    return ans - 1