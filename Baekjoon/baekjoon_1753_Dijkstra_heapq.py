from sys import stdin

input = stdin.readline
import heapq

INF = 1000000
V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
d = [INF] * (V + 1)
heap = []


def dijkstra(start):
  d[start] = 0
  heapq.heappush(heap, [0, start])

  while heap:
    weight, node = heapq.heappop(heap)
    if d[node] < weight:
      continue
    for next_node, wei in graph[node]:
      next_weight = weight + wei
      if next_weight < d[next_node]:
        d[next_node] = next_weight
        heapq.heappush(heap, [next_weight, next_node])


for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append([v, w])

dijkstra(start)

for i in range(1, V + 1):
  if d[i] == INF:
    print("INF")
  else:
    print(d[i])