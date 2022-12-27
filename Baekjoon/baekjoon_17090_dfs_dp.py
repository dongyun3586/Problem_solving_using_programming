import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(n)]
check = [[-1] * m for _ in range(n)]
dir = {'U': [0, -1], 'R': [1, 0], 'D': [0, 1], 'L': [-1, 0]}

def dfs(x, y):
    dx, dy = dir[maze[y][x]]
    x = x + dx
    y = y + dy

    if x<0 or x>=m or y<0 or y>=n:
        return 1
    if check[y][x] == 1:
        return 1

    if check[y][x] == -1:     # 검사 전
        check[y][x] = 0
        check[y][x] = dfs(x, y)
        return check[y][x]
    if check[y][x] == 0:
        return 0

escape = 0
for y in range(n):
    for x in range(m):
        check[y][x] = dfs(x, y)
        escape += check[y][x]
print(escape)