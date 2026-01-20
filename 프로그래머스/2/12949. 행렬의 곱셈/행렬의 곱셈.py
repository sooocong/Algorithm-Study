def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    
    # 행렬곱
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            cnt = 0
            for k in range(len(arr1[0])):
                cnt += arr1[i][k] * arr2[k][j]
            answer[i].append(cnt)

    return answer