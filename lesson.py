# 3.Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(s: str) -> int:
    temp = ""
    lengths = []

    if len(s) < 2:
        return len(s)

    for l in s:
        if l in temp:
            lengths.append(len(temp))
            temp = temp[temp.index(l) + 1:] + l
        else:
            temp += l

    lengths.append(len(temp))
    return max(lengths)
