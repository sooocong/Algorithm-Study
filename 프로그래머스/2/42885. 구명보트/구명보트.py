from collections import deque

def solution(people, limit):
    boat = 0
    people = deque(sorted(people))
    
    while len(people) != 0:
        if len(people) == 1:
            boat += 1
            break
        elif people[0] + people[-1] > limit:
            people.pop()
            boat += 1
        else:
            people.popleft()
            people.pop()
            boat += 1
    
    return boat