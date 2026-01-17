def solution(n, words):
    dict = {}
    dict[words[0]] = 1
    for i in range(1, len(words)):
        if words[i] not in dict:
            dict[words[i]] = 1
            if words[i - 1][-1] != words[i][0]:
                return [i % n + 1, i // n + 1] # 번호, 차례
            else:
                continue
        else:
            dict[words[i]] += 1
            return [i % n + 1, i // n + 1] # 번호, 차례
        
    return [0, 0] # 탈락자 x