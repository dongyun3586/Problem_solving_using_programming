class Animal:
  def __init__(self, name, weight, value):
    self.name = name
    self.weight = weight
    self.value = value

def choose_animals(animals, payload_limit):
  n = len(animals)
  dp = [[0] * (payload_limit + 1) for _ in range(n + 1)]   # DP를 위한 2차원 리스트 초기화
  names = [[[] for _ in range(payload_limit + 1)] for _ in range(n + 1)]  # 동물 이름 저장 2차원 리스트 초기화
  for i in range(n + 1):  # 동물 숫자만큼 반복
    for w in range(payload_limit + 1):  # 트럭의 무게한도만큼 반복
      if i == 0 or w == 0:  # 0번째 행/열은 0으로 세팅
        dp[i][w] = 0
      elif animals[i - 1].weight <= w:  # 현재 동물을 싣는 것이 가능하면
        # K[i-1][w]: 이전 동물의 가치
        # animals[i-1][2]+K[i-1][w-animals[i-1][1]]: 현재동물의가치+이전 데이터 중(트럭하중-현재동물무게)
        # K[i][w] = max(animals[i-1][2] + K[i-1][w-animals[i-1][1]], K[i-1][w])    # max 함수 사용하여 큰 것 선택
        if animals[i - 1].value + dp[i - 1][w - animals[i - 1].weight] > dp[i - 1][w]:
          dp[i][w] = animals[i - 1].value + dp[i - 1][w - animals[i - 1].weight]
          names[i][w].append(animals[i - 1].name)
          if dp[i - 1][w - animals[i - 1].weight]:
            # names[i][w].append(names[i-1][w-animals[i-1][1]])
            names[i][w] = names[i][w] + names[i - 1][w - animals[i - 1].weight]
        else:
          dp[i][w] = dp[i - 1][w]
          # names[i][w].append(names[i-1][w])
          names[i][w] = names[i][w] + names[i - 1][w]
      else:
        dp[i][w] = dp[i - 1][w]
        if dp[i - 1][w]:
          # names[i][w].append(names[i-1][w])
          names[i][w] = names[i][w] + names[i - 1][w]
  return dp[n][payload_limit], names[n][payload_limit]


animals = [
  Animal('호랑이', 2, 1), Animal('사자', 2, 1), Animal('얼룩말', 2, 1),
  Animal('물소', 3, 4), Animal('하마', 4, 3), Animal('기린', 5, 5),
  Animal('코끼리', 6, 6)
  ]

truck_payload_limit = 7  # 트럭의 무게 한도
preference_sum, selected_animals = choose_animals(animals, truck_payload_limit)
print('선호도 합: ', preference_sum)
print('선택된 동물들: ', selected_animals)