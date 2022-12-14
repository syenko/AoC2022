f = open("inputs/14.txt", "r")

lines = [x.strip() for x in f]

blockages = []

for line in lines:
    paths = line.split(" -> ")
    for i in range(len(paths)-1):
        blockages.append(
            [
            [int(x) for x in paths[i].split(",")],
            [int(x) for x in paths[i + 1].split(",")]
             ]
        )

maxY = 0
for block in blockages:
    maxY = max({maxY, block[0][1], block[1][1]})

positions = set()

for block in blockages:
    block.sort(key=lambda x : x[0])
    # x
    for i in range(block[0][0], block[1][0] + 1):
        positions.add((i,block[0][1]))
    # y
    block.sort(key=lambda x : x[1])
    for i in range(block[0][1], block[1][1] + 1):
        positions.add((block[0][0],i))

def move():
    x = 500
    y = -1
    while y < maxY:
        if (x, y + 1) not in positions:
            y += 1
            continue
        elif (x - 1, y + 1) not in positions:
            x -= 1
            y += 1
            continue
        elif (x + 1, y + 1) not in positions:
            x += 1
            y += 1
            continue
        else:
            break

    if y >= maxY:
        return False

    positions.add((x, y))
    return True

count = 0
while (True):
    if not move():
        break
    else:
        count += 1

print(count)