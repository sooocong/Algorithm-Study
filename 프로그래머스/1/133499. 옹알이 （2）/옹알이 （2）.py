def solution(babbling):
    answer = 0
    pos = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        temp = b
        for p in pos:
            if p * 2 not in b:
                temp = temp.replace(p, " ")
        if temp.strip() == "":
            answer += 1
    
    return answer