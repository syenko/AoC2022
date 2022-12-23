from dataclasses import dataclass

f = open("../inputs/23.txt", "r")
lines = [x.strip() for x in f]

MAX_VALUE = 100000000

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

@dataclass
class Elf:
    x: int
    y: int
    dirs: list
    newX: int
    newY: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.newX = x
        self.newY = y
        self.dirs = [NORTH, SOUTH, WEST, EAST]

    def canMoveInDir(self, dir, pos, props):
        if dir == NORTH:
            positions = [(self.x - 1, self.y - 1), (self.x, self.y - 1), (self.x + 1, self.y - 1)]
        elif dir == SOUTH:
            positions = [(self.x - 1, self.y + 1), (self.x, self.y + 1), (self.x + 1, self.y + 1)]
        elif dir == WEST:
            positions = [(self.x - 1, self.y - 1), (self.x - 1, self.y), (self.x - 1, self.y + 1)]
        else:
            positions = [(self.x + 1, self.y - 1), (self.x + 1, self.y), (self.x + 1, self.y + 1)]
        for position in positions:
            if position in pos:
                return False
        return True

    def changeNewPos(self, dir, props):
        if dir == NORTH:
            self.newX = self.x
            self.newY = self.y - 1
        if dir == SOUTH:
            self.newX = self.x
            self.newY = self.y + 1
        if dir == WEST:
            self.newX = self.x - 1
            self.newY = self.y
        if dir == EAST:
            self.newX = self.x + 1
            self.newY = self.y

        props.append((self.newX, self.newY))


    def update(self, pos, props):
        positions = [
            (self.x - 1, self.y - 1),
            (self.x, self.y - 1),
            (self.x + 1, self.y - 1),
            (self.x - 1, self.y + 1),
            (self.x, self.y + 1),
            (self.x + 1, self.y + 1),
            (self.x - 1, self.y),
            (self.x + 1, self.y)
        ]

        for position in positions:
            if position in pos:
                for dir in self.dirs:
                    if self.canMoveInDir(dir, pos, props):
                        self.changeNewPos(dir, props)
                        return
                return
        # print("did not move")
        self.newX = self.x
        self.newY = self.y
        # props.append((self.newX, self.newY))

    def tryMove(self, pos, props):
        if props.count((self.newX, self.newY)) == 1:
            pos.remove((self.x, self.y))
            self.x = self.newX
            self.y = self.newY
            pos.add((self.x, self.y))
        first = self.dirs.pop(0)
        self.dirs.append(first)


elves = []
pos = set()
for (y, line) in enumerate(lines):
    for (x, char) in enumerate(line):
        if char == "#":
            pos.add((x, y))
            elves.append(Elf(x, y))

props = []

for roundNum in range(10):
    print(f"round #{roundNum}")
    props.clear()
    for elf in elves:
        elf.update(pos, props)

    for elf in elves:
        elf.tryMove(pos, props)

print(pos)

minX = MAX_VALUE
minY = MAX_VALUE
maxX = -MAX_VALUE
maxY = -MAX_VALUE
for position in pos:
    minX = min(position[0], minX)
    minY = min(position[1], minY)
    maxX = max(position[0], maxX)
    maxY = max(position[1], maxY)

for y in range(minY, maxY + 1):
    for x in range(minX, maxX + 1):
        if (x, y) in pos:
            print("#", end="")
        else:
            print(".", end="")
    print("\n",end="")

print(f"x: {minX}, {maxX} ::: y:{minY}, {maxY}")
print((maxX - minX + 1) * (maxY - minY + 1) - len(pos))