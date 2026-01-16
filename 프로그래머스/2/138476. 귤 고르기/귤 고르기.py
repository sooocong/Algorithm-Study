def solution(k, tangerine):
    answer = 0
    tan_dict = {}
    
    # 딕셔너리로 만들고, 개수 기준 역순으로 정렬
    # k개까지 ..
    for i in range(len(tangerine)):
        if tangerine[i] not in tan_dict:
            tan_dict[tangerine[i]] = 1
        else:
            tan_dict[tangerine[i]] += 1

    lst = list(tan_dict.items())
    lst.sort(key=lambda x:x[1], reverse = True)

    i = 0
    while k > 0:
        answer += 1
        k -= lst[i][1]
        i += 1
        
    return answer