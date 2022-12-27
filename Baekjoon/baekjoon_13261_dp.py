import sys

MAXL, MAXG, MAXC = 8000, 800, 1000000000
dp, prefix = [[sys.maxsize] * (MAXL + 1) for _ in range(MAXG + 1)], [0] * (MAXL + 1)

def dcopt(s, f, finds, findf, lv):
  global dp
  global prefix

  if (s > f):
    return
  m = (s + f) // 2

  for i in range(finds, min(findf + 1, m)):
    if dp[lv][m] > dp[lv - 1][i] + (prefix[m] - prefix[i]) * (m - i):
      dp[lv][m] = dp[lv - 1][i] + (prefix[m] - prefix[i]) * (m - i)
      opt = i
  dcopt(s, m - 1, finds, opt, lv)
  dcopt(m + 1, f, opt, findf, lv)


L, G = map(int, sys.stdin.readline().split())

if (L < G):
  G = L

danger = list(map(int, sys.stdin.readline().split()))

prefix[0] = danger[0]

for i in range(1, L):
  prefix[i] = prefix[i - 1] + danger[i]

for i in range(0, L):
  dp[0][i] = (i + 1) * prefix[i]

for i in range(1, G):
  dcopt(i, L - 1, 0, L - 1, i)

print(dp[G - 1][L - 1])