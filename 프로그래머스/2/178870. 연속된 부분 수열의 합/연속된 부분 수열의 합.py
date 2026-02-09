def solution(sequence, k):
    n = len(sequence)
    i, j = 0, 0
    cnt = sequence[0]

    best_i, best_j = 0, n - 1
    best_len = n  # 큰 값

    while i < n and j < n:
        if cnt == k:
            cur_len = j - i
            if cur_len < best_len:   # 길이 짧은 것 우선
                best_len = cur_len
                best_i, best_j = i, j

            # 다음 후보 찾기 위해 왼쪽을 줄여서 이동
            cnt -= sequence[i]
            i += 1

        elif cnt < k:
            j += 1
            if j == n:
                break
            cnt += sequence[j]

        else:  # cnt > k
            cnt -= sequence[i]
            i += 1
            if i > j and i < n:      # i가 j를 넘어가면 윈도우 재정비
                j = i
                cnt = sequence[i]

    return [best_i, best_j]