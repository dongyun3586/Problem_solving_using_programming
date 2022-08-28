import collections

class Poly:
    def __init__(self, term=None, coef=None):
        self.term = term if term else []
        self.coef = coef if term else []


def printPoly(name, poly):
    polyStr = f'{name} = '

    for i in range(len(poly.term)):
        term = poly.term[i]  # 항 차수
        coef = poly.coef[i]  # 계수

        if (coef >= 0):
            polyStr += "+"

        polyStr += str(coef) + "x^" + str(term) + " "
    print(polyStr)


def addSparsePoly(p1, p2):
    p3 = Poly()

    # 다항식 하나의 항이 없어질 때 까지 반복
    while p1.term and p2.term:
        if p1.term[0] > p2.term[0]:
            term = p1.term.pop(0)
            coef = p1.coef.pop(0)
        elif p1.term[0] < p2.term[0]:
            term = p2.term.pop(0)
            coef = p2.coef.pop(0)
        else:
            term = p1.term.pop(0)
            p2.term.pop(0)
            coef = p1.coef.pop(0) + p2.coef.pop(0)
        p3.term.append(term)
        p3.coef.append(coef)

    # 항이 남은 다항식 추가
    if p1.term:
        for _ in p1.term:
            p3.term.append(p1.term.pop(0))
            p3.coef.append(p1.coef.pop(0))
    if p2.term:
        for _ in p2.term:
            p3.term.append(p2.term.pop(0))
            p3.coef.append(p2.coef.pop(0))

    return p3


## 전역 변수 선언 부분 ##
p1 = Poly(term=[300, 20, 0], coef=[7, -4, 5])
p2 = Poly(term=[300, 50, 0], coef=[2, -8, 5])

## 메인 코드 부분 ##
if __name__ == "__main__":
    printPoly("p1", p1)
    printPoly("p2", p2)
    p3 = addSparsePoly(p1, p2)
    printPoly("p3", p3)