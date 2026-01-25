def solution(order):
    stack = []
    ans = 0
    now = 1
    n = len(order)

    for target in order:
        # 벨트에서 target이 나올 때까지 stack에 쌓기
        while now <= n and (not stack or stack[-1] != target):
            stack.append(now)
            now += 1

        # stack 맨 위가 target이면 꺼내기
        if stack and stack[-1] == target:
            stack.pop()
            ans += 1
        else:
            break

    return ans