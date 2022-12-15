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
# lineCheck = 10
lineCheck = 2000000
X = 0
Y = 1
DIST = 2

for sensor in sensors:
    if abs(lineCheck - sensor[Y]) < sensor[DIST]:
        bounds = sensor[DIST] - abs(lineCheck - sensor[Y])
        for i in range(sensor[X] - bounds, sensor[X] + bounds + 1):
            linePos.add(i)

for beacon in beacons:
    if beacon[Y] == lineCheck:
        if beacon[X] in linePos:
            linePos.remove(beacon[X])

print(len(linePos))
