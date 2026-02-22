import sys
input = sys.stdin.readline

king, stone, N = input().split()
N = int(N)

# king
kx = ord(king[0]) - ord('A')
ky = int(king[1]) - 1

# stone
sx = ord(stone[0]) - ord('A')
sy = int(stone[1]) - 1

move_dict = {
    'R':  (1, 0),
    'L':  (-1, 0),
    'B':  (0, -1),
    'T':  (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1)
}

def in_board(x, y):
    return 0 <= x < 8 and 0 <= y < 8

for _ in range(N):
    move = input().strip()
    dx, dy = move_dict[move]

    nkx, nky = kx + dx, ky + dy
    if not in_board(nkx, nky):
        continue

    if nkx == sx and nky == sy:
        nsx, nsy = sx + dx, sy + dy
        if not in_board(nsx, nsy):
            continue
        sx, sy = nsx, nsy

    kx, ky = nkx, nky

print(chr(kx + ord('A')) + str(ky + 1))
print(chr(sx + ord('A')) + str(sy + 1))