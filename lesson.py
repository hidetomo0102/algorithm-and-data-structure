# ABC128 C - Switches
from itertools import product


def judge(pro):
    # 電球iに繋がったスイッチが押された回数
    count = [0] * M
    for i in range(N):
        if not pro[i]:
            continue
        for x in S[i]:
            count[x] += 1

    for p, c in zip(P, count):
        if c % 2 != p:
            return 0
    return 1


N, M = map(int, input().split())
S = [[] for _ in range(M)]
for i in range(M):
    k, *T = map(int, input().split())
    for x in T:
        S[x - 1].append(i)

P = list(map(int, input().split()))

ans = 0
for pro in product((0, 1), repeat=N):
    ans += judge(pro)
