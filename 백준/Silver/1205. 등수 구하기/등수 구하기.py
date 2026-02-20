import sys
input = sys.stdin.readline

N, score, P = map(int, input().split())
rank_dict = {}
cnt = 0

if N > 0:
    rank = list(map(int, input().split()))
    for r in rank:
        if r not in rank_dict:
            rank_dict[r] = 1
        else:
            rank_dict[r] += 1
    sorted_rank = sorted(rank_dict.items(), key=lambda x: x[0], reverse=True)

    if len(rank) == P:
        if score > rank[-1]:
            for s, n in sorted_rank:
                if s < score:
                    print(cnt + 1)
                    sys.exit()
                if s != score:
                    cnt += n
                else:
                    print(cnt + 1)
                    sys.exit()
            print(cnt + 1)
            sys.exit()
        else:
            print(-1)
            sys.exit()
    else:
        for s, n in sorted_rank:
            if s < score:
                print(cnt + 1)
                sys.exit()
            if s != score:
                cnt += n
            else:
                print(cnt + 1)
                sys.exit()
        print(cnt + 1)
        sys.exit()
else:
    print(1)
    sys.exit()