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
    else:
        number = int(parts[1])

    monkeys[name] = Monkey(number, next, symbol)

start = "root"

visited = {}
for name in monkeys.keys():
    visited[name] = False


def dfs(node):

    monkey = monkeys[node]
    if monkey.number != -MAX_VALUE or visited[node]:
        visited[node] = True
        return monkey.number

    visited[node] = True
    if monkey.symbol == "+":
        monkey.number = dfs(monkey.next[0]) + dfs(monkey.next[1])
    elif monkey.symbol == "-":
        monkey.number = dfs(monkey.next[0]) - dfs(monkey.next[1])
    elif monkey.symbol == "/":
        monkey.number = dfs(monkey.next[0]) / dfs(monkey.next[1])
    elif monkey.symbol == "*":
        monkey.number = dfs(monkey.next[0]) * dfs(monkey.next[1])

    return monkey.number


print(dfs(start))