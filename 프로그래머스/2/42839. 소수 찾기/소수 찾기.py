from itertools import permutations

def solution(numbers):
    a = set()
    num_list = [numbers[i] for i in range(len(numbers))]
    
    for i in range(1, len(num_list) + 1):
        for p in permutations(num_list, i):
            num = ''.join(p)
            num = int(num)
            if num != 0 and num != 1:
                a.add(num)
                
    answer = 0
    for i in a:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
    
    return answer