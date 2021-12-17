# 6.Zigzag Conversion
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    res = [""] * numRows

    j = 0
    k = numRows - 1
    for i in range(len(s)):
        if j < numRows:
            res[j] += s[i]
            j += 1

        if j >= numRows:
            if 1 <= k <= numRows - 2:
                res[k] += s[i]
            k -= 1

        if k == 0 and j >= numRows:
            j = 0
            k = numRows - 1

    return "".join(res)


a = convert("PAYPALISHIRING", 3)
print(a)
