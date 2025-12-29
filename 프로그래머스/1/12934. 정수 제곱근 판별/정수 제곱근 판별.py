import math

def solution(n):
    sqrt = math.sqrt(n)
    
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    else:
        return -1