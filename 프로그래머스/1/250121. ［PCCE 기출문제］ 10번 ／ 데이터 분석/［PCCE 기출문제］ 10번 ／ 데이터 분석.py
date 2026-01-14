def solution(data, ext, val_ext, sort_by):
    answer = []
    a = ['code', 'date', 'maximum', 'remain']
    
    for i in range(len(data)):
        if data[i][a.index(ext)] < val_ext:
            answer.append(data[i])
            
    answer.sort(key = lambda x:x[a.index(sort_by)])
    return answer