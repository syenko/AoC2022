f = open("../inputs/7.txt", "r")

lines = [x for x in f]

directories = {}

cwd = ""

for i in range(len(lines)):
    x = lines[i].strip()
    # cd command
    if x[0] == "$":
        print(f"cwd: {cwd}")
        print(f"x: {x}")
        chars = x.split(" ")

        if chars[1] == 'cd':
            if chars[2] == "..":
                cwd = ''.join(folder + ";" for folder in cwd.split(";")[:-2])
                continue
            else:
                cwd += chars[2] + ";" # add file path to end of current working directory
                i += 2
                if (cwd not in directories):
                    directories[cwd] = 0

                while i < len(lines) and lines[i][0] != "$":
                    if lines[i].split(" ")[0] == "dir":
                        i += 1
                        continue
                    else:
                        folders = cwd.split(";")[:-1]
                        build_dir = ""
                        for folder in folders:
                            build_dir += folder + ";"
                            directories[build_dir] += int(lines[i].split(" ")[0])
                    i += 1

print(directories)

totalAmt = directories["/;"] - (70000000 - 30000000)

ans = 70000000000
for (key, val) in directories.items():
    if (val > totalAmt):
        ans = min(ans, val)

print(ans)