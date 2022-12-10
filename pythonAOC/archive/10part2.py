f = open("inputs/10.txt", "r")

lines = [x.strip() for x in f]

signalStrengths = []

signal = 1
cycleNum = 0

for line in lines:
    if line == "noop":
        cycleNum += 1
        signalStrengths.append(signal)
        continue
    else:
        num = int(line.split(" ")[1])
        cycleNum += 1
        signalStrengths.append(signal)
        cycleNum += 1
        signalStrengths.append(signal)
        signal += num

ans = ""

for (i, sig) in enumerate(signalStrengths):
    if (i % 40 in [sig - 1, sig, sig + 1]):
        ans += "#"
    else:
        ans += "."

for i in range(6):
    print(ans[i*40:(i+1)*40])