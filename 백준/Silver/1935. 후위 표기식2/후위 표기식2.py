N = int(input())
a = list(input()) 
alpha = [0] * N

for i in range(N):
    alpha[i] = int(input())

stack = []

for i in a:
    if 'A' <= i <= 'Z':
        stack.append(alpha[ord(i) - 65])

    else:
        num2 = stack.pop()
        num1 = stack.pop()
        
        if i == '+':
            stack.append(num1 + num2)
        elif i == '-':
            stack.append(num1 - num2)
        elif i == '/':
            stack.append(num1 / num2)
        elif i == '*':
            stack.append(num1 * num2)

print('%.2f' %stack[0])