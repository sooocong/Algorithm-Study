def solution(s, skip, index):
    answer = []
    skip_set = set(skip)
    
    for ch in s:
        cnt = 0
        cur = ch
        
        while cnt < index:
            cur = chr((ord(cur) - 97 + 1) % 26 + 97)
            if cur not in skip_set:
                cnt += 1
                
        answer.append(cur)
    
    return ''.join(answer)