# ABC127 C - Prison
N, M = map(int, input().split())

l, r = map(int, input().split())
for _ in range(M - 1):
    L, R = map(int, input().split())
    l = max(l, L)
    r = min(r, R)

print(max(0, r - l + 1))
