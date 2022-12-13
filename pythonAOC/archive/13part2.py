import functools

f = open("inputs/13.txt", "r")

lines = [x.strip() for x in f]

index = 1

ans = 0


# -1 = right sort after
# 1 = left sort after
# 0 = tie
def compare(left, right):
    for i in range(len(left)):
        # left list has more items than right
        if i >= len(right):
            return -1

        # both are ints
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
            else:
                continue

        # at least one is a list
        else:
            temp = compare(
                [left[i]] if type(left[i]) == int else left[i],
                [right[i]] if type(right[i]) == int else right[i]
            )
            if temp != 0:
                return temp

    # entire list checked w/o problems
    if len(left) < len(right):
        return 1
    else:
        return 0

i = 0
packets = [[[2]], [[6]]]
# read in all the packets
while i < len(lines):
    left = eval(lines[i])
    right = eval(lines[i + 1])

    packets.append(left)
    packets.append(right)

    i += 3

# sort
packets.sort(key=functools.cmp_to_key(compare), reverse=True)

ans = 1
for (i, val) in enumerate(packets):
    if val == [[6]]:
        ans *= (i + 1)
    if val == [[2]]:
        ans *= (i + 1)

print(ans)
