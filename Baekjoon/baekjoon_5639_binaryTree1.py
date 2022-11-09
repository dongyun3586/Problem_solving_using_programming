import sys
sys.setrecursionlimit(10 ** 5)

arr = []

# 더 이상 값이 없을 때까지 입력받기
while True:
    try:
        a = int(input())
    except:
        break
    arr.append(a)

# 후위순회
def post_order(start, end):
    print(f'post_order({start}, {end})')
    if start > end:
        return

    s = arr[start]
    div = end + 1
    for i in range(start + 1, end + 1):
        if s < arr[i]:
            div = i
            break

    post_order(start + 1, div - 1)
    post_order(div, end)
    print(arr[start])


post_order(0, len(arr)-1)