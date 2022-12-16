f = open("inputs/16.txt", "r")

lines = [x.strip() for x in f]

valvesGraph = {}
rates = {}
valves = []
allDists = {}

start = "AA"
MAX_VAL = 10000000000

for line in lines:
    parts = line.split(" ")
    valve = parts[1]
    rate = parts[4][:-1].split("=")[1]

    if "valves" in line:
        nextValves = line.split("valves ")[1].split(", ")
    elif "valve" in line:
        nextValves = line.split("valve ")[1].split(", ")

    valves.append(valve)
    valvesGraph[valve] = nextValves
    rates[valve] = int(rate)

# create distance map for a specified start node
def calcDists(start):
    visited = {}
    dist = {}
    for valve in valves:
        visited[valve] = False
        dist[valve] = MAX_VAL

    dist[start] = 0
    toSearch = [start]
    time = 30

    while len(toSearch) != 0:
        top = toSearch.pop(0)
        for point in valvesGraph[top]:
            dist[point] = min(dist[point], dist[top] + 1)
            if not visited[point]:
                visited[point] = True
                toSearch.append(point)

    allDists[start] = dist

for valve in valves:
    calcDists(valve)

importantValves = [] # only valves with rates > 0
for i in valves:
    if rates[i] > 0:
        importantValves.append(i)

checkNext = [
    # [time, flowRate, total, curNode, unvisited, pastValves]
    [30, 0, 0, start, importantValves, [start]]
]
TIME = 0
FLOW_RATE = 1
TOTAL = 2
CUR_NODE = 3
UNVISITED = 4
PAST = 5

ans = 0
while len(checkNext) > 0:
    top = checkNext.pop()
    if top[TIME] <= 0:
        if top[TOTAL] > ans:
            print(f"{top[TOTAL]} ::: {top[PAST]}")
        ans = max(top[TOTAL], ans)
        continue

    foundMove = False
    for closedValve in top[UNVISITED]:
        timeToNext = allDists[top[CUR_NODE]][closedValve] + 1
        if timeToNext < top[TIME]:
            unvisited = top[UNVISITED][:]
            past = top[PAST][:]
            past.append(closedValve)
            unvisited.remove(closedValve)
            checkNext.append([
                top[TIME] - timeToNext,
                top[FLOW_RATE] + rates[closedValve],
                top[TOTAL] + timeToNext*top[FLOW_RATE],
                closedValve,
                unvisited,
                past
            ])
            foundMove = True

    if not foundMove:
        if top[TOTAL] + top[FLOW_RATE]*top[TIME] > ans:
            print(f"ran out {top[TOTAL] + top[FLOW_RATE]*top[TIME]} ::: {top[PAST]}")
        ans = max(top[TOTAL] + top[FLOW_RATE]*top[TIME], ans)

print(ans)