from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    arr1 = []
    arr2 = []
    
    for i in range(len(str1) - 1):
        s = str1[i : i + 2]
        if s.isalpha():
            arr1.append(s)
            
    for i in range(len(str2) - 1):
        s = str2[i : i + 2]
        if s.isalpha():
            arr2.append(s)
    
    # Counter로 다중집합 생성
    c1 = Counter(arr1)
    c2 = Counter(arr2)
    
    # 교집합 / 합집합
    intersection = c1 & c2
    union = c1 | c2
    
    inter_cnt = sum(intersection.values())
    union_cnt = sum(union.values())
    
    if union_cnt == 0:
        return 65536
    
    return int((inter_cnt / union_cnt) * 65536)