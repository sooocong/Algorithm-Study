def solution(s):
    answer = 0
    i = 0

    while i < len(s):
        x = s[i]
        x_count = 0
        other_count = 0

        while i < len(s):
            if s[i] == x:
                x_count += 1
            else:
                other_count += 1

            i += 1

            # 두 개수가 같아지는 순간 분리
            if x_count == other_count:
                break

        answer += 1  # 문자열 하나 분리됨

    return answer