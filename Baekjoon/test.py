def print_matrix(graph):
  n = len(graph)
  for i in range(1, n):
    for j in range(1, n):
      print(graph[i][j], end=' ')
    print()


def dfs(graph, v):
  visited[v] = True
  print(v, end=' ')
  for i in range(len(graph)):
    if graph[v][i] and (not visited[i]):
      dfs(graph, i)


vertices = list(range(1, 8))
n = len(vertices) + 1
graph = [[0] * n for _ in range(n)]

edges = [(1, 2), (1, 3), (2, 3), (3, 5), (3, 6), (4, 5), (5, 7), (6, 7)]
visited = [False] * len(edges)

for v, u in edges:
  graph[v][u] = graph[u][v] = 1

# print_matrix(graph)
dfs(graph, 3)