# 재귀를 제거한 recur() 함수
def recur1(n: int) -> int:
  if n>0:
    recur1(n-1)
    print(n, end=' ')
    recur1(n-2)

recur1(5)
print()

# recur(n-2)의 꼬리 재귀를 제거하기 위해
# n값을 n-2시키고 함수의 시작 지점으로 돌아간다.
def recur2(n: int) -> int:
  while n>0:
    recur2(n-1)
    print(n, end=' ')
    n -= 2

recur2(5)
print()

def recur3(n: int) -> int:
  s = []
  while True:
    if n>0:
      s.append(n)
      n-=1
      continue
    if s:
      n = s.pop()
      print(n, end=' ')
      n-=2
      continue
    break

recur3(5)