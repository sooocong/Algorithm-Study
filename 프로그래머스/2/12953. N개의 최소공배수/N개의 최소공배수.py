# 배열 최소공배수 = 앞에서부터 LCM 누적
def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        # answer 새로운 최소공배수로 초기화
        answer = lcm(answer, arr[i])
        
    return answer

# 최대공약수
# from math import gcd -> 표준 라이브러리
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)