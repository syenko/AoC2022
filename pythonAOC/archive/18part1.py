f = open("inputs/18.txt", "r")

lines = [x.strip() for x in f]

blocks = []

MAX_VAL = 1000000000000

maxX = 0
maxY = 0
maxZ = 0

for line in lines:
    (x, y, z) = line.split(",")
    blocks.append((int(x), int(y), int(z)))

surfaceArea = 0
for a in blocks:
    x = a[0]
    y = a[1]
    z = a[2]
    if (x-1, y, z) not in blocks:
        surfaceArea += 1
    if (x+1, y, z) not in blocks:
        surfaceArea += 1
    if (x, y-1, z) not in blocks:
        surfaceArea += 1
    if (x, y+1, z) not in blocks:
        surfaceArea += 1
    if (x, y, z+1) not in blocks:
        surfaceArea += 1
    if (x, y, z-1) not in blocks:
        surfaceArea += 1

print(surfaceArea)