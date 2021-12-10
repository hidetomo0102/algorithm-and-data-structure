# 168.Excel Sheet Column Title


def convertToTitle(columnNumber: int) -> str:
    result = ""
    while columnNumber:
        residue = columnNumber % 26

        if residue == 0:
            result = chr(90) + result
            columnNumber = columnNumber // 26 - 1
        else:
            result = chr(64 + residue) + result
            columnNumber = columnNumber // 26

    return result
