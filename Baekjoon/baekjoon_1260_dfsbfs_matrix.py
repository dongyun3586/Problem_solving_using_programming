from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in range(len(graph)):
        if graph[v][i] and (not visited[i]):
            dfs(graph, i, visited)


def bfs(graph, start):
    queue = deque([start])
    visited = [False] * len(graph)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i, v in enumerate(graph[v]):
            if v and not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, [False] * len(graph))
print()
bfs(graph, v)