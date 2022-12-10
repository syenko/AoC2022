f = open("inputs/10.txt", "r")

lines = [x.strip() for x in f]

signalStrengths = []

signal = 1
cycleNum = 0

good = [20, 60, 100, 140, 180, 220]

for line in lines:
    if line == "noop":
        cycleNum += 1
        if (cycleNum in good):
            print(f"cycleNum {cycleNum} sig {signal}")
        signalStrengths.append(cycleNum * signal)
        continue
    else:
        num = int(line.split(" ")[1])
        cycleNum += 1
        signalStrengths.append(cycleNum * signal)
        if (cycleNum in good):
            print(f"cycleNum {cycleNum} sig {signal}")
        cycleNum += 1
        signalStrengths.append(cycleNum * signal)
        signal += num

    if (cycleNum in good):
        print(f"cycleNum {cycleNum} sig {signal}")

ans = 0
for i in good:
    print(signalStrengths[i-1])
    ans += signalStrengths[i-1]

print(ans)