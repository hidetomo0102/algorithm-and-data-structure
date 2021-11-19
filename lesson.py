def lengthOfLastWord(s: str) -> int:
    strs = s.split()
    return len(strs[-1])


a = lengthOfLastWord("   fly me   to   the moon  ")
print(a)
