"""
Count the numbers of the most frequent letter

Input: "This is a pen. This is an apple. Applepen."
Output: ('p', 6)
"""
from typing import Any, Tuple
from operator import itemgetter
from collections import Counter


def count_most_frequent_letter(chars: str) -> Tuple[Any, int]:
    chars = chars.lower().replace(' ', '').replace('.', '')
    char_counter = Counter(chars).most_common()
    return char_counter[0]


def count_most_frequent_letter2(chars: str) -> Tuple[Any, int]:
    chars = chars.lower().replace(' ', '').replace('.', '')

    l = [(c, chars.count(c)) for c in chars]

    return max(l, key=itemgetter(1))


a = count_most_frequent_letter2("This is a pen. This is an apple. Applepen.")
print(a)
