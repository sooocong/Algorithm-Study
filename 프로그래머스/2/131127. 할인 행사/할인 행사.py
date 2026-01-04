from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    
    # 원하는 상품 딕셔너리 생성
    for i in range(len(want)):
        dic[want[i]] = number[i]

    # 10일씩 슬라이딩
    for i in range(len(discount) - 9):
        if dic == Counter(discount[i : i + 10]): 
            answer += 1

    return answer