from dataclasses import dataclass

f = open("../inputs/24.txt", "r")
# f = open("inputs/24test.txt", "r")

lines = [x.strip() for x in f]

HEIGHT = len(lines) - 2
WIDTH = len(lines[0]) - 2

print(WIDTH, HEIGHT)

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

directions = {
    "^": UP,
    "<": LEFT,
    "v": DOWN,
    ">": RIGHT
}
dirStr = ["^", "<", "v", ">"]

positionsPerTurn = {
    0: (set(), []) # (positions, blizzards)
}

@dataclass
class Blizzard:
    direction: int
    x: int
    y: int

    def __init__(self, dirStr, _x, _y, _dir=0):
        if dirStr != "":
            self.direction = directions[dirStr]
        else:
            self.direction = _dir
        self.x = _x
        self.y = _y

    def update(self, pos, numTurns=1):
        # if (self.x, self.y) in pos:
        #     pos.remove((self.x, self.y))

        newX = self.x
        newY = self.y
        if self.direction == UP:
            newY -= numTurns
        elif self.direction == DOWN:
            newY += numTurns
        elif self.direction == LEFT:
            newX -= numTurns
        elif self.direction == RIGHT:
            newX += numTurns

        newY %= HEIGHT
        newX %= WIDTH

        pos.add((newX, newY))
        return Blizzard("", newX, newY, _dir=self.direction)


startPos = 0
for (i, char) in enumerate(lines[0]):
    if char == ".":
        startPos = i - 1
        break

for i in range(1, len(lines) - 1):
    line = lines[i]
    for j in range(1, len(line) - 1):
        char = line[j]
        if char != ".":
            x = j-1
            y = i-1
            positionsPerTurn[0][0].add((x, y))
            positionsPerTurn[0][1].append(Blizzard(char, x, y))

checkNext = [
    # ((x, y), turn#)
    ((startPos, -1), 0)
]
checking = {((startPos, -1), 0)}
turn = 0
startGoals = [
    (startPos, -1),
    (WIDTH - 1, HEIGHT),
    (startPos, -1)
]
endGoals = [
    (WIDTH - 1, HEIGHT),
    (startPos, -1),
    (WIDTH - 1, HEIGHT)
]
for i, endGoal in enumerate(endGoals):
    print("******* RESTARTING!!! ********")
    checkNext = [
        # ((x, y), turn#)
        (startGoals[i], turn)
    ]
    checking = {(startGoals[i], turn)}
    while len(checkNext) > 0:
        top = checkNext.pop(0)
        x = top[0][0]
        y = top[0][1]
        turn = top[1]
        print(f"--- Minute {turn}::: ({x}, {y}) ---")
        if x == endGoal[0] and y == endGoal[1]:
            break

        turn += 1

        # print(f"CHECKING: {checking}")
        # print(f"NEXT: {checkNext}")
        checking.remove(top)

        if turn not in positionsPerTurn.keys():
            newPositions = set()
            newBlizzards = []
            # add positions
            for blizzard in positionsPerTurn[turn - 1][1]:
                newBlizzards.append(blizzard.update(newPositions))
            positionsPerTurn[turn] = (newPositions, newBlizzards)

            print(f"{turn} --- ")
            display = [["." for i in range(WIDTH)] for j in range(HEIGHT)]
            for blizzard in positionsPerTurn[turn][1]:
                display[blizzard.y][blizzard.x] = dirStr[blizzard.direction]
            for line in display:
                for char in line:
                    print(char, end="")
                print()

        pos = positionsPerTurn[turn][0]
        # print(pos)
        added = False
        # right
        if x + 1 < WIDTH and (x + 1, y) not in pos and y >= 0 and y < HEIGHT:
            if ((x + 1, y), turn) not in checking:
                checkNext.append(((x + 1, y), turn))
                checking.add(((x + 1, y), turn))
            added = True
        # down
        if (y + 1 < HEIGHT or (x == WIDTH - 1 and y + 1 == HEIGHT)) and (x, y + 1) not in pos:
            if ((x, y + 1), turn) not in checking:
                checkNext.append(((x, y + 1), turn))
                checking.add(((x, y + 1), turn))
            added = True

        # wait
        if (x, y) not in pos:
            if ((x, y), turn) not in checking:
                # print(f"({x}, {y}), {turn} ::: {((x, y), turn) in checking}")
                checkNext.append(((x, y), turn))
                checking.add(((x, y), turn))

        # left
        if x - 1 >= 0 and (x - 1, y) not in pos and y >= 0 and y < HEIGHT:
            if ((x - 1, y), turn) not in checking:
                checkNext.append(((x - 1, y), turn))
                checking.add(((x - 1, y), turn))
        # up
        if (y - 1 >= 0 or (x == 0 and y - 1 >= -1)) and (x, y - 1) not in pos:
            if ((x, y - 1), turn) not in checking:
                checkNext.append(((x, y - 1), turn))
                checking.add(((x, y - 1), turn))

    # print(checkNext[0])

print(turn)