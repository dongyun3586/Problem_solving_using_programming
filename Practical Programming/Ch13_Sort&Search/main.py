from typing import Any


def binary_search(L: list, target: Any, start: int, end: int) -> Any:
    if start == end + 1:
        if 0 <= end and L[end] == target:
            return end
        else:
            return -1

    mid = (start + end) // 2
    if L[mid] > target:
        return binary_search(L, target, start, mid - 1)
    else:
        return binary_search(L, target, mid + 1, end)


if __name__ == "__main__":
  arr =  [1, 2, 2, 2, 10, 10, 10, 10]
print(binary_search(arr, 2, 0, len(arr)-1))