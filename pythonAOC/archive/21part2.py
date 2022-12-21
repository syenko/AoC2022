from dataclasses import dataclass

f = open("../inputs/21.txt", "r")

lines = [x.strip() for x in f]

graph = {}

MAX_VALUE = 1000000000

@dataclass
class Monkey:
    number : int
    next : list
    symbol : str
    calcVal : bool

    def __str__(self):
        if self.calcVal:
            return f"{self.next[0]} {self.symbol} {self.next[1]}"
        else:
            return f"{self.number}"

monkeys = {}

for line in lines:
    parts = line.split(": ")
    name = parts[0]
    next = []
    symbol = ""
    if "+" in parts[1] or "-" in parts[1] or "*" in parts[1] or "/" in parts[1]:
        eqx = parts[1].split(" ")
        symbol = eqx[1]
        next = [eqx[0], eqx[2]]
        number = -MAX_VALUE
        calcVal = True
    else:
        number = int(parts[1])
        calcVal = False

    monkeys[name] = Monkey(number, next, symbol, calcVal)

root = "root"
you = "humn"

visited = {}
for name in monkeys.keys():
    visited[name] = False

visitedHuman = []

def dfs(node, visHuman=False):
    monkey = monkeys[node]

    if visited[node]:
        return (monkey.number, visHuman)

    visited[node] = True
    if node == you:
        visHuman = True

    if not monkey.calcVal:
        if not visHuman:
            monkey.calcVal = False
        return (monkey.number, visHuman)

    visited[node] = True
    res1 = dfs(monkey.next[0])
    res2 = dfs(monkey.next[1])
    visHuman = visHuman or res1[1] or res2[1]
    if monkey.symbol == "+":
        monkey.number = res1[0] + res2[0]
    elif monkey.symbol == "-":
        monkey.number = res1[0] - res2[0]
    elif monkey.symbol == "/":
        monkey.number = res1[0] / res2[0]
    elif monkey.symbol == "*":
        monkey.number = res1[0] * res2[0]

    if not visHuman:
        monkey.calcVal = False
    else:
        visitedHuman.append(node)

    return (monkey.number, visHuman)

check1 = monkeys[root].next[0]
check2 = monkeys[root].next[1]

monkeys[you].number = 1
val1 = dfs(check1)
val2 = dfs(check2)

print(val1, val2)

print(len(visitedHuman))
visitedHuman.reverse()
print(visitedHuman)
check = val2[0]
coefficient = []
for (index, val) in enumerate(visitedHuman):
    monkey = monkeys[val]

    print(monkey)

    if index != len(visitedHuman) - 1:
        (next, constIsFirst) = \
            (monkey.next[0], True) if monkey.next[0] != visitedHuman[index + 1] else \
            (monkey.next[1], False)
    else:
        (next, constIsFirst) = \
            (monkey.next[0], True) if monkey.next[0] != you else \
            (monkey.next[1], False)



    # always calc value
    if monkey.symbol == "+":
        check -= monkeys[next].number
    elif monkey.symbol == "-":
        if not constIsFirst:
            check += monkeys[next].number
        else:
            check = monkeys[next].number - check
    elif monkey.symbol == "/":
        if not constIsFirst:
            check *= monkeys[next].number
        else:
            check = monkeys[next].number / check
    elif monkey.symbol == "*":
        check /= monkeys[next].number

print(check)

for i in range(0):
    for name in monkeys.keys():
        visited[name] = False

    for monkey in monkeys.values():
        if monkey.calcVal:
            monkey.number = -MAX_VALUE

    monkeys[you].number = i

    res = dfs(check1)
    print(res)

    if res == check:
        print(i)
        break