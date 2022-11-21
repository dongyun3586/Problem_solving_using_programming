from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  p, c = map(int, input().split())
  graph[p].append(c)
  graph[c].append(p)

def bfs(graph, start, target):
  queue = deque([start])
  visited = [0] * len(graph)

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = visited[v] + 1

  return visited[target] if visited[target] > 0 else -1

print(bfs(graph, a, b))