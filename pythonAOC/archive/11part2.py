f = open("inputs/11.txt", "r")

lines = [x.strip() for x in f]

monkeys = []

class Monkey():
    # objects = []
    # testVal = 0

    def __init__(self, objs, op, test, trueThrow, falseThrow):
        self.objects = objs
        self.op = op # string representing operation
        self.test = test
        self.trueThrow = trueThrow
        self.falseThrow = falseThrow
        self.inspects = 0

    def __str__(self):
        return f"objects: {self.objects}"

    # def inspect(self, value):
    #     return eval(self.op.replace("old"), str(value))//3

    def testValue(self, value, totalMod):
        val = eval(self.op.replace("old", str(value))) % totalMod
        self.inspects += 1
        # print(val)
        if val % self.test == 0:
            monkeys[self.trueThrow].addObj(val)
        else:
            monkeys[self.falseThrow].addObj(val)

    def runTurn(self, totalMod):
        for obj in self.objects:
            self.testValue(obj, totalMod)
        self.objects = []

    def clearList(self):
        self.objects = []

    def addObj(self, obj):
        self.objects.append(obj)

for i in range(len(lines)):
    line = lines[i]

    if line.split(" ")[0] == "Monkey":
        objects = [int(x) for x in lines[i+1].split(": ")[1].split(", ")]
        op = lines[i+2].split("new = ")[1]
        test = int(lines[i+3].split(" ")[3])
        trueThrow = int(lines[i+4].split(" ")[5])
        falseThrow = int(lines[i+5].split(" ")[5])

        monkeys.append(Monkey(objects, op, test, trueThrow, falseThrow))
        print(monkeys[len(monkeys)-1])

        i = i + 5

totalMod = 1
for monkey in monkeys:
    totalMod *= monkey.test

for i in range(10000):
    for monkey in monkeys:
        monkey.runTurn(totalMod)

print("---")
inspects = []
for monkey in monkeys:
    print(monkey)
    inspects.append(monkey.inspects)

inspects.sort(reverse=True)

print(inspects[0] * inspects[1])