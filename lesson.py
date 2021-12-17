# 7.Reverse Integer


def reverse(x: int) -> int:
    if x == 0:
        return x

    if x > 0:
        nums = int(str(x)[::-1])
    else:
        nums = -int(str(x)[:-2])

    if abs(nums) > pow(2, 31):
        return 0

    return nums
