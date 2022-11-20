n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * len(graph)


def dfs(graph, v):
    visited[v] = True
    # print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)


dfs(graph, 1)
print(sum(visited)-1)
