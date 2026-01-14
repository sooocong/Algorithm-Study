def solution(board, moves):
    answer = 0
    stack = []

    for i in range(len(moves)):
        col = moves[i] - 1
        for j in range(len(board)):
            if board[j][col] != 0:
                stack.append(board[j][col])
                board[j][col] *= 0
                break

        if len(stack) > 1 and stack[-1] == stack[-2]:
            del stack[-1]
            del stack[-1]
            answer += 2
                    
    return answer