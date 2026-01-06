def solution(clothes):
    answer = 1
    closet = {}
    
    for Kind, Type in clothes:
        if Type not in closet:
            closet[Type] = 1
        else:
            closet[Type] += 1
            
    for key, value in closet.items():
        answer *= (value + 1)
    
    return answer - 1