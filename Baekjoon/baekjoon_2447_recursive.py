n = int(input())

def returnline(n):
    if n == 1:
        return '*'

    s = returnline(n / 3)
    linelist = []

    for line in s:
        linelist.append(line * 3)
    for line in s:
        linelist.append(line + ' ' * len(s) + line)
    for line in s:
        linelist.append(line * 3)

    return linelist


for line in returnline(n):
    print(line)