def solution(s):
    answer = ''
    answer = sorted(s, key=lambda x: ord(x), reverse = True)
    
    return ''.join(answer)