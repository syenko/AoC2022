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

maxX = 0
maxY = 0
minX = 1000000
minY = 1000000
for block in blockages:
    maxX = max({maxX, block[0][0], block[1][0]})
    maxY = max({maxY, block[0][1], block[1][1]})
    minX = min({minX, block[0][0], block[1][0]})
    minY = min({minY, block[0][1], block[1][1]})

grid = []

for i in range(maxY+1):
    grid.append([])
    for j in range(maxX+1):
        grid[i].append(-1)

# print(len(grid[0]))

for block in blockages:
    print(block)
    block.sort(key=lambda x : x[0])
    # x
    for i in range(block[0][0], block[1][0] + 1):
        grid[block[0][1]][i] = 0
    # y
    block.sort(key=lambda x : x[1])
    for i in range(block[0][1], block[1][1] + 1):
        grid[i][block[0][0]] = 0

class Sand:
    def __init__(self):
        self.x = 500
        self.y = -1

    def move(self):
        while self.x + 1 < len(grid[0]) and self.y + 1 < len(grid) and self.x - 1 > 0:
            if grid[self.y + 1][self.x] < 0:
                self.y += 1
                continue
            elif grid[self.y + 1][self.x - 1] < 0:
                self.x -= 1
                self.y += 1
                continue
            elif grid[self.y + 1][self.x + 1] < 0:
                self.x += 1
                self.y += 1
                continue
            else:
                break

        print(f"x: {self.x}, y: {self.y}")

        if self.x < minX or self.x > maxX or self.y < 0 or self.y >= maxY:
            return False

        grid[self.y][self.x] = 1
        return True

print(f"max: ({maxX}, {maxY}), min: ({minX}, {minY})")
print(f"grid dimens: {len(grid[0])}, {len(grid)}")
better = "\n"

for line in grid[minY:maxY + 1]:
    for char in line[minX:maxX + 1]:
        if char == -1:
            print(".", end="")
        if char == 1:
            print("o", end="")
        if char == 0:
            print("#", end="")
    print()

count = 0
while (True):
    sand = Sand()
    if not sand.move():
        break
    else:
        count += 1

for line in grid[minY:maxY + 1]:
    for char in line[minX:maxX + 1]:
        if char == -1:
            print(".", end="")
        if char == 1:
            print("o", end="")
        if char == 0:
            print("#", end="")
    print()

print(count)