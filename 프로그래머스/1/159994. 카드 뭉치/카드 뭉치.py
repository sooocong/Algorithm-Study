def solution(cards1, cards2, goal):
    start1, start2 = 0, 0
    
    for i in range(len(goal)):
        if start1 < len(cards1) and goal[i] == cards1[start1]:
            start1 += 1
        elif start2 < len(cards2) and goal[i] == cards2[start2]:
            start2 += 1
        else:
            return "No"
            
    return "Yes"