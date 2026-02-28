def solution(answers):
    ans = []
    answer = []

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt_a, cnt_b, cnt_c = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            cnt_a += 1
        if answers[i] == b[i % len(b)]:
            cnt_b += 1
        if answers[i] == c[i % len(c)]:
            cnt_c += 1
            
    ans.append(cnt_a)
    ans.append(cnt_b)
    ans.append(cnt_c)
    max_ans = max(ans)
    
    for i in range(len(ans)):
        if ans[i] == max_ans:
            answer.append(i + 1)
    return answer