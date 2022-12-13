f = open("inputs/13.txt", "r")

lines = [x.strip() for x in f]

index = 1

ans = 0

# 1 = success
# 2 = do nothing
# 0 = fail
def compare(left, right):
    for j in range(len(left)):
        if j >= len(right):
            return 0
        if type(left[j]) == int and type(right[j]) == int:
            if left[j] < right[j]:
                return 1
            elif left[j] > right[j]:
                return 0
            else:
                continue

        else:
            if type(left[j]) == int:
                left[j] = [left[j]]
            if type(right[j]) == int:
                right[j] = [right[j]]

            temp = compare(left[j], right[j])
            if temp != 2:
                return temp
    if len(left) < len(right):
        return 1
    elif len(right) < len(left):
        return 0
    else:
        return 2


i = 0
while i < len(lines):
    left = eval(lines[i])
    right = eval(lines[i + 1])

    failed = False

    if compare(left, right) != 0:
        ans += index
    index += 1

    i += 3

print(ans)
