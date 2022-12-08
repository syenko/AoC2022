f = open("input.txt", "r")

lines = [x.strip() for x in f]

grid = []
ansMat = []

for i in range(len(lines)):
    grid.append([])
    ansMat.append([])
    for j in range(len(lines[i])):
        grid[i].append(lines[i][j])
        ansMat[i].append(False)

print(len(ansMat[0]))

for i in range(len(lines)):
    row = lines[i]
    maxVal = -1
    for j in range(len(row)):
        height = int(row[j])

        if (height > maxVal):
            ansMat[i][j] = True
            maxVal = height

    maxVal = -1
    for j in range(len(row)-1,-1,-1):
        height = int(row[j])

        if (height > maxVal):
            ansMat[i][j] = True
            maxVal = height

for i in range(len(lines[0])):
    maxVal = -1
    for j in range(len(lines)):
        height = int(lines[j][i])

        if (height > maxVal):
            ansMat[j][i] = True
            maxVal = height

    maxVal = -1
    for j in range(len(lines) - 1, -1, -1):
        height = int(lines[j][i])

        if (height > maxVal):
            ansMat[j][i] = True
            maxVal = height

ans = 0

print(ansMat)

for row in ansMat:
    for col in row:
        if col:
            ans += 1

print(ans)