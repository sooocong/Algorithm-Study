from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache_hit, cache_miss = 1, 5
    
    mini_city = deque()
    for city in cities:
        city = city.lower()
        
        if cacheSize == 0:
            return len(cities) * cache_miss
        
        if city not in mini_city:
            if len(mini_city) == cacheSize:
                mini_city.popleft()
            mini_city.append(city)
            answer += cache_miss
        # LRU 알고리즘 -> 이미 안에 있더라도 다시 사용되면 최근 사용된 페이지로 교체됨
        else:
            a = mini_city.remove(city)
            mini_city.append(city)
            answer += cache_hit
    
    return answer