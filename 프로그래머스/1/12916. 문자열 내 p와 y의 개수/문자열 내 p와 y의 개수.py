def solution(s):
    p_len, y_len = 0, 0
    
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            p_len += 1
        elif s[i] == 'y' or s[i] == 'Y':
            y_len += 1
    
    if p_len == y_len:
        return True
    else:
        return False