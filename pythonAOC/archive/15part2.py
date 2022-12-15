import functools

f = open("inputs/15.txt", "r")

lines = [x.strip() for x in f]


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


sensors = []
beacons = []

for line in lines:
    parts = line.split(" ")
    sensorX = int(parts[2][:-1].split("=")[1])
    sensorY = int(parts[3][:-1].split("=")[1])
    beaconX = int(parts[8][:-1].split("=")[1])
    beaconY = int(parts[9].split("=")[1])

    minDist = dist(sensorX, sensorY, beaconX, beaconY)

    sensors.append((sensorX, sensorY, minDist))
    beacons.append((beaconX, beaconY))

linePos = set()
size = 4000000
# size = 20
size += 1

X = 0
Y = 1
DIST = 2

checkSet = {x for x in range(size)}

lines = {}

count = 0

for sensor in sensors:
    print(count)
    for lineCheck in range(max(0, sensor[Y] - sensor[DIST]), min(size, sensor[Y] + sensor[DIST] + 1)):
        if lineCheck in lines.keys():
            linePos = lines[lineCheck]
        else:
            linePos = []
        bounds = sensor[DIST] - abs(lineCheck - sensor[Y])
        linePos.append((max(0, sensor[X] - bounds), min(size, sensor[X] + bounds)))

        lines[lineCheck] = linePos
    count += 1

print("DONE ADDING")


def sortFunc(a, b):
    if a[0] == b[0]:
        if a[1] < b[1]:
            return -1
        elif a[1] == b[1]:
            return 0
        else:
            return 1
    elif a[0] < b[0]:
        return -1
    else:
        return 1


for (key, linePos) in lines.items():
    linePos.sort(key=functools.cmp_to_key(sortFunc))
    maxX = 0
    for i in range(len(linePos) - 1):
        maxX = max(maxX, linePos[i][1])
        if maxX < linePos[i + 1][0] - 1:
            print((linePos[i][1] + 1) * 4000000 + key)

print("DONE")
