"""
二部グラフの判定

N := 頂点の数
M := 辺の数
"""
from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(set)

for i in range(M):
    a, b = list(map(int, input().split()))

    d[a].add(b)
    d[b].add(a)

color = [0 for i in range(N + 1)]
res = "Yes"


def dfs(v, c):
    queue = []

    def _dfs(v, c, queue: list):
        queue.append(v)

        for i in list(d[v]):
            if color[i] == c:
                return "No"
            elif i not in queue:
                color[i] = c * -1
                _dfs(i, -c, queue)
        return "Yes"

    return _dfs(v, c, queue)


color[1] = 1
print(dfs(1, 1))
