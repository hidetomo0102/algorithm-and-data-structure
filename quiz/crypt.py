"""
シーザー暗号
"""
import string
from typing import Generator, Tuple


def ceasar_cipher_v1(text: str, shift: int) -> str:
    result = ''
    for char in text:
        if char.isupper():
            alphabet = string.ascii_uppercase
        elif char.islower():
            alphabet = string.ascii_lowercase
        else:
            result += char
            continue

        index = (alphabet.index(char) + shift) % len(alphabet)
        result += alphabet[index]
    return result


def ceasar_cipher_v2(text: str, shift: int) -> str:
    result = ''
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            result += char

    return result


def hack_ceasar_cipher(text: str) -> Generator[Tuple[int, str], None, None]:
    for candidate in range(1, 26):
        reverted = ''
        for char in text:
            if char.isupper():
                alphabet = string.ascii_uppercase
            elif char.islower():
                alphabet = string.ascii_lowercase
            else:
                reverted += char
                continue

            index = alphabet.index(char) - candidate
            if index < 0:
                index += 26
            reverted += alphabet[index]

        yield candidate, reverted


"""
ヴィジュネル暗号
"""

ALPHABET = string.ascii_uppercase


def generate_key(message: str, keyword: str) -> str:
    key = keyword
    remain_length = len(message) - len(keyword)
    for i in range(remain_length):
        key += key[i]

    return key


def encrypt(message: str, generated_key: str) -> str:
    result = ''
    for i, char in enumerate(message):
        # スペースなどのとき
        if char not in ALPHABET:
            result += char
            continue

        index = (ALPHABET.index(char) + ALPHABET.index(generated_key[i])) % len(ALPHABET)
        result += ALPHABET[index]

    return result


def decrypt(cipher_text: str, generated_key: str) -> str:
    result = ''
    for i, char in enumerate(cipher_text):
        if char not in ALPHABET:
            result += char
            continue

        index = (ALPHABET.index(char) - ALPHABET.index(generated_key[i]) + len(ALPHABET)) % len(ALPHABET)
        result += ALPHABET[index]

    return result
