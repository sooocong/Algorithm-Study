from collections import deque

def solution(s):
    ans = 0
    s = deque(s)
            
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            if j == 0:
                stack.append(s[0])
            elif len(stack) == 0:
                stack.append(s[j])
            elif s[j] == ')' and stack[-1] == '(':
                stack.pop()

            elif s[j] == '}' and stack[-1] == '{':
                stack.pop()

            elif s[j] == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s[j])
            
        if len(stack) == 0:
                ans += 1
        s.append(s.popleft())

    return ans