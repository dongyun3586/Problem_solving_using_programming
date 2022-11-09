def dfs(x, y):
  # 주어진 범위를 벗어나는 경우 return False
  if x <= -1 or x >= n or y <= -1 or y >= n:
    return 0

  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 1:
    # 해당 노드 방문 처리
    graph[x][y] = 0
    # 상, 하, 좌, 우의 위치 모두 재귀적으로 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return 1
  return 0

n = int(input())

# 2차원 리스트로 맵 정보 입력 받기
graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤, 이와 연결된 모든 노드 방문
count = 0

for i in range(n):
  for j in range(n):
    # 현재 위치에서 DFS 수행
    if dfs(i, j):
      count += 1

print(count)