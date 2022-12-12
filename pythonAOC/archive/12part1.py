f = open("inputs/12.txt", "r")

lines = [x.strip() for x in f]

chars = [[c for c in line] for line in lines]

startPos = (-1, -1)
endPos = (-1, -1)

graph = {}
dist = {}
visited = {}

MAX_VAL = 10000000000

# find start and end
for i in range(len(chars)):
    for j in range(len(chars[i])):
        if chars[i][j] == "E":
            endPos = (i, j)
            chars[i][j] = "z"
        elif chars[i][j] == "S":
            startPos = (i, j)
            chars[i][j] = "a"


# going backwards checking
def initializeVertex(i, j):
    val = ord(chars[i][j])

    graph[(i, j)] = []
    dist[(i, j)] = MAX_VAL
    visited[(i, j)] = False

    if i > 0 and val - ord(chars[i - 1][j]) <= 1:
        graph[(i, j)].append((i - 1, j))

    if i < len(chars) - 1 and val - ord(chars[i + 1][j]) <= 1:
        graph[(i, j)].append((i + 1, j))

    if j > 0 and val - ord(chars[i][j - 1]) <= 1:
        graph[(i, j)].append((i, j - 1))

    if j < len(chars[i]) - 1 and val - ord(chars[i][j + 1]) <= 1:
        graph[(i, j)].append((i, j + 1))


# initialize all vertices
for i in range(len(chars)):
    for j in range(len(chars[i])):
        initializeVertex(i, j)

dist[endPos] = 0
toSearch = [endPos]
curDist = 0
# bfs?
while len(toSearch) != 0:
    top = toSearch.pop(0)
    for point in graph[top]:
        dist[point] = min(dist[point], dist[top] + 1)
        if not visited[point]:
            visited[point] = True
            toSearch.append(point)

print(dist[startPos])
