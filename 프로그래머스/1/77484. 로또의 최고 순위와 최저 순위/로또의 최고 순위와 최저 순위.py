def solution(lottos, win_nums):
    answer = []
    cnt, zero = 0, 0
    
    for num in win_nums:
        if num in lottos:
            cnt += 1
    for lot in lottos:
        if lot == 0:
            zero += 1
    
    # 최고 순위
    if cnt == 6:
        up = 1
    elif cnt == 5:
        up = 2
    elif cnt == 4:
        up = 3
    elif cnt == 3:
        up = 4
    elif cnt == 2:
        up = 5
    else:
        up = 6
    
    down = up - zero
    answer.append(1 if down <= 0 else down)
    answer.append(up)

    return answer