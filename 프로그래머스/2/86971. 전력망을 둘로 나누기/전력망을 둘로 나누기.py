from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    ans = n
    for i in range(len(wires)):
        cut_a, cut_b = wires[i]

        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True
        cnt = 1

        while q:
            x = q.popleft()
            for nx in graph[x]:
                if (x == cut_a and nx == cut_b) or (x == cut_b and nx == cut_a):
                    continue

                if not visited[nx]:
                    visited[nx] = True
                    q.append(nx)
                    cnt += 1

        diff = abs(cnt - (n - cnt))
        ans = min(ans, diff)

    return ans