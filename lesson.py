"""
Symmetric
INPUT: [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
OUTPUT: [(5, 3), (7, 4)]
"""


def symmetric_pair1(pairs: list):
    center = len(pairs) // 2
    pair_list = []
    ans = []
    for i, value in enumerate(pairs):
        if i <= center:
            pair_list.append((value[1], value[0]))
        else:
            if value in pair_list:
                ans.append(value)

    return ans


def symmetric_pair2(pairs: list):
    cache = {}
    ans = []
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif value == first:
            ans.append(pair)
    return ans
