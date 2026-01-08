def solution(s):
    sets = s[2:-2].split("},{")
    sets = [list(map(int, x.split(","))) for x in sets]
    sets.sort(key=len) # 원소 개수 기준으로 오름차순 정렬
    
    answer = []
    seen = set()

    for group in sets:
        for num in group:
            if num not in seen:
                answer.append(num)
                seen.add(num)
    
    return answer