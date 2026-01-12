def solution(keymap, targets):
    answer = []
    
    key_dict = {}
    
    for key in keymap:
        for idx, char in enumerate(key):
            if char not in key_dict:
                key_dict[char] = idx + 1
            else:
                key_dict[char] = min(key_dict[char], idx + 1)
    
    for target in targets:
        total = 0
        possible = True
        
        for char in target:
            if char not in key_dict:
                possible = False
                break
            total += key_dict[char]
        
        if possible:
            answer.append(total)
        else:
            answer.append(-1)

    return answer