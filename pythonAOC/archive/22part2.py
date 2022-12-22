from dataclasses import dataclass

MAX_VALUE = 10000000

f = open("../inputs/22.txt", "r")

lines = [x.replace("\n", "") for x in f]

pos = {}

SIZE = 50

WALL = "#"
TILE = "."

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

dirStrings = ["right", "down", "left", "up"]

@dataclass
class AdjFace:
    num: int
    dir: int
    flipped: int

    def __init__(self, _num, _dir, _flipped=False):
        self.num = _num
        self.dir = _dir
        self.flipped = _flipped

# hard coded for input
# [(face, orientiation on new faced, flipped?)]
adjFaces = [
    [AdjFace(1, RIGHT), AdjFace(2, DOWN), AdjFace(3, RIGHT, True), AdjFace(5, RIGHT)], # 0
    [AdjFace(4, LEFT, True), AdjFace(2, LEFT), AdjFace(0, LEFT), AdjFace(5, UP)], # 1
    [AdjFace(1, UP), AdjFace(4, DOWN), AdjFace(3, DOWN), AdjFace(0, UP)], # 2
    [AdjFace(4, RIGHT), AdjFace(5, DOWN), AdjFace(0, RIGHT, True), AdjFace(2, RIGHT)], # 3
    [AdjFace(1, LEFT, True), AdjFace(5, LEFT), AdjFace(3, LEFT), AdjFace(2, UP)], # 4
    [AdjFace(4, UP), AdjFace(1, DOWN), AdjFace(0, DOWN), AdjFace(3, UP)] # 5
]
# hard coded for test


MIN = 1
MAX = 2
maxX = max([len(line) for line in lines])
maxY = len(lines) - 2


@dataclass
class Face:
    fNum: int
    rows: list
    cols: list
    startX: int
    startY: int

    def __init__(self):
        self.num = -1
        self.rows = []
        self.cols = ["" for i in range(SIZE)]
        self.startX = -1
        self.startY = -1

    def __str__(self):
        ans = f"---- {self.num} ({self.startX}, {self.startY})---- \n"
        # for row in self.rows:
        #     ans += row + "\n"
        return ans


faces = [Face() for i in range(6)]

completedFaces = 0
# parse faces
while completedFaces < 6:
    for yGroup in range((len(lines) - 2) // SIZE):
        for y in range(yGroup * SIZE, (yGroup + 1) * SIZE):
            line = lines[y]
            parts = [line[i: i + SIZE] for i in range(0, len(line), SIZE)]

            count = 0
            for (partNum, part) in enumerate(parts):
                if part[0] != " ":
                    fNum = completedFaces + count
                    faces[fNum].num = fNum
                    faces[fNum].startY = yGroup * SIZE
                    faces[fNum].startX = partNum * SIZE

                    faces[fNum].rows.append(part)
                    for (x, char) in enumerate(part):
                        faces[fNum].cols[x] += char
                    count += 1

        completedFaces += len([part for part in parts if part[0] != " "])

for face in faces:
    print(face)

# parse instructions
instructionsLine = lines[len(lines) - 1]
instructions = []
index = 0
numStr = ""
for y in instructionsLine:
    if y == "R" or y == "L":
        instructions.append(int(numStr))
        instructions.append(y)
        numStr = ""
    else:
        numStr += y
instructions.append(int(numStr))

direction = RIGHT
curX = 0
curY = 0
curFace = 0


def bound(value, arr):
    return (value - arr[MIN]) % (arr[MAX] - arr[MIN]) + arr[MIN]


def outOfBounds(value):
    return value < 0 or value >= SIZE


def getNewCoords(notChangingCoord, newDirection, flipped):
    if flipped:
        notChangingCoord = SIZE - notChangingCoord - 1
    if newDirection == RIGHT:
        return 0, notChangingCoord
    elif newDirection == LEFT:
        return SIZE - 1, notChangingCoord
    elif newDirection == DOWN:
        return notChangingCoord, 0
    elif newDirection == UP:
        return notChangingCoord, SIZE - 1


print(f"START: ({curX}, {curY}) f: {dirStrings[direction]}")

for instruction in instructions:
    print(f"I: {instruction}")
    if type(instruction) == int:
        for y in range(instruction):
            newX = curX
            newY = curY
            newFace = curFace
            newDir = direction
            if direction == LEFT:
                if outOfBounds(newX - 1):
                    newFace = adjFaces[curFace][LEFT].num
                    newDir = adjFaces[curFace][LEFT].dir
                    (newX, newY) = getNewCoords(curY, newDir, adjFaces[curFace][LEFT].flipped)
                else:
                    newX -= 1
            elif direction == RIGHT:
                if outOfBounds(newX + 1):
                    newFace = adjFaces[curFace][RIGHT].num
                    newDir = adjFaces[curFace][RIGHT].dir
                    (newX, newY) = getNewCoords(curY, newDir, adjFaces[curFace][RIGHT].flipped)
                else:
                    newX += 1
            elif direction == UP:
                if outOfBounds(newY - 1):
                    newFace = adjFaces[curFace][UP].num
                    newDir = adjFaces[curFace][UP].dir
                    (newX, newY) = getNewCoords(curX, newDir, adjFaces[curFace][UP].flipped)
                else:
                    newY -= 1
            elif direction == DOWN:
                if outOfBounds(newY + 1):
                    newFace = adjFaces[curFace][DOWN].num
                    newDir = adjFaces[curFace][DOWN].dir
                    (newX, newY) = getNewCoords(curX, newDir, adjFaces[curFace][DOWN].flipped)
                else:
                    newY += 1

            if faces[newFace].rows[newY][newX] == WALL:
                break
            else:
                curX = newX
                curY = newY
                direction = newDir
                curFace = newFace
    else:
        if instruction == "R":
            direction = (direction + 1) % 4
        elif instruction == "L":
            direction = (direction - 1) % 4

    print(f"({curX}, {curY}) f: {dirStrings[direction]}")

print(curX, curY, direction, faces[curFace])
print(1000 * (curY + faces[curFace].startY + 1) + 4 * (curX + faces[curFace].startX + 1) + direction)
