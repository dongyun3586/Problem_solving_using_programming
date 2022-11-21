from collections import deque

def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    graph[y][x] = 0
    count = 1

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1:
                queue.append((nx, ny))
                graph[ny][nx] = 0
                count += 1
    return count


n = int(input())
apartment = []
number = []
for _ in range(n):
    apartment.append(list(map(int, input())))

for y in range(n):
    for x in range(n):
        if apartment[y][x] == 1:
            number.append(bfs(apartment, x, y))

number.sort()
print(len(number))
for i in number:
    print(i)