def solution(s):
    answer = 0
    pair = {')': '(', ']': '[', '}': '{'}
    
    for i in range(len(s)):
        stack = []
        valid = True
        
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pair[ch]:
                    valid = False
                    break
                stack.pop()
        if valid and not stack:
            answer += 1
        
        s = s[1:] + s[0]
        
    return answer