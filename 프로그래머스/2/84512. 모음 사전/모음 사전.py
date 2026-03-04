from itertools import product

def solution(word):
    result = 0
    moeum = ['A', 'E', 'I', 'O', 'U']
    moeum_list = []
    
    for i in range(len(moeum)):
        mo = list(product(moeum, repeat = i + 1))
        for m in mo:
            moeum_list.append(''.join(m))
    moeum_list.sort()
    
    return moeum_list.index(word) + 1