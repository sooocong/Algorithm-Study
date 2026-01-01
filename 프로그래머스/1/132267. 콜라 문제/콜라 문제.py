def solution(a, b, n):
    answer = 0

    while n >= a:
        exchanged = (n // a) * b
        answer += exchanged
        n = exchanged + (n % a)

    return answer