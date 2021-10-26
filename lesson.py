"""
2つの文字列 S, Tが与えられる。
Sに対し、変更・挿入・削除といった操作を施してTに変換する
このとき最小の操作回数は？
INPUT: S T
"""


def levenshtein_distance(s: str, t: str) -> int:
    if s == t:
        return 0
    s_len = len(s)
    t_len = len(t)

    if s == "": return t_len
    if t == "": return s_len

    matrix = []
    for i in range(s_len + 1):
        matrix.append([0 for _ in range(t_len + 1)])

    for i in range(1, s_len + 1):
        sc = s[i - 1]
        for j in range(1, t_len + 1):
            tc = t[j - 1]
            cost = 0 if (sc == tc) else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )
    return matrix[s_len][t_len]
