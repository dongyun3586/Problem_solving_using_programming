# 피보나치 수열 => 함수 호출 횟수 세기
def fibonacci(n):
    global count
    count += 1
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 40):
    count = 0
    print(f'fibonacci({i:2d}) = {fibonacci(i):2d}, count = {count:,}')