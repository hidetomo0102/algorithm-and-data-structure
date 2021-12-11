# 171.Excel Sheet Column Number


def titleToNumber(columnTitle: str) -> int:
    res = 0
    for col in columnTitle:
        res = (res * 26 + ord(col) - 64)

    return res


a = titleToNumber("AB")
print(a)
