import functools

f = open("inputs/13.txt", "r")

lines = [x.strip() for x in f]

index = 1

ans = 0

# -1 = right sort after
# 1 = left sort after
# 0 = tie
def largerCompare(left, right):
    for i in range(len(left)):
        if i >= len(right):
            return -1
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
            else:
                continue

        else:
            if type(left[i]) == int:
                left[i] = [left[i]]
            if type(right[i]) == int:
                right[i] = [right[i]]

            temp = largerCompare(left[i], right[i])
            if temp != 0:
                return temp

    if len(left) < len(right):
        return 1
    elif len(right) < len(left):
        return -1
    else:
        return 0


i = 0
packets = [[[2]], [[6]]]
while i < len(lines):
    left = eval(lines[i])
    right = eval(lines[i + 1])

    packets.append(left)
    packets.append(right)

    i += 3

def sortFunc(a, b):
    return -largerCompare(a, b)

sortPack = sorted(packets, key=functools.cmp_to_key(sortFunc))

ans = 1
for (i, val) in enumerate(sortPack):
    print(val)
    if val == [[[[6]]]]:
        ans *= (i + 1)
    if val == [[[[2]]]]:
        ans *= (i + 1)

print(ans)
