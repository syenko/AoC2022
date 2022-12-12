f = open("input.txt", "r")

lines = [x.strip() for x in f]

chars = [[c for c in line] for line in lines]

startPos = (-1, -1)
endPos = (-1, -1)

graph = {}
dist = {}
visited = {}

MAX_VAL = 10000000000

check = []

for i in range(len(chars)):
    for j in range(len(chars[i])):
        if chars[i][j] == "E":
            endPos = (i, j)
            chars[i][j] = "z"
        elif chars[i][j] == "S" or chars[i][j] == "a":
            startPos = (i, j)
            chars[i][j] = "a"

            check.append((i,j))

# going backwards checking
def checkNearest(i, j):
    val = ord(chars[i][j])

    graph[(i,j)] = []
    dist[(i, j)] = MAX_VAL
    visited[(i, j)] = False

    if i > 0 and val - ord(chars[i-1][j]) <= 1:
        graph[(i, j)].append((i-1, j))

    if i < len(chars)-1 and val - ord(chars[i + 1][j]) <= 1:
        graph[(i, j)].append((i + 1, j))

    if j > 0 and val - ord(chars[i][j-1]) <= 1:
        graph[(i, j)].append((i, j-1))

    if j < len(chars[i])-1 and val - ord(chars[i][j+1]) <= 1:
        graph[(i, j)].append((i, j+1))

for i in range(len(chars)):
    for j in range(len(chars[i])):
        checkNearest(i, j)

dist[endPos] =0

sptSet = set()

toSearch = [endPos]

for (key, val) in graph.items():
    print(f"{key} :: {val}")

curDist = 0
while len(toSearch) != 0:
    top = toSearch.pop(0)
    for point in graph[top]:
        # print(f"p {point} d {dist[top]}")
        dist[point] = min(dist[point], dist[top] + 1)
        if not visited[point]:
            visited[point] = True
            toSearch.append(point)

print(startPos)

ans = MAX_VAL

for pos in check:
    ans = min(dist[pos],ans)

print(ans)

