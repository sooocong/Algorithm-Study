def solution(citations):
    # 앞에 있을수록 인용수 많음
    citations.sort(reverse=True)
    
    # (i + 1) -> 현재까지 본 논문 개수
    for i in range(len(citations)):
        if (i + 1) > citations[i]:
            return i
    return len(citations)