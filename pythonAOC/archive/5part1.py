f = open("inputs/5.txt", "r")

crates = []

for x in f:
    if x == "\n":
        break
    if x[1] == "1":
        continue
    print(x)
    crates.append(x)

stacks = []

for i in range(9):
    stacks.append([])

for i in range(len(crates)-1,-1, -1):
    for j in range(1,len(crates[i]),4):
        if (crates[i][j] != ' '):
            stacks[(j-1)//4].append(crates[i][j])

for x in f:
    vals = x.split(" ")
    numMove = int(vals[1])
    start = int(vals[3]) - 1
    end = int(vals[5]) - 1

    for i in range(numMove):
        stacks[end].append(stacks[start].pop())


# print(stacks)
for i in stacks:
    print(i.pop(),end="")

