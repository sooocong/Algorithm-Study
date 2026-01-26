def solution(skill, skill_trees):
    answer = 0
    
    for i in range(len(skill_trees)):
        new = []
        for s in skill_trees[i]:
            if s in skill:
                new.append(s)

        cnt = 0
        for j in range(len(new)):
            if new[j] != skill[j]:
                break
            else:
                cnt += 1
            
        if cnt == len(new):
            answer += 1
            
    return answer