def bubble_sort(numbers: list):
    limit = len(numbers) - 1
    for i in range(limit):
        for j in range(limit):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        limit -= 1
    return numbers


def cocktail_sort(numbers: list):
    swap = True
    start = 0
    end = len(numbers) - 1
    while swap:
        swap = False
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swap = True
        end -= 1

        if not swap:
            break

        for i in range(end, start):
            if numbers[i] < numbers[i - 1]:
                numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
                swap = True
        start += 1
    return numbers


def comb_sort(numbers: list):
    length = len(numbers)
    gap = length
    swap = True

    while gap != 1 or swap:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        for i in range(0, length, gap):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swap = True
    return numbers


def selection_sort(numbers: list):
    length = len(numbers)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if numbers[min_index] > numbers[j]:
                min_index = j
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


def gnome_sort(numbers: list):
    length = len(numbers)
    idx = 1

    while idx < length:
        if idx == 0:
            idx = 1

        # 左右の大小が正しければ、右にずれる
        if numbers[idx] > numbers[idx - 1]:
            idx += 1
        else:
            numbers[idx], numbers[idx - 1] = numbers[idx - 1], numbers[idx]
            idx -= 1

    return numbers


def insertion_sort(numbers: list):
    length = len(numbers)
    for i in range(1, length):
        while i > 0 and (numbers[i] < numbers[i - 1]):
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            i -= 1
    return numbers
