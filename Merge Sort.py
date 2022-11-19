def merge(arr, l, m, r):
    print(f'merge(arr, {l}, {m}, {r})')
    n1 = m - l + 1
    n2 = r - m
    L = [arr[l + i] for i in range(0, n1)]
    R = [arr[m + 1 + i] for i in range(0, n2)]

    i = j = 0   # Initial index of first and second subarray
    k = l       # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    print(f'mergeSort(arr, {l}, {r})')
    if l < r:
        m = (l + r) // 2            # middle
        print(f'm={m}', end=' ')
        mergeSort(arr, l, m)        # 왼쪽 부분 집합을 2개로 분할
        print(f'm={m}', end=' ')
        mergeSort(arr, m + 1, r)    # 오른쪽 부분 집합을 2개로 분할
        merge(arr, l, m, r)         # 부분 집합 2개를 하나로 합침


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전  :', arr)
mergeSort(arr, 0, len(arr) - 1)
print('정렬 후  :', arr)