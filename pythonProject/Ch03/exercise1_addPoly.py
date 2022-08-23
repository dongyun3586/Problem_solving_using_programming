from ex01_polynomial import printPoly

def addPoly(a, b):
    # 최고차수
    c = list()
    index_a = 0
    index_b = 0
    degree_a = len(a) - 1
    degree_b = len(b) - 1
    d_a = degree_a
    d_b = degree_b

    while index_a <= degree_a and index_b <= degree_b:
        if(d_a > d_b):
            c.append(a[index_a])
            index_a += 1
            d_a -= 1
        elif d_a == d_b:
            c.append(a[index_a] + b[index_b])
            index_a += 1
            index_b += 1
            d_a -= 1
            d_b -= 1
        else:
            c.append(b[index_b])
            index_b += 1
            d_b -= 1

    return c

if __name__ == "__main__":
    poly_a = [4, 3, 5, 0]
    poly_b = [3, 1, 0, 2, 1]

    poly_c = addPoly(poly_a, poly_b)

    print(printPoly(poly_a))
    print(printPoly(poly_b))
    print(printPoly(poly_c))