def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1

    return haystack.find(needle)


a = strStr("hello", "ll")
b = strStr("", "")
print(a)
print(b)
