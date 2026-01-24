def solution(word):
    answer = 0
    moeum = ['A', 'E', 'I', 'O', 'U']
    order = []
    
    def dfs(cur):
        if len(cur) > 5:
            return
        if cur != "": # 빈 문자열
            order.append(cur)
        for v in moeum:
            dfs(cur + v)
    
    dfs("")
    return order.index(word) + 1