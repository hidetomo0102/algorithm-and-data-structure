from typing import List, Iterator


def all_perms(elements: List[int]) -> Iterator[List[int]]:
    """
    アプローチ
    elementsの先頭をtempとする
    そして残りの要素の組み合わせに応じてtempを配置する

    ex) [1, 2, 3] => temp:1, rest: [2, 3]
    1rap. 1, [2, 3] => [1, 2, 3] [2, 1, 3] [2, 3, 1]
    2rap. 1, [3, 2] => [1, 3, 2] [3, 1, 2] [3, 2, 1]
    """
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


for p in all_perms([1, 2, 3]):
    print(p)
