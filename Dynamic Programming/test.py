animals = [
    ['호랑이', 2, 1],
    ['사자', 2, 1],
    ['얼룩말', 2, 1],
    ['물소', 3, 4],
    ['하마', 4, 3],
    ['기린', 5, 5],
    ['코끼리', 6, 6]
  ]

def go(i, w, limit):
    # 종료 조건
    if i < 0:
        return 0

    n1 = 0
    if w+animals[i][1] <= limit:
        n1 = animals[i][2] + go(i-1, w+animals[i][1], limit)   # 포함
    n2 = 0 + go(i-1, w+0, limit)                               # 미포함
    return max(n1, n2)

result = go(len(animals)-1, 0, 7)
print(result)