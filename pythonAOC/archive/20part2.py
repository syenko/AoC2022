f = open("input.txt", "r")

lines = [x.strip() for x in f]

values = []
reorder = []

decrypt = 811589153
for (i, line) in enumerate(lines):
    values.append(int(line) * decrypt)
    reorder.append(i)

print("starting lineup")
for j in reorder:
    print(values[j], end = ", ")
print()

for j in range(10):
    for (i, num) in enumerate(values):
        # print(i)
        startPos = reorder.index(i)
        if startPos + num == 0:
            endPos = (startPos + num - 1) % len(values)
        else:
            endPos = (startPos + num) % (len(values) - 1)
        reorder.remove(i)
        reorder.insert(endPos, i)
        # for j in reorder:
        #     print(values[j], end=", ")
        # print()

for j in reorder:
    print(values[j], end = ", ")
print()

zeroIndex = reorder.index(values.index(0)) # okay

print(zeroIndex)

print("---")

ans = 0
indexes = [1000, 2000, 3000]
for i in indexes:
    ans += values[reorder[(i + zeroIndex) % len(values)]]
print(ans)