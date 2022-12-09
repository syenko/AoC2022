f = open("inputs/9.txt", "r")

lines = [i for i in f]

positions = {(0,0)}

posH = [0,0]
posT = (0,0)


def clamp(i, minV, maxV):
    return min(maxV, max(i, minV))


def updateT(posH, posT):
    dist = (-posH[0]+posT[0], -posH[1]+posT[1])

    if abs(dist[0]) <= 1 and abs(dist[1]) <= 1:
        print(f"NO MOVE: {posT}")
        return posT

    posT = (
        posT[0] - (0 if abs(dist[0]) <= 0 else clamp(dist[0], -1, 1)),
        posT[1] - (0 if abs(dist[1]) <= 0 else clamp(dist[1], -1, 1))
    )
    print(posT)
    positions.add(posT)

    return posT

for line in lines:
    parts = line.split(" ")
    movement = parts[0]
    steps = int(parts[1])

    print(f"H: {posH}")

    if movement == "D":
        for i in range(steps):
            posH[1] -= 1
            posT = updateT(posH, posT)
    elif movement == "U":
        for i in range(steps):
            posH[1] += 1
            posT = updateT(posH, posT)
    elif movement == "L":
        for i in range(steps):
            posH[0] -= 1
            posT = updateT(posH, posT)
    elif movement == "R":
        for i in range(steps):
            posH[0] += 1
            posT = updateT(posH, posT)

print(positions)

print(len(positions))