def solution(array, commands):
    result = []
    
    for com in commands:
        k = array[com[0] - 1:com[1]]
        k.sort()
        result.append(k[com[2] - 1])
    
    return result