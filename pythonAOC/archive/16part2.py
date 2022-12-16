from dataclasses import dataclass

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

@dataclass
class Snapshot:
    # time: int
    elephantTime: int
    personTime: int
    flowRate: int
    total: int
    eleNode: str
    personNode: str
    unvisited: list
    elePastValues: list
    personPastValues: list


checkNext = [
    Snapshot(
        # time=0,
        elephantTime=26,
        personTime=26,
        flowRate=0,
        total=0,
        eleNode=start,
        personNode=start,
        unvisited=importantValves,
        elePastValues=[start],
        personPastValues=[start]
    )
]

ans = 0
while len(checkNext) > 0:
    top = checkNext.pop()
    if top.personTime <= 0 and top.elephantTime <= 0:
        if top.total > ans:
            print(f"{top.total} ::: \nELE: {top.elePastValues} \nPER: {top.personPastValues}")
        ans = max(top.total, ans)
        continue

    foundMove = False
    # print(top)
    for closedValve in top.unvisited:
        # move elephant
        if top.elephantTime > top.personTime:
            timeToNext = allDists[top.eleNode][closedValve] + 1
            if timeToNext < top.elephantTime:
                unvisited = top.unvisited[:]
                past = top.elePastValues[:]
                past.append(closedValve)
                unvisited.remove(closedValve)
                checkNext.append(Snapshot(
                    elephantTime=top.elephantTime - timeToNext,
                    personTime=top.personTime,
                    flowRate=top.flowRate + rates[closedValve],
                    total=top.total - (top.personTime - (top.elephantTime - timeToNext)) * rates[closedValve],
                    eleNode=closedValve,
                    personNode=top.personNode,
                    unvisited=unvisited,
                    elePastValues=past,
                    personPastValues=top.personPastValues
                ))
                foundMove = True
        # move person (always goes first)
        else:
            timeToNext = allDists[top.personNode][closedValve] + 1
            if timeToNext < top.personTime:
                unvisited = top.unvisited[:]
                past = top.personPastValues[:]
                past.append(closedValve)
                unvisited.remove(closedValve)
                checkNext.append(Snapshot(
                    elephantTime=top.elephantTime,
                    personTime=top.personTime - timeToNext,
                    flowRate=top.flowRate + rates[closedValve],
                    total=top.total + timeToNext * top.flowRate,
                    eleNode=top.eleNode,
                    personNode=closedValve,
                    unvisited=unvisited,
                    personPastValues=past,
                    elePastValues=top.elePastValues
                ))
                foundMove = True

    if not foundMove:
        # elephant has no more moves
        if top.elephantTime > top.personTime:
            checkNext.append(Snapshot(
                elephantTime=0,
                personTime=top.personTime,
                flowRate=top.flowRate,
                total=top.total,
                eleNode=top.eleNode,
                personNode=top.personNode,
                unvisited=top.unvisited,
                personPastValues=top.personPastValues,
                elePastValues=top.elePastValues
            ))
        # person has no more moves
        else:
            checkNext.append(Snapshot(
                elephantTime=top.elephantTime,
                personTime=0,
                flowRate=top.flowRate,
                total=top.total + top.flowRate*top.personTime,
                eleNode=top.eleNode,
                personNode=top.personNode,
                unvisited=top.unvisited,
                personPastValues=top.personPastValues,
                elePastValues=top.elePastValues
            ))
print(ans)