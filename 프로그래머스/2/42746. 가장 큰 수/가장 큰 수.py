def solution(numbers):
    num = []
    for n in numbers:
        num.append(str(n))
    num.sort(key=lambda x: x * 3, reverse = True)
    
    cnt = 0
    for n in num:
        cnt += int(n)
    if cnt == 0:
        return "0"
    else:
        return ''.join(n for n in num)