animals = [
    ['호랑이', 2, 1],
    ['사자', 2, 1],
    ['얼룩말', 2, 1],
    ['물소', 3, 4],
    ['하마', 4, 3],
    ['기린', 5, 5],
    ['코끼리', 6, 6]
  ]

dp = [[0]*10 for _ in range(10)]
limit = 7
n = len(animals)

for i in range(1, n):
  for j in range(1, n):
    if dp
    dp[i][j]

    n1 = 0
    if w + animals[i][1] <= limit:
      n1 = animals[i][2] + go(i - 1, w + animals[i][1], limit)  # 포함
    n2 = dp[i][j]   # 미포함
    dp[i][w] = max(n1, n2)

