# ABC129 C - Typical Stairs
N, M = map(int, input().split())
obstacles = [int(input()) for _ in range(M)]

dp = [0] * N
dp[0] = 1

for i in range(N):
    for d in range(1, 3):
        step = i + d
        if step > N or step in obstacles:
            continue
        dp[i + d] += dp[i]

print(dp[N] % (1000 ** 3 + 7))
