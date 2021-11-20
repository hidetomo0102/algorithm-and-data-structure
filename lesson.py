def addBinary(a: str, b: str) -> str:
    a, b = int(a, 2), int(b, 2)
    return format(a + b, 'b')


a = addBinary("1010", "1011")
print(a)
