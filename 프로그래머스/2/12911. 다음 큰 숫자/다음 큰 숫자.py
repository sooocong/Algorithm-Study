def solution(n):
    target = bin(n).count('1') # n을 2진수 문자열로 변환 후 1 개수 카운트
    next_num = n + 1

    while True:
        if bin(next_num).count('1') == target:
            return next_num
        next_num += 1