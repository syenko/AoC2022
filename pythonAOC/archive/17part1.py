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


for i in range(2022):
    print(f"i: {i} topPos: {topPos}")
    rockPos = i % len(rocks)
    # print(f"RRRR{rockPos}")
    rock = rocks[rockPos]

    startX = 2 # left
    startY = topPos + 3 + len(rock) # top

    while True:
        # print(f"-- x: {startX} y: {startY}")
        jetPoint += 1
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

    topPos = max(topPos, startY)
    print(f"x {startX} y {startY}")

print(topPos + 1)