f = open("inputs/17.txt", "r")

lines = [x.strip() for x in f]

jetPoint = -1
stream = lines[0]

rocks = [
    # 0
    ["####"],
    # 1
    [
    ".#.",
    "###",
    ".#.",
    ],
    # 2
    [
    "..#",
    "..#",
    "###",
    ],
    # 3
    [
    "#",
    "#",
    "#",
    "#",
    ],
    # 4
    [
    "##",
    "##"
    ]
]

positions = set()

topPos = -1

def addRock(rock, startX, startY):
    for row in range(len(rock)):
        for col in range(len(rock[row])):
            if rock[row][col] == "#":
                if (startX + col, startY - row) in positions:
                    print(f"AHHHHHHH: rock {rock} row {row} col {col}");
                positions.add((
                    startX + col,
                    startY - row
                ))

def canPlaceRock(rock, startX, startY):
    for row in range(len(rock)):
        for col in range(len(rock[row])):
            if rock[row][col] == "#":
                if (startX + col, startY - row) in positions:
                    return False
    return True

rockHeights = []


total = 0

# calc cycle #1
for i in range(100000000):
    print(f"i: {i} topPos: {topPos}")
    rockPos = i % len(rocks)
    # print(f"RRRR{rockPos}")
    rock = rocks[rockPos]

    startX = 2 # left
    startY = topPos + 3 + len(rock) # top
    END = False
    added = 0
    while True:
        # print(f"-- x: {startX} y: {startY}")
        jetPoint += 1
        if total >= 1*len(stream):
            END = True
            break
        added += 1
        jetPoint = jetPoint % len(stream)

        failed = False
        # right
        if stream[jetPoint] == ">":
            # hit bound
            if startX + len(rock[0]) >= 7:
                failed = True

            blocked = not canPlaceRock(rock, startX + 1, startY)

            if not blocked and not failed:
                # print("move right")
                startX += 1
        # left
        else:
            if startX - 1 < 0:
                failed = True

            blocked = not canPlaceRock(rock, startX - 1, startY)

            if not blocked and not failed:
                startX -= 1

        total += 1
        # print(f"x: {startX} y: {startY}")
        # move down
        if startY - (len(rock) - 1) - 1 < 0:
            addRock(rock, startX, startY)
            break

        end = not canPlaceRock(rock, startX, startY - 1)

        if end:
            addRock(rock, startX, startY)
            break
        startY -= 1

    if END:
        break

    topPos = max(topPos, startY)
    rockHeights.append(topPos)

    print(f"x {startX} y {startY}")
    # print(f"i {i} pos {positions}")

initCycleNum = i
initCyclePos = topPos

total = 0
jetPoint = -1

cycleHeights = []

# calc cycle #2
for i in range(initCycleNum, 100000000):
    print(f"i: {i} topPos: {topPos}")
    rockPos = i % len(rocks)
    # print(f"RRRR{rockPos}")
    rock = rocks[rockPos]

    startX = 2 # left
    startY = topPos + 3 + len(rock) # top
    END = False
    added = 0
    while True:
        # print(f"-- x: {startX} y: {startY}")
        jetPoint += 1
        if total >= 1*len(stream):
            END = True
            break
        added += 1
        jetPoint = jetPoint % len(stream)

        failed = False
        # right
        if stream[jetPoint] == ">":
            # hit bound
            if startX + len(rock[0]) >= 7:
                failed = True

            blocked = not canPlaceRock(rock, startX + 1, startY)

            if not blocked and not failed:
                # print("move right")
                startX += 1
        # left
        else:
            if startX - 1 < 0:
                failed = True

            blocked = not canPlaceRock(rock, startX - 1, startY)

            if not blocked and not failed:
                startX -= 1

        total += 1
        # print(f"x: {startX} y: {startY}")
        # move down
        if startY - (len(rock) - 1) - 1 < 0:
            addRock(rock, startX, startY)
            break

        end = not canPlaceRock(rock, startX, startY - 1)

        if end:
            addRock(rock, startX, startY)
            break
        startY -= 1

    if END:
        break

    cycleHeights.append(topPos)

    topPos = max(topPos, startY)

    print(f"x {startX} y {startY}")

cycleLength = i - initCycleNum
cycleAddedHeight = topPos - initCyclePos

print(rock)
print(added)
print(jetPoint)
print(topPos + 1)

FINAL = 1000000000000

ans = \
    (1000000000000 - initCycleNum) // cycleLength * cycleAddedHeight + \
    cycleHeights[(1000000000000 - initCycleNum) % cycleLength] + 1

print(ans)

# print((1000000000000 // loopCount) * (topPos + 1) + rockHeights[(1000000000000 % loopCount) - 1] + 1)