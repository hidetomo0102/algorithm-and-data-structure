def binary_search(numbers: list, value: int) -> int:
    """
    目的値のインデックスを返す
    """
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def recursive_binary_search(numbers: list, value: int) -> int:
    def _binary_search(numbers: list, value: int, left: int, right: int) -> int:
        if left <= right:
            return -1
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid + 1, right)
        else:
            return _binary_search(numbers, value, left, mid - 1)

    return _binary_search(numbers, value, 0, len(numbers) - 1)
