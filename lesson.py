from typing import List


def plusOne(digits: List[int]) -> List[int]:
    s = ""
    for d in digits:
        s += str(d)

    a = int(s) + 1
    return [int(x) for x in str(a)]


a = plusOne([9])
b = plusOne([4, 3, 2, 1])
print(a)
