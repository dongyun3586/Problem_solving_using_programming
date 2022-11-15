N = int(input())    # 1 <= N <= 100

d = [[0] * 11 for _ in range(N+1)]

for i in range(1, 10):
  d[1][i] = 1

for i in range(2, N+1):
  d[i][0] = d[i-1][1]
  for j in range(1, 10):
    d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % 1000000000

sum  = 0
for i in range(10):
  sum += d[N][i]

print(sum % 1000000000)