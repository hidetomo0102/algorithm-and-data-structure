"""
Generate Prime Numbers
Input: 50 => [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 37, 41, 43, 47]
"""
import math
from collections import defaultdict
from typing import List, Tuple


def generate_primes_v1(number: int) -> List[int]:
    primes = []
    cache = {}
    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        primes.append(x)
        cache[x] = True
        for y in range(x * 2, number + 1, x):
            cache[y] = False
    return primes


def generate_primes_v2(number: int) -> List[int]:
    cache = {}
    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        yield x
        cache[x] = True
        # 素数の倍数はprimeではない
        for y in range(x * 2, number + 1, x):
            cache[y] = False


"""
素数判定
"""


def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False
    # √numまで見てあげればよい
    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def is_prime_v2(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    # 偶数は素数ではないのでスキップ
    for i in range(3, math.floor(math.sqrt(num) + 1), 2):
        if num % i == 0:
            return False
        return True


def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False
    if num % 2 == 0 or num % 3 == 0:
        return False
    # 6k ± 1で割り切れないものが素数
    for i in range(5, math.floor(math.sqrt(num) + 1), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
        return True


"""
ラハムジャンのTaxicab_number
1729 = Ta(2) = 1**3 + 12**3 + = 9**3 + 10**3

Input: 1, 2 => [(1729, [(1, 12), (9, 10))]
Input: 2, 2 => [(1729, [(1, 12), (9, 10))], [(4104, [(2, 16), (9, 15))]
Input: 1, 3 => [(87539319, [(167, 436), (228, 423), (225, 414))]
"""


def taxicab_number(max_ans_num: int, match_ans_num: int = 2) -> List[Tuple[int, List[Tuple[int, int]]]]:
    result = []
    got_ans_count = 0
    ans = 1
    while got_ans_count < max_ans_num:
        match_ans_count = 0
        memo = defaultdict(list)

        max_param = int(pow(ans, 1.0 / 3)) + 1
        for x in range(1, max_param):
            for y in range(x + 1, max_param):
                if x ** 3 + y == ans:
                    match_ans_count += 1
                    memo[ans].append((x, y))

        if match_ans_count == match_ans_num:
            result.append((ans, memo[ans]))
            got_ans_count += 1

        ans += 1

    return result


"""
フェルマーの最終定理を証明
-> x**n + y**n = z**nについて、n <= 2までなら成立するが n >= 3では成立しない（x < y)

Input: 10（x, yは10以下）, 2（乗数） => [(3, 4, 5), (6, 8, 10)]
Input: 10, 3 => []
Input: 10, 4 => []
...
10, n => []
"""


def fermat_last_theory(max_num: int, squire_num: int = 2) -> List[Tuple[int, int, int]]:
    result = []
    if squire_num < 2:
        return result

    for x in range(1, max_num + 1):
        for y in range(x + 1, max_num + 1):
            pow_sum = pow(x, squire_num) + pow(y, squire_num)
            z = pow(pow_sum, 1.0 / squire_num)

            if not z.is_integer():
                continue

            z = int(z)
            z_pow = pow(z, squire_num)
            if z_pow == pow_sum:
                result.append((x, y, z))
