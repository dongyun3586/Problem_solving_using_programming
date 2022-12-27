import collections

n, m = map(int, input().split())
list1 = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
lista = collections.deque()
day = 0
check = False


def bfs(a, b):
  lista.append((a, b))
  while lista:
    x, y = lista.popleft()
    visit[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if list1[nx][ny] != 0 and visit[nx][ny] == False:
          visit[nx][ny] = True
          lista.append((nx, ny))
        elif list1[nx][ny] == 0:
          count[x][y] += 1
  return 1


while True:
  visit = [[False] * m for _ in range(n)]
  count = [[0] * m for _ in range(n)]
  result = []
  for i in range(n):
    for j in range(m):
      if list1[i][j] != 0 and visit[i][j] == False:
        result.append(bfs(i, j))

  for i in range(n):
    for j in range(m):
      list1[i][j] -= count[i][j]
      if list1[i][j] < 0:
        list1[i][j] = 0

  if len(result) == 0:
    break
  if len(result) >= 2:
    check = True
    break
  day += 1

if check:
  print(day)
else:
  print(0)