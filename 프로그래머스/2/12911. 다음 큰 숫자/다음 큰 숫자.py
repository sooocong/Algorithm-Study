from collections import Counter

def solution(n):
    new = n
    while 1:
        new += 1
        if Counter(bin(new)[2:])['1'] == Counter(bin(n)[2:])['1']:
            return new