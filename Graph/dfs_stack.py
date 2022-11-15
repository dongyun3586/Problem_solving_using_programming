def dfs(graph, v):
  visited = [False] * 9  # 각 노드가 방문된 정보를 리스트 자료형으로 표현
  stack = [v]
  visited[v] = True  # 현재 노드를 방문 처리
  print(v, end=' ')

  while stack:
    flag = True
    for node in graph[stack[-1]]:
      if not visited[node]:
        flag = False
        stack.append(node)
        visited[node] = True
        print(node, end=' ')
        break
    if flag:
      stack.pop()

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 정의된 DFS 함수 호출
dfs(graph, 3)