import pprint

n, m = map(int, input().split())

m += 1
INF = 9
weight = [[INF] * m for _ in range(m)]

# 가중치 인접행렬 구성
for i in range(1, m):
    a, b = map(int, input().split())
    weight[a][b] = weight[b][a] = 1

# pprint.pprint(weight)

def floydWarshall(g):
    step = -1

    for k in range(1, m):          # k = 거쳐가는 노드
        for v in range(1, m):      # v = 출발 노드
            for w in range(1, m):  # w = 도착 노드
                if g[v][k] + g[k][w] < g[v][w]:
                    g[v][w] = g[v][k] + g[k][w]
        pprint.pprint(weight)
        print()

floydWarshall(weight)



