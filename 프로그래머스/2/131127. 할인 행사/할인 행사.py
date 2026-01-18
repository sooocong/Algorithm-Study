def solution(want, number, discount):
    ans = 0
    want_dict = {}
    
    # want, number -> 하나의 딕셔너리 쌍으로 만들기
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    for i in range(len(discount) - 9):
        dis_dict = {}
        for j in range(i, i + 10):
            if discount[j] not in dis_dict:
                dis_dict[discount[j]] = 1
            else:
                dis_dict[discount[j]] += 1
                
        if want_dict == dis_dict:
            ans += 1
    return ans