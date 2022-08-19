import random

# Generator 로또 번호 생성기
def lotto_numbers_generator():
    while True:
        yield random.sample(range(1, 46), 6)
print("** 로또 번호 생성을 시작합니다. **")
count = int(input('몇 번을 뽑을까요?'))

my_lotto = lotto_numbers_generator()
for i, _ in enumerate(range(count)):
    lotto_number = next(my_lotto)
    lotto_number.sort()
    print(f"{i+1:3d}", lotto_number)
