# 피보나치 수열 memorization 기법
dp = {1: 1, 2: 1}
count = 0

def fibonacci(n):
    global count
    count += 1
    if n in dp:
        return dp[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dp[n] = output
        return output

print(f'fibonacci({40:02d}) = {fibonacci(40):,}')

# for i in range(1, 40):
#     count = 0
#     print(f'fibonacci({i:2d}) = {fibonacci(i):2d}, count = {count:,}')

print(dp)
