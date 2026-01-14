from collections import Counter

def solution(X, Y):
    answer = []

    x_cnt = Counter(X)
    y_cnt = Counter(Y)
    
    for num in x_cnt:
        common = min(x_cnt[num], y_cnt.get(num, 0))
        answer.extend([num] * common)

    if len(answer) == 0:
        return "-1"
    
    answer.sort(reverse = True)

    if answer[0] == "0":
        return "0"
    
    return ''.join(answer)