import time
import sys

def elapsed(func):
  def inner_func(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"함수 수행시간: {end-start}초")
    return result
  return inner_func

@elapsed
def my_func(a: int , b: int):
  sum = 0
  for i in range(a, b + 1):
    sum += i
  return sum

a, b = map(int, input().split())
print(my_func(a, b))

