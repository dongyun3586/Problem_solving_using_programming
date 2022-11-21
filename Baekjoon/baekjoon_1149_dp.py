n = int(input())
rgb_costs = [0, 0, 0]
for i in range(n):
    r, g, b = map(int, input().split())
    rgb_costs = [
        min(rgb_costs[1], rgb_costs[2]) + r,
        min(rgb_costs[0], rgb_costs[2]) + g,
        min(rgb_costs[0], rgb_costs[1]) + b]

print(min(rgb_costs))

'''
만약 sys.stdin.readlines() 사용하고 싶으시다면 제일 앞에
from sys import stdin
input = lambda: stdin.readlines().strip() # 내가 하면 오버라이딩 남이 하면 '이게맞나'

넣어주시면 됩니다. 그럼 더 빨리될듯...
'''