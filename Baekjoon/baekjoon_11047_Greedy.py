n, k = map(int, input().split())
coins = []

for i in range(n):
  coins.append(int(input()))

total = 0

for i in range(len(coins)-1, -1, -1):
  if k >= coins[i]:
    count = k // coins[i]
    total += count
    k -= coins[i] * count
  if k == 0:
    break

print(total)