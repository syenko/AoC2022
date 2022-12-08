f = open("inputs/4.txt", "r")

count = 0

for x in f:
    (a, b) = x.split(",")
    elf1 = [int(i) for i in a.split("-")]
    elf2 = [int(i) for i in b.split("-")]
    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
        count += 1
    print(f"{elf1[0]} {elf2[0]}")

print(count)
