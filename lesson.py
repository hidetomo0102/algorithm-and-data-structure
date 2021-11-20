def mySqrt(x: int) -> int:
    root = -1
    start = 0
    end = x

    while start <= end:
        mid = start + (end - start) // 2
        if mid * mid == x:
            root = mid
            break
        if mid * mid > x:
            end = mid - 1
        else:
            start = mid + 1
            root = mid

    return root
