def solution(a, b):
    answer = ''
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cnt = 0

    for i in range(a - 1):
        cnt += day[i]
    cnt += b
    
    if cnt % 7 == 1:
        answer = "FRI"
    elif cnt % 7 == 2:
        answer = "SAT"
    elif cnt % 7 == 3:
        answer = "SUN"
    elif cnt % 7 == 4:
        answer = "MON"
    elif cnt % 7 == 5:
        answer = "TUE"
    elif cnt % 7 == 6:
        answer = "WED"
    else:
        answer = "THU"

    return answer