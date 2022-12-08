f = open("inputs/8.txt", "r")

lines = [x.strip() for x in f]

grid = []
ansMat = []

for i in range(len(lines)):
    grid.append([])
    ansMat.append([])
    for j in range(len(lines[i])):
        grid[i].append(lines[i][j])
        ansMat[i].append(False)

ans = 0

def checkBounds(val, index, arr, start, end, step=1):
    # print(f"val: {val}, index: {index}, arr: {arr}, start: {start}, end: {end}")
    for i in range(start, end, step):
        if arr[i] >= val:
            # print(f"i: {abs(i-index)}")
            return abs(i-index)

    # print(f"end i: {abs(index-(end-1))}")
    return abs(index-(end-step))

best = (-1, -1) # testing purposes

for i in range(len(grid)):
    for j in range(len(grid[i])):
        # print(f"--{i}, {j}---")
        val = grid[i][j]
        row = grid[i]
        col = [grid[i][j] for i in range(len(grid))]

        # print(f"row: {row}, col: {col}")

        curTotal = 1

        # rows
        # right
        curTotal *= checkBounds(val, j, row, j+1, len(row))
        # left
        curTotal *= checkBounds(val, j, row, j-1, -1,  -1)
        # down
        curTotal *= checkBounds(val, i, col, i + 1, len(col))
        # up
        curTotal *= checkBounds(val, i, col, i-1, -1, -1)

        if (curTotal > ans):
            best = (i, j)
        ans = max(curTotal, ans)


print(ans)
# print(best)