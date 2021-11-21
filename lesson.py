def climbStairs(n: int) -> int:
    s = [1, 1]
    for i in range(2, n + 1):
        s.append(s[-1] + s[-2])
    return s[-1]
