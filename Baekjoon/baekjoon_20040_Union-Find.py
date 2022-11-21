from typing import List
from sys import stdin
input = stdin.readline

# 부모 노드를 찾는 함수
def getParent(parent: List, x: int):
  if parent[x] == x:
    return x
  return getParent(parent, parent[x])

# 두 부모 노드를 합치는 함수
def unionParent(parent: List, a: int, b: int):
  a = getParent(parent, a)
  b = getParent(parent, b)

  # 부모를 합칠때는 더 작은 값으로 합친다.
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

# 같은 부모를 가지는지 확인
def findParent(parent: List, a, b):
  a = getParent(parent, a)
  b = getParent(parent, b)
  return 1 if a == b else 0

# 본문 코드
n, m = map(int, input().split())

parent = list(range(n))
result = 0

for i in range(m):
  a, b = map(int, input().split())
  if findParent(parent, a, b) and result == 0:
    result = i + 1
  unionParent(parent, a, b)

print(result)
