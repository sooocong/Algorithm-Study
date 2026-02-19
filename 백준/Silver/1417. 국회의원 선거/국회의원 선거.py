import sys
input = sys.stdin.readline

N = int(input())
people = []
for i in range(N):
    people.append(int(input()))

if N == 1:
    print(0)
    sys.exit()

cnt = 0 # 매수 인원
while people[0] <= max(people[1:]):
    for i in range(1, len(people)):
        if people[i] == max(people[1:]) and people[0] <= max(people[1:]):
            people[i] -= 1
            people[0] += 1
            cnt += 1

print(cnt)