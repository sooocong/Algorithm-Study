def solution(array, commands):
    a = len(commands)
    letter = []
    answer = []
    
    for i in range(a):
        letter.append(array[commands[i][0] - 1 : commands[i][1]])
        letter[i] = sorted(letter[i])
        
    for i in range(a):
        answer.append(letter[i][commands[i][2] - 1])
        
    return answer
