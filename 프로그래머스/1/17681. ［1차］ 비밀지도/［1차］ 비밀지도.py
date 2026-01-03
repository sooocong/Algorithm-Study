def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        row = format(arr1[i] | arr2[i], f'0{n}b')
        row = row.replace('1', '#').replace('0', ' ')
        answer.append(row)
        
    return answer