import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess = [list(input().strip()) for _ in range(N)]

answer = float('inf')
# 8 * 8 로 자르기 필요
for x in range(N - 7):
    for y in range(M - 7):
        # 시작점이 w or b
        cnt_w, cnt_b = 0, 0

        for i in range(8):
            for j in range(8):
                cur = chess[x + i][y + j]

                if (i + j) % 2 == 0:
                    if cur != 'W':
                        cnt_w += 1
                    if cur != 'B':
                        cnt_b += 1
                else:
                    if cur != 'B':
                        cnt_w += 1
                    if cur != 'W':
                        cnt_b += 1

        answer = min(answer, cnt_w, cnt_b)

print(answer)