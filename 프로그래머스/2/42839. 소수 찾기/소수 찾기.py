from itertools import permutations

def solution(numbers):
    num = [numbers[i] for i in range(len(numbers))]
    ans = set()
    
    for i in range(len(num)):
        a = list(permutations(num, i + 1))
        
        for j in a:
            t = ''.join(j)
            ans.add(int(t))

    return is_prime(ans)

def is_prime(ans):
    answer = 0

    for a in ans:
        if a < 2:
            continue
            
        is_flag = True
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                is_flag = False
                break

        if is_flag:
            answer += 1
            
    return answer