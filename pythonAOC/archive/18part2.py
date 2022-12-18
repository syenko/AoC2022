from collections import Counter
import sys

sys.setrecursionlimit(5000) # inefficient solutions wooo

f = open("inputs/18.txt", "r")

lines = [x.strip() for x in f]

blocks = []

MAX_VAL = 1000000000000

maxX = 0
maxY = 0
maxZ = 0

minX = MAX_VAL
minY = MAX_VAL
minZ = MAX_VAL

for line in lines:
    (x, y, z) = line.split(",")
    x = int(x)
    y = int(y)
    z = int(z)

    maxX = max(x, maxX)
    maxY = max(y, maxY)
    maxZ = max(z, maxZ)

    minX = min(x, minX)
    minY = min(y, minY)
    minZ = min(z, minZ)

    blocks.append((x, y, z))

air = []

surfaceArea = 0
for a in blocks:
    x = a[0]
    y = a[1]
    z = a[2]

    pointsToCheck = [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]
    for point in pointsToCheck:
        if point not in blocks:
            surfaceArea += 1
            air.append(point)

counts = Counter(air)
air = set(air)

visited = set()

FAIL = -1
SUCCESS = 1

print(f"x: {maxX}, {minX}, y: {maxY}, {minY}, z: {maxZ}, {minZ}")

bad = set()
pastValues = set()


def checkAirBlock(airBlock, visited, component, recur):
    if airBlock in visited:
        return 0
    visited.add(airBlock)

    # print(recur)

    x = airBlock[0]
    y = airBlock[1]
    z = airBlock[2]

    if x > maxX or x < minX or y > maxY or y < minY or z > maxZ or z < minZ:
        if airBlock in air:
            bad.add(airBlock)
        # print(x, y, z)
        return FAIL
    elif airBlock in blocks:
        return SUCCESS

    component.add(airBlock)

    result = 0

    pointsToCheck = [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]

    for point in pointsToCheck:
        if point not in visited:
            result = min(checkAirBlock(point, visited, component, recur + 1), result)

    if result != FAIL:
        return SUCCESS
    else:
        return FAIL

for airBlock in air:
    if airBlock not in visited:
        component = {airBlock}
        if checkAirBlock(airBlock, visited, component, 0) == SUCCESS:
            print("SUCCESS")
            # sa = findSurfaceArea(component)
            # print(f"component: {component} sa: {sa}")
            # surfaceArea = surfaceArea - sa

            for x in component:
                surfaceArea -= counts[x]
                if x in pastValues:
                    print("AHHHH")
                pastValues.add(x)

            print(surfaceArea)
        else:
            print("FAILED")

print(len(pastValues), len(air))

print(surfaceArea)
