def solution(s, n):
    answer = []
    n %= 26

    for c in s:
        if c.islower():
            answer.append(chr((ord(c) - ord('a') + n) % 26 + ord('a')))
        elif c.isupper():
            answer.append(chr((ord(c) - ord('A') + n) % 26 + ord('A')))
        else:
            answer.append(c)

    return ''.join(answer)