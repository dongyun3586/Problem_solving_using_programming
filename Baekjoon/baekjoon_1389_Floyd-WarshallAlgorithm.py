from math import inf

n, m = map(int, input().split())
weight = [[inf] * n for _ in range(n)]

# 가중치 인접행렬 구성
for i in range(n):
    a, b = map(int, input().split())
    weight[a-1][b-1] = 1
    weight[b-1][a-1] = 1

# k = 거쳐가는 노드, v = 출발 노드, w = 도착 노드
for k in range(n):
    weight[k][k] = 0
    for v in range(n):
        for w in range(n):
            weight[v][w] = min(weight[v][w], weight[v][k] + weight[k][w])

row_sum = inf
min_index = 0
for i in range(n):
    kb = sum(weight[i])
    if kb < row_sum:
        row_sum = kb
        min_index = i

print(min_index + 1)

