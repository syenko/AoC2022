f = open("inputs/4.txt", "r")

count = 0

for x in f:
    (a, b) = x.split(",")
    elf1 = [int(i) for i in a.split("-")]
    elf2 = [int(i) for i in b.split("-")]
    range1 = {i for i in range(elf1[0], elf1[1] + 1)}
    range2 = {i for i in range(elf2[0], elf2[1] + 1)}
    if len(range1.intersection(range2)) > 0:
        count +=1
    print(f"{elf1[0]} {elf2[0]}")

print(count)
