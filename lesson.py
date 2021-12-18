# C - Dice and Coin
N, K = map(int, input().split())

possibility = 0
for i in range(1, N + 1):
    if i >= K:
        possibility += 1 / N
    else:
        s = i
        prob = 1 / N
        while s < K:
            prob *= 0.5
            s *= 2
        possibility += prob

print(possibility)
