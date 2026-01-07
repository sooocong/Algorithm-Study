def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            cnt[0] += 1
        if answers[i] == two[i % len(two)]:
            cnt[1] += 1
        if answers[i] == thr[i % len(thr)]:
            cnt[2] += 1
            
    max_cnt = max(cnt)

    return [i + 1 for i, v in enumerate(cnt) if v == max_cnt]