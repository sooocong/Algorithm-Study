def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer
    
# 최대공약수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)