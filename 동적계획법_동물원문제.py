def choose_animals(animals, payload_limit):  #  W: 트럭의 무게한도, wt: 각 동물의 무게, val: 각 동물의 가치, n: 동물의 수
  n = len(animals)
  # K = [[0 for x in range(payload_limit+1)] for x in range(n+1)]      # DP를 위한 2차원 리스트 초기화
  K = [[0] * (payload_limit + 1) for i in range(n + 1)]
  names = [[[] for x in range(payload_limit + 1)] for x in range(n + 1)]  # 동물 이름 저장 2차원 리스트 초기화
  for i in range(n + 1):  # 동물 숫자만큼 반복
    for w in range(payload_limit + 1):  # 트럭의 무게한도만큼 반복
      if i == 0 or w == 0:  # 0번째 행/열은 0으로 세팅
        K[i][w] = 0
      elif animals[i - 1][1] <= w:  # 현재 동물을 싣는 것이 가능하면
        # K[i-1][w]: 이전 동물의 가치
        # animals[i-1][2]+K[i-1][w-animals[i-1][1]]: 현재동물의가치+이전 데이터 중(트럭하중-현재동물무게)
        # K[i][w] = max(animals[i-1][2] + K[i-1][w-animals[i-1][1]], K[i-1][w])    # max 함수 사용하여 큰 것 선택
        if animals[i - 1][2] + K[i - 1][w - animals[i - 1][1]] > K[i - 1][w]:
          K[i][w] = animals[i - 1][2] + K[i - 1][w - animals[i - 1][1]]
          names[i][w].append(animals[i - 1][0])
          if K[i - 1][w - animals[i - 1][1]]:
            # names[i][w].append(names[i-1][w-animals[i-1][1]])
            names[i][w] = names[i][w] + names[i - 1][w - animals[i - 1][1]]
        else:
          K[i][w] = K[i - 1][w]
          # names[i][w].append(names[i-1][w])
          names[i][w] = names[i][w] + names[i - 1][w]
      else:
        K[i][w] = K[i - 1][w]
        if K[i - 1][w]:
          # names[i][w].append(names[i-1][w])
          names[i][w] = names[i][w] + names[i - 1][w]

  # print('   ', end='')
  # for i in range(n+1):
  #   print(i, end='  ')
  # print()
  # for i, v in enumerate(K):
  #   print(i, v)
  # print()
  # for i in names:
  #   print(i)

  return K[n][payload_limit], names[n][payload_limit]


animals = [
  ['호랑이', 2, 1], ['사자', 2, 1], ['얼룩말', 2, 1], ['물소', 3, 4],
  ['하마', 4, 3], ['기린', 5, 5], ['코끼리', 6, 6]
  ]

truck_payload_limit = 7  # 트럭의 무게 한도
preference_sum, selected_animals = choose_animals(animals, truck_payload_limit)
print('선호도 합: ', preference_sum)
print('선택된 동물들: ', selected_animals)