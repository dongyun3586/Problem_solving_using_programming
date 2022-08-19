import random

total_lotto = []
count = 0

print("** 로또 번호 생성을 시작합니다. **")
count = int(input('몇 번을 뽑을까요?'))

for _ in range(count):
    lotto = []
    while True:
        pick_num = random.randint(1, 45)
        if pick_num not in lotto:
            lotto.append(pick_num)
        if len(lotto) >= 6:
            break
    total_lotto.append(lotto)

for lotto in total_lotto:
    lotto.sort()
    print('자동번호-->', end=' ')
    for i in range(6):
        print(f"{lotto[i]:2d}", end=' ')
    print()