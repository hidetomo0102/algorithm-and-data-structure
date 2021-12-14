# 5.Longest Palindromic Substring


def longestPalindrome(s: str) -> str:
    def expand(l, r):
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1

        return min(l + 1, len(s) - 1), max(r - 1, 0)

    max_len = 0
    maxl = maxr = 0

    for i in range(len(s)):
        l1, r1 = expand(i, i + 1)
        l2, r2 = expand(i, i)

        if r1 - l1 > max_len:
            max_len = r1 - l1
            maxl = l1
            maxr = r1
        elif r2 - l2 > max_len:
            max_len = r2 - l2
            maxl = l2
            maxr = r2

    return s[maxl:maxr + 1]
