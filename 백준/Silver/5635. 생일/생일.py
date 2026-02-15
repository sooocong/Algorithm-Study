import sys
input = sys.stdin.readline

n = int(input())
people = []
for _ in range(n):
    name, d, m, y = input().split()
    d, m, y = map(int, (d, m, y))
    people.append((name, d, m, y))

people.sort(key=lambda x: (x[3], x[2], x[1]))

print(people[n - 1][0])
print(people[0][0])