MAX_VALUE = 10000000

f = open("../inputs/22.txt", "r")

lines = [x.replace("\n", "") for x in f]

pos = {}

WALL = "#"
TILE = "."

MIN = 1
MAX = 2
maxX = max([len(line) for line in lines])
maxY = len(lines) - 2
rows = [
    ["", MAX_VALUE, -MAX_VALUE] for i in range(maxY)
    # [row string (only important stuff), minX, maxX]
]
cols = [
    ["", MAX_VALUE, -MAX_VALUE] for i in range(maxX)
    # [col string (only important stuff), minY, maxY]
]

for (y, line) in enumerate(lines[:-2]):
    for (x, char) in enumerate(line):
        if char != " ":
            pos[(x, y)] = char
            rows[y][0] += char
            rows[y][1] = min(rows[y][1], x)
            rows[y][2] = max(rows[y][2], x)

            cols[x][0] += char
            cols[x][1] = min(cols[x][1], y)
            cols[x][2] = max(cols[x][2], y)

for row in rows:
    row[MAX] += 1
for col in cols:
    col[MAX] += 1

# parse instructions
instructionsLine = lines[len(lines) - 1]
instructions = []
index = 0
numStr = ""
for i in instructionsLine:
    if i == "R" or i == "L":
        instructions.append(int(numStr))
        instructions.append(i)
        numStr = ""
    else:
        numStr += i
instructions.append(int(numStr))

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

dirStrings = ["right", "down", "left", "up"]

direction = RIGHT
curX = rows[0][MIN]
curY = 0


print(rows)
print(cols)

def bound(value, arr):
    return (value - arr[MIN]) % (arr[MAX] - arr[MIN]) + arr[MIN]


print(f"START: ({curX}, {curY}) f: {dirStrings[direction]}")

for instruction in instructions:
    print(f"I: {instruction}")
    if type(instruction) == int:
        if direction == LEFT:
            newPos = curX
            for i in range(instruction):
                newPos = bound(newPos - 1, rows[curY])
                if pos[(newPos, curY)] == WALL:
                    newPos = bound(newPos + 1, rows[curY])
                    break
            curX = newPos
        elif direction == RIGHT:
            newPos = curX
            for i in range(instruction):
                newPos = bound(newPos + 1, rows[curY])
                if pos[(newPos, curY)] == WALL:
                    newPos = bound(newPos - 1, rows[curY])
                    break
            curX = newPos
        elif direction == UP:
            newPos = curY
            for i in range(instruction):
                newPos = bound(newPos - 1, cols[curX])
                if pos[(curX, newPos)] == WALL:
                    newPos = bound(newPos + 1, cols[curX])
                    break
            curY = newPos
        elif direction == DOWN:
            newPos = curY
            for i in range(instruction):
                newPos = bound(newPos + 1, cols[curX])
                if pos[(curX, newPos)] == WALL:
                    newPos = bound(newPos - 1, cols[curX])
                    break
            curY = newPos
    else:
        if instruction == "R":
            direction = (direction + 1) % 4
        elif instruction == "L":
            direction = (direction - 1) % 4

    print(f"({curX}, {curY}) f: {dirStrings[direction]}")

print(curX, curY, direction)
print(1000 * (curY + 1) + 4 * (curX + 1) + direction)
# curX = col
# curY = row
