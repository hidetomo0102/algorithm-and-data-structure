def isPalindrome(s: str) -> bool:
    s = ''.join([c.lower() for c in s if c.isalpha() or c.isnumeric()])
    if s == "":
        return True

    if s == s[::-1]:
        return True
    return False


a = isPalindrome("0P")
print(a)
