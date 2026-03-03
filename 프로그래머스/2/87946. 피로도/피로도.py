from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    for case in permutations(dungeons, len(dungeons)):
        cnt = 0
        temp_k = k
        for i in range(len(case)):
            if temp_k >= case[i][0] and temp_k - case[i][1] >= 0:
                temp_k -= case[i][1]
                cnt += 1
            else:
                break
        answer.append(cnt)
    
    return max(answer)