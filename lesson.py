"""
N 個の荷物があり、i(1≦i≦N) 番目の荷物には価値 vi と重さ wiが割り当てられている。
許容重量 Wのナップサックが1つある。
重さの和が W以下となるように荷物の集合を選びナップサックに詰め込むとき、価値の和の最大値を求めよ。
（ただし、同じ荷物は一度しか選ぶことができない）

INPUT:  N W
        v(1) w(1)
        v(2) w(2)
        ...
        v(n) w(n)
"""

N, W = map(int, input().split())
w = []
v = []

for i in range(N):
    x, y = map(int, input().split())
    w.append(x)
    v.append(y)

# テーブルの作成
dp = [[0] * (W + 1) for j in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        if j < w[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])

print(dp[N][W])
