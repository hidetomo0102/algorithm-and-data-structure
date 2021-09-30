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


def bucket_sort(numbers: list):
    max_num = max(numbers)
    length = len(numbers)
    size = max_num // length

    # バケット分だけリストを作成
    buckets = [[] for _ in range(size)]
    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[i - 1].append(num)

    result = []
    for j in range(size):
        # 各バケットに対してInsertionSort
        insertion_sort(buckets[j])
        result += buckets[j]

    return result


def shell_sort(numbers: list):
    length = len(numbers)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            # 入れ替えた数字はgapごとに左端まで比較
            while i >= gap:
                if numbers[i] < numbers[i - gap]:
                    numbers[i], numbers[i - gap] = numbers[i - gap], numbers[i]
                i -= gap
        gap //= 2

    return numbers


def counting_sort(numbers: list):
    max_num = max(numbers)
    counts = [0] * (max_num + 1)
    result = [0] * len(numbers)

    for num in numbers:
        counts[num] += 1
    # 各インデックスの累積和を取る（前から何番目にあるのか）
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    j = len(numbers) - 1
    while j >= 0:
        idx = numbers[j]
        result[counts[idx]] = numbers[j]
        j -= 1

    return result


def radix_sort(numbers: list):
    def _counting_sort(numbers: list, place: int):
        counts = [0] * 10
        result = [0] * len(numbers)

        for num in numbers:
            index = int(num / place) % 10
            counts[index] += 1

        for i in range(1, 10):
            counts[i] += counts[i - 1]

        j = len(numbers) - 1
        while j >= 0:
            idx = int(numbers[j] / place) % 10
            result[counts[idx] - 1] = numbers[j]
            counts[idx] -= 1
            j -= 1

        return result

    max_num = max(numbers)
    place = 1
    while max_num > place:
        numbers = _counting_sort(numbers, place)
        place *= 10

    return numbers
