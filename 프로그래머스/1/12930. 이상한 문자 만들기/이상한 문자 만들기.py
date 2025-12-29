def solution(s):
    words = s.split(' ')
    p = []
    for word in words:
        answer = ''
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        p.append(answer)
    return ' '.join(p)