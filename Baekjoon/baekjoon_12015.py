import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

max = nums[0]
count = 1
for i in nums[1:]:
  if max < i:
    max = i
    count += 1

print(count)