def solution(number, k):
    answer = ''
    stack = []
    t = 0
    
    for n in number:
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
            
    if t == 0:
        for _ in range(k):
            del stack[-1]
            
    return ''.join(stack)