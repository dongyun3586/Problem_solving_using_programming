dp = {1: 1, 2: 1}
n = 40

for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

for i in range(1, 41):
    print(f'fibonacci({i:02d}) = {dp[i]:,}')
