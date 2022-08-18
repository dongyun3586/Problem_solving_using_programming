# Iterator 사용
import random


class LottoIterator:
    def __init__(self):
        self.data = list(range(1, 46))

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.data) < 1:
            raise StopIteration
        result = self.data.pop(random.randint(0, len(self.data)))
        return result


my_lotto = LottoIterator()
for i in my_lotto:
    print(i)

# data = list(range(1, 46))
# for _ in range(5):
#     print(data.pop(random.randint(0, len(data))))
