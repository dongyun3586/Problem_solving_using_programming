import sys

def knapsack(W, wt, val, n):  # W: 트럭의 무게한도, wt: 각 동물의 무게, val: 각 동물의 가치, n: 동물의 수
  K = [[0 for x in range(W+1)] for x in range(n+1)]   # DP를 위한 2차원 리스트 초기화
  for i in range(n+1):      # 동물 숫자만큼 반복
    for w in range(W+1):    # 트럭의 무게한도만큼 반복
      if i==0 or w==0:      # 0번째 행/열은 0으로 세팅
        K[i][w] = 0 
      elif wt[i-1] <= w:    # 현재 동물을 싣는 것이 가능하면
        # K[i-1][w]: 이전 동물의 가치
        # val[i-1] + K[i-1][w-wt[i-1]]: 현재동물의가치+이전 데이터 중(트럭하중-현재동물무게)
        K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])    # max 함수 사용하여 큰 것 선택
      else: 
        K[i][w] = K[i-1][w] 
  
  return K[n][W]

wt = []
val = []
animal_name = ['호랑이', '사지', '얼룩말', '물소', '하마', '기린', '코끼리']
N, K = map(int, sys.stdin.readline().strip().split()) # N 동물수, K 트럭의 무게 한도

# 동물 무게와 가치 입력받기
for _ in range(N):
  w, v = map(int, sys.stdin.readline().strip().split())
  wt.append(w)
  val.append(v)
print(knapsack(K, wt, val, N))