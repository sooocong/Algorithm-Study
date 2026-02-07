import sys
input = sys.stdin.readline

s = input().rstrip()

stack = []
answer = []
in_tag = False

for ch in s:
    if ch == "<":
        # 단어 처리
        while stack:
            answer.append(stack.pop())
        in_tag = True
        answer.append(ch)

    elif ch == ">":
        in_tag = False
        answer.append(ch)

    elif in_tag:
        # 태그 안은 그대로
        answer.append(ch)

    elif ch == " ":
        # 단어 끝
        while stack:
            answer.append(stack.pop())
        answer.append(" ")

    else:
        stack.append(ch)

# 마지막 단어 처리
while stack:
    answer.append(stack.pop())

print("".join(answer))