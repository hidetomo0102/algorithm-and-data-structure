# 190.Reverse Bits


def reverseBits(n: int) -> int:
    reverse_binary = ""
    while n > 0:
        reverse_binary += str(n % 2)
        n //= 2

    for i in range(0, 32 - len(reverse_binary)):
        reverse_binary += "0"
    return int(reverse_binary, 2)
