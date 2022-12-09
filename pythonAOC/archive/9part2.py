f = open("inputs/9.txt", "r")

lines = [i for i in f]

positions = {(0,0)}

posH = [0,0]
knots = []

for i in range(10):
    knots.append([0,0])

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
    # print(posT)
    # positions.add(posT)

    return [posT[0], posT[1]]

def update():
    for j in range(1, len(knots)):
        knots[j] = updateT(knots[j - 1], knots[j])

    positions.add((knots[9][0], knots[9][1]))

for line in lines:
    parts = line.split(" ")
    movement = parts[0]
    steps = int(parts[1])

    posH = knots[0]

    print(f"H: {posH}")

    if movement == "D":
        for i in range(steps):
            posH[1] -= 1
            update()
    elif movement == "U":
        for i in range(steps):
            posH[1] += 1
            update()
    elif movement == "L":
        for i in range(steps):
            posH[0] -= 1
            update()
    elif movement == "R":
        for i in range(steps):
            posH[0] += 1
            update()

print(positions)

print(len(positions))

