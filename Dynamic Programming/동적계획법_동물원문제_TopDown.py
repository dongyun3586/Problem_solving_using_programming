class Animal:
  def __init__(self, name, weight, value):
    self.name = name
    self.weight = weight
    self.value = value


animals = [
  Animal('호랑이', 2, 1), Animal('사자', 2, 1), Animal('얼룩말', 2, 1),
  Animal('물소', 3, 4), Animal('하마', 4, 3), Animal('기린', 5, 5),
  Animal('코끼리', 6, 6)
  ]

n = len(animals) - 1
truck_payload_limit = 7  # 트럭의 무게 한도
dp = [[0] * (truck_payload_limit + 1) for _ in range(n + 1)]   # DP를 위한 2차원 리스트 초기화


def choose_animals(num, payload_limit):
  print(f'choose_animals({num}, {payload_limit})')
  # 종료 조건
  if num < 1 or payload_limit < 1:
    return 0
  if payload_limit == animals[num].weight:
    return animals[num].value

  # dp 테이블에 계산 결과가 있으면 반환
  if dp[num][payload_limit] != 0:
    return dp[num][payload_limit]

  # dp 테이블에 걔산 결과가 없으면 계산하여 dp 테이블에 저장
  result = max(choose_animals(num-1, payload_limit),
                               choose_animals(num-1, payload_limit - animals[num].weight) + animals[num].value)
  if result <= 7:
    dp[num][payload_limit] = result
  return dp[num][payload_limit]


if __name__=='__main__':
  preference_sum = choose_animals(n, truck_payload_limit)
  print('선호도 합: ', preference_sum)
  # print('선택된 동물들: ', selected_animals)